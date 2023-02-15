---
# User change
title: "Automate AWS EC2 instance creation using Terraform"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

##  Deploy Graviton based EC2 instances with Terraform 

## Prerequisites

* An AWS account
* An [installation of Terraform](https://www.terraform.io/cli/install/apt)
* An installation of [AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/cli-chap-install.html)
      
## Generate Access keys (access key ID and secret access key)

The installation of Terraform on your desktop or laptop needs to communicate with AWS. Thus, Terraform needs to be able to authenticate with AWS. For authentication, generate access keys (access key ID and secret access key). These access keys are used by Terraform for making programmatic calls to AWS via the AWS CLI.
  
### Go to My Security Credentials
   
![image](https://user-images.githubusercontent.com/87687468/190137370-87b8ca2a-0b38-4732-80fc-3ea70c72e431.png)

### On Your Security Credentials page click on create access keys (access key ID and secret access key)
   
![image](https://user-images.githubusercontent.com/87687468/190137925-c725359a-cdab-468f-8195-8cce9c1be0ae.png)
   
### Copy the Access Key ID and Secret Access Key 

![image](https://user-images.githubusercontent.com/87687468/190138349-7cc0007c-def1-48b7-ad1e-4ee5b97f4b90.png)

## Generate key-pair(public key, private key) using ssh keygen

### Generate the public key and private key

Before using Terraform, first generate the key-pair (public key, private key) using ssh-keygen. Then associate both public and private keys with AWS EC2 instances.

Generate the key-pair using the following command:

```console
ssh-keygen -t rsa -b 2048
```
       
By default, the above command will generate the public as well as private key at location **$HOME/.ssh**. You can override the end destination with a custom path (for example, /home/ubuntu/aws/ followed by key name aws_keys).

Output when a key pair is generated:
      
![image](https://user-images.githubusercontent.com/87687468/192259698-8219d63c-e28b-41e2-a67c-7f77dff20e9a.png)
      
**Note:** Use the public key aws_keys.pub inside the Terraform file to provision/start the instance and private key aws_keys to connect to the instance.

## Create your first Terraform infrastructure (main.tf)

Terraform files are created with a  **.tf** extension. Start by creating an empty main.tf file.

### Provider

Tell Terraform which cloud provider we are going to connect, AWS for this example. 

Here is the basic syntax for the provider
      
```console
resource "<PROVIDER>_<TYPE>" "<NAME>" {
  [CONFIG …]
}
```
      
1. "PROVIDER_TYPE" is AWS 
2. "NAME" - Select a name
   
This is how our main.tf will look like for AWS -
   
      provider "aws" {
      region     = "eu-central-1"
      access_key = "XXXXXXXXXXXXXXXXXXXX"
      secret_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
      } 
      
### Resource - "aws_instance"
Next, after defining the provider, we are going to define the resource. Resource is something that we are going to provision/start on AWS. We are going to provision an EC2 instance on AWS.
But before we provision the EC2 instance, we need to gather a few points -
   
1. **ami** = you need to tell Terraform which AMI(Amazon Machine Image) you are going to use. Is it going to be Ubuntu, CentOS or something else
2. **instance_type** = Also based on your need you have to choose the instance_type and it can be t4g.nano, t4g.micro, t4g.small etc.

### How to find ami(Amazon Machine Image)
1. To find the correct ami you need to Goto >> **EC2**
   
![image](https://user-images.githubusercontent.com/87687468/190343196-051e752a-a61d-4a6b-80d6-25369f41e97c.png)
   
2. In the left Navigation you will find **Images -> AMIs**
   
![image](https://user-images.githubusercontent.com/87687468/190343512-54fb7a3c-d048-4c23-bb66-0a0ebfb0fa80.png)
   
3. On the search menu click on public images and then apply filters as per your reuirment. e.g. architecture=arm64, platform=ubuntu.
copy the AMI ID from the search result.
   
![image](https://user-images.githubusercontent.com/87687468/190345166-846344fe-09b8-4ab8-96b0-907b67fd0abd.png)

### How to find correct instance_type
We can find the correct ìnstance_type by visiting [this page](https://aws.amazon.com/ec2/instance-types/).
Since I am looking for a very basic instance_type not production level instance, so I choose **t4g.nano**
Here is the aws_instance configuration -
   
```console
resource "aws_instance" "ec2_example" {
  ami = "ami-02a92e06fd643c11b"  
  instance_type = "t4g.nano" 
  key_name= "aws_key"
  vpc_security_group_ids = [aws_security_group.main.id]
}
```

#### Here is the complete main.tf file
    

```console
provider "aws" {
  region     = "us-east-2"
  access_key = "Axxxxxxxxxxxxxxxxxxxx"
  secret_key = "JzZKiCia2vjbq4zGGGxxxxxxxxxxxxxxxxxxxxxx"
}

resource "aws_instance" "ec2_example" {
  ami = "ami-02a92e06fd643c11b"  
  instance_type = "t4g.nano" 
  key_name= "aws_key"
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
    private_key = file("/home/ubuntu/aws/aws_key")
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
  key_name   = "aws_key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDbvRN/gvQBhFe+dE8p3Q865T/xTKgjqTjj56p1IIKbq8SDyOybE8ia0rMPcBLAKds+wjePIYpTtRxT9UsUbZJTgF+SGSG2dC6+ohCQpi6F3xM7ryL9fy3BNCT5aPrwbR862jcOIfv7R1xVfH8OS0WZa8DpVy5kTeutsuH5suehdngba4KhYLTzIdhM7UKJvNoUMRBaxAqIAThqH9Vt/iR1WpXgazoPw6dyPssa7ye6tUPRipmPTZukfpxcPlsqytXWlXm7R89xAY9OXkdPPVsrQdkdfhnY8aFb9XaZP8cm7EOVRdxMsA1DyWMVZOTjhBwCHfEIGoePAS3jFMqQjGWQd xxxx@xxx-HP-ZBook-15-G2"
}
```

NOTE : "Key_name" and "Public_key" should be replaced with actual value.

## Terraform commands
    
### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. This command is responsible for downloading all the dependencies which are required for the provider AWS.

```console
terraform init
```
    
![image](https://user-images.githubusercontent.com/87687468/190346590-e5be6def-5d6b-470a-a0cb-1057a1334cd7.png)

### Create a Terraform execution plan

Run `terraform plan` to create an execution plan.

```console
terraform plan
```

**NOTE:** The **terraform plan** command is optional. You can directly run **terraform apply** command. But it is always better to check the resources about to be created.

### Apply a Terraform execution plan

Run `terraform apply` to apply the execution plan to your cloud infrastructure. Below command creates all required infrastructure.

```console
terraform apply
```      

![image](https://user-images.githubusercontent.com/87687468/199248572-9966e305-f502-4444-943d-7eb0ba0ee9ae.png)
   
### Verify the EC2 setup

Verify the setup by going back to the AWS console.

Goto **EC2 -> instances** you should see the instance running.   
   
![image](https://user-images.githubusercontent.com/87687468/192154191-7c0c97c6-4119-4395-bd8a-2873835e2f73.png)

You can also see the tag name, Terraform EC2, which was used in the Terraform script.
   
### Use private key 'aws_key' to SSH into EC2 instance

The EC2 instance is running, now connect using the private key.

You can find the connect command from the AWS console.

![image](https://user-images.githubusercontent.com/87687468/190621116-0e9fb285-960f-437d-bfc0-77352349372c.png)   
   
### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

It will remove all resource groups, virtual networks, and all other resources created through Terraform.
   
![image](https://user-images.githubusercontent.com/87687468/199249004-71ba8ba6-d67e-49ae-bb8d-865b5c16d54f.png)

