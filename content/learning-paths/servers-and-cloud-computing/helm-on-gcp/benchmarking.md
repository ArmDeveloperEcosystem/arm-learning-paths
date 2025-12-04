---
title: Helm Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


##  Helm Benchmark on GCP SUSE Arm64 VM
This guide explains **how to benchmark Helm on an Arm64-based GCP SUSE VM** using only the **Helm CLI**.  
Since Helm does not provide built-in performance metrics, we measure **concurrency behavior** by running multiple Helm commands in parallel and recording the total execution time.

### Prerequisites
Before starting the benchmark, ensure Helm is installed and the Kubernetes cluster is accessible.

```console
helm version
kubectl get nodes
```

All nodes should be in `Ready` state.


### Add Helm Repository
Helm installs applications using “charts.”
This step tells Helm where to download those charts from and updates its local chart list.

```console
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
```

### Create Benchmark Namespace
Isolate benchmark workloads from other cluster resources.

```console
kubectl create namespace helm-bench
```

### Warm-Up Run (Recommended)
This step prepares the cluster by pulling container images and initializing caches.

```console
helm install warmup bitnami/nginx \
  -n helm-bench \
  --set service.type=ClusterIP \
  --timeout 10m
```
The first install is usually slower because of following reasons:

- Images must be downloaded.
- Kubernetes initializes internal objects.

This warm-up ensures the real benchmark measures Helm performance, not setup overhead.

**After validation, remove the warm-up deployment:**

```console
helm uninstall warmup -n helm-bench
```

{{% notice Note %}}
Helm does not provide native concurrency or throughput metrics. Concurrency benchmarking is performed by executing multiple Helm CLI operations in parallel and measuring overall completion time.
{{% /notice %}}

### Concurrent Helm Install Benchmark (No Wait)
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
* Arm64 client-side performance

You should see an output similar to:
```output
real 0m4.109s
user 0m12.178s
sys 0m0.470s
```

### Verify Deployments

This confirms:

- Helm reports that all components were installed successfully
- Kubernetes actually created and started the applications

```console
helm list -n helm-bench
kubectl get pods -n helm-bench
```

Expected:

* All releases in `deployed` state
* Pods in `Running` status

### Concurrent Helm Install Benchmark (With `--wait`)
This benchmark includes workload readiness time.

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

What this measures:

* Helm concurrency plus scheduler and image-pull contention
* End-to-end readiness impact

You should see an output similar to:
```output
WARNING: There are "resources" sections in the chart not set. Using "resourcesPreset" is not recommended for production. 
For production installations, please set the following values according to your workload needs: - cloneStaticSiteFromGit.gitSync.resources - resources +info https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/ 
real 0m12.758s
user 0m7.360s
sys 0m0.227s
```

### Metrics to Record

- **Total elapsed time**: Overall time taken to complete all installs.
- **Number of parallel installs**: Number of Helm installs run at the same time.
- **Failures**: Any Helm failures or Kubernetes API errors.
- **Pod readiness delay**: Time pods take to become Ready (resource pressure)

### Benchmark summary on x86_64
To compare the benchmark results, the following results were collected by running the same benchmark on an `x86 - c4-standard-4` (4 vCPUs, 15 GB Memory) x86_64 VM in GCP, running SUSE:

| Test Case                    | Parallel Installs | `--wait` Used | Timeout | Total Time (real) |
| ---------------------------- | ----------------- | ------------- | ------- | ----------------- |
| Parallel Install (No Wait)   | 5                 | No          | 10m     | **6.06 s**        |
| Parallel Install (With Wait) | 3                 | Yes         | 15m     | **14.41 s**       |


### Benchmark summary on Arm64
Results from the earlier run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE):

| Test Case                    | Parallel Installs | `--wait` Used | Timeout | Total Time (real) |
| ---------------------------- | ----------------- | ------------- | ------- | ----------------- |
| Parallel Install (No Wait)   | 5                 |  No          | 10m     | **4.11 s**        |
| Parallel Install (With Wait) | 3                 | Yes         | 15m     | **12.76 s**       |

### Helm Benchmark comparison insights

- **Arm64 shows faster Helm execution** for both warm and ready states, indicating efficient CLI and Kubernetes API handling on Arm-based GCP instances.
- **The `--wait` flag significantly increases total execution time** because Helm waits for pods and services to reach a Ready state, revealing scheduler latency and image-pull delays rather than Helm CLI overhead.
- **Parallel Helm installs scale well on Arm64**, with minimal contention observed even at higher concurrency levels.
- **End-to-end workload readiness dominates benchmark results**, showing that cluster resource availability and container image pulls
