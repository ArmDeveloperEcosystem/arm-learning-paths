---
title: Create the AKS Cluster
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Project Overview

Arm CPUs are widely used in web server workloads on Kubernetes (k8s). In this Learning Path, you'll learn how to deploy [nginx](https://nginx.org/) on Arm-based CPUs within a hybrid architecture (x64 and arm64) K8s cluster on Azure's AKS.

Many people begin their journey with Arm on K8s by adding Arm nodes to an existing x64-based cluster.  This tutorial begins the same way.   

To begin, login to azure-cli, and bring up the initial AKS cluster:

### Login to Azure via azure-cli 
If you haven't already, login to your Azure account using the Azure CLI:

```commandline
az login
```

### Create the cluster and resource
Once logged in, you can create the resource group and AKS cluster with two node pools: one with Intel-based nodes, and one with Arm-based nodes:


```commandline
# Set environment variables
export RESOURCE_GROUP=nginx-on-arm-rg
export LOCATION=westus2
export CLUSTER_NAME=nginx-on-arm

# Create resource group
az group create --name $RESOURCE_GROUP --location $LOCATION

# Create AKS cluster with Intel node pool in zone 2
az aks create \
  --resource-group $RESOURCE_GROUP \
  --name $CLUSTER_NAME \
  --location $LOCATION \
  --zones 2 \
  --node-count 1 \
  --node-vm-size Standard_D2s_v6 \
  --nodepool-name intel \
  --generate-ssh-keys

# Add ARM node pool in zone 2
az aks nodepool add \
  --resource-group $RESOURCE_GROUP \
  --cluster-name $CLUSTER_NAME \
  --name arm \
  --zones 2 \
  --node-count 1 \
  --node-vm-size Standard_D2ps_v6

```

### Connect to the cluster

Verify `kubectl` is available by running:

```bash
kubectl version --client
```

If `kubectl` is installed the version information is printed. If you don't see the version information printed refer to the [Azure CLI](/install-guides/azure-cli) and [kubectl](/install-guides/kubectl/) install guides.

Next, set up your newly-created K8s cluster credentials using the Azure CLI:

```bash
az aks get-credentials --resource-group $RESOURCE_GROUP --name $CLUSTER_NAME
```

Finally, test the connection to the cluster with this command:

```bash
kubectl cluster-info
```

If you receive a non-error response, you're successfully connected to the K8s cluster.

Verify your node pools are created correctly:

```bash
kubectl get nodes -o wide
```

You should see two nodes with different instance types:
- `aks-intel-*`: Intel (Standard_D2s_v6)
- `aks-arm-*`: ARM (Standard_D2ps_v6) 

All nodes should show `Ready` status.
