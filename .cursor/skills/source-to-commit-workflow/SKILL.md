---
name: source-to-commit-workflow
description: 一键执行「新闻源整理 → 延伸并入正文 → 改动说明与提交」全流程。依次执行 news/source.md 多篇整理到 files/source/、docs 内延伸与参考并入正文、根目录中文改动说明 MD、英文 commit，可选 push。当用户说「一键执行」「三个 skill 一起跑」「全流程」时使用。
---

# 新闻源 + 延伸并入正文 + 提交 一键工作流

按**固定顺序**依次执行三阶段，无需用户分步触发。执行前确认：`news/source.md` 存在且为当前要处理的源；工作区为项目根。

---

## 总览

```
Phase A  新闻源整理     news/source.md → Plan → 逐篇整理 → files/source/*.md → 检查
Phase B  延伸并入正文   扫描 docs 含「延伸与参考」的 MD → 每条入对应小节末 → 删文末块
Phase C  改动说明与提交 写根目录改动说明 MD（中文）→ 英文 commit → 若用户说上传则 push
```

---

## Phase A：新闻源整理（对应 news-pdf-integration）

1. **Plan（必做）**
   - 读取 `news/source.md` 全文。
   - 识别多篇文章边界（主标题、END、下一篇文章标题、留言等为界）。
   - 列出：序号、标题/主题、建议输出文件名 `files/source/<主题简写>.md`。
   - 确认共 N 篇。

2. **逐篇整理**
   - 对每篇：截取该篇正文 → 原创归纳（核心观点、术语、结论、数据），不逐段抄录 → 写入 `files/source/<主题简写>.md`。
   - 单篇结构：标题、整理说明、分节正文、可选「—— 整理自 Xbotics 具身智能学习指南 | 供学习参考」。

3. **检查**
   - 每篇：内容与原文核心一致、无实质遗漏或偏差；主产出均在 `files/source/`。

4. **可选**
   - 若本次新增内容需进文档：在 `files/papers/` 或 `files/interviews/` 做索引/摘要，并在 docs 相应小节加延伸链接（见 news-pdf-integration 第七、八节）。

---

## Phase B：延伸并入正文（对应 docs-extensions-inline）

1. **扫描**
   - 在 `docs/` 下查找含「### 延伸与参考」「### 延伸阅读」「### 参考」的 `.md` 文件。

2. **对每个文件**
   - 列出该块内每条链接及主题。
   - 按主题选定目标小节末尾（概念→核心节末；视频/VAM→视频生成节末；机器人/VLA→机器人节末；产业→应用场景节末）。
   - 在目标小节末插入「**延伸**：[显示文本](路径)（说明）」；删除「### 延伸与参考」到该块最后一条之间的全部内容；保留文末导航。

3. **路径**
   - 相对路径以当前 MD 所在目录为基准（如 `../../files/source/xxx.md`）。

---

## Phase C：改动说明与提交（对应 commit-changelog-workflow）

1. **写改动说明 MD（必须）**
   - 位置：**仓库根目录**，文件名 `改动说明-XXX.md`（如 `改动说明-新闻源整理与文档skill更新.md`）。
   - 语言：中文。
   - 内容须含：
     - **一、知识库新增/更新总览**：表格（类型、名称、路径、说明），覆盖本次 Phase A 新增的 `files/source/*.md`、Phase B 修改的 docs 文件、以及本次若有 Step 3 的 papers/interviews 与 docs 链接。
     - **二、逐条说明**：每条「知识库位置」「内容概要」「链接」（仓库内 GitHub 链接 + 可选外部）。
     - **三、小结**：共新增/修订 X 项。
   - 便于直接摘编为公众号。

2. **提交**
   - `git add`：包含本次改动的所有文件（含新增的 `files/source/*.md`、修改的 docs、根目录 `改动说明-XXX.md`）。若用户明确说「改动说明不上传」，则把该文件名加入 `.gitignore` 且不要 add 该文件。
   - **Commit 信息**：英文，概括本次操作，例如 `docs: source digests, inline extensions, and changelog` 或 `docs: news integration + extensions inline + changelog`。
   - **Push**：仅当用户明确说「上传」「push」时执行 `git push`；否则只做到 commit。

---

## 执行顺序与检查清单

- [ ] Phase A：Plan → 逐篇整理 → 检查（可选 Step 3）
- [ ] Phase B：扫描 docs → 各文件延伸并入正文并删块
- [ ] Phase C：写根目录改动说明 MD → `git add` → 英文 commit → 按需 push

若某阶段无工作可做（例如 source.md 无新文章、或 docs 已无「延伸与参考」块），可跳过该阶段，但 Phase C 的改动说明与 commit 仍要执行，用于记录本次其他改动。

---

## 与原子 Skill 的关系

- 本工作流**覆盖**「news-pdf-integration」「docs-extensions-inline」「commit-changelog-workflow」在本项目中的**连续执行**；三者仍可单独调用。
- 细节（如单篇 MD 模板、延伸放置原则、改动说明固定格式）以各原子 skill 为准，此处仅给出执行顺序与最小必要步骤。
