---
title: Read the report and drive the improvement loop
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The analysis report

After every recipe run, the skill returns a structured report instead of raw
data. Expect these sections:

- **Bottleneck Summary**: what dominates, and how confident the skill is
- **Key Metrics**: the three to five most decision-relevant numbers
- **Hot Functions**: ranked, each with a brief root-cause note
- **Recommended Actions**: concrete, prioritized fixes (file, function, line)
- **Ruled Out**: hypotheses the data did *not* support, and why
- **Next Step**: a single actionable instruction to run next, such as the next
  recipe to try or one code change to make, then re-profile

This report is the skill's primary deliverable. If the data is noisy or
insufficient, the skill says so plainly and recommends a re-run rather than
guessing.

## A worked example

For a compute-bound workload, a first Code Hotspots report from the skill looks
like this:

```markdown
## Performix Analysis Report

**Recipe:** Code Hotspots
**Target:** neoverse-box (Arm Neoverse, 64 cores)
**Workload:** /home/me/build/myapp --input /home/me/data/bench.dat

### Bottleneck Summary

The escape-check loop in `escape_iterations` dominates CPU time (72% of samples),
driven by an avoidable `sqrt` call inside the tight iteration. High confidence:
a single function, stable across runs.

### Key Metrics

| Metric | Value | Assessment |
|--------|-------|------------|
| escape_iterations self % | 72.3% | Critical: single dominant hotspot |
| sqrt self % | 45.1% | Critical: unnecessary math |
| Total samples | 48,201 | Good: enough for reliable data |

### Hot Functions

| # | Function | Samples (%) | Root Cause |
|---|----------|-------------|------------|
| 1 | escape_iterations | 72.3% | sqrt in inner loop |
| 2 | sqrt | 45.1% | magnitude check in escape_iterations |

### Recommended Actions (priority order)

1. **Remove sqrt** in `mandelbrot.c:22`: replace `sqrt(zr2 + zi2) > 2.0` with
   `(zr2 + zi2) > 4.0`.

### Ruled Out

- Memory locality is not the issue: the hotspot is purely scalar floating-point
  compute.

### Next Step

Rebuild with the sqrt removal, re-run Code Hotspots, and confirm
escape_iterations falls under 30%.
```

The report names a file and line, ranks the cost by measured samples, and ends
with a single action you can take immediately, rather than a wall of raw
counters.

## Expect a two-pass investigation

The skill does not let a single Code Hotspots run justify "this is as fast as it
gets." Code Hotspots shows *where* time goes, never *why*. Expect the skill to
propose a **second pass** with a characterizing recipe (CPU Microarchitecture,
Instruction Mix, or Memory Access) to explain why the hot spot is hot. Let it
run that pass before deciding a cost is irreducible.

## Drive the improvement loop

Work with the skill one change at a time:

1. It establishes a **baseline** run.
2. You or the skill make **one** focused change.
3. It **re-profiles** with the same recipe and workload.
4. It reports a **before/after comparison** with a measurement, not a claim.
5. It looks for the **next bottleneck**, or summarizes the remaining trade-offs.

If you want to stop, ask for the remaining opportunities. The skill is designed to
hand you measured options with their trade-offs rather than declare the work
finished on its own.

{{% notice Tip %}}
If you are using the CLI, you can ask the skill to export a run or render results
as JSON:

```bash
apx run export <run_id> <target_directory>
apx run render <run_id> --json
```

Use the `Run ID` from the analysis report, or run `apx run list` to find it. The
`<target_directory>` is a directory on the host where Arm Performix writes the
exported `.zip` file. Run export/import and render commands are CLI workflows,
not MCP tool operations.
{{% /notice %}}

You now have a measurement-first workflow for using the arm-performix skill to profile Arm Neoverse workloads, read the results, and make focused improvements.
