---
# User change
title: "Automate Azure VM creation with Terraform"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
This Learning Path uses [Terraform Cloud](https://registry.terraform.io/) to automate instantiation of Arm instances. Reader may wish to also see:
* [Getting Started with Microsoft Azure](/learning-paths/servers-and-cloud-computing/csp/azure/)
* [Deploy a Windows on Arm virtual machine on Microsoft Azure](/learning-paths/cross-platform/woa_azure/)
     * These same instructions can be used to deploy Linux as well.

You will need an [Azure portal account](https://portal.azure.com/). Create an account if needed.

## Before you begin

Two tools are required on the computer you are using. Follow the links to install the required tools.

* [Terraform](/install-guides/terraform)
* [Azure CLI](/install-guides/azure-cli)

## Generate an SSH key-pair

Generate an SSH key-pair (public key, private key) using `ssh-keygen` to use for Arm VMs access. To generate the key-pair, follow this [
guide](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

## Acquire Azure Access Credentials

The installation of Terraform on your Desktop/Laptop needs to communicate with Azure. Thus, Terraform needs to be authenticated.

For Azure authentication, follow this [guide](/install-guides/azure_login).

## Image References

Before provisioning Terraform infrastructure, retrieve the required image details. For reference, please follow https://learn.microsoft.com/en-us/azure/virtual-machines/linux/cli-ps-findimage. The publisher, offer, sku and version details are needed to create a VM.

Get list of publishers for a specific location (eastus2):

```console
az vm image list-publishers --location eastus2 --output table
```

Get list of offers for required publishers (Canonical):

```console
az vm image list-offers --location eastus2 --publisher Canonical --output table
```

Get list of skus for required publisher and offer:

```console
az vm image list-skus --location eastus2 --publisher Canonical --offer 0001-com-ubuntu-server-focal --output table
```

Get image details for required publisher, offer and sku:

```console
az vm image list --location eastus2 --publisher Canonical --offer 0001-com-ubuntu-server-focal --sku 20_04-lts-arm64 --all --output table
```

**Image list:**

![image #center](https://user-images.githubusercontent.com/42368140/196460588-3aa72ac1-5f0f-4c57-a6d7-70e81787f137.PNG)

## Terraform infrastructure
Start by creating empty `providers.tf`, `variables.tf`, `main.tf` and `outputs.tf` files in your desired directory:

```console
touch providers.tf variables.tf main.tf outputs.tf
```

### Providers

Tell Terraform which cloud provider to connect to, Azure for this example.

Add below code to the `providers.tf` file:

```console
terraform {
  required_version = ">=0.12"

  required_providers {
    azurerm = {
      source= "hashicorp/azurerm"
      version = "~>2.0"
    }
    random = {
      source= "hashicorp/random"
      version = "~>3.0"
    }
    tls = {
    source = "hashicorp/tls"
    version = "~>4.0"
    }
  }
}

provider "azurerm" {
  features {}
}
``` 

### Variables

Define required variables to create a virtual machine.

Add below code to the `variables.tf` file: 

```console
variable "resource_group_location" {
  default = "eastus2"
  description = "Location of the resource group."
}

variable "resource_group_name_prefix" {
  default = "rg"
  description = "Prefix of the resource group name that's combined with a random ID so name is unique in your Azure subscription."
}
```

### Create required resources

Define required resources to create a virtual machine.

Add below code to the `main.tf` file:

```console
resource "random_pet" "rg_name" {
  prefix = var.resource_group_name_prefix
}

resource "azurerm_resource_group" "rg" {
  location = var.resource_group_location
  name = random_pet.rg_name.id
}

# Create virtual network
resource "azurerm_virtual_network" "my_terraform_network" {
  name = "myVnet"
  address_space = ["10.0.0.0/16"]
  location = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

# Create subnet
resource "azurerm_subnet" "my_terraform_subnet" {
  name = "mySubnet"
  resource_group_name = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.my_terraform_network.name
  address_prefixes = ["10.0.1.0/24"]
}

# Create Public IPs
resource "azurerm_public_ip" "my_terraform_public_ip" {
  name = "myPublicIP"
  location = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  allocation_method = "Dynamic"
}

# Create Network Security Group and rule
resource "azurerm_network_security_group" "my_terraform_nsg" {
  name= "myNetworkSecurityGroup"
  location= azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  security_rule {
    name= "SSH"
    priority= 1001
    direction= "Inbound"
    access = "Allow"
    protocol= "Tcp"
    source_port_range= "*"
    destination_port_range = "22"
    source_address_prefix= "*"
    destination_address_prefix = "*"
  }
}

# Create network interface
resource "azurerm_network_interface" "my_terraform_nic" {
  name= "myNIC"
  location= azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  ip_configuration {
    name= "my_nic_configuration"
    subnet_id = azurerm_subnet.my_terraform_subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id= azurerm_public_ip.my_terraform_public_ip.id
  }
}

# Connect the security group to the network interface
resource "azurerm_network_interface_security_group_association" "example" {
  network_interface_id= azurerm_network_interface.my_terraform_nic.id
  network_security_group_id = azurerm_network_security_group.my_terraform_nsg.id
}

# Generate random text for a unique storage account name
resource "random_id" "random_id" {
  keepers = {
    # Generate a new ID only when a new resource group is defined
    resource_group = azurerm_resource_group.rg.name
  }

  byte_length = 8
}

# Create storage account for boot diagnostics
resource "azurerm_storage_account" "my_storage_account" {
  name = "diag${random_id.random_id.hex}"
  location = azurerm_resource_group.rg.location
  resource_group_name= azurerm_resource_group.rg.name
  account_tier = "Standard"
  account_replication_type = "LRS"
}

# Create virtual machine
resource "azurerm_linux_virtual_machine" "my_terraform_vm" {
  name= "myVM"
  location= azurerm_resource_group.rg.location
  resource_group_name= azurerm_resource_group.rg.name
  network_interface_ids = [azurerm_network_interface.my_terraform_nic.id]
  size= "Standard_D2ps_v5"

  os_disk {
    name = "myOsDisk"
    caching= "ReadWrite"
    storage_account_type = "Premium_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer = "0001-com-ubuntu-server-focal"
    sku= "20_04-lts-arm64"
    version= "20.04.202209200"
  }

  computer_name= "myvm"
  admin_username= "azureuser"
  disable_password_authentication = true

  admin_ssh_key {
    username= "azureuser"
    public_key = file("~/.ssh/id_rsa.pub")
  }

  boot_diagnostics {
    storage_account_uri = azurerm_storage_account.my_storage_account.primary_blob_endpoint
  }
}
```
 
### Outputs

Get the **Resource group** name and **Public IP** to output after Terraform deployment.

Add below code to the `outputs.tf` file: 

```console
output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}

output "public_ip_address" {
  value = azurerm_linux_virtual_machine.my_terraform_vm.public_ip_address
}
```

## Terraform commands

### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. This command downloads the Azure modules required to manage your Azure resources. 

```console
terraform init
```

![image #center](https://user-images.githubusercontent.com/42368140/196460749-f9d7ea1e-fc69-4ba6-887c-da488053ef91.PNG)

### Create a Terraform execution plan

Run `terraform plan` to create and preview an execution plan before applying it to your cloud infrastructure.

```console
terraform plan -out main.tfplan
```
**Key points:**

* The **terraform plan** command is optional. You can directly run **terraform apply** command. But it is always better to check the resources about to be created.
* The terraform plan command creates an execution plan, but doesn't execute it. Instead, it determines what actions are necessary to create the configuration specified in your configuration files. This pattern allows you to verify whether the execution plan matches your expectations before making any changes to actual resources.
* The optional -out parameter allows you to specify an output file for the plan. Using the -out parameter ensures that the plan you reviewed is exactly what is applied.

### Apply a Terraform execution plan

Run `terraform apply` to apply the execution plan to your cloud infrastructure. The command below creates all required infrastructure.
```console
terraform apply main.tfplan
```

Make note of the `public_ip_address` and `resource_group_name` outputs, as shown in the image below.

These outputs will be used to verify your created resources in the Azure Portal.

![image #center](https://user-images.githubusercontent.com/67620689/227440412-c01e6f30-c32f-431b-819e-6b7e1937a0df.PNG)

### Verify created resources
On the Azure Portal, go to **Azure Dashboard** and choose **Resource group** created from Terraform. 

Verify that the Resource Group Name matches your output.

![image #center](https://user-images.githubusercontent.com/67620689/227440421-20642716-8eee-4f82-a5de-f4dd4592b65d.PNG)

Go to Azure Dashboard and choose **Virtual Machine** created from Terraform.

Verify that the Resource Group Name and Public IP Address match your output.

![image #center](https://user-images.githubusercontent.com/67620689/227440425-fe5d1685-e957-46ec-b49c-e848d211fbe3.PNG)

### Use private key to SSH into Azure VM
Connect to Azure VM using the private key(~/.ssh/id_rsa) created through `ssh-keygen`.

Use the connect command mentioned in the azure VM **GOTO >> connect** section:

![image #center](https://user-images.githubusercontent.com/67620689/227440429-f2b1249e-18eb-4db0-bce0-2eed07204fed.PNG)

Run following command to connect to VM through SSH:

```console
ssh azureuser@<Public IP>
```

![image #center](https://user-images.githubusercontent.com/67620689/227440438-90f5c9e9-ba55-486e-a874-0e5c2d7f9958.PNG)

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

It will remove all resource groups, virtual networks, and all other resources created through Terraform.

![image #center](https://user-images.githubusercontent.com/42368140/196463306-1e559148-4b9a-414c-b862-06c6aa33557e.PNG)
