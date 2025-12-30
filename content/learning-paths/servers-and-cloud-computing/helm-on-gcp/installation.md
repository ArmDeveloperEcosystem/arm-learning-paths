---
title: Install Helm
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you prepare a SUSE Linux Arm64 virtual machine to work with Helm by installing Docker, kubectl, Helm, and KinD. You then create and verify a local Kubernetes cluster that you use in later sections of this Learning Path to validate Helm workflows.

## Prepare the system

Update the system packages and install dependencies:

```console
sudo zypper refresh
sudo zypper update -y
sudo zypper install -y curl git tar gzip
```

## Enable SUSE Containers Module
Enable the SUSE Containers Module to ensure that Docker and container-related tools are fully supported.
``` console
sudo SUSEConnect -p sle-module-containers/15.5/arm64
sudo SUSEConnect --list-extensions | grep Containers
```
Verify that the output shows the Containers module as **Activated**. 

## Install Docker
Docker is required to run KinD and the Kubernetes control plane components.

Install Docker, start the service, and add your user to the docker group so that Docker commands can be run without sudo:
``` console
sudo zypper refresh
sudo zypper install -y docker
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
exit
```

Exit the current shell and reconnect to the virtual machine so that the group membership change takes effect. Then verify that Docker is running:

```console
docker ps
```

Output similar to the following indicates that Docker is installed and accessible:

```output
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

## Install kubectl
Install kubectl, the command-line tool for interacting with Kubernetes clusters, compiled for the Arm64 architecture.

```console
curl -LO https://dl.k8s.io/release/v1.30.1/bin/linux/arm64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

## Verify kubectl

Confirm that kubectl is installed and accessible from the command line:

```console
kubectl version --client
```

Output similar to the following indicates that kubectl is installed correctly:
```output
Client Version: v1.30.1
Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
```

## Install Helm
Install Helm using the official Helm installation script to get a verified and up-to-date release.

```console
curl -sSfL https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 > get_helm.sh
chmod 755 ./get_helm.sh
./get_helm.sh
```

## Verify Helm
Confirm that Helm is installed correctly and ready to use.

```console
helm version
```

You should see an output similar to:
```output
version.BuildInfo{Version:"v3.19.2", GitCommit:"8766e718a0119851f10ddbe4577593a45fadf544", GitTreeState:"clean", GoVersion:"go1.24.9"}
```

## Install KinD

Install KinD (Kubernetes-in-Docker) to run a lightweight Kubernetes cluster locally on your Arm64 virtual machine:

```console
curl -Lo kind https://kind.sigs.k8s.io/dl/v0.30.0/kind-linux-arm64
chmod +x kind
sudo mv kind /usr/local/bin/
```

## Create a local Kubernetes cluster

Create a local Kubernetes cluster named helm-lab that you use to deploy Helm charts:

```console
kind create cluster --name helm-lab
```

## Verify cluster status
This step verifies that the Kubernetes cluster is operating correctly and is fully prepared to run workloads.

```console
kubectl get nodes
```

You should see an output similar to:
```output
NAME                     STATUS   ROLES           AGE   VERSION
helm-lab-control-plane   Ready    control-plane   23h   v1.34.0
```
The node should be in the **Ready** state. If not, retry the command after waiting 30 seconds for the cluster to fully initialize.

You now have a fully working local Kubernetes cluster running on an Arm64-based virtual machine.

## What you've accomplished and what's next

You've successfully set up your development environment by:
- Installing Docker, kubectl, and Helm on your Arm64 SUSE VM
- Creating a local Kubernetes cluster using KinD
- Verifying that all components are working correctly

Next, you'll validate Helm functionality by performing install, upgrade, and uninstall workflows on your Arm64 Kubernetes cluster.
