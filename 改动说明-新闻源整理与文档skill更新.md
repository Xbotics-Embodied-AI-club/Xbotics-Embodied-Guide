# 新闻源整理、1.3 延伸并入正文与 docs-extensions-inline Skill 知识库更新说明

> 用于公众号/对外发布：知识库新增与修订条目一览。

---

## 一、知识库新增/更新总览

| 类型 | 名称 | 路径 | 说明 |
|------|------|------|------|
| 来源整理 | 全身遥操作与宇树生态方案合集 2026 | `files/source/embodied-teleop-parkour-catalog-2026.md` | TWIST/RGMT、DeepMimic/OmniRetarget/HumanX、跑酷、Go1、格斗赛论文等归纳与链接。 |
| 来源整理 | 千寻创始人专访 2026 | `files/source/qianxun-hanfengtao-interview-2026.md` | 《晚点》韩峰涛：20 亿融资、26 年模型淘汰赛、可穿戴采数、宁德时代、先工业再家庭。 |
| 来源整理 | NVIDIA SAGE 3D 场景生成 2026 | `files/source/nvidia-sage-3d-scenes-2026.md` | SAGE 框架：Agent+MCP、双重校验、三级增强、SAGE-10k 开源与机器人训练效果。 |
| 文档修订 | 世界模型综述 1.3 | `docs/1-embodied-overview/1.3-世界模型综述.md` | 文末「延伸与参考」块删除，7 条链接按主题分散到正文各小节末尾（1.3.1/1.3.6.1/1.3.7.2/1.3.7 末）。 |
| Skill 更新 | docs-extensions-inline | `.cursor/skills/docs-extensions-inline/SKILL.md` | 将 MD 文末「延伸与参考」按主题并入正文的流程，可复用到全项目 MD。 |

---

## 二、逐条说明（内容 + 链接）

### 1. 全身遥操作与宇树生态方案合集 2026（来源整理）

- **知识库位置**：`files/source/embodied-teleop-parkour-catalog-2026.md`
- **内容概要**：整理自 news/source.md 首段目录式内容。涵盖全身遥操作与数据采集（TWIST/TWIST2、RGMT、身外化身）、Motion Tracking 与模仿学习（GMR、DeepMimic、AMP、BeyondMimic、OmniRetarget、HumanX 的 XGen/XMimic 与蒸馏）、宇树跑酷与感知（PH Parkour、Project Instinct）、宇树 Go1 机器狗论文、宇树人形格斗赛相关（ASAP、VideoMimic、HuB、HoST、BeamDojo、HUGWBC、HOMIE 等）。每条保留核心要点与项目/论文链接，便于查阅与延伸。
- **链接**：
  - 仓库内：https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/files/source/embodied-teleop-parkour-catalog-2026.md

### 2. 千寻创始人专访 2026（来源整理）

- **知识库位置**：`files/source/qianxun-hanfengtao-interview-2026.md`
- **内容概要**：整理自《晚点》对千寻智能创始人韩峰涛的专访。20 亿融资与估值破百亿、26 年具身类似 23 年大模型「模型跑不到头部就没牌桌」；良性竞争与中厂策略（大厂下场前一年卖 10 万台）；数据卡点与可穿戴采数（视频+遥操作→可穿戴 4 代迭代、可用性 30%→95%、成本约遥操作 1/10、26 年目标 100 万小时）；宁德时代合作与电池插拔检测场景、先工业再商业再家庭；与高阳合伙、主航道聚焦模型。供产业与融资视角延伸用。
- **链接**：
  - 仓库内：https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/files/source/qianxun-hanfengtao-interview-2026.md
  - 外部：可检索《晚点》千寻韩峰涛专访原文

### 3. NVIDIA SAGE 3D 场景生成 2026（来源整理）

- **知识库位置**：`files/source/nvidia-sage-3d-scenes-2026.md`
- **内容概要**：整理自 SAGE 框架报道。自然语言指令生成可交互、可直接对接模拟器的高质量 3D 场景；Agent 驱动 + MCP、四大生成工具（场景初始化、资产放置/移动/移除）、视觉与物理双重校验（Isaac Sim）；三级场景增强（物体配置/类别/布局）与 SAGE-10k 开源；拾取放置与移动操作任务上优于 Holodeck、SceneWeaver，泛化与稳定性指标突出。供仿真与场景生成、机器人数据扩展延伸用。
- **链接**：
  - 仓库内：https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/files/source/nvidia-sage-3d-scenes-2026.md
  - 外部：论文 https://arxiv.org/pdf/2602.10116 项目 https://nvlabs.github.io/sage/

### 4. 世界模型综述 1.3 延伸并入正文（文档修订）

- **知识库位置**：`docs/1-embodied-overview/1.3-世界模型综述.md`
- **内容概要**：原文档末尾独立「延伸与参考」块已删除，其中 7 条链接按主题分散到正文相关小节末尾：1.3.1 末增加 1X 对谈；1.3.6.1 末增加 VAM 综述；1.3.7.2 末增加北大王鹤、小米 VLA、星海图 G0、HumanX；1.3.7 节末增加乐聚展厅战略。读者在对应小节即可看到延伸，无需翻到文末。
- **链接**：
  - 仓库内：https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/docs/1-embodied-overview/1.3-世界模型综述.md

### 5. docs-extensions-inline Skill（Skill 更新）

- **知识库位置**：`.cursor/skills/docs-extensions-inline/SKILL.md`
- **内容概要**：项目级 Skill，规定将 MD 文末「延伸与参考」等链接块按主题分散到正文各小节末尾、删除文末独立块的流程。包含 Plan 阶段（识别块、为每条选定目标小节）、放置原则（概念/视频/机器人/产业等）、正文格式（「**延伸**：」+ 链接）、实施步骤与可复用说明。后续可对任意 docs 或项目 MD 执行「延伸并入正文」。
- **链接**：
  - 仓库内：https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/.cursor/skills/docs-extensions-inline/SKILL.md

---

## 三、小结

- 本次共新增 3 项来源整理（遥操作/宇树合集、千寻专访、NVIDIA SAGE）、1 项文档修订（1.3 延伸并入正文）、1 项 Skill 更新（docs-extensions-inline）。
- 整理稿均位于 `files/source/`，符合 news-pdf-integration 流程；1.3 与 Skill 便于全项目 MD 统一「延伸在正文」的写法。
- 本文档记录知识库更新内容与链接，便于公众号撰写与读者查阅。
