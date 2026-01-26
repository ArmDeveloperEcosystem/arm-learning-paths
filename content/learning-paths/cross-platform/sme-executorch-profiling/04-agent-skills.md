---
title: "Agent skills: AI assistants and CI automation"
weight: 5
layout: "learningpathall"
---

## Goal: Automate performance analysis with AI coding assistants

This learning path includes a set of structured, verifiable agent skills that allow the performance analysis workflow to be automated by AI coding assistants (such as Codex, Claude, Cursor, or Copilot) and by CI systems.
Traditional documentation describes what a human should do. Agent skills describe how an automated system should do it, with explicit definitions of inputs, actions, expected outputs, and validation criteria. This structure enables workflows that are reproducible, verifiable, and suitable for automation.
Each skill defines:
  * Required inputs and preconditions
  * The exact actions to perform
  * The files and artifacts that should be produced
  * Validation steps that confirm successful execution
  * 
This makes the workflow suitable for use in AI-assisted development, automated regression testing, and repeatable onboarding.

## 1. Where the agent workflows live

All agent skills are included in the same code repository as the performance analysis kit under::

- [`agent_skill_ml_profiling/`](https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling/tree/main/agent_skill_ml_profiling)

Start by reading the [skill catalog](https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling/blob/main/agent_skill_ml_profiling/readme.md)

Each skill is documented as a standalone, executable workflow.
Available skills include:
1. `01_setup_workspace.md` - Initialize performance analysis environment
2. `02_build_runners.md` - Build SME2-on/off runner binaries
3. `03_export_model.md` - Export PyTorch model to ExecuTorch .pte
4. `04_run_profiling.md` - Execute performance measurement pipeline (timing + trace)
5. `05_analyze_results.md` - Generate operator-category breakdown
6. `06_validate_workflow.md` - End-to-end smoke test
7. `07_report_generation.md` - Generate comprehensive markdown report
8. `08_onboard_edgetam.md` - Onboard EdgeTAM image encoder model

## 2. Agent skill structure

Each agent skill follows a consistent structure designed for both human readability and machine execution:

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

**The key feature**: Each skill is self-contained and verifiable. Validation steps ensure that the skill completed successfully before downstream skills are executed. This makes the workflow robust when automated.

## 3. Quick reference

| Skill | Time | Prerequisites | Outputs |
|-------|------|---------------|---------|
| `setup_workspace` | ~30 min | Python 3.9+, CMake 3.29+ | `.venv/`, `executorch/` |
| `build_runners` | ~20 min | Setup complete | `executorch/cmake-out/android-arm64-v9a*/executor_runner` (for mobile device testing) or `executorch/cmake-out/mac-arm64*/executor_runner` (developer accessibility) |
| `export_model` | ~5 min | Setup complete | `out_<model>/artifacts/*.pte` |
| `run_profiling` | ~10 min | Runners + model | `out_<model>/runs/<platform>/*.etdump` |
| `analyze_results` | ~2 min | Performance measurement complete | `out_<model>/runs/<platform>/analysis_summary.json` |
| `validate_workflow` | ~15 min | Setup complete | Full smoke test validation |
| `report_generation` | ~1 min | Analysis complete | `out_<model>/runs/<platform>/report.md` |

Times are approximate and depend on host performance and network availability.

## 4. Recommended workflow

For AI assistants, use skills in this order:

**First-time setup** (required for fresh downloads):
1. `01_setup_workspace.md` - Initialize environment (run this first if you just downloaded the repo)
   - Creates the Python virtual environment
   - Clones and installs ExecuTorch
   - Required before any other skill

**After setup is complete**:
2. `06_validate_workflow.md` - Quick end-to-end test (recommended after setup)
   - Runs a complete smoke test using a toy model
   - Confirms the environment is correctly configured
   - Recommended immediately after setup
     
**Ongoing usage**:
For regular model analysis:
  - `02_build_runners.md` (only if runners are missing or ExecuTorch changed)
  - `03_export_model.md`
  - `04_run_profiling.md`
  - `05_analyze_results.md`

Skills can be executed individually or chained together depending on the use case.
Skills are composable. You can chain them together for end-to-end automation, or use them individually for specific tasks. Each skill includes verification steps to ensure success before proceeding.

## 5. Example: Using skills with an AI assistant

Agent skills are designed to be pulled directly into an AI agent’s context as executable instructions. Each skill is a standalone Markdown file (*.md) that the agent reads and follows step by step.
The typical interaction model is:
  * The AI agent is provided with one or more skill files (for example, by loading them into the agent’s context, workspace, or prompt memory).
  * The user issues a high-level intent prompt.
  * The agent executes the steps defined in the skill file, rather than inferring actions on its own.
  * The agent verifies success using the validation steps defined in the skill before proceeding.
This separation is intentional:
Skill files define how to perform a task, including commands, expected outputs, and validation.
User prompts define what outcome is desired.

Try this example User prompt in your AI agent: "Set up the performance analysis environment and run a smoke test"

Agent behavior:
1. Reads `01_setup_workspace.md` and creates `.venv/`, `executorch/`
2. Verifies that the virtual environment and ExecuTorch checkout exist.
3. Reads `02_build_runners.md` and builds the required runner binaries.
4. Verifies that SME2-on and SME2-off runners were produced.
5. Reads 06_validate_workflow.md and runs the end-to-end smoke test.
6. Confirms all validation gates pass before reporting success.

At no point does the agent need to guess which commands to run or how to validate results, the skill files provide that information explicitly.
Skills make automation reliable. The agent doesn't need to guess what commands to run or how to verify success. It follows the skill's structured steps. This makes the performance analysis workflow portable across human-driven, AI-driven, and fully automated environments.

This Learning Path showed how to analyze ExecuTorch performance on Arm using SME2, operator-level profiling, and agent-driven automation for repeatable optimization.
