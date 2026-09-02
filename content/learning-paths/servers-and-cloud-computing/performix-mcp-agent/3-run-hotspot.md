---
title: Run Code Hotspots with an AI agent
description: Use an AI agent and the dedicated Arm Performix MCP server to run Code Hotspots and review evidence tied to a specific run ID.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Execute profiling through the Arm Performix MCP server

You'll keep collection and analysis as separate requests. This lets you confirm the target and workload before remote execution and use the resulting run ID for analysis.

{{% notice Note %}}
The prompts use natural language instead of internal MCP tool names. This makes them suitable for compatible AI coding assistants that are connected to the dedicated Arm Performix MCP server. For a tested setup, see [Configure the Arm Performix MCP server in Codex](/learning-paths/servers-and-cloud-computing/performix-agentic-dynamic-insights-codex/configure_mcp_codex/).
{{% /notice %}}

## Select the configured target

Ask your AI assistant to list the Performix targets:

```text
Use the Arm Performix MCP server to list the configured targets. Include each target's name and connection status when available.
```

Choose the friendly target name that you verified in the previous section. You don't need to provide its SSH username or IP address again because those details belong to the Performix target configuration.

## Run the Code Hotspots recipe

Replace `<target-name>` in this prompt, then send it to your AI assistant:

```text
Use Arm Performix to run the Code Hotspots recipe on target "<target-name>"
with workload
"/home/ec2-user/Mandelbrot-Example/build/mandelbrot_single_thread_debug".
Before starting, repeat the target and workload and ask me to confirm them.
When the run completes, return its run ID and collection status.
```

Review the target and workload before approving collection. The dedicated server runs the recipe, waits for it to finish, and returns a stable run ID with the collection status.

{{% notice Note %}}
The single-threaded workload can take one to two minutes on the example system. Runtime and sample counts vary with the target, workload build, and Performix version.
{{% /notice %}}

## Generate an AI insight

Use the returned run ID to request evidence for that exact profile:

```text
Use Arm Performix to generate an AI insight for run ID "<run-id>".
Identify the highest-impact finding, cite the profile evidence that supports it,
and suggest the first investigation or optimization step. State any missing
evidence or uncertainty.
```

Replace `<run-id>` with the ID from the completed Code Hotspots run.

A useful response identifies the analyzed run and connects each finding to measured evidence. For this unoptimized debug build, the profile can expose:

- `Mandelbrot::getIterations` in the per-pixel iteration loop
- `std::__complex_abs` and `hypotf64` in the square-root-based escape check
- `std::complex<double>` operator overhead that remains visible without compiler inlining

Exact percentages vary, so use the values returned for your run rather than treating example values as fixed results.

The following flame graph comes from the same single-threaded Mandelbrot workload in the manual Performix workflow. It shows `std::__complex_abs` as the dominant sampled function and provides a visual check for the evidence returned by the agent.

![Arm Performix flame graph for the single-threaded Mandelbrot workload showing std::__complex_abs as the dominant hotspot, which confirms the square-root-based escape check is a candidate for investigation#center](../cpu_hotspot_performix/single-thread-flame-graph.jpg "Single-threaded Mandelbrot flame graph in Arm Performix")

You can open the run in the Performix GUI when you want to inspect the flame graph, call paths, and source attribution directly.

## What you've accomplished and what's next

You've used the dedicated Arm Performix MCP server to select a configured target, run Code Hotspots, and generate an AI insight for a specific run ID.

Next, you'll apply one optimization at a time, rebuild the workload, and create a new profile to measure the effect.
