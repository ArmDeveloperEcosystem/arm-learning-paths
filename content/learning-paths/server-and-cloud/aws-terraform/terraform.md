---
# User change
title: "Automate AWS EC2 instance creation using Terraform"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Deploy Graviton based EC2 instances with Terraform 

Another way to start an AWS EC2 instance is with Terraform. You can follow the steps here to automate your AWS EC2 instance creation.

## Before you begin

Any computer which has the required tools installed can be used for this section.

You will need an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start). Create an account if needed.

Two tools are required on the computer you are using. Follow the links to install the required tools.

* [Terraform](/install-guides/terraform)
* [AWS CLI](/install-guides/aws-cli)

## Generate the SSH key-pair

Generate the SSH key-pair (public key, private key) using `ssh-keygen` to use for AWS EC2 access. To generate the key-pair, follow this [documentation](/install-guides/ssh#ssh-keys).

{{% notice Note %}}
If you already have an SSH key-pair present in the `~/.ssh` directory, you can skip this step.
{{% /notice %}}

## Generate Access keys (access key ID and secret access key)

The installation of Terraform on your desktop or laptop needs to communicate with AWS. Thus, Terraform needs to be able to authenticate with AWS. For authentication, generate access keys (access key ID and secret access key). These access keys are used by Terraform for making programmatic calls to AWS via the AWS CLI.
  
### Go to My Security Credentials
   
![alt-text #center](https://user-images.githubusercontent.com/87687468/190137370-87b8ca2a-0b38-4732-80fc-3ea70c72e431.png "Security credentials")

### On Your Security Credentials page click on create access keys (access key ID and secret access key)
   
![alt-text #center](https://user-images.githubusercontent.com/87687468/190137925-c725359a-cdab-468f-8195-8cce9c1be0ae.png "Access keys")
   
### Copy the Access Key ID and Secret Access Key 

![alt-text #center](https://user-images.githubusercontent.com/87687468/190138349-7cc0007c-def1-48b7-ad1e-4ee5b97f4b90.png "Copy keys")

## Create your first Terraform infrastructure (main.tf)

Terraform files are created with a  **.tf** extension. Start by creating a `main.tf` file.

### Provider

Tell `Terraform` which cloud provider we are going to connect, `AWS` for this example. 

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
      region     = "eu-central-1"
      access_key = "XXXXXXXXXXXXXXXXXXXX"
      secret_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
      } 
```

### Resource - "aws_instance"
Next, after defining the provider, we are going to define the resource. Resource is something that we are going to provision/start on AWS. We are going to provision an EC2 instance on AWS.
But before we provision the EC2 instance, we need to gather a few points -
   
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
We can find the correct ìnstance_type by visiting [this page](https://aws.amazon.com/ec2/instance-types/).
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
  access_key = "Axxxxxxxxxxxxxxxxxxxx"
  secret_key = "JzZKiCia2vjbq4zGGGxxxxxxxxxxxxxxxxxxxxxx"
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
    
![alt-text #center](https://user-images.githubusercontent.com/87687468/190346590-e5be6def-5d6b-470a-a0cb-1057a1334cd7.png "Terraform init")

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

![alt-text #center](https://user-images.githubusercontent.com/87687468/199248572-9966e305-f502-4444-943d-7eb0ba0ee9ae.png "Terraform apply")

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
   
![alt-text #center](https://user-images.githubusercontent.com/87687468/199249004-71ba8ba6-d67e-49ae-bb8d-865b5c16d54f.png "Terraform destroy")
