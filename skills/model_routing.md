# Skill: Model Routing Strategy

## Purpose

Guide model selection based on task type, complexity, and cost. Avoid using expensive models for simple tasks or cheap models for complex reasoning.

---

## Task Classification

Before executing any task, classify it into one of these categories:

### A. Plan / Read-Only Analysis

**Use for:**
- Reading project structure
- Finding relevant files
- Analyzing error logs
- Creating modification plans
- No file changes allowed

**Requirements:**
- Prefer cheap, stable, long-context models
- No strong reasoning needed
- Must not enter large-scale modification mode

**Indicators:**
- "Analyze this project"
- "Find the bug"
- "What files need to change"
- "Create a plan for..."

---

### B. Build / Daily Execution

**Use for:**
- Small bug fixes
- Config changes
- Adding tests
- Updating README
- Small scope script modifications

**Requirements:**
- Prefer medium-cost models
- Change minimal files per step
- Must run minimal verification after changes

**Indicators:**
- "Fix this bug"
- "Add a test for..."
- "Update the config"
- "Change this function"

---

### C. Debug / Complex Problem Solving

**Use for:**
- 2-3 consecutive failures
- Multi-file complex bugs
- Architecture conflicts
- Unclear test failure causes
- API / model / toolchain issues

**Requirements:**
- Switch to strong reasoning model
- Must summarize failure trajectory first
- Forbidden to continue with cheap model indefinitely

**Indicators:**
- "Why is this failing"
- "Fix this complex issue"
- "Multiple things are broken"
- After 2-3 failed attempts on same problem

---

### D. Long Context / Deep Analysis

**Use for:**
- Reading large projects
- Analyzing long logs
- Comparing multiple files
- Understanding historical implementations
- Generating migration plans

**Requirements:**
- Prefer long-context models
- Analysis only, no direct large changes

**Indicators:**
- "Read this entire codebase"
- "Analyze these logs"
- "Compare these implementations"
- "What's the history of this feature"

---

### E. Batch / Low-Risk Repetitive Tasks

**Use for:**
- Batch renaming
- Documentation organization
- Format cleanup
- Simple repetitive tasks

**Requirements:**
- Prefer lowest-cost models
- Must have dry-run or checkpoint
- Failure must not affect completed results

**Indicators:**
- "Rename all instances of..."
- "Format these files"
- "Update all versions"
- "Clean up whitespace"

---

## Model Selection Guide

| Task Type | Cost Priority | Context Need | Reasoning Need |
|-----------|---------------|--------------|----------------|
| Plan | Low | High | Low |
| Build | Medium | Medium | Medium |
| Debug | High | Medium | High |
| Long Context | Medium | Very High | Medium |
| Batch | Low | Low | Low |

---

## Decision Flowchart

```
Start Task
    │
    ├─ Is this read-only analysis?
    │   └─ Yes → Plan (cheap, long-context)
    │
    ├─ Is this a small, routine change?
    │   └─ Yes → Build (medium cost)
    │
    ├─ Has this failed 2+ times?
    │   └─ Yes → Debug (strong model)
    │
    ├─ Need to read lots of code/logs?
    │   └─ Yes → Long Context (long-context model)
    │
    ├─ Is this repetitive batch work?
    │   └─ Yes → Batch (cheapest model)
    │
    └─ Default → Build (medium cost)
```

---

## Anti-Stall Integration

When combined with anti_stall rules:

1. If Build task fails 3 times → escalate to Debug
2. If Debug task fails with strong model → stop and report
3. Never stay on cheap model for complex debugging
4. Never waste expensive model on simple formatting

---

## Usage Example

When receiving a task, output:

```text
Task type: [Plan/Build/Debug/Long Context/Batch]
Reason: [why this classification]
Recommended model tier: [cheap/medium/strong/long-context]
```

Then proceed with appropriate model constraints.
