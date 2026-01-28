---
title: Prepare a GKE cluster for Argo CD deployments
weight: 4

layout: learningpathall
---

## Set up your GKE environment

In this section, you prepare a **production-ready Arm64 Google Kubernetes Engine (GKE) cluster** for **GitOps with Argo CD**.

This cluster is designed for:
- Arm-based workloads (Axion / C4A)
- GitOps-based deployments
- Production-style Kubernetes operation

## Prerequisites

You must have:
- A **SUSE Linux Arm64 VM**
- A **Google Cloud account**
- Internet access from the VM

## Prepare the system

Update the system packages and install dependencies:

```console
sudo zypper refresh
sudo zypper update -y
sudo zypper install -y curl git tar gzip
```

## Install kubectl

Install the kubectl command-line tool for interacting with Kubernetes clusters:

```console
curl -LO https://dl.k8s.io/release/v1.30.1/bin/linux/arm64/kubectl
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

## Verify kubectl installation

Confirm that kubectl is installed and accessible in your PATH:

```console
kubectl version --client
```

The output is similar to:
```output
Client Version: v1.30.1
Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
```

## Install Python 3.11

Install Python 3.11:

```bash
sudo zypper install -y python311
which python3.11
```

### Install Google Cloud SDK (gcloud)

The Google Cloud SDK is required to create and manage GKE clusters.

Download and extract the SDK package:

```console
wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-460.0.0-linux-arm.tar.gz
tar -xvf google-cloud-sdk-460.0.0-linux-arm.tar.gz
```

Run the installation script to set up gcloud:

```console
./google-cloud-sdk/install.sh
```

After installation completes, exit the terminal and reconnect via SSH to apply the PATH changes:

```console
exit
```

### Initialize gcloud

Authenticate and configure the Google Cloud CLI:

```console
gcloud init
```

During initialization, select **Login with a new account**. You'll be prompted to authenticate using your browser and receive an auth code to copy back. Select the project you want to use and choose default settings when unsure.

### Get the list of Google project IDs

Retrieve the list of project IDs:

```console
gcloud projects list
```

The output is similar to:

```output
PROJECT_ID               NAME              PROJECT_NUMBER
imperial-time-463411-q5  My First Project  662694175852
```

Note the **PROJECT_ID** for use in the next step.

### Set the active project

Ensure the correct GCP project is selected:

```console
gcloud config set project <YOUR_PROJECT_ID>
```

Replace `<YOUR_PROJECT_ID>` with your actual project ID from the previous step.

### Install the auth plugin for gcloud

```console
gcloud components install gke-gcloud-auth-plugin
```

### Enable Kubernetes API

Enable the required API for GKE:

```console
gcloud services enable \
  compute.googleapis.com \
  container.googleapis.com
```

### Create a GKE cluster

Create a Kubernetes cluster to host Argo CD deployments:

```console
gcloud container clusters create argocd-arm-cluster   \
--zone us-central1-a   \
--machine-type c4a-standard-4   \
--num-nodes 2   \
--release-channel regular   \
--workload-pool=$(gcloud config get-value project).svc.id.goog \
--enable-ip-alias
```

### Configure kubectl access to GKE

Fetch cluster credentials:

```console
gcloud container clusters get-credentials argocd-arm-cluster   --zone us-central1-a
```

### Verify cluster access

Confirm Kubernetes access:

```console
kubectl get nodes
```

The output is similar to:
```output
NAME                                                STATUS   ROLES    AGE     VERSION
gke-argocd-arm-cluster-default-pool-301523aa-6t7f   Ready    <none>   3h11m   v1.33.5-gke.2072000
gke-argocd-arm-cluster-default-pool-301523aa-cczh   Ready    <none>   3h11m   v1.33.5-gke.2072000

```

All nodes should be in **Ready** state, and the Kubernetes control plane should be accessible.

```console
kubectl get nodes -o jsonpath='{.items[*].status.nodeInfo.architecture}'
```

The output is similar to:

```output
arm64 arm64
```

## Remove taint on the cluster nodes for Arm64 support

Remove the taint on the nodes to ensure proper scheduling on Arm64 VMs. For each node starting with **gke**, run the following taint command. 

{{% notice Note %}}
The required "-" at the end is important for the taint command to work correctly.
{{% /notice %}}

For example, using the node IDs in the output above: 

```console
kubectl taint nodes gke-argocd-arm-cluster-default-pool-301523aa-6t7f kubernetes.io/arch=arm64:NoSchedule-
kubectl taint nodes gke-argocd-arm-cluster-default-pool-301523aa-cczh kubernetes.io/arch=arm64:NoSchedule-
```

Replace the node names with your actual node names from the previous command output.

The output is similar to:

```output
node/gke-argocd-arm-cluster-default-pool-c090f2b1-48t7 untainted
```

## What you've accomplished and what's next

You've successfully prepared a production-ready Arm64 GKE environment by installing and configuring the Google Cloud SDK, creating an Arm-based (Axion) GKE cluster, connecting kubectl to the cluster, and verifying cluster access and node architecture. Your Kubernetes environment is now ready to support GitOps workflows.

In the next section, you'll install Argo CD on the GKE cluster, expose the Argo CD server for external browser access, install and configure the Argo CD CLI, and verify connectivity between the CLI, browser UI, and cluster.
