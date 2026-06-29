---
title: Benchmark Gerrit on your Google Cloud Axion C4A virtual machine
description: Run a benchmark script on your Google Cloud C4A Arm virtual machine to measure Gerrit throughput, latency, and resource usage.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download and install the benchmarking script

You'll use a script to benchmark Gerrit performance on your Axion virtual machine (VM). The script exercises and times key Gerrit features and functions. 

Clone the following repository into your VM:

```bash
cd $HOME
git clone https://github.com/DougAnsonAustinTx/gerrit_test
```

## Run the benchmark script

Run the benchmark:

```bash
cd $HOME/gerrit_test
chmod 755 *.sh
sudo SYNTH_PROFILE=production_like REQUIRE_GERRIT_METRICS=true ./gerrit_perf_test.sh
```

The benchmark script runs through sample exercises that Gerrit supports and captures performance data from those exercises.

The script then places the data into a specified JSON file similar to (partially omitted for brevity):

```json
{
  "run": {
    "run_id": "20260622T152549Z",
    "timestamp_utc": "2026-06-22T15:35:19Z",
    "host": "douans01-gerrit-arm-6.c.arm-deveco-stedvsl-prd.internal",
    "os": "Debian GNU/Linux 13 (trixie)"
  },
  "software": {
    "java_version": "openjdk version \"21.0.11\" 2026-04-21 OpenJDK Runtime Environment (build 21.0.11+10-1-deb13u2-Debian) OpenJDK 64-Bit Server VM (build 21.0.11+10-1-deb13u2-Debian, mixed mode, sharing) ",
    "gerrit_version": "gerrit version 3.11.2",
    "gerrit_base_url": "http://127.0.0.1:8080",
    "gerrit_test_http_user": "admin",
    "prometheus_url": "http://127.0.0.1:9090",
    "gerrit_metrics_url": "http://127.0.0.1:8080/plugins/metrics-reporter-prometheus/metrics",
    "gerrit_metrics_probe_status": "ok",
    "gerrit_metrics_auth_mode": "bearer"
  },
  "workload": {
    "test_duration_seconds_per_step": 120,
    "concurrency_steps": "2,1,1 4,2,1 6,3,2 8,4,2",
    "legacy_single_step_defaults": {
      "rest_concurrency": 6,
      "git_clone_concurrency": 3,
      "git_push_concurrency": 2
    },
    "synthetic_profile": "production_like",
    "synthetic_projects": 8,
    "synthetic_initial_files_per_project": 300,
    "synthetic_initial_commits_per_project": 50,
    "synthetic_review_changes_per_project": 40,
    "synthetic_large_files_per_project": 8,
    "synthetic_large_file_kb": 1024
  },
  "startup_state": {
    "initial_gerrit_was_running": "true"
  },
  "operation_summary": [
    {
      "type": "git_clone",
      "count": 4301,
      "ok_count": 4301,
      "fail_count": 0,
      "min_ms": 105,
      "avg_ms": 244.42269239711695,
      "p50_ms": 220,
      "p90_ms": 418,
      "p95_ms": 456,
      "p99_ms": 521,
      "max_ms": 611
    },
    {
      "type": "git_push_refs_for",
      "count": 570,
      "ok_count": 570,
      "fail_count": 0,
      "min_ms": 75,
      "avg_ms": 157.13333333333333,
      "p50_ms": 155,
      "p90_ms": 222,
      "p95_ms": 239,
      "p99_ms": 288,
      "max_ms": 344
    },
    {
      "type": "rest_change_query",
      "count": 42992,
      "ok_count": 42992,
      "fail_count": 0,
      "min_ms": 12,
      "avg_ms": 31.553265723855603,
      "p50_ms": 30,
      "p90_ms": 50,
      "p95_ms": 56,
      "p99_ms": 69,
      "max_ms": 105
    }
  ]
  // rest of file omitted for brevity...
}
```

You can process this JSON file to create a summary of the performance of Gerrit on the Axion C4A VM. 

## Performance summary

The benchmark run completed successfully on the production-like profile with Gerrit metrics enabled. It recorded 47,863 measured client operations over four 120-second steps, with 47,863 successes and zero failures.

The benchmark gives a high-quality performance view: client latency, stepwise concurrency behavior, node CPU/memory/disk. Gerrit-side JVM, GC, Jetty, cache, queue, Git, REST, NoteDB, and receive-commits metrics are all present:

![Charts and graphs showing the Gerrit benchmark performance summary including operation counts, success rates, and latency metrics across the four 120-second test steps.#center](images/analysis.png "Gerrit benchmark summary")

All 47,863 measured client-side operations succeeded. REST query latency remains low with a p99 of 69 ms. Clone is the dominant pressure point at a p99 of 521 ms, and push remains sub-second at a p99 of 288 ms:

![Performance metrics showing client-side operation summary with statistics for git_clone, git_push_refs_for, and rest_change_query operations, including latency percentiles and success rates.#center](images/client-summary.png "Client-side operation summary")

The useful capacity signal is the flattening throughput curve after step 2. CPU is already near saturation in step 2, then stays around 99% in steps 3 and 4. Latency continues rising: clone p99 increases from 221 ms in step 2 to 550 ms in step 4, while aggregate throughput only rises from 103.3 to 108.4 ops/sec:

![Graph showing throughput and latency trends across four concurrency steps, demonstrating how performance degrades as concurrency increases and CPU approaches saturation.#center](images/stepwise-summary.png "Stepwise concurrency behavior summary")

The following chart shows host CPU pressure:

![Chart displaying CPU usage metrics across the benchmark steps, showing how CPU pressure increases and stabilizes near saturation levels as concurrency increases.#center](images/cpu-pressure.png "CPU pressure summary")

The following table lists Gerrit server-side correlation observations:

![Table showing correlations between various Gerrit server-side metrics such as GC pressure, cache performance, and queue depths in relation to client request latency.#center](images/gerrit-correlation.png "Gerrit server-side correlation findings")

The following table lists server metrics:

![Server metrics dashboard showing host resource utilization metrics including memory, disk I/O, and other system-level performance indicators during the benchmark run.#center](images/server-metrics.png "Basic additional server metrics")

## What you've accomplished

You've successfully deployed Gerrit on a Google Cloud C4A Axion Arm64 VM running Ubuntu 24.04 LTS, verified the web console, and measured its performance using a production-like benchmark profile. All operations completed with zero failures, and the results establish a practical capacity baseline for a single-node Gerrit deployment on Arm-based infrastructure.

To build on this foundation, you can explore multi-node Gerrit deployments, tune JVM flags for the Neoverse-V2 core, or compare performance across different C4A instance sizes to find the right balance of cost and throughput for your workload.
