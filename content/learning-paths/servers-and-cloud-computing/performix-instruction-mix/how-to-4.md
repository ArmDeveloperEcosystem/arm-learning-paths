---
title: (Optional) Optimize matmul with vector intrinsics
description: Optionally implement a custom Neon or SVE matrix multiplication kernel and profile it with Arm Performix or the Arm MCP Server.
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

### Use the Arm MCP Server with Performix 

You can also use an MCP-compatible coding assistant, such as GitHub Copilot or Codex, with the Arm MCP Server. This gives the assistant direct tool access to run Performix recipes on your remote Arm target and create a faster feedback loop while you iterate on `matmul_user`.

For setup details, see [Automate x86-to-Arm application migration using Arm MCP Server](/learning-paths/servers-and-cloud-computing/arm-mcp-server/).

Install Docker if needed, then pull the MCP server image:

```bash
docker pull armlimited/arm-mcp:latest
```

To allow Performix access to remote targets from inside the container, mount your workspace plus SSH key and known hosts in your Codex MCP configuration (example `~/.codex/config.toml`):

```output
[mcp_servers.arm-mcp]
command = "docker"
args = [
	"run",
	"--rm",
	"-i",
	"-v", "/path/to/your/workspace:/workspace",
	"-v", "/path/to/your/ssh/private_key:/run/keys/ssh-key.pem:ro",
	"-v", "/path/to/your/ssh/known_hosts:/run/keys/known_hosts:ro",
	"armlimited/arm-mcp"
]
```

Restart your coding assistant, then prompt it to run Performix Instruction Mix and Code Hotspots on your `gpt2_user` binary and suggest Arm intrinsics improvements.

![Screenshot of a coding assistant prompt configured to use Arm MCP Server tools for running Performix recipes and analyzing `matmul_user` optimization opportunities in the GPT-2 workload.#center](./mcp-performix-prompt.webp "Coding assistant prompt for Performix analysis through Arm MCP Server")

## What you've accomplished and what's next

You've now optionally implemented and profiled a custom `matmul_user` kernel using the same workflow you used for baseline analysis. 

Next, you'll compare Instruction Mix and throughput across scalar, Neon, SVE, and KleidiAI variants.
