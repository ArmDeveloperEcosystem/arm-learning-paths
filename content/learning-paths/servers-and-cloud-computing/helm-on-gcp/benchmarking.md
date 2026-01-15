---
title: Benchmark Helm concurrency on a Google Axion C4A virtual machine
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Overview

This section explains how to benchmark Helm CLI concurrency on an Arm64-based GCP SUSE virtual machine.

Since Helm does not provide built-in performance metrics, concurrency behavior is measured by running multiple Helm commands in parallel and recording the total execution time.

### Prerequisites

{{% notice Note %}} Ensure the local Kubernetes cluster created earlier is running and has sufficient resources to deploy multiple NGINX replicas.{{% /notice %}}

Before starting the benchmark, ensure Helm is installed and the Kubernetes cluster is accessible.

```console
helm version
kubectl get nodes
```
All nodes should be in `Ready` state.

### Add a Helm repository
Helm installs applications using "charts." Configure Helm to download charts from the Bitnami repository and update the local chart index.

```console
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

### Create a benchmark namespace
Isolate benchmark workloads from other cluster resources.

```console
kubectl create namespace helm-bench
```

### Warm-up run (recommended)
Prepare the cluster by pulling container images and initializing caches.

```console
helm install warmup bitnami/nginx \
  -n helm-bench \
  --set service.type=ClusterIP \
  --timeout 10m
```
The first install is usually slower because images must be downloaded and Kubernetes needs to initialize internal objects. This warm-up run reduces image-pull and initialization overhead so the benchmark focuses more on Helm CLI concurrency and Kubernetes API behavior.

You should see output (near the top of the output) that is similar to:
```output
NAME: warmup
LAST DEPLOYED: Tue Dec  9 21:10:44 2025
NAMESPACE: helm-bench
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: nginx
CHART VERSION: 22.3.3
APP VERSION: 1.29.3
```

**After validation, remove the warm-up deployment:**

```console
helm uninstall warmup -n helm-bench
```

{{% notice Note %}}
Helm does not provide native concurrency or throughput metrics. Concurrency benchmarking is performed by executing multiple Helm CLI operations in parallel and measuring overall completion time.
{{% /notice %}}
### Concurrent Helm install benchmark (no wait)
Run multiple Helm installs in parallel using background jobs.

```console
time (
for i in {1..5}; do
  helm install nginx-$i bitnami/nginx \
    -n helm-bench \
    --set service.type=ClusterIP \
    --timeout 10m &
done
wait
)
```
This step simulates multiple teams deploying applications at the same time.
Helm submits all requests without waiting for pods to fully start.

What this measures:

* Helm concurrency handling
* Kubernetes API responsiveness
* Helm CLI client-side execution behavior on Arm64

You should see an output similar to:
```output
real    0m3.998s
user    0m12.798s
sys     0m0.339s
```

### Verify deployments

Confirm that Helm reports all components were installed successfully and that Kubernetes created and started the applications:

```console
helm list -n helm-bench
kubectl get pods -n helm-bench
```

Expected:

* All releases in `deployed` state
* Pods in `Running` status

### Concurrent Helm install benchmark (with --wait)
Run a benchmark that includes workload readiness time.

```console
time (
for i in {1..3}; do
  helm install nginx-wait-$i bitnami/nginx \
    -n helm-bench \
    --set service.type=ClusterIP \
    --wait \
    --timeout 15m &
done
wait
)
```

Measure Helm concurrency combined with scheduler and image-pull contention to understand end-to-end readiness impact.

The output is similar to:
```output
real    0m12.924s
user    0m7.333s
sys     0m0.312s
```

### Metrics to record

- Total elapsed time: overall time taken to complete all installs.
- Number of parallel installs: number of Helm installs run at the same time.
- Failures: any Helm failures or Kubernetes API errors.
- Pod readiness delay: time pods take to become Ready (resource pressure)

### Benchmark summary
Results from the earlier run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE):

| Test Case                    | Parallel Installs | `--wait` Used | Timeout | Total Time (real) |
| ---------------------------- | ----------------- | ------------- | ------- | ----------------- |
| Parallel Install (No Wait)   | 5                 | No            | 10m     | **3.99 s**        |
| Parallel Install (With Wait) | 3                 | Yes           | 15m     | **12.92 s**       |

Key observations:
- In this configuration, Helm CLI operations complete efficiently on an Arm64-based Axion C4A virtual machine, establishing a baseline for further testing.
- The --wait flag significantly increases total execution time because Helm waits for workloads to reach a Ready state, reflecting scheduler and image-pull delays rather than Helm CLI overhead.
- For this baseline test, parallel Helm installs complete with minimal contention, indicating that client-side execution and Kubernetes API handling are not bottlenecks at this scale.
- End-to-end workload readiness dominates total deployment time, showing that cluster resource availability and container image pulls have a greater impact than Helm CLI execution.

## What you've accomplished

You have successfully benchmarked Helm concurrency on a Google Axion C4A Arm64 virtual machine. The benchmarks demonstrated that:

- Helm CLI operations execute efficiently on Arm64 architecture with the Axion processor
- Parallel Helm installs complete in under 4 seconds when not waiting for pod readiness
- Using the `--wait` flag extends deployment time to reflect actual workload initialization
- Kubernetes API and client-side performance scale well under concurrent load
- Image pulling and resource scheduling have more impact on total deployment time than Helm CLI execution

These results establish a performance baseline for deploying containerized workloads with Helm on Arm64-based cloud infrastructure, helping you make informed decisions about deployment strategies and resource allocation.
