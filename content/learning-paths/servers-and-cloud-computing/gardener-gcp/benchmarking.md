---
title: Gardener Benchmarking
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---


##  Gardener Benchmark on GCP SUSE Arm64 VM
This guide shows how to check the security health of a Gardener Kubernetes cluster running on a GCP SUSE Arm64 VM. We use a tool called **kube-bench**, which checks the cluster against CIS security standards

### Prerequisites
Before starting, make sure:
- Gardener Local successfully installed
- Garden cluster and Shoot cluster in Ready state
- Docker is running
- Admin access on the VM

**Why this matters:**
If the cluster is not running or you don’t have admin access, security checks won’t work.

**Verify cluster:**

```console
kubectl get shoots -n garden
kubectl get nodes
```
If the cluster is not ready, benchmarking does not make sense yet.

### Download kube-bench
Download the Arm64-compatible kube-bench binary from the official GitHub release. This tool will be used to check your Kubernetes cluster against CIS security benchmarks.

```console
curl -L \
https://github.com/aquasecurity/kube-bench/releases/download/v0.10.3/kube-bench_0.10.3_linux_arm64.tar.gz
```

### Extract and Install kube-bench Configuration
Extract the downloaded file and place the kube-bench binary and configuration files in standard system locations so the tool can run correctly.

```console
tar -xvf kube-bench_0.10.3_linux_arm64.tar.gz
sudo mkdir -p /etc/kube-bench
sudo cp -r cfg /etc/kube-bench/
sudo mv kube-bench /usr/local/bin/
```

**Verify binary:**

Confirm that kube-bench is installed in the correct path and make it executable. This ensures the system can successfully run the benchmarking tool.

```console
ls -l /usr/local/bin/kube-bench
```

**Make it executable:**

Execute kube-bench to scan the Kubernetes cluster and evaluate its security based on industry standard CIS checks.

```console
sudo chmod +x /usr/local/bin/kube-bench
```

### Run kube-bench Benchmark
Execute kube-bench to scan the Kubernetes cluster and evaluate its security based on industry standard CIS checks.

```console
sudo /usr/local/bin/kube-bench --config-dir /etc/kube-bench/cfg
```
You should see an output similar to:

```output
5.2.11 Add policies to each namespace in the cluster which has user workloads to restrict the
admission of containers that have `.securityContext.windowsOptions.hostProcess` set to `true`.

5.2.12 Add policies to each namespace in the cluster which has user workloads to restrict the
admission of containers with `hostPath` volumes.

5.2.13 Add policies to each namespace in the cluster which has user workloads to restrict the
admission of containers which use `hostPort` sections.

5.3.1 If the CNI plugin in use does not support network policies, consideration should be given to
making use of a different plugin, or finding an alternate mechanism for restricting traffic
in the Kubernetes cluster.

5.3.2 Follow the documentation and create NetworkPolicy objects as you need them.

5.4.1 If possible, rewrite application code to read Secrets from mounted secret files, rather than
from environment variables.

5.4.2 Refer to the Secrets management options offered by your cloud provider or a third-party
secrets management solution.

5.5.1 Follow the Kubernetes documentation and setup image provenance.

5.7.1 Follow the documentation and create namespaces for objects in your deployment as you need
them.

5.7.2 Use `securityContext` to enable the docker/default seccomp profile in your pod definitions.
An example is as below:
  securityContext:
    seccompProfile:
      type: RuntimeDefault

5.7.3 Follow the Kubernetes documentation and apply SecurityContexts to your Pods. For a
suggested list of SecurityContexts, you may refer to the CIS Security Benchmark for Docker
Containers.

5.7.4 Ensure that namespaces are created to allow for appropriate segregation of Kubernetes
resources and that all new resources are created in a specific namespace.


== Summary policies ==
4 checks PASS
4 checks FAIL
27 checks WARN
0 checks INFO

== Summary total ==
43 checks PASS
38 checks FAIL
49 checks WARN
0 checks INFO
```
### Benchmark summary on x86_64
To compare the benchmark results, the following results were collected by running the same benchmark on a `x86 - c4-standard-4` (4 vCPUs, 15 GB Memory) x86_64 VM in GCP, running SUSE:

| Category / Subsection                       | PASS | FAIL | WARN |
| ------------------------------------------- | :--: | :--: | :--: |
| **1. Control Plane Security Configuration** |      |      |      |
| └─ 1.1 Control Plane Node Configuration Files  |  0   | 18   |  3   |
| └─ 1.2 API Server                              |  9   |  7   |  5   |
| └─ 1.3 Controller Manager                      |  5   |  0   |  1   |
| └─ 1.4 Scheduler                               |  1   |  1   |  0   |
| **2. Etcd Node Configuration**              |      |      |      |
| └─ 2.1-2.7 Etcd Node Config                    |  7   |  0   |  0   |
| **3. Control Plane Configuration**          |      |      |      |
| └─ 3.1 Authentication and Authorization       |  0   |  0   |  3   |
| └─ 3.2 Logging                                 |  0   |  0   |  2   |
| **4. Worker Node Security Configuration**   |      |      |      |
| └─ 4.1 Worker Node Configuration Files         |  2   |  5   |  4   |
| └─ 4.2 Kubelet                                 |  5   |  3   |  3   |
| └─ 4.3 kube-proxy                              |  1   |  0   |  0   |
| **5. Kubernetes Policies**                  |      |      |      |
| └─ 5.1 RBAC and Service Accounts               |  0   |  6   |  7   |
| └─ 5.2 Pod Security Standards                  |  0   |  0   | 13   |
| └─ 5.3 Network Policies and CNI                |  0   |  0   |  2   |
| └─ 5.4 Secrets Management                      |  0   |  0   |  2   |
| └─ 5.5 Extensible Admission Control            |  0   |  0   |  1   |
| └─ 5.7 General Policies                        |  0   |  0   |  4   |
| **Total**                                   | 34   | 42   | 54   |

### Benchmark summary on Arm64
Results from the earlier run on the `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in GCP (SUSE):

| Category / Subsection                            | PASS | FAIL | WARN |
|-------------------------------------------------|:----:|:----:|:----:|
| **1. Control Plane Security Configuration**         |      |      |      |
| └─ 1.1 Control Plane Node Configuration Files  | 0    | 18   | 3    |
| └─ 1.2 API Server                               | 9    | 7    | 5    |
| └─ 1.3 Controller Manager                        | 5    | 0    | 1    |
| └─ 1.4 Scheduler                                | 1    | 1    | 0    |
| **2. Etcd Node Configuration**                       |      |      |      |
| └─ 2.1-2.7 Etcd Node Config                     | 7    | 0    | 0    |
| **3. Control Plane Configuration**                   |      |      |      |
| └─ 3.1 Authentication and Authorization        | 0    | 0    | 3    |
| └─ 3.2 Logging                                  | 1    | 0    | 1    |
| **4. Worker Node Security Configuration**           |      |      |      |
| └─ 4.1 Worker Node Configuration Files         | 2    | 5    | 4    |
| └─ 4.2 Kubelet                                  | 5    | 3    | 3    |
| └─ 4.3 kube-proxy                               | 1    | 0    | 0    |
| **5. Kubernetes Policies**                           |      |      |      |
| └─ 5.1 RBAC and Service Accounts                | 2    | 4    | 6    |
| └─ 5.2 Pod Security Standards                   | 2    | 0    | 9    |
| └─ 5.3 Network Policies and CNI                 | 0    | 0    | 2    |
| └─ 5.4 Secrets Management                       | 0    | 0    | 2    |
| └─ 5.5 Extensible Admission Control             | 0    | 0    | 1    |
| └─ 5.7 General Policies                          | 0    | 0    | 4    |
| **Total**                                       | 43   | 38   | 49   |

### Gardener benchmarking comparison on Arm64 and x86_64

- **Strong Baseline Security:** The cluster passed **43 CIS checks**, indicating a solid foundational security posture out of the box on **Arm64 (C4A)** infrastructure.
- **Control Plane Hardening Gaps:** A significant number of **FAIL results (38)** are concentrated in **control plane file permissions and API server settings**, which are commonly unmet in development and local/KinD-based setups.
- **Healthy Etcd Configuration:** All **Etcd-related checks passed (7/7)**, demonstrating correct encryption, access controls, and secure peer/client configuration on **Arm64**.
- **Worker Node Improvements Needed:** Worker node checks show mixed results, with failures mainly around **kubelet configuration and file permissions**, highlighting clear opportunities for security hardening.
- **Policy-Level Defaults:** Most **Kubernetes policy checks surfaced as WARN**, reflecting features such as **Pod Security Standards, NetworkPolicies, and admission controls** being optional or not strictly enforced by default.
- **Arm64 Parity with x86_64:** The overall benchmark profile aligns with typical results seen on **x86_64 clusters**, confirming that **Arm64 introduces no architecture-specific security limitations**.
- **Production Readiness Signal:** With targeted remediation—especially for **control plane and kubelet configurations**—the **Arm64-based cluster** can achieve **full CIS compliance** while benefiting from **Arm’s cost and energy efficiency**.
