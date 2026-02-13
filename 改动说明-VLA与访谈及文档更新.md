# VLA、访谈与文档更新 知识库更新说明

> 用于公众号/对外发布：知识库新增与修订条目一览。

---

## 一、知识库新增/更新总览

| 类型       | 名称                         | 路径                                                                 | 说明                                                                 |
|------------|------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| 来源整理   | 星海图 G0 系列端侧 VLA 2026   | `files/source/galaxea-g0-tiny-vla-2026.md`                           | G0 Plus 3B 开源、G0 Tiny 250M Orin 10Hz、后训练框架与部署链路。       |
| 来源整理   | HumanX 人-物交互访谈 2026     | `files/source/humanx-hoi-interview-2026.md`                          | 王荫槐访谈：从人体视频学 HOI、PhysHOI→Skillmimic→HumanX、半合成数据。 |
| 来源整理   | VAM 视频动作模型综述 2026     | `files/source/vam-video-action-model-survey-2026.md`                 | VLA 后新趋势、6 篇 VAM 汇总、两流派与对比。                           |
| 访谈纪要   | HumanX HOI 访谈纪要          | `files/interviews/humanx-hoi-interview-2026-纪要.md`                 | HumanX 访谈要点与整理稿链接。                                        |
| 论文索引   | 星海图 G0 系列索引           | `files/papers/galaxea-g0-tiny-vla-2026-索引.md`                      | 端侧 VLA 要点与 docs 延伸用索引。                                     |
| 论文索引   | VAM 视频动作模型索引         | `files/papers/vam-video-action-model-survey-2026-索引.md`            | 6 篇综述要点与 docs 延伸用索引。                                      |
| 文档修订   | 世界模型综述                 | `docs/1-embodied-overview/1.3-世界模型综述.md`                       | 内容或链接修订。                                                      |
| 文档修订   | VLA / SOTA                   | `docs/5-sota/5.1-VLA.md`、`docs/5-sota/README.md`                   | 新增星海图 G0、VAM 综述条目与延伸链接。                               |
| 文档修订   | 人物                         | `docs/8-people/README.md`                                            | HumanX 访谈链接与简介更新。                                           |

---

## 二、逐条说明（内容 + 链接）

### 1. 星海图 G0 系列端侧 VLA 2026（来源整理 + 论文索引）

- **知识库位置**：完整整理 `files/source/galaxea-g0-tiny-vla-2026.md`，索引 `files/papers/galaxea-g0-tiny-vla-2026-索引.md`。
- **内容概要**：整理自星海图 G0 系列升级与开源报道。G0 Plus 3B 权重与代码开源，更大规模本体与 Web Data 预训练，开箱支持万物抓取、衣物折叠等高泛化操作；G0 Tiny 250M 端侧 VLA，R1 Pro 遥操作数据预训练，TensorRT 量化，NVIDIA Orin 上 10Hz 实时推理，约 5 分钟部署、物品传递开箱即用，为首个开源端侧部署 VLA；后训练框架支持 G0 Plus / G0 Tiny 及 pi0 / pi0-FAST。索引稿提炼要点并指向完整整理，供 docs/5-sota、1-embodied-overview 延伸用。
- **链接**：
  - 仓库内（完整整理）：[galaxea-g0-tiny-vla-2026.md](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/files/source/galaxea-g0-tiny-vla-2026.md)
  - 仓库内（索引）：[galaxea-g0-tiny-vla-2026-索引.md](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/files/papers/galaxea-g0-tiny-vla-2026-索引.md)
  - 外部：OpenGalaxea/GalaxeaVLA <https://github.com/OpenGalaxea/GalaxeaVLA>

### 2. HumanX 人-物交互访谈 2026（来源整理 + 访谈纪要）

- **知识库位置**：完整整理 `files/source/humanx-hoi-interview-2026.md`，访谈纪要 `files/interviews/humanx-hoi-interview-2026-纪要.md`。
- **内容概要**：整理自对 HumanX 一作王荫槐博士的访谈。核心为从人体视频学习人-物交互（HOI）、用原生 HOI 数据训通用交互控制器；系列演进 PhysHOI→Skillmimic→HumanX，XGen 从视频合成数据、XMimic 解决怎么学；与全身运动控制经典工作（PHC/WBC）的区别、接触与相对运动约束、半合成数据与「合成」思路；项目页 https://wyhuai.github.io/human-x/ 。纪要提供要点与整理稿链接，供 docs/8-people 与模仿学习/人形控制延伸用。
- **链接**：
  - 仓库内（完整整理）：[humanx-hoi-interview-2026.md](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/files/source/humanx-hoi-interview-2026.md)
  - 仓库内（访谈纪要）：[humanx-hoi-interview-2026-纪要.md](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/files/interviews/humanx-hoi-interview-2026-纪要.md)
  - 外部：HumanX 项目页 <https://wyhuai.github.io/human-x/>

### 3. VAM 视频动作模型综述 2026（来源整理 + 论文索引）

- **知识库位置**：完整整理 `files/source/vam-video-action-model-survey-2026.md`，索引 `files/papers/vam-video-action-model-survey-2026-索引.md`。
- **内容概要**：整理自 VLA 后新趋势的 6 篇视频动作模型（VAM）汇总。从 VLA 到 VAM 的范式背景（next physical state prediction、视频生成模型做控制）；两流派：先想象再模仿（LVP、1XWM）与借用大脑/联合生成（Video Policy、mimic-video、Cosmos Policy、DreamZero）；各篇思路、数据与训练、从视频到动作的衔接方式及局限。索引稿提炼要点并指向完整整理，供 docs/5-sota、1.3 世界模型综述延伸用。
- **链接**：
  - 仓库内（完整整理）：[vam-video-action-model-survey-2026.md](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/files/source/vam-video-action-model-survey-2026.md)
  - 仓库内（索引）：[vam-video-action-model-survey-2026-索引.md](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/files/papers/vam-video-action-model-survey-2026-索引.md)

### 4. 文档修订（世界模型、VLA/SOTA、人物）

- **知识库位置**：`docs/1-embodied-overview/1.3-世界模型综述.md`、`docs/5-sota/5.1-VLA.md`、`docs/5-sota/README.md`、`docs/8-people/README.md`。
- **内容概要**：1.3 世界模型综述做内容或链接修订；5.1-VLA 与 5-sota README 新增星海图 G0 系列、VAM 视频动作模型条目及指向整理稿/索引的延伸链接；8-people README 更新 HumanX 访谈链接与简介，便于在文档内跳转与协作维护。
- **链接**：
  - 仓库内：[1.3-世界模型综述.md](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/docs/1-embodied-overview/1.3-世界模型综述.md) | [5.1-VLA.md](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/docs/5-sota/5.1-VLA.md) | [5-sota README](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/docs/5-sota/README.md) | [8-people README](https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/blob/main/docs/8-people/README.md)

---

## 三、小结

- 本次共新增/修订 9 类条目，涵盖来源整理（星海图 G0、HumanX 访谈、VAM 综述）、访谈纪要、论文索引与文档修订（世界模型、VLA/SOTA、人物）。
- 本文档记录知识库更新内容与链接，便于公众号撰写与读者查阅。
