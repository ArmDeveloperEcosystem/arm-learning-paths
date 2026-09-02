---
title: (Optional) Optimize matmul with vector intrinsics
description: Optionally implement a custom Neon or SVE matrix multiplication kernel and profile it using the Arm Performix GUI or the Arm Performix MCP server.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Complete the challenge 

`src/kernels/matmul_user.cpp` is your editable implementation file. The baseline behavior in this file is scalar, and the build uses `-O2 -g`, so compiler optimization is enabled but vector hardware is still underused in the hot loop.

Use the profiling evidence from Performix to implement your own Neon or SVE intrinsics in `src/kernels/matmul_user.cpp`, then rebuild and profile `gpt2_user`.

{{% notice Note %}}

Focus on the accumulation loop in `matmul_user` (`acc += row[j] * x[j];`). Think about lane utilization, loop unrolling, and handling the tail when the input width is not an exact multiple of the vector width.

{{% /notice %}}

Rebuild after your edits:

```bash
cmake -S . -B build -DBUILD_USER_MATMUL=ON
cmake --build build --parallel
```

Then, profile the `build/gpt2_user` binary with the same runtime arguments and compare the Instruction Mix and throughput against baseline.

Example solutions are available in:

- `src/kernels/matmul_neon.cpp`
- `src/kernels/matmul_sve.cpp`

You can use `AGENTS.md` in the GPT-2 example repository for guided learning support.

### Use the Arm Performix MCP server

You can also use an MCP-compatible coding assistant, such as GitHub Copilot or Codex, with the Arm Performix MCP server. This gives the assistant access to Performix tools so it can run recipes on your configured remote Arm target and help you iterate on `matmul_user`.

For setup instructions, see [Configure the Arm Performix MCP server in Codex](/learning-paths/servers-and-cloud-computing/performix-agentic-dynamic-insights-codex/configure_mcp_codex/).

After you confirm that the MCP server is connected, use a focused prompt:

```text
Use the Arm Performix MCP server to list the available recipes and targets.

For the target named "<target-name>", run the Instruction Mix recipe with this workload:
"/home/ubuntu/GPT-2-Example/build/gpt2_user --model gpt2-medium \"Once upon a time\" -n 150"

Before starting, inspect the recipe parameters, target support, and MCP guidance. Repeat the target and workload, and ask me to confirm them. When the run completes, summarize the Instruction Mix results for `matmul_user` and suggest Neon or SVE improvements.
```

{{% notice Note %}}

The Arm Performix MCP server can run Instruction Mix, but Dynamic Insights are available only for successful Code Hotspots and System Utilization runs.

{{% /notice %}}

## What you've accomplished and what's next

You've now optionally implemented and profiled a custom `matmul_user` kernel using the same workflow you used for baseline analysis. 

Next, you'll compare Instruction Mix and throughput across scalar, Neon, SVE, and KleidiAI variants.
