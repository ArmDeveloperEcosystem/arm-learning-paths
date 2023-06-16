---
# User change
title: "Automate AWS instance creation using Terraform"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
This Learning Path uses [Terraform Cloud](https://registry.terraform.io/) to automate creation of Arm instances. Reader may wish to also see:
* [Getting Started with AWS](/learning-paths/servers-and-cloud-computing/csp/aws/)

## Before you begin

You should have the prerequisite tools installed before starting the Learning Path.

Any computer which has the required tools installed can be used for this section. The computer can be your desktop, laptop, or a virtual machine with the required tools.

You will need an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) to complete this Learning Path. Create an account if you don't have one. See the [Creating an AWS account documentation](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html) for full instructions.

Before you begin, you will also need:
- An AWS access key ID and secret access key
- An SSH key pair

The instructions to create these keys are below.

### Generate the SSH key-pair

Generate the SSH key-pair (public key, private key) using `ssh-keygen` to use for AWS EC2 access. To generate the key-pair, follow this [guide](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

### Acquire AWS Access Credentials

The installation of Terraform on your desktop or laptop needs to communicate with AWS. Thus, Terraform needs to be authenticated.

For authentication, generate access keys (access key ID and secret access key). These access keys are used by Terraform for making programmatic calls to AWS via the AWS CLI.

To generate and configure the Access key ID and Secret access key, follow this [guide](/install-guides/aws_access_keys).

## Create your first Terraform infrastructure

Terraform files are created with a  **.tf** extension. 

Start by creating a `main.tf` file in your desired directory.

```console
touch main.tf
```

### Configure your Provider

Tell `Terraform` which cloud provider to connect to, AWS for this example. Also, specify an AWS region for the connection.

Add the code below to the `main.tf` file:

```console
provider "aws" {
  region = "us-east-2"
}
```

### Configure your Resources
After defining the provider, define your resources. Resources are infrastructure objects that will be provisioned for your instance. 

Here is the basic syntax for defining a resource:

```console
resource "<PROVIDER>_<TYPE>" "<NAME>" {
  [CONFIGS …]
}
```
Where:
  * `PROVIDER` is the cloud provider name, `aws` in this case
  * `TYPE` is the type of resource to be declared
  * `NAME` is an optional, local name used to reference this resource
  * `CONFIGS` are configuration arguments, declared in a key-value format

For additional information on resource blocks and their syntax, see the [Terraform Documentation](https://developer.hashicorp.com/terraform/language/resources/syntax).

### Defining the "aws_instance" Resource
You will provision an AWS EC2 instance resource, which requires you to find and declare the following configuration arguments:
   
1. **ami** = choose an [AMI (Amazon Machine Image)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) based on your needs (e.g., Ubuntu, CentOS, Red Hat) 
2. **instance_type** = choose an Arm-based [Instance Type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) based on your needs (e.g., t4g.nano, t4g.micro, t4g.small). 

### Find an Amazon Machine Image (AMI)

1. Navigate to the **EC2 Dashboard**, either by searching (`Alt+S`) for `EC2`, or via **Services** > **Compute** > **EC2**.

![alt-text #center](https://user-images.githubusercontent.com/97123064/246459829-1ecc75fd-a916-4018-87cf-2f804836aaee.png "Navigate to the EC2 Dashboard")

2. On the left menu bar, you will find the **AMI Catalog** from the **Images** pull-down.
   
![alt-text #center](https://user-images.githubusercontent.com/97123064/246462379-6401d990-0a8d-48de-a909-af49e8453d1c.png "Navigate to the AMI Catalog")
   
3. Choose an AMI that suits your compute needs by selecting an AMI category (**Quickstart AMIs**, **AWS Marketplace AMIs**, etc.) and utilizing the filters and search options. 

    For now, find a Ubuntu AMI (e.g., `Ubuntu Server 22.04 LTS`) from **Quickstart AMIs**. Be sure to filter by **64-bit (Arm)** Architecture.

    Copy or make note of the **AMI ID** for 64-bit (Arm), as it will be used for your `ami` argument.
   
![alt-text #center](https://user-images.githubusercontent.com/97123064/246468548-d4438768-127b-48ae-8a5d-167c386dd87e.png "Copy an Arm-based, Ubuntu AMI ID")

### Find an Instance Type
A list of all AWS instance types can be [viewed here](https://aws.amazon.com/ec2/instance-types/). As a general rule, instances with a `g` at the end of their name (e.g., `M7g`, `M6g`, `T4g`) are Arm-based [Graviton](https://aws.amazon.com/ec2/graviton/) instances.

For now, select the **T4g** tab to view a list of Amazon EC2 T4g instance sizes.

![alt-text #center](https://user-images.githubusercontent.com/97123064/245550408-0362bd27-b0e4-411b-87d9-09c572089243.png "Select 'T4g' under General Purpose instances")

For now, use a small, non-production level instance size, such as **t4g.nano**. Copy or make note of this **Instance Size** name, as it will be used for your `instance_type` argument.

![alt-text #center](https://user-images.githubusercontent.com/97123064/245565342-76176f11-6c9e-4f9e-af62-0b5da2798a5e.png "Make note of the instance type name under 'Instance Size`")

### Set your Resource Block Arguments

Shown below is the `aws_instance` resource block configuration using the arguments found above:
   
```console
resource "aws_instance" "ec2_example" {
  ami           = "ami-0a0c8eebcdd6dcbd0"
  instance_type = "t4g.nano"
}
```

### A complete **main.tf** file

To complete the `main.tf` file, we will need to include additional arguments to the `aws_instance` resource and define additional resources.

Shown below is an example of a complete `main.tf` file:
    
```console
provider "aws" {
  region = "us-east-2"
}

resource "aws_instance" "ec2_example" {
  ami                    = "ami-0a0c8eebcdd6dcbd0"
  instance_type          = "t4g.nano"
  key_name               = aws_key_pair.deployer.key_name
  vpc_security_group_ids = [aws_security_group.main.id]

  provisioner "remote-exec" {
    inline = [
      "touch hello.txt",
      "echo helloworld remote provisioner >> hello.txt",
    ]
  }

  provisioner "local-exec" {
    command = "echo ${self.private_ip} >> private_ips.txt && echo ${self.public_ip} >> public_ips.txt && echo ${self.public_dns} >> public_ips.txt"
  }

  connection {
    type        = "ssh"
    host        = self.public_ip
    user        = "ubuntu"
    private_key = file("~/.ssh/id_rsa")
    timeout     = "4m"
  }
}

resource "aws_security_group" "main" {
  egress = [
    {
      cidr_blocks      = ["0.0.0.0/0", ]
      description      = ""
      from_port        = 0
      ipv6_cidr_blocks = []
      prefix_list_ids  = []
      protocol         = "-1"
      security_groups  = []
      self             = false
      to_port          = 0
    }
  ]

  ingress = [
    {
      cidr_blocks      = ["0.0.0.0/0", ]
      description      = ""
      from_port        = 22
      ipv6_cidr_blocks = []
      prefix_list_ids  = []
      protocol         = "tcp"
      security_groups  = []
      self             = false
      to_port          = 22
    }
  ]
}

resource "aws_key_pair" "deployer" {
  key_name   = "id_rsa"
  public_key = file("~/.ssh/id_rsa.pub")
}
```

## Terraform commands
    
### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. This command is responsible for downloading all required dependencies for the provider AWS.

```console
terraform init
```

The output should be similar to what is shown below:
    
```output
Initializing the backend...
Initializing provider plugins...
- Reusing previous version of hashicorp/local from the dependency lock file
- Reusing previous version of hashicorp/aws from the dependency lock file
- Using previously-installed hashicorp/local v2.3.0
- Using previously-installed hashicorp/aws v4.52.0
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

A long output of resources to be created will be printed. The bottom of the output should be similar to:

```output
Plan: 1 to add, 0 to change, 0 to destroy.

────────────────────────────────────────────────────────────────────────────────────────────────

Saved the plan to: main.tfplan
```

{{% notice Note %}}
The **terraform plan** command is optional. You can directly run the **terraform apply** command, but it is always better to confirm the resources that will be created.
{{% /notice %}}

### Apply a Terraform execution plan

Run `terraform apply` to apply the execution plan to your cloud infrastructure. The command below creates all required infrastructure.

```console
terraform apply main.tfplan
```      

If prompted to confirm if you want to create AWS resources, answer `yes`.

The output should be similar to:

```output
aws_instance.ec2_example: Creation complete after 31s [id=i-000a33ed1fe30b5df]

Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

Make note of the instance `id` (e.g., `i-000a33ed1fe30b5df`) to identify your instance. This is particularly useful when having multiple instances.

### Verify the EC2 setup

Verify the instance setup on the AWS Console.

Go to **EC2 -> Instances** and you should see an instance with the same **Instance ID** as your output `id` above. Its **Instance state** should be `Running`.

Click on the **Instance ID** to display the **Instance Summary** view which includes more details about your instance. 
   
![alt-text #center](https://user-images.githubusercontent.com/67620689/226522634-3da95b61-5655-4c27-b5ab-913d3f731c2c.PNG "Locate your instance on the AWS Console")
   
### SSH into EC2 instance

Connect to your EC2 Instance with your preferred SSH client. You will be using the private key created through [ssh-keygen](/install-guides/ssh#ssh-keys), located at `~/.ssh/id_rsa`.

In the `Instance summary` view, click `Connect`, and select the `SSH client` tab to see the commands used to launch the native SSH client.

![alt-text #center](https://user-images.githubusercontent.com/67620689/226522564-67404d25-85ad-49e1-ba63-ca64725e6e51.PNG "Connect to the EC2 instance with an SSH client")

For example, if using a `ubuntu` AMI:

```console
ssh -i <private_key> ubuntu@<public_ip_address>
```

{{% notice Note %}}
Replace `<private_key>` with your private key on your local machine and `<public_ip_address>` with the public IP of the target VM.
{{% /notice %}}

Terminal applications such as [PuTTY](https://www.putty.org/), [MobaXterm](https://mobaxterm.mobatek.net/) and similar can be used.

Different Linux distributions have different default usernames you can use to connect. 

[Default usernames](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connection-prereqs.html) for AMIs are listed in a table. Find your operating system and see the default username you should use to connect.

Once connected, you are now ready to use your instance.

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

It will remove all resource groups, virtual networks, and all other resources created through Terraform.

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
