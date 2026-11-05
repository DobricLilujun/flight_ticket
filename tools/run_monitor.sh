#!/bin/bash
# Daily CES-2027 price monitor: scrape floors, append to results/price_track.md, commit + push.
set -u
REPO="/home/ubadmin/projects/flight_ticket"
LOG="/home/ubadmin/flight_monitor.log"
cd "$REPO" || exit 1
echo "=== run $(date -Is)" >> "$LOG"
python3 tools/monitor.py >> "$LOG" 2>&1
if [ -n "$(git status --porcelain -- results/price_track.md)" ]; then
  DROP=$(grep -o "Alerts this run:.*" results/price_track.md 2>/dev/null | tail -1)
  git add results/price_track.md
  git commit -q -m "price track $(date +%F): floors refreshed (Skyscanner+Kayak, live FX)${DROP:+ | }${DROP}"
  git push -q origin master && echo "pushed" >> "$LOG" || echo "push FAILED" >> "$LOG"
else
  echo "no change" >> "$LOG"
fi
