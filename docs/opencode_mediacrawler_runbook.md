# OpenCode MediaCrawler Runbook

> 本手册为 OpenCode / Hermes Agent 执行 MediaCrawler 任务时的操作标准。

---

## 1. 当前稳定基线

| 项目 | 值 |
|------|-----|
| 本地项目路径 | `L:\scripts\MediaCrawler` |
| 远程 fork | https://github.com/a1072970354-code/MediaCrawler |
| upstream | https://github.com/NanmiCoder/MediaCrawler |
| 稳定标签 | `opencode-dryrun-baseline` |
| 当前能力 | OpenCode 工作流基线、爬虫执行 Skill、平台安全边界 Skill、--dry-run 安全预览、三平台 dry-run 验证通过 |

---

## 2. 安全原则

1. **先 dry-run，再真实执行。**
2. **先小样本，再扩大范围。**
3. 不自动发布、点赞、评论、私信、关注。
4. 不绕过验证码、风控、登录限制。
5. 不打印、不提交、不上传 cookie / token / session / localStorage。
6. 不把 `browser_data`、`cache`、`downloads`、`data`、`logs` 加入 Git。
7. 单个平台失败不能中断整体流程。
8. 任何连续失败必须停止并汇报。

---

## 3. 日常启动检查

```powershell
cd L:\scripts\MediaCrawler
git status
git log --oneline -5
git remote -v
```

确认：

- 工作树干净
- 远程 origin 是自己的 fork
- upstream 指向原作者仓库

---

## 4. dry-run 使用方法

```powershell
uv run python main.py --platform tieba --dry-run yes
uv run python main.py --platform bili --dry-run yes
uv run python main.py --platform xhs --dry-run yes
```

**dry-run 必须满足：**

- ✅ 不启动浏览器
- ✅ 不登录
- ✅ 不请求平台
- ✅ 不写 data
- ✅ 不下载
- ✅ 不创建 browser_data
- ✅ 只打印配置

---

## 5. 零风险验证

```powershell
uv run pytest tests/ -v
uv run python main.py --help
```

**当前已知情况：**

- 现有测试中 `test_create_excel_store` 有 1 个历史失败（非本次引入）
- dry-run 新增测试已通过（10/10）
- `--help` 已验证通过

---

## 6. 最小真实测试前检查清单

真实测试前必须确认：

- [ ] 已完成 dry-run
- [ ] 已确认平台
- [ ] 已确认关键词
- [ ] 已限制 `crawler_max_notes_count`
- [ ] 已关闭评论或限制评论数量
- [ ] 已确认是否需要登录
- [ ] 已确认输出目录
- [ ] 已确认清理方式
- [ ] 已确认不会下载大文件
- [ ] 已确认不打印敏感信息

---

## 7. 最小真实测试命令模板

> ⚠️ 需要用户确认后才能执行。可能访问真实平台、产生 `data/`、需要登录态。

```powershell
uv run python main.py --platform tieba --type search --keywords "测试" --crawler_max_notes_count 2 --get_comment no --get_sub_comment no --save_data_option csv
```

---

## 8. 测试产物清理

> ⚠️ 清理前必须确认路径，禁止删除整个项目目录。

```powershell
Remove-Item -Recurse -Force .\data\tieba\
Remove-Item -Recurse -Force .\data\xhs\
Remove-Item -Recurse -Force .\logs\
```

---

## 9. Git 工作流

```powershell
git status
git add <files>
git commit -m "<message>"
git push
```

**说明：**

- `origin` 是自己的 fork
- `upstream` 是原作者仓库
- 正常 push 不要 force
- 同步上游使用 fetch / merge，不要直接覆盖本地工作

---

## 10. 同步 upstream

```powershell
git fetch upstream
git checkout main
git merge upstream/main
git push
```

---

## 11. 回滚方式

```powershell
git checkout opencode-dryrun-baseline
```

查看标签：

```powershell
git show opencode-dryrun-baseline
```

> ⚠️ checkout tag 会进入 detached HEAD。若要基于标签新建分支：

```powershell
git checkout -b recover-from-dryrun-baseline opencode-dryrun-baseline
```

---

## 12. OpenCode 使用模板

### 分析模式

```markdown
先用 plan 模式分析，不要改文件。

任务：
[具体任务]

要求：
1. 先判断任务类型
2. 读取 AGENTS.md 和 skills
3. 不触碰敏感信息
4. 不运行真实爬虫
5. 给出最小方案
```

### 执行模式

```markdown
按刚才方案执行。

要求：
1. 小步修改
2. 先 git status
3. 不触碰 cookie/token/session
4. 修改后运行最小测试
5. 连续失败停止汇报
```

---

## 13. 禁止事项

| 禁止 | 原因 |
|------|------|
| 提交 cookie / token / session | 安全风险 |
| 提交 browser_data / cache / data / downloads / logs | 隐私与体积 |
| 自动绕过验证码 | 违反平台条款 |
| 自动发布 / 点赞 / 评论 / 私信 | 违反平台条款 |
| 未经 dry-run 直接全量抓取 | 风险不可控 |
| force push（除非用户明确确认） | 可能覆盖远程历史 |

---

*最后更新：2026-06-13*
*基线标签：opencode-dryrun-baseline*
