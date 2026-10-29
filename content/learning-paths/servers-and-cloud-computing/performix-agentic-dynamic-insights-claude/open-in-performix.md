---
title: Open the run in Arm Performix for deeper inspection

weight: 6

description: Validate an AI insight by inspecting flame graphs, functions, call paths, source, and disassembly from the same Arm Performix run.

layout: learningpathall
---
## Open the selected run

A chat response helps you triage a performance problem, but the underlying profile is the source of evidence. Use the run ID from your insight request to retrieve the profile's details. From a terminal with `apx` on your `PATH`, run:

```console
apx run info "<run-id>"
```

Replace `<run-id>` with the ID you recorded. Use the returned workload, recipe, target information, and timestamps to identify the corresponding run in the GUI:

1. Open Arm Performix on the host that stores the run used by the MCP server.
2. Select **Runs** in the activity bar on the left, or select **Explore run data** on the home page.
3. Locate the Code Hotspots run using its timestamp, recipe, and workload labels, then select it to open its results.
4. Open **Run Details** and compare the workload, execution times, target configuration, and recipe parameters with the selected run's details. Don't rely on the display name alone.

If you can't identify the matching run, return to the MCP connection page's [missing-run checks](/learning-paths/servers-and-cloud-computing/performix-agentic-dynamic-insights-claude/configure_mcp_claude/#code-hotspots-runs-are-missing) before evaluating the insight.

## Validate the insight in Arm Performix

Inspect the views relevant to the claim:

- **Flame graph** to see where sampled CPU time accumulates across call paths
- **Functions** to confirm which functions account for the largest sample percentages
- **Call Stack** to distinguish a function's own cost from the cost of its callees
- **Source** to correlate samples with source lines when source mapping is available
- **Disassembly** to inspect generated instructions and confirm claims about the compiled code
- **Compare** to evaluate equivalent before-and-after runs

For a concrete check of the highest-impact hotspot finding:

1. Record the function name, sample count or percentage, and call path cited by Claude Code. If the response omits these details, ask for them before continuing.
2. Locate the function in **Functions** and compare the reported metric with the profile. Use the same filters and distinguish samples attributed to the function itself from samples that include its callees.
3. Open **Call Stack** and check that the cited callers and callees match the profile.
4. If the recommendation refers to a source line or instruction, double-click the function to open the **Source Code Viewer**. Use **Source**, **Disassembly**, or **Split** to inspect the claim. If source mapping is missing, select **Specify Root Directory** and choose the matching source tree on your host.
5. Record whether the observation matches, conflicts with, or can't be established from the available data. Ask Claude Code to revise any finding whose function, metric, or call path doesn't match.

Matching a hotspot metric confirms the observation. It doesn't establish that the proposed optimization will improve performance; validate that separately with a controlled before-and-after measurement.

Use the AI insight to focus your investigation, not replace it. For example, if the insight says a loop appears scalar, inspect its disassembly and compiler flags before changing the implementation. If Code Hotspots only shows that the loop is hot, run Instruction Mix or another appropriate recipe before concluding that scalar execution is the cause.

For a before-and-after comparison, keep the workload, target, input, thread count, CPU affinity, and collection settings consistent. A lower sample percentage doesn't prove that a function became faster if total runtime or the surrounding workload changed.

## What you've accomplished

You've now configured the Arm Performix MCP server, selected or created a Code Hotspots run, generated an AI insight, and checked its recommendation against the profile.

You can continue with the [Arm Performix getting-started video](https://youtu.be/_eX8ZpNT0kc) to explore the graphical workflow.
