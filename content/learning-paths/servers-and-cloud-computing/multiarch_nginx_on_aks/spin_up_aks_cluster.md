---
title: Create the AKS Cluster
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Project Overview

Arm CPUs are widely used in web server workloads on Kubernetes (k8s). In this Learning Path, you'll learn how to deploy [nginx](https://nginx.org/) on Arm-based CPUs within a heterogeneous (x64 and arm64) K8s cluster on Azure's AKS.

### Benefits of the multi-architecture approach

Many developers begin their journey with Arm on K8s by adding Arm nodes to an existing x64-based cluster.  This has many advantages:

1. Since you are already familiar with K8s on x64, you can leverage that knowledge to quickly get the core components up and running.
2. Leveraging the multi-architectural container image of your existing x64 workload expedites the migration to Arm with minimal deployment modifications. 
3. With both x64 and Arm workloads running in the same cluster, comparing performance across them is simplified.

This Learning Path explains how to create an initial AKS environment and install nginx on x64.  From there, you'll add Arm-based nodes running the same exact workload.  You'll see how to run simple tests to verify functionality, and then run performance testing to better understand the performance characteristics of each architecture.

### Login to Azure using the Azure CLI

To begin, login to your Azure account using the Azure CLI:

```bash
az login
```

### Create the cluster and resource

Once logged in, create the resource group and AKS cluster with two node pools: one with Intel-based nodes (Standard_D2s_v6), and one with Arm-based (Standard_D2ps_v6) nodes.  

{{% notice Note %}}
This tutorial uses the `westus2` region, which supports both Intel and Arm VM sizes. You can choose a different region if you prefer, but ensure it supports both VM types and AKS.
{{% /notice %}}

Set the environment variables as shown below and run the `az aks` commands on your command line.
 
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

Each command returns JSON output. Verify that `"provisioningState": "Succeeded"` appears in each response.

### Connect to the cluster

Verify `kubectl` is available by running:

```bash
kubectl version --client
```

The output should look similar to:

```output
Client Version: v1.34.1
Kustomize Version: v5.7.1
```

If `kubectl` is installed the version information is printed. If you don't see the version information printed refer to the [Azure CLI](/install-guides/azure-cli) and [kubectl](/install-guides/kubectl/) install guides.

Next, set up your newly-created K8s cluster credentials using the Azure CLI:

```bash
az aks get-credentials --resource-group $RESOURCE_GROUP --name $CLUSTER_NAME
```

You should see:

```output
Merged "nginx-on-arm" as current context in /home/user/.kube/config
```

To verify you're connected to the cluster:

```bash
kubectl cluster-info
```

A message similar to the following should be displayed:

```output
Kubernetes control plane is running at https://nginx-on-a-nginx-on-arm-rg-dd0bfb-eenbox6p.hcp.westus2.azmk8s.io:443
```

With the cluster running, verify the node pools are ready with the following command:

```bash
kubectl get nodes -o wide
```

You should see output similar to:

```output
NAME                            STATUS   ROLES    AGE    VERSION
aks-arm-13087205-vmss000002     Ready    <none>   6h8m   v1.32.7
aks-intel-39600573-vmss000002   Ready    <none>   6h8m   v1.32.7
```


With all nodes showing `Ready` status, you're ready to continue to the next section.
