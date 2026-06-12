# Skill: Testing Rules

## Purpose

Ensure code changes are verified with appropriate tests before completion.

---

## Test Priority Order

1. **Unit test for changed module** - Fastest, most targeted
2. **Targeted script or command** - Quick verification
3. **Lint/type check** - Static analysis
4. **Full test suite** - Only when necessary

---

## Before Changing Code

1. Identify the fastest relevant check.
2. Check if test framework exists.
3. Locate existing tests for the module.
4. Understand test patterns used in project.

---

## After Changing Code

1. Run the smallest useful verification first.
2. If test fails, analyze before fixing.
3. If no tests exist, consider adding a targeted test.
4. Document any tests that cannot be run and why.

---

## Test Commands by Project Type

| Project Type | Common Commands |
|---|---|
| Python | `pytest`, `python -m pytest`, `ruff check` |
| Node.js | `npm test`, `npx jest`, `npx vitest` |
| Go | `go test ./...`, `go vet` |
| Rust | `cargo test`, `cargo clippy` |

---

## Rules

1. Never skip tests without explanation.
2. Never modify tests to make them pass without fixing the code.
3. Never claim tests pass without running them.
4. If tests cannot be run, provide the exact command for user to run manually.

---

## Output

After testing, report:

- Tests run
- Tests passed
- Tests failed
- Tests skipped
- Coverage (if available)
- Recommended next step
