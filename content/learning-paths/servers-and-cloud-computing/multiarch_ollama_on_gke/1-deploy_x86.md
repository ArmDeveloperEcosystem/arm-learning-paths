---
title: Deploy ollama x86 to the cluster
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

Any easy way to experiment with Arm nodes in your K8s cluster is to deploy Arm nodes and pods alongside your existing x86 node and pods. In this section of the tutorial, you'll bootstrap the cluster with ollama on x86, which prepares you for the next section of the tutorial, where you'll add Arm nodes and pods to the mix.

### Connect to the cluster

{{% notice Note %}}
The following assumes you have gcloud and kubectl already installed.  If not, please follow the instructions on the first page under "Prerequisites". 
{{% /notice %}}

You'll first setup your newly created K8s cluster credentials using the gcloud utility.  Enter the following in your command prompt (or cloud shell), and make sure to replace "YOUR_PROJECT_ID" with the ID of your GCP project:

```bash
export ZONE=us-central1
export CLUSTER_NAME=ollama-on-arm
export PROJECT_ID=YOUR_PROJECT_ID
gcloud container clusters get-credentials $CLUSTER_NAME --zone $ZONE --project $PROJECT_ID
```
If you get the error:

```commandline
CRITICAL: ACTION REQUIRED: gke-gcloud-auth-plugin, which is needed for continued use of kubectl, was not found or is not executable. Install gke-gcloud-auth-plugin for use with kubectl by following https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#install_plugin
```
This command should help resolve it:

```bash
gcloud components install gke-gcloud-auth-plugin
```
Test the connection to the cluster with this command:

```commandline
kubectl cluster-info
```
If you receive a non-error response, you're successfully connected to the k8s cluster!

### Deployment and Service

1. Copy the following YAML, and save it to a file called x86_ollama.yaml:
```yaml

```
