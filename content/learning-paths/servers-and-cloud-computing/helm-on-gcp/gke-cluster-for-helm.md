---
title: Prepare GKE Cluster for Helm Deployments
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
This section explains how to prepare a **Google Kubernetes Engine (GKE) cluster** for deploying Helm charts.
The prepared GKE cluster is used to deploy the following services using custom Helm charts:

- PostgreSQL
- Redis
- NGINX

This setup differs from the earlier KinD-based local cluster, which was intended only for local validation.

## Prerequisites

Before starting, ensure the following are already completed:

- Docker installed
- kubectl installed
- Helm installed
- Google Cloud account available

If Helm and kubectl are not installed, complete the **Install Helm** section first.

### Verify kubectl Installation
Confirm that kubectl is available:

```console
kubectl version --client
```
You should see an output similar to:
```output
Client Version: version.Info{Major:"1", Minor:"26+", GitVersion:"v1.26.15-dispatcher", GitCommit:"5490d28d307425a9b05773554bd5c037dbf3d492", GitTreeState:"clean", BuildDate:"2024-04-18T22:39:37Z", GoVersion:"go1.21.9", Compiler:"gc", Platform:"linux/arm64"}
Kustomize Version: v4.5.7
```

### Install Google Cloud SDK (gcloud)
The Google Cloud SDK is required to create and manage GKE clusters.

**Download and extract:**

```console
wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-460.0.0-linux-arm.tar.gz
tar -xvf google-cloud-sdk-460.0.0-linux-arm.tar.gz
```

**Install gcloud:**

```console
./google-cloud-sdk/install.sh
```
Restart the shell or reload the environment if prompted.

### Initialize gcloud
Authenticate and configure the Google Cloud CLI:

```console
./google-cloud-sdk/bin/gcloud init
```

During initialization:

- Log in using a Google account
- Select the correct project
- Choose default settings when unsure

### Set the Active Project
Ensure the correct GCP project is selected:

```console
gcloud config set project YOUR_PROJECT_ID
```

### Enable Kubernetes API
Enable the required API for GKE:

```console
gcloud services enable container.googleapis.com
```

### Create a GKE Cluster
Create a Kubernetes cluster that will host Helm deployments.

```console
gcloud container clusters create helm-arm64-cluster \
  --zone us-central1-a \
  --machine-type c4a-standard-4 \
  --num-nodes 2
```

- This creates a standard GKE cluster
- Node count and machine type can be adjusted later
- Arm64 compatibility depends on available node types in the region

### Configure kubectl Access to GKE
Fetch cluster credentials:

```console
gcloud container clusters get-credentials helm-arm64-cluster \
  --zone us-central1-a
```

### Verify Cluster Access
Confirm Kubernetes access:

```console
kubectl get nodes
```

You should see an output similar to:
```output
NAME                                                STATUS   ROLES    AGE     VERSION
gke-helm-arm64-cluster-default-pool-f4ab8a2d-5h6f   Ready    <none>   5h54m   v1.33.5-gke.1308000
gke-helm-arm64-cluster-default-pool-f4ab8a2d-5ldp   Ready    <none>   5h54m   v1.33.5-gke.1308000
```

- Nodes in Ready state
- Kubernetes control plane accessible

### Outcome
At this point:

- Google Cloud SDK is installed and configured
- GKE cluster is running
- kubectl is connected to the cloud cluster
- Helm is ready to deploy applications on GKE

The environment is now prepared to deploy Helm charts.

