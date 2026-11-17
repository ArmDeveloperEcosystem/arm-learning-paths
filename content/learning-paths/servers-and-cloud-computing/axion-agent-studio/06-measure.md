---
title: Interpret CPU usage and isolation
description: Read workload CPU samples accurately and identify what the sandbox and validation boundaries do and do not establish.
weight: 7
layout: learningpathall
---

## Read workload CPU usage correctly

The dashboard presents manager, backend, frontend, and QA workload measurements. These are not four separate VM measurements. The three engineer workloads share one C4A VM, while the manager runs on N4A.

A core measurement is CPU time consumed over the sample interval. For example, 3.37 cores means the workload consumed CPU time at an average rate equivalent to 3.37 fully occupied vCPUs during that interval.

The engineer percentage uses the **combined Pod CPU limit**, 6.5 CPUs:

```text
CPU percentage = measured workload cores / 6.5 × 100
3.37 cores / 6.5 × 100 = approximately 51.8%
```

The denominator includes a 6-CPU model-server limit and a 0.5-CPU worker-service limit. It is not the 16-vCPU machine size and is not the 4.25-CPU scheduling request.

The inference server is configured with four threads. Four busy inference threads alone correspond to about 61.5% of the combined 6.5-CPU Pod limit. More quota does not automatically create more threads or make token generation scale linearly.

A lower frontend percentage does not imply that its model is remote or absent. Its constrained fragment task can finish sooner, while model loading, prompt processing, token generation, and waiting create different CPU patterns. Memory bandwidth, sampling windows, and contention also affect utilization. Inspect the stage and timestamps with the measurement.

| Quantity | Meaning in this demo |
| --- | --- |
| VM vCPUs | Virtual CPU capacity provisioned for the node; some is reserved for system workloads |
| Pod CPU request | CPU capacity Kubernetes uses when placing the Pod; this does not mean dedicated cores |
| Pod CPU limit | Sum of the configured CPU limits across this Pod's workload containers |
| Inference threads | llama.cpp's configured CPU worker parallelism |
| Sampled cores | Observed CPU consumption averaged over a time interval |
| CPU percentage | Sampled cores divided by the declared workload limit, multiplied by 100 |

For example, 3.9 sampled cores against a 6.5-CPU limit produces 60%. That is 60% of the agent's configured limit, not 60% of the shared 16-vCPU VM. A CPU limit is a ceiling, not a reservation: the three 6.5-CPU limits do not create 19.5 vCPUs on the 16-vCPU node.

Use the current metrics endpoint for an idle-versus-active comparison:

```bash
curl --fail --silent --show-error \
  http://127.0.0.1:8090/api/metrics/current | python3 -m json.tool
```

Run-specific history remains a record of that run after it finishes. Refreshing the browser does not rerun the models. Check the source and sample time; a missing or stale sample must not be presented as current utilization.

## Explain the isolation and test boundaries

Workers and validation run under gVisor, as non-root users, with dropped capabilities and a read-only container root filesystem. Writable temporary volumes are limited. Worker Sandboxes do not receive Kubernetes service-account tokens, and NetworkPolicies restrict their network access.

The manager handles generated source as data. The separate validator executes it with bounded subprocess and test controls. Protected acceptance checks are not supplied by the model, so a worker cannot pass simply by rewriting those expected results.

These measures reduce exposure to generated code. They do not establish a complete production security review, correctness for every possible input, or isolation between mutually hostile end users. The demo has one active workflow and no production user authentication layer.

## Record the run results

Save the actual node placement, image digests, model checksum, inference settings, policy, tests, and sample timestamps with your run. The saved October 21 run completed in 130.21 seconds with no repair round. That is one observation, not a latency guarantee or comparative benchmark.

This workflow demonstrates local model execution and application validation on Arm. It does not measure a C4A-versus-N4A speedup, x86 comparison, throughput under concurrent users, or cost savings. Those claims require a separate controlled experiment with comparable quality and completion criteria.

You have now traced a request through local CPU inference, independent checks, and an updated application. Remove the tutorial resources when you finish collecting evidence.
