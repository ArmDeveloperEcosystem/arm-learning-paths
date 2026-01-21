# SME2 ExecuTorch Profiling Learning Path — Rewrite Request (Source of Truth)

This file restates the requested “major change” for the learning path `sme-executorch-profiling`, and pins **reference sources** (with **absolute paths**) that must drive the rewrite.

## Goal

Replace the current multi-step learning-path content with a **short, high-quality, context-based** learning path that is:

- **Outcome-first**: readers can stop after the Overview and still leave with a complete, usable workflow.
- **Model-onboarding-centric (can be model-specific)**: repository structure + registration + export script is the critical centerpiece. Model onboarding may require **non-trivial, model-specific code edits** (wrappers, input/output normalization, export-friendly refactors, operator replacements, shape constraints, etc.). The learning path should treat this as first-class work, not a footnote.
- **Model-agnostic, pipeline-complete**: users should be able to take the pipeline “as-is” and reuse it across models, and it should be documented end-to-end on a single page (build runner + config + run + analyze). The only model-specific work should be:
  - adding a model package under `model_profiling/models/<model_name>/` (or equivalent),
  - exporting a `.pte` (+ `.etrecord`/metadata if available),
  - supplying a config that points at those artifacts.
  Everything else (runner build, pipeline invocation, analysis tooling, report generation) should remain unchanged.
  - **Critical nuance**: the pipeline must explicitly cover building/selecting the **correct runner variants** and config options for the job (for example: baseline vs SME2-on/off, and **XNNPACK kernel trace logging / xnntrace** enabled runners when kernel-level insights are needed). Without the right runner + logging, results are incomplete and misleading.
- **Agent-friendly**: provides “agent skills” entrypoint to automate setup + smoke tests + pipeline runs.
- **Designed/edited**: clean typography, consistent hierarchy, balanced visuals (not giant images), and non-boring writing.

## Hard constraints / directives

- **Do not create 9 step pages.** Keep this to **4 content pages** (plus the `_index.md` landing page, which is frontmatter-driven).
- **Do not use a separate `00-introduction.md`.** The landing experience must make sense and be context-based.
- **`_index.md` is landing-only**: we cannot change the effective landing structure here, so create a separate Overview page immediately after `_index.md`.
- **Fix layout quality**: avoid “one giant sentence headline + lots of tiny text + huge images”. Act as designer/editor.
- **Preserve existing work by archiving**: do not delete; archive the current content so we can restart cleanly (and keep the archive out of the published navigation).

## Target pages to create (explicit filenames)

- `01-overview.md`: stop-here Overview + Quickstart (includes “get the code package” first)
- `02-setup-and-model-onboarding.md`: minimal env + model onboarding contract (includes EdgeTAM image encoder as the advanced onboarding example)
- `03-pipeline-and-analysis.md`: runner variants + config + run + analysis (includes xnntrace / kernel logging runners)
- `04-agent-skills.md`: agent skills + validation gates + sample use-cases + sample report

## Proposed high-level structure (user request)

1) **Overview (single page experience)** (this is a separate page right after `_index.md`)  
   Include:
   - The runtime **stack flow**
   - **Expected results** (latency charts + operator breakdown)
   - A sample **report**
   - **Download code** instructions
   - The “minimum viable” commands so a reader can stop here and still run independently

2) **Environment setup + model onboarding (most critical)**  
   Keep env setup short (a few lines), then focus on:
   - Recommended **repo structure**
   - Model build + registration scripts
   - A comprehensive **model export script** (source: `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/export/export_model.py`)

3) **Pipeline (single page)**  
   All in one place:
   - Runner building
   - Config generation + run pipeline
   - Results analysis + how to interpret

4) **Agent skills (single page)**  
   - Point to agent-skill markdown files
   - Include test use-cases and sample report outputs
   - Help developers use AI coding agents to do setup + initial testing + pipeline runs

## MUST-read reference sources (absolute paths)

### Primary “structure + reproduction guide” source (Part 2)

- `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/out_squeeze_sam/report/SqueezeSAM_Transpose_Overhead_Analysis_and_Reproduction_Guide.md`
  - Read **Part 2** starting at:
    - “## Part 2: SqueezeSAM Operator-Level Profiling Reproduction Guide”
    - (requested focus was lines after 103 where Part 2 begins)

### “Comprehensive local repo setup” reference

- `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/README.md`

### “Fresh ExecuTorch checkout + PR validation” reference

- `/Users/jaszhu01/Local/Github/sme2_executorch/pr16533_env_setup.md`

### “Old workflow (may be partially outdated)”

- `/Users/jaszhu01/Local/Github/sme2_executorch/PROFILING_WORKFLOW.md`

### Sample reports (style + completeness target)

- `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/out_squeeze_sam/report/SqueezeSAM_INT8_SME2_Performance_Report.md`
- `/Users/jaszhu01/Local/Github/sme2_executorch/reference/SqueezeSAM_SME2_Performance_Report_12022025.md`

### Blog draft + final (learning path must match the blog’s “repo link + what to do next”)

- Markdown draft:
  - `/Users/jaszhu01/Local/Github/sme2_executorch/reference/blog/blog_draft_sme2_executorch_improved_v3.md`
- Word final:
  - `/Users/jaszhu01/Local/Github/sme2_executorch/reference/blog/blog_sme2_draft/blog_draft_sme2_executorch_01062026-CLEAN.docx`

### Example advanced model onboarding target (external reference)

- EdgeTAM (use its **image encoder** as an example of a model that may require significant onboarding edits):
  - `https://github.com/facebookresearch/EdgeTAM`

### Export script to base onboarding on (must be reused)

- `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/export/export_model.py`
  - Specifically requested: “take the comprehensive model export scripts from here”

## Scripts/code expected to be copied (to be planned explicitly)

From `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/` into this learning-path repo (exact destination paths TBD in the plan):

- **Export**: `model_profiling/export/export_model.py` (+ supporting export docs if needed)
- **Model registry + onboarding scaffolding**: `model_profiling/models/` (including registry patch hook in `models/__init__.py`)
- **Pipeline**: `model_profiling/scripts/mac_pipeline.py`, `model_profiling/scripts/android_pipeline.py`, and/or `model_profiling/pipeline/*`
- **Analysis tools**: `model_profiling/tools/*` (ETDump conversion, operator categorization, kernel view generation)
- **Configs/examples**: `model_profiling/configs/` (sample configs that match the learning path)

## Deliverable expectations for the rewrite

- **Fewer pages, higher information density** (avoid repetition / trivia).
- **Clear connections** between: stack → export → run → artifacts → analysis → report.
- **Strong visual hierarchy**: short scannable sections, callouts, and correctly sized images with captions.
- **Validation gates**: per section, define “what you should see” (files/commands/expected metrics).

