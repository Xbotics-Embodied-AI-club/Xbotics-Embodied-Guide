# VLA 后新趋势（上）：VAM——6 篇视频动作模型汇总分析

*基于原文的整理，仅保留核心内容，供学习参考。*

---

## 1. 从 VLA 到 VAM 的范式背景

自 2022 年后，具身控制主流为 **VLA**（Vision-Language-Action）：在 VLM 的视频/图像理解上增加动作头，从大量机器人演示数据中学习物理运动规律（如 PI π0 系列、Figure Helix、Google Gemini Robotics、英伟达 GR00T）。VLM 擅理解场景与语言，但不直接输出控制且对物理规律的学习难、数据需求大。

**VAM（Video Action Model）**：2025 年底至 2026 年初兴起，用**视频生成模型**做机器人控制。英伟达也称 **WAM（World Action Model）**，强调视频生成模型作为世界模型、生成符合物理的视频。VAM 与 WAM 内核一致；若视频模型只生成“好看”却物理不合理，则难以准确驱动动作。

**为何成为趋势**：① 符合「预训练第二种范式」——**next physical state prediction**：像 LLM 在文本上 scaling 得到语言知识一样，视频 scaling 可学到物理知识；② 视频生成模型本身变好，更易生成物理合理的动作视频。VAM 从预训练视频模型出发，训练核心是「帧与帧之间的变化对应什么动作」；视频到动作的衔接通常有两种方式：**逆动力学模型（IDM）**或**用神经网络替代 IDM**。因物理理解已在视频模型中，VAM 对机器人动作数据的需求通常低于 VLA。

---

## 2. 六篇工作概览与两大流派

综述的六项工作：**Video Policy**（Columbia/丰田研究院，2025.8）、**LVP**（MIT/UCB/Harvard，2025.12）、**mimic-video**（mimic/ETH/微软，2025.12）、**1XWM**（1X，2026.1）、**Cosmos Policy**（斯坦福/英伟达，2026.1）、**DreamZero**（英伟达 GEAR，2026.2）。

按「大脑如何工作」类比分为两派：

- **第一流派：先想象，再模仿（Explicit Video Generation）**  
  先生成完整未来视频，再把视频转成动作指令。代表：**LVP**、**1XWM**。

- **第二流派：借用大脑（Internal Representation / Joint Policy）**  
  不必然生成完整视频，利用视频模型中间表示或把动作与图像一起生成。代表：**Video Policy**、**Cosmos Policy**、**mimic-video**、**DreamZero**。

---

## 3. 第一流派：LVP 与 1XWM

**LVP（Large Video Planner）**  
- 思路：用互联网人类操作视频（如 YouTube）训练 14B 视频生成模型，做具身决策。  
- 流程：给定图像+指令 → 生成人手/机器人完成任务的视频 → 用视觉工具（**HaMeR** 3D 手部重建、**MegaSAM** 4D 时空对齐）提取手部轨迹 → **重定向**到机械臂/灵巧手或二指夹爪（GraspNet 等）。  
- 技术：**Diffusion Forcing**（历史/未来分段加噪，推理时可单帧或多帧输入）、**History Guidance**（强制生成紧跟第一帧，保证物理连贯）。  
- 特点：通用性强、可零样本想象新任务；弱点：多步流水线、误差易累积。

**1XWM（1X World Model）**  
- 思路：为自家机器人 NEO 打造「世界模型+IDM」，生成 NEO 视角未来视频再反推动作。  
- 组成：世界模型骨干（14B 文本条件扩散，经 900h 第一人称人类视频 mid-training、70h NEO 数据微调；caption upsampling 用 VLM 生成细粒度字幕）+ **IDM**（根据 WM 生成的两帧预测其间动作，带 DTW 等约束保证运动学正确）。  
- IDM：滑动窗口 W=8，Depth Anything 骨干 + flow matching 头，400h 机器人数据训练，可追踪 NEO 任意状态。后训练数据以抓取-放置为主（98.5%），手部可见的桌面操作。  
- 特点：物理一致、为特定硬件优化；数据与算力需求大。

---

## 4. 第二流派：Video Policy、Cosmos Policy、mimic-video、DreamZero

**Video Policy**  
- 结构：大视频生成器（Video U-Net，基于 Stable Video Diffusion）+ 小动作生成器（Action U-Net）；**联合去噪**，动作从视频模型**中间层特征**解码。  
- 训练：两阶段——先只用视频（可无动作标注）训视频模型学物理；再冻结视频模型，只训动作头。约 **50 demos** 即可达 SOTA。  
- 特点：可用 action-free 视频、极省数据；动作与视频同步生成。

**mimic-video**  
- 提出 **VAM（Video-Action Model）**：视频主干（Cosmos-Predict2）+ 轻量动作解码器（充当 IDM）。  
- **Partial Denoising**：不生成完整像素，只在去噪极早期截取**潜空间特征**，认为已含运动意图与物理规划，直接解码为动作。  
- 特点：计算效率高、数据利用率高（较传统方法省约 10 倍数据）。

**Cosmos Policy**  
- **Latent Injection**：把本体感知、动作、价值都编码成「帧」输入视频模型（Cosmos-Predict2-2B），统一成去噪过程；同时输出动作、未来图像、**Value**。  
- 训练：策略 50%、世界模型 25%、价值函数 25% 联合训练。  
- **Best-of-N 规划**：推理时提出 N 个动作序列，用世界模型想象未来，用价值函数打分，选最优执行；复杂任务成功率提升约 12.5%。  
- 特点：唯一明确做 test-time 搜索与规划；需大量带奖励/价值的轨迹数据。

**DreamZero**  
- 底座：**14B** 视频扩散模型 Wan 2.1（DiT），互联网规模视频预训练。  
- 机制：**自回归**联合去噪——当前观测+指令+本体感知 → 同时输出未来帧与当前 **action chunk**；推理时若真实观测与预测不符则用真实观测更新（如更新 KV Cache），减轻幻觉累积。  
- 优化：Flash Attention、异步执行等，14B 可达 **7Hz** 实时控制；证明大视频模型（14B vs 5B）即使动作头简单也可靠物理理解占优。  
- 数据：强调**多样性**而非重复——22 个环境、每事只做一次等多样化数据即可，依赖预训练已有物理常识。

---

## 5. 对比小结

**架构**：Video Policy / LVP / 1XWM / mimic-video 为多模块或双模型；Cosmos Policy / DreamZero 为单一 Transformer/DiT 大模型。

**从视频到动作**：LVP 用**固定算法**（3D 重建+重定向）；其余 5 种为**学习**——Video Policy、1XWM、mimic-video 为独立动作模块/IDM 从视频或特征反推；Cosmos Policy 把动作当 token 与图像一起生成；DreamZero 把动作与 latent 一起去噪、解码器直接输出。

**数据与训练**：Video Policy、LVP、mimic-video 数据需求少（LVP 生成动作阶段可 training-free）；1XWM、Cosmos Policy 需求大；DreamZero 强调多样化、单次演示即可。

---

## 6. 局限与展望

- **算力与实时性**：VAM 常需实时推理视频，算力要求高；DreamZero 虽优化仍依赖顶级硬件（如 GB200）。  
- **是否真正学到物理**：若视频模型只是模仿画面而非物理规律，控制会出错；可类比 LLM——scaling 与涌现、思维链与 RL 对知识的重要性；视频侧也需 scaling、涌现，以及「视频思维链」等（如 Jim Fan《预训练的第二种范式》所述）。

VAM 在泛化与数据效率上已有提升，有望成为 VLA 之后的重要路线；第二种预训练范式 **next physical state prediction** 能否带来机器人领域的「ChatGPT 时刻」仍待观察。

---

*—— 整理自 Xbotics 具身智能学习指南 | 供学习参考*
