---
title: "Agent skills: AI assistants + CI automation"
weight: 5
layout: "learningpathall"
---

## Goal: Automate profiling with AI coding assistants

This learning path ships structured, verifiable agent skills that make the profiling workflow automatable by AI coding assistants (Codex, Claude, Cursor, Copilot etc) and CI pipelines. Traditional documentation tells humans what to do, but agent skills tell AI assistants how to do it, with clear inputs, outputs, and verification gates.

The profiling kit includes skill definitions that specify what the agent needs (inputs), what commands to run (actions), what files to produce (outputs), and how to verify success (validation gates). This makes the workflow reproducible (same commands, same results), verifiable (each step has success criteria), and composable (skills chain together for end-to-end automation).

Real-world use cases include AI coding assistants that can set up the profiling environment on command, CI pipelines that run automated regression testing after ExecuTorch updates, and faster onboarding for new team members who can use agent skills to get started quickly.

## 1. Where the agent workflows live

This learning path ships structured, verifiable agent skills under the profiling kit:

- [`executorch_sme2_kit/agent_skill_ml_profiling/`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/tree/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/agent_skill_ml_profiling)

Start here: Read [`executorch_sme2_kit/agent_skill_ml_profiling/README.md`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/agent_skill_ml_profiling/README.md) for the complete skill catalog.

Available skills:
1. `01_setup_workspace.md` - Initialize profiling environment
2. `02_build_runners.md` - Build SME2-on/off runner binaries
3. `03_export_model.md` - Export PyTorch model to ExecuTorch .pte
4. `04_run_profiling.md` - Execute profiling pipeline (timing + trace)
5. `05_analyze_results.md` - Generate operator-category breakdown
6. `06_validate_workflow.md` - End-to-end smoke test
7. `07_report_generation.md` - Generate comprehensive markdown report

## 2. Agent skill structure

Each skill follows a consistent format based on current practices among developers:

- YAML frontmatter: `name` and `description` metadata
- Overview: Context and key concepts (why this skill matters)
- When to use: Clear use cases
- Prerequisites: Required inputs/state
- Steps: Ordered, executable commands
- Verification: How to confirm success (with test commands)
- Expected outputs: Artifacts/files created
- Failure handling: Common issues and fixes (table format)
- Best practices: Recommendations
- Implementation checklist: Step-by-step verification
- References: Related scripts, docs, learning path pages
- Assets: Supporting files used by the skill

**The key insight**: Skills are self-contained and verifiable. Each skill includes validation steps that ensure success before proceeding. This makes them reliable for automation.

## 3. Quick reference

| Skill | Time | Prerequisites | Outputs |
|-------|------|---------------|---------|
| `setup_workspace` | ~30 min | Python 3.9+, CMake 3.29+ | `.venv/`, `executorch/` |
| `build_runners` | ~20 min | Setup complete | `executorch/cmake-out/mac-arm64*/executor_runner` |
| `export_model` | ~5 min | Setup complete | `out_<model>/artifacts/*.pte` |
| `run_profiling` | ~10 min | Runners + model | `out_<model>/runs/<platform>/*.etdump` |
| `analyze_results` | ~2 min | Profiling complete | `out_<model>/runs/<platform>/analysis_summary.json` |
| `validate_workflow` | ~15 min | None (does setup) | Full smoke test validation |
| `report_generation` | ~1 min | Analysis complete | `out_<model>/runs/<platform>/report.md` |

## 4. Recommended workflow

For AI assistants, use skills in this order:

1. `validate_workflow.md` - Quick end-to-end test (recommended first action)
   - This runs the complete workflow with a toy model
   - Validates that the environment is correctly configured
   - Takes ~15 minutes and gives you confidence everything works

2. Or step-by-step: `setup_workspace` → `build_runners` → `export_model` → `run_profiling` → `analyze_results`
   - Use this when you want to understand each step
   - Or when `validate_workflow` fails and you need to debug

**The insight**: Skills are composable. You can chain them together for end-to-end automation, or use them individually for specific tasks. Each skill includes verification steps to ensure success before proceeding.

## 5. Example: Using skills with an AI assistant

User: "Set up the profiling environment and run a smoke test"

Agent workflow:
1. Use `01_setup_workspace.md` skill → creates `.venv/`, `executorch/`
2. Use `02_build_runners.md` skill → builds runners
3. Use `06_validate_workflow.md` skill → runs end-to-end smoke test
4. Verify all validation checks pass

Result: Complete profiling environment ready, validated with a working example.

The value: Skills make automation reliable. The agent doesn't need to guess what commands to run or how to verify success. It follows the skill's structured steps.