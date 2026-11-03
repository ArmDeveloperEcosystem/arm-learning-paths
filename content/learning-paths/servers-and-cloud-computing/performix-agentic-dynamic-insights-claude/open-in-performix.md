---
title: Open the run in Arm Performix for deeper inspection

weight: 6

description: Validate an AI insight by inspecting flame graphs, functions, call paths, source, and disassembly from the same Arm Performix run.

layout: learningpathall
---
## Open the selected run

After generating insights using Claude Code, you can view the same run in Arm Performix.

A chat response helps you triage a performance problem, but the underlying profile is the source of evidence. Use the run ID from your insight request to retrieve the details of the profile. From a terminal with `apx` on your `PATH`, run:

```console
apx run info "<run-id>"
```

Replace `<run-id>` with the ID that you recorded. Use the returned workload, recipe, target information, and timestamps to identify the corresponding run in the GUI:

1. Open Arm Performix on the host that stores the run that was used by the Model Context Protocol (MCP) server.
2. Select **Runs** in the activity bar on the left, or select **Explore run data** on the home page.
3. Locate the Code Hotspots run using its timestamp, recipe, and workload labels.
4. Select the run to open its results.
5. Select **Run Details**. Compare the returned workload, execution times, target configuration, and recipe parameters with those of the selected run. Don't rely on the display name alone.

If you can't identify the matching run, perform the missing-run checks described in [Troubleshoot the MCP connection](/learning-paths/servers-and-cloud-computing/performix-agentic-dynamic-insights-claude/configure_mcp_claude/#code-hotspots-runs-are-missing) before evaluating the insight.

## Validate the insight in Arm Performix

Inspect the following views to verify the claim:

- **Flame graph**: Identify where sampled CPU time accumulates across call paths.
- **Functions**: Confirm which functions account for the largest sample percentages.
- **Call Stack**: Distinguish the cost of a function from the cost of its callees.
- **Source**: Correlate samples with source lines when source mapping is available.
- **Disassembly**: Inspect generated instructions and confirm claims about the compiled code.
- **Compare**: Evaluate equivalent before-and-after runs.

For a concrete check of the highest-impact hotspot finding, complete the following steps:

1. Record the function name, sample count or percentage, and call path cited by Claude Code. If the response omits these details, ask for them before continuing.
2. Locate the function in **Functions** and compare the reported metric with the profile. Use the same filters and distinguish samples that are attributed to the function from samples that include its callees.
3. Open **Call Stack** and check that the cited callers and callees match the profile.
4. If the recommendation refers to a source line or instruction, double-click the function to open the **Source Code Viewer**. Use **Source**, **Disassembly**, or **Split** to inspect the claim. If source mapping is missing, select **Specify Root Directory** and choose the matching source tree on your host.
5. Record whether the observation matches, conflicts with, or can't be established from the available data. Ask Claude Code to revise any finding whose function, metric, or call path doesn't match.

Matching a hotspot metric confirms the observation. However, it doesn't establish that the proposed optimization will improve performance. Validate performance improvement separately with a controlled before-and-after measurement.

Use the AI insight to focus your investigation instead of replacing it. For example, if the insight says a loop appears scalar, inspect its disassembly and compiler flags. Change the implementation after inspection. If Code Hotspots only shows that the loop is hot, run Instruction Mix or another appropriate recipe. Conclude that scalar execution is the cause only after running another recipe.

For a before-and-after comparison, keep the following details consistent:

- Workload
- Target
- Input
- Thread count
- CPU affinity
- Collection settings  
 
A lower sample percentage doesn't prove that a function became faster if total runtime or the surrounding workload changed.

## What you've accomplished

You've now checked a generated AI insight against the profile on Arm Performix.

You can continue with the [Arm Performix getting-started video](https://youtu.be/_eX8ZpNT0kc) to explore the graphical workflow.
