# Skill: Anti-Stall Execution

## Purpose

Prevent OpenCode from silently hanging, looping, or retrying without progress.

---

## Stop Conditions

The agent must stop current execution and report if:

1. Same command has no useful new output for a long period.
2. Same error appears after 3 attempts.
3. Logs contain repeated:
   - timeout
   - retry
   - waiting
   - no progress
   - 502
   - bad gateway
   - connection reset
4. No file changed, no test result appeared, and no conclusion was reached after multiple tool rounds.
5. The next action is based on guessing rather than evidence.

---

## Required Stop Report

When stopping, output:

```text
Current goal:
Completed:
Blocked at:
Last error:
Tried:
Likely cause:
Recommended next step:
Need user decision:
```

---

## Forbidden Behavior

- Do not silently wait.
- Do not repeat the same command without a new reason.
- Do not keep retrying failed API calls.
- Do not start a broad refactor to escape a local bug.
- Do not claim success without verification.

---

## Recovery Rules

For batch jobs:

1. Preserve completed results.
2. Mark failed item clearly.
3. Continue with remaining items when safe.
4. Provide resume command.
5. Never delete raw responses unless explicitly requested.
