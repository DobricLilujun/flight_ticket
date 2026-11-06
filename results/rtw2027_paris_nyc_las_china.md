# 绕地球一周：巴黎 → 纽约 → 拉斯维加斯 → (湾区/洛杉矶) → 北京/上海 → 巴黎
**目标**：12 月底或 1 月初（**1 月 4 日之前**）从巴黎出发；中途在纽约停留；1 月中从美国飞中国（北京或上海）；**2 月 10 日前后**回巴黎；可多次中转；越便宜越好，**理想目标 €1000 以内**。
**数据日期：2026-11-06**（三站实时取价：Google Flights / Skyscanner / Kayak；£1 = €1.1982，FX 实时抓取）

---

## 0) 结论（先看这里）
| 方案 | 结构 | 最低价（三站地板组合） | 备注 |
|---|---|---|---|
| **C1 🥇 最便宜（拆票）** | 巴黎→纽约→拉斯维加斯→**上海**→巴黎 | **€1,252** | 极限拼价（French bee + 廉价境内段 + 自转联程） |
| C1b 同结构、**全程联程保障** | 同上，联程承运人（UA/ANA、JetBlue 直飞） | **€1,393** | 无自转风险，行李规则更稳 |
| C2 | 拉斯维加斯→**洛杉矶**→上海（Frontier €17-26 + CX） | €1,261–1,290 | 湾区/洛杉矶中转 |
| C3 | 洛杉矶→**北京**（CX/东航 €379-398）+ 北京→巴黎 €418 | €1,326–1,333 | 北京到达版 |
| C4 | 拉斯维加斯→**旧金山**→上海 | €1,267–1,296 | 湾区版 |
| C5 | **一张票多程（multi-city 单张预订）** | **€1,360–1,524** | 一张票最便宜 €1,360；比拆票贵 €108 |
**€1000 以内目前市场上不存在**（四段地板相加 €1,252）。差距 €250，需要 2–3 个特价同时出现（见 §6 触发价）。自动盯盘已上线（`tools/monitor.py` + cron，每天 8:15 / 20:15 自动 push 到本仓库 `results/price_track.md`）。

---

## 1) C1 最优组合（航班号 / 时刻 / 中转 / 价格）
| 段 | 日期 | 航班号 | 时刻 / 中转 | 三站价格 | 链接 |
|---|---|---|---|---|---|
| ① 巴黎→纽约 | **12/23（周三）** | **BF 720**（French bee，A350，**直飞**） | ORY 18:40 → EWR 21:00（8h20） | **Kayak €381** · Skyscanner €385 · Google €392 | https://www.kayak.co.uk/flights/PAR-NYC/2026-12-23 · https://www.skyscanner.net/transport/flights/PAR/NYC/261223/?adults=1&currency=GBP&locale=en-GB&market=UK |
| ② 纽约→拉斯维加斯 | **1/4（周一）** | **B6 711**（JetBlue，A320，**直飞**） | NYC 19:50 → LAS 22:48（2h58） | Kayak €129（当日最低价）· **Kayak 直飞行 £156 = €187** · Google €191 · Skyscanner（1/3）€188 | https://www.kayak.co.uk/flights/NYC-LAS/2027-01-04 · Google `Flights from NYC to LAS on 2027-01-04 one way` |
| ②′ 更便宜的 ② | **1/3（周日）** | **Frontier**（1 停） | 22:28 → 08:45+1 | Google €160 · Skyscanner(Kayak) €168 | https://www.kayak.co.uk/flights/NYC-LAS/2027-01-03 |
| ③ 拉斯维加斯→上海 | **1/12（周二）** | **AS 701 + AS 123 + GK 35**（Alaska + Jetstar Japan） | LAS 07:00 → SEA 09:50 → SEA 12:00 → NRT → NRT 22:20 → PVG 01:10+1（2 停，⚠️**自转/无联程保障**） | Google **€423** · Kayak €401–415 · Skyscanner €497 | https://www.kayak.co.uk/flights/LAS-PVG/2027-01-12 · https://www.skyscanner.net/transport/flights/LAS/PVG/270112/?adults=1&currency=GBP&locale=en-GB&market=UK |
| ③′ ③ 的**联程保障**版 | 1/12 | **UA（SkyWest）+ NH**（经 LAX，2 停） | LAS 10:30 → LAX → PVG 01:15+2 | Kayak €484–497 · Google €501（1/11） | 同上链接（选联程项） |
| ④ 上海→巴黎 | **2/10（周三）** | **GF 125 + GF 19**（Gulf Air，B787 + A321neo） | PVG 16:30/17:00 → BAH 22:40 → BAH 01:20 → CDG 06:45+1（1 停 2h40） | **Kayak €341** · Google €348 · Skyscanner €367（Etihad）/€344（GF 17:00） | https://www.kayak.co.uk/flights/PVG-PAR/2027-02-10 · https://www.skyscanner.net/transport/flights/PVG/CDG/270210/?adults=1&currency=GBP&locale=en-GB&market=UK |
| **合计** | | | | **€1,252（① Kayak + ② Kayak 最低 + ③ €401-423 + ④ €341）** ；保守全联程 **€1,393** | |

## 2) C2–C4 备选（"湾区/洛杉矶"版）
| 组合 | 明细 | 合计 |
|---|---|---|
| **C2（洛杉矶→上海）** | ① 381 + ② 129 + **Frontier LAS→LAX 06:55→08:13 €17-26** + **CX 883（LAX 11:05→HKG）+ CX 316（HKG→PVG 23:55）€392-411** + ④ 341 | **€1,261–1,290** |
| **C3（洛杉矶→北京）** | ① 381 + ② 129 + LAS→LAX €26 + **LAX→PEK €379-398**（Kayak £316；Skyscanner China Eastern 11:30→21:50 €382；Google Cathay 1 停 €398）+ **PEK→PAR 2/11 Cathay €418** | **€1,326–1,333** |
| **C4（旧金山→上海）** | ① 381 + ② 129 + **Frontier LAS→SFO 07:00→08:48 €22-24** + **SFO→PVG €399-430**（CZ 660 经武汉 + CZ 3823；Skyscanner £333 = €399）+ ④ 341 | **€1,267–1,296** |
| 直飞代价 | LAX→PVG **直飞** UA €524 / DL €525；SFO→PVG 直飞 UA857/MU590 在 1/12-14 未出现低价 | 直飞多花 €110-130 |

## 3) 每段日度网格（Google Flights 实时，EUR）
### ① 巴黎→纽约（单程，全部机场 PAR→NYC）
12/19 €508 · 12/20 €538 · 12/21 €490 · 12/22 €490 · **12/23 €392 🏆（French bee 直飞 BF 720）** · 12/26 €450 · 12/27 €469 · 12/28 €458（DL 直飞）· 12/29 €458 · 12/30 €466 · **12/31 €412**（BA+AA 2 停）· 1/1 €552 · 1/2 €810 · 1/3 €725 → **1 月出发完全不可取；12/23 或 12/31 是窗口内低点**（Kayak 更低：12/23 €381，12/28 €425）。
### ② 纽约→拉斯维加斯（单程）
12/27 €297 · 12/29 €209 · 12/30 €205 · **12/31 €152（Frontier 1 停）** · 1/2 €168 · 1/3 €160 · 1/4 €191（JetBlue 直飞）｜Kayak：1/3 €168、**1/4 €129**、直飞行 €187 → 结论：**12/31–1/4 在 €129-191 区间**，比跨年夜前后便宜 €100。
### ③ 美国→中国（单程，日度 + 门户）
| 出发地 | 1/12 | 1/13 | 1/14 | 1/15-20 | 备注 |
|---|---|---|---|---|---|
| **LAS→PVG** | **€423**（AS+GK 2 停自转）/ Kayak €401 | €490-491 | €467 | €505-568 | 1/12 是地板 |
| LAS→PEK | €435 | **€422**（AS+KE） | – | – | |
| **LAX→PVG** | €411 | **€411**（CX 经 HKG） | €411 | – | CX 883+CX 316 |
| **LAX→PEK** | – | **€398 🏆**（CX）/ Skyscanner 东航 €382 | – | – | 全窗口最低 ③ |
| SFO→PVG | €430（CZ） | €477 | €430 | – | |
| SFO→PEK | – | €435 | – | – | |
| SEA→PVG | – | €411 | – | – | |
| OAK→PVG | 无结果（无直飞/无低价） | | | | |
| 接驳（Frontier/United 直飞） | **LAS→LAX €17**（6:55→8:13）· **LAS→SFO €22**（7:00→8:48）· LAS→SEA 需联程 | | | | 境内段只要 €17-26，所以"从湾区/LA 走"完全可行 |
### ④ 中国→巴黎（单程，春节 2027-02-06 之后）
PVG→PAR：2/9 €376 · **2/10 €348 🏆**（GF 125+GF 19；Kayak €341）· 2/11 €376 · 2/12 €353 · 2/14-28 €345-353（2/21 €347）
PEK→PAR：2/10 €423 · 2/11 €418 · 2/12 €418 → **上海回巴黎比北京便宜 €70；2/10 已是低点，2/12 与 2/21 基本持平**

## 4) 门户替代测试（为什么不用别的城市出发去纽约）
Dec-23 出发：PAR→NYC €392 < **LHR→NYC €426**（+PAR→LON €57 = €483）< MAN→NYC €431（+PAR→MAN €26 = €457）< LGW €452 < DUB €518（+PAR→DUB €22 = €540）< EDI €561 < AMS €? （+PAR→AMS €72）→ **巴黎直飞 French bee 就是地板**，Norse/其他廉航在该窗口没有更低报价（Google 38-44 条结果中均未出现）。
巴黎→纽约 12/23 各承运人：BF 720 直飞 €381-392；AA 43（经 PHL）€400+；DL 267 直飞 €458。

## 5) 单张票（multi-city）网格 — Kayak 链式 URL
| 结构 | 价格 |
|---|---|
| PAR-NYC 12/23 · NYC-LAS 1/3 · **LAS-LAX 1/12 · LAX-PVG 1/13** · PVG-PAR 2/10 | **£1,135 = €1,360 🏆** |
| 同上但 LAS-SFO 1/12 · SFO-PVG 1/12 | €1,396 |
| PAR-NYC 12/23 · NYC-LAS 1/3 · **LAS-PVG 1/12** · PVG-PAR 2/10 | €1,476 |
| …LAS-PEK 1/13 · PEK-PAR 2/11 | €1,486 |
| …LAS-PVG 1/13（12/23 出发 / 12/31 出发 / 1/4 内飞 LAS） | €1,495-1,500 |
| PAR-NYC 12/28 · NYC-LAS 12/31 · LAS-PVG 1/12 · PVG-PAR 2/10 | €1,524 |
| 仅前两段一张票（PAR-NYC + NYC-LAS，含 12 天停留） | **€572-573**（vs 拆票 €510；若要多段联程保障，这 €572 只贵 €62 但省一次自转） |
| 6 段（再绕 SEA） | €1,631 |
**结论：拆票 €1,252 < 单张多程 €1,360**。若你要"一张票更省心"，选 €1,360 那条（经洛杉矶）。

## 6) 怎么打到 €1000（触发价 + 盯盘）
四段地板 381 + 129 + 401 + 341 = €1,252。要 ≤€1000，需要同时满足下面 2-3 项（历史波动证明都可能发生：都柏林 CES 往返 24h 内 −£21，12 月底 CDG-LAS 曾 −£151/日）：
| 段 | 当前地板 | 触发价（报警） | 触发后合计 |
|---|---|---|---|
| ① Paris→NYC 12/23（French bee/Norse 闪促） | €381 | **≤ €250** | −131 |
| ② NYC→LAS 1/4（Frontier/Spirit 促销） | €129 | ≤ €90 | −39 |
| ③ 美→华 1/12-13（东航/国航 LAX→PVG/PEK 直飞特价） | €379-423 | **≤ €330** | −70 |
| ④ PVG→PAR 2/10（GF/东航促销） | €341 | **≤ €290** | −51 |
三项同时命中 → **€990**。`tools/monitor.py` 已加入这四段固定行程每日两次抓价，任一段下降 ≥€15 会在 `results/price_track.md` 写 DROP 行并 push；命中触发价时直接按 §1 链接下单（先买 ④，最稳；再 ①；最后 ②③）。

## 7) 行李 / 风险（下单前必看）
| 段 | 舱位 | 托运 | 风险 |
|---|---|---|---|
| ① French bee BF 720 | 基础经济 | 23kg 约 €30-45（线上预付）；手提 1 件免费 | 单人航司，A350 湿租，时刻可能调整 |
| ② JetBlue B6 711 | 经济 | **首件免费** | 无 |
| ②′ Frontier | ULCC | 每件 $50-65 | 延误不保护 |
| ③ AS+GK（Jetstar Japan） | ULCC 组合 | 每件 ¥2,000-3,000 ≈ €15-20 | **SEA、NRT 两次自转**：建议只买 ③′ 联程（€484-497）或在 SEA 过夜 |
| ③′/C2/C4 联程（UA-NH / CX / CZ） | 经济 | 23kg ×1 免费（CX/CZ）| 无自转 |
| ④ Gulf Air GF 125/19 | 经济 | **20-30kg 免费** | 无 |
含 1 件托运的真实到手：拆票 ≈ **€1,330-1,380**；全联程拆票 ≈ €1,430；单张多程 €1,360（Basic 舱无托运，加钱后接近 €1,500）。
**如果只买一张联程最省心**：€1,360（经洛杉矶）→ 平均"每段含保障"最划算。

## 8) 预订链接（全部实时可用，2026-11-06）
- ①：https://www.kayak.co.uk/flights/PAR-NYC/2026-12-23 · https://www.frenchbee.com （BF 720 官网直购更稳）
- ②：https://www.kayak.co.uk/flights/NYC-LAS/2027-01-04 · https://www.skyscanner.net/transport/flights/NYC/LAS/270104/?adults=1&currency=GBP&locale=en-GB&market=UK
- ③：https://www.kayak.co.uk/flights/LAS-PVG/2027-01-12 · https://www.kayak.co.uk/flights/LAX-PEK/2027-01-13 · https://www.kayak.co.uk/flights/LAX-PVG/2027-01-13
- ④：https://www.kayak.co.uk/flights/PVG-PAR/2027-02-10 · https://www.skyscanner.net/transport/flights/PVG/CDG/270210/?adults=1&currency=GBP&locale=en-GB&market=UK
- 单张多程：https://www.kayak.co.uk/flights/PAR-NYC/2026-12-23/NYC-LAS/2027-01-03/LAS-LAX/2027-01-12/LAX-PVG/2027-01-13/PVG-PAR/2027-02-10/?sort=flight_price
- 前两段单张：https://www.kayak.co.uk/flights/PAR-NYC/2026-12-23/NYC-LAS/2027-01-04/?sort=flight_price
- Google Flights（含航班号明细）：`Flights from PAR to NYC on 2026-12-23 one way` / `Flights from NYC to LAS on 2027-01-04 one way` / `Flights from LAS to PVG on 2027-01-12 one way` / `Flights from PVG to PAR on 2027-02-10 one way`（curr=EUR）
