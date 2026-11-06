# 绕地球一周：巴黎 → 纽约 → 拉斯维加斯 →（洛杉矶/湾区）→ 上海/北京 → 巴黎
**要求**：12 月底或 1 月初（**1 月 4 日之前**）从巴黎出发 · 巴黎→纽约 · 纽约→拉斯维加斯 · 从维加斯附近城市或湾区/洛杉矶城市飞中国（北京或上海）· **2 月 10 日前后**回巴黎 · 可多次中转 · 越便宜越好，希望 €1000 以内。
**核价日期：2026-11-06（第三轮全量复核）**：Google Flights（curr=EUR, gl=fr）+ Skyscanner + Kayak 三站实时取价；£1 = €1.1982（Frankfurter 实时汇率）。所有价格都是"单程"报价，拆票=分开下单。

---

## 0) 结论（先看这里）
| # | 方案 | 明细 | 价格 | 保障 |
|---|---|---|---|---|
| **R1 🥇** | **4 张单程拆票（每段都是正常票）** | ① BF 720 直飞 12/24 · ② Frontier 1 停 12/31 · ③ Frontier LAS→LAX 1/12 **+** 四川航空 3U 3838 + 3U 5252（LAX→天府→浦东）1/12 · ④ Gulf Air GF 125 + GF 19 2/10 | **€1,195**（三站最低价拼合）<br>**€1,289**（Google 同结构价） | ✅ 每段单独出票、联程段内部有保障；只有 ③a→③b 之间需自提行李重值机（LAX 隔 13h，可接受） |
| **R2 🥈** | **一张票多程（Kayak multi-city，非 hack）** | 同一预订：PAR-NYC 12/24 · NYC-LAS 12/31 · LAS-LAX 1/12 · LAX-PVG 1/12 · PVG-PAR 2/10 | **€1,262**（£1,053） | ✅ 一次预订、一家负责；比拆票贵 €67，比 R1 的 Google 价便宜 €27 |
| R3 | 北京到达版（拆票） | ① 340 + ② 149 + ③a 17 + **3U 3838 + 3U 天府→北京 1/12 €365** + **PEK→PAR 2/11 CX €418** | **€1,289** | ✅ 比上海版贵 €94（北京回程贵） |
| R4 | 不进洛杉矶、直接从维加斯飞中国 | ① 340 + ② 149 + **UA/ANA 联程 LAS→PVG €484-575** + ④ 328 | **€1,301–1,392** | ✅ 全联程，最省心（只 3 张票） |
| R5 | 极限 hack 价（**不建议**） | Kayak "Self-transfer hack"：② 28h19（€138）+ ③ Frontier+川航经天府 35h35（€401） | €1,215–1,252 | ❌ 自转不保障；同结构正常价只贵几十欧，没必要买 |

**关于 €1000：市场上现在没有 ≤€1000 的完整组合。** 全段正常票地板 **€1,195**，离 €1000 差 **€195**；四个触发价里有 3 个同时命中才 ≈€1,006，4 个全命中 ≈€967（见 §6）。自动盯盘已上线并包含本结构：`tools/monitor.py` + cron（每天 8:15 / 20:15 自动抓价、降价 ≥€15 写 DROP 行并 push 到 `results/price_track.md`）。

⚠️ **本轮审计更正**（前两轮结论已作废）：
1. Kayak 的 NYC→LAS 1/4「£115/€138」与 LAS→PVG 1/12「£335/€401」是 **Self-transfer hack**（28h19 / 35h35，自转不保障），不能当正常票买；本轮已换成正常票口径。
2. **① 的最低点不是 12/23 而是 12/24**：French bee ORY→EWR 直飞 12/24 = Kayak €340 / Skyscanner €346 / Google €352（12/23 €381-392，12/25 €388，12/26 €459）。
3. **② 的最低点是 12/31**（12/31 Frontier 经 DFW = Google €152 / Kayak €149），比 1/3-1/4 便宜 €10-40；跨年夜在维加斯过夜反而省钱。
4. **③ 的真正地板是四川航空 3U 3838（LAX→天府 TFU→浦东/北京）**：1/12 = Kayak €361 / Skyscanner €364，比国泰低 €50、比 LAS 直联程低 €120+。Google 不销售 3U，所以只能从 Kayak/Skyscanner/OTA 或 3U 官网下单。
5. 上一轮写的"单张多程最便宜 €1,360"那条其实是 hack 组合（末段落 **博韦 BVA**，离巴黎 80km，维也纳自转）；本轮 12/24 版非 hack 单张多程 = **€1,262**。

---

## 1) R1 最优组合：航班号 / 时刻 / 中转 / 三站比价
| 段 | 日期 | 航班号（机型） | 时刻 / 中转 | 三站价格 | 查价链接 |
|---|---|---|---|---|---|
| **① 巴黎→纽约** | **2026-12-24（四）** | **BF 720**（French bee，A350-900） | ORY 奥利 18:40 → EWR 纽瓦克 21:00，**直飞** 8h20 | **Kayak €340** · Skyscanner €346 · Google €352 | https://www.kayak.co.uk/flights/PAR-NYC/2026-12-24 · https://www.skyscanner.net/transport/flights/PAR/NYC/261224/?adults=1&currency=GBP&locale=en-GB&market=UK · https://www.frenchbee.com |
| **② 纽约→拉斯维加斯** | **2026-12-31（四）** | **F9（Frontier）** 2 段，经 DFW | LGA/EWR 20:30 → DFW 达拉斯（中转 7h50）→ LAS 08:38+1（1/1 到） | **Google €152** · **Kayak €149** · Skyscanner €189（JetBlue） | https://www.kayak.co.uk/flights/NYC-LAS/2026-12-31 · Google `Flights from NYC to LAS on 2026-12-31 one way` |
| **③a 维加斯→洛杉矶** | **2027-01-12（二）** | **F9（Frontier）直飞** | LAS 06:55 → LAX 08:13（1h18） | **Skyscanner €17** · Google €17 · Kayak €18-26 | https://www.skyscanner.net/transport/flights/LAS/LAX/270112/?adults=1&currency=GBP&locale=en-GB&market=UK |
| **③b 洛杉矶→上海** | **2027-01-12（二）** | **3U 3838**（川航 A350-900，周二/五/日）**+ 3U 5252**（=MU 5404 共享） | LAX 21:30 → TFU 天府 05:50+2（中转 2h10）→ PVG 浦东 10:25/10:30+2（1/14 到） | **Kayak €361** · **Skyscanner €364**（Google 不售 3U，Google 最便宜是国泰 €411） | https://www.kayak.co.uk/flights/LAX-PVG/2027-01-12 · https://www.skyscanner.net/transport/flights/LAX/PVG/270112/?adults=1&currency=GBP&locale=en-GB&market=UK |
| **④ 上海→巴黎** | **2027-02-10（三）** | **GF 125 + GF 19**（Gulf Air，A320neo/B787） | PVG 16:30 → BAH 巴林（中转 2h40）→ CDG 戴高乐 06:45+1 | **Kayak €328** · Google €348（CX 备选 €376） | https://www.kayak.co.uk/flights/PVG-PAR/2027-02-10 · https://www.skyscanner.net/transport/flights/PVG/CDG/270210/?adults=1&currency=GBP&locale=en-GB&market=UK |
| **合计** | 巴黎 12/24 走 → 纽约 7 晚 → 维加斯 12 晚（含跨年）→ 上海 4 周 → 巴黎 2/11 早 | | | **340+149+17+361+328 = €1,195**（Google 口径 352+152+26+411+348 = €1,289） | |

**停留结构**：纽约 12/24→12/31（7 晚）· 拉斯维加斯 12/31→1/12（12 晚，跨年夜在维加斯）· 上海 1/14→2/10（27 晚）。若想把纽约缩短：① 12/30 €466 + ② 12/31 €149 也行，总价 €1,321；若想去掉 LA 中转：见 R4。

---

## 2) 备选结构
| 组合 | 明细（① €340 + ② €149 固定） | 合计 |
|---|---|---|
| **R2 单张多程 🥈** | Kayak 多程：PAR-NYC 12/24 · NYC-LAS 12/31 · LAS-LAX 1/12 · LAX-PVG 1/12 · PVG-PAR 2/10 | **£1,053 = €1,262**（该搜索"Best"档 €1,444；hack 档不再列出） |
| **R3 北京到达** | ③a €17 + **3U 3838 + 天府→PEK（1/12，21:30→14:10+2）€364-365** + **PEK→PAR 2/11 CX 1 停 €418** | **€1,289** |
| **R4 全程从 LAS 飞** | **UA 10:30→LAX(0h46)→PVG 18:55+1 €567 Basic** / **UA+ANA 2 停 €484** / **AC+NH 经 YVR €575** | **€1,301–1,392** |
| **走湾区（SFO）** | **Frontier LAS→SFO 07:00→08:48 €22-24** + **SFO→PVG 1/12 CZ 经武汉 €399** 或 **1/13 CX 经 HKG €453** + ④ €328 | **€1,240–1,294**（比 LA 版略贵，因为 SFO→中国地板更高） |
| **LAS→PEK 直连（不落地 LA）** | AS+KE 1/13 €422 | €1,336（回程 PEK→PAR 2/11 €418） |
| 直飞的代价 | LAX→PVG 直飞 UA €524 / DL €525；SFO→PVG 直飞 UA857/MU590 该窗口无低价 | 多花 €110-160 |

---

## 3) 每段日度网格（实时，EUR）
### ① 巴黎→纽约（Google 全机场口径 / Kayak 补低价）
12/19 €508 · 12/20 €538 · 12/21 €490 · 12/22 €490 · 12/23 €381(Kayak)/€392(Google) · **12/24 €340 🏆（BF 720 直飞）** · 12/25 €388 · 12/26 €459 · 12/27 €469 · 12/28 €425-458 · 12/29 €458 · 12/30 €466 · 12/31 €412 · 1/1 €552 · 1/2 €810 · 1/3 €725
→ **12/24 是窗口内绝对低点；1 月出发完全不可取（€550-810）**，所以"1 月 4 日之前"实际只有 12 月可用。
### ② 纽约→拉斯维加斯
12/27 €297 · 12/29 €209 · **12/30 €183**（Frontier 经 DTW 17:30→09:16+1）· **12/31 €149-152 🏆**（Frontier 经 DFW 7h50）· 1/2 €168 · 1/3 €160-168（Frontier 经 ATL 22:28→08:45+1）· 1/4 €187-191（**JetBlue B6 711 直飞 JFK 19:50→22:48，首件托运免费**）
→ 12/31 最便宜；想要直飞+行李，1/4 的 B6 711 €187 是最省心的选择。
### ③ 美国→中国（Kayak 非 hack 地板 / Google 交叉验证）
| 航线 | 1/10 | 1/11 | **1/12** | 1/13 | 1/14 | 1/16 |
|---|---|---|---|---|---|---|
| **LAX→PVG** | 3U €401 | ANA €403 | **3U 3838+5252 €361 🏆**（Skyscanner €364） | CX €392（CX 883+CX 316） | CX €392 | CZ 经 CAN €434 |
| **LAX→PEK** | – | – | **3U €365 🏆** | – | CX €379 | – |
| LAS→PVG（联程，不拆 LA） | €568 | €501 | **UA+ANA €484 / UA €567 / AC+NH €575** | €490-491 | €467 | – |
| LAS→PEK | – | – | €435 | **€422**（AS+KE） | – | – |
| SFO→PVG | – | – | CZ 经武汉 €399 | CX €453 | €430 | – |
| SEA→PVG | – | – | – | €411 | – | – |
| OAK→PVG | 无低价结果（无直飞） | | | | | |
| **境内接驳（关键）** | **LAS→LAX Frontier €17-26**（06:55→08:13）· **LAS→SFO Frontier €22-24**（07:00→08:48）· LAS→SEA 需联程 | | | | | |
→ 结论：**"维加斯附近的城市"就是洛杉矶**（€17 接驳 + €361 跨太平洋），比直接从维加斯飞便宜 €100+。
### ④ 中国→巴黎（2 月 10 日前后）
| 航线 | 2/9 | **2/10** | 2/11 | 2/12 |
|---|---|---|---|---|
| **PVG→PAR** | €361 | **GF 125+GF 19 €328 🏆**（Kayak；Google €348） | €341 | €341-353 |
| PEK→PAR | – | – | **CX 1 停 €418** | €423 |
| PVG→CDG 直飞（MU/AF） | – | €520+ | – | – |

---

## 4) 单张多程（multi-city）网格 — Kayak 链式 URL
| 结构 | 正常票最低价 | hack 价（不保障，仅记录） |
|---|---|---|
| **PAR-NYC 12/24 · NYC-LAS 12/31 · LAS-LAX 1/12 · LAX-PVG 1/12 · PVG-PAR 2/10** | **£1,053 = €1,262 🏆** | – |
| PAR-NYC 12/24 · NYC-LAS 12/31 · LAS-PVG 1/12 · PVG-PAR 2/10 | €1,414 | – |
| PAR-NYC 12/24 · NYC-LAS 12/31 · LAS-LAX 1/12 · LAX-PEK 1/12 · PEK-PAR 2/11 | **€1,372-1,378** | – |
| PAR-NYC 12/23 · NYC-LAS 1/3 · LAS-LAX 1/12 · LAX-PVG 1/13 · PVG-PAR 2/10 | €1,414 | €1,360（末段落 BVA + 维也纳自转） |
| 同结构走 SFO | €1,444 | €1,396 |
| 其他 7 组（12/26、12/28、12/30、12/31 出发；PVG/PEK；SEA 绕飞） | €1,444–1,806 | €1,396–1,701 |
| 只前两段一张票（PAR-NYC 12/24 + NYC-LAS 12/31） | €573（=拆票 €489 + €84，不如拆） | – |
**结论：拆票 €1,195 < 单张多程 €1,262**；要"一次预订、一家负责"就买 €1,262 那条（选非 hack 项）。

---

## 5) Google Flights 交叉验证（curr=EUR, gl=fr，2026-11-06）
| 段 | Google 最低 | 航班 |
|---|---|---|
| PAR→NYC 12/24 | €352 | BF 720 直飞 ORY 18:40 → EWR 21:00（French bee） |
| NYC→LAS 12/31 | €152 | Frontier 1 停，DFW 中转 7h50，20:30 → 08:38+1 |
| LAX→PVG 1/12 | €411 | CX 883 + CX 316，HKG 中转 2h10，11:05 → 23:55（Google 不售 3U €361） |
| PVG→PAR 2/10 | €348 | GF 125 + GF 19，BAH 中转 2h40，16:30 → 06:45+1 |
→ Google 与 Kayak/Skyscanner 的差异都在 €10-50 之间，**没有"幽灵票价"**；3U 那条 Google 不销售，需在 Kayak/Skyscanner/OTA 或川航官网下单。

---

## 6) 怎么打到 €1000（触发价 + 盯盘）
四段（+接驳）正常地板 **340 + 149 + 17 + 361 + 328 = €1,195**，缺口 **€195**。历史上单日就能跌 €100+（12 月底 CDG-LAS 曾 −£151/日，都柏林 CES 往返 24h 内 −£21），所以要同时命中下面 2-3 项：
| 段 | 当前地板 | 触发价（报警） | 命中后合计 |
|---|---|---|---|
| ① Paris→NYC 12/24（French bee / Norse 闪促） | €340 | **≤ €250** | −90 → €1,105 |
| ③b 洛杉矶→上海/北京（3U 3838 或东航直飞 1/12） | €361 | **≤ €300** | −61 → €1,134（与 ① 同时 → €1,044） |
| ④ PVG→PAR 2/10（GF / 东航促销） | €328 | **≤ €290** | −38 → 三项同时 **≈ €1,006** |
| ② NYC→LAS 12/31（Frontier / JetBlue 促销） | €149 | **≤ €110** | −39 → 四项全中 **≈ €967 ✅** |
| ③a LAS→LAX 1/12 | €17 | ≤ €25（已很低，忽略） | – |
**为什么 ① 很难再跌**：Norse Atlantic 已把纽约航线（CDG-JFK、LGW/FCO-JFK）从 2026-27 冬季时刻表里删除（10 月 25 日后不再飞纽约，只保 LGW-MCO），所以巴黎→纽约的廉价直飞基本只剩 **French bee**。它的往返价地板在 €447-449、单程报价通 $333（≈€315）一带，所以 €340 已接近地板，想跌到 €250 只能等闪促（参考：https://www.kayak.com/flight-routes/Paris-Orly-ORY/New-York-Newark-EWR ）。
盯盘现状：`tools/monitor.py` 已把这四段 + 单张多程链加入每日两次抓取（cron `15 8,20 * * *` → `tools/run_monitor.sh`，自动 commit+push）；任一段比上次下降 ≥€15 会在 `results/price_track.md` 写 `DROP` 行；命中触发价会写 `TRIGGER` 行。**下单顺序建议：先 ④（回程最稳、波动最大先锁），再 ①，然后 ③b，最后 ③a/②（美国境内段临近出发才降价）。**

---

## 7) 行李 / 风险（下单前必看）
| 段 | 舱位 | 托运 | 风险 |
|---|---|---|---|
| ① French bee BF 720 | 基础经济 | 23kg 需加购 €30-45（线上预付更便宜）；手提 1 件免费 | 单一航司、A350 湿租，时刻可能微调；建议官网直购 |
| ② Frontier（经 DFW 7h50） | ULCC | 每件 $50-65 ≈ €45-60 | **中转 7h50 不保障**：延误就误第二天航班；建议买 Frontier 同日备选或改 JetBlue 直飞 €187 |
| ③a Frontier LAS→LAX | ULCC | $50-65 | 早班 06:55，前晚住维加斯即可 |
| ③b 3U 3838 + 3U 5252 | 经济（国际段） | **通常含 23kg×1**（下单时确认）；天府中转 2h10 同航司，行李直挂 | 3U 在 TFU 中转需过检但行李直挂；护照/签证：中国护照回国无问题，美国境内段需 ESTA/签证 |
| ③a→③b 之间（LAX） | 自提重值机 | 中间 13h，可出机场 | **不同票**：建议 ③a 买可改签或留足缓冲（已在 LA 留 13h） |
| ④ Gulf Air GF 125/19 | Economy Light/Classic | **20-30kg 免费** | 无自转 |
**含 1 件托运的真实到手**：拆票 ≈ **€1,335**（+French bee €35 +Frontier 两段 ≈ €100；3U/GF 已含）；R2 单张多程 Basic 舱加行李后 ≈ **€1,360-1,400**。
**最省心的选择**：R4（€1,301-1,392，三张票全联程）或 R2 单张多程（€1,262，一次预订）。

---

## 8) 预订 / 查价链接（2026-11-06 全部可用）
- ①：https://www.kayak.co.uk/flights/PAR-NYC/2026-12-24 · https://www.skyscanner.net/transport/flights/PAR/NYC/261224/?adults=1&currency=GBP&locale=en-GB&market=UK · https://www.frenchbee.com
- ②：https://www.kayak.co.uk/flights/NYC-LAS/2026-12-31 · https://www.google.com/travel/flights?q=Flights%20from%20NYC%20to%20LAS%20on%202026-12-31%20one%20way&curr=EUR&gl=fr
- ③a：https://www.skyscanner.net/transport/flights/LAS/LAX/270112/?adults=1&currency=GBP&locale=en-GB&market=UK
- ③b：https://www.kayak.co.uk/flights/LAX-PVG/2027-01-12 · https://www.skyscanner.net/transport/flights/LAX/PVG/270112/?adults=1&currency=GBP&locale=en-GB&market=UK · 北京版 https://www.kayak.co.uk/flights/LAX-PEK/2027-01-12
- ④：https://www.kayak.co.uk/flights/PVG-PAR/2027-02-10 · https://www.skyscanner.net/transport/flights/PVG/CDG/270210/?adults=1&currency=GBP&locale=en-GB&market=UK
- 单张多程（R2 €1,262）：https://www.kayak.co.uk/flights/PAR-NYC/2026-12-24/NYC-LAS/2026-12-31/LAS-LAX/2027-01-12/LAX-PVG/2027-01-12/PVG-PAR/2027-02-10/?sort=flight_price
- 川航时刻参考：3U 3838 LAX 21:30 → TFU 05:50+2（周二/五/日，A350-900）https://info.flightmapper.net/route/Sichuan_Airlines_3U_LAX_TFU · TFU→PVG 08:00→10:25（3U 5252 = MU 5404）
- 自动盯盘：`tools/monitor.py`（cron 8:15 / 20:15），历史序列见 `results/price_track.md` 的 "Structure B" 表。
