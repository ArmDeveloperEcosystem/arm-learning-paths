---
title: Benchmark Helm concurrency on a Google Axion C4A virtual machine
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Run concurrent Helm benchmarks

In this section, you'll benchmark Helm CLI concurrency on your Arm64-based GCP SUSE VM. Since Helm doesn't provide built-in performance metrics, you'll measure concurrency behavior by running multiple Helm commands in parallel and recording total execution time.

### Prerequisites

{{% notice Note %}}
Ensure the local Kubernetes cluster is running and has sufficient resources to deploy multiple NGINX replicas.
{{% /notice %}}

Verify Helm and Kubernetes access:

```console
helm version
kubectl get nodes
```
All nodes should be in `Ready` state.

### Add a Helm repository

Configure Helm to download charts from the Bitnami repository:

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

Prepare the cluster by pulling container images:

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

Run multiple Helm installs in parallel:

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

This measures Helm concurrency handling, Kubernetes API responsiveness, and client-side execution on Arm64.

You should see an output similar to:
```output
real    0m3.998s
user    0m12.798s
sys     0m0.339s
```

### Verify deployments

Confirm that all components were installed successfully:

```console
helm list -n helm-bench
kubectl get pods -n helm-bench
```

All releases should be in `deployed` state and pods should be in `Running` status.

### Concurrent Helm install benchmark (with --wait)

Run a benchmark that includes workload readiness time:

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

Record the following:

- Total elapsed time (overall time taken to complete all installs)
- Number of parallel installs
- Any failures or Kubernetes API errors
- Pod readiness delay (time pods take to become Ready under resource pressure)

### Benchmark summary
Results from the earlier run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE):

| Test Case                    | Parallel Installs | `--wait` Used | Timeout | Total Time (real) |
| ---------------------------- | ----------------- | ------------- | ------- | ----------------- |
| Parallel Install (No Wait)   | 5                 | No            | 10m     | **3.99 s**        |
| Parallel Install (With Wait) | 3                 | Yes           | 15m     | **12.92 s**       |

Key observations:

- Helm CLI operations complete efficiently on an Arm64-based Axion C4A VM, establishing a baseline for further testing
- The `--wait` flag significantly increases total execution time because Helm waits for workloads to reach Ready state, reflecting scheduler and image-pull delays rather than Helm CLI overhead
- Parallel Helm installs complete with minimal contention, indicating that client-side execution and Kubernetes API handling aren't bottlenecks at this scale
- End-to-end workload readiness dominates total deployment time, showing that cluster resource availability and container image pulls have greater impact than Helm CLI execution

## What you've accomplished

You have successfully benchmarked Helm concurrency on a Google Axion C4A Arm64 VM:

- Helm CLI operations execute efficiently on Arm64 architecture with Axion processors
- Parallel Helm installs complete in under 4 seconds when not waiting for pod readiness
- Using the `--wait` flag extends deployment time to reflect actual workload initialization
- Kubernetes API and client-side performance scale well under concurrent load
- Image pulling and resource scheduling have more impact on total deployment time than Helm CLI execution

These results establish a performance baseline for deploying containerized workloads with Helm on Arm64-based cloud infrastructure.
