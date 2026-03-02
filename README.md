<div align="center">

  <pre style="font-family: 'Courier New', monospace; font-size: 14px; color: #1a1a2e; margin: 0; padding: 0; line-height: 1.2;">
  ██╗  ██╗██████╗  ██████╗ ████████╗██╗ ██████╗███████╗
  ╚██╗██╔╝██╔══██╗██╔═══██╗╚══██╔══╝██║██╔════╝██╔════╝
   ╚███╔╝ ██████╔╝██║   ██║   ██║   ██║██║     ███████╗
   ██╔██╗ ██╔══██╗██║   ██║   ██║   ██║██║     ╚════██║
  ██╔╝ ██╗██████╔╝╚██████╔╝   ██║   ██║╚██████╗███████║
  ╚═╝  ╚═╝╚═════╝  ╚═════╝    ╚═╝   ╚═╝ ╚═════╝╚══════╝
  </pre>

  # Xbotics : Roadmap to Embodied AI

  <p align="center">
    <em>更偏重机器人基础学习与开源项目实践 · 路线 + 资源导航，助你快速定位路径、落地项目与参与开源</em>
  </p>

  <p align="center">
    📌 <a href="#quick-start">快速开始 (Quick Start)</a> · ✨ <a href="#learning-map">学习地图 (Learning Map)</a> · 🤝 <a href="docs/10-contributing/README.md">如何贡献 (Contributing)</a>
  </p>

  <p align="center">
    <a href="https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide" target="_blank">
      <img src="https://img.shields.io/github/stars/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide?color=0052cc&style=for-the-badge&logo=star&logoColor=white&labelColor=1a1a2e" alt="Stars"></a>
    <a href="https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide/network/members" target="_blank">
      <img src="https://img.shields.io/github/forks/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide?color=0052cc&style=for-the-badge&logo=git-fork&logoColor=white&labelColor=1a1a2e" alt="Forks"></a>
    <a href="LICENSE" target="_blank">
      <img src="https://img.shields.io/badge/License-CC--BY%204.0-4ecdc4?style=for-the-badge&logo=creative-commons&logoColor=white&labelColor=1a1a2e" alt="License"></a>
    <img src="https://api.visitorbadge.io/api/visitors?path=Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide&label=visitors&countColor=%23263759&style=flat" alt="Visitors">
  </p>

</div>

---

Xbotics 社区具身智能学习指南：我们把 **「具身综述 → 学习路线 → 仿真学习 → 开源实物 → 人物与公司图谱」** 串起来，帮助新手和实战者快速定位路径、落地项目与参与开源。面向「**机器人基础学习 + 开源项目学习**」，强调可复现与快速上手；不追求百科全书，而是 **清晰路径 + 工程落地**。

<span id="quick-start"></span>
## 🚀 快速开始 (Quick Start)：三步上手本指南

本仓库以**文档与路线**为主，无需运行脚本即可开始学习。推荐三步：

```bash
# 1. 克隆仓库
git clone https://github.com/Xbotics-Embodied-AI-club/Xbotics-Embodied-Guide.git
cd Xbotics-Embodied-Guide
```

2. **打开文档**：从 [1. 具身综述](docs/1-embodied-overview/README.md) 建立大图景，再在 [2. 学习路线](docs/2-roadmaps/README.md) 中选一条 4–8 周路线（RL / IL / 3D 视觉 / VLA / 仿真等）。
3. **动手与反馈**：按路线实作；遇到问题在仓库 **提 Issue**（AMA），或参与贡献（见 [如何贡献](docs/10-contributing/README.md)）。

![Roadmap](https://github.com/user-attachments/assets/054c89b9-d114-4477-b751-a01f2e7a6376)

---

<table align="center">
  <tr>
    <td width="33%" valign="top" align="center">
      <strong><a href="docs/1-embodied-overview/README.md">具身综述</a></strong>
      <br><sub>术语、操作/世界模型/运控/导航全景</sub>
    </td>
    <td width="33%" valign="top" align="center">
      <strong><a href="docs/2-roadmaps/README.md">学习路线</a></strong>
      <br><sub>RL、IL、3D 视觉、VLA、Sim2Real 等 10 条 4–8 周路线</sub>
    </td>
    <td width="33%" valign="top" align="center">
      <strong><a href="docs/6-simulation/README.md">仿真学习</a></strong>
      <br><sub>Isaac Lab、MuJoCo、PyBullet、Genesis、Gazebo</sub>
    </td>
  </tr>
  <tr>
    <td width="33%" valign="top" align="center">
      <strong><a href="docs/7-real-robots/README.md">开源实物</a></strong>
      <br><sub>LeRobot（HF）预训练、数据集、Sim2Real</sub>
    </td>
    <td width="33%" valign="top" align="center">
      <strong><a href="docs/5-sota/README.md">前沿技术</a></strong>
      <br><sub>VLA、Diffusion Policy、Sim2Real、大模型 SFT</sub>
    </td>
    <td width="33%" valign="top" align="center">
      <strong><a href="docs/8-people/README.md">人物</a> · <a href="docs/9-landscape/README.md">公司图谱</a></strong>
      <br><sub>学术界/产业界人物；硬件与算法生态</sub>
    </td>
  </tr>
</table>

<div align="center">
  <p><strong>⭐ 欢迎 Star，一起构建具身智能学习生态</strong></p>
</div>

---

## 项目理念

- **入门友好**：路线清晰，每节优先给出「起步三件事」，不要求一开始就啃长篇教程。
- **实践导向**：以「路线 + 清单 + 实作任务」组织，强调开源项目与可复现。
- **前沿连接**：从综述、经典算法到 VLA / Diffusion Policy / Sim2Real，与人物、公司图谱衔接。

## 项目受众

- **Python / 控制基础学习者**：希望系统进入具身智能与机器人方向。
- **高校学生与研究生**：需要课程项目、毕设或论文复现的路线与资源。
- **算法与机器人工程师**：希望把视觉、RL、大模型迁移到具身与真实硬件。
- **硬件与开源社区参与者**：关心从仿真到实物、从数据到部署的完整链路。

---

<span id="learning-map"></span>
## 🗺️ 学习地图 (Learning Map)

| 章节 | 关键内容 | 链接 |
| :--- | :--- | :--- |
| **1. 具身综述** | 术语速览、操作/世界模型/运控/导航综述；感知—决策—控制全景 | [📖 阅读](docs/1-embodied-overview/README.md) |
| **2. 学习路线** | RL、IL、3D 视觉、规划控制、定位导航、触觉、VLA、Sim2Real、世界模型、数据飞轮等 10 条路线；前置→4–8 周计划→里程碑→验收 | [📖 阅读](docs/2-roadmaps/README.md) |
| **3. 基础学习** | 机器人学、Transformer、Diffusion、工程环境；坐标系→运动学→深度学习→多模态 | [📖 阅读](docs/3-foundations/README.md) |
| **4. 技术基础与经典** | BC/DAgger/GAIL、值函数/策略/Actor-Critic、SigLIP/CLIP、iLQR/MPPI/MPC；经典算法与理论 | [📖 阅读](docs/4-classical/README.md) |
| **5. 前沿技术** | VLA、Diffusion Policy、Sim2Real、大模型 SFT；2023–2025 最新进展与评测 | [📖 阅读](docs/5-sota/README.md) |
| **6. 仿真学习** | Isaac Lab、MuJoCo、PyBullet、Genesis、Gazebo；虚拟环境搭建与模型训练 | [📖 阅读](docs/6-simulation/README.md) |
| **7. 开源实物** | LeRobot（HF 框架）；预训练模型、数据集、硬件支持、Sim2Real 落地 | [📖 阅读](docs/7-real-robots/README.md) |
| **8. 人物** | 学术界与产业界核心人物名录；操作、人形、VLA 领域约 120 人 | [📖 阅读](docs/8-people/README.md) |
| **9. 公司图谱** | 硬件整机、关键部件、算法平台、数据服务；人形/四足/移动+操作 | [📖 阅读](docs/9-landscape/README.md) |
| **10–11. AMA & 贡献** | 提 Issue 提问、PR 规则、目录约定、如何贡献、License | [📖 阅读](docs/10-contributing/README.md) |

---

## 使用说明

- **定位**：面向新人、进阶与工程落地；以「路线 + 清单 + 实作任务」组织，而非长篇教程。
- **风格**：中文为主、英文补充；强调开源项目与可复现。
- **先修建议**：Python / 线性代数 / 概率统计 / 控制基础 / Linux & Git。
- **图标约定**：⭐ 必看 · 🧪 实作 · 🧱 SOP · 📦 代码/数据 · 📄 论文 · 🎥 视频（可选）。
- **结构**：每个小节优先给出可操作的「起步三件事」。

---

## 🔥 News & 最近更新

- **[2026-03-02]** [新闻源整理（source.docx）](改动说明-新闻源整理source-docx-20260302.md)：基于 ArXiv 机器人学每日速递的 21 篇整理稿及源文件入库。
- 文档持续更新，欢迎 Star 与 PR；更多更新见 [如何贡献](docs/10-contributing/README.md) 与仓库 Issue。

---

## 🤝 参与贡献

我们欢迎社区的贡献：无论是修复 typo、补充文档、还是提交新的路线与复现笔记。

- **参与方式**：见 [如何贡献 & 目录约定](docs/10-contributing/README.md#11-如何贡献--目录约定)（PR 规则、目录结构、提交检查清单）。

### 贡献者名单

| 贡献者 | 说明 |
| :--- | :--- |
| @Xbotics-木木 | 核心维护 |
| @Xbotics-土豆 | 核心维护 |
| @FTZP | 贡献者 |
| @KandS | 贡献者（含学习路线等） |
| @maomao725 | 贡献者 |

感谢所有参与文档、路线与资源整理的小伙伴。🎯 想加入？见 [如何贡献](docs/10-contributing/README.md#11-如何贡献--目录约定)。

---

## 📬 联系我们

- 在本仓库 **提 Issue** 提问（学习/复现/工程落地/选型均可），使用「AMA 问答」模板。
- 参与 PR、一起完善路线与文档：**加入 Xbot 社区，一起探索具身智能的未来。** 详见 [10. Ask Me Anything & 贡献](docs/10-contributing/README.md)。

---

## 📄 License

<div align="center">
  <a rel="license" href="https://creativecommons.org/licenses/by/4.0/">
    <img alt="CC BY 4.0 License" style="border-width:0" src="https://img.shields.io/badge/license-CC--BY%204.0-lightgrey" />
  </a>
  <br />
  本项目文档与教程内容采用 <strong>Creative Commons Attribution 4.0 International (CC BY 4.0)</strong> 许可协议。
  <br />
  你可以自由分享与改编本项目内容，但需保留来源署名。详细条款见 <a href="LICENSE">LICENSE</a>。
</div>
