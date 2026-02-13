# VAM 视频动作模型 6 篇综述索引

*技术综述：VLA 后新趋势，Video Action Model / World Action Model。*

**完整整理稿**（仅保留核心内容）：[vam-video-action-model-survey-2026.md](../source/vam-video-action-model-survey-2026.md)

---

## 要点

- **范式**：2025 底–2026 初兴起，用视频生成模型做机器人控制；符合「预训练第二种范式」next physical state prediction，对机器人动作数据需求通常低于 VLA。
- **两流派**：① 先想象再模仿（LVP、1XWM）；② 借用大脑/联合生成（Video Policy、mimic-video、Cosmos Policy、DreamZero）。六篇：Video Policy、LVP、mimic-video、1XWM、Cosmos Policy、DreamZero。
- **对比**：从视频到动作——LVP 用固定算法（3D 重建+重定向），其余为学习（IDM 或特征解码）；数据需求从少（50 demos / training-free）到多（1XWM/Cosmos）不等；DreamZero 14B、7Hz 实时，强调多样性数据。
- **局限**：算力与实时性要求高；视频模型是否真正学到物理规律仍待 scaling / 涌现与视频思维链等方向验证。

---

*—— 供 docs/5-sota、1.3 世界模型综述延伸用*
