---
title: Optimizing with the Arm MCP Server
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Optimizing with the Arm MCP Server

Use the Arm MCP Server after the manual baseline is complete. The agent should accelerate analysis and execution, but your benchmark artifacts remain the source of truth for what actually improved.

If you are new to this toolchain, start with the [Arm MCP Server learning path](https://learn.arm.com/learning-paths/servers-and-cloud-computing/arm-mcp-server/) for setup and core usage patterns.

## 1. Identify endpoints likely to benefit most

Ask the agent to analyze your application routes and classify optimization candidates by CPU intensity, serialization cost, synchronization, and cache behavior.

Prompt template:

```text
Analyze this .NET application for Arm optimization opportunities.
Identify endpoints most likely to benefit from Arm tuning.
Rank them by expected impact and explain why.
```

Expected output:

- Ranked endpoint list
- Bottleneck hypotheses per endpoint
- Instrumentation plan to validate hypotheses

## 2. Generate and run a targeted endpoint test suite

Ask the agent to extend the manual endpoint tester or build a repeatable suite that exercises the ranked endpoints and emits machine-readable output. Keep the same command-line controls used earlier: base URL, concurrency, iterations, and JSON output path.

Prompt template:

```text
Create a reproducible endpoint benchmark suite for these routes.
Use concurrency, iterations, and JSON output.
Include pass/fail checks for HTTP behavior and error rate.
```

The suite should produce:

- Per-endpoint latency percentiles
- Throughput summary
- Error counts
- Before/after comparison artifacts
- The exact route list and request method for each endpoint

## 3. Plan and implement Arm optimizations on Azure Cobalt

Ask the agent to create an execution plan, apply changes, run tests, and report deltas.

Prompt template:

```text
On this Ubuntu Neoverse (Azure Cobalt) instance:
1) establish baseline,
2) apply Arm-focused .NET runtime and deployment optimizations,
3) rerun tests,
4) report statistically meaningful deltas and risks.
```

Typical optimization actions include:

- Runtime settings (`DOTNET_TieredPGO`, `DOTNET_ReadyToRun`, thread pool tuning, and spin-wait experiments)
- Container/runtime configuration cleanup
- Architecture-conditional deployment settings
- Repeated measurement loops with fixed workload parameters and fixed endpoint order

## Practical guardrails

- Keep manual baseline artifacts as source of truth.
- Require raw output files for every claim.
- Ask the agent to separate observed facts from inferred explanations.
- Re-run on production-like traffic before release.
