---
# User change
title: "Deploy an Arm-based AKS Cluster using Terraform"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

You can run Azure Kubernetes Service (AKS), a fully managed Kubernetes platform, on Azure Cobalt 200 virtual machines. Azure Cobalt 200 is Microsoft's second-generation Arm-based processor, built on Arm Neoverse Compute Subsystems V3 (CSS V3). In this Learning Path, you use the general-purpose Dpsv7 virtual machine series for the AKS nodes.

Your subscription and selected region must have access to Dpsv7 sizes and sufficient vCPU quota. This Learning Path was validated in **West US 2**.

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

For Azure authentication, follow this [guide](/install-guides/azure_login/).

### Create an SSH key pair

Generate an SSH key-pair (public key, private key) using `ssh-keygen`. To generate the key-pair, follow this [guide](/install-guides/ssh/#ssh-keys).

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
      version = "~>5.0"
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
  default     = "westus2"
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
output "cluster_name" {
  value = azurerm_kubernetes_cluster.k8s.name
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
    vm_size    = "Standard_D2ps_v7"
    node_count = var.agent_count
  }
  node_provisioning_profile {
    mode = "Manual"
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

The nodes are specified to use the `Standard_D2ps_v7` virtual machine type, which is a 2 vCPU Cobalt 200 virtual machine.

The `node_provisioning_profile` block is required by the current Azure provider for Terraform. Setting `mode` to `Manual` means that you choose the node pool size and VM type yourself.

There are various Arm-based virtual machines that can be selected. The Cobalt 200 series include Dpsv7, Dpdsv7, Dplsv7, Dpldsv7, Epsv7, and Epdsv7. See the [Azure Cobalt 200 virtual machines overview](https://azure.microsoft.com/en-us/blog/new-azure-cobalt-200-vms-deliver-50-performance-improvement-fully-optimized-for-modern-agentic-ai-workloads/) for details. Any of these virtual machine types can be used to create an Arm-based cluster, provided your subscription and region have access to them.

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
- Finding hashicorp/azurerm versions matching "~> 5.0"...
- Installing hashicorp/random v3.9.1...
- Installed hashicorp/random v3.9.1 (signed by HashiCorp)
- Installing hashicorp/azurerm v5.14.0...
- Installed hashicorp/azurerm v5.14.0 (signed by HashiCorp)

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

Answer `yes` at the prompt to confirm you want to create the Azure resources.

It will take about 5 to 10 minutes to create the resources. 

When it completes, the name of the resource group and the cluster are printed.

```output
Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

Outputs:

cluster_name = "arm-aks-cluster-demo"
resource_group_name = "arm-aks-demo-rg-possible-mastiff"
```

### Configure kubectl

1. Use the Terraform outputs to get the credentials for the new cluster and add them to your `kubectl` configuration:

```console
az aks get-credentials --resource-group $(terraform output -raw resource_group_name) --name $(terraform output -raw cluster_name)
```

The output is similar to:

```output
Merged "arm-aks-cluster-demo" as current context in /home/ubuntu/.kube/config
```

You are now ready to use `kubectl`.

2. Run the following command to see the status of the nodes. 

```console
kubectl get nodes
```

Three nodes should be in the `Ready` state:

```output
NAME                               STATUS   ROLES    AGE    VERSION
aks-demopool-15110407-vmss000000   Ready    <none>   2m5s   v1.36.5
aks-demopool-15110407-vmss000001   Ready    <none>   2m5s   v1.36.5
aks-demopool-15110407-vmss000002   Ready    <none>   2m4s   v1.36.5
```

3. Confirm the virtual machine size and architecture of the nodes:

```console
kubectl get nodes -L node.kubernetes.io/instance-type,kubernetes.io/arch
```

The output shows that the nodes are Cobalt 200 `Standard_D2ps_v7` virtual machines with the `arm64` architecture:

```output
NAME                               STATUS   ROLES    AGE    VERSION   INSTANCE-TYPE      ARCH
aks-demopool-15110407-vmss000000   Ready    <none>   2m5s   v1.36.5   Standard_D2ps_v7   arm64
aks-demopool-15110407-vmss000001   Ready    <none>   2m5s   v1.36.5   Standard_D2ps_v7   arm64
aks-demopool-15110407-vmss000002   Ready    <none>   2m4s   v1.36.5   Standard_D2ps_v7   arm64
```

4. Run the following command to see the current pods running on the cluster.

```console
kubectl get pods -A
```

The output will be similar to:

```output
NAMESPACE     NAME                                             READY   STATUS    RESTARTS   AGE
kube-system   azure-cns-9hlcm                                  2/2     Running   0          4m8s
kube-system   azure-cns-9zpvw                                  2/2     Running   0          4m7s
kube-system   azure-cns-m6xqg                                  2/2     Running   0          4m8s
kube-system   azure-ip-masq-agent-g8nr4                        1/1     Running   0          4m7s
kube-system   azure-ip-masq-agent-wv4zh                        1/1     Running   0          4m8s
kube-system   azure-ip-masq-agent-zhzq6                        1/1     Running   0          4m8s
kube-system   cloud-node-manager-8vxcc                         1/1     Running   0          4m8s
kube-system   cloud-node-manager-dr5m5                         1/1     Running   0          4m8s
kube-system   cloud-node-manager-vhkz5                         1/1     Running   0          4m7s
kube-system   coredns-5bf45f87d-95zhw                          1/1     Running   0          4m34s
kube-system   coredns-5bf45f87d-tgmx7                          1/1     Running   0          3m42s
kube-system   coredns-autoscaler-7467554f77-b5jvl              1/1     Running   0          4m34s
kube-system   csi-azuredisk-node-8nstr                         3/3     Running   0          4m7s
kube-system   csi-azuredisk-node-jtjxn                         3/3     Running   0          4m7s
kube-system   csi-azuredisk-node-rwqqz                         3/3     Running   0          4m8s
kube-system   csi-azurefile-node-7pxf6                         4/4     Running   0          4m7s
kube-system   csi-azurefile-node-ljgdr                         4/4     Running   0          4m7s
kube-system   csi-azurefile-node-zgkx5                         4/4     Running   0          4m8s
kube-system   konnectivity-agent-7d7c8bcd59-8cr8d              1/1     Running   0          3m42s
kube-system   konnectivity-agent-7d7c8bcd59-qmc7g              1/1     Running   0          4m21s
kube-system   konnectivity-agent-autoscaler-5b658f6697-mhpkl   1/1     Running   0          4m21s
kube-system   kube-proxy-4td8b                                 1/1     Running   0          4m7s
kube-system   kube-proxy-p2rxj                                 1/1     Running   0          4m7s
kube-system   kube-proxy-zdhdm                                 1/1     Running   0          4m8s
kube-system   metrics-server-866c8cb87d-5ptrp                  2/2     Running   0          3m36s
kube-system   metrics-server-866c8cb87d-9jmmb                  2/2     Running   0          3m36s
```

You have successfully created a Kubernetes cluster on AKS using Arm-based instances. 

