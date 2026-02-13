# HumanX：从人体视频学习人-物交互（王荫槐访谈）摘要

*学术访谈：HOI 模仿、HumanX 系列（PhysHOI → Skillmimic → HOT → HumanX）。*

**完整整理稿**（仅保留核心内容）：[humanx-hoi-interview-2026.md](../source/humanx-hoi-interview-2026.md)

---

## 要点

- **核心路线**：把模仿从「只模仿身体」扩展到「模仿人与物体交互」（HOI）；learn from human video + 仿真强化学习，数据需求远低于 behavior cloning；自 2023 年 PhysHOI 起持续做 HOI imitation。
- **系列工作**：PhysHOI（概念）→ Skillmimic（动捕高质量 HOI、技能切换）→ Skillmimic-V2（单条鲁棒、数据增强）→ HOT/V3（纯合成数据、通用交互 controller）→ HumanX（XGen 半合成 + XMimic 学习）。
- **与 WBC 区别**：原生交互，不需先训全身控制器；约束相对运动与接触（contact graph），避免「模仿身体+物体轨迹」的局部最优。
- **数据与泛化**：半合成避开设 retargeting，一条 video 合成多变化；单条数据下相对运动学得好即可小范围泛化；动捕可用于感知或高质量锚点，约 100 条即可能多技能演示。项目页：https://wyhuai.github.io/human-x/

---

*—— 供 docs/8-people、1.3 产业/学术视角延伸用*
