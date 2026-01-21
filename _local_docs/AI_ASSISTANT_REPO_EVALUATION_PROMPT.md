# AI Assistant Prompt: Evaluate + Iteratively Improve Learning Path Repo (Quality & Usability)

Use this prompt with an AI coding assistant to evaluate and iteratively improve this repo’s learning-path content and local toolkits.

## Scope

Primary target learning path folder:
- `content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/`

This learning path includes:
- Web pages (`*.md`) rendered by Hugo
- A self-contained local profiling kit: `scripts/`, `configs/`, `test-cases/`, and `agentic-kits/` (local-only playbooks; should not render as normal web pages)

## Copy/paste prompt (give this to an AI assistant)

You are an expert technical writer + build engineer + on-device ML performance engineer. Your job is to **evaluate the quality and usability** of this learning path content repo and propose **concrete, minimal, high-leverage improvements** that raise it toward a **9.8/10**.

### Context

This repo contains a learning path: **“SME2 ExecuTorch profiling”**. It has:

- Web pages under:
  - `content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/*.md`
- A **self-contained local profiling kit** under:
  - `content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/`
    - `scripts/` (setup/build/pipeline/analyze/validate)
    - `configs/templates/` and `configs/examples/`
    - `agentic-kits/` (AI automation playbooks; should not render as web pages)
    - `test-cases/fixtures/known_good_mac/` (known-good schema fixture + tests)

Your evaluation must be both:
- **Human-first** (average developer, not an expert)
- **AI-first** (can an AI coding assistant autonomously run it, validate it, troubleshoot it)

### Before you start

Confirm you have access to:
- The full repo contents (or at least the learning path folder via sparse checkout)
- Ability to read all files in `content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/`
- (Optional but preferred) Ability to run commands to validate the "quick flow" end-to-end

If you cannot run commands, state this upfront and base your evaluation on code review + manifest inspection.

**Time budget**: Plan for 60–90 minutes of evaluation (cold-read + simulated journey + scoring + backlog).

**Quick self-check (confirm before proceeding)**:
- [ ] I understand this is about **SME2 ExecuTorch profiling** (not a generic ExecuTorch guide)
- [ ] I will evaluate both **web pages** (Hugo-rendered) and **local kits** (scripts/agentic-kits)
- [ ] I will score using the 8-dimension rubric and compute a weighted total
- [ ] My output will follow the mandatory format (8 sections)

### What you must do

1. **Do a cold-read** of the key entrypoints (don’t assume prior knowledge):
   - Web landing + flow pages: `_index.md`, `01-09 *.md` (especially `02`, `03`, `05`, `06`, `07`, `09`)
   - Human local entrypoint: `scripts/README.md`
   - AI local entrypoint: `agentic-kits/README.md` + the `*-agent.md` files

2. **Simulate an average developer journey**:
   - Identify the first place they might get stuck
   - Evaluate whether expected outputs, validation gates, and troubleshooting are sufficient
   - Check whether it’s clear what “done” looks like and how long things take

3. **Simulate an AI assistant journey**:
   - Determine if the repo provides enough “operational truth” (exact commands, prerequisites, output checks, known-good validation)
   - Check for brittle steps (manual edits, missing prereqs, ambiguous file paths)
   - Verify the agentic kits read like executable playbooks (not prose)

4. **Score the repo** using the rubric below and explain the score with evidence and file references.

5. Provide a **prioritized improvement backlog (top 6–8 items)**, each with:
   - Goal (why it matters)
   - Exact file(s) to change
   - Concrete edits (bullet points; include example command/output snippets when useful)
   - Expected impact on the score (e.g., +0.2)

6. Provide a **known-good validation checklist** (minimum commands to confirm "this repo works"), suitable for:
   - A new user validating their setup
   - An AI agent deciding "pass/fail"
   - CI/automation (if applicable)

### Constraints and non-goals

- Do not propose large rewrites. Prefer **small, high-leverage edits**.
- Prefer `.sh` for orchestration; Python only when it adds unique value (export/analysis/utilities).
- The repo must remain compatible with being served by Hugo, and **`agentic-kits/*.md` must not render as normal web pages**.
- Balance commands with essential snippets and sample outputs (human-friendly and operator-grade).

---

## Rubric (0–10 each, explicit criteria + validation callouts; weighted total; target 9.8/10)

### Scoring rules (apply to all dimensions)

- **0–2**: Broken or missing; cannot complete the workflow without external help.
- **3–5**: Works with significant friction; missing key expected outputs/validation; frequent ambiguity.
- **6–7**: Works reliably for most users; some unclear spots; validation exists but not first-class.
- **8–9**: Polished and dependable; minor nits; validation gates are clear and repeatable.
- **9.5–10**: “Tech blogpost gold standard”: vivid, operator-grade insights, minimal ambiguity, strong validation gates, and agent-automation-ready.

For every dimension, include **(a) score, (b) justification with file references, (c) what to validate**.

### 1) Time-to-first-success (Weight 0.20)

**Measures**: Can an average dev get a first successful run quickly.
- **10**: Fresh checkout → first pipeline success in **≤60 min**, with **≤30 min setup**, and at least **one fast preflight** that fails early with actionable messages.
- **9**: Typically ≤75 min; a few manual steps but clearly explained; preflight exists.
- **7**: Often 1–2 hours; missing time estimates or some non-obvious prerequisites.
- **5**: Unpredictable time; users frequently stuck due to missing tools.
- **0–3**: No reliable first success path.

**Validate**:
- From clean repo state: run the documented “quick flow” exactly as written.
- Confirm time estimates match reality and failures occur early with clear errors (prereqs/pip/cmake).

### 2) Flow clarity + mental model (Weight 0.12)

**Measures**: Whether the reader understands the pipeline and why.
- **10**: Clear “what you will build”, clear pipeline diagram/mental model, and crisp “why this matters” connecting profiling → SME2 insights → actions.
- **9**: Mostly clear; minor jumps; still outcome-driven.
- **7**: Steps exist but rationale is thin; readers can execute but not explain.
- **5**: Fragmented; users follow commands blindly.
- **0–3**: Confusing structure; unclear purpose.

**Validate**:
- Ask: “After reading, can a typical dev explain what an ETDump is and what `analysis_summary.json` means?”
- Verify each page has a concrete outcome and checkpoint.

### 3) Command correctness + copy/paste fidelity (Weight 0.12)

**Measures**: Commands match reality and are safe to run.
- **10**: Every command works copy/paste; flags/paths match scripts; no stale argument names; no hidden assumptions.
- **9**: One or two minor typos/edge cases; overall reliable.
- **7**: Several mismatches or missing flags; users must improvise.
- **5**: Frequent command drift vs code; breaks flow.
- **0–3**: Commands largely unusable.

**Validate**:
- Execute every code block in the quick path on a clean workspace.
- Verify scripts’ `--help` aligns with docs; ensure template configs are referenced consistently.

### 4) Validation gates + “what good looks like” (Weight 0.16)

**Measures**: Whether the repo provides deterministic success criteria.
- **10**: Clear validations after each stage (setup/build/run/analyze). Includes expected files and sample outputs. Includes **known-good fixture** and comparison that is robust (schema + sanity thresholds).
- **9**: Strong validation but one stage is weaker or under-documented.
- **7**: Some checks exist, but not integrated into the narrative; limited expected outputs.
- **5**: Validation is ad-hoc; users don’t know if results are correct.
- **0–3**: No validation.

**Validate**:
- Run `validate_setup`, `validate_results`, and known-good comparison as documented.
- Confirm outputs: `manifest.json`, `metrics.json`, `analysis_summary.json`, and `.etdump` presence.

### 5) Profiling insight quality (operator-level profiling + SME2 interpretation) (Weight 0.14)

**Measures**: Whether the content delivers "operator-level profiling insights" and ties to SME2.
- **10**: Explains nested events pitfalls, correct E2E computation, category breakdown, kernel hint interpretation (`__neonsme2`), and gives actionable “what to optimize next”.
- **9**: Good insight, minor missing nuance or fewer examples.
- **7**: Mostly procedural; limited interpretive guidance.
- **5**: Superficial; doesn’t teach profiling reasoning.
- **0–3**: No meaningful profiling insight.

**Validate**:
- Confirm analysis scripts produce operator/category summaries.
- Confirm docs explain interpreting deltas SME2-on vs off and what signals confirm SME2 path.

### 6) Troubleshooting effectiveness (Weight 0.10)

**Measures**: How quickly users recover from common failures.
- **10**: Most common failures covered with symptom → cause → fix, and “how to confirm it’s fixed”.
- **9**: Strong, missing 1–2 common cases.
- **7**: Some troubleshooting but shallow or not linked from main flow.
- **5**: Sparse; users resort to internet searches.
- **0–3**: None.

**Validate**:
- Intentionally break prerequisites (missing cmake/ndk/adb) and confirm messages are actionable.
- Validate stale download/build cache recovery guidance.

### 7) Agentic automation readiness (Weight 0.10)

**Measures**: Whether an AI coding assistant can run it autonomously and safely.
- **10**: Agent playbooks are deterministic: required tools listed, exact commands, expected outputs, validation gates, and minimal “human editing” ambiguity. Includes known-good run comparison and cleanup guidance.
- **9**: Mostly there; one weak spot (e.g., config edit ambiguity).
- **7**: Agent kits exist but missing gates or tool assumptions.
- **5**: Too much prose; not executable as a workflow.
- **0–3**: No agent-first materials.

**Validate**:
- Hand the agent only `agentic-kits/README.md` and see if it can complete setup→run→validate without reading the whole site.
- Confirm it can decide “pass/fail” via validators and fixture compare.

### 8) Reproducibility + provenance (Weight 0.06)

**Measures**: Whether results are attributable and portable.
- **10**: Records ExecuTorch SHA + dirty state, device info (Android), config used, relative paths in manifests, and has a cleanup/reset story. Minimal nondeterminism.
- **9**: Strong, minor metadata gaps.
- **7**: Some metadata, incomplete provenance.
- **5**: Hard to reproduce; missing version capture.
- **0–3**: No provenance.

**Validate**:
- Check `manifest.json` captures SHA and portable file references.
- Verify rerun produces comparable output schema.

---

## Weighted total score calculation (required)

Compute:

\[
\text{Total} = \sum_i (w_i \times s_i)
\]

Where each \(s_i \in [0, 10]\) and weights sum to **1.0**. Report:
- Per-dimension score + evidence
- Weighted total (0–10)
- Gap to **9.8** and the **top 3 changes** that would most increase the score

---

## Mandatory output format (required)

Return your response with these headings and content:

1. **Executive summary (5 bullets max)**

2. **Scorecard (table)**
   - Format: `| Dimension | Weight | Score | Evidence (file + line/section) |`
   - Include weighted subtotal per dimension and final weighted total
   - Show gap to 9.8 and which dimension(s) have the most room to improve

3. **Top 10 friction points (human)**

4. **Top 10 friction points (AI agent)**

5. **High-leverage improvements (prioritized backlog, top 6–8 items)**

6. **Known-good validation checklist (minimum commands)**

7. **One "golden path" narrative (8–12 sentences)**
   - Describe the ideal user journey from sparse checkout to first validated run
   - Include time estimates, key decision points, and "what good looks like" checkpoints
   - Written as if onboarding a colleague who's never seen the repo

8. **Risks / unknowns / assumptions**
   - What you couldn't validate without running on real hardware (e.g., Android/SME2 device)
   - Assumptions you made about the user's environment or skill level
   - Any repo state issues (e.g., missing fixture data, broken links)

When citing evidence, reference files using backticks (e.g., `scripts/README.md`) and quote short snippets if needed.

---

## Mandatory “areas to validate” section

After scoring, include a concise checklist titled **“Validation hotspots (must verify)”** with:
- **Setup**: prereqs + venv + ExecuTorch SHA capture
- **Build**: SME2 on/off runners built; Android optional gates
- **Run**: `.etdump` produced; logs captured
- **Analyze**: `analysis_summary.json` produced; E2E latency populated
- **Compare**: known-good fixture compare passes (schema + sanity)
- **Cleanup**: generated artifacts removable without deleting authored content


