# 新闻源整理（source.docx）知识库更新说明

> 用于公众号/对外发布：基于 2026-03-02 ArXiv 机器人学每日速递的 21 篇整理稿及源文件一览。

---

## 一、知识库新增/更新总览

| 类型 | 名称 | 路径 | 说明 |
|------|------|------|------|
| 来源聚合 | ArXiv 机器人学每日速递 2026-03-02 | news/source.md | 从 source.docx 提取并结构化的当日速递全文 |
| 来源整理 | StemVLA 4D-VLA CALVIN | files/source/stemvla-4d-vla-calvin-2026.md | 融合 3D 未来几何与 4D 历史时空表征的 VLA，CALVIN SOTA |
| 来源整理 | FAVLA 力觉快慢解耦 VLA | files/source/favla-force-vla-2026.md | 力觉自适应快慢解耦的视觉-语言-动作策略 |
| 来源整理 | VCA Vision-Click-Action | files/source/vca-vision-click-action-2026.md | 用点击替代语言指令的机器人操控框架 |
| 来源整理 | KEEP KV 缓存具身规划 | files/source/keep-kv-cache-embodied-planning-2026.md | 高效具身规划的 KV 缓存中心记忆管理，DAC 2026 |
| 来源整理 | ABPolicy B 样条流匹配 | files/source/abpolicy-bspline-flow-matching-2026.md | B 样条控制点动作空间中的异步流匹配操控策略 |
| 来源整理 | 动作空间设计 13k 实证 | files/source/action-space-empirical-13k-2026.md | 13,000+ 次真实部署的动作空间设计系统性研究 |
| 来源整理 | AoE 第一视角数据采集 | files/source/aoe-egocentric-data-collection-2026.md | 面向具身基础模型的始终在线第一视角数据采集系统 |
| 来源整理 | VLA 基准压测与泛化 | files/source/vla-benchmark-generalization-2026.md | 指令跟随 vs 操控技能习得，语言泛化评测 |
| 来源整理 | OmniTrack 人形运动追踪 | files/source/omnitrack-humanoid-motion-tracking-2026.md | 解耦物理可行性与通用运动追踪的人形框架 |
| 来源整理 | OmniXtreme 人形极限运动 | files/source/omnxtreme-humanoid-motion-2026.md | 突破保真度-可扩展性权衡的极限运动追踪 |
| 来源整理 | 人形机器人辅助外科手术 | files/source/humanoid-surgical-unitree-g1-2026.md | Unitree G1 遥操作完成尸体蝶窦切除术里程碑 |
| 来源整理 | Tilt-X 空中连续臂操控 | files/source/tilt-x-aerial-manipulation-2026.md | 多方向工作空间倾斜式连续臂空中操控，ICRA 2026 |
| 来源整理 | 无人机竞速课程 RL | files/source/drone-racing-curriculum-rl-2026.md | 障碍物丰富环境中的视觉课程强化学习框架 |
| 来源整理 | MRIO 多雷达惯性里程计 | files/source/mrio-radar-inertial-odometry-2026.md | 地下烟雾环境定位与建图，ICRA 2026 开源 |
| 来源整理 | SpikingTac 神经形态触觉 | files/source/spikingtac-tactile-neuromorphic-2026.md | 低成本神经形态触觉传感器，约 150 美元、1000Hz |
| 来源整理 | STE-VLN 知识图谱导航 | files/source/ste-vln-knowledge-graph-vln-2026.md | 事件中心知识图谱增强的视觉-语言导航 |
| 来源整理 | SafeGen-LLM 安全任务规划 | files/source/safegen-llm-task-planning-2026.md | 具备安全泛化能力的大语言模型任务规划框架 |
| 来源整理 | refineCBF/HJ-Patch 安全屏障 | files/source/refinecbf-hj-patch-safety-2026.md | 基于 HJ 可达性的在线安全屏障函数精炼 |
| 来源整理 | TSC 密集交通 Stackelberg | files/source/tsc-stackelberg-dense-traffic-2026.md | 拓扑条件 Stackelberg 博弈的去中心化多智能体协调 |
| 来源整理 | GPAs 几何可编程气动执行器 | files/source/gpas-soft-pneumatic-actuator-2026.md | CNC 热封腔室约束层的软体气动执行器 |
| 来源整理 | 今日速览与编辑点评 | files/source/arxiv-daily-misc-20260302.md | 当日其他精选论文速览及编辑点评三方向 |

---

## 二、逐条说明（内容 + 链接）

### 1. 源文件与整体说明

- **知识库位置**：`news/source.md`
- **内容概要**：由 `news/source.docx`（ArXiv 机器人学每日速递 2026-03-02 第 1 期）提取的全文，涵盖具身智能与操控、人形机器人、无人机、传感与安全、自动驾驶、软体机器人等多领域共 39 篇 cs.RO 相关提交的精选整理。
- **链接**：仓库内对应路径即可查阅；公众号源为当日速递推文。

### 2. 具身智能与 VLA（8 篇）

- **知识库位置**：`files/source/` 下 stemvla、favla、vca、keep、abpolicy、action-space、aoe、vla-benchmark 共 8 个 MD。
- **内容概要**：StemVLA（4D 时空 + CALVIN）、FAVLA（力觉快慢解耦）、VCA（点击替代语言）、KEEP（KV 缓存记忆）、ABPolicy（B 样条异步流匹配）、动作空间 13k 实证、AoE 第一视角数据采集、VLA 基准压测与泛化结论；覆盖世界模型、力觉、交互方式、记忆效率、动作平滑与数据规模化等方向。
- **链接**：各文件路径见上表；原文链接见各 MD 内 arXiv 链接。

### 3. 人形机器人（3 篇）

- **知识库位置**：`files/source/omnitrack-humanoid-motion-tracking-2026.md`、`omnxtreme-humanoid-motion-2026.md`、`humanoid-surgical-unitree-g1-2026.md`。
- **内容概要**：OmniTrack 解耦物理可行性与运动追踪、OmniXtreme 突破保真度-规模权衡、Unitree G1 首次辅助尸体蝶窦切除术；涵盖运动控制与医疗辅助里程碑。
- **链接**：同上表及文内 arXiv 链接。

### 4. 无人机与传感（4 篇）

- **知识库位置**：`files/source/tilt-x-aerial-manipulation-2026.md`、`drone-racing-curriculum-rl-2026.md`、`mrio-radar-inertial-odometry-2026.md`、`spikingtac-tactile-neuromorphic-2026.md`。
- **内容概要**：Tilt-X 空中多向连续臂、障碍物环境无人机竞速课程 RL、MRIO 地下烟雾多雷达惯性里程计、SpikingTac 神经形态触觉；涵盖空中操控、竞速、定位与触觉传感。
- **链接**：同上。

### 5. 导航、安全与自动驾驶（4 篇）

- **知识库位置**：`files/source/ste-vln-knowledge-graph-vln-2026.md`、`safegen-llm-task-planning-2026.md`、`refinecbf-hj-patch-safety-2026.md`、`tsc-stackelberg-dense-traffic-2026.md`。
- **内容概要**：STE-VLN 事件中心知识图谱 VLN、SafeGen-LLM 安全任务规划、refineCBF/HJ-Patch 在线安全屏障、TSC 密集交通 Stackelberg 协调。
- **链接**：同上。

### 6. 软体与速览（2 篇）

- **知识库位置**：`files/source/gpas-soft-pneumatic-actuator-2026.md`、`arxiv-daily-misc-20260302.md`。
- **内容概要**：GPAs 几何可编程气动执行器及外骨骼/触觉/双足应用；当日其他精选（MGGO、MPAIL、手术力控、SAGE-LLM、Neural ODE PAM、无蓝图搭建、四足安全综述、MicroPush）及编辑点评三方向。
- **链接**：同上。

---

## 三、小结

- 本次新增 **1 个源文件**（`news/source.md`，由 `news/source.docx` 提取）与 **21 篇** 原创整理稿，均位于 `files/source/`，对应 2026 年 3 月 2 日 ArXiv 机器人学每日速递第 1 期内容。
- 无 docs 延伸块调整（Phase B 未发现需并入正文的延伸与参考块）。
- 共 **22 项** 知识库新增/更新，便于后续在公众号或知识库中按主题引用与延伸阅读。
