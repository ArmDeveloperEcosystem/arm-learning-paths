---
title: Performance tuning on Cobalt
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Performance tuning on Cobalt

Treat tuning as an experiment pipeline, not a one-shot tweak. On Arm, apply changes in a controlled sequence, measure with fixed workloads, and keep only optimizations that repeatedly improve your target metrics.

## Tuned run configuration

Start with a conservative runtime profile that is commonly effective for server workloads. Keep these settings outside the application code at first so you can switch profiles without rebuilding.

```bash
export DOTNET_TieredCompilation=1
export DOTNET_TieredPGO=1
export DOTNET_ReadyToRun=1
export DOTNET_gcServer=1
export DOTNET_gcConcurrent=1
export DOTNET_EnableDiagnostics=0
export DOTNET_ThreadPool_ForceMinWorkerThreads=2
```

Increase `DOTNET_ThreadPool_ForceMinWorkerThreads` only when traces or load-test data show thread-pool starvation.

### Optional spin-wait experiment for .NET 8, 9, and 10

If the workload burns CPU while waiting for short-lived thread-pool work, test disabling the thread-pool unfair semaphore spin limit:

```bash
export DOTNET_ThreadPool_UnfairSemaphoreSpinLimit=0
```

Treat this as an experiment, not a default. Turning off spin waiting can reduce wasted CPU on small instances or oversubscribed containers, but it can also increase wake-up latency and reduce peak throughput. Validate it separately from the base tuned profile.

### Tiered PGO and ReadyToRun optimize different phases

`DOTNET_TieredPGO=1` and `DOTNET_ReadyToRun=1` are not the same optimization:

- `ReadyToRun` favors startup and early request latency by using precompiled code when it is available.
- `TieredPGO` favors steady-state throughput by letting the JIT recompile hot methods with runtime profile data.
- Test them together and separately if startup latency and warmed throughput both matter.

Run the same endpoint suite used in the baseline:

```bash
# Keep benchmark parameters identical to baseline for valid comparison.
python3 test_nopcommerce_endpoints.py \
  --base-url http://127.0.0.1:5000 \
  --concurrency 8 \
  --iterations 20 \
  --json-out arm_after.json
```

## Validation rules for credible tuning gains

Use these rules before adopting a tuning profile:

- Run at least 5 baseline and 5 tuned trials.
- Keep endpoint sequence fixed across all runs.
- Reset warm-up policy consistently (always warm or always cold).
- Require improvement in both throughput and p95 latency, not just one.
- Set a minimum practical threshold (for example, >=5% median gain) before rollout.

## Instance-size tradeoffs

Do not assume the same profile wins on every Azure Cobalt VM size. Smaller instances often benefit from lower CPU burn and predictable p95 latency. Larger instances often benefit from higher concurrency, but can expose GC, database, and shared-resource contention. Compare throughput, p95/p99 latency, CPU utilization, and error rate for each instance size before keeping a tuning profile.

## Interpretation

- If only one metric improves while p95 or error rate regresses, do not treat the change as a win.
- If run-to-run variation is near the observed delta, treat it as noise.
- Keep architecture-specific profiles separate; do not force one profile onto all architectures.


Use this page as a tuning workflow template, then validate with your production-like traffic profile before rollout.
