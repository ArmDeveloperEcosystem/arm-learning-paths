# SME2 ExecuTorch Profiling Learning Path — Proposed Structure & Implementation Plan

This plan assesses and improves the proposed structure, grounded in the referenced materials (especially the **Part 2 reproduction guide** and the **blog final**), before we make content changes in `arm-learning-paths-sme2-executorch`.

## A. What the references imply (key design constraints)

From the blog final (text extract for working notes, kept in-folder):

- `content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/_rewrite/blog_draft_sme2_executorch_01062026-CLEAN.txt`

Key implications:

- The story arc is: **SME2 speedups → operator profiling → transpose/data-movement bottleneck → “here’s a hands-on repo + learning path”**.
- The “hands-on” promise is specifically:
  - export to ExecuTorch with XNNPACK delegation,
  - build/run on SME2-enabled devices,
  - collect ETDump operator timing,
  - identify/quantify data movement bottlenecks.

From the reproduction guide Part 2 (`/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/out_squeeze_sam/report/SqueezeSAM_Transpose_Overhead_Analysis_and_Reproduction_Guide.md`):

- The reader needs a **self-service** workflow with an explicit **repo structure**:
  - `executorch/` + `model_profiling/` side-by-side (or env var override),
  - model onboarding via `model_profiling/models/`,
  - export via `model_profiling/export/export_model.py`,
  - pipeline + analysis producing artifacts in `model_profiling/out_<model>/...`.

From the profiling workflow (`/Users/jaszhu01/Local/Github/sme2_executorch/PROFILING_WORKFLOW.md`):

- The essential workflow collapses cleanly into 4 actions:
  - **Export model → Create config → Run pipeline → Review results**

## B. Improved information architecture (IA): `_index.md` landing + 4 content pages (explicit filenames)

### Target file map (what we will actually create)

- Landing (existing): `_index.md` (frontmatter-driven landing/wayfinding; keep structure minimal)
- Page 1: `01-overview.md` (stop-here “Overview + Quickstart”)
- Page 2: `02-setup-and-model-onboarding.md` (env + model onboarding contract; includes EdgeTAM example)
- Page 3: `03-pipeline-and-analysis.md` (runner variants + config + run + analysis; includes xnntrace/kernel logging)
- Page 4: `04-agent-skills.md` (agent workflows + validation gates + sample use-cases)

Everything else in the current folder (the old 9-step series, including `00-introduction.md`) will be archived under `_archive/` and removed from the active learning-path navigation.

### Page 0 (landing): `_index.md` (structure fixed; keep it as wayfinding only)

Constraint: we cannot change the effective structure/rendering of `_index.md` in this repo/theme, so `_index.md` should stay a **clean landing / wayfinding** page driven by frontmatter and light content only.

**Goal**: get the reader oriented in <60 seconds and funnel them to the full Overview page.

**Sections (clear overview + “get the code” first; skimmable but not cramped)**:

- **What this is**: 2–3 sentence context (interactive segmentation / SME2 case study).
- **What you’ll do**: 3–5 bullets (export → run → profile → analyze → report).
- **Entry button/link**: “Start: Overview + Quickstart” (next page).
- **Optional small visuals**: 1 small stack diagram thumbnail + 1 results thumbnail (no giant images).

**Design requirements**:

- No giant hero images; use **max-width** constraints and consistent captions.
- Use short “cards”/callouts, and keep tables narrow.
- Avoid the “giant headline + tiny text” mismatch: enforce a single typographic rhythm (H2/H3 + body).

---

### Page 1: `01-overview.md` (stop-here page: Overview + Quickstart)

**Goal**: a reader can stop here and still:

- understand the stack + why SME2 matters,
- see expected results and what “good” looks like,
- copy/paste minimal commands to run the workflow in their own workspace.

**Sections (clear overview + “get the code package” first; skimmable but not cramped)**:

- **Get the code package (primary)**:
  - where the “profiling kit” lives in this repo
  - minimal copy/paste to pull it into a workspace
  - what folder layout you should end up with
- **The stack (diagram)**: PyTorch → ExecuTorch → XNNPACK → Arm KleidiAI → SME2.
- **Expected results (small visuals)**:
  - latency comparison chart (SME2 on/off)
  - operator/category stacked breakdown (show bottleneck shift to data movement)
  - (optional) transpose hotspot callout
- **What you get (expected outputs)**: list the exact artifacts:
  - `.pte`
  - `.etdump`
  - `*_robust_stats.json`
  - operator/category breakdown CSV/JSON
  - optional XNN trace / kernel view
  - a “report template” output (or a sample report link)
- **Download the code (two modes)**:
  - **Mode A (recommended)**: use the in-repo “profiling kit” folder
  - **Mode B (advanced)**: clone ExecuTorch + point `EXECUTORCH_REPO` to it
- **Quickstart (copy/paste)**:
  - preflight
  - export
  - run pipeline
  - open outputs

**Validation gate (“what you should see”)**:

- 1 command prints: “export ok”, “pipeline ok”
- output directory exists with the exact artifact list above.

---

### Page 2: `setup-and-model-onboarding.md` (env setup + onboarding = the centerpiece)

### Page 2: `02-setup-and-model-onboarding.md` (env setup + onboarding = the centerpiece)

**Goal**: make onboarding a new model feel *obvious* and *repeatable*, while keeping the **pipeline model-agnostic** (swap model package + exported artifacts + config; pipeline stays unchanged).

**Sections**:

- **Minimal env setup (few lines)** (don’t bury the lead; link out for edge cases): derive from:
  - `/Users/jaszhu01/Local/Github/sme2_executorch/pr16533_env_setup.md`
- **Repo layout (canonical)**: copy the structure from Part 2 reproduction guide.
- **Model onboarding contract**:
  - where model code lives
  - how it registers itself
  - what the exporter expects (inputs, sample inputs, shapes, dtype)
  - what must remain model-agnostic (pipeline + analysis tooling)
  - **advanced onboarding example (EdgeTAM image encoder)**:
    - document the typical “hard mode” edits (wrappers/refactors/op fixes) required to make it exportable
    - end with the same artifact contract: `.pte` (+ metadata) that plugs into the unchanged pipeline
- **The exporter**:
  - document the key flags that matter and their outputs, based on:
    - `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/export/export_model.py`
  - include a “minimum export” and “debug export” mode.
- **What to commit vs what to fetch**:
  - model vendor code and weights are too large to embed; provide a fetch step.

**Validation gate**:

- `python ... export_model.py --model <name> ...` produces:
  - `<outdir>/*.pte`
  - optional `graph.json`
  - `export_meta.json` (if we add it) containing model name, dtype, backend, shapes.
  - the resulting `.pte` is runnable by the *same* runner + pipeline commands used for other models (no code changes).

---

### Page 3: `03-pipeline-and-analysis.md` (runner build + config + run + analysis on one page)

**Goal**: a single, linear “do this, then that” page.

**Sections**:

- **Build runners (mac + android)**:
  - summarise presets and why SME2 on/off exists
  - call out **logging variants** explicitly (timing-only vs ETDump vs XNNPACK kernel trace / xnntrace runners) and when to use each
  - link deeper details only if needed
- **Create config**:
  - show a minimal JSON config
  - list required keys + defaults
- **Run pipeline**:
  - mac pipeline
  - android pipeline (optional block)
- **Read results**:
  - robust stats
  - operator/category view
  - how to spot “transpose/layout churn” quickly
  - kernel view (optional)

**Validation gate**:

- output dir contains:
  - robust stats JSON
  - operator stats CSV/JSON
  - ETDump trace
  - (optional) kernel comparison artifacts

---

### Page 4: `04-agent-skills.md` (automation workflows for AI assistants / CI)

**Goal**: make “agentic usage” real: inputs/outputs, checks, and examples.

**Sections**:

- **Skill contracts** (each skill: inputs → steps → outputs → verification):
  - `skill.env_setup`
  - `skill.export_model`
  - `skill.build_runners`
  - `skill.run_pipeline`
  - `skill.summarize_results`
- **Test use cases**:
  - minimal smoke test
  - regression check against a known-good run
- **Sample outputs**:
  - a sample report (link to sample report MD)
  - example JSON/CSV snippets

**Validation gate**:

- each skill has an automated check (file exists, command returns 0, required keys present).

## C. Practical note: `_index.md` is landing-only by design here

We will not attempt to put the full quickstart on `_index.md`. Instead:

- `_index.md` stays as wayfinding + minimal visuals.
- The full “stop here” experience lives on the next page: `01-overview.md`.

## D. Reference-driven quality bar (what “good” looks like)

Use these reports as the “presentation + completeness” bar:

- `/Users/jaszhu01/Local/Github/sme2_executorch/reference/SqueezeSAM_SME2_Performance_Report_12022025.md`
- `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/out_squeeze_sam/report/SqueezeSAM_INT8_SME2_Performance_Report.md`

## E. Next steps (before editing the site content)

1) Keep `_index.md` as landing-only, and create `01-overview.md` as the “stop-here” page.
2) Decide what code we ship **inside** this learning path repo vs what we fetch/clone externally (to avoid vendored weights).
3) Archive the existing learning-path folder contents (no deletion) and start the new 4-page set.

## G. Archival move proposal (preserve old content, restart cleanly)

User request: “save the content under this folder into a place outside the learning path folder.”

### What we will archive

- Current folder:
  - `content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/`

### Where we will archive it (proposal; must stay inside `sme-executorch-profiling/`)

To comply with “only change files under `sme-executorch-profiling/`”, we will archive under an underscore-prefixed folder to keep it out of normal navigation/publishing:

- `content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/_archive/2026-01-14_prev/`

### How we will do it (safe + reversible)

- **Copy** (not move) the entire folder into the archive location first.
- Verify the archive copy exists and has the same file count.
- Then **replace** the published learning path folder contents with the new 4-page version.

This preserves all the previous SVGs/images/markdown for future reuse without keeping the old navigation structure live.

## F. Scripts/assets to copy from `sme2_executorch` (proposed)

This is the explicit “copy list” requested, with **source** (absolute path) and a proposed **destination** inside this repo (final destination can be adjusted once we decide the “profiling kit” folder layout).

### Core framework (must-have)

- **Local model registry + ExecuTorch registry patch hook**
  - **Source**: `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/models/__init__.py`
  - **Source**: `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/models/model_base.py`
  - **Dest (proposal)**: `content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/models/`
  - **Notes**: This enables `export_model.py` to export locally-onboarded models without editing ExecuTorch sources.

- **Exporter (the onboarding centerpiece)**
  - **Source**: `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/export/export_model.py`
  - **Dest (proposal)**: `.../executorch_sme2_kit/model_profiling/export/export_model.py`
  - **Also copy**:
    - `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/export/EXPORT_COMMANDS.md`
    - `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/export/export_all_models.sh`

- **Pipeline runner CLIs**
  - **Source**: `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/scripts/mac_pipeline.py`
  - **Source**: `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/scripts/android_pipeline.py`
  - **Dest (proposal)**: `.../executorch_sme2_kit/model_profiling/scripts/`

- **Pipeline internals (needed by the CLIs)**
  - **Source dir**: `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/pipeline/`
  - **Dest (proposal)**: `.../executorch_sme2_kit/model_profiling/pipeline/`
  - **Notes**: includes config parsing, orchestration, and analysis hooks.

- **Analysis tools (standalone and used by pipeline)**
  - **Source dir**: `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/tools/`
  - **Dest (proposal)**: `.../executorch_sme2_kit/model_profiling/tools/`
  - **High-signal tools to call out in docs**:
    - `etdump_to_csv.py`, `etdump_to_ops_json.py`
    - `robust_latency_analysis.py`
    - `categorize_operators.py`, `analyze_etdump_csv.py`
    - `xnntrace_to_kernels.py`, `generate_kernel_view.py`
    - `analyze_transpose_patterns.py` (ties to the transpose overhead story)

### Configs + examples (must-have for usability)

- **Configs**
  - **Source dir**: `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/configs/`
  - **Dest (proposal)**: `.../executorch_sme2_kit/model_profiling/configs/`
  - **Notes**: we should include at least 1 minimal mac config + 1 android config.

### Model packages (careful: avoid vendored weights in this repo)

- **SqueezeSAM onboarding package (code only; avoid weights)**
  - **Source dir**: `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/models/squeeze_sam/`
  - **Source dir**: `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/models/mobile_sam/` (optional)
  - **Dest (proposal)**: `.../executorch_sme2_kit/model_profiling/models/`
  - **Notes**:
    - Do **not** copy `vendor/weights/*` into this repo unless explicitly approved (likely too large).
    - Instead, provide “fetch weights” scripts and pin exact upstream commits.

### Documentation seeds to reuse in the learning path pages

- **Repro guide Part 2**
  - **Source**: `/Users/jaszhu01/Local/Github/sme2_executorch/model_profiling/out_squeeze_sam/report/SqueezeSAM_Transpose_Overhead_Analysis_and_Reproduction_Guide.md`
  - **Usage**: the learning path’s “overview/quickstart”, onboarding structure, and pipeline narrative should align to this.

- **Workflow quick start**
  - **Source**: `/Users/jaszhu01/Local/Github/sme2_executorch/PROFILING_WORKFLOW.md`
  - **Usage**: fold into the single “pipeline + analysis” page.

- **Env setup (fresh PR checkout)**
  - **Source**: `/Users/jaszhu01/Local/Github/sme2_executorch/pr16533_env_setup.md`
  - **Usage**: compress into the minimal env setup section.

