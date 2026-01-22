---
title: Agent Skills for ML Profiling (SME2 ExecuTorch)
draft: false
---

# Agent Skills for ML Profiling

These are **structured, verifiable agent skills** for AI coding assistants (Claude, Codex, Cursor, Copilot) to automate SME2 ExecuTorch profiling workflows.

**Format**: Based on [claudekit-skills](https://github.com/mrgoonie/claudekit-skills) best practices with enhanced verification, decision matrices, and implementation checklists.

## Skill Format

Each skill follows a structured format inspired by [claudekit-skills](https://github.com/mrgoonie/claudekit-skills):

**YAML Frontmatter** (metadata):
```yaml
---
name: skill_name
description: What the skill does and when Claude should use it
---
```

**Markdown Body** (structured content):
- **Overview**: Context and key concepts
- **When to use**: Clear use cases
- **Prerequisites**: Required inputs/state
- **Steps**: Ordered, executable commands
- **Verification**: How to confirm success (with test commands)
- **Expected outputs**: Artifacts/files created
- **Failure handling**: Common issues and fixes (table format)
- **Best practices**: Recommendations
- **Implementation checklist**: Step-by-step verification
- **References**: Related scripts, docs, learning path pages
- **Assets**: Supporting files used by the skill

## Available Skills

1. **[01_setup_workspace.md](01_setup_workspace.md)** - Initialize profiling environment
2. **[02_build_runners.md](02_build_runners.md)** - Build SME2-on/off runner binaries
3. **[03_export_model.md](03_export_model.md)** - Export PyTorch model to ExecuTorch .pte
4. **[04_run_profiling.md](04_run_profiling.md)** - Execute profiling pipeline (timing + trace)
5. **[05_analyze_results.md](05_analyze_results.md)** - Generate operator-category breakdown
6. **[06_validate_workflow.md](06_validate_workflow.md)** - End-to-end smoke test
7. **[07_report_generation.md](07_report_generation.md)** - Generate comprehensive markdown report
8. **[08_onboard_edgetam.md](08_onboard_edgetam.md)** - Onboard EdgeTAM image encoder model

## Usage Pattern

**For AI assistants**: Reference these skills by name when the user requests profiling tasks.

**Example**:
- User: "Set up the profiling environment"
- Agent: Use `01_setup_workspace.md` skill

**For developers**: These are automation playbooks. Run commands sequentially (01 → 02 → 03 → 04 → 05), verify each step.

## Key Features

- **Structured format**: YAML frontmatter + organized markdown sections
- **Decision matrices**: Clear guidance on when to use different options
- **Implementation checklists**: Step-by-step verification at each stage
- **Failure handling tables**: Common issues with specific fixes
- **Rich context**: Overview sections explain why, not just how
- **Reference navigation**: Clear pointers to related scripts and docs

## Ground Rules

- **Always verify prerequisites** before executing steps
- **Check verification gates** after each skill completes
- **Preserve artifacts**: Don't delete `.etdump`, `.pte`, or analysis outputs
- **Record context**: Note ExecuTorch SHA, model name, config paths
- **Fail fast**: If verification fails, stop and troubleshoot before proceeding
- **Use timing-only runners for latency** - Trace-enabled runners are for kernel analysis only

## Skill Dependencies

```
01_setup_workspace → 02_build_runners → 03_export_model → 04_run_profiling → 05_analyze_results → 07_report_generation
                                                              ↓
                                                    06_validate_workflow (can run anytime)

08_onboard_edgetam → 03_export_model (onboard before export)
```

## Quick Reference

| Skill | Time | Outputs |
|-------|------|---------|
| `01_setup_workspace` | ~30 min | `.venv/`, `executorch/` |
| `02_build_runners` | ~20 min | `executorch/cmake-out/mac-arm64*/executor_runner` |
| `03_export_model` | ~5 min | `out_<model>/artifacts/*.pte` |
| `04_run_profiling` | ~10 min | `runs/<platform>/*.etdump`, CSV files, pipeline summary |
| `05_analyze_results` | ~2 min | `runs/<platform>/analysis_summary.json` (optional - automatic by pipeline) |
| `06_validate_workflow` | ~15 min | Full smoke test validation |
| `07_report_generation` | ~1 min | `runs/<platform>/report.md` |
| `08_onboard_edgetam` | ~5 min | Setup complete | `models/edgetam/` (model wrapper, checkpoint, config) |