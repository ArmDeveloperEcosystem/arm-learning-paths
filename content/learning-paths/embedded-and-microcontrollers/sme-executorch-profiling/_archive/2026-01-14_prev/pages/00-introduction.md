---
title: Introduction (what you’ll build and why it matters)
weight: 2
layout: "learningpathall"
---

<p>
  <img
    src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/sme2_stack.svg"
    alt="Runtime stack: PyTorch → ExecuTorch → XNNPACK → Arm Kleidi → SME2"
    class="content-uploaded-image centered"
  />
  <span class="content-image-caption centered">
    Runtime stack: PyTorch → ExecuTorch → XNNPACK → Arm Kleidi kernels → SME2 instructions.
  </span>
</p>

## What you will build (end-to-end)

<p>
  <img
    src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/step_flow_overview.svg"
    alt="Workflow overview: setup → build → export → run → analyze → automate"
    class="content-uploaded-image centered"
  />
  <span class="content-image-caption centered">
    Workflow: setup → build → export → run → analyze (and optionally automate).
  </span>
</p>

By the end, you will have a **repeatable, validated profiling workflow** that produces:

- `runs/mac/manifest.json` (run provenance, including ExecuTorch SHA)
- `runs/mac/metrics.json` (end-to-end latency summaries)
- `runs/mac/**.etdump` (operator-level traces)
- `runs/mac/analysis_summary.json` (category + operator-level breakdown, with kernel hints)

## What you will learn (the insights)

### 1) SME2 is either “actually used” or it isn’t
You will learn how to confirm, from your traces, whether SME2 kernels were used (for example kernel names containing `__neonsme2`).

### 2) SME2 changes *what* is slow
When compute-heavy ops become faster, **other costs become visible**—often data movement (layout conversions) or non-delegated operators.

### 3) Operator-level profiling gives actionable next steps
Instead of “latency is high”, you will see “these specific operators dominate” and can connect that back to export/delegation/layout decisions.

## Example outputs (what “good results” look like)

<p>
  <img
    src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/squeeze_sam_latency_comparison.png"
    alt="End-to-end latency comparison (SME2 on vs off)"
    class="content-uploaded-image centered"
  />
  <span class="content-image-caption centered">
    Example: end-to-end latency changes when SME2 is enabled.
  </span>
</p>

<p>
  <img
    src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/combined_operator_breakdown_stacked.png"
    alt="Operator category breakdown (SME2 shifts bottlenecks)"
    class="content-uploaded-image centered"
  />
  <span class="content-image-caption centered">
    Example: operator-category breakdown—compute shrinks, other costs become visible.
  </span>
</p>

## How to follow this learning path

- **Hands-on (human)**: continue to **Prerequisites** (page 01) and follow the steps.
- **Automation-first (AI / CI)**: start at **Automation workflows** (page 09), then use the playbooks in `agentic-kits/`.

