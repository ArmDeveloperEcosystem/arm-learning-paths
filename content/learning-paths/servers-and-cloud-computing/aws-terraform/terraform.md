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

Any computer which has the required tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine with the required tools.

You will need an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) to complete this Learning Path. Create an account if you don't have one.

Before you begin, you will also need:
- An AWS access key ID and secret access key
- An SSH key pair

The instructions to create the keys are below.

### Generate the SSH key-pair

Generate the SSH key-pair (public key, private key) using `ssh-keygen` to use for AWS EC2 access. To generate the key-pair, follow this [guide](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

### Acquire AWS Access Credentials

The installation of Terraform on your desktop or laptop needs to communicate with AWS. Thus, Terraform needs to be able to authenticate with AWS. For authentication, generate access keys (access key ID and secret access key). These access keys are used by Terraform for making programmatic calls to AWS via the AWS CLI.

To generate and configure the Access key ID and Secret access key, follow this [guide](/install-guides/aws_access_keys).

## Create your first Terraform infrastructure (main.tf)

Terraform files are created with a  **.tf** extension. Start by creating a `main.tf` file.

### Provider

Tell `Terraform` which cloud provider to connect to, `AWS` for this example. 

Here is the basic syntax for the provider:
```console
resource "<PROVIDER>_<TYPE>" "<NAME>" {
  [CONFIG …]
}
```
Set:
  * `PROVIDER_TYPE` to `aws`
  * `NAME` optional name
   
This is how `main.tf` will look like for AWS:

```console   
      provider "aws" {
        region     = "us-east-2"
      } 
```

### Resource - "aws_instance"
Next, after defining the provider, define the resource. Resource is something to provision/start on AWS. You will provision an EC2 instance on AWS.
But before you provision the EC2 instance, you need to gather a few points -
   
1. **ami** = you need to tell Terraform which AMI(Amazon Machine Image) you are going to use. Is it going to be Ubuntu, CentOS or something else
2. **instance_type** = Also based on your need you have to choose the instance_type and it can be t4g.nano, t4g.micro, t4g.small etc.

### How to find Amazon Machine Image (AMI)

1. To find the correct AMI you need to go to **EC2** in your AWS Dashboard.
   
![alt-text #center](https://user-images.githubusercontent.com/87687468/190343196-051e752a-a61d-4a6b-80d6-25369f41e97c.png "EC2")

2. In the left Navigation you will find **Images -> AMIs**
   
![alt-text #center](https://user-images.githubusercontent.com/87687468/190343512-54fb7a3c-d048-4c23-bb66-0a0ebfb0fa80.png "AMIs")
   
3. On the search menu click on public images and then apply filters as per your requirement. e.g. `architecture=arm64`, `platform=ubuntu`.
copy the AMI ID from the search result.
   
![alt-text #center](https://user-images.githubusercontent.com/87687468/190345166-846344fe-09b8-4ab8-96b0-907b67fd0abd.png "AMI ID")

### How to find correct instance_type
You can find the correct ìnstance_type by visiting [this page](https://aws.amazon.com/ec2/instance-types/).
For a very basic instance_type not production level instance, choose **t4g.nano**

Shown below is the aws_instance configuration:
   
```console
resource "aws_instance" "ec2_example" {
  ami = "ami-02a92e06fd643c11b"  
  instance_type = "t4g.nano" 
  key_name= aws_key_pair.deployer.key_name
  vpc_security_group_ids = [aws_security_group.main.id]
}
```
 Here is a complete `main.tf` file example:
    
```console
provider "aws" {
  region     = "us-east-2"
}

resource "aws_instance" "ec2_example" {
  ami = "ami-02a92e06fd643c11b"  
  instance_type = "t4g.nano" 
  key_name= aws_key_pair.deployer.key_name
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
      cidr_blocks      = [ "0.0.0.0/0", ]
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
      cidr_blocks      = [ "0.0.0.0/0", ]
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

Run `terraform init` to initialize the Terraform deployment. This command is responsible for downloading all the dependencies which are required for the provider AWS.

```console
terraform init
```
The output from this command will look similar to:
    
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

Run `terraform plan` to create an execution plan.

```console
terraform plan
```
{{% notice Note %}}
The **terraform plan** command is optional. You can directly run **terraform apply** command. But it is always better to check the resources about to be created.
{{% /notice %}}

### Apply a Terraform execution plan

Run `terraform apply` to apply the execution plan to your cloud infrastructure. Below command creates all required infrastructure.

```console
terraform apply
```      

Answer `yes` to the prompt to confirm you want to create AWS resources.

The output should be similar to:

```output
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```
### Verify the EC2 setup

Verify the setup by going back to the AWS console.

Goto **EC2 -> instances** you should see the instance running.   
   
![alt-text #center](https://user-images.githubusercontent.com/67620689/226522634-3da95b61-5655-4c27-b5ab-913d3f731c2c.PNG "Verify")

You can also see the tag name, Terraform EC2, which was used in the Terraform script.
   
### SSH into EC2 instance

The EC2 instance is running, now connect using the private key '~/.ssh/id_rsa'.

You can find the connect command from the AWS console.

![alt-text #center](https://user-images.githubusercontent.com/67620689/226522564-67404d25-85ad-49e1-ba63-ca64725e6e51.PNG "Use private key")

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

It will remove all resource groups, virtual networks, and all other resources created through Terraform.
