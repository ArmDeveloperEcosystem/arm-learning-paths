---
title: Understand the arm-performix skill
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What the skill is

Arm Performix is a desktop application for hardware-specific performance
tuning. It offers curated analysis pathways for performance-critical factors in
applications, libraries, runtimes, and source code.

The `arm-performix` skill is a set of instructions you can add to your AI assistant so that it knows how to use Performix correctly on your behalf: which recipe to pick, how to gather context, how to read the results, and how to report findings.

Without the skill, an assistant tends to guess at performance problems by reading
your source code.

When the skill is active, the assistant:

- Asks for the target, binary path, and workload command before profiling
- Chooses the narrowest Performix recipe that answers your question
- Runs the recipe through the `apx` command-line interface (CLI), or through the
  Arm Model Context Protocol (MCP) Server
- Returns a structured Analysis Report with a bottleneck summary, key metrics,
  hot functions, ranked recommendations, and a single next step

## What recipes the skill can run

Performix exposes five profiling recipes, and the skill orchestrates them as a
workflow: it picks a starting recipe from your question, then follows the
evidence into whichever further recipes are needed to explain and confirm the
bottleneck. Each recipe provides a different view of application performance:

| Recipe | What it shows |
| --- | --- |
| Code Hotspots | Hottest functions, call paths, and flame graphs to identify where time is spent |
| CPU Microarchitecture | Front-end and back-end pipeline stalls, bad speculation, retiring |
| Instruction Mix | Scalar versus vector instruction balance |
| Memory Access | L1 cache hit rate, latency, translation lookaside buffer (TLB) and page-walk pressure to identify whether memory is the bottleneck |
| System Characterization | Memory bandwidth and latency baseline per non-uniform memory access (NUMA) node to identify what the hardware can do |

{{% notice Note %}}
- The four microarchitecture-level recipes — CPU Microarchitecture, Instruction Mix,
  Memory Access, and System Characterization — require an Arm Neoverse target
  on Linux. The Code Hotspots recipe additionally runs on x86-64 Linux and on
  Windows 11 on Arm or x86-64.
- To use the Memory Access recipe, enable the Statistical Profiling Extension
  (SPE).
- The host machine can be macOS, Windows, or Linux on either arm64 or x86-64. The host can connect to the target locally or over SSH.
- The Arm MCP Server is useful for agent-driven launch-mode profiling, but it doesn't expose the System Characterization recipe. To access the System Characterization recipe, use the `apx` CLI or the GUI. 
{{% /notice %}}

## What you've learned and what's next

You've now learned how the `arm-performix` skill can help an assistant use Performix correctly, and what Performix recipes the skill can run.

Next, you'll install the skill. 