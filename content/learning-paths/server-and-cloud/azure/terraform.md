---
# User change
title: "Automate virtual machine creation with Terraform"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Deploy a Arm based virtual machine using Terraform.

## Prerequisites

* An Azure portal account
* An [installation of Terraform](https://www.terraform.io/cli/install/apt)
* An installation of [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt).

## Azure-cli installation

Follow [Azure installation steps](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt).

## Azure authentication

The installation of Terraform on your Desktop/Laptop needs to communicate with Azure. Thus, Terraform needs to be authenticated.

For authentication, we need to run `az login` which provides code to run in browser.

![image](https://user-images.githubusercontent.com/42368140/196459799-6278da9d-e91c-4dc1-b8c3-c327dfa0394b.png)

Run in browser as below:
![image](https://user-images.githubusercontent.com/42368140/196459871-9a3e1c1e-0582-4d55-838a-03e397d68ed7.png)

You will see details in command line as below after logging in browser
![image](https://user-images.githubusercontent.com/42368140/197953418-ddb9cd41-72b9-4a97-88f1-1f490644f36b.PNG)

## Generate key-pair (public key, private key) using ssh keygen

### Generate the public key and private key

Before using Terraform, first generate the key-pair (public key, private key) using ssh-keygen. Then associate both public and private keys with Arm VMs.

Generate the key pair using the following command:

```console
ssh-keygen -t rsa -b 2048
``` 

By default, the above command will generate the public as well as private key at location **$HOME/.ssh**. You can override the end destination with a custom path (for example, **/home/ubuntu/azure/** followed by key name **azure_key**).

Output when a key pair is generated:

![image](https://user-images.githubusercontent.com/42368140/196460197-587b96b5-f108-432b-85d6-9cf9976d26a1.PNG)

**Note:** Use the public key **azure_key.pub** inside the Terraform file to provision/start the Arm VMs and private key **azure_key** to connect to the virtual machine. 

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

![image](https://user-images.githubusercontent.com/42368140/196460588-3aa72ac1-5f0f-4c57-a6d7-70e81787f137.PNG)

## Terraform infrastructure
Start by creating an empty `providers.tf`, `variables.tf`, `main.tf` and `outputs.tf` files.

### Providers

Tell Terraform which cloud provider we are going to connect, Azure for this example.

Add below code in `providers.tf` file:

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

Add below code in `variables.tf` file: 

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

Add the resources required to create a virtual machine in `main.tf`.

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
    public_key = file("/home/ubuntu/azure/azure_keys.pub")
  }

  boot_diagnostics {
    storage_account_uri = azurerm_storage_account.my_storage_account.primary_blob_endpoint
  }
}
```
 
### Outputs

Add the below code in `outputs.tf` to get **Resource group** name and **Public IP**:

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

![image](https://user-images.githubusercontent.com/42368140/196460749-f9d7ea1e-fc69-4ba6-887c-da488053ef91.PNG)

### Create a Terraform execution plan

Run `terraform plan` to create an execution plan.

```console
terraform plan -out main.tfplan
```
**Key points:**

* The **terraform plan** command is optional. We can directly run **terraform apply** command. But it is always better to check the resources about to be created.
* The terraform plan command creates an execution plan, but doesn't execute it. Instead, it determines what actions are necessary to create the configuration specified in your configuration files. This pattern allows you to verify whether the execution plan matches your expectations before making any changes to actual resources.
* The optional -out parameter allows you to specify an output file for the plan. Using the -out parameter ensures that the plan you reviewed is exactly what is applied.

### Apply a Terraform execution plan

Run `terraform apply` to apply the execution plan to your cloud infrastructure. Below command creates all required infrastructure.
```console
terraform apply main.tfplan
```
![image](https://user-images.githubusercontent.com/42368140/196460956-609770ff-c263-4dd6-b8ad-03c740ec42cf.PNG)

### Verify created resources
Go to Azure Dashboard and choose **Resource group** created from Terraform.

![image](https://user-images.githubusercontent.com/42368140/196461182-bde106db-1def-4270-be53-df97b87be21b.PNG)

Go to Azure Dashboard and choose **Virtual Machine** created from Terraform.

![image](https://user-images.githubusercontent.com/42368140/196461281-d56abe30-9a4f-42e8-9533-895ef779ebf1.PNG)

### Use private key to SSH into Azure VM
Connect to Azure VM using the private key(/home/ubuntu/azure/azure_key) created through `ssh-keygen`.

Use the connect command mentioned in the azure VM **GOTO >> connect** section:

![image](https://user-images.githubusercontent.com/42368140/196461435-bf928a89-4c3f-453b-8d20-91c384e6552f.PNG)

Run following command to connect to VM through SSH:

```console
ssh -i "/home/ubuntu/azure/azure_key" azureuser@<Public IP>
```

![image](https://user-images.githubusercontent.com/42368140/196461586-4e2a93ba-2379-4d7c-b737-b0918eaa54da.PNG)

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

It will remove all resource groups, virtual networks, and all other resources created through Terraform.
![image](https://user-images.githubusercontent.com/42368140/196463306-1e559148-4b9a-414c-b862-06c6aa33557e.PNG)

