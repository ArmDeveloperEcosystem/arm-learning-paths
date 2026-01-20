---
title: Prepare a GKE cluster for Helm deployments
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up your GKE environment

In this section you'll prepare a Google Kubernetes Engine (GKE) cluster for deploying Helm charts. The GKE cluster hosts the following services:

- PostgreSQL
- Redis
- NGINX

This setup differs from the earlier KinD-based local cluster, which was used only for local validation.

## Prerequisites

Ensure that Docker, kubectl, and Helm are installed, and that you have a Google Cloud account available. If Helm and kubectl aren't installed, complete the previous section first.

### Verify kubectl installation

Confirm that kubectl is available:

```console
kubectl version --client
```
You should see an output similar to:
```output
Client Version: v1.30.1
Kustomize Version: v5.0.4-0.20230601165947-6ce0bf390ce3
```

### Install Python 3.11

Install Python 3.11:

```bash
sudo zypper install -y python311
which python3.11
```

### Install Google Cloud SDK (gcloud)

The Google Cloud SDK is required to create and manage GKE clusters.

Download and extract:

```console
wget https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-460.0.0-linux-arm.tar.gz
tar -xvf google-cloud-sdk-460.0.0-linux-arm.tar.gz
```

Install gcloud:

```console
./google-cloud-sdk/install.sh
```

After installation completes, exit and reconnect to apply the PATH changes:

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
PROJECT_ID              NAME             PROJECT_NUMBER
arm-lp-test             arm-lp-test      834184475014
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
gcloud services enable container.googleapis.com
```

### Create a GKE cluster

Create a Kubernetes cluster to host Helm deployments:

```console
gcloud container clusters create helm-arm64-cluster \
  --zone us-central1-a \
  --machine-type c4a-standard-4 \
  --num-nodes 2 \
  --no-enable-ip-alias
```

### Configure kubectl access to GKE

Fetch cluster credentials:

```console
gcloud container clusters get-credentials helm-arm64-cluster \
  --zone us-central1-a
```

### Verify cluster access

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

All nodes should be in **Ready** state and the Kubernetes control plane should be accessible.

## What you've accomplished and what's next

You've successfully prepared your GKE environment by installing and configuring the Google Cloud SDK, creating a GKE cluster, connecting kubectl to the cluster, and verifying cluster access. Your environment is now ready to deploy applications using Helm charts.

Next, you'll deploy PostgreSQL on your GKE cluster using a custom Helm chart with persistent storage and secure credentials.

