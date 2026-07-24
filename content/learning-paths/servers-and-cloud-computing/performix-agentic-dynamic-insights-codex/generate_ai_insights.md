---
title: Generate Arm Performix AI insights for a Code Hotspots run

weight: 5

description: Ask Codex for an Arm Performix AI Insight tied to a specific run and assess whether the response is supported by profile evidence.

layout: learningpathall
---
## Select the exact run

Use a run ID whenever possible. It prevents Codex from selecting a similarly named run or a more recent run from a different workload.

If you don't have the ID, ask Codex to list supported runs:

```text
Use Arm Performix to list supported Code Hotspots runs. Include the run ID, target, workload, and creation time for each run.
```

## Generate AI insights for a specific run

Request an insight for the selected run:

```text
Use Arm Performix to generate an AI Insight for run ID "<run-id>". Identify the highest-impact finding, cite the profile evidence that supports it, and suggest the first investigation or optimization step. State any missing evidence or uncertainty.
```

Replace `<run-id>` with the ID returned by Arm Performix.

If you are investigating a specific function, make the request more focused:

```text
Use Arm Performix to explain why function "<function-name>" is hot in run ID "<run-id>".
```

Focused prompts usually produce more useful results than broad application-wide prompts.

## Evaluate the response

A useful response identifies the run it analyzed and connects its conclusion to measured evidence, such as sample percentages, call paths, source attribution, or disassembly. It should also state when the available data can't establish a root cause.

Ask follow-up questions when a recommendation isn't traceable:

```text
Which measured evidence in this Performix run supports that recommendation?

What alternative explanations fit the same evidence?

Which additional Performix recipe or view would distinguish between those explanations?

What is the first optimization I should try, and why?
```

## Improve a generic AI Insight

Ask for one finding and its evidence:

```text
Focus on the highest-impact finding in run ID "<run-id>". Cite the measured evidence, distinguish hypotheses from observations, and identify the next Performix view or recipe to inspect.
```

For a known hotspot:

```text
For function "<function-name>" in run ID "<run-id>", summarize what Code Hotspots proves, what it doesn't prove, and which additional evidence is needed to identify the root cause.
```

If the response remains generic, confirm that the run has enough samples, symbols, source mapping, and disassembly. Code Hotspots locates sampled CPU time; use a more specific Performix recipe when you need evidence about microarchitecture, instruction mix, or memory access.

## Iterate and measure

After you review the evidence, use a controlled optimization loop:

1. Record the baseline workload, target, run configuration, and elapsed time.
2. Change one performance-relevant variable.
3. Rebuild the workload.
4. Rerun the same workload on the same target.
5. Profile it again with the same Performix settings.
6. Compare elapsed time and profile evidence with the baseline.

Codex can help with more of this loop if your environment exposes build, deployment, remote-execution, or source-control tools. Review proposed code changes and command approvals before Codex applies or runs them.

## What you've accomplished and what's next

You've now generated an evidence-based hypothesis.

Next, you'll open the same run in Arm Performix to inspect the underlying profile views.
