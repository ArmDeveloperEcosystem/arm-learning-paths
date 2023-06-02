---
# User change
title: "Automate Azure VM creation with Terraform"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
This Learning Path uses [Terraform Cloud](https://registry.terraform.io/) to automate instantiation of Arm instances. Reader may wish to also see:
* [Getting Started with Microsoft Azure](/learning-paths/servers-and-cloud-computing/csp/azure/)
* [Deploy a Windows on Arm virtual machine on Microsoft Azure](/learning-paths/cross-platform/woa_azure/)
     * These same instructions can be used to deploy Linux as well.

## Before you begin

You should have the prerequisite tools installed before starting the Learning Path.

Any computer which has the required tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine with the required tools.

You will need an [Azure portal account](https://azure.microsoft.com/en-in/get-started/azure-portal) to complete this Learning Path. Create an account if you don't have one.

Before you begin, you will also need:
- Login to the Azure CLI
- An SSH key pair

The instructions to login to the Azure CLI and create the keys are below.

### Generate an SSH key-pair

Generate an SSH key-pair (public key, private key) using `ssh-keygen` to use for Arm VMs access. To generate the key-pair, follow this [
guide](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

### Acquire Azure Access Credentials

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

```output
ubuntu@ip-172-31-38-39:~$ az vm image list --location eastus2 --publisher Canonical --offer 0001-com-ubuntu-server-focal --sku 20_04-lts-arm64 --all --output table
Architecture    Offer                         Publisher    Sku              Urn                                                                     Version
--------------  ----------------------------  -----------  ---------------  ----------------------------------------------------------------------  ---------------
Arm64           0001-com-ubuntu-server-focal  Canonical    20_04-lts-arm64  Canonical:0001-com-ubuntu-server-focal:20_04-lts-arm64:20.04.202206150  20.04.202206150
Arm64           0001-com-ubuntu-server-focal  Canonical    20_04-lts-arm64  Canonical:0001-com-ubuntu-server-focal:20_04-lts-arm64:20.04.202206220  20.04.202206220
Arm64           0001-com-ubuntu-server-focal  Canonical    20_04-lts-arm64  Canonical:0001-com-ubuntu-server-focal:20_04-lts-arm64:20.04.202207050  20.04.202207050
Arm64           0001-com-ubuntu-server-focal  Canonical    20_04-lts-arm64  Canonical:0001-com-ubuntu-server-focal:20_04-lts-arm64:20.04.202207130  20.04.202207130
Arm64           0001-com-ubuntu-server-focal  Canonical    20_04-lts-arm64  Canonical:0001-com-ubuntu-server-focal:20_04-lts-arm64:20.04.202208100  20.04.202208100
Arm64           0001-com-ubuntu-server-focal  Canonical    20_04-lts-arm64  Canonical:0001-com-ubuntu-server-focal:20_04-lts-arm64:20.04.202209050  20.04.202209050
Arm64           0001-com-ubuntu-server-focal  Canonical    20_04-lts-arm64  Canonical:0001-com-ubuntu-server-focal:20_04-lts-arm64:20.04.202209200  20.04.202209200
Arm64           0001-com-ubuntu-server-focal  Canonical    20_04-lts-arm64  Canonical:0001-com-ubuntu-server-focal:20_04-lts-arm64:20.04.202210100  20.04.202210100
Arm64           0001-com-ubuntu-server-focal  Canonical    20_04-lts-arm64  Canonical:0001-com-ubuntu-server-focal:20_04-lts-arm64:20.04.202210140  20.04.202210140
Arm64           0001-com-ubuntu-server-focal  Canonical    20_04-lts-arm64  Canonical:0001-com-ubuntu-server-focal:20_04-lts-arm64:20.04.202210180  20.04.202210180
Arm64           0001-com-ubuntu-server-focal  Canonical    20_04-lts-arm64  Canonical:0001-com-ubuntu-server-focal:20_04-lts-arm64:20.04.202211151  20.04.202211151
```

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

The output should be similar to:

```output
Initializing the backend...
Initializing provider plugins...
- Reusing previous version of hashicorp/local from the dependency lock file
- Reusing previous version of hashicorp/tls from the dependency lock file
- Reusing previous version of hashicorp/azurerm from the dependency lock file
- Reusing previous version of hashicorp/random from the dependency lock file
- Using previously-installed hashicorp/local v2.4.0
- Using previously-installed hashicorp/tls v4.0.4
- Using previously-installed hashicorp/azurerm v2.99.0
- Using previously-installed hashicorp/random v3.4.3
Terraform has been successfully initialized!
You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.
If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

### Create a Terraform execution plan

Run `terraform plan` to create and preview an execution plan before applying it to your cloud infrastructure.

```console
terraform plan -out main.tfplan
```
A long output of resources to be created will be printed.

### Apply a Terraform execution plan

Run `terraform apply` to apply the execution plan to your cloud infrastructure. The command below creates all required infrastructure.
```console
terraform apply main.tfplan
```
```output
Apply complete! Resources: 11 added, 0 changed,0 destroyed

outputs:

public_ip_address = *20.242.3.39"
resource. group_name = *rg-definite-mole"
```

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

```output
ubuntu@ip-172-31-17-218:~$ ssh azureuser@20.242.3.39
The authenticity of host *20.242.3.39 (20.242.3.39)" can't be established.
ED25519 key fingerprint is SHA256:9HqZbneGF wsn2L JrNu70a+S50s 1xvK7aCHImSDNOCH.
This key is not known by any other names

Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '20.242.3.35' (ED25519) to the list of known hosts.
Welcome to Ubuntu 20.04.5 LTS (GNU/Linux 5.15.0-1020-azure aarch64)
```

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

It will remove all resource groups, virtual networks, and all other resources created through Terraform.
