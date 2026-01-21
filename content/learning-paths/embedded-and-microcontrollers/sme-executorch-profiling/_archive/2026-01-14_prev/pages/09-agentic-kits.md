---
title: "Automation workflows (for AI assistants and CI)"
weight: 3
layout: "learningpathall"
---

<p>
  <img
    src="/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/images/agent_workflow.svg"
    alt="Automation workflow: preflight → setup → run → validate/compare"
    class="content-uploaded-image centered"
  />
  <span class="content-image-caption centered">
    Workflow: preflight → setup → run → validate/compare.
  </span>
</p>

## What this is (and who it is for)

This learning path includes a set of **automation workflows** for AI coding assistants (Cursor, Copilot, Claude Code, Codex, etc.) and for CI automation.

They are designed to be:
- **deterministic** (config-driven, minimal interactive steps)
- **validated** (explicit gates: prereqs → run → validate → compare)
- **reproducible** (record ExecuTorch SHA in the run manifest)

## Where the workflows live

After sparse checkout, the workflows are in:
- `agentic-kits/`

Start here:
- `agentic-kits/README.md`

## The “agent contract” (what an assistant should do)

An AI assistant should treat each workflow as a contract:
- **Inputs**: a config JSON + a model (`.pte` + `.etrecord`)
- **Outputs**: a run directory (`manifest.json`, `metrics.json`, `*.etdump`, logs)
- **Validation**: `validate_results.py` and `compare_run_to_known_good.py`

## How to use them

- **Hands-on readers**: you can ignore this page and follow 01 → 08.
- **AI / automation users**: start here, then run playbooks in order (setup → pipeline → validation → troubleshooting).

{{% notice Note %}}
The `agentic-kits/*.md` files are not meant to be read as tutorial prose. They are operational runbooks with explicit commands and validation gates.
{{% /notice %}}


