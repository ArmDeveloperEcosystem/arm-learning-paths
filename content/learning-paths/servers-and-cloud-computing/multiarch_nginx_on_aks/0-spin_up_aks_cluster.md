---
title: Create the AKS Cluster
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Project Overview

Arm CPUs are widely used in web server workloads on Kubernetes. In this Learning Path, you'll learn how to deploy [nginx](https://nginx.org/) on Arm-based CPUs within a hybrid architecture (amd64 and arm64) K8s cluster.

First, you'll bring up an initial Kubernetes cluster with an amd64 node running an nginx Deployment and Service.

Next, you'll expand the cluster by adding an arm64 deployment and service to it, forming a hybrid cluster. This allows you to test both architectures together, and separately, to investigate performance. 

Once satisfied with arm64 performance, you can remove the amd64-specific node, deployment, and service, which then completes your migration to an arm64-only cluster.

Once you've seen how easy it is to add arm64 nodes to an existing cluster, you will be ready to explore arm64 nodes for other workloads in your environment.
 
### Create the cluster

Create the resource group and AKS cluster with all three node pools:

```bash
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

# Add AMD node pool in zone 2
az aks nodepool add \
  --resource-group $RESOURCE_GROUP \
  --cluster-name $CLUSTER_NAME \
  --name amd \
  --zones 2 \
  --node-count 1 \
  --node-vm-size Standard_D2as_v6
```

### Connect to the cluster

Ensure you have `kubectl` and `az` (Azure CLI) installed. 

You can verify each command by printing the version.

Verify `az` by running:

```bash
az version
```

If `az` is installed the version information is printed. 

Verify `kubectl` by running:

```bash
kubectl version --client
```

If `kubectl` is installed the version information is printed. 

If you don't see the version information printed refer to the [Azure CLI](/install-guides/azure-cli) and [kubectl](/install-guides/kubectl/) install guides.

Now you can set up your newly-created K8s cluster credentials using the Azure CLI:

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

Verify your node pools are created correctly:

```bash
kubectl get nodes -o wide
```

You should see three nodes with different instance types:
- `aks-intel-*`: Intel (Standard_D2s_v6)
- `aks-arm-*`: ARM (Standard_D2ps_v6) 
- `aks-amd-*`: AMD (Standard_D2as_v6)

All nodes should show `Ready` status and be running Ubuntu 22.04.5 LTS.
