---
name: people-readme-links
description: Updates docs/8-people/README.md with real direct links (Scholar profile, lab/project page, video, code) and a one-line bio after each name. Use when maintaining the People directory, replacing Google/search links with verified URLs, or adding person intros (简介). Unfound links are written as 更新中.
---

# 人物 README 真实链接与简介

更新 [docs/8-people/README.md](docs/8-people/README.md)：每人增加**简介**，四类链接改为**真实直达 URL**，找不到则写 **更新中**；每次写入链接前必须**自我验证**。

---

## 目标与范围

- **文件**：`docs/8-people/README.md`
- **简介**：每人名后一句（机构/身份 + 方向或代表工作，约 10–25 字；暂无写「更新中」）。
- **链接类型**：📄 Paper（Scholar 个人页）、🧪 Project（lab/项目页）、🎥 Video（单条视频）、💻 Code（仓库或 profile）。禁止搜索页 URL。
- **未找到**：统一写 `📄 更新中`（无链接），全文档一致。

---

## 链接自我验证（每次找到后必做）

采纳前必须通过，否则该条写「更新中」：

1. **格式**：合法 HTTPS URL；禁止 `google.com/search`、`scholar.google.com/scholar?q=...`、`youtube.com/results?search_query=...`、`github.com/search?q=...`。Paper 须为 `scholar.google.com/citations?user=...`。
2. **可访问性**：对 URL 发 HEAD（或 GET），2xx 或 3xx→2xx 通过；4xx/5xx、超时、失败 → 不写入。可用 `curl -sI -o NUL -w "%{http_code}" <url>`（Windows）或浏览器确认。
3. **内容（建议）**：Scholar 页见该学者姓名；Project 见机构/学者；Video 为单条视频；Code 为具体 repo/profile。

流程：找到链接 → 验证（格式 + 可访问性）→ 通过则写入，否则写「更新中」。

---

## 执行顺序

1. **链接类型说明**：在 README 顶部表中注明「未找到时显示 更新中」，统一 `📄 更新中` 写法。
2. **按章节**：Berkeley → Stanford → CMU → MIT → DeepMind → FAIR → 其他北美 → 欧洲 → 国际产业 → 国内高校 → 国内产业。
3. **每人**：先写简介（人名后、链接前），再逐条替换四类链接；每写一条链接前执行一次验证。
4. **收尾**：全文档检查无残留 `google.com/search`、`youtube.com/results`、`github.com/search`。

---

## 条目格式

每人一条目，格式：

```markdown
N. **姓名**（机构 + 方向/代表工作，约 10–25 字）
   📄 [Paper](真实URL) 或 更新中 · 🧪 [Project](URL) 或 更新中 · 🎥 [Video](URL) 或 更新中 · 💻 [Code](URL) 或 更新中
```

简介可换行缩进书写；「更新中」无链接，纯文本。

---

## 可选

- 仓库内增加 link-check 脚本，对 README 中 `](http` 链接做 HEAD 检查，死链报错或生成待修复列表。
