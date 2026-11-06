#!/usr/bin/env python3
"""CES 2027 price monitor — appends a dated floor-price row to results/price_track.md.

Probes (live, cross-site):
  Skyscanner (Scrapling/StealthyFetcher) : leg1 CDG->LAS 261231, leg2 LAS->PVG 270112,
      leg3 PVG->CDG 270210, RT CDG-LAS 261231/270113, RT DUB-LAS 261228/270111,
      RT PAR-PVG 270114/270210
  Kayak      (Scrapling/StealthyFetcher) : same set + single-ticket multi-city chain

Derived numbers: RTW split total, two-RT bundle total, single-ticket RTW price.
FX: GBP->EUR is fetched live (frankfurter.app) and falls back to 1.1982.
Exit code is 0 even when individual probes fail (missing cells are written as "-").
"""
import json
import re
import subprocess
import sys
import time
from datetime import date
from pathlib import Path

GBP = "\u00a3"
FX_FALLBACK = 1.1982
REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "results" / "price_track.md"

# canonical itineraries (do not change: rows must stay comparable across days)
SKY_ONEWAYS = [("CDG", "LAS", "261231"), ("LAS", "PVG", "270112"), ("PVG", "CDG", "270210")]
SKY_RTS = [("CDG", "LAS", "261231/270113"), ("DUB", "LAS", "261228/270111"), ("PAR", "PVG", "270114/270210")]
KAY_ONEWAYS = [("CDG-LAS", "2026-12-31"), ("LAS-PVG", "2027-01-12"), ("PVG-CDG", "2027-02-10"),
               ("LAS-SFO", "2027-01-12"), ("SFO-PVG", "2027-01-12")]
KAY_RTS = [("CDG-LAS", "2026-12-31/2027-01-13"), ("DUB-LAS", "2026-12-28/2027-01-11"),
           ("PAR-PVG", "2027-01-14/2027-02-10")]
KAY_MULTI = [("RTW_direct", "CDG-LAS/2026-12-31/LAS-PVG/2027-01-12/PVG-CDG/2027-02-10"),
             ("RTW_bayarea", "CDG-LAS/2026-12-31/LAS-SFO/2027-01-12/SFO-PVG/2027-01-12/PVG-CDG/2027-02-10")]

# --- structure B (2026-11-06 re-audited): RTW via New York, cheapest protected structure
# R1: PAR->NYC 12/24 (BF 720) -> LAS 12/31 (F9) -> LAX 1/12 (F9) -> PVG 1/12 (3U3838+3U5252) -> PAR 2/10 (GF)
SKY_B = [("PAR", "NYC", "261224"), ("NYC", "LAS", "261231"), ("LAS", "LAX", "270112"),
         ("LAX", "PVG", "270112"), ("LAX", "PEK", "270112"), ("PVG", "PAR", "270210")]
KAY_B = [("PAR-NYC", "2026-12-24"), ("NYC-LAS", "2026-12-31"), ("LAS-LAX", "2027-01-12"),
         ("LAX-PVG", "2027-01-12"), ("LAX-PEK", "2027-01-12"), ("PVG-PAR", "2027-02-10")]
KAY_MULTI_B = [("RTW_NYC_lax", "PAR-NYC/2026-12-24/NYC-LAS/2026-12-31/LAS-LAX/2027-01-12/LAX-PVG/2027-01-12/PVG-PAR/2027-02-10")]
# buy triggers (EUR) for the sub-EUR1000 round-the-world goal (floor 340+149+17+361+328 = 1195)
TRIGGERS = {"sk.PAR-NYC.261224": 250, "sk.NYC-LAS.261231": 110,
            "sk.LAX-PVG.270112": 300, "sk.LAX-PEK.270112": 300, "sk.PVG-PAR.270210": 290}


def log(msg: str) -> None:
    print(msg, flush=True)


def fx_rate() -> float:
    try:
        out = subprocess.run(["curl", "-s", "--max-time", "20",
                              "https://api.frankfurter.app/latest?from=GBP&to=EUR"],
                             capture_output=True, text=True, timeout=30).stdout
        return float(json.loads(out)["rates"]["EUR"])
    except Exception as exc:  # noqa: BLE001
        log(f"fx fallback ({exc})")
        return FX_FALLBACK


def fetch(url: str, tries: int = 3) -> str:
    from scrapling.fetchers import StealthyFetcher
    last = ""
    for attempt in range(tries):
        try:
            page = StealthyFetcher.fetch(url, headless=True, humanize=True,
                                         solve_cloudflare=True, network_idle=True, timeout=90000)
            return " ".join(page.get_all_text(ignore_tags=("script", "style")).split())
        except Exception as exc:  # noqa: BLE001
            last = str(exc)[:80]
            time.sleep(15)
    log(f"  ! fetch failed {url} :: {last}")
    return ""


def to_int(raw: str) -> int:
    return int(raw.replace(",", ""))


def kayak_price(text: str):
    if not text:
        return None
    m = re.search(r"Cheapest " + GBP + r"([\d,]+)", text)
    if m:
        return to_int(m.group(1))
    vals = [to_int(x) for x in re.findall(GBP + r"([\d,]+)", text) if to_int(x) > 100]
    return min(vals) if vals else None


def sk_price(text: str):
    if not text:
        return None
    best = None
    for chunk in re.split(r"Flight option \d+:", text)[1:]:
        m = re.search(GBP + r"([\d,]+)", chunk)
        if not m:
            continue
        c = to_int(m.group(1))
        if best is None or c < best:
            best = c
    return best


def main() -> int:
    fx = fx_rate()
    log(f"GBP->EUR = {fx}")
    cells = {}

    for o, d, dt in SKY_ONEWAYS + SKY_RTS + SKY_B:
        v = sk_price(fetch(f"https://www.skyscanner.net/transport/flights/{o}/{d}/{dt}/"
                           f"?adults=1&currency=GBP&locale=en-GB&market=UK"))
        cells[f"sk.{o}-{d}.{dt}"] = v
        log(f"  sk {o}-{d} {dt} = GBP{v}")

    for rt, dt in KAY_ONEWAYS + KAY_RTS + KAY_B:
        v = kayak_price(fetch(f"https://www.kayak.co.uk/flights/{rt}/{dt}?sort=flight_price"))
        cells[f"ky.{rt}.{dt}"] = v
        log(f"  ky {rt} {dt} = GBP{v}")

    for tag, path in KAY_MULTI + KAY_MULTI_B:
        v = kayak_price(fetch(f"https://www.kayak.co.uk/flights/{path}/?sort=flight_price"))
        cells[f"mc.{tag}"] = v
        log(f"  mc {tag} = GBP{v}")

    def eur(key):
        v = cells.get(key)
        return round(v * fx) if v else None

    legs = [eur("sk.CDG-LAS.261231"), eur("sk.LAS-PVG.270112"), eur("sk.PVG-CDG.270210")]
    rtw_split_sk = sum(x for x in legs if x) if all(legs) else None
    kl = [eur("ky.CDG-LAS.2026-12-31"), eur("ky.LAS-PVG.2027-01-12"), eur("ky.PVG-CDG.2027-02-10")]
    rtw_split_ky = sum(x for x in kl if x) if all(kl) else None
    bay_ky = ([eur("ky.CDG-LAS.2026-12-31"), eur("ky.LAS-SFO.2027-01-12"),
               eur("ky.SFO-PVG.2027-01-12"), eur("ky.PVG-CDG.2027-02-10")])
    bay_total = sum(x for x in bay_ky if x) if all(bay_ky) else None
    bundle_sk = ([x for x in (eur("sk.CDG-LAS.261231/270113"), eur("sk.PAR-PVG.270114/270210"))])
    bundle_sk = sum(bundle_sk) if len(bundle_sk) == 2 else None
    bundle_ky = ([x for x in (eur("ky.CDG-LAS.2026-12-31/2027-01-13"), eur("ky.PAR-PVG.2027-01-14/2027-02-10"))])
    bundle_ky = sum(bundle_ky) if len(bundle_ky) == 2 else None

    def s(v):
        return f"EUR{v}" if v else "-"

    row = (f"| {date.today().isoformat()} | fx {fx:.4f} | {s(eur('sk.CDG-LAS.261231'))} | "
           f"{s(eur('sk.LAS-PVG.270112'))} | {s(eur('sk.PVG-CDG.270210'))} | "
           f"{s(rtw_split_sk)} | {s(rtw_split_ky)} | {s(bay_total)} | "
           f"{s(eur('sk.CDG-LAS.261231/270113'))} | {s(eur('sk.DUB-LAS.261228/270111'))} | "
           f"{s(eur('sk.PAR-PVG.270114/270210'))} | {s(bundle_sk)} | {s(bundle_ky)} | "
           f"{s(eur('mc.RTW_direct'))} | {s(eur('mc.RTW_bayarea'))} |")

    header = ("| Date | FX | leg1 CDG→LAS 12/31 | leg2 LAS→PVG 1/12 | leg3 PVG→CDG 2/10 | "
              "RTW split (Skyscanner) | RTW split (Kayak) | RTW Bay Area (Kayak) | "
              "CES RT CDG 12/31→1/13 | CES RT DUB 12/28→1/11 | China RT PAR⇄PVG 1/14→2/10 | "
              "bundle (Skyscanner) | bundle (Kayak) | single-ticket RTW direct | single-ticket RTW Bay Area |")

    # ---- structure B derived rows ----
    def bmin(*keys):
        vals = [eur(k) for k in keys if eur(k)]
        return min(vals) if vals else None

    rtwB_1 = bmin("sk.PAR-NYC.261224", "ky.PAR-NYC.2026-12-24")
    rtwB_2 = bmin("sk.NYC-LAS.261231", "ky.NYC-LAS.2026-12-31")
    rtwB_3a = bmin("sk.LAS-LAX.270112", "ky.LAS-LAX.2027-01-12")
    rtwB_3b = bmin("sk.LAX-PVG.270112", "ky.LAX-PVG.2027-01-12")
    rtwB_4 = bmin("sk.PVG-PAR.270210", "ky.PVG-PAR.2027-02-10")
    legs4 = [rtwB_1, rtwB_2, rtwB_3b, rtwB_4]
    rtwB_split = sum(x for x in legs4 if x) if all(legs4) else None
    legs5 = legs4 + [rtwB_3a]
    rtwB_full = sum(x for x in legs5 if x) if all(legs5) else None
    rowB = (f"| {date.today().isoformat()} | fx {fx:.4f} | {s(rtwB_1)} | {s(rtwB_2)} | {s(rtwB_3a)} | "
            f"{s(rtwB_3b)} | {s(rtwB_4)} | {s(rtwB_split)} | {s(rtwB_full)} | "
            f"{s(eur('mc.RTW_NYC_lax'))} |")
    headerB = ("| Date | FX | ① PAR→NYC 12/24 | ② NYC→LAS 12/31 | ③a LAS→LAX 1/12 | ③b LAX→PVG 1/12 (3U) | "
               "④ PVG→PAR 2/10 | split 4 legs | split 5 legs (= total) | single ticket multi-city |")

    prev_rows, prev_rowsB = [], []
    if OUT.exists():
        for line in OUT.read_text().splitlines():
            m = re.match(r"^\| (\d{4}-\d{2}-\d{2}) \|", line)
            if not m:
                continue
            (prev_rowsB if line.count("|") == 11 else prev_rows).append(line)

    notes = []
    for key, trig in TRIGGERS.items():
        v = eur(key)
        if v and v <= trig:
            notes.append(f"TRIGGER {key} EUR{v} <= {trig}")
    if prev_rows:
        prev = prev_rows[-1]
        def nums(line):
            return [int(x) for x in re.findall(r"EUR(\d+)", line)]
        a, b = nums(prev), nums(row)
        if len(a) == len(b):
            for new, old in zip(b, a):
                if old - new >= 15:
                    notes.append(f"DROP {old} → {new}")

    OUT.write_text(
        "# CES 2027 price track (automated)\n\n"
        "Generated by `tools/monitor.py` (Skyscanner + Kayak live floors, EUR via live GBP/EUR FX).\n"
        "Itineraries are fixed so rows are comparable day to day. Run daily via cron "
        "(`tools/run_monitor.sh` commits and pushes).\n"
        "⚠️ Values are the cheapest *listed* price; Kayak/Skyscanner sometimes list 'self-transfer hack'"
        " combos (unprotected, 28-36 h). Always read the itinerary before buying — see "
        "`rtw2027_paris_nyc_las_china.md` §0/§1 for the protected picks.\n\n"
        "### Structure A — CES round trip + China round trip (EUR600 target)\n\n"
        + header + "\n|---|---|" + "---|" * 14 + "\n"
        + "\n".join(prev_rows[-30:] + [row]) + "\n\n"
        "### Structure B — round the world PAR→NYC→LAS→(LAX)→PVG/PEK→PAR (EUR1000 target)\n\n"
        + headerB + "\n|---|---|" + "---|" * 8 + "\n"
        + "\n".join(prev_rowsB[-15:] + [rowB]) + "\n"
        + (("\n**Alerts this run:** " + "; ".join(notes) + "\n") if notes else "")
    )
    log(f"wrote {OUT}")
    if notes:
        log("ALERT: " + "; ".join(notes))
    return 0


if __name__ == "__main__":
    sys.exit(main())
