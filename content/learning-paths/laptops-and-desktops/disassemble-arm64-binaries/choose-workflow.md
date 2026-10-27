---
title: Choose static inspection or Arm Performix
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose the workflow that answers your question

Static disassembly and runtime performance analysis answer different questions. Choose the workflow that matches the claim you need to make:

| Question | Recommended workflow |
| --- | --- |
| What extension-specific code is present in this artifact, where is it, and what exact bytes support the claim? | This static-disassembly Learning Path |
| What executed on an Arm Linux target, where was time spent, and which CPU or memory behavior should be optimized? | Arm Performix |

[Arm Performix](/install-guides/performix/) is a performance-analysis environment. Its host application can run on macOS, Windows, or Linux and connects to a supported Arm Linux profiling target. Use the existing Learning Paths to answer specific runtime questions:

- [Find Code Hotspots with Arm Performix](/learning-paths/servers-and-cloud-computing/cpu_hotspot_performix/) identifies functions that consume CPU cycles.
- [Optimize application performance using Arm Performix CPU microarchitecture analysis](/learning-paths/servers-and-cloud-computing/performix-microarchitecture/) covers the CPU Microarchitecture and Instruction Mix recipes.
- [Optimize memory access behavior using Arm Performix and the Arm MCP Server](/learning-paths/servers-and-cloud-computing/performix-memory-access/) investigates cache and address-translation behavior.
- [Characterize system performance with Arm Performix](/learning-paths/servers-and-cloud-computing/performix-system-characterization/) measures system configuration, memory latency, and memory bandwidth.

Arm Performix Instruction Mix can report categories of instructions observed during profiling. That runtime view complements static inspection, but it doesn't replace the exact static-PC, symbol, operand, and byte-level artifact evidence you collected here.

You will often use both workflows. Start with static inspection to confirm that the required extension-specific code shipped. Then use Arm Performix on the supported Arm Linux target to learn whether the application executed that code path and where to focus performance work.

## What you've learned and what's next

You can now choose an evidence method without mixing static presence, runtime execution, and performance claims. The next page lists the Learning Path resources you can use to continue.
