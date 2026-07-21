---
title: What is the arm-performix skill?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## A skill, not a tool

**Arm Performix** is a desktop application for hardware-specific performance
tuning. It offers curated analysis pathways for performance-critical factors in
applications, libraries, runtimes, and source code. The **arm-performix skill** is
a set of instructions you add to your AI assistant so that it knows how to use
Performix correctly on your behalf: which recipe to pick, how to gather context,
how to read the results, and how to report findings.

Without the skill, an assistant tends to guess at performance problems by reading
your source code. With the skill, it follows a disciplined workflow: measure
first, characterize the bottleneck, change one thing at a time, and confirm the
improvement with before/after data.

## What the skill does for you

When the skill is active, the assistant:

- Asks for the target, binary path, and workload command before profiling
- Chooses the narrowest Performix recipe that answers your question
- Runs the recipe through the `apx` command-line interface (CLI), or through the
  Arm Model Context Protocol (MCP) Server
- Returns a structured Analysis Report with a bottleneck summary, key metrics,
  hot functions, ranked recommendations, and a single next step

## What the skill does not do

- Profile non-Neoverse Arm cores, such as phone-class SoCs
- Guess at bottlenecks from source reading instead of measurement
- Silently switch to another profiler when Performix is unavailable; it asks you
  how to proceed instead

## The recipes it can run

Performix exposes five profiling recipes, and the skill orchestrates them as a
workflow: it picks a starting recipe from your question, then follows the
evidence into whichever further recipes are needed to explain and confirm the
bottleneck. Each recipe answers a different question:

| Your question | Recipe | What it shows |
| --- | --- | --- |
| Where is my time spent? | **Code Hotspots** | Hottest functions, call paths, flame graph |
| Why is the pipeline stalling? | **CPU Microarchitecture** | Front-end and back-end stalls, bad speculation, retiring |
| Am I using single instruction, multiple data (SIMD), such as Neon or Scalable Vector Extension (SVE)? | **Instruction Mix** | Scalar vs vector instruction balance |
| Is memory the bottleneck? | **Memory Access** | L1 cache hit rate, latency, translation lookaside buffer (TLB) and page-walk pressure |
| What can the hardware do? | **System Characterization** | Memory bandwidth and latency baseline per non-uniform memory access (NUMA) node |

{{% notice Note %}}
**Where the recipes run:**

- **Profiling target** (the machine running your workload). The four
  microarchitecture-level recipes (CPU Microarchitecture, Instruction Mix,
  Memory Access, and System Characterization) require an **Arm Neoverse** target
  on Linux; Memory Access additionally needs the Statistical Profiling Extension
  (SPE) enabled. Code Hotspots is broader: it also runs on x86-64 Linux and on
  Windows 11 on Arm or x86-64.
- **Host** (the machine where you run the `apx` CLI or your AI assistant). It can
  be macOS, Windows, or Linux on either arm64 or x86-64, and connects to the
  target locally or over Secure Shell (SSH).
{{% /notice %}}

{{% notice Note %}}

The `apx` CLI is the full-capability interface. Use it for attach-to-process ID
(PID), system-wide captures, timed captures, run export/import, custom result
queries, CI/CD automation, and the System Characterization recipe. The Arm MCP
Server is useful for agent-driven launch-mode profiling, but it exposes only the
`code_hotspots`, `instruction_mix`, `cpu_microarchitecture`, and `memory_access`
recipes. If you need System Characterization or run-history operations, use the
CLI or the graphical user interface (GUI).
{{% /notice %}}
