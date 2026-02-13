# 小米首代 VLA 大模型 Xiaomi-Robotics-0 索引

*技术/模型发布：双脑 MoT、低延迟、全面开源。*

**完整整理稿**（仅保留核心内容）：[xiaomi-vla-open-source-2026.md](../source/xiaomi-vla-open-source-2026.md)

---

## 要点

- **Xiaomi-Robotics-0**：4.7B 参数，推理延迟约 80ms，30Hz 控制，单卡 RTX 4090 实时；LIBERO / CALVIN / SimplerEnv 等超越约 30 个模型。
- **架构**：VLM「大脑」+ 16 层 DiT「小脑」、Action Chunk、流匹配、KV Cache 复用。
- **训练**：Action Proposal 对齐视觉与动作；两阶段（VLM 协同预训练 + DiT 专项训练）；后训练 Clean Action Prefix + Λ-shape Attention Mask 缓解动作惯性。
- **开源**：全面开源，降低具身 VLA 开发与部署门槛。

---

*—— 供 docs/5-sota、1-embodied-overview 延伸用*
