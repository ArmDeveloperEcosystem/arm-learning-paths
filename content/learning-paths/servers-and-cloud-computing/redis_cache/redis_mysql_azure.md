---
# User change
title: "Deploy Redis as a cache for MySQL on an Azure Arm based Instance"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Deploy Redis as a cache for MySQL on an Azure Arm based Instance

You can deploy Redis as a cache for MySQL on Azure using Terraform and Ansible. 

In this section, you will deploy Redis as a cache for MySQL on an Azure instance. 

If you are new to Terraform, you should look at [Automate Azure instance creation using Terraform](/learning-paths/servers-and-cloud-computing/azure-terraform/terraform/) before starting this Learning Path.

## Before you begin

You should have the prerequisite tools installed before starting the Learning Path. 

Any computer which has the required tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine with the required tools. 

You will need an [Azure portal account](https://azure.microsoft.com/en-in/get-started/azure-portal) to complete this Learning Path. Create an account if you don't have one.

Before you begin, you will also need:
- Login to the Azure CLI
- An SSH key pair

The instructions to login to the Azure CLI and create the keys are below.

### Acquire Azure Access Credentials

The installation of Terraform on your Desktop/Laptop needs to communicate with Azure. Thus, Terraform needs to be authenticated.

For Azure authentication, follow this [guide](/install-guides/azure_login).

### Generate an SSH key-pair

Generate an SSH key-pair (public key, private key) using `ssh-keygen` to use for Azure instance access. To generate the key-pair, follow this [
guide](/install-guides/ssh#ssh-keys).

{{% notice Note %}} 
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

## Create Azure instances using Terraform

For Azure Arm based instance deployment, the Terraform configuration is broken into three files: `providers.tf`, `variables.tf` and `main.tf`. Here you are creating 2 instances.

Add the following code in `providers.tf` file to configure Terraform to communicate with Azure.
    
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
Create a `variables.tf` file for describing the variables referenced in the other files with their type and a default value.

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
  address_space = ["10.1.0.0/16"]
  location = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
}

# Create subnet
resource "azurerm_subnet" "my_terraform_subnet" {
  name = "mySubnet"
  resource_group_name = azurerm_resource_group.rg.name
  virtual_network_name = azurerm_virtual_network.my_terraform_network.name
  address_prefixes = ["10.1.1.0/24"]
}

# Create Public IPs
resource "azurerm_public_ip" "my_terraform_public_ip" {
  name = "myPublicIP${format("%02d", count.index)}-test"
  count= 2
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
  security_rule {
    name= "MYSQL"
    priority= 1002
    direction= "Inbound"
    access = "Allow"
    protocol= "Tcp"
    source_port_range= "*"
    destination_port_range = "3306"
    source_address_prefix= "*"
    destination_address_prefix = "*"
  }
}

# Create network interface
resource "azurerm_network_interface" "my_terraform_nic" {
  count= 2
  name= "NIC-${format("%02d", count.index)}-test"
  location= azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  ip_configuration {
    name= "my_nic_configuration"
    subnet_id = azurerm_subnet.my_terraform_subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id= azurerm_public_ip.my_terraform_public_ip.*.id[count.index]
  }
}

# Connect the security group to the network interface
resource "azurerm_network_interface_security_group_association" "example" {
  count= 2
  network_interface_id= azurerm_network_interface.my_terraform_nic.*.id[count.index]
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
resource "azurerm_linux_virtual_machine" "MYSQL_TEST" {
  name= "MYSQL_TEST${format("%02d", count.index + 1)}"
  count= 2
  location= azurerm_resource_group.rg.location
  resource_group_name= azurerm_resource_group.rg.name
  network_interface_ids = [azurerm_network_interface.my_terraform_nic.*.id[count.index]]
  size= "Standard_D2ps_v5"

  os_disk {
    name = "myOsDisk${format("%02d", count.index + 1)}"
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
  admin_username= "ubuntu"
  disable_password_authentication = true

  admin_ssh_key {
    username= "ubuntu"
    public_key = file("~/.ssh/id_rsa.pub")
  }

  boot_diagnostics {
    storage_account_uri = azurerm_storage_account.my_storage_account.primary_blob_endpoint
  }
}
resource "local_file" "inventory" {
    depends_on=[azurerm_linux_virtual_machine.MYSQL_TEST]
    filename = "/tmp/inventory"
    content = <<EOF
[mysql1]
${azurerm_linux_virtual_machine.MYSQL_TEST[0].public_ip_address}
[mysql2]
${azurerm_linux_virtual_machine.MYSQL_TEST[1].public_ip_address}
[all:vars]
ansible_connection=ssh
ansible_user=ubuntu
                EOF
}
```
The inventory file is automatically generated and does not need to be changed.

## Terraform Commands

Use Terraform to deploy the `main.tf` file.

### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. This command downloads the dependencies required for Azure.

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

Run `terraform plan` to create an execution plan.

```console
terraform plan
```

A long output of resources to be created will be printed. 

### Apply a Terraform execution plan

Run `terraform apply` to apply the execution plan and create all Azure resources. 

```console
terraform apply
```      

Answer `yes` to the prompt to confirm you want to create Azure resources. 

The output should be similar to:

```output
Apply complete! Resources: 16 added, 0 changed, 0 destroyed.
```

## Configure MySQL through Ansible

Install MySQL and the required dependencies on both the instances.

You can use the same `playbook.yaml` file used in the section, [Deploy Redis as a cache for MySQL on an AWS Arm based Instance](/learning-paths/servers-and-cloud-computing/redis_cache/redis_mysql_aws#configure-mysql-through-ansible).

### Ansible Commands

Run the playbook using the  `ansible-playbook` command:

```console
ansible-playbook playbook.yaml -i /tmp/inventory
```

Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:

```output
PLAY [mysql1, mysql2] ********************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************
The authenticity of host '20.114.166.37 (20.114.166.37)' can't be established.
ED25519 key fingerprint is SHA256:AFYNvATg2zT/PQJ8I5Qr0JKO+3Jwq6lGYSex4/2gDKs.
This key is not known by any other names
The authenticity of host '20.114.166.67 (20.114.166.67)' can't be established.
ED25519 key fingerprint is SHA256:0gpYKMdRIHpFxaXePtYFxs+k6JSioKcVEN6CMrCJUBA.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
yes
ok: [20.114.166.37]
ok: [20.114.166.67]

TASK [Update the Machine and Install dependencies] ***************************************************************************************************************
changed: [20.114.166.37]
changed: [20.114.166.67]

TASK [start and enable mysql service] ****************************************************************************************************************************
ok: [20.114.166.67]
ok: [20.114.166.37]

TASK [Change Root Password] **************************************************************************************************************************************
changed: [20.114.166.37]
changed: [20.114.166.67]

TASK [Create database user with password and all database privileges and 'WITH GRANT OPTION'] ********************************************************************
changed: [20.114.166.37]
changed: [20.114.166.67]

TASK [Create a new database with name 'arm_test1'] ***************************************************************************************************************
skipping: [20.114.166.67]
changed: [20.114.166.37]

TASK [Create a new database with name 'arm_test2'] ***************************************************************************************************************
skipping: [20.114.166.37]
changed: [20.114.166.67]

TASK [MySQL secure installation] *********************************************************************************************************************************
changed: [20.114.166.67]
changed: [20.114.166.37]

TASK [Enable remote login by changing bind-address] **************************************************************************************************************
changed: [20.114.166.67]
changed: [20.114.166.37]

RUNNING HANDLER [Restart mysql] **********************************************************************************************************************************
changed: [20.114.166.67]
changed: [20.114.166.37]

PLAY RECAP *******************************************************************************************************************************************************
20.114.166.37              : ok=9    changed=7    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
20.114.166.67              : ok=9    changed=7    unreachable=0    failed=0    skipped=1    rescued=0    ignored=0
```

## Connect to Database from local machine

Follow the instructions given in this [documentation](/learning-paths/servers-and-cloud-computing/redis_cache/redis_mysql_aws#connect-to-database-from-local-machine) to connect to the database from local machine.

## Deploy Redis as a cache for MySQL using Python

Follow the instructions given in this [documentation](/learning-paths/servers-and-cloud-computing/redis_cache/redis_mysql_aws#deploy-redis-as-a-cache-for-mysql-using-python) to deploy Redis as a cache for MySQL using Python.

You have successfully deployed Redis as a cache for MySQL on an Azure Arm based Instance.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

Continue the Learning Path to deploy Redis as a cache for MySQL on a GCP Arm based Instance.
