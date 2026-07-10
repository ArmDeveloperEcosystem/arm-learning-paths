---
title: Generate AI insights

weight: 5

layout: learningpathall
---

## Generate AI insights for the latest run

If you want to start with the most recent supported run, use:

```
Generate AI insights for the last profiling run. Suggest where I should start investigating next. 
```

The assistant should call the Arm Performix MCP server, gather relevant run data, and return an evidence-based summary.

## Generate AI insights for a specific run

If you want to choose the run first, ask for the list of supported runs, then follow up with:

```
Generate AI insights for the run named "<run ID>".
```

Replace `<run ID>` with the run name or ID returned by the assistant.

If you are investigating a specific function, make the request more focused:

```
Use Arm Performix to explain why function <function-name> is hot in run <run ID>. Use profile evidence from the run.
```

Focused prompts usually produce more useful results than broad application-wide prompts.

## Use the Agentic workflow for iteration

Once you trust the diagnosis, you can ask follow-up questions:

```
Which evidence in the Performix run supports that recommendation?

What is the first optimization I should try, and why?

Suggest a minimal code change to test this hypothesis.
```

If your development environment also exposes build, deployment, remote execution, or source-control tools, the assistant may be able to help with a broader loop:

1. Modify the code.
2. Rebuild the workload.
3. Run it on the target.
4. Profile again with Arm Performix.
5. Compare the new run with the previous run.

The exact level of automation depends on the tools available in your VS Code environment and the Arm Performix MCP tools supported by your release.
