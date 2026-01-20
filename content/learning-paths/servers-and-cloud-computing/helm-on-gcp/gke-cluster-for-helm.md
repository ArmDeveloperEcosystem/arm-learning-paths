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

Before starting, ensure that Docker, kubectl, and Helm are installed, and that you have a Google Cloud account available. If Helm and kubectl aren't installed, complete the **Install Helm** section first.

### Verify kubectl Installation
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

Install python3.11:

```bash
sudo zypper install -y python311
which python3.11
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

The shell will exit. Bring up a new SSH Shell:
```console
exit
```

### Initialize gcloud
Authenticate and configure the Google Cloud CLI:

```console
gcloud init
```

During initialization, select **Login with a new account**. You'll be prompted to use your browser to authenticate to Google and receive an auth code to copy back. Select the project you want to use and choose default settings when unsure.

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

Note the **PROJECT_ID** for the project you want to set as active for use in the next step. 
### Set the Active Project
Ensure the correct GCP project is selected:

```console
gcloud config set project YOUR_PROJECT_ID
```

### Install the auth plugin for gcloud
```console
gcloud components install gke-gcloud-auth-plugin
```

### Enable Kubernetes API
Enable the required API for GKE:

```console
gcloud services enable container.googleapis.com
```

### Create a GKE Cluster
Create a Kubernetes cluster to host Helm deployments. Replace `YOUR_PROJECT_ID` with the project ID you set previously.

```console
gcloud container clusters create helm-arm64-cluster \
  --zone us-central1-a \
  --machine-type c4a-standard-4 \
  --num-nodes 2 \
  --no-enable-ip-alias
```

This creates a standard GKE cluster. You can adjust the node count and machine type later as needed.

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

All nodes should be in **Ready** state and the Kubernetes control plane should be accessible.

### Taint the cluster nodes

Taint the nodes to ensure proper scheduling. For each node starting with **gke**, run the taint command. For example: 

```console
kubectl taint nodes gke-helm-arm64-cluster-default-pool-f4ab8a2d-5h6f kubernetes.io/arch=arm64:NoSchedule-
kubectl taint nodes gke-helm-arm64-cluster-default-pool-f4ab8a2d-5ldp kubernetes.io/arch=arm64:NoSchedule-
```

Replace the node names with your actual node names from the previous command output.

### Create hyperdisk storage class for our cluster

In order to use the c4a architecture with our cluster, a new storage class must be created. 

Create a new file, hyperdisk.yaml, with this content:
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: my-hyperdisk-sc
provisioner: pd.csi.storage.gke.io
parameters:
  type: hyperdisk-balanced # Or hyperdisk-ssd, etc.
reclaimPolicy: Delete
volumeBindingMode: WaitForFirstConsumer
```

Apply the hyperdisk.yaml file to the cluster:

```console
kubectl apply -f ./hyperdisk.yaml
```

Confirm that the new storage class has been added:

```console
kubectl get storageclass
```

The output should contain the new **my-hyperdisk-sc** storage class:

```output
NAME                     PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
my-hyperdisk-sc          pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   false                  7m27s
premium-rwo              pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   true                   20m
standard                 kubernetes.io/gce-pd    Delete          Immediate              true                   20m
standard-rwo (default)   pd.csi.storage.gke.io   Delete          WaitForFirstConsumer   true                   20m
```

The new storage class will be used in the next section. 

## What you've accomplished and what's next

You've successfully prepared your GKE environment by installing and configuring the Google Cloud SDK, creating a GKE cluster, connecting kubectl to the cluster, and verifying cluster access. Your environment is now ready to deploy applications using Helm charts.

Next, you'll deploy PostgreSQL on your GKE cluster using a custom Helm chart with persistent storage and secure credentials.

