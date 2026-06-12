# Project Rules: MediaCrawler

## Project Goal

MediaCrawler is a media platform crawler that extracts content, comments, and metadata from various platforms. The project must prioritize stability, resumability, and safe operation over aggressive refactoring.

---

## Must Preserve

Do not break these behaviors:

1. Already downloaded files should be skipped when possible.
2. Cache and browser data should be preserved for resume workflows.
3. Download/checkpoint/resume workflows must continue working.
4. Cookie/session management must remain secure and traceable.
5. Batch processing must not lose completed results when one item fails.
6. Error logging and retry status must remain traceable.

---

## Preferred Workflow

Before editing:

1. Read project structure.
2. Locate existing tests.
3. Identify the smallest file set to change.
4. Check existing CLI arguments and config files.
5. Avoid inventing new commands before searching the repo.

When fixing bugs:

1. Reproduce or explain the bug.
2. Find the direct cause.
3. Make the smallest fix.
4. Add or update a targeted test if test framework exists.
5. Run the fastest relevant check.

---

## Anti-Stall Rules

1. Never allow one failed command to block the entire workflow.
2. If a command fails 3 times, stop and report.
3. Preserve partial results.
4. Write enough logs to diagnose issues later.
5. Prefer checkpoint/resume over restarting from zero.

---

## Model Routing Rule

Before executing any task, classify it and state the recommended model tier:

1. **Plan** - Read-only analysis, no file changes → cheap, long-context
2. **Build** - Small routine changes → medium cost
3. **Debug** - Complex issues, 2+ failures → strong reasoning
4. **Long Context** - Large codebase/log analysis → long-context model
5. **Batch** - Repetitive low-risk tasks → cheapest model

State classification before proceeding. See `skills/model_routing.md` for details.

---

## MediaCrawler Specific Rules

1. 不得泄露、打印、提交 cookie、token、session、账号信息。
2. 不得自动发布、自动点赞、自动评论、自动私信。
3. 不得绕过平台风控、验证码、登录限制。
4. 不得破坏已有下载、缓存、断点续爬流程。
5. 不得让单个失败链接中断整个批处理。
6. browser_data、cache、downloads、data 等目录必须避免被 watcher 扫描和 Git 提交。
7. 所有批处理任务必须优先支持 dry-run / checkpoint / resume。
8. 下载或解析失败时必须记录失败原因，并继续处理剩余任务。
9. 修改爬虫逻辑前必须先定位平台模块和最小改动文件。
10. 涉及平台规则、API、网页结构变化时，必须先说明不确定性，不得凭空猜测。

---

## Output Requirements

When finishing a task, report:

- Changed files
- Behavior before
- Behavior after
- How to run
- How to resume
- Tests/checks run
- Remaining risks
