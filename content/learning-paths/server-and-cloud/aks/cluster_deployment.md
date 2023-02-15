---
# User change
title: "Deploy an AKS Cluster"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Prerequisites

* [Azure account](https://azure.microsoft.com/)
* [Install Terraform](https://www.terraform.io/downloads)
* [Install Kubectl](https://kubernetes.io/docs/tasks/tools/)
* [Install Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt)

## Deploy the AKS cluster

For AKS deployment, the Terraform configuration is separated into four files: 
- providers.tf
- variables.tf
- main.tf
- outputs.tf

Add the following code in **providers.tf** file:

```console
terraform {
  required_version = ">=1.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~>3.0"
    }
  }
}
provider "azurerm" {
  features {}
}
```

Add the following code in **variables.tf** file:

```console
variable "agent_count" {
  default = 3
}
variable "cluster_name" {
  default = "arm-aks-cluster-demo"
}
variable "dns_prefix" {
  default = "arm-aks"
}
variable "resource_group_location" {
  default     = "eastus2"
  description = "Location of the resource group."
}
variable "resource_group_name_prefix" {
  default     = "arm-aks-demo-rg"
  description = "Prefix of the resource group name that's combined with a random ID so name is unique in your Azure subscription."
}
variable "ssh_public_key" {
  default = "~/.ssh/id_rsa.pub"
}
```

Add the following code in **outputs.tf** file:

```console
output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}
```

Add the following code in **main.tf** file:

```console
# Generate random resource group name
resource "random_pet" "rg_name" {
  prefix = var.resource_group_name_prefix
}
resource "azurerm_resource_group" "rg" {
  location = var.resource_group_location
  name     = random_pet.rg_name.id
}
resource "azurerm_kubernetes_cluster" "k8s" {
  location            = azurerm_resource_group.rg.location
  name                = var.cluster_name
  resource_group_name = azurerm_resource_group.rg.name
  dns_prefix          = var.dns_prefix
  tags                = {
    Environment = "Demo"
  }
  default_node_pool {
    name       = "demopool"
    vm_size    = "Standard_D2ps_v5"
    node_count = var.agent_count
  }
  linux_profile {
    admin_username = "ubuntu"
    ssh_key {
      key_data = file(var.ssh_public_key)
    }
  }
  identity {
    type = "SystemAssigned"
  }
}
```

The block labeled **default_node_pool** is where we select the VM **(vm_size)** and number of nodes **(node_count)** for the cluster. **vm_size** is how we set the cluster to be deployed with Altra Arm-based VMs. Here we select **Standard_D2ps_v5** which is a 2 vCPU Altra-based VM with standard SSDs.

There are various Arm-based VMs that can be selected. The [Azure VM series descriptions](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/series/) show that the Dpsv5, Dpdsv5, Dplsv5, Dpldsv5, Epsv5, Epdsv5 all use Ampere Altra. Using any of these VM types creates an Arm-based cluster.

Log into Azure.

```console
az login
```

Create an SSH key pair.

```console
ssh-keygen -m PEM -t rsa -b 4096
```

Initialize a working directory containing Terraform configuration files.

```console
terraform init
```

Deploy the cluster with Terraform.

```console
terraform apply
```
Once it completes the name of the resource group is displayed.

![Output_screenshot](https://user-images.githubusercontent.com/67620689/201339586-c2d12941-a24f-4ca7-9418-c8475834abc7.PNG)

Download the cluster credentials so that we can use the kubectl command. 

Within the Kubernetes services console, select the cluster and click on connect.

![Connect_screenshot](https://user-images.githubusercontent.com/67620689/201339809-5bc576c8-d945-431f-ab0b-f0b426b1edec.PNG)

Clicking connect brings up instructions that list two commands. An **az account** set command, and an **az aks get-credentials** command. 

Once these two commands are executed, we will be able to use kubectl.

![aks_screenshot](https://user-images.githubusercontent.com/67620689/201339840-5d3a414b-e944-4a3e-96a5-bbbe7a3b13f3.PNG)

Run the following command to see the status of the nodes. They should be in the ready state.

```console
kubectl get nodes
```

![status_screenshot](https://user-images.githubusercontent.com/67620689/200743934-20374d3f-21af-4f4e-893c-154bbae573d8.PNG)

Run the following command to see the current pods running on the cluster.

```console
kubectl get pods -A
```

![pod_screenshot](https://user-images.githubusercontent.com/67620689/200744042-582be388-fabb-4c86-a983-af230f3806f0.PNG)
