# 全身遥操作、模仿学习与宇树生态方案合集（整理）

*基于原文的整理，仅保留核心内容，供学习参考。*

---

## 1. 全身遥操作与数据采集

- **TWIST / TWIST2**：全身遥操作与仿制系统；TWIST2 强调可扩展、便携、 holistic 人形数据采集（[TWIST](https://yanjieze.com/TWIST)、[TWIST2](https://yanjieze.com/TWIST2)）。
- **RGMT**：鲁棒且通用的人形运动追踪（[RGMT](https://zeonsunlightyu.github.io/RGMT.github.io)）。
- **身外化身**：西工大/西湖等「影子」式 AI，实时镜像人体运动（[报道](https://news.housebots.com/news/westlake-robotics-unveils-gae-a-breakthrough-shadow-function-ai-that-lets-robots-mirror-human-movement-in-real-time)）。

---

## 2. Motion Tracking 与模仿学习

- **GMR**：通用运动重定向（[GMR](https://github.com/YanjieZe/GMR)）。
- **DeepMimic**（2018）：单段动捕 + RL，跑步、后空翻、侧手翻等；RSI/ET 加速训练；可加任务奖励做旋踢、走平衡木等；多段动捕+指令切换多动作（[DeepMimic](https://xbpeng.github.io/projects/DeepMimic/index.html)）。
- **AMP**：对抗运动先验，风格化物理角色控制（[AMP](https://xbpeng.github.io/projects/AMP/index.html)）。
- **BeyondMimic**：从运动追踪到通用人形控制，Guided Diffusion（[BeyondMimic](https://beyondmimic.github.io)）。
- **OmniRetarget**（亚马逊）：人形全身 loco-manipulation 与场景交互的**交互保持**数据生成。流程：动捕 → 德劳内四面体化得人-物交互网格 → 拉普拉斯变形能量最小化将人体重定向为机器人轨迹；单条动捕+数据增强（改物体尺寸、位置等再求最优）生成大量轨迹，用于 RL 再 sim2real（[OmniRetarget](https://omniretarget.github.io)）。宇树春晚蹬墙后空翻等可由此工作流实现。
- **HumanX**：从人体视频学人形交互（接抛篮球、上篮、踢球、搬桶等）。XGen：人体 3D 姿态+轨迹 → GMR 重定向 → 反向/正向仿真拼接接球等轨迹 → 数据增强；XMimic：Teacher 专精模型 → 蒸馏为单一 Student，无奖励模仿、无需参考动作输入即可本能反应；动捕物体位置即可部署（[HumanX](https://wyhuai.github.io/human-x)）。

---

## 3. 宇树跑酷与感知方案

- **PH Parkour**：感知人形跑酷，Motion Matching 链式动态技能（[PH Parkour](https://php-parkour.github.io)）。
- **Project Instinct**：Deep Whole-Body Parkour、Hiking in the Wild、Robot Parkour Learning 等（[Project instinct](https://project-instinct.github.io)）。

---

## 4. 宇树 Go1 机器狗论文

DrEureka（瑜伽球）、Robot Parkour Learning（跑酷）、DribbleBot（运球）、A1 射门、Walk These Ways（步态）、Eurekaverse（LLM 设计奖励函数）等，均可在对应项目页查看（略列链接见原文）。

---

## 5. 宇树人形格斗赛相关论文

- **ASAP**：仿真-现实物理对齐，「差异动作模型」拟合残差，微调后模仿人类视频（科比投篮、C罗腾空等）（[human2humanoid](https://human2humanoid.com)）。
- **VideoMimic**：手机视频 → real-to-sim-to-real，上下楼梯、坐椅子（[videomimic](https://videomimic.net)）。
- **HuB**：极限平衡，李小龙侧踢、燕式平衡（[HuB](https://hub-robot.github.io)）。
- **Embrace Collisions**：多部位接触可部署人形 shadowing，膝盖/臀部/手肘碰撞仍可丝滑起身（[Project instinct](https://project-instinct.github.io)）。
- **HoST**：多姿势站起（趴地、靠墙、坐椅），翻身-跪起-站立三阶段+课程学习（[HoST](https://taohuang13.github.io/humanoid-standingup.github.io)）。
- **BeamDojo**：梅花桩、平衡木等稀疏落脚点行走（[BeamDojo](https://why618188.github.io/beamdojo)）。
- **HUGWBC**：统一全身控制器，行走/跳跃/单脚跳，可调步频、摆腿高度等（[HUGWBC](https://hugwbc.github.io)）。
- **HOMIE**：外骨骼驾驶舱式 loco-manipulation，踏板+动捕手套控制行走、抓取、搬运（[HOMIE](https://homietele.github.io)）。

---

*—— 整理自 Xbotics 具身智能学习指南 | 供学习参考*
