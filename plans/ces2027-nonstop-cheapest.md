# Plan: CES 2027 直飞最便宜方案研究

## Context
用户想要**直飞（nonstop）**往返拉斯维加斯看 CES 2027：
- 行程约 **一周半（10–11 晚）**，必须包含 CES 日期（2027-01-06 ~ 01-09）
- 硬约束不变：**1/5 之前抵达 LAS**
- 其余日期自选（出发窗口大约 1/2–1/4，回程大约 1/14–1/18）
- 之前所有方案均为一次中转；现在要回答"直飞要多少钱"

## 已知直飞情报（待验证）
| 航线 | 航司 | 状态 |
|---|---|---|
| CDG → LAS | Delta（DL229，周日一班）| ✅ 已确认 2027/1/3 10:30→12:15 存在 |
| LAS → CDG/ORY | Frontier/Delta 回程直飞 | ❓ Frontier 2026 新开 LAS→欧洲线方向，待验证 2027/1 |
| LHR → LAS | Virgin | ❓ 回程见过 Virgin 执飞 LAS→LHR，去程班期待验证（非巴黎出发，仅参照） |

## 用户已确认（2026-11-04）
1. **可接受纽约中转**（Paris↔NYC↔LAS 拼法有效，含拆票）
2. 接受 **(b) 去程直飞 + 回程一次短转机**；纯去回双直飞不强求
3. **预算越低越好，~€500 最理想**（直飞若超支需明说；NYC 中转拼票是最可能接近 €500 的路径）
4. **出发城市锁定巴黎**（CDG/ORY 两机场；FRA 方案仅作价格参照保留）

## Approach（已按答复收窄）
### 路径 A — 直飞去 + 短转机回（舒适优先档）
1. 验证 2027/1 直飞班期：DL229 CDG→LAS（✅已知 1/3 周日 10:30→12:15）；AF/DL 代码共享；LAS→欧洲回程直飞（Frontier 等）逐条验证，无则明说
2. Scrapling 抓 PAR(CDG/ORY)↔LAS 往返：去 1/2–1/4 × 回 1/14–1/18 网格，筛含直飞去程的选项
3. 拆票对比：DL 直飞单程 + 回程单独（如 Delta LAX 短转回程单程 £267 档）vs 整票

### 路径 B — 纽约中转拼票（€500 冲击档）⭐ 重点
4. 国际段低价源：Norse Atlantic（CDG/ORY→JFK，2026 开线待验证）、AF/DL/UA 单程；抓 PAR→NYC(JFK/EWR/NYC-all) 单程日历 1/2–1/4 去、1/14–1/18 回
5. 国内段：NYC→LAS 单程（B6/DL/AA/UA/Frontier EWR），抓同窗口单程日历
6. **组合最小化**：min(整票 PAR↔LAS 经NYC中转, 国际段+国内段拆票×4向组合)；拆票无联程保障，中转留 ≥6h 缓冲
7. 与既有冠军（CDG 12/31 £564、CDG 1/3 夜航 £642；FRA £549 仅参照）对比列表

### 收尾
8. 输出两个答案：**巴黎出发直飞去回最便宜** / **NYC 中转最便宜**，标注与 €500 预算差距
9. 更新 `results/ces2027_flight_research.md` 新增 "NONSTOP & NYC-LAYOVER HUNT" 章节（commit+push）

## Files to modify
- `results/ces2027_flight_research.md` — 新增章节
- 临时脚本放 `/tmp`（不入库）

## Reuse
- 抓取脚本模式：`/tmp/rescan.py`、`/tmp/ret2.py`（StealthyFetcher + "Flight option N:" 解析）
- 班期验证模式：`/tmp/fm.py`、`/tmp/av4.py`（flightmapper / aviability）
- 已有回程单程日历数据：LAS→CDG 1/17 £267、1/18 £269（2026-11-02 抓取）

## Verification
- 每个"直飞"结论必须有：航线 + 班期日 + 时刻 + 来源链接；无法验证的标 ❓ 不呈现
- 价格全部来自当日 Skyscanner 实时抓取（GBP→EUR 注明换算汇率）
- 拆票方案列出行李费追加后的到手价（Norse/Frontier 托运行李 $30-45/程）
- 对比表与旧冠军数据并列，Git diff 可追溯
