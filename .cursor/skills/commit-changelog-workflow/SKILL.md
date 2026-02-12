---
name: commit-changelog-workflow
description: Fix or rename files, write a Chinese changelog MD, commit in English, and optionally push. Use when fixing garbled filenames, documenting changes in Chinese, committing with English messages, or when the user asks for the project's commit flow or to "写 skill 提交流程".
---

# 提交与改动说明流程

在修文件（如乱码文件名）、写中文改动说明、用英文提交并可选上传时，按本流程执行。

---

## 流程概览

```
1. 做内容/文件名修改
2. 写改动说明 MD（中文）
3. 确定改动说明放哪、是否上传
4. 英文 commit，可选 push
```

---

## 1. 做修改

- 重命名、改内容等按用户要求完成。
- 若涉及乱码文件名：用正确 UTF-8 中文命名（如 `4.1-模仿学习.md`），并删除旧乱码文件；README 等链接若已指向正确名，无需改。

---

## 2. 写改动说明 MD（中文）

- **语言**：正文用中文。
- **建议结构**：
  - 标题：如「XXX 改动说明」
  - **改动了什么**：列表写具体改动（文件名、路径、行为变化等）。
  - **有什么用**：列表写目的与好处（可读性、链接可用、协作、一致性等）。
  - 末尾可加一句「本文档记录本次改动与目的，便于后续查阅。」

---

## 3. 改动说明放哪、是否上传

按用户要求二选一：

| 用户要求 | 做法 |
|----------|------|
| **放到仓库里并随提交上传** | 放在相关目录（如 `docs/4-classical/`），随 `git add` 一起提交。 |
| **放到最外面 / 不上传** | 放在**仓库根目录**，并把该文件名加入 `.gitignore`，不 `git add` 该文件。若没有 `.gitignore` 则在根目录新建并写入该文件名。 |

---

## 4. 提交与推送

- **Commit 语言**：用英文。
- **Commit 信息**：简洁说明类型与内容，例如：
  - `fix: rename garbled 4.1/4.2 filenames to correct Chinese and add changelog`
  - `docs: add changelog for section 4.1/4.2 filename fix`
- **Shell**：Windows PowerShell 用 `;` 连接命令，不用 `&&`。
- **Push**：仅当用户明确要求「上传」「push」时执行 `git push`；若用户说「不用上传」，则不要 add 改动说明（见上）、不要 push。

---

## 检查清单

- [ ] 修改已完成（含删除旧文件、更新链接若需要）
- [ ] 改动说明 MD 已写且为中文
- [ ] 已按用户要求决定：改动说明在子目录并上传，或在根目录且加入 .gitignore 不上传
- [ ] 已执行 `git add`（仅包含用户要提交的文件）
- [ ] Commit 信息为英文且清晰
- [ ] 仅在用户要求时执行 `git push`
