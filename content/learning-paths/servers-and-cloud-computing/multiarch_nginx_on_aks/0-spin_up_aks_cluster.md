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

```bash
az login
```

### Create the cluster and resource
Once logged in, create the resource group and AKS cluster with two node pools: one with Intel-based nodes (Standard_D2s_v6), and one with Arm-based (Standard_D2ps_v6) nodes.  

{{% notice Note %}}
This tutorial uses the `westus2` region, which supports both Intel and Arm VM sizes. You can choose a different region if you prefer, but ensure it supports both VMs and AKS.
{{% /notice %}}

 
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

To verify you're connected to the cluster:

```bash
kubectl cluster-info
```

A message similar to the following should be displayed:

```output
Kubernetes control plane is running at https://nginx-on-a-nginx-on-arm-rg-dd0bfb-eenbox6p.hcp.westus2.azmk8s.io:443
...
```

With the cluster running, verify the node pools are ready (and you're ready to continue to the next chapter), with the following command:

```bash
kubectl get nodes -o wide
```

You should see output similar to this:

```output
NAME                            STATUS   ROLES    AGE    VERSION
aks-arm-13087205-vmss000002     Ready    <none>   6h8m   v1.32.7
aks-intel-39600573-vmss000002   Ready    <none>   6h8m   v1.32.7
```


With all nodes showing `Ready` status, you're ready to continue to the next chapter.
