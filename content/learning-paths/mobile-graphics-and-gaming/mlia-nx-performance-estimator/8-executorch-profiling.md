---
title: (Optional) Analyze ExecuTorch ETRecord and ETDump profiling
description: Analyze matching ExecuTorch ETRecord and ETDump artifacts with MLIA, inspect runtime timings and VGF cycles, and optionally explore a companion PTE graph.
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare artifacts from your ExecuTorch deployment

Use this workflow when your application runs an ExecuTorch program and you already have its profiling artifacts. MLIA reads the captured data and reports measured performance. The earlier LiteRT conversion and Scenario Runner steps don't generate these artifacts.

Collect the following files from the same deployed program and model build:

| Artifact | Contents |
| --- | --- |
| `model.etrecord` or `model.bin` | Recorded model graphs and debug mappings generated during export |
| `run.etdump` or `run.etdp` | One matching runtime capture, including VGF profiling when enabled |
| `model.pte` (optional) | The deployed program containing a VGF delegate, for companion graph associations |

For artifact generation, see the [ExecuTorch 1.5 profiling tutorial](https://docs.pytorch.org/executorch/1.5/tutorials/devtools-integration-tutorial.html). VGF cycle analysis additionally requires VGF profiling data in the ETDump. An ordinary runtime-only capture can provide source timings, but it can't provide VGF counters or companion VGF associations.

Run the remaining commands from `mlia-demo`. Copy your artifacts into a new `et-profile` directory and use the example filenames above, or substitute their paths in the commands. Keep the original files together so that you can confirm which export and execution produced them.

## Install the ExecuTorch analysis support

Activate the environment from the setup page and install the Neural Technology `executorch` extra:

```bash
source mlia-venv/bin/activate
python -m pip install "mlia-neural-technology[executorch]==0.3.0" mlia-converters-pytorch==0.1.4
python -m pip check
```

This extra installs the shared ExecuTorch artifact readers from `mlia-converters-pytorch`. Neural Technology provides the runtime analysis, VGF decoding, and NX metrics. The converter package requires ExecuTorch `1.5.1`; use compatible artifacts from that toolchain.

The expected output from `pip check` is `No broken requirements found.` Model Explorer is optional for the analysis itself.

## Analyze the matching ETRecord and ETDump

Run a measured performance check:

```bash
mlia check et-profile/model.etrecord \
  --target-profile neural-technology \
  --performance \
  --profiling-data et-profile/run.etdump \
  --output-dir runs/executorch-measured
```

`--profiling-data` selects the measured backend automatically. Use performance analysis for this workflow; compatibility analysis belongs to the earlier model-based checks.

For an ETRecord with several methods, select the method that produced the dump. For example, append the following option for a method named `decode`:

```text
--neural-technology-profiling-data.etrecord-method decode
```

Single-method selection is automatic. If method selection or graph mapping fails, check that the artifacts come from the same deployed program and selected method.

Inspect the saved results and warnings:

```bash
python - <<'PY'
import json
from pathlib import Path

report_path = Path("runs/executorch-measured/mlia-output/mlia-output.json")
report = json.loads(report_path.read_text())
results = [result for result in report["results"] if result["kind"] == "performance"]
assert results, "No performance results found. Review the MLIA log."
for result in results:
    assert result["status"] == "ok", "Review the performance result for errors."
    assert result.get("mode") == "measured", "Expected measured profiling data."
    print(json.dumps(result, indent=2))
PY
```

The check confirms that MLIA produced successful measured performance results and prints their metrics, breakdowns, and any warnings. Values depend on your capture. Check the reported execution coverage and decoder assumptions before treating cycle summaries as full-inference costs.

## (Optional) Open the profiling views in Model Explorer

Use Model Explorer `0.2.0`, which supports MLIA core `0.13.x`. Install its `executorch` extra in the same environment, even if you installed the `vgf` extra during setup:

```bash
python -m pip install "mlia-model-explorer[executorch]==0.2.0"
python -m pip check
```

The extra includes ETRecord, PTE, and VGF adapters. After `pip check` succeeds, rerun the analysis into a separate directory and request a visualization:

```bash
mlia check et-profile/model.etrecord \
  --target-profile neural-technology \
  --performance \
  --profiling-data et-profile/run.etdump \
  --output-dir runs/executorch-visualized \
  --model-explorer open
```

If you also have the matching deployed VGF-backed PTE and VGF profiling in the dump, append `--companion-model et-profile/model.pte` to add its compiler graph. Supplying a companion alone doesn't enable visualization. Runtime-only captures support visualization without a companion.

Use `--model-explorer files` to generate the files without opening a browser. The standalone page is `runs/executorch-visualized/mlia-output/model-explorer/bundle/index.html`.

In Model Explorer, inspect the views available for your capture:

| View | What to inspect |
| --- | --- |
| **Source Model** | Source operators and available runtime timings |
| **segment_cascade_chain** | Captured NX hierarchy and cycle measurements |
| **ETRecord Chain Mapping** | Chains associated with source operators; the initial detailed view when available |
| **ETDump Backend Trace** | Compiler operations and their measured chain groups |
| **PTE - VGF Backend Hierarchy** | Companion compiler graph and associated chain groups, when supplied |

Select a mapped operator or group to navigate between related views. Compiler transformations can rename, insert, combine, or reorder operations, so some source links can be incomplete or absent. Unmatched compiler operations remain visible. A missing link doesn't establish that an operation wasn't executed or that its chain has no profiling data.

## Interpret runtime timings and NX counters

Ordinary runtime timings use milliseconds. VGF counters use cycles and describe recorded accelerator activity. Cycle counters don't reconstruct idle gaps or establish elapsed latency.

Repeated executions provide averages, minimum, maximum, P50, and execution counts where supported. Independent observations are combined within each recorded execution before summaries are calculated. Don't add minimum, maximum, P50, or execution counts across operators. Averages can be combined only when their measurements are independent and cover the same executions.

A runtime event can cover several source operators. Each associated operator can display the same shared timing; that value isn't an independent cost for each operator. VGF chain or cascade measurements can also cover several compiler operations. Use the authoritative hierarchy measurements and model-level results instead of summing every overlay or hierarchy level.

Mixed-backend dumps keep ordinary runtime timings separate from VGF counters. Instructions with VGF profiling are excluded from ordinary runtime aggregation to avoid counting the same work twice. Runtime event counts describe contributing event records, rather than the number of complete inferences.

MLIA doesn't estimate missing measurements. If instructions or segments cover different executions, model cycle summaries can be unavailable with a warning while individual measurements remain available. Even matching coverage doesn't prove every expected stripe was captured. Review warnings and, for older captures, any assumed statistics mode or device layout.

Companion matching checks structural compatibility and assumes you supplied the matching PTE. It doesn't prove that the PTE produced the capture. Model Explorer checks that the companion file hasn't changed since analysis; rerun analysis if it has.

## What you've accomplished

You've analyzed an ExecuTorch ETRecord/ETDump pair and checked its measured results. With a compatible Model Explorer installation, you can also inspect runtime timings, NX hierarchy measurements, and optional companion graph associations.

Use the measured costs to select a model change to investigate. Repeat the capture under the same conditions and validate accuracy before drawing deployment conclusions.
