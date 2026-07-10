---
title: What is the arm-performix skill?
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## A skill, not a tool

**Arm Performix** is the profiling tool. The **arm-performix skill** is a set of
instructions you add to your AI assistant so that it knows *how* to use Performix
correctly on your behalf: which recipe to pick, how to gather context, how to
read the results, and how to report findings.

Without the skill, an assistant tends to guess at performance problems by reading
your source code. With the skill, it follows a disciplined workflow: measure
first, characterize the bottleneck, change one thing at a time, and prove the win
with before/after data.

## What the skill does for you

When the skill is active, the assistant will:

- Ask for the target, binary path, and workload command before profiling
- Choose the narrowest Performix recipe that answers your question
- Run the recipe (through the `apx` CLI or the Arm MCP Server)
- Return a structured **Analysis Report**: bottleneck summary, key metrics, hot
  functions, ranked recommendations, and a single next step

## What the skill will not do

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
| Why is the pipeline stalling? | **CPU Microarchitecture** | Frontend/backend stalls, bad speculation, retiring |
| Am I using SIMD (Neon/SVE)? | **Instruction Mix** | Scalar vs vector instruction balance |
| Is memory the bottleneck? | **Memory Access** | L1 hit rate, latency, TLB/page-walk pressure |
| What can the hardware do? | **System Characterization** | Memory bandwidth and latency baseline per NUMA node |

{{% notice Note %}}
**Where the recipes run:**

- **Profiling target** (the machine running your workload). The four
  microarchitecture-level recipes (CPU Microarchitecture, Instruction Mix,
  Memory Access, and System Characterization) require an **Arm Neoverse** target
  on Linux; Memory Access additionally needs the Statistical Profiling Extension
  (SPE) enabled. Code Hotspots is broader: it also runs on x86-64 Linux and on
  Windows 11 (Arm or x86).
- **Host** (the machine where you run the `apx` CLI or your AI assistant). It can
  be macOS, Windows, or Linux on either Arm64 or x86-64, and connects to the
  target locally or over SSH.
{{% /notice %}}
