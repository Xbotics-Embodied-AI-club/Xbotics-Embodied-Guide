---
name: news-pdf-integration
description: Integrate PDF content from news/ (papers, interviews, foundations) into Xbotics-Embodied-Guide. Use when the user adds PDFs to news/, wants to incorporate news content into the project, or asks about integrating papers, interviews, or foundational materials.
---

# News PDF 内容集成流程

将 `news/` 下的 PDF（论文、访谈、基础类资料）提取并集成到项目中。**必须生成原创整理内容**，避免侵权；不直接复制原文。

---

## 一、内容类型与集成目标

| 类型 | 示例 | 主要集成位置 |
|------|------|--------------|
| **论文** (论文) | 世界模型、VLA、Diffusion Policy 等论文 | docs/1-embodied-overview、docs/5-sota、docs/4-classical、docs/2-roadmaps |
| **访谈** (访谈) | 1X、公司、人物对谈 | docs/8-people、docs/9-landscape、docs/1-embodied-overview（产业视角） |
| **基础类** (基础) | 教程、入门材料 | docs/3-foundations、docs/2-roadmaps |

---

## 二、目录与文件规范

### 1. 源文件位置

- PDF 放在 `news/` 下，文件名保持原样（可含中文）
- 同主题索引：`news/<主题简写>-整理.md`（可选，用于多 PDF 聚合）

### 2. 原创整理文档（按内容类型选目录）

按类型选择输出目录，文件名：`<主题>-笔记.md` 或 `<主题>-整理.md`。**格式**：Markdown；**必须包含**：标题、原文链接（指向 `news/` 下 PDF）、原创整理正文。

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

- **方案 B**：统一在 `files/news/` 下分子目录  
  - 论文 → `files/news/papers/`  
  - 访谈 → `files/news/interviews/`  
  - 基础 → `files/news/foundations/`

- **方案 C**：与 docs 命名风格一致  
  - 论文 → `files/paper/`  
  - 访谈 → `files/people/` 或 `files/talks/`（对应 docs/8-people）  
  - 基础 → `files/foundations/`

### 3. 图片

- 提取的图片放在 `files/images/news/`
- 命名：`<主题>-p{页号}-img{序号}.png`

---

## 三、原创整理文档模板

```markdown
# [主题名称]

*基于 [原文标题] 的整理与延伸*

**原文链接**：[原文标题](../../news/原文文件名.pdf)（PDF，X 页）  
（从 `files/papers/` 或 `files/interviews/` 出发时用 `../../news/`）

---

[原创整理内容，非原文摘录。按主题分节撰写。]

---

*—— 整理自 Xbotics 具身智能学习指南 | 供学习参考*
```

**要点**：

- 正文为**原创归纳**：提炼观点、方法论、术语，用自己的话重写
- 不逐段抄录原文，避免版权问题
- 原文链接使用相对路径：`../../news/xxx.pdf`（从 `files/papers/` 或 `files/interviews/` 出发）；若使用 `files/news/xxx/` 则用 `../../../news/xxx.pdf`

---

## 四、实施步骤

### Step 1：提取 PDF

运行或改造 `news/extract_pdf.py`，支持任意 PDF：

```python
# 修改 PDF_NAME、输出路径后运行
python news/extract_pdf.py
```

- 文本输出：`news/<主题>-提取.txt`
- 图片输出：`files/images/news/<主题>-p*.png`
- 若文本为 0 字符，说明 PDF 可能为扫描件，需 OCR 或手动整理

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

### Step 4：更新 news 索引（可选）

若存在 `news/<主题>-整理.md`，在其中加入对 `files/papers/`、`files/interviews/` 或 `files/foundations/` 下对应原创笔记的链接。

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

- **论文**：`files/papers/xxx-笔记.md` → 链到 docs/5-sota、4-classical 等
- **访谈**：`files/interviews/1X对谈-世界模型与模型评估笔记.md`（或 `files/people/`、`files/talks/` 视所选方案而定）
- **链接**：`docs/1-embodied-overview/1.3-世界模型综述.md`（1.3.7 产业视角）、`docs/8-people/README.md`（对谈表、Bernt Børnich）、`docs/9-landscape/README.md`（1X 条目）、`docs/2-roadmaps/README.md`（2.9 延伸）

---

## 七、提取脚本通用化

`news/extract_pdf.py` 当前写死单个 PDF。新增 PDF 时：

1. 将 `PDF_NAME` 改为新文件名，或
2. 改为支持命令行参数：`python news/extract_pdf.py "news/新文件.pdf"`
3. 输出路径中的前缀（如 `对谈1X`）改为与主题一致的标识
