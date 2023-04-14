---
# User change
title: "Deploy Arm instances on AWS and provide access via Jump Server"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Introduction to Jump Server

A Jump Server (also known as bastion host) is an intermediary device responsible for funnelling traffic through firewalls using a supervised secure channel. By creating a barrier between networks, jump servers create an added layer of security against outsiders wanting to maliciously access sensitive company data. Only those with the right credentials can log into a jump server and obtain authorization to proceed to a different security zone.

## Deploying Arm instances on AWS and providing access via Jump Server

For deploying Arm instances on AWS and providing access via Jump Server, the Terraform configuration is broken into 7 files: `ec2.tf`, `outputs.tf`, `provider.tf`, `security_groups.tf`, `variables.tf` and `VPC_subnet_IG_RT.tf`

`variable.tf` configures the region, ami, instance type, disk size, and IP range.

```console
	variable "region" {
		description = "The AWS region to create resources in."
		default = "us-east-1"
	}


	variable "ubuntu-ami" {
		description = "Ubuntu 22.04  AMI image"
		default = "ami-0f69dd1d0d03ad669"    // Ubuntu ARM64 Image
		nullable= false
	}

	// Bastion Server Credentials 

	variable "bastionhost-instance-type" {
		description = "Instance Type of bastion/Jump server"
		default = "t4g.small"
	}

	variable "bastionhost-disk-size" {
		description = "Root disk size of bastion/Jump server"
		default = 8
	}


	variable "jump-server-IP-Range" {
	  default= "0.0.0.0/0"
	}

	// Private Server Credentials 

	variable "instance-type-1" {
		description = "Instance Type of private server"
		default = "t4g.small"
	}

	variable "disk-size-1" {
		description = "Root disk size of private server"
		default = 40
	}
```

`provider.tf` contains a region variable that controls where to deploy the instances.

```console
provider "aws" {
        region = "${var.region}"
}
```

`VPC_subnet_IG_RT.tf` writes an infrastructure as code, which automatically creates a VPC with a CIDR block size of /16.
In that VPC, we have to create 2 subnets with a CIDR block size of /24 each:
  1.  Public Subnet (Accessible for Public World)
  2.  Private Subnet (Restricted for Public World)

Then create a routing table for the Internet gateway so that instance can connect to the outside world, update it, and associate it with the private subnet. Create a NAT gateway to connect our VPC/Network to the internet and attach this gateway to our VPC in the public network.
```console
		// VPC creation
		resource "aws_vpc" "Demo_VPC" {
			cidr_block           = "10.1.0.0/16"
			instance_tenancy     = "default"
			enable_dns_support   = "true"
			enable_dns_hostnames = "true"
		 
			tags = {
				Name = "VPC"
			}
		}
		// Subnet creation 
		resource "aws_subnet" "Public_Subnet" {
			vpc_id                  = aws_vpc.Demo_VPC.id
			cidr_block              = "10.1.1.0/24"
			map_public_ip_on_launch = "true"
			availability_zone       = "us-east-1a"
			tags = {
			  Name = "Jump Public Subnet"
			}
		}

		resource "aws_subnet" "Private_Subnet" {
			vpc_id                  = aws_vpc.Demo_VPC.id
			map_public_ip_on_launch = "true"
			cidr_block              = "10.1.2.0/24"
			availability_zone       = "us-east-1b"
			tags = {
			  Name = "Private Subnet"
			}
		}  

	resource "aws_internet_gateway" "IGW" {
		vpc_id = aws_vpc.Demo_VPC.id
		tags = {
				Name = "VPC Internet Gateway"
		}
	}


	resource "aws_route_table" "Route_table" {
		vpc_id = aws_vpc.Demo_VPC.id
		tags = {
				Name = "VPC Route Table"
		}
	}

	resource "aws_route" "VPC_internet_access" {
		route_table_id         = aws_route_table.Route_table.id
		destination_cidr_block =  "0.0.0.0/0"
		gateway_id             = aws_internet_gateway.IGW.id
	}

	resource "aws_route_table_association" "VPC_association" {
		subnet_id      = aws_subnet.Public_Subnet.id
		route_table_id = aws_route_table.Route_table.id
	}

		resource "aws_eip" "jump-eip" {
			vpc              = true
			public_ipv4_pool = "amazon"
		}

	resource "aws_nat_gateway" "eip" {
		depends_on=[aws_eip.jump-eip]
		allocation_id = aws_eip.jump-eip.id
		subnet_id     = aws_subnet.Public_Subnet.id
		tags = {
			Name = "NAT_Gateway"
		  }
	}
	
	// Route table for SNAT in private subnet
	
	resource "aws_route_table" "private_subnet_route_table" {
		depends_on=[aws_nat_gateway.eip]
		vpc_id = aws_vpc.Demo_VPC.id

		route {
		  cidr_block = "0.0.0.0/0"
		  gateway_id = aws_nat_gateway.eip.id
		}

		tags = {
		  Name = "private_subnet_route_table"
		}
	}

	resource "aws_route_table_association" "private_subnet_route_table_association" {
		depends_on = [aws_route_table.private_subnet_route_table]
		subnet_id      = aws_subnet.Private_Subnet.id
		route_table_id = aws_route_table.private_subnet_route_table.id
	}
```
		
`security_groups.tf` creates two security groups, one for Bastion Host and one for Private Instance, in order to allow SSH access from this Bastion Host.
```console
	resource "aws_security_group" "only_ssh_bastion" {
		depends_on=[aws_subnet.Public_Subnet]
		name        = "only_ssh_bastion"
		vpc_id      =  aws_vpc.Demo_VPC.id

		ingress {
			from_port   = 22
			to_port     = 22
			protocol    = "tcp"
			cidr_blocks = ["${var.jump-server-IP-Range}"]
		  }

		egress {
		  from_port   = 0
		  to_port     = 0
		  protocol    = "-1"
		  cidr_blocks = ["0.0.0.0/0"]
		}

		tags = {
		  Name = "only_ssh_bastion"
		}
	}

	resource "aws_security_group" "only_ssh_private_instance" {
		depends_on=[aws_subnet.Public_Subnet]
		name        = "only_ssh_private_instance"
		description = "allow ssh bastion inbound traffic"
		vpc_id      =  aws_vpc.Demo_VPC.id

		ingress {
			description = "Only ssh_sql_bastion in public subnet"
			from_port   = 22
			to_port     = 22
			protocol    = "tcp"
			security_groups=[aws_security_group.only_ssh_bastion.id]
		
		}

		egress {
			from_port   = 0
			to_port     = 0
			protocol    = "-1"
			cidr_blocks = ["0.0.0.0/0"]
			ipv6_cidr_blocks =  ["::/0"]
		  }

		tags = {
		  Name = "only_ssh_sql_bastion"
		}
	}
```

`ec2.tf` creates a Bastion/Jump server and a Private Instance.
```console
	// Bastion/Jump server
	
	resource "aws_instance" "BASTION" {
		ami           = "${var.ubuntu-ami}"
		instance_type = "${var.bastionhost-instance-type}"
		subnet_id = aws_subnet.Public_Subnet.id
		vpc_security_group_ids = [ aws_security_group.only_ssh_bastion.id ]
		key_name = aws_key_pair.deployer.key_name

		root_block_device {
			volume_size = "${var.bastionhost-disk-size}"
			volume_type = "gp2"
			encrypted             = true
			delete_on_termination = true
			}

		tags = {
			Name = "bastion-host"
			}
	}

	// Private instance

	resource "aws_instance" "ec2" {
		ami           = "${var.ubuntu-ami}"
		instance_type = "${var.instance-type-1}"
		subnet_id = aws_subnet.Private_Subnet.id
		vpc_security_group_ids = [ aws_security_group.only_ssh_private_instance.id]
		key_name = aws_key_pair.deployer.key_name

		root_block_device {
			volume_size = "${var.disk-size-1}"
			volume_type = "gp2"
			encrypted             = true
			delete_on_termination = true
			}

		tags = {
			Name = "terraform"
			}
	}
        resource "aws_key_pair" "deployer" {
               key_name   = "id_rsa"
               public_key = file("~/.ssh/id_rsa.pub")
        }
```

`outputs.tf` defines the output values for this configuration.
```console
output "EC2-public_ip" {
  value = aws_instance.ec2.public_ip
}

output "EC2-private_ip" {
  value = aws_instance.ec2.private_ip
}

output "bastionhost-public-ip" {
  value = aws_instance.BASTION.public_ip
}
```

## Terraform commands
    
### Initialize Terraform
Run `terraform init` to initialize the Terraform deployment. This command is responsible for downloading all the dependencies which are required for the provider AWS.
```console
  terraform init
```
The output should be similar to what is shown below:

![alt-text #center](https://user-images.githubusercontent.com/71631645/203960502-a22b68bb-c1d2-49bf-bb7c-5eee5ac6944c.jpg "Terraform init")

### Create a Terraform execution plan
Run `terraform plan` to create an execution plan.
```console
  terraform plan
```

### Apply a Terraform execution plan
Run `terraform apply` to apply the execution plan to your cloud infrastructure. Below command creates all required infrastructure.
```console
  terraform apply
```      
The output should be similar to what is shown below:

   ![alt-text #center](https://user-images.githubusercontent.com/71631645/203950999-94167eaa-6f22-45f5-9647-ef2d131e9daa.jpg "Terraform apply")

### Verify the Instance and Bastion Host setup
Let's verify the setup by going to the AWS console.
Goto **EC2 -> instances** you should see the instances running.

![alt-text #center](https://user-images.githubusercontent.com/71631645/203951115-5a8f8ac1-e415-4e82-bb3d-aae65c1f3c65.png "Verify")

You can also see the tag name - terraform and bastion-host, which we mentioned in the Terraform script.
   
### Use Jump Host to access the Private Instance
Connect to a target server via a Jump Host using the `-J` flag from the command line. This tells ssh to make a connection to the jump host and then establish a TCP forwarding to the target server, from there
```console
ssh -J username@jump-host-IP username@target-server-IP
```
The output is shown below:

![alt-text #center](https://user-images.githubusercontent.com/71631645/203960729-38f353d1-8a4e-4704-b039-04608896d114.jpg "ssh -j")

### Clean up resources
Run `terraform destroy` to delete all resources created.
```console
  terraform destroy
```
It will remove all resource groups, virtual networks, and all other resources created through Terraform.

![alt-text #center](https://user-images.githubusercontent.com/71631645/203960620-bc580385-2fd6-477d-93c3-29895eeb5290.jpg "Terraform destroy")
