---
title: Install Helm
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Helm on GCP VM
This section covers preparing a SUSE Arm64 system and installing the required tools to work with Helm using a local Kubernetes cluster created with KinD.

### System Preparation
Update the system and install basic dependencies:

```console
sudo zypper refresh
sudo zypper update -y
sudo zypper install -y curl git tar gzip
```
### Install kubectl
This step installs kubectl, the command-line tool used to interact with Kubernetes clusters, compiled for the Arm64 architecture.

```console
curl -LO https://dl.k8s.io/release/v1.30.1/bin/linux/arm64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

### Verify Installation

This step confirms that `kubectl` is installed correctly and accessible from the command line.

```console
kubectl version --client
```

You should see an output similar to:
```output
Client Version: v1.30.1
Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
```

### Install Helm
This step installs Helm using the official Helm installation script, ensuring you get a verified and up-to-date release.

```console
curl -sSfL https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | console
```

### Verify Installation
This step confirms that Helm is installed correctly and ready to be used.

```console
helm version
```

You should see an output similar to:
```output
version.BuildInfo{Version:"v3.19.2", GitCommit:"8766e718a0119851f10ddbe4577593a45fadf544", GitTreeState:"clean", GoVersion:"go1.24.9"}
```

### Create a Local Kubernetes Cluster (KinD)
This step installs KinD (Kubernetes-in-Docker), which allows you to run a lightweight Kubernetes cluster locally on your Arm64 VM.

```console
curl -Lo kind https://kind.sigs.k8s.io/dl/v0.30.0/kind-linux-arm64
chmod +x kind
sudo mv kind /usr/local/bin/
```

**Create a local Kubernetes cluster:**

This step creates a local Kubernetes cluster named helm-lab that will be used to deploy Helm charts.

```console
kind create cluster --name helm-lab
```

### Verify Cluster Status
This step verifies that the Kubernetes cluster is operating correctly and is fully prepared to run workloads.

```console
kubectl get nodes
```

You should see an output similar to:
```output
NAME                     STATUS   ROLES           AGE   VERSION
helm-lab-control-plane   Ready    control-plane   23h   v1.34.0
```
The node should be in the **Ready** state.

You now have a fully working local Kubernetes environment on Arm64, ready for deploying applications using Helm.
