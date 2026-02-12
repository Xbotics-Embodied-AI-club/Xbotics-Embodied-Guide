---
name: news-pdf-integration
description: Integrate PDF content from news/ (papers, interviews, foundations) into Xbotics-Embodied-Guide. Use when the user adds PDFs to news/, wants to incorporate news content into the project, or asks about integrating papers, interviews, or foundational materials.
---

# News PDF 内容集成流程

将 `news/` 下的 PDF（论文、访谈、基础类资料）**仅提取文字**并集成到项目中。**必须生成原创整理内容**，避免侵权；不直接复制原文。**不处理图片**。

---

## 一、内容类型与集成目标

| 类型 | 示例 | 主要集成位置 |
|------|------|--------------|
| **论文** (论文) | 世界模型、VLA、Diffusion Policy 等论文 | docs/1-embodied-overview、docs/5-sota、docs/4-classical、docs/2-roadmaps |
| **访谈** (访谈) | 1X、公司、人物对谈 | docs/8-people、docs/9-landscape、docs/1-embodied-overview（产业视角） |
| **基础类** (基础) | 教程、入门材料 | docs/3-foundations、docs/2-roadmaps |

---

## 二、目录与文件规范

**路径约定**：假定项目根下 `files/` 与 `news/` 同级；从 `files/papers/` 或 `files/interviews/` 到 `news/` 的相对路径为 `../../news/`。

**主题约定**：主题优先用 PDF 文件名（去掉 `.pdf`），或人工指定简短英文/拼音标识；多 PDF 聚合时的主题简写由人工定名。输出目录（如 `files/papers/`、`files/interviews/`）若不存在则按所选方案创建。

### 1. 源文件位置

- PDF 放在 `news/` 下。**开始时先将 PDF 与后续生成的 `-提取.txt` 重命名为英文**（如 `1X-interview-world-models.pdf`、`isaac-lab-rl-practice-extract.txt`），避免移动或跨环境后出现乱码；可用拼音或主题简写。
- **执行完成后**：将已处理过的 PDF 移至 `files/source/` 下归档（保持英文文件名）；原创整理文档中的**原文链接**指向 `../source/英文文件名.pdf`（从 `files/papers/`、`files/interviews/`、`files/foundations/` 出发）。
- 同主题索引：`news/<主题简写>-整理.md`（可选，用于多 PDF 聚合；多 PDF 聚合本期不展开，仅保留索引文件约定）

### 2. 原创整理文档（按内容类型选目录）

按类型选择输出目录，文件名：`<主题>-笔记.md` 或 `<主题>-整理.md`。**格式**：Markdown；**必须包含**：标题、原文链接（指向 `news/` 下 PDF，执行完成后改为指向 `files/source/` 下 PDF）、原创整理正文。

| 内容类型 | 推荐路径（任选一种方案） | 说明 |
|----------|--------------------------|------|
| **论文** | `files/papers/` | 论文笔记、SOTA/经典方法整理（与 docs/4-classical、5-sota 对应） |
| **访谈/对谈** | `files/interviews/` | 人物访谈、公司对谈（与 docs/8-people、9-landscape 对应） |
| **基础/教程** | `files/foundations/` | 入门、教程类（与 docs/3-foundations、2-roadmaps 对应；工程已有此目录） |

**可选方案**（与工程现有结构兼容）：

- **方案 A（推荐）**：按类型分顶层目录  
  - 论文 → `files/papers/`  
  - 访谈 → `files/interviews/`  
  - 基础 → `files/foundations/`（已有）
- **方案 B**：保留待定。

- **方案 C**：与 docs 命名风格一致  
  - 论文 → `files/paper/`  
  - 访谈 → `files/people/` 或 `files/talks/`（对应 docs/8-people）  
  - 基础 → `files/foundations/`

---

## 三、原创整理文档模板

```markdown
# [主题名称]

*基于 [原文标题] 的整理与延伸*

**原文链接**：[原文标题](../source/原文文件名.pdf)（PDF，X 页）  
（执行完成后 PDF 归档在 `files/source/`，从 `files/papers/`、`files/interviews/`、`files/foundations/` 出发用 `../source/`）

---

[原创整理内容，非原文摘录。按主题分节撰写。]

---

*—— 整理自 Xbotics 具身智能学习指南 | 供学习参考*
```

**要点**：

- 正文为**原创归纳**：提炼观点、方法论、术语，用自己的话重写
- 不逐段抄录原文，避免版权问题
- 原文链接使用相对路径：执行完成后 PDF 在 `files/source/`，用 `../source/xxx.pdf`（从 `files/papers/`、`files/interviews/`、`files/foundations/` 出发）；执行前可临时用 `../../news/xxx.pdf`

---

## 四、实施步骤

### Step 0：将 news/ 下 PDF 重命名为英文（必做）

为避免移动或跨环境后出现乱码，**在提取与归档前**将 `news/` 下的 PDF 重命名为英文（或拼音/主题简写），例如：`对谈1X 模型评估...pdf` → `1X-interview-world-models-evaluation.pdf`，`Isaac Lab 机器人强化学习...pdf` → `isaac-lab-rl-practice.pdf`。后续生成的 `-提取.txt` 也使用同一英文前缀（如 `1X-interview-world-models-evaluation-extract.txt`）。

### Step 1：提取 PDF 文字

若仓库中无 `news/extract_pdf.py`，则先创建最小可用脚本：支持单 PDF 路径参数（如 `python news/extract_pdf.py "news/xxx.pdf"`），仅输出文本到 `news/<英文主题>-extract.txt`，再执行下述步骤。

运行或改造 `news/extract_pdf.py`，**仅提取文本**（不提取图片）：

```python
# 修改 PDF_NAME、输出路径后运行
python news/extract_pdf.py
```

- 文本输出：`news/<英文主题>-extract.txt`（或 `-提取.txt`，建议统一用英文避免乱码）
- 若文本为 0 字符，说明 PDF 可能为扫描件。**本流程不包含 OCR**，扫描件请先自行 OCR 或手动整理后再放入 `news/` 或跳过该 PDF。

### Step 2：创建原创整理文档

1. 按内容类型选择目录（见上文「2. 原创整理文档」）：
   - **论文** → `files/papers/`（或所选方案中的论文目录）
   - **访谈** → `files/interviews/`
   - **基础** → `files/foundations/`
2. 在该目录下新建 `xxx-笔记.md` 或 `xxx-整理.md`
3. 按模板填写标题、原文链接
4. 根据提取文本或主题，撰写**原创**分节内容

### Step 3：在 docs 中建立链接

按内容类型选择目标：

| 类型 | 目标文件 | 更新方式 |
|------|----------|----------|
| 论文 | docs/1-embodied-overview、5-sota、4-classical | 在相关小节末增加「延伸」「参考」链接 |
| 访谈 | docs/8-people（对谈表 + 人物条目）、docs/9-landscape（公司条目） | 增加对谈/笔记链接 |
| 访谈-世界模型 | docs/1-embodied-overview/1.3-世界模型综述.md | 增加「产业视角」小节 |
| 基础 | docs/3-foundations、docs/2-roadmaps | 在对应路线「延伸」或子节中增加链接 |

**相关小节**由内容类型与关键词匹配决定：论文看 1.3/4.x/5.x/2.x 目录与标题，访谈看 8-people、9-landscape、1.3 产业视角，基础看 3-foundations、2-roadmaps；不确定时在对应章末 README 或最接近的节末加链接。

### Step 4：更新 news 索引（可选）

若存在 `news/<主题>-整理.md`，在其中加入对 `files/papers/`、`files/interviews/` 或 `files/foundations/` 下对应原创笔记的链接。

### Step 5：归档源 PDF 至 files/source（执行完成后）

1. 将本流程已处理过的 PDF 从 `news/` 移至 `files/source/`，**保持英文文件名**（若 Step 0 已重命名则无需再改）。
2. 更新对应原创整理文档（`files/papers/`、`files/interviews/`、`files/foundations/` 下的笔记）中的**原文链接**：由 `../../news/xxx.pdf` 改为 `../source/英文文件名.pdf`。
3. `news/` 下可保留 `-提取.txt` 供后续查阅，或按需清理。

---

## 五、集成位置速查

```
docs/
├── 1-embodied-overview/   # 术语、操作、世界模型、运控、导航
├── 2-roadmaps/            # 各技术学习路线（2.1–2.10）
├── 3-foundations/         # 机器人学、Transformer、Diffusion 等
├── 4-classical/           # 模仿学习、RL、视觉、轨迹优化
├── 5-sota/                # VLA、Diffusion Policy、Sim2Real、SFT
├── 6-simulation/          # Isaac Lab、MuJoCo 等
├── 7-real-robots/         # LeRobot 等
├── 8-people/              # 人物名录 + 对谈/访谈区
└── 9-landscape/           # 公司图谱（如 1X 等）
```

- **论文**：优先 1.3 世界模型、5.x 前沿、4.x 经典、2.x 路线延伸
- **访谈**：8-people 对谈表、9-landscape 公司条目、1.3 产业视角
- **基础**：3-foundations、2-roadmaps 延伸

---

## 六、参考示例

以下为路径与命名示例，无需与仓库内已有文件一致。

- **论文**：`files/papers/xxx-笔记.md` → 链到 docs/5-sota、4-classical 等
- **访谈**：`files/interviews/1X对谈-世界模型与模型评估笔记.md`（或 `files/people/`、`files/talks/` 视所选方案而定）
- **链接**：`docs/1-embodied-overview/1.3-世界模型综述.md`（1.3.7 产业视角）、`docs/8-people/README.md`（对谈表、Bernt Børnich）、`docs/9-landscape/README.md`（1X 条目）、`docs/2-roadmaps/README.md`（2.9 延伸）

---

## 七、提取脚本通用化

若不存在 `news/extract_pdf.py`，见 Step 1：先创建再使用。已有脚本时，`news/extract_pdf.py` 可能写死单个 PDF。新增 PDF 时：

1. 将 `PDF_NAME` 改为新文件名，或
2. 改为支持命令行参数：`python news/extract_pdf.py "news/新文件.pdf"`
3. 输出路径中的前缀（如 `对谈1X`）改为与主题一致的标识

**约定**：本流程仅做文字提取，脚本中若有图片导出逻辑可移除或关闭，以保持「只提取相关文字」的流程一致。
