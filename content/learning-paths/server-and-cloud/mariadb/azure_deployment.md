---
# User change
title: "Install MariaDB on an Azure Arm based instance"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Install MariaDB on an Azure Arm based instance 

You can deploy MariaDB on Azure using Terraform and Ansible. 

In this topic, you will deploy MariaDB on a single Azure instance. 

If you are new to Terraform, you should look at [Automate Azure instance creation using Terraform](/learning-paths/server-and-cloud/azure-terraform/terraform/) before starting this Learning Path.

## Before you begin

Any computer which has [Terraform](/install-guides/terraform/), [Ansible](/install-guides/ansible/), and the [Azure CLI](/install-guides/azure-cli/)installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine.

You will need an [an Azure portal account](https://azure.microsoft.com/en-in/get-started/azure-portal) to complete this Learning Path. Create an account if you don't have one.

Before you begin you will also need:
- Login to Azure CLI
- An SSH key pair

The instructions to login to Azure CLI and to create the keys are below.

### Acquire Azure Access Credentials

Terraform on your local machine needs to communicate with Azure.

For Azure authentication, follow the [Azure Authentication](/install-guides/azure_login) install guide.

### Generate an SSH key-pair

Generate an SSH key-pair (public key, private key) using `ssh-keygen` to use for Arm VMs access. To generate the key-pair, follow this [
guide](/install-guides/ssh#ssh-keys).

{{% notice Note %}} 
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

## Create an Azure instance using Terraform

For Azure Arm based instance deployment, the Terraform configuration is broken into four files: `providers.tf`, `variables.tf`, `main.tf`, and `outputs.tf`.

1. Use a text editor to add the contents below to a new file named `providers.tf`

```terraform
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

2. Use a text editor to add the contents below to a new file named `variables.tf`

```terraform
variable "resource_group_location" {
  default = "eastus2"
  description = "Location of the resource group."
}

variable "resource_group_name_prefix" {
  default = "rg"
  description = "Prefix of the resource group name that's combined with a random ID so name is unique in your Azure subscription."
}
```

3. Use a text editor to add the contents below to a new file named `main.tf`

```terraform
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
  security_rule {
    name= "MariaDB"
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
    depends_on=[azurerm_linux_virtual_machine.my_terraform_vm]
    filename = "/tmp/inventory"
    content = <<EOF
[all]
ansible-target1 ansible_connection=ssh ansible_host=${azurerm_linux_virtual_machine.my_terraform_vm.public_ip_address} ansible_user=ubuntu
                EOF
}
```

The inventory file is automatically generated and does not need to be changed.

4. Use a text editor to add the contents below to a new file named `outputs.tf`.


```terraform
output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}

output "public_ip_address" {
  value = azurerm_linux_virtual_machine.my_terraform_vm.public_ip_address
}
```

The `outputs.tf` file prints the Resource group name and Public IP.

## Terraform Commands

Use Terraform to deploy MariaDB on Azure.

### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. 

This command downloads the dependencies required for Azure.

```bash
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

```bash
terraform plan
```

A long output of resources to be created will be printed. 

### Apply a Terraform execution plan

1. Run `terraform apply` to apply the execution plan and create all Azure resources. 

```bash
terraform apply
```      

2. Answer `yes` to the prompt to confirm you want to create Azure resources. 

The public IP address will be different, but the output should be similar to:

```output
Apply complete! Resources: 12 added, 0 changed, 0 destroyed.

Outputs:

public_ip_address = "20.110.185.235"
resource_group_name = "rg-tight-dove"
```

## Configure MariaDB through Ansible

You can install the MariaDB and the required dependencies using Ansible.

Use the same `playbook.yaml` file used in the topic, [Install MariaDB on a single AWS Arm based instance](/learning-paths/server-and-cloud/mariadb/ec2_deployment#configure-mariadb-through-ansible).

Use a text editor to save the `playbook.yaml` file if you don't already have it. 

### Ansible Commands

Run the playbook using the  `ansible-playbook` command:

```bash
ansible-playbook playbook.yaml -i /tmp/inventory
```

Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:

```output
PLAY [all] ******************************************************************************************************************************

TASK [Gathering Facts] ******************************************************************************************************************
The authenticity of host '20.110.185.235 (20.110.185.235)' can't be established.
ED25519 key fingerprint is SHA256:XC9CnqxdGvrGCyo19WtfBsnUyFJU8hCoIDKWxiNaAVc.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [ansible-target1]

TASK [Update the Machine and Install dependencies] **************************************************************************************
changed: [ansible-target1]

TASK [start and enable maridb service] **************************************************************************************************
ok: [ansible-target1]

TASK [Change Root Password] *************************************************************************************************************
changed: [ansible-target1]

TASK [Create database user with password and all database privileges and 'WITH GRANT OPTION'] *******************************************
changed: [ansible-target1]

TASK [MariaDB secure installation] ******************************************************************************************************
changed: [ansible-target1]

TASK [Enable remote login by changing bind-address] *************************************************************************************
changed: [ansible-target1]

RUNNING HANDLER [Restart mariadb] *******************************************************************************************************
changed: [ansible-target1]

PLAY RECAP ******************************************************************************************************************************
ansible-target1            : ok=8    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

## Connect to Database from local machine

Follow the instructions from the previous section to [connect to the database](/learning-paths/server-and-cloud/mariadb/ec2_deployment#connect-to-database-from-local-machine).

You have successfully deployed MariaDB on an Azure instance.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```bash
terraform destroy
```
