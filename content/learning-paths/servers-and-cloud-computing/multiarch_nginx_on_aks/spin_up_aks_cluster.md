---
title: Create the AKS cluster
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up a multi-architecture AKS cluster

In this section, you'll create a multi-architecture Azure Kubernetes Service (AKS) cluster that supports both Intel and Arm-based nodes. This setup allows you to deploy and compare workloads across different CPU architectures within the same Kubernetes environment.

You'll work through three activities: 

* Set up authentication - you'll connect to your Azure account using the Azure CLI
* Create the cluster infrastructure - you'll build an AKS cluster with two distinct node pools (one x86 and one Arm)
* Verify connectivity -  you'll confirm your cluster is running and accessible using `kubectl`

This multi-architecture approach gives you the flexibility to run workloads optimized for specific CPU types while maintaining a unified Kubernetes management experience. By the end of this section, you'll have a fully functional cluster ready for deploying containerized applications.

## Create the cluster and resource

To begin, login to your Azure account using the Azure CLI:

```bash
az login
```
Once logged in, create the resource group and AKS cluster with two node pools: 

- One with Intel-based nodes (Standard_D2s_v6)
- One with Arm-based nodes (Standard_D2ps_v6)

{{% notice Note %}}
This Learning Path uses the `westus2` region because it supports both Intel and Arm VM sizes. You can use a different region, but make sure it supports both VM types and AKS.
{{% /notice %}}

Set the environment variables as shown below and run the `az aks` commands on your command line:
 
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
Each command returns JSON output with status information. Look for `"provisioningState": "Succeeded"` in each response to confirm the operation completed successfully.

## Connect to the cluster

Verify `kubectl` is available by running:

```bash
kubectl version --client
```

The output should look similar to:

```output
Client Version: v1.34.1
Kustomize Version: v5.7.1
```

If `kubectl` is installed the version information is printed. If you don't see the version information printed, refer to the [Azure CLI Install Guide](/install-guides/azure-cli) and [kubectl Install Guide](/install-guides/kubectl/).

Next, set up your newly-created K8s cluster credentials using the Azure CLI:

```bash
az aks get-credentials --resource-group $RESOURCE_GROUP --name $CLUSTER_NAME
```
The expected output is:

```output
Merged "nginx-on-arm" as current context in /home/user/.kube/config
```

Now verify you're connected to the cluster:

```bash
kubectl cluster-info
```
The expected output is:

```output
Kubernetes control plane is running at https://nginx-on-a-nginx-on-arm-rg-dd0bfb-eenbox6p.hcp.westus2.azmk8s.io:443
```

With the cluster running, verify the node pools are ready:

```bash
kubectl get nodes -o wide
```

You should see output similar to:

```output
NAME                            STATUS   ROLES    AGE    VERSION
aks-arm-13087205-vmss000002     Ready    <none>   6h8m   v1.32.7
aks-intel-39600573-vmss000002   Ready    <none>   6h8m   v1.32.7
```


With all nodes showing `Ready` status, you're now ready to continue to the next section.

## What you've accomplished and what's next

Great job! You’ve successfully created a multi-architecture AKS cluster with both Arm and x64 node pools. This is a significant milestone and you're now set up to deploy and compare workloads across architectures. Keep going to see your cluster in action!
