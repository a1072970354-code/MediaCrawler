# Skill: Git Workflow

## Purpose

Ensure safe, clean Git operations with proper review and minimal risk.

---

## Before Editing

1. Run `git status` to check working tree state.
2. Run `git diff` to see uncommitted changes.
3. Run `git log --oneline -5` to understand recent history.

---

## Before Committing

1. Review all changes with `git diff`.
2. Check for secrets, tokens, API keys, or credentials.
3. Verify no unintended files are staged.
4. Run tests if available.

---

## Commit Message Format

Use conventional commits:

```
<type>(<scope>): <description>

[optional body]
[optional footer]
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `style`: Formatting, missing semicolons, etc.
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `test`: Adding missing tests
- `chore`: Updating build tasks, configs, etc.

---

## Rules

1. Never force-push unless explicitly requested.
2. Never commit directly to main/master without explicit approval.
3. Never amend existing commits without explicit request.
4. Never auto-merge without conflict resolution.
5. Always provide commit message summary after committing.

---

## After Finishing

Report:

- Files changed
- What changed in each file
- Commit hash (if committed)
- Suggested next command (push, PR, etc.)
