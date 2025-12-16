---
title: Benchmark Gardener cluster security with kube-bench
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Benchmark your Gardener cluster security

This section shows you how to evaluate the security health of your Gardener Kubernetes cluster running on a Google Cloud Arm64 (C4A) VM. You'll use kube-bench, a security scanning tool that checks your cluster against Center for Internet Security (CIS) Kubernetes benchmarks. These benchmarks provide industry-standard security recommendations for Kubernetes deployments.

## Verify prerequisites

Before benchmarking, confirm that your environment is ready. You need a running Gardener Local installation with Garden and Shoot clusters in Ready state, Docker running, and admin access to your VM.

Check your cluster status:

```console
cd ~/gardener
export KUBECONFIG=$PWD/example/gardener-local/kind/local/kubeconfig
kubectl apply -f example/provider-local/shoot.yaml
kubectl -n garden-local get shoots
kubectl get nodes
```

The output shows your Shoot cluster and node status. Both should display "Ready" state before proceeding. If your cluster isn't ready, wait for all components to start before running security benchmarks.

## Download kube-bench for Arm64

Download the Arm64-compatible kube-bench binary from the official GitHub release. This version is compiled specifically for aarch64 architecture and ensures accurate security scanning on your C4A VM.

```console
cd ~
curl -L https://github.com/aquasecurity/kube-bench/releases/download/v0.10.3/kube-bench_0.10.3_linux_arm64.tar.gz --output ./kube-bench_0.10.3_linux_arm64.tar.gz
```

## Install kube-bench

Extract the downloaded archive and place the kube-bench binary and configuration files in standard system locations:

```console
tar -xvf kube-bench_0.10.3_linux_arm64.tar.gz
sudo mkdir -p /etc/kube-bench
sudo cp -r cfg /etc/kube-bench/
sudo mv kube-bench /usr/local/bin/
```

Verify the installation and make the binary executable:

```console
ls -l /usr/local/bin/kube-bench
```

Make it executable:

Execute kube-bench to scan the Kubernetes cluster and evaluate its security based on industry standard CIS checks.

```console
sudo chmod +x /usr/local/bin/kube-bench
```

The binary is now ready to scan your cluster.

### Run the security benchmark

Execute kube-bench to scan your Kubernetes cluster against CIS security standards:

```console
sudo /usr/local/bin/kube-bench --config-dir /etc/kube-bench/cfg
```

The tool evaluates your cluster configuration across multiple security domains, including control plane settings, node configurations, Role-Based Access Control (RBAC) policies, and network policies. The scan takes one to two minutes to complete.

The output is similar to:

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
suggested list of SecurityContexts, you may see the CIS Security Benchmark for Docker
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

## Interpret the results

The kube-bench output categorizes security checks into four result types:

- PASS: your cluster meets the CIS security recommendation
- FAIL: your cluster doesn't meet the recommendation and needs remediation
- WARN: the check requires manual review or represents optional security hardening
- INFO: informational findings that don't require action

Your benchmark results show 43 passing checks, 38 failures, and 49 warnings. These numbers provide a baseline security score for your Gardener cluster on Arm64 infrastructure.

## Review the benchmark summary

The following table shows typical results from running kube-bench on a `c4a-standard-4` (4 vCPU, 16 GB memory) Arm64 VM in Google Cloud with SUSE Linux Enterprise Server:

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

## Interpret your security posture

Your benchmark results reveal several key insights about your Gardener cluster's security on Arm64 infrastructure:

- Strong foundational security: the cluster passed 43 CIS checks, demonstrating solid baseline security out of the box on C4A Arm64 infrastructure. This indicates that Gardener's default configurations align well with security best practices.

- Etcd security is excellent: all seven Etcd-related checks passed, confirming correct encryption, access controls, and secure peer and client configuration. Your distributed key-value store, which holds critical cluster state, is properly secured.

- Control plane needs hardening: the 38 failed checks concentrate in control plane file permissions and API server settings. These failures are typical in development and Kubernetes in Docker (KinD) based setups. For production deployments, you should remediate control plane configuration issues.

- Worker node improvements available: worker node checks show mixed results, with failures mainly in kubelet configuration and file permissions. These represent clear opportunities for security hardening, particularly around authentication and authorization settings.

- Policy enforcement is optional: most Kubernetes policy checks appear as warnings, reflecting that features such as Pod Security Standards, network policies, and admission controls aren't strictly enforced by default. You can enable these features based on your security requirements.

- Arm64 architecture shows no security limitations: the benchmark profile matches typical results on x86_64 clusters, confirming that Arm64 introduces no architecture-specific security constraints. You can achieve the same security standards on Arm as on traditional x86 infrastructure while benefiting from Arm's cost and energy efficiency.

With targeted remediation of control plane and kubelet configurations, your Arm64-based Gardener cluster can achieve full CIS compliance while maintaining the performance and cost advantages of Google Cloud's C4A instances.

## Summary and what's next

You have successfully benchmarked your Gardener cluster's security posture using industry-standard CIS checks. You now understand your cluster's security strengths and areas for improvement. Your next step is to implement security hardening based on the failed and warned checks to prepare your cluster for production workloads.
