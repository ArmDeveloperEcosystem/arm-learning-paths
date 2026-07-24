---
title: Tune the performance of the .NET application on Azure
description: Apply .NET runtime tuning on an Azure Cobalt-based virtual machine and compare endpoint benchmark results to decide whether a profile improves nopCommerce performance.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Apply performance tuning changes

Treat tuning as an experiment pipeline, not a one-shot tweak. On Arm, apply changes in a controlled sequence, measure with fixed workloads, and keep only optimizations that repeatedly improve your target metrics.

### Configure a tuned run

Start with a conservative runtime profile that's commonly effective for server workloads. Keep these settings outside the application code at first so you can switch profiles without rebuilding.

Runtime environment variables are read when the .NET process starts. Stop the baseline `dotnet run` process, set the variables in the same terminal, and then restart nopCommerce. 

The following thread-pool minimum matches the 2-vCPU validation VM. Treat it as a starting point, not a universal value for every VM size:

```bash
export DOTNET_TieredCompilation=1
export DOTNET_TieredPGO=1
export DOTNET_ReadyToRun=1
export DOTNET_gcServer=1
export DOTNET_gcConcurrent=1
export DOTNET_EnableDiagnostics=0
export DOTNET_ThreadPool_ForceMinWorkerThreads=2
```

Restart the application from the same shell so it inherits the tuning profile:

```bash
cd ~/nopCommerce/src/Presentation/Nop.Web  # replace with your clone path if different
dotnet run -c Release --no-build --urls http://0.0.0.0:5000
```

Increase `DOTNET_ThreadPool_ForceMinWorkerThreads` only when traces or load-test data show thread-pool starvation. Keep `DOTNET_EnableDiagnostics=0` for final measurement runs only. Remove it when you need `dotnet-trace`, `dotnet-counters`, or profiler-based evidence.

#### (Optional) Run spin-wait experiment for .NET 8, 9, and 10

If the workload burns CPU while waiting for short-lived thread-pool work, test disabling the thread-pool unfair semaphore spin limit:

```bash
export DOTNET_ThreadPool_UnfairSemaphoreSpinLimit=0
```

Treat this as an experiment, not a default. Turning off spin waiting can reduce wasted CPU on small instances or oversubscribed containers, but it can also increase wake-up latency and reduce peak throughput. Validate it separately from the base tuned profile by changing only this variable between trials.

### Optimize tiered PGO and ReadyToRun 

`DOTNET_TieredPGO=1` and `DOTNET_ReadyToRun=1` aren't the same optimization:

- `ReadyToRun` favors startup and early request latency by using precompiled code when it's available.
- `TieredPGO` favors steady-state throughput by letting the JIT recompile hot methods with runtime profile data.
- Test them together and separately if startup latency and warmed throughput both matter.

Run the same endpoint suite used in the baseline from a second terminal. Keep the app running with the tuning profile in the first terminal, and run the tester from the repository root so the before and after JSON files sit next to each other:

```bash
cd ~/nopCommerce  # replace with your clone path if different

# Keep benchmark parameters identical to baseline for valid comparison.
python3 test_nopcommerce_endpoints.py \
  --base-url http://127.0.0.1:5000 \
  --concurrency 8 \
  --iterations 20 \
  --json-out arm_after.json
```

Inspect the summaries before comparing results:

```bash
jq '.summary' arm_before.json
jq '.summary' arm_after.json
```

### Validation rules for credible tuning gains

Use these rules before adopting a tuning profile:

- Run at least five baseline and five tuned trials.
- Keep endpoint sequence fixed across all runs.
- Reset warm-up policy consistently (always warm or always cold).
- Require improvement in both throughput and p95 latency, not just one.
- Set a minimum practical threshold (for example, >=5% median gain) before rollout.
- Don't assume the same profile wins on every Azure VM size. Smaller instances often benefit from lower CPU burn and predictable p95 latency. Larger instances often benefit from higher concurrency, but can expose GC, database, and shared-resource contention. Compare throughput, p95/p99 latency, CPU utilization, and error rate for each instance size before keeping a tuning profile.

### Considerations for interpreting metric improvements

When interpreting metric improvements, consider the following:

- If only one metric improves while p95 or error rate regresses, don't treat the change as a win.
- If run-to-run variation is near the observed delta, treat it as noise.
- Keep architecture-specific profiles separate. Don't force one profile onto all architectures.

## What you've accomplished and what's next

You've applied performance tuning changes to the .NET application. 

Next, you'll use the Arm MCP Server to optimize application performance.
