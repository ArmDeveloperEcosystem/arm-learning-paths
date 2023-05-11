---
# User change
title: "Install Redis on a single Azure Arm based instance"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Install Redis on a single Azure Arm based instance 

You can deploy Redis on Azure using Terraform and Ansible. 

In this section, you will deploy Redis on a single Azure instance. 

If you are new to Terraform, you should look at [Automate Azure instance creation using Terraform](/learning-paths/servers-and-cloud-computing/azure-terraform/terraform/) before starting this Learning Path.

## Before you begin

Install [Terraform](/install-guides/terraform) and [Ansible](/install-guides/ansible) on your computer. 

Any computer which has these tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine with the required tools. 

You will need an [an Azure portal account](https://azure.microsoft.com/en-in/get-started/azure-portal) to complete this Learning Path. Create an account if you don't have one.

You will also need:
- A SSH key pair
- Azure Access Credentials to login to Azure CLI

The instructions to generate the SSH key pair and login to Azure CLI are below.

### Generate the SSH key-pair

Generate the SSH key-pair (public key, private key) using `ssh-keygen` to use for Arm VMs access. To generate the key-pair, follow this [guide](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

### Acquire Azure Access Credentials

The installation of Terraform on your Desktop/Laptop needs to communicate with Azure. Thus, Terraform needs to be authenticated.

For Azure authentication, follow this [guide](/install-guides/azure_login).

## Create an Azure instance using Terraform
For Azure Arm based instance deployment, the Terraform configuration is broken down into four files: `providers.tf`, `variables.tf`, `main.tf`, and `outputs.tf`.

Use a text editor and add the following code in `providers.tf` file to configure Terraform to communicate with Azure.

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

Use a text editor and create a `variables.tf` file with the content below. This file describes the variables referenced in the other terraform files with their type and default value.

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

Add the resources required to create a virtual machine in a file named `main.tf`.

Scroll down to see the information you need to change in `main.tf`.

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
  security_rule {
    name= "Redis-port"
    priority= 1002
    direction= "Inbound"
    access = "Allow"
    protocol= "Tcp"
    source_port_range= "*"
    destination_port_range = "6379"
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


Add the code below in `outputs.tf` to get the Resource group name and Public IP.

```console
output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}

output "public_ip_address" {
  value = azurerm_linux_virtual_machine.my_terraform_vm.public_ip_address
}
```

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

A long output of resources to be created will be printed to the console. 

### Apply a Terraform execution plan

Run `terraform apply` to apply the execution plan and create all Azure resources. 

```console
terraform apply
```      

Answer `yes` wen prompted to confirm you want to create Azure resources. 

The public IP address will be different, but the output should be similar to:

```output
Apply complete! Resources: 12 added, 0 changed, 0 destroyed.

Outputs:

public_ip_address = "20.110.186.231"
resource_group_name = "rg-tight-dove"
```

## Configure Redis through Ansible

Install Redis and the required dependencies.

You can use the same `playbook.yaml` file used in the topic, [Install Redis on a single AWS Arm based instance](/learning-paths/servers-and-cloud-computing/redis/aws_deployment#configure-redis-through-ansible).

### Ansible Commands

Substitute your private key name, and run the playbook using the  `ansible-playbook` command.

```console
ansible-playbook playbook.yaml -i /tmp/inventory
```

Answer `yes` when prompted for the SSH connection. 

Deployment may take a few minutes. 

The output should be similar to:

```output
PLAY [all] *****************************************************************************************************************************************************

TASK [Gathering Facts] *****************************************************************************************************************************************
The authenticity of host '20.110.186.231 (20.110.186.231)' can't be established.
ED25519 key fingerprint is SHA256:LHk4u86Sw5Uw7WPPvKaz7qp2mKyxn+X7Gxz1DogTL+4.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
ok: [ansible-target1]

TASK [Update the Machine and install dependencies] *************************************************************************************************************
changed: [ansible-target1]

TASK [Create directories] **************************************************************************************************************************************
changed: [ansible-target1]

TASK [Create configuration files] ******************************************************************************************************************************
changed: [ansible-target1]

TASK [Stop redis-server] ***************************************************************************************************************************************
changed: [ansible-target1]

TASK [Start redis server with configuration files] *************************************************************************************************************
changed: [ansible-target1]

TASK [Set Authentication password] *****************************************************************************************************************************
changed: [ansible-target1]

PLAY RECAP *****************************************************************************************************************************************************
ansible-target1            : ok=7    changed=6    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

```

## Connecting to the Redis server from local machine

Execute the steps below to connect to the remote Redis server from your local machine.
1. Install redis-tools to interact with redis-server:
```console
sudo apt install redis-tools
```
2. Connect to redis-server through redis-cli:
```console
redis-cli -h <public-IP-address> -p 6379
```
The output will be similar to:
```output
ubuntu@ip-172-31-38-39:~$ redis-cli -h 20.110.186.231 -p 6379
20.110.186.231:6379> 
```
3. Authorize Redis with the password set by us in playbook.yaml file.
The output from running the authorization command is shown below:
```output
20.110.186.231:6379> ping
(error) NOAUTH Authentication required.
20.110.186.231:6379> AUTH 123456789
OK
20.110.186.231:6379> ping
PONG
```
4. Try out commands in the redis-cli. Example output from some commands is shown here:
```output
20.110.186.231:6379> set name test
OK
20.110.186.231:6379> get name
"test"
20.110.186.231:6379>
```
You have successfully installed Redis on an Azure instance.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

Continue the Learning Path to deploy Redis on a single Google Cloud instance.

