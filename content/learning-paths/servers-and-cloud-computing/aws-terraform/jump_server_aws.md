---
# User change
title: "Deploy Arm instances on AWS and provide access via Jump Server"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Introduction to Jump Server

A Jump Server (also known as a bastion host) is an intermediary device responsible for funneling traffic through firewalls using a supervised secure channel. By creating a barrier between networks, jump servers create an added layer of security against outsiders wanting to maliciously access sensitive company data. Only those with the right credentials can log into a jump server and obtain authorization to proceed to a different security zone.

## Deploying Arm instances on AWS and providing access via Jump Server

For deploying Arm instances on AWS and providing access via Jump Server, the Terraform configuration can be broken down into six files: `variables.tf`, `provider.tf`, `VPC_subnet_IG_RT.tf`, `security_groups.tf`, `ec2.tf` and `outputs.tf`.

Once configured, it creates an instance with OS Login configured to use as a bastion host and a private instance to use alongside the bastion host.

Start by creating these files in your desired directory.

```console
touch variables.tf provider.tf VPC_subnet_IG_RT.tf security_groups.tf ec2.tf outputs.tf
```

### Variables

`variables.tf` configures the **region**, **ami**, **instance type**, **disk size**, and **IP range** for both the private server and jump server.

Add the code below to the `variables.tf` file:

```console
variable "region" {
  description = "The AWS region to create resources in."
  default     = "us-east-1"
}

variable "ubuntu-ami" {
  description = "Ubuntu 22.04 AMI image"
  default     = "ami-0f69dd1d0d03ad669" // Ubuntu ARM64 Image
  nullable    = false
}

// Bastion Server Credentials

variable "bastionhost-instance-type" {
  description = "Instance Type of bastion/Jump server"
  default     = "t4g.small"
}

variable "bastionhost-disk-size" {
  description = "Root disk size of bastion/Jump server"
  default     = 8
}

variable "jump-server-IP-Range" {
  default = "0.0.0.0/0"
}

// Private Server Credentials

variable "instance-type-1" {
  description = "Instance Type of private server"
  default     = "t4g.small"
}

variable "disk-size-1" {
  description = "Root disk size of private server"
  default     = 40
}
```

### Provider

`provider.tf` contains a `region` variable that controls where to deploy the instances.

Add the code below to the `provider.tf` file:

```console
provider "aws" {
  region = var.region
}
```

### Main Resources

`VPC_subnet_IG_RT.tf` contains the following several resources. For more information about these resources, see the [Amazon VPC Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/how-it-works.html).

  1. [Virtual Private Cloud (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
  2. [Subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)
  3. [Internet Gateway (IG)](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
  4. [Route Table (RT)](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html)
  5. [Network Address Translation (NAT) gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)

Specifically, we will have a Virtual Private Cloud (VPC) with a CIDR block size of /16. In that VPC, we will have the following two subnets with a CIDR block size of /24 each:

  1.  Public Subnet (for Jump Server access, accessible from Public World)
  2.  Private Subnet (for Private Server access, restricted from Public World)

Then, we will have a Route Table for the Internet Gateway so that instance can connect to the outside world, update it, and associate it with the private subnet. 

Finally, create a Network Address Translation gateway to connect your VPC/Network to the internet and attach this gateway to your VPC in the public network.

Add the code below to the `VPC_subnet_IG_RT.tf` file:

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
  destination_cidr_block = "0.0.0.0/0"
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
  depends_on    = [aws_eip.jump-eip]
  allocation_id = aws_eip.jump-eip.id
  subnet_id     = aws_subnet.Public_Subnet.id

  tags = {
    Name = "NAT_Gateway"
  }
}

// Route table for SNAT in private subnet

resource "aws_route_table" "private_subnet_route_table" {
  depends_on = [aws_nat_gateway.eip]
  vpc_id     = aws_vpc.Demo_VPC.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_nat_gateway.eip.id
  }
  
  tags = {
    Name = "private_subnet_route_table"
  }
}

resource "aws_route_table_association" "private_subnet_route_table_association" {
  depends_on     = [aws_route_table.private_subnet_route_table]
  subnet_id      = aws_subnet.Private_Subnet.id
  route_table_id = aws_route_table.private_subnet_route_table.id
}
```
### Security Groups
		
`security_groups.tf` creates two security groups, one for the Bastion Host and one for the Private Instance, in order to allow SSH access from this Bastion Host.

Add the code below to the `security_groups.tf` file:

```console
resource "aws_security_group" "only_ssh_bastion" {
  depends_on = [aws_subnet.Public_Subnet]
  name       = "only_ssh_bastion"
  vpc_id     = aws_vpc.Demo_VPC.id

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
  depends_on  = [aws_subnet.Public_Subnet]
  name        = "only_ssh_private_instance"
  description = "allow ssh bastion inbound traffic"
  vpc_id      = aws_vpc.Demo_VPC.id

  ingress {
    description     = "Only ssh_sql_bastion in public subnet"
    from_port       = 22
    to_port         = 22
    protocol        = "tcp"
    security_groups = [aws_security_group.only_ssh_bastion.id]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
  
  tags = {
    Name = "only_ssh_sql_bastion"
  }
}
```

### AWS EC2 Instance Resources

`ec2.tf` creates a Bastion/Jump server and a Private Instance.

Add the code below to the `ec2.tf` file:

```console
// Bastion/Jump server

resource "aws_instance" "BASTION" {
  ami                    = var.ubuntu-ami
  instance_type          = var.bastionhost-instance-type
  subnet_id              = aws_subnet.Public_Subnet.id
  vpc_security_group_ids = [aws_security_group.only_ssh_bastion.id]
  key_name               = aws_key_pair.deployer.key_name

  root_block_device {
    volume_size           = var.bastionhost-disk-size
    volume_type           = "gp2"
    encrypted             = true
    delete_on_termination = true
  }

  tags = {
    Name = "bastion-host"
  }
}

// Private instance

resource "aws_instance" "ec2" {
  ami                    = var.ubuntu-ami
  instance_type          = var.instance-type-1
  subnet_id              = aws_subnet.Private_Subnet.id
  vpc_security_group_ids = [aws_security_group.only_ssh_private_instance.id]
  key_name               = aws_key_pair.deployer.key_name

  root_block_device {
    volume_size           = var.disk-size-1
    volume_type           = "gp2"
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

### Outputs

`outputs.tf` defines the output values for this configuration.

Add the code below to the `outputs.tf` file:

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

```output
Initializing the backend...

Initializing provider plugins...

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
terraform plan -out main.tfplan
```

A long output of resources to be created will be printed. The bottom of the output should be similar to:

```output
Plan: 19 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + EC2-private_ip        = (known after apply)
  + EC2-public_ip         = (known after apply)
  + bastionhost-public-ip = (known after apply)

────────────────────────────────────────────────────────────────────────────────────────────────

Saved the plan to: main.tfplan
```

### Apply a Terraform execution plan
Run `terraform apply` to apply the execution plan to your cloud infrastructure. The command below creates all required infrastructure.

```console
terraform apply main.tfplan
```

If prompted to confirm if you want to create AWS resources, answer `yes`.

The bottom of the output should be similar to what is shown below:

```output
Apply complete! Resources: 19 added, 0 changed, 0 destroyed

outputs:

EC2-private_ip = "10.1.2.76"
EC2-public_ip = "54.221.51.159"
bastionhost-public_ip = "54.152.41.75"
```

Make note of the outputs to identify your instances. This is particularly useful when having multiple instances.

### Verify the Instance and Bastion Host setup
Verify the instances setup on the AWS Console.

Go to **EC2 -> instances** you should see the following two instances running:

  1. An instance named **terraform** with the **Public** and **Private IPv4 addresses** matching your `EC2-public_ip` and `EC2-private_ip` outputs above.
  2. An instance named **bastion** with the **Public IPv4 address** matching your `bastionhost-public_ip` output above.

Click on the **Instance ID**s to display the **Instance Summary** view which includes more details about your instances. 

![alt-text #center](https://user-images.githubusercontent.com/71631645/203951115-5a8f8ac1-e415-4e82-bb3d-aae65c1f3c65.png "Locate your instances on the AWS Console")
   
### Use Jump Host to access the Private Instance
Connect to a target server via a Jump Host using the `-J` flag from the command line. This tells SSH to make a connection to the jump host and then establish a TCP forwarding to the target server from there. For example, if using a `ubuntu` AMI:

```console
ssh -J ubuntu@<jump-host-IP> ubuntu@<target-server-IP>
```

{{% notice Note %}}
Replace `<jump-host-IP>` with the public IP of the bastion VM and `<target-server-IP>` with the private IP of the target VM.
{{% /notice %}}

Terminal applications such as [PuTTY](https://www.putty.org/), [MobaXterm](https://mobaxterm.mobatek.net/) and similar can be used.

Different Linux distributions have different default usernames you can use to connect. 

[Default usernames](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connection-prereqs.html) for AMIs are listed in a table. Find your operating system and see the default username you should use to connect.

The output is shown below. Once connected, you are now ready to use your instance.

```output
ubuntu@ip-172-31-46-24:~/ $ ssh -J ubuntu@54.205.132.186 ubuntu@10.1.2.76
The authenticity of host '54.205.132.186 (54.205.132.186)' can't be established.
ED25519 key fingerprint is SHA256:LEP11QPanpvagrBEfz71C5111gUQjAUTtzIF8ovAdzT.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '54.205.132.186' (ED25519) to the list of known hosts.
The authenticity of host '10.1.2.76 (<no hostip for proxy command>)' can't be established.
ED25519 key fingerprint is SHA256:4FsZ5txilwvvrbaIkvdxJuznb6dKQiN2FSyd7/I/EtQ.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.1.2.76' (ED25519) to the list of known hosts.
Welcome to Ubuntu 22.04.1 LTS (GNU/Linux 5.15.0-1019-aws aarch64)
```

### Clean up resources
Run `terraform destroy` to delete all resources created through Terraform, including resource groups, virtual networks, and all other resources.

```console
terraform destroy
```

A long output of resources to destroy will be printed. If prompted to confirm if you want to destroy all resources, answer `yes`.

The bottom of the output should be similar to:

```output
Destroy complete! Resources: 19 destroyed.
```

## Explore your instance

### Run uname

Use the [uname](https://en.wikipedia.org/wiki/Uname) utility to verify that you are using an Arm-based server. For example:

```console
uname -m
```
will identify the host machine as `aarch64`.

### Run hello world

Install the `gcc` compiler. If you are using `Ubuntu`, use the following commands. If not, refer to the [GNU compiler install guide](/install-guides/gcc):

```console
sudo apt-get update
sudo apt install -y gcc
```

Using a text editor of your choice, create a file named `hello.c` with the contents below:

```C
#include <stdio.h>
int main(){
    printf("hello world\n");
    return 0;
}
```
Build and run the application:

```console
gcc hello.c -o hello
./hello
```

The output is shown below:

```output
hello world
```
