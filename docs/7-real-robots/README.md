# 7. 开源实物（Real Robots & Tooling）

**贡献者**：@owner

---

### 7.1 LeRobot 简介

**LeRobot** 是 Hugging Face 于 2024 年 5 月发布的开源机器人学习框架，目标是降低 AI 机器人开发门槛。

- **GitHub**: [huggingface/lerobot](https://github.com/huggingface/lerobot) ⭐ 19,000+ (截至 2025 年 10 月)
- **官方页面**: [huggingface.co/lerobot](https://huggingface.co/lerobot)
- **核心特性**: 预训练模型、数据集、硬件支持、Sim2Real

---

### 7.2 快速开始

#### 环境安装

```bash
conda create -n lerobot python=3.10 -y
conda activate lerobot
pip install lerobot

# 或从源码安装
git clone https://github.com/huggingface/lerobot.git
cd lerobot
pip install -e .
```

#### 数据集可视化

```python
from lerobot.common.datasets.lerobot_dataset import LeRobotDataset

dataset = LeRobotDataset("lerobot/pusht")
episode_index = 0
from_idx = dataset.episode_data_index["from"][episode_index].item()
to_idx = dataset.episode_data_index["to"][episode_index].item()

for idx in range(from_idx, to_idx):
    frame = dataset[idx]
    print(f"观测: {frame['observation'].keys()}")
    print(f"动作: {frame['action']}")
```

#### 训练与评估

```bash
# 训练
python lerobot/scripts/train.py \
    policy=diffusion env=pusht \
    dataset_repo_id=lerobot/pusht

# 评估
python lerobot/scripts/eval.py \
    -p outputs/train/diffusion_pusht/checkpoints/last.ckpt \
    eval.n_episodes=10
```

---

### 7.3 硬件平台与数据集

#### 支持的硬件

| 平台 | 自由度 | 特点 |
|------|--------|------|
| **SO-ARM100/SO-101** | 5 DOF | 3D打印、开源 |
| **ALOHA** | 双臂 | 高精度协作 |
| **Moss v1** | 5 DOF | 教学适用 |
| **Koch v1.1** | 5 DOF | Hackathon平台 |

#### 常用数据集

| 数据集 | 任务 | 链接 |
|--------|------|------|
| `lerobot/pusht` | 推方块 | [🔗](https://huggingface.co/datasets/lerobot/pusht) |
| `lerobot/aloha_sim_insertion_human` | ALOHA仿真 | [🔗](https://huggingface.co/datasets/lerobot/aloha_sim_insertion_human) |
| `lerobot/xarm_push_medium` | xArm推物体 | [🔗](https://huggingface.co/datasets/lerobot/xarm_push_medium) |

> 更多: [LeRobot Datasets](https://huggingface.co/lerobot) (160+)

---

### 7.4 学习资源

#### 官方资源
- [LeRobot GitHub](https://github.com/huggingface/lerobot)
- [HIL-SERL 真机训练](https://huggingface.co/docs/lerobot/hilserl)
- [真机上手指南](https://github.com/huggingface/lerobot/tree/main/examples)

#### 中文教程
- [LeRobotTutorial-CN](https://github.com/CSCSX/LeRobotTutorial-CN)
- [CSDN: 源码分析与部署](https://blog.csdn.net/v_JULY_v/article/details/139692392)
- [CSDN: 入门指南](https://blog.csdn.net/lovechris00/article/details/142308934)
- 知乎搜索: "LeRobot" 或 "具身智能"

#### 社区
- Discord: [Hugging Face Discord](https://discord.gg/huggingface) #lerobot
- [GitHub Issues](https://github.com/huggingface/lerobot/issues)
- [Lumina社区](https://lumina-embodied.ai)

#### 核心论文
- **ACT**: [arXiv:2304.13705](https://arxiv.org/abs/2304.13705) - 双臂精细操作
- **Diffusion Policy**: [arXiv:2303.04137](https://arxiv.org/abs/2303.04137) - 复杂轨迹
- **TDMPC**: [arXiv:2203.04955](https://arxiv.org/abs/2203.04955) - 实时控制

---

---
[<- Main](../../README.md)
