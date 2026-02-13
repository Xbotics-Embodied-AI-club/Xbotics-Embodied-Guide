# 北大王鹤老师团队 2025 年具身智能工作盘点

*基于《具身智能学术之星｜北大王鹤老师团队2025年工作盘点》的整理与延伸（原文已通过 OCR 提取）*

**原文链接**：[具身智能学术之星｜北大王鹤老师团队2025年工作盘点](../source/PKU-WangHe-team-2025-embodied-roundup.pdf)（PDF）

---

## 一、王鹤老师与实验室简介

王鹤，银河通用创始人，北京大学前沿计算研究中心（CFCS）助理教授、博士生导师。2014 年清华大学学士，2021 年斯坦福大学博士（师从美国三院院士 Leonidas J. Guibas），后加入北大投身具身智能科研与教学。创立并领衔**北大具身感知与交互实验室（EPIC Lab）**，以具身技能与具身多模态大模型为核心，推进通用具身智能；兼任北大-银河通用具身智能联合实验室主任、北京智源人工智能研究院具身智能研究中心主任。已在 CVPR、ICCV、ECCV、TRO、RAL、ICRA、NeurIPS、ICLR、AAAI 等发表 50 余篇论文，获 ICCV 2023 最佳论文候选、ICRA 2023 最佳操纵论文候选、2022 世界人工智能大会青年优秀论文奖、Eurographics 2019 最佳论文提名等。研究方向涵盖 **VLA、灵巧手操作、具身导航、仿真预训练** 等。个人主页：<https://scholar.google.com/citations?hl=zh-CN&user=roCAWKOAAAAJ>；实验室：<https://cfcs.pku.edu.cn/people/faculty/hewang/index.htm>。

---

## 二、2025 年至今已发表/录用工作盘点

### 灵巧抓取与操作

**[ICRA 2025] BODex: Scalable and Efficient Robotic Dexterous Grasp Synthesis Using Bilevel Optimization**  
- **机构**：北京大学、Galbot、北京智源人工智能研究院。  
- **问题**：数据驱动灵巧抓取需大规模高质量数据；现有梯度优化方法效率低、能量函数假设强、实验对象有限，且缺乏统一基准。  
- **内容**：将灵巧抓取合成构建为**双层优化**（下层 QP 求接触力，上层梯度下降优化手部姿态），结合 cuRobo 与 ReLU-QP 实现大规模并行（单张 3090 每秒超 49 个抓取，相对基线约 50 倍加速）；**粗到精接触建模**平衡速度与精度；建立基于 MuJoCo 的灵巧抓取基准；生成大规模 800e* 数据集（含漂浮/桌面、预抓取姿态与无碰撞手-臂轨迹）。  
- **结果**：仿真中 Shadow/Allegro/Leap 手成功率均超 75%，穿透深度 &lt;1mm；基于 BODex 数据训练的学习模型仿真成功率由约 40% 提升至 80%；真机 Shadow 手对 20 种物体抓取成功率 81%。  
- 论文：<https://arxiv.org/abs/2412.16490>；项目：<https://pku-epic.github.io/BODex>。

**[ICCV 2025] DexVLG: Dexterous Vision-Language-Grasp Model at Scale**  
- **机构**：北京智源、Galbot、清华大学、北京大学等。  
- **内容**：构建 **DexGraspNet 3.0**（约 1700 万灵巧抓取姿态、17.4 万物体及部分级语义描述）；训练 **DexVLG**，以单视图 RGB-D + 语言指令为输入，融合视觉-语言特征与流匹配去噪，生成语言对齐的灵巧抓取姿态；在 Isaac Gym 中设计部分感知灵巧抓取基准。  
- **结果**：仿真零样本成功率超 76%，部分抓取精度 SOTA；真机简单物体抓取成功率 80%，部分对齐精度 75%。  
- 论文：<https://arxiv.org/pdf/2507.02747.pdf>；项目：<https://jiaweihe.com/dexvlg>。

**[ICRA 2026] Robust Differentiable Collision Detection for General Objects**  
- **机构**：北京大学、Galbot、清华大学、香港理工大学。  
- **问题**：传统碰撞检测（如 GJK+EPA）不可微，限制抓取/操作等接触密集型任务的梯度优化；现有可微方法多限于凸体。  
- **内容**：提出**可微碰撞检测框架**，支持凸与凹形；距离基一阶随机平滑、自适应采样、等效梯度传输，可计算接触点导数，适用于抓取优化等下游。  
- **结果**：在 DexGraspNet 与 Objaverse 复杂网格上中位数误差低于 0.1 mm，毫米级精度显著优于基线；灵巧抓取优化中可细化抓取姿态并保持高效。  
- 论文：<https://arxiv.org/abs/2511.06267>；项目：<https://github.com/jychen18/DiffCollision>。

### 非抓取操作与动力学建模

**[ICCV 2025] DyWA: Dynamics-adaptive World Action Model for Generalizable Non-prehensile Manipulation**  
- **机构**：北京大学、Galbot 等。  
- **问题**：非抓取操作依赖多视图与精确姿态跟踪，且难泛化到质量、摩擦等物理条件变化。  
- **内容**：**DyWA** 联合预测未来状态并基于历史轨迹适配动力学；动力学适配模块编码历史观测-动作对、融合几何与物理；世界动作模型提供额外监督；FiLM 调节将动力学嵌入与世界模型桥接。  
- **结果**：仿真中单视图点云观测成功率较基线提升 31.5%；真机平均成功率 68%，可泛化物体几何、桌面摩擦、非均匀质量与光滑物体。  
- 论文：<https://arxiv.org/pdf/2503.16806>；项目：<https://pku-epic.github.io/DYWA/>。

**[ICLR 2026] DexNDM: Closing the Reality Gap for Dexterous In-hand Rotation via Joint-wise Neural Dynamics Model**  
- **机构**：清华大学、北京大学、上海期智研究院、Galbot。  
- **问题**：灵巧手内旋转存在严重仿真-现实鸿沟；现有方法多限于简单几何、固定手腕，且数据采集依赖人工。  
- **内容**：**关节级神经动力学模型**将高维动力学分解为单关节演化，仅用关节本体感受历史预测状态；「专家-通用」策略蒸馏 + 残差策略适配实现 Sim2Real；「混沌箱」自主数据采集策略生成多样化真机交互数据。  
- **结果**：仿真中通用策略在 unseen 物体上超越基线约 37%–81%；真机完成复杂形状、高长宽比物体及多手腕姿态的空中旋转，遥操作任务优于 AnyRotate、Visual Dexterity 等。  
- 论文：<https://arxiv.org/abs/2510.08556>；项目：<https://meowuu7.github.io/DexNDM>。

### 故障检测、人机交接与空间推理

**[CVPR 2025] Code-as-Monitor: Constraint-aware Visual Programming for Reactive and Proactive Robotic Failure Detection**  
- **机构**：北京航空航天大学、北京大学、北京智源、Galbot。  
- **内容**：**CaM** 将反应式与主动式故障检测统一为时空约束满足；约束元素将实体/部件抽象为点线等几何元素；约束生成器、绘制器、监测器 + 约束感知分割模型 ConSeg；VLM 生成监测代码，子目标开始时生成一次即可实时监测。  
- **结果**：在 CLIPort、Omnigibson、RLBench 及真机中，严重干扰下任务成功率提升约 28.7%，执行时间减少约 31.8%；ConSeg 在约束感知分割上优于现有 SOTA。  
- 论文：<https://arxiv.org/abs/2412.04455>；项目：<https://zhoues.github.io/Code-as-Monitor>。

**[CVPR 2025] MobileH2R: Learning Generalizable Human to Mobile Robot Handover Exclusively from Scalable and Diverse Synthetic Data**  
- **机构**：清华大学、Galbot、北京大学、上海人工智能实验室、上海期智研究院。  
- **内容**：**MobileH2R-Sim** 两阶段流水线生成多样化全身人机交接运动；自动演示生成兼顾安全与模仿友好性（未来避障、最终姿态约束、视觉神经损失）；3D 模仿学习融合人体与物体点云，多尺度集合抽象，端到端学习底座与机械臂协调。  
- **结果**：纯合成数据到真机有效 Sim2Real，无需人体动捕；仿真中交接成功率较 Grasp Selection、Trajectory Planning、GenH2R 等至少提升 15%；真机简单/复杂场景交接成功率分别达 80% 与 63.3%。  
- 论文：<https://arxiv.org/abs/2501.04595>；项目：<https://MobileHzR.github.io>。

**[NeurIPS 2025] SOFAR: Language-Grounded Orientation Bridges Spatial Reasoning and Object Manipulation**  
- **机构**：清华大学、上海交通大学、Galbot、北京大学等。  
- **内容**：**语义朝向（Semantic Orientation）** 用自然语言定义物体朝向；**OrienText300K** 数据集（350K+ 3D 模型与语言-朝向标注）；**PointsO** 零样本语义朝向预测；**SOFAR** 整合 PointsO 与 SAM 等构建含 6-DoF 信息的场景图，支持 VLM 链式思维空间推理与机器人操作；OpenGDOR V2、6-DOF SpatialBench 基准。  
- **结果**：OpenGDOR 零样本成功率 48.7%；SIMPLER-Env 零样本成功率 74.9%；真机 60 项任务优于基线，并在导航、VQA 等泛化良好。  
- 论文：<https://arxiv.org/abs/2502.13143>；项目：<https://github.com/qizekun/SoFar>。

### VLA、世界知识与导航

**[NeurIPS 2025] DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge**  
- **机构**：上海交通大学、EIT、清华大学、Galbot、北京大学、UIUC、中国科学技术大学。  
- **内容**：将 VLA 重构为**感知-预测-动作**；预测动态区域、深度图与高层语义等综合世界知识；块结构注意力避免跨类型知识泄露；扩散 Transformer 解码器做多步动作推理。  
- **结果**：CALVIN ABC-D 平均任务长度 4.44（SOTA）；真机任务成功率 76.7%；LBERO 各赛道优于或媲美现有方法。  
- 论文：<https://arxiv.org/abs/2507.04447>；项目：<https://github.com/Zhangwenyaol/DreamVLA>。

**[ICLR 2026] Embodied Navigation Foundation Model (NavFoM)**  
- **机构**：北京大学、Galbot 等。  
- **内容**：**跨载体、跨任务**导航基础模型；约 800 万导航样本，涵盖四足、无人机、轮式机器人、车辆及视觉-语言导航、目标搜索、目标跟踪、自动驾驶等；**TVI 令牌**嵌入视角与时间；**BATS** 预算感知时间采样；联合训练导航与图像/视频问答数据。  
- **结果**：7 个公开基准上达最优或极具竞争力；VLN-CE RxR 多相机成功率由 56.3% 提升至 64.4%；真机在四足、无人机、轮式机器人等验证泛化与实用性。  
- 论文：<https://arxiv.org/abs/2509.12129>；项目：<https://pku-epic.github.io/NavFoM-Web/>。

**[ICRA 2026] TrackVLA++: Unleashing Reasoning and Memory Capabilities in VLA Models for Embodied Visual Tracking**  
- **机构**：北京大学、Galbot 等。  
- **内容**：基于 NavFoM 的 VLA；**Polar-CoT** 极坐标链式思维空间推理；**TIM** 目标识别记忆模块、置信度门控更新；支持多视图。  
- **结果**：EVT-Bench、Gym-Unreal 等单/多视图 SOTA；真机遮挡、蜿蜒路径、干扰物场景鲁棒，零样本泛化与推理效率兼顾。  
- 论文：<https://arxiv.org/abs/2510.07134>；项目：<https://pku-epic.github.io/TrackVLA-plus-plus-Web/>。

**[ICRA 2026] UrbanVLA: A Vision-Language-Action Model for Urban Micromobility**  
- **机构**：北京大学、中国科学技术大学、北京智源。  
- **内容**：**路线条件**城市微移动 VLA，将导航工具路线与视觉观测对齐并预测轨迹；**HTL** 启发式轨迹提升；SFT + IQL/RFT 两阶段训练（模拟 + 真实混合）。  
- **结果**：MetaUrban SocialNav 超越基线 55%+；真机天桥穿越、行人交互、转弯、避障等 500 米以上长时程可靠导航。  
- 论文：<https://arxiv.org/abs/2510.23576>；项目：<https://pku-epic.github.io/UrbanVLA-Web/>。

---

## 三、实验室整体布局（原文小结）

原文将王鹤老师实验室的研究概括为：**以灵巧操作为核心，以具身多模态大模型为主线，全面推动通用具身智能的系统性突破**。

- **硬件载体**：灵巧手、移动机器人、四足、无人机、城市微移动平台等。  
- **技术路径**：灵巧抓取（BODex、DexVLG）→ 非抓取操作（DyWA）→ 手内旋转（DexNDM）→ 具身导航（NavFoM）→ 视觉跟踪（TrackVLA++）→ 城市微移动（UrbanVLA），打通感知、推理、规划与控制。  
- **方法创新**：双层优化、可微碰撞、神经动力学、视觉编程、流匹配、扩散 Transformer 等，持续突破仿真-现实鸿沟与开集泛化。  
- **数据与基准**：DexGraspNet 3.0、OrienText300K、多载体导航数据集等大规模高质量资源，推动标准化与可复现研究。

---

*—— 整理自《具身智能之心》公众号原文（OCR）| Xbotics 具身智能学习指南 供学习参考*
