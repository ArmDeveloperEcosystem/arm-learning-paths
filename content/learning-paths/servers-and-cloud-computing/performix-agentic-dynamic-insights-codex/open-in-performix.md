---
title: Open the run in Arm Performix for deeper inspection

weight: 6

description: Validate an AI Insight by inspecting flame graphs, functions, call paths, source, and disassembly from the same Arm Performix run.

layout: learningpathall
---
## Validate the insight in Arm Performix

A chat response helps you triage a performance problem, but the underlying profile is the source of evidence. Open the same run ID in Arm Performix and inspect the views relevant to the claim:

- **Flame graph** to see where sampled CPU time accumulates across call paths.
- **Functions** to confirm which functions account for the largest sample percentages.
- **Call Stack** to distinguish a function's own cost from the cost of its callees.
- **Source** to correlate samples with source lines when source mapping is available.
- **Disassembly** to inspect generated instructions and confirm claims about the compiled code.
- **Compare** to evaluate equivalent before-and-after runs.

Use the AI Insight to focus your investigation, not replace it. For example, if the insight says a loop appears scalar, inspect its disassembly and compiler flags before changing the implementation. If Code Hotspots only shows that the loop is hot, run Instruction Mix or another appropriate recipe before concluding that scalar execution is the cause.

For a before-and-after comparison, keep the workload, target, input, thread count, CPU affinity, and collection settings consistent. A lower sample percentage doesn't prove that a function became faster if total runtime or the surrounding workload changed.

You have configured the Performix MCP server, selected or created a Code Hotspots run, generated an AI Insight, and checked its recommendation against the profile. Continue with the [Arm Performix getting-started video](https://youtu.be/_eX8ZpNT0kc) to explore the graphical workflow.
