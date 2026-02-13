# News PDF 集成与 OCR 流程 改动说明

## 改动了什么

- **Skill**：在 `.cursor/skills/news-pdf-integration/SKILL.md` 中增加 **Step 1b 扫描件 OCR**（当文字提取为空时，使用 `news/ocr_pdf.py` 做 EasyOCR 识别）；新增 **「五、对 files/source/ 下已有 PDF 的整理」**，约定对已归档 PDF 补做 OCR 后按正文重写/新建笔记；原「五、六、七」顺延为六、七、八。
- **脚本**：新增 `news/ocr_pdf.py`（PyMuPDF 渲染页面 + EasyOCR 中英文识别，输出 `-ocr.txt`）；保留并沿用 `news/extract_pdf.py`（仅文字提取）。两者均可对 `news/` 或 `files/source/` 下 PDF 执行，OCR 结果建议统一放在 `news/` 下。
- **笔记与链接**：
  - 新增 `files/interviews/PKU-WangHe-team-2025-embodied-roundup-笔记.md`（基于 OCR 的北大王鹤团队 2025 工作盘点整理）。
  - 重写 `files/papers/NVIDIA-CHIP-humanoid-motor-skills-笔记.md`、`files/papers/NVIDIA-30auth-44k-hours-video-dexterous-manipulation-笔记.md`，均以对应 PDF 的 OCR 正文为主做分节归纳。
  - 在 `docs/8-people/README.md` 对谈表增加「北大王鹤团队 2025 年工作盘点」条目；在 `docs/5-sota/README.md`、`docs/1-embodied-overview/1.4-运控综述.md`、`docs/4-classical/README.md` 增加上述论文/报道笔记的延伸链接。
- **目录与归档**：`files/source/`、`files/papers/` 下已有 PDF 与笔记；本次将 news 中的提取与 OCR 脚本纳入版本库（`news/extract_pdf.py`、`news/ocr_pdf.py`），便于复现「提取 → 若为空则 OCR → 按正文整理」的流程。
- **根目录**：删除已过时或重复的根目录说明文件（如原「根目录说明-news-pdf集成.md」「根目录说明-人物README链接与简介.md」），以本次改动说明替代记录。

## 有什么用

- 扫描版 PDF 可走统一 OCR 流程，整理内容以正文为依据，减少「仅标题/主题」的空白笔记。
- 对已归档在 `files/source/` 的 PDF 可批量补 OCR 并重写笔记，与 skill 描述一致，便于协作与后续维护。
- 将 `news/` 下 Python 脚本纳入仓库，任何人拉取后即可在本地对 news 或 source 下 PDF 执行提取与 OCR，不依赖未文档化的本地工具。
- docs 延伸链接集中指向 papers/interviews 下的笔记，便于从综述与人物页跳转到具体整理。

本文档记录本次改动与目的，便于后续查阅。
