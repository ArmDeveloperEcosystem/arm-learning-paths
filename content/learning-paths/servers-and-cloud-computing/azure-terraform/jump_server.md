---
# User change
title: "Deploy Arm VMs on Azure and provide access via Jump Server"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Introduction to Jump Server

A Jump Server (also known as a bastion host) is an intermediary device responsible for funneling traffic through firewalls using a supervised secure channel. By creating a barrier between networks, jump servers create an added layer of security against outsiders wanting to maliciously access sensitive company data. Only those with the right credentials can log into a jump server and obtain authorization to proceed to a different security zone.

{{% notice Note %}}
An alternative to setting up a Jump server like below is to use [Azure Bastion](https://learn.microsoft.com/en-us/azure/bastion/bastion-overview).
{{% /notice %}}

## Deploying Arm VMs on Azure and providing access via Jump Server

For deploying Arm VMs on Azure and providing access via Jump Server, the Terraform configuration is broken into 4 files: `main.tf`, `variables.tf`, `outputs.tf` and `providers.tf`.
It creates an instance with OS Login configured to use as a bastion host and a private instance to use alongside the bastion host.

### Providers

Tell Terraform which cloud provider to connect to, Azure for this example.

Using a file editor of your choice, add the code below to a file named `providers.tf`:

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

### Create required resources

Add the code shown below in a file named `main.tf` to create the required resources and VM:

```console
# Create a resource group if it doesn’t exist.
resource "azurerm_resource_group" "resource_group" {
  name     = "${var.resource_prefix}-rg"
  location = "${var.location}"

}

# Create virtual network with public and private subnets.
resource "azurerm_virtual_network" "vnet" {
  name                = "${var.resource_prefix}-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = "${var.location}"
  resource_group_name = "${azurerm_resource_group.resource_group.name}"

}

# Create public subnet for hosting bastion/public VMs.
resource "azurerm_subnet" "public_subnet" {
  name                      = "${var.resource_prefix}-pblc-sn001"
  resource_group_name       = "${azurerm_resource_group.resource_group.name}"
  virtual_network_name      = "${azurerm_virtual_network.vnet.name}"
  address_prefixes          = ["10.0.1.0/24"]

}

# Create network security group and SSH rule for public subnet.
resource "azurerm_network_security_group" "public_nsg" {
  name                = "${var.resource_prefix}-pblc-nsg"
  location            = "${var.location}"
  resource_group_name = "${azurerm_resource_group.resource_group.name}"

  # Allow SSH traffic in from Internet to public subnet.
  security_rule {
    name                       = "allow-ssh-all"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

}

# Associate network security group with public subnet.
resource "azurerm_subnet_network_security_group_association" "public_subnet_assoc" {
  subnet_id                 = "${azurerm_subnet.public_subnet.id}"
  network_security_group_id = "${azurerm_network_security_group.public_nsg.id}"
}

# Create a public IP address for bastion host VM in public subnet.
resource "azurerm_public_ip" "public_ip" {
  name                = "${var.resource_prefix}-ip"
  location            = "${var.location}"
  resource_group_name = "${azurerm_resource_group.resource_group.name}"
  allocation_method   = "Dynamic"

}

# Create network interface for bastion host VM in public subnet.
resource "azurerm_network_interface" "bastion_nic" {
  name                      = "${var.resource_prefix}-bstn-nic"
  location                  = "${var.location}"
  resource_group_name       = "${azurerm_resource_group.resource_group.name}"

  ip_configuration {
    name                          = "${var.resource_prefix}-bstn-nic-cfg"
    subnet_id                     = "${azurerm_subnet.public_subnet.id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = "${azurerm_public_ip.public_ip.id}"
  }

}

# Create private subnet for hosting target VMs.
resource "azurerm_subnet" "private_subnet" {
  name                      = "${var.resource_prefix}-prvt-sn001"
  resource_group_name       = "${azurerm_resource_group.resource_group.name}"
  virtual_network_name      = "${azurerm_virtual_network.vnet.name}"
  address_prefixes          = ["10.0.2.0/24"]

}

# Create network security group and SSH rule for private subnet.
resource "azurerm_network_security_group" "private_nsg" {
  name                = "${var.resource_prefix}-prvt-nsg"
  location            = "${var.location}"
  resource_group_name = "${azurerm_resource_group.resource_group.name}"

  # Allow SSH traffic in from public subnet to private subnet.
  security_rule {
    name                       = "allow-ssh-public-subnet"
    priority                   = 100
    direction                  = "Inbound"
    access                     = "Allow"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "22"
    source_address_prefix      = "10.0.1.0/24"
    destination_address_prefix = "*"
  }

  # Block all outbound traffic from private subnet to Internet.
  security_rule {
    name                       = "deny-internet-all"
    priority                   = 200
    direction                  = "Outbound"
    access                     = "Deny"
    protocol                   = "Tcp"
    source_port_range          = "*"
    destination_port_range     = "*"
    source_address_prefix      = "*"
    destination_address_prefix = "*"
  }

}

# Associate network security group with private subnet.
resource "azurerm_subnet_network_security_group_association" "private_subnet_assoc" {
  subnet_id                 = "${azurerm_subnet.private_subnet.id}"
  network_security_group_id = "${azurerm_network_security_group.private_nsg.id}"
}

# Create network interface for target host VM in private subnet.
resource "azurerm_network_interface" "target_nic" {
  name                      = "${var.resource_prefix}-trgt-nic"
  location                  = "${var.location}"
  resource_group_name       = "${azurerm_resource_group.resource_group.name}"

  ip_configuration {
    name                          = "${var.resource_prefix}-trgt-nic-cfg"
    subnet_id                     = "${azurerm_subnet.private_subnet.id}"
    private_ip_address_allocation = "Dynamic"
  }

}

# Generate random text for a unique storage account name.
resource "random_id" "random_id" {
  keepers = {

    # Generate a new ID only when a new resource group is defined.
    resource_group = "${azurerm_resource_group.resource_group.name}"
  }

  byte_length = 8
}

# Create storage account for boot diagnostics.
resource "azurerm_storage_account" "storage_account" {
  name                     = "diag${random_id.random_id.hex}"
  resource_group_name      = "${azurerm_resource_group.resource_group.name}"
  location                 = "${var.location}"
  account_tier             = "Standard"
  account_replication_type = "LRS"

}

# Create bastion host VM.
resource "azurerm_linux_virtual_machine" "bastion_vm" {
  name                  = "${var.resource_prefix}-bstn-vm001"
  location              = "${var.location}"
  resource_group_name   = "${azurerm_resource_group.resource_group.name}"
  network_interface_ids = ["${azurerm_network_interface.bastion_nic.id}"]
  size               = "Standard_D2ps_v5"

  os_disk {
    name = "${var.resource_prefix}-bstn-dsk001"
    caching= "ReadWrite"
    storage_account_type = "Premium_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer = "0001-com-ubuntu-server-focal"
    sku= "20_04-lts-arm64"
    version= "20.04.202209200"
  }

  computer_name= "${var.resource_prefix}-bstn-vm001"
  admin_username= "${var.username}"
  disable_password_authentication = true

  admin_ssh_key {
    username= "${var.username}"
    public_key = file("~/.ssh/id_rsa.pub")
  }

  boot_diagnostics {
    storage_account_uri = azurerm_storage_account.storage_account.primary_blob_endpoint
  }

}

# Create target host VM.
resource "azurerm_linux_virtual_machine" "target_vm" {
  name                  = "${var.resource_prefix}-trgt-vm001"
  location              = "${var.location}"
  resource_group_name   = "${azurerm_resource_group.resource_group.name}"
  network_interface_ids = ["${azurerm_network_interface.target_nic.id}"]
  size               = "Standard_D2ps_v5"

  os_disk {
    name = "${var.resource_prefix}-trgt-dsk001"
    caching= "ReadWrite"
    storage_account_type = "Premium_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer = "0001-com-ubuntu-server-focal"
    sku= "20_04-lts-arm64"
    version= "20.04.202209200"
  }

  computer_name= "${var.resource_prefix}-trgt-vm001"
  admin_username= "${var.username}"
  disable_password_authentication = true

  admin_ssh_key {
    username= "${var.username}"
    public_key = file("~/.ssh/id_rsa.pub")
  }

  boot_diagnostics {
    storage_account_uri = azurerm_storage_account.storage_account.primary_blob_endpoint
  }

}
```
 
### Variables

To define the variables required to create a virtual machine, add the code below in a file named `variables.tf`: 

```console
# Define prefix for consistent resource naming.
variable "resource_prefix" {
  default     = "bastion-test"
  description = "Service prefix to use for naming of resources."
}

# Define Azure region for resource placement.
variable "location" {
  default     = "eastus2"
  description = "Azure region for deployment of resources."
}

# Define username for use on the hosts.
variable "username" {
  default     = "ubuntu"
  description = "Username to build and use on the VM hosts."
}
```

### Outputs

Add the code below in `outputs.tf` to get the **Private IP addresses** name and **Public IP Address of bastion VM**:

```console
# IP address of public IP addresses provisioned for bastion VM.
output "public_ip_addresses" {
  description = "IP address of public IP addresses provisioned for bastion VM."
  value       = azurerm_linux_virtual_machine.bastion_vm.public_ip_address
}

# IP addresses of private IP addresses provisioned.
output "private_ip_addresses" {
  description = "IP addresses of private IP addresses provisioned."
  value       = "${concat(azurerm_network_interface.bastion_nic.*.private_ip_address, azurerm_network_interface.target_nic.*.private_ip_address)}"
}
```

## Deploy Virtual Machines

To deploy the VMs, you need to initialize Terraform, generate an execution plan and apply the execution plan to your cloud infrastructure. Follow this [section of the learning path](/learning-paths/servers-and-cloud-computing/azure-terraform/terraform#terraform-commands) to deploy the `main.tf` file.

### Verify the Instance and Bastion Host setup

In the Azure Portal, go to the [Virtual Machines page](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Compute%2FVirtualMachines). The instances created through Terraform will be displayed on the screen.

![azure_vm #center](https://user-images.githubusercontent.com/42368140/230090582-49331e8f-7afb-45ed-ae12-8d49da0dde34.png)

### Use Jump Host to access the Private Instance

Connect to a target server via a Jump Host using the `-J` flag from the command line. This tells SSH to make a connection to the jump host and then establish a TCP forwarding to the target server:
```console
  ssh -J ubuntu@bastion-vm-public-IP ubuntu@target-vm-private-IP
```

![azure_connect_vm #center](https://user-images.githubusercontent.com/42368140/230090899-246a5391-a504-47a7-9ae7-5a3826c25ebe.png)

{{% notice Note %}}
Replace **bastion-vm-public-IP** with the public IP of the bastion VM and **target-vm-private-IP** with the private IP of the target VM.
{{% /notice %}}

### Clean up resources
Run `terraform destroy` to delete all resources created:
```console
  terraform destroy
```

![azure_terraform_destroy #center](https://user-images.githubusercontent.com/42368140/230092816-e2db8e58-b1ec-4d85-b3d4-012ce3e5385a.png)
