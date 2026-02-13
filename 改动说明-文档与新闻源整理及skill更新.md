# 文档与新闻源整理及 Skill 更新 知识库更新说明

> 用于公众号/对外发布：知识库新增与修订条目一览。

---

## 一、知识库新增/更新总览

| 类型       | 名称                         | 路径                                                                 | 说明                                                                 |
|------------|------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| 来源整理   | 乐居展厅战略 2026            | `files/source/leju-showroom-strategy-2026.md`                        | 乐聚「夸父」展厅版 3.0、社交智能与展厅商业化、市场规模与护城河。     |
| 来源整理   | 北大王鹤团队 2025 具身盘点   | `files/source/pku-wanghe-2025-embodied-roundup.md`                   | EPIC Lab 灵巧手、故障检测、人机交接、空间推理等方向工作梳理。       |
| 来源整理   | 小米 VLA 开源 2026           | `files/source/xiaomi-vla-open-source-2026.md`                        | Xiaomi-Robotics-0 双脑 MoT、低延迟、跨模态预训练与全面开源。        |
| 访谈摘要   | 乐居展厅战略摘要             | `files/interviews/leju-showroom-strategy-2026-摘要.md`               | 产业视角要点与完整整理稿链接。                                       |
| 访谈摘要   | 北大王鹤团队具身盘点笔记     | `files/interviews/PKU-WangHe-team-2025-embodied-roundup-笔记.md`     | 团队与工作要点，指向来源整理稿。                                     |
| 论文索引   | 小米 VLA 开源索引            | `files/papers/xiaomi-vla-open-source-2026-索引.md`                   | 技术要点与 docs 延伸用索引，指向完整整理稿。                         |
| 文档修订   | 世界模型综述指引             | `docs/1-embodied-overview/1.3-世界模型综述.md`                       | 理解世界 vs 预测未来、分类与应用、开放问题。                         |
| 文档修订   | VLA / SOTA                   | `docs/5-sota/5.1-VLA.md`、`docs/5-sota/README.md`                   | VLA 与 SOTA 部分内容更新。                                           |
| 文档修订   | 人物与生态                   | `docs/8-people/README.md`、`docs/9-landscape/README.md`              | 人物目录链接或简介、生态/格局文档更新。                              |
| Skill 更新  | news-pdf 集成                | `.cursor/skills/news-pdf-integration/SKILL.md`                       | 从 source.md 到 files/source 的整理流程与侵权规避。                 |
| 文档修订   | 根目录说明                   | `根目录说明-news-pdf集成与OCR流程.md`                                | news-pdf 集成与 OCR 流程说明修订。                                  |

---

## 二、逐条说明（内容 + 链接）

### 1. 乐居展厅战略 2026（来源整理）

- **知识库位置**：`files/source/leju-showroom-strategy-2026.md`
- **内容概要**：整理自乐聚 2026 年初展厅战略相关报道。围绕「夸父」展厅版 3.0，归纳战略定位（同一场景做深做细、二十余省落地）、产品演进（社交智能、VIP 识别与 1 米跟随、开箱即用与运维降门槛、41 自由度与抗扰步态）、市场规模（博物馆/科技馆/品牌体验中心等存量与泛商业增量）、护城河（高规格事件、场景数据、人形机器人+生态）及后续挑战与方向。适合作为产业视角下展厅商业化与护城河的参考。
- **链接**：
  - 仓库内：[leju-showroom-strategy-2026.md](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/files/source/leju-showroom-strategy-2026.md)

### 2. 北大王鹤团队 2025 具身盘点（来源整理）

- **知识库位置**：`files/source/pku-wanghe-2025-embodied-roundup.md`
- **内容概要**：整理自北大王鹤老师团队 2025 年工作盘点。涵盖人物与 EPIC Lab 简介，灵巧抓取与操作（BODex、DexVLG、DyWA、DexNDM、可微碰撞检测等），故障检测与人机交接（Code-as-Monitor、MobileH2R、SOFAR 等），以及空间推理与具身多模态等方向。每条工作含会议/期刊与核心结果，便于快速检索与延伸阅读。
- **链接**：
  - 仓库内：[pku-wanghe-2025-embodied-roundup.md](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/files/source/pku-wanghe-2025-embodied-roundup.md)

### 3. 小米 VLA 开源 2026（来源整理 + 论文索引）

- **知识库位置**：完整整理 `files/source/xiaomi-vla-open-source-2026.md`，索引 `files/papers/xiaomi-vla-open-source-2026-索引.md`
- **内容概要**：整理自小米首代具身 VLA 大模型 Xiaomi-Robotics-0 发布与开源报道。4.7B 参数、约 80ms 推理延迟、30Hz 控制、单卡 RTX 4090 可实时运行；双脑 MoT（VLM 大脑 + 16 层 DiT 小脑）、Action Chunk 与流匹配、KV Cache 复用；两阶段跨模态预训练（Action Proposal 对齐、DiT 专项训练）及后训练策略。索引稿提炼要点并指向完整整理，供 docs/5-sota、1-embodied-overview 延伸用。
- **链接**：
  - 仓库内（完整整理）：[xiaomi-vla-open-source-2026.md](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/files/source/xiaomi-vla-open-source-2026.md)
  - 仓库内（索引）：[xiaomi-vla-open-source-2026-索引.md](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/files/papers/xiaomi-vla-open-source-2026-索引.md)

### 4. 乐居展厅战略摘要（访谈摘要）

- **知识库位置**：`files/interviews/leju-showroom-strategy-2026-摘要.md`
- **内容概要**：乐聚展厅战略的「进与守」摘要，产业视角下的人形机器人展厅场景商业化与护城河。含战略、产品、市场、护城河、挑战与方向等要点，并链接至完整整理稿，供 docs/9-landscape 与产业视角延伸用。
- **链接**：
  - 仓库内：[leju-showroom-strategy-2026-摘要.md](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/files/interviews/leju-showroom-strategy-2026-摘要.md)

### 5. 世界模型综述指引（文档修订）

- **知识库位置**：`docs/1-embodied-overview/1.3-世界模型综述.md`
- **内容概要**：基于清华 FIB Lab 世界模型综述的阅读指引。以「理解世界 vs 预测未来」为主线，梳理核心问题、历史与概念、分类框架、决策与应用（含自动驾驶、机器人、社交仿真）、开放问题与未来方向。适合作为进入该综述的路线图。
- **链接**：
  - 仓库内：[1.3-世界模型综述.md](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/docs/1-embodied-overview/1.3-世界模型综述.md)
  - 外部参考：综述 GitHub <https://github.com/tsinghua-fib-lab/World-Model>

### 6. VLA / SOTA 与人物、生态文档（文档修订）

- **知识库位置**：`docs/5-sota/5.1-VLA.md`、`docs/5-sota/README.md`、`docs/8-people/README.md`、`docs/9-landscape/README.md`
- **内容概要**：VLA 与 SOTA 小节内容更新；人物目录 README 链接或简介更新；生态/格局 README 更新。便于在文档内跳转与协作维护。
- **链接**：
  - 仓库内：[5.1-VLA.md](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/docs/5-sota/5.1-VLA.md) | [5-sota README](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/docs/5-sota/README.md) | [8-people README](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/docs/8-people/README.md) | [9-landscape README](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/docs/9-landscape/README.md)

### 7. news-pdf Skill 与根目录说明（Skill / 文档）

- **知识库位置**：`.cursor/skills/news-pdf-integration/SKILL.md`、`根目录说明-news-pdf集成与OCR流程.md`
- **内容概要**：news-pdf-integration Skill 与从 news/source.md 到 files/source 的整理流程、Plan 阶段与侵权规避约定保持一致；根目录说明对 news-pdf 集成与 OCR 流程做了修订，便于项目内批量处理来源文章与流程查阅。
- **链接**：
  - 仓库内：[news-pdf-integration SKILL.md](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/.cursor/skills/news-pdf-integration/SKILL.md)；根目录说明见仓库根目录 `根目录说明-news-pdf集成与OCR流程.md`。

---

## 三、小结

- 本次共新增/修订 11 类条目，涵盖来源整理（乐居、北大王鹤、小米 VLA）、访谈摘要与论文索引、世界模型与 VLA/SOTA/人物/生态文档、news-pdf Skill 与根目录说明。
- 本文档记录知识库更新内容与链接，便于公众号撰写与读者查阅。
