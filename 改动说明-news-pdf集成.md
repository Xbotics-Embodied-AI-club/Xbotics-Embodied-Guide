# News PDF 集成与提交范围改动说明

## 改动了什么

- **news-pdf-integration Skill**：补充 Step 0（PDF 先重命名为英文防乱码）、源文件归档至 `files/source/`、原文链接指向 `../source/` 等约定；明确执行完成后将 PDF 移至 `files/source/` 并保持英文文件名。
- **files/source/**：新增目录，用于归档已处理的 PDF（如 `1X-interview-world-models-evaluation.pdf`、`isaac-lab-rl-practice.pdf`）。
- **files/interviews/**：新增 1X 对谈原创笔记，并已链至 `files/source/` 下 PDF。
- **files/foundations/**：新增 Isaac Lab RL 实战笔记，并已链至 `files/source/` 下 PDF。
- **docs**：在 8-people 增加「访谈与对谈」表并链至笔记；在 1.3 世界模型综述末增加「产业视角」延伸链接；在 3-foundations README 增加 Isaac Lab 实战延伸链接。
- **.gitignore**：新增 `news/`，使 `news/` 下 PDF 与提取文本仅保留在本地，不随仓库上传。

## 有什么用

- 源 PDF 统一归档在 `files/source/`，笔记与原文链接清晰、移动后无乱码（英文文件名）。
- 产业访谈与基础教程有对应笔记与 docs 入口，便于查阅与延伸阅读。
- `news/` 不提交可避免大文件与本地资料进入仓库，只上传整理后的笔记与规范。

本文档记录本次改动与目的，便于后续查阅。
