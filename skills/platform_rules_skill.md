# Skill: Platform Rules and Security Boundaries

## Purpose

Constrain platform adaptation, login state, cookies, signatures, and risk control related modifications.

---

## Security Boundaries

1. Do not print, commit, upload, or expose:
   - Cookies
   - Tokens
   - Session data
   - localStorage
   - Account credentials
2. Do not write account information into logs.
3. Do not automatically:
   - Publish content
   - Like posts
   - Comment on posts
   - Send private messages
   - Follow accounts
4. Do not bypass:
   - CAPTCHA
   - Risk control mechanisms
   - Login restrictions
5. Do not crack, evade, or attack platform security mechanisms.
6. Do not modify signature logic to enable high-risk evasion.

---

## Platform Module Modification Rules

Before modifying platform logic, must locate:

1. Platform directory: `media_platform/{platform}/`
2. Client module: `client.py`
3. Login module: `login.py`
4. Config file: `config/{platform}_config.py`
5. Extractor/parser: `extractor.py`
6. Store path: `store/{platform}/`
7. Tests: `tests/test_{platform}_*.py`

---

## Login Related Rules

1. Login state is for local use only.
2. `browser_data/` must be treated as sensitive directory.
3. Cookie login failure must prompt re-login.
4. Do not attempt credential stuffing or brute force.
5. Do not add `browser_data/` to Git.
6. Do not display complete cookies in reports.

---

## Cookie and Token Handling

1. Cookies must be stored locally only.
2. Cookies must not be committed to repository.
3. Cookie expiration must trigger re-login prompt.
4. Token refresh must be handled gracefully.
5. Session data must not be shared between machines.

---

## Platform Change Handling

When page structure, API, fields, or signature methods change:

1. Must explain uncertainty.
2. Must create minimal reproduction first.
3. Must preserve old logic for rollback.
4. Must add failure examples or test documentation.
5. Do not guess field meanings without evidence.

---

## Signature and Encryption Rules

1. Do not reverse engineer platform signatures for malicious purposes.
2. Do not share signature bypass methods publicly.
3. Signature changes must be documented with uncertainty.
4. Must test signature changes with small samples first.
5. Must preserve rollback capability for signature changes.

---

## Risk Control Handling

When encountering risk control:

1. Stop immediately.
2. Report the situation.
3. Do not attempt to bypass.
4. Suggest waiting or manual intervention.
5. Record the risk control trigger for future avoidance.

---

## Output Requirements

When modifying platform logic, must output:

```text
Platform modified:
Files changed:
涉及登录态: Yes/No
涉及 Cookie/Token: Yes/No
涉及签名: Yes/No
风控风险: Low/Medium/High
测试方式:
回滚方式:
```

---

## Platform-Specific Rules

### 小红书 (xhs)
- High risk control sensitivity
- Signature changes frequently
- Must test with small samples

### 抖音 (dy)
- Complex signature mechanism
- Frequent API changes
- Must verify with actual requests

### 快手 (ks)
- Moderate risk control
- Stable API structure
- Standard testing sufficient

### B站 (bilibili)
- Low risk control
- Stable API
- Standard testing sufficient

### 微博 (weibo)
- Moderate risk control
- Cookie-based sessions
- Must handle cookie refresh

### 贴吧 (tieba)
- Low risk control
- Simple API structure
- Standard testing sufficient

### 知乎 (zhihu)
- High risk control
- Complex authentication
- Must handle login carefully

---

## Forbidden Behavior

- Do not expose credentials in any form.
- Do not bypass security mechanisms.
- Do not guess platform changes.
- Do not modify signatures without testing.
- Do not ignore risk control signals.
- Do not commit sensitive data.
