# MediaCrawler Real Run Test Report

> 记录每次真实爬取测试的结果，用于追踪问题和验证修复。

---

## Test #1: tieba 最小真实测试

### 基本信息

| 项目 | 值 |
|------|-----|
| 测试时间 | 2026-06-13 01:38 |
| 测试平台 | tieba（百度贴吧） |
| 测试类型 | search（关键词搜索） |
| 测试关键词 | 测试 |
| 登录方式 | --lt cookie（无需真实 cookie） |

### 测试命令

```powershell
uv run python main.py --platform tieba --type search --keywords "测试" --crawler_max_notes_count 2 --get_comment no --get_sub_comment no --save_data_option csv --lt cookie
```

### 执行结果

| 项目 | 结果 |
|------|------|
| 是否成功 | ✅ 成功 |
| 是否需要登录 | ❌ 不需要（cookie 模式自动跳过登录） |
| 是否遇到风控 | ❌ 未遇到 |
| 执行时长 | ~46 秒（01:38:05 - 01:38:51） |

### 产物信息

| 项目 | 值 |
|------|-----|
| 产物路径 | `data/tieba/csv/search_contents_2026-06-13.csv` |
| 产物大小 | 9,706 字节 |
| 产物行数 | 11 行（1 行表头 + 10 行数据） |
| 是否产生 browser_data | ✅ 是（`browser_data/tieba_user_data_dir/`） |
| Git 状态 | ✅ 干净（data 和 browser_data 已在 .gitignore） |

### CSV 字段

```
note_id, title, desc, note_url, publish_time,
user_link, user_nickname, user_avatar,
tieba_name, tieba_link,
total_replay_num, total_replay_page,
ip_location, source_keyword, last_modify_ts
```

### 关键发现

#### ⚠️ crawler_max_notes_count 未严格生效

**问题：** 指定 `crawler_max_notes_count=2`，但实际产出 10 条。

**分析：**
- tieba 搜索 API 一次返回 10 条（rn=20，实际返回 10 条）
- `crawler_max_notes_count` 可能只限制了详情页抓取数量，未限制搜索结果存储
- 或者 tieba 平台的 count 限制逻辑与其他平台不同

**影响：**
- 如果 limit 不可靠，未来批量任务会失控
- 需要单独审计 `crawler_max_notes_count` 在 tieba 平台是否真正生效

**后续行动：**
- [ ] 审计 tieba 的 `crawler_max_notes_count` 实现
- [ ] 确认是搜索结果过滤还是详情页过滤
- [ ] 对比其他平台（xhs, bili）的 count 限制逻辑

### 结论

```text
✅ tieba 最小真实测试通过
✅ 不需要登录即可搜索
✅ 产出可控（CSV 格式）
✅ 无风控触发
⚠️ crawler_max_notes_count 需要审计
```

---

## Test #2: 待执行

> 待审计 crawler_max_notes_count 后再执行下一平台测试。

---

*最后更新：2026-06-13*
