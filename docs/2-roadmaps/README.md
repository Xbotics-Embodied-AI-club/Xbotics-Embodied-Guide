# 2. 各技术学习路线（Roadmaps）

**贡献者**：@KandS

> 每条路线 = 前置要求 → 4–8 周分周计划 → 里程碑 → 作业与验收 → 延伸阅读

## 小标题

* [2.1 强化学习](#21-强化学习)
* [2.2 模仿学习](#22-模仿学习)
* [2.3 3D 视觉](#23-3d-视觉)
* [2.4 规划与控制](#24-规划与控制)
* [2.5 定位与导航](#25-定位与导航)
* [2.6 触觉与力控](#26-力控与触觉)
* [2.7 VLA](#27-vla)
* [2.8 Sim2Real](#28-sim2real)
* [2.9 世界模型](#29-世界模型)
* [2.10 数据飞轮与遥操作](#210-数据飞轮与遥操作)

**通用路线模板**

```md
#### <方向名> 学习路线（4–8 周）
- 前置要求：<课程/工具/数学>
- 第 1–2 周：跑通最小可行 demo（给出命令与脚本名）
- 第 3–4 周：改 1–2 个关键模块做对比实验
- 第 5–8 周：选择 1 个实战任务，交付 Demo+报告
- 里程碑：<成功率/曲线/可视化>
- 常见坑：<列 3–5 条>
- 延伸：<论文/代码/数据集 3–6 条>
- 贡献者：@yourname
```

**样板 A｜Diffusion Policy 路线（可直接用）**

* 前置：Python/PyTorch；理解轨迹/动作参数化
* 周程：`train_dp.py` 跑通 → 更换视觉编码器（SigLIP）/动作表示 → 加入遥操作数据，完成桌面抓取
* 里程碑：成功率≥80%，采样/去噪可视化
* 坑：时间对齐、动作尺度、采样步数引入时延
* 延伸：DP/ACT/LEAP；Bridge/RT-*；W&B/TensorBoard

**样板 B｜VLA 路线（OpenVLA/π0/RT-2 思路）**

* 前置：Transformer、CLIP/SigLIP
* 周程：最小 Demo（回放推理）→ 换编码器/提示/动作 token 化 → 多步骤指令任务
* 里程碑：多指令可控 Demo + 评测脚本
* 坑：动作对齐、长序列退化、指令歧义
* 延伸：OpenVLA/RT-2/π0；Hydra/Accelerate/LoRA；Bridge/Libero/Open-X

```md
#### <方向名>
- **前置要求**：<工具/数学>
- **理论**：
    - **基础**：<方法发展路线> 
    - **课程**：<课程名（链接）> | <课程简介>
- **实践**：
    - **工具**：<资料库（链接）> | <资料库简介>
    - **最小目标**：
    - **进阶目标**：
- **延伸**：
    - **论文/项目**：<论文链接> （可选）
    - **工具**：<代码库链接>（可选）
```

---

#### 2.1 强化学习
- **前置要求**：Pytorch / 马尔可夫决策过程（MDP）
- **理论**：
  - **基础**：Q-learning → DQN → REINFORCE → Actor-Critic → PPO
  - **课程**：
    - [OpenAI Spinning Up in Deep RL](https://spinningup.openai.com/)：提供 REINFORCE、TRPO、PPO、DDPG、TD3、SAC 等算法的理论讲解与实现
- **实践**：
  - **工具**：
    - [Stable-Baselines3](https://github.com/DLR-RM/stable-baselines3) ：实现 DQN、PPO、A2C、TD3、SAC 等算法，广泛用于 RL 实验，兼容 Gym
    - [Gymnasium](https://github.com/Farama-Foundation/Gymnasium)：提供 CartPole、MountainCar、LunarLander 等经典任务，用于入门测试
  - **最小目标**：使用 PPO 训练智能体，完成 CartPole 平衡杆任务
  - **进阶目标**：探索稀疏奖励情境下的 MountainCar 爬坡车任务
- **延伸**：
  - **项目**：
    - [RDT-1B](https://rdt-robotics.github.io/rdt-robotics/)：12 亿参数的扩散基础模型，支持语言、图像和动作输入，适用于单臂、双臂和移动机器人等多种平台
    - [RTX](https://robotics-transformer-x.github.io/)：结合视觉、语言和动作信息，实现端到端的机器人控制
  - **工具**：
    - [RLlib](https://github.com/ray-project/ray)：分布式强化学习库，支持并行训练，部署简单，适合大规模强化学习实验

---

#### 2.2 模仿学习
- **前置要求**：PyBullet / 强化学习
- **理论**：
  - **基础**：BC → DAgger → GAIL
  - **课程**：
    - [CS285 深度强化学习课程（UC Berkeley）](https://rail.eecs.berkeley.edu/deeprlcourse/)：包含 DQN、REINFORCE、PPO、DDPG、SAC、BC、DAgger 等算法的完整作业和实现
- **实践**：
  -  **工具**：
     -  [Imitation](https://github.com/HumanCompatibleAI/imitation?tab=readme-ov-file) ：提供 Behavior Cloning、DAgger、GAIL 等算法的实现，适配 Stable Baselines3，广泛用于仿人任务研究
     -  [PyBullet](https://github.com/bulletphysics/bullet3)：支持机器人、强化学习和虚拟现实的物理仿真，提供 Python 接口
  -  **最小目标**：在 PyBullet 中采集机械臂轨迹，使用 Behavior Cloning 拟合策略，验证成功率
  -  **进阶目标**：先用少量专家演示预训练（BC），再微调（PPO）实现迁移学习效果
- **延伸**：
  - **项目**：
    - [Diffusion Policy](https://github.com/real-stanford/diffusion_policy)：基于扩散模型的策略学习方法，适用于高维动作空间的机器人控制任务
    - [DP3](https://3d-diffusion-policy.github.io/) ：将 3D 视觉表示与扩散策略相结合
    - [HumanPlus](https://humanoid-ai.github.io/)：人形机器人系统，融合了模仿学习、强化学习和影子学习技术
  - **工具**：
    - [RoboMimic](https://github.com/ARISE-Initiative/robomimic)：集成多个 IL 算法，支持多机器人数据集，适合多任务与多模态策略研究
    - [LeRobot](https://github.com/huggingface/lerobot)：支持 Diffusion Policy 等多种策略，适合多任务机器人操作研究

---

#### 2.3 3D 视觉

- **前置要求**：OpenCV / PyTorch / 基础线性代数与几何
- **理论**：
  - **基础**：2D/3D 视觉分割（Mask R-CNN/PointNet） → 6D 姿态估计（PoseCNN/CosyPose） → 手眼标定 → 抓取策略 (2D/6D)
  - **课程**：
    - [《动手学深度学习》中文版](https://github.com/d2l-ai/d2l-zh)：提供PyTorch实现的CNN等深度学习基础
    - [OpenCV-Python 中文教程](https://github.com/makelove/OpenCV-Python-Tutorial)：涵盖图像处理、特征提取等CV基础
- **实践**：
  - **工具**：
    - [Detectron2](https://github.com/facebookresearch/detectron2)：支持Mask R-CNN等先进检测与分割算法
    - [Open3D-ML](https://github.com/isl-org/Open3D-ML)：专注于3D机器学习任务，如语义点云分割
    - [PyBullet](https://github.com/bulletphysics/bullet3)：轻量级物理仿真平台，用于搭建机械臂抓取实验环境
  - **最小目标**：使用 Detectron2 在自定义数据集上训练一个实例分割模型
  - **进阶目标**：在 YCB-Video 数据集上复现 PoseCNN，完成物体 6D 姿态估计
- **延伸**：
  - **项目**：
    - [GraspNet-1Billion](https://github.com/graspnet/graspnet-baseline)：大规模抓取数据集与基线模型
    - [Dex-Net 2.0](https://github.com/BerkeleyAutomation/dex-net)：基于物理的抓取评分与规划框架
    - [Tac2Pose](https://github.com/harvard-visionlab/tac2pose)：视觉与触觉融合的姿态回归方法
  - **工具**：
    - [MuJoCo](https://github.com/google-deepmind/mujoco)：高性能物理引擎，适合研究和开发
    - [Gazebo](https://github.com/osrf/gazebo)：功能强大的机器人仿真平台

---

#### 2.4 规划与控制

- **前置要求**：ROS / 线性代数 / 基础微积分
- **理论**：
  - **基础**：正运动学（DH参数） → 逆运动学（解析/数值解法） → 动力学建模（Lagrangian/Newton-Euler） → 采样法规划（PRM/RRT） → 轨迹生成与平滑（B样条） → 经典控制器（PID） → 阻抗控制 → 模型预测控制（MPC）
  - **课程**：
    - [《机器人学：规划、控制及应用》](https://github.com/qqfly/how-to-learn-robotics)：开源中文学习指南，涵盖运动学、动力学、控制等核心内容
    - [《Modern Robotics》配套代码库 (C++)](https://github.com/fan-ziqi/ModernRoboticsCpp_CN)：提供《Modern Robotics》一书的C++实现，注释为中文，便于理解
    - [ROSBOT](https://github.com/Githubcxy666/ROSBOT)：汇总了ROS机器人开发的相关资料，包含运动学模型、路径规划算法（Dijkstra, A*, RRT）、ROS常用命令等内容
- **实践**：
  - **工具**：
    - [Gazebo](https://gazebosim.org/home)：真实物理模拟环境，用于验证控制器效果
    - [nobleo/path_tracking_pid](https://github.com/nobleo/path_tracking_pid)：基于 ROS 的 PID 路径追踪控制器，支持平滑路径追踪与多种测试用例
  - **最小目标**：使用 DH 参数描述一个 2-DOF 或 6-DOF 机械臂，并实现其正/逆运动学模拟器
  - **进阶目标**：在 Gazebo 中仿真 UR5 机械臂，实现基于 PID 的轨迹跟踪控制，并可视化运动路径
- **延伸**：
  - **项目**：
    - [modulabs/arm-control](https://github.com/modulabs/arm-control)：支持 Elfin 6 机械臂的 ROS 轨迹一体化控制框架，包含多种控制器和 Gazebo 仿真
    - [ferasboulala/five-dof-robot-arm](https://github.com/ferasboulala/five-dof-robot-arm)：使用 ROS + MoveIt! 驱动 5 DOF 机械臂，支持 Gazebo 仿真与 Arduino 物理执行
    - [JZX-MY/psolqr_local_planner](https://github.com/JZX-MY/psolqr_local_planner)：ROS 本地路径规划插件，实现 PSO 优化 + LQR 控制一体设计
    - [itsahmedkhali/MobileRobotEKF-LQR](https://github.com/itsahmedkhali/MobileRobotEKF-LQR)：差分驱动机器人项目，使用EKF 做状态估计，LQR 做控制，并在 Gazebo & ROS 中仿真
  - **工具**：
    - [MATLAB Simulink](https://uk.mathworks.com/products/simulink.html)：用于MPC等复杂控制器的快速原型验证

---

#### 2.5 定位与导航

- **前置要求**：ROS / 基础概率论与线性代数
- **理论**：
  - **基础**：状态估计理论（贝叶斯滤波、卡尔曼滤波、粒子滤波） → 位姿图优化（Pose Graph / Factor Graph） → 图搜索算法（Dijkstra, A*, D* Lite） → 随机采样法（RRT, PRM） → 优化方法（MPC, CHOMP, TEB）
  - **课程**：
    - [MIT 6.141 / UZH V-SLAM 公开课](https://www.youtube.com/playlist?list=PLUl4u3cNGP63EdVPNLG3ToM6LaEUuStEY)：提供SLAM的系统性理论讲解
    - [Stanford CS237A (Autonomous Driving)](https://bulletin.stanford.edu/courses/2185453)：涵盖路径规划的基础理论与应用
- **实践**：
  - **工具**：
    - [Cartographer ROS](https://github.com/cartographer-project/cartographer_ros)：Google 出品的 2D/3D 激光 SLAM 框架，支持 TurtleBot2 等平台
    - [MoveIt + OMPL](https://github.com/ros-planning/moveit_tutorials)：用于机械臂高维空间路径规划
    - [LVI-SAM](https://github.com/TixiaoShan/LVI-SAM)：激光+视觉+IMU 的 SLAM 系统
    - [teb_local_planner](https://github.com/rst-tu-dortmund/teb_local_planner)：基于最优控制的局部路径规划器，常用于 ROS 导航
  - **最小目标**：使用 Cartographer 搭建 TurtleBot 2D 激光 SLAM 导航系统；使用 OMPL 创建高维路径规划任务
  - **进阶目标**：用 LVI-SAM +TEB 在非结构化环境中实现实时导航
- **延伸**：
  - **项目**：
    - [VINS-Fusion](https://github.com/HKUST-Aerial-Robotics/VINS-Fusion)：清华出品的多传感器融合SLAM系统，支持双目、IMU、GPS
    - [DSO (Direct Sparse Odometry)](https://github.com/JakobEngel/dso)：直接法视觉里程计，适用于特征点稀疏场景
    - [VINS-Mono](https://github.com/HKUST-Aerial-Robotics/VINS-Mono)：单目+IMU的滑动窗口优化实现
    - [Multi-Robot Exploration](https://github.com/hrnr/m-explore)：多机器人协作探索与地图共享系统
  - **工具**：
    - [OMPL](https://ompl.kavrakilab.org/)：开源运动规划库，提供多种采样规划算法

---

#### 2.6 力控与触觉

- **前置要求**：ROS / 基础力学与控制理论
- **理论**：
  - **基础**：刚体动力学与逆动力学 → 力-位置控制（Hybrid Control） → 阻抗控制（Impedance Control） → 导纳控制（Admittance Control） → 优化控制 + MPC → 触觉传感器类型 → 触觉信号处理
  - **课程**：
    - 《现代机器人学》：强烈推荐第6章"力/力矩传感"，涵盖力控核心理论
    - MIT 6.141 Robotics：包含力控基础，适合系统性学习
- **实践**：
  - **工具**：
    - [Gazebo](https://gazebosim.org/home)：真实物理模拟环境
    - [Isaac Sim](https://developer.nvidia.com/isaac/sim)：NVIDIA 基于其 Omniverse 平台构建的开源机器人仿真工具
  - **最小目标**：在 Gazebo 中安装 `ros_control` 并配置一个六维力/力矩传感器插件（ForceTorqueSensor），实现简单的阻抗控制
  - **进阶目标**：使用 Isaac Sim 搭建一个触觉反馈环境，训练一个基于触觉信号的抓取策略
- **延伸**：
  - [Feel the Force (FTF)](https://feel-the-force-ftf.github.io)：从人类示范中学习力敏感操作的开源项目，结合力控与学习算法
  - [HATPIC](https://arxiv.org/abs/2502.17362)：开源单轴触觉操纵杆，用于远程操作与力反馈实验
  - ["Dexterous Manipulation through Imitation Learning: A Survey"](https://arxiv.org/html/2504.03515v3)：关于灵巧操作的综述论文

---

#### 2.7 VLA

- **前置要求**：Transformer / CLIP / SigLIP / 模仿学习
- **理论**：
  - **基础**：Isaac 与 RoboMimic 使用 → Diffusion / Flow Matching 生成策略 → OpenVLA
  - **材料**：
    - [Isaac Lab 中文文档](https://docs.omniverse.nvidia.com/isaacsim/latest/)：学习任务定义、环境创建与操作演示
    - [Diffusion Policy](https://github.com/real-stanford/diffusion_policy)：基于扩散模型的策略学习方法
    - [3D Diffusion Policy (DP3)](https://github.com/YanjieZe/3D-Diffusion-Policy)：将3D视觉表示与扩散策略相结合
    - [OpenVLA](https://github.com/OpenVLA/OpenVLA)：开源通用 VLA 模型，基于 SigLIP+DINOV2 视觉编码器和 Llama 2-7B 语言模型
- **实践**：
  - **工具**：
    - [Isaac Sim](https://developer.nvidia.com/isaac-sim)：机器人三维仿真平台
    - [Isaac Lab](https://github.com/NVIDIA-Omniverse/IsaacLab.git)：用于任务定义和训练的框架
  - **最小目标**：使用 OpenVLA 为基础构建多任务环境（pick-place、开关抽屉、积木等），融合多模态输入
  - **进阶目标**：搭建 ROS2 + Isaac Sim/Real Franka 桥接环境，实现 camera calibration + 实时 image embedding
- **延伸**：
  - **项目**：
    - [ALOHA / ACT](https://github.com/tonyzhaozh/aloha)：低成本双臂机器人系统与配套的动作分块策略
    - [RT-1](https://github.com/google-research/robotics_transformer)：Google 提出的 Transformer 模型
    - [RDT-1B](https://github.com/thu-ml/RoboticsDiffusionTransformer)：清华大学发布的 12 亿参数扩散基础模型
    - [n0 (Pi-0)](https://github.com/Physical-Intelligence/openpi)：VLA 流匹配模型
    - [DexVLA](https://github.com/juruobenruo/DexVLA)：Cornell 大学提出的 VLA模型
  - **工具**：
    - [Hugging Face Transformers](https://huggingface.co/)：用于加载和微调大型视觉-语言模型
    - [RoboMimic](https://github.com/ARISE-Initiative/robomimic.git)：模仿学习库

---

#### 2.8 Sim2Real

- **前置要求**：ROS / 强化学习
- **理论**：
  - **基础**：主流仿真环境（MuJoCo, Isaac Gym, Isaac Sim, PyBullet） → Sim2Sim → 域适应 → 域随机化 → 增量网络 → 逆动力学模型
  - **材料**：
    - [MuJoCo](https://github.com/google-deepmind/mujoco)、[Isaac Gym](https://developer.nvidia.com/isaac-gym)、[PyBullet](https://github.com/bulletphysics/bullet3)
    - [Tzeng等人 (2015) - Domain Adaptation](https://arxiv.org/abs/1505.07683)
    - [Gupta等人 (2017) - DTW](https://arxiv.org/abs/1703.06891)
    - [Rusu等人 (2016) - Progressive Nets](https://arxiv.org/abs/1608.07243)
    - [Peng等人 (2018) - Dynamics Randomization](https://arxiv.org/abs/1803.07070)
    - [Tobin等人 (2017) - 视觉领域随机化](https://arxiv.org/abs/1703.06891)
- **实践**：
  - **工具**：
    - [SplitNet](https://grail.cs.washington.edu/projects/splitnet/)
    - [NVlabs/handover-sim2real](https://github.com/NVlabs/handover-sim2real)
    - [facebookresearch/spot-sim2real](https://github.com/facebookresearch/spot-sim2real)
    - [UT-Austin-RobIn/lang4sim2real](https://github.com/UT-Austin-RobIn/lang4sim2real)
  - **最小目标**：安装 Habitat + SplitNet，测试 sim-to-sim performance
  - **进阶目标**：运行任意 Sim2Real demo，插入 Domain Randomization、逆动力模型或语言提示
- **延伸**：
  - [Unitree RL GYM](https://github.com/unitreerobotics/unitree_rl_gym)
  - [Humanoid-Gym](https://github.com/roboterax/humanoid-gym)

---

#### 2.9 世界模型

- **前置要求**：强化学习 / 概率建模 / 变分自编码器（VAE）
- **理论**：
  - **基础**：潜在动力学建模 → 世界模型 → Dreamer → DreamerV2 → DreamerV3 → MBRL
  - **材料**：
    - [World Models (Ha & Schmidhuber, 2018)](https://arxiv.org/abs/1803.10122)
    - [DreamerV2 (Hafner et al., 2021)](https://arxiv.org/abs/2010.02193)
    - [DreamerV3 (Hafner et al., 2023)](https://arxiv.org/abs/2301.04104)
    - [PlaNet (Hafner et al., 2019)](https://arxiv.org/abs/1811.04551)
- **实践**：
  - **工具**：
    - [DreamerV3 Official Implementation](https://github.com/danijar/dreamerv3)
    - [gymnax](https://github.com/RobertTLange/gymnax)
  - **最小目标**：使用 Dreamer 复现 CartPole / Cheetah 环境中的潜在动力学预测
  - **进阶目标**：结合 PyBullet 或 Isaac Gym 训练机械臂模型的世界模型
- **延伸**：
  - [DreamerV3 Robotics](https://github.com/DreamerV3Robotics)
  - [WM-PG](https://github.com/icoz69/WM-PG)
  - [MIRAGE](https://github.com/robustrobotics/MIRAGE)
  - [BraX](https://github.com/google/brax)

---

#### 2.10 数据飞轮与遥操作

- **前置要求**：强化学习 / 模仿学习 / 数据工程基础
- **理论**：
  - **基础**：数据飞轮与遥操作概念 → 力反馈遥操作 → AR/VR 远程控制 → 模型辅助示教
  - **材料**：
    - [Tele-operation & Flywheel](https://medium.com/@chaseyvy/teleoperation-the-human-link-and-flywheel-of-physical-ai-1c5b82ba1c80)
    - [PATO](https://arxiv.org/abs/2212.04708)
    - [Open-TeleVision](https://arxiv.org/html/2407.01512v2)
- **实践**：
  - **工具**：
    - [ALOHA](https://github.com/tonyzhaozh/aloha)
    - [Open-TeleVision](https://github.com/OpenTeleVision/TeleVision)
  - **最小目标**：使用 ALOHA 采集单任务数据 → 训练 BC 策略 → 部署并采集新演示
  - **进阶目标**：构建完整数据飞轮管线
- **延伸**：
  - [SharedAssembly](https://arxiv.org/abs/2503.12287)
  - [Super-Linear Scaling](https://arxiv.org/html/2412.01770v3)
  - [DexFlyWheel](https://arxiv.org/html/2509.23829v1)

---

[← 返回主 README](../../README.md)
