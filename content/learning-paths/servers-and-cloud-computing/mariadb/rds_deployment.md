---
# User change
title: "Deploy MariaDB using RDS(AWS)"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Deploy MariaDB using Amazon RDS (Relational Database Service) 

You can deploy [MariaDB](https://mariadb.org/) on Amazon RDS using Terraform.

## Before you begin

For this section you will need a computer which has [Terraform](/install-guides/terraform/) and the [AWS CLI](/install-guides/aws-cli/) installed.

Any computer which has the required tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine with the required tools.

You will need an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) to complete this Learning Path. Create an account if you don't have one.

Before you begin you will also need:
- An AWS access key ID and secret access key

### Acquire AWS Access Credentials

Terraform requires AWS authentication to create AWS resources. You can generate access keys (access key ID and secret access key) to perform authentication. Terraform uses the access keys to make calls to AWS using the AWS CLI. 

To generate and configure the Access key ID and Secret access key, follow the [AWS Credentials install guide](/install-guides/aws_access_keys).

## Deploy MariaDB RDS instances

RDS is a relational database service provided by AWS. 

The AWS documentation covering [Creating and connecting to a MariaDB DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MariaDB.html) might also be helpful for you.

To deploy an RDS instance of MariaDB you can use Terraform files. 

1. Use a text editor to add the contents below to a new file named `main.tf`.

```console
provider "aws" {
  region = "us-east-2"
}

resource "aws_db_parameter_group" "default" {
  name   = "mariadb"
  family = "mariadb10.6"
}

resource "aws_db_instance" "Testing_mariadb" {
  identifier           = "mariadbdatabase"
  allocated_storage    = 10
  db_name              = "mydb"
  engine               = "mariadb"
  engine_version       = "10.6.10"
  instance_class       = "db.m6g.large"
  parameter_group_name = "mariadb"
  skip_final_snapshot  = true
  username             = var.username
  password             = var.password
  availability_zone    = "us-east-2a"
  publicly_accessible  = true
  deletion_protection  = false

  tags = {
    name = "TEST MariaDB"
  }
}
```  

2. Use a text editor to add the contents below to a new file named `credential.tf`.

```console
variable "username" {
  default = "admin"
}

variable "password" {
  default = "Armtest1" #we_can_choose_any_password, except special_characters.
}
```
{{% notice Note %}}
The password length should be atleast 8 characters.
{{% /notice %}}

This file is used for configuring your password.  

To run RDS instances based on AWS Graviton processors you need to elect either **M6g** or **R6g** as the instance type.

The `main.tf` file selects **db.m6g.large** as the instance type. 

## Terraform commands

Use the same sequence of Terraform commands as the previous topics: init, plan, and apply. 

1. Initialize Terraform:

```bash
terraform init
```

2. Create a Terraform execution plan (optional):

```bash
terraform plan
```

3. Apply a Terraform execution plan:

```bash
terraform apply
```      

{{% notice Note %}}
Creating the RDS database may take a few minutes.
{{% /notice %}}
                                                                                                           
Wait for the deployment and then go to the AWS console. 

### Verify RDS

In the AWS console, go to **RDS » Databases**, and check if the RDS instance is running.  

![mariadb1 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/40816837/e692ab7a-2ab5-4017-b435-90fddec603ba)

## Connect to RDS 

Make sure that the instance is correctly associated with a security group and VPC. 

To connect to the RDS instance, find the endpoint. To find the Endpoint, go to **RDS »Dashboard » {{YOUR_RDS_INSTANCE}}**.

![mariadb2 #center](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/assets/40816837/df03a3ff-a91a-41de-a980-bcadee8ff6fd)

Using the **Endpoint** and the **user** and **password** mentioned in the `credential.tf` file you can connect using `mariadb`

```console
mariadb -h {{Endpoint}} -u {{user}} -p {{password}}
```
{{% notice Note %}} 
Replace **{{Endpoint}}**, **{{user}}** and **{{password}}** with your values.
{{% /notice %}}
                   

Run `mariadb` to connect. The output is similar to:

```bash { output_lines="2-15"}
mariadb -h {{Endpoint}} -u admin -pArmtest
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 6
Server version: 10.6.12-MariaDB-0ubuntu0.22.04.1 Ubuntu 22.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

For more information about accessing RDS refer to [Connecting to an Amazon RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.Connect.html).

### Create Database and Table

You can use the instructions from the previous topic to [access the Database and create a table](/learning-paths/servers-and-cloud-computing/mariadb/ec2_deployment#access-database-and-create-table).

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

