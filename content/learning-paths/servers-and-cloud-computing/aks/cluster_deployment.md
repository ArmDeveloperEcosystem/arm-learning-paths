---
# User change
title: "Deploy an Arm-based AKS Cluster using Terraform"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

You can run Azure Kubernetes Service (AKS), a fully managed Kubernetes platform, on the Azure Dpsv5 Virtual Machine series featuring Ampere Altra Arm–based processors. Dpsv5 virtual machines offer compelling price-performance.

## Before you begin


You should have the prerequisite tools installed before starting the Learning Path.

Any computer which has the required tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine with the required tools.

You will need an [Azure portal account](https://azure.microsoft.com/en-in/get-started/azure-portal) to complete this Learning Path. Create an account if you don't have one.

Before you begin, you will also need:
- Login to the Azure CLI
- An SSH key pair

The instructions to create the keys are below.

### Acquire Azure Access Credentials

The installation of Terraform on your desktop or laptop needs to communicate with Azure. Thus, Terraform needs to be authenticated.

For Azure authentication, follow this [guide](/install-guides/azure_login).

### Create an SSH key pair

Generate an SSH key-pair (public key, private key) using `ssh-keygen`. To generate the key-pair, follow this [guide](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

## Create an AKS cluster using Terraform

You can create a new AKS cluster using Terraform.

### Create Terraform files

To create the cluster on AKS, the Terraform configuration is separated into four files: 
- `providers.tf`
- `variables.tf`
- `main.tf`
- `outputs.tf`

Create each of the files with the provided content. 

1. Use a text editor to create the file `providers.tf` with the code below: 

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

2. Use a text editor to create the file `variables.tf` with the code below: 

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

3. Use a text editor to create the file `outputs.tf` with the code below: 

```console
output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}
```

4. Use a text editor to create the file `main.tf` with the code below: 

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

The block labeled `default_node_pool` is used to select the virtual machine type, size, and the number of nodes. 

The nodes are specified to use the `Standard_D2ps_v5` virtual machine type which is a 2 vCPU Altra-based virtual machine with standard SSDs.

There are various Arm-based virtual machines that can be selected. The [Azure VM series descriptions](https://azure.microsoft.com/en-us/pricing/details/virtual-machines/series/) shows that the Dpsv5, Dpdsv5, Dplsv5, Dpldsv5, Epsv5, Epdsv5 all use Ampere Altra. Any of these virtual machine types can be used to create an Arm-based cluster.

### Run the Terraform commands

Run the Terraform commands in the directory where you saved the Terraform files.

### Initialize Terraform

Run `terraform init` to download the dependencies required for Azure as a provider and set up a working directory.

```console
terraform init
```

The output will be similar to:

```output
Initializing the backend...

Initializing provider plugins...
- Finding hashicorp/random versions matching "~> 3.0"...
- Finding hashicorp/azurerm versions matching "~> 3.0"...
- Installing hashicorp/random v3.4.3...
- Installed hashicorp/random v3.4.3 (signed by HashiCorp)
- Installing hashicorp/azurerm v3.48.0...
- Installed hashicorp/azurerm v3.48.0 (signed by HashiCorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

### Deploy the AKS cluster and connect

Run `terraform apply` to create the infrastructure:

```console
terraform apply
```

Answer yes to the prompt to confirm you want to create Google Cloud resources.

It will take about 5 minutes to create the resources. 

When it completes the name of the resource group is printed.

```output
Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

Outputs:

resource_group_name = "arm-aks-demo-rg-exact-wombat"
```

### Configure kubectl

1. In a browser, go to the Azure Kubernetes services console, select the cluster, and click on connect.

![aks1 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/2b50015f-51fb-46f1-8ee1-28fc5db35154)

Instructions for running `az account` and `az aks get-credentials` will be displayed. 

![aks2 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/71631645/45732e69-fe88-4757-98d4-264bf392d10c)

2. Copy the 2 commands and run them

Run the `az account` and `az aks get-credentials` commands you copied.

There is no output from the first command.

The output from the second command is similar to:

```output
Merged "arm-aks-cluster-demo" as current context in /home/ubuntu/.kube/config
```

You are now ready to use `kubectl`

3. Run the following command to see the status of the nodes. 

```console
kubectl get nodes
```

Three nodes should be in the `Ready` state:

```output
NAME                               STATUS   ROLES   AGE   VERSION
aks-demopool-40436376-vmss000000   Ready    agent   10m   v1.24.9
aks-demopool-40436376-vmss000001   Ready    agent   10m   v1.24.9
aks-demopool-40436376-vmss000002   Ready    agent   10m   v1.24.9
```

4. Run the following command to see the current pods running on the cluster.

```console
kubectl get pods -A
```

The output will be similar to:

```output
NAMESPACE     NAME                                  READY   STATUS    RESTARTS   AGE
kube-system   azure-ip-masq-agent-fw66d             1/1     Running   0          12m
kube-system   azure-ip-masq-agent-q7ltm             1/1     Running   0          12m
kube-system   azure-ip-masq-agent-qs2rp             1/1     Running   0          12m
kube-system   cloud-node-manager-k8fdg              1/1     Running   0          12m
kube-system   cloud-node-manager-ml5jq              1/1     Running   0          12m
kube-system   cloud-node-manager-phng2              1/1     Running   0          12m
kube-system   coredns-59b6bf8b4f-msdzd              1/1     Running   0          13m
kube-system   coredns-59b6bf8b4f-wbcgl              1/1     Running   0          11m
kube-system   coredns-autoscaler-5655d66f64-g94zj   1/1     Running   0          13m
kube-system   csi-azuredisk-node-9njln              3/3     Running   0          12m
kube-system   csi-azuredisk-node-mnqnz              3/3     Running   0          12m
kube-system   csi-azuredisk-node-rjmq7              3/3     Running   0          12m
kube-system   csi-azurefile-node-7qmdn              3/3     Running   0          12m
kube-system   csi-azurefile-node-fbpm7              3/3     Running   0          12m
kube-system   csi-azurefile-node-j2sf5              3/3     Running   0          12m
kube-system   konnectivity-agent-77467c5c84-52zsj   1/1     Running   0          2m19s
kube-system   konnectivity-agent-77467c5c84-wdhms   1/1     Running   0          2m15s
kube-system   kube-proxy-hnbpp                      1/1     Running   0          12m
kube-system   kube-proxy-wr6rm                      1/1     Running   0          12m
kube-system   kube-proxy-zssbf                      1/1     Running   0          12m
kube-system   metrics-server-5f8d84558d-5rtgs       2/2     Running   0          11m
kube-system   metrics-server-5f8d84558d-lh2xk       2/2     Running   0          11m
```

5. Run `kubectl` to open a shell on one of the nodes.

```console
kubectl debug node/aks-demopool-40436376-vmss000000 -it --image=ubuntu
```

The terminal will open a shell with output similar to:

```output
Creating debugging pod node-debugger-aks-demopool-40436376-vmss000000-b9tj5 with container debugger on node aks-demopool-40436376-vmss000000.
If you don't see a command prompt, try pressing enter.
root@aks-demopool-40436376-vmss000000:/# 
```

6. At the new shell prompt, run the `uname` command:

```console
uname -a
```

The output confirm the node is an Arm instance:

```output
Linux aks-demopool-40436376-vmss000000 5.15.0-1034-azure #41-Ubuntu SMP Fri Feb 10 19:59:55 UTC 2023 aarch64 aarch64 aarch64 GNU/Linux
``` 

You have successfully created a Kubernetes cluster on AKS using Arm-based instances. 

