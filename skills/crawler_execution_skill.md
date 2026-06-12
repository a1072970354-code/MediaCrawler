# Skill: Crawler Execution Rules

## Purpose

Constrain MediaCrawler execution to ensure crawler tasks are safe, controllable, and resumable.

---

## Execution Principles

1. Default to dry-run or small sample testing first.
2. Full-scale crawling is not allowed without prior testing.
3. Batch tasks must support checkpoint / resume.
4. Single link failure must not interrupt the entire batch.
5. Every task must explicitly specify:
   - Platform
   - Keywords or target links
   - Crawl scope
   - Page / quantity limit
   - Whether to download media files
   - Output directory
   - Storage format

---

## Concurrency and Rate Limiting

1. Do not blindly increase concurrency.
2. Do not bypass platform restrictions for speed.
3. Must explain risks before modifying request frequency.
4. Must stop and report when encountering:
   - Rate limiting
   - CAPTCHA
   - Login expiration
5. Do not automatically attempt to bypass CAPTCHA or platform restrictions.

---

## Failure Handling

1. Record failed links, platform, and failure reason.
2. Preserve successful results.
3. Support only-failed / resume to continue processing.
4. Stop current platform task when consecutive failures exceed threshold.
5. Do not retry indefinitely.

---

## Stop Conditions

Must stop and report if:

1. More than 3 consecutive failures on same platform.
2. CAPTCHA or verification page detected.
3. Login session expired.
4. Rate limiting detected (429, 403, etc.).
5. No useful output after 5 retry attempts.

---

## Output Requirements

After each execution, must report:

```text
Platform:
Keywords/Target:
Success count:
Failed count:
Skipped count:
Output location:
Need re-login:
Can resume:
Suggested next command:
```

---

## Batch Processing Rules

1. Process one platform at a time.
2. Within platform, process one keyword/link at a time.
3. Save results after each page/batch.
4. Do not accumulate all results in memory.
5. Support interrupted resume from last checkpoint.

---

## Media Download Rules

1. Do not download media by default unless explicitly requested.
2. Must check disk space before large downloads.
3. Must support resume for interrupted downloads.
4. Must skip already downloaded files.
5. Record download failures without stopping batch.

---

## Forbidden Behavior

- Do not start full crawl without testing.
- Do not ignore rate limiting signals.
- Do not retry failed requests indefinitely.
- Do not bypass platform security mechanisms.
- Do not increase concurrency without explaining risks.
- Do not claim success without verification.
