---
# User change
title: "Deploy MariaDB using RDS"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Before you begin

You should have the prerequisite tools installed before starting the Learning Path.

Any computer which has the required tools installed can be used for this section. The computer can be your desktop or laptop computer or a virtual machine with the required tools.

You will need an [AWS account](https://portal.aws.amazon.com/billing/signup?nc2=h_ct&src=default&redirect_url=https%3A%2F%2Faws.amazon.com%2Fregistration-confirmation#/start) to complete this Learning Path. Create an account if you don't have one.

Before you begin you will also need:
- An AWS access key ID and secret access key

The instructions to create the keys are below

### Acquire AWS Access Credentials

Terraform requires AWS authentication to create AWS resources. You can generate access keys (access key ID and secret access key) to perform authentication. Terraform uses the access keys to make calls to AWS using the AWS CLI.
To generate and configure the Access key ID and Secret access key, follow this [documentation](/install-guides/aws_access_keys).

## Deploy MariaDB RDS instances

RDS is a Relational database service provided by AWS. More information can be found [here](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MariaDB.html).
To deploy an RDS instance of MariaDB, we have to create a Terraform file called `main.tf`. Below is the complete `main.tf`.

```terraform

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
  skip_final_snapshot  =  true
  username              = var.username
  password              = var.password
  availability_zone     = "us-east-2a"
  publicly_accessible  = true
  deletion_protection   = false

  tags = {
        name                 = "TEST MariaDB"
  }
}

```  

We also need to create a `credential.tf` file, for passing our password. Below is the `credential.tf` file

```terraform
variable "username"{
      default  = "admin"
}

variable "password"{
      default  = "Armtest"    #we_can_choose_any_password, except special_characters.
}

```

To run Graviton (Arm) based DB instance, we need to select Amazon **M6g** and **R6g** as a [instance type](https://aws.amazon.com/blogs/database/key-considerations-in-moving-to-graviton2-for-amazon-rds-and-amazon-aurora-databases/). Here, we select **db.m6g.large** as a **instance_class**. 

Now, use the below Terraform commands to deploy `main.tf` file.

## Terraform commands

Same instructions as on the [previous page](/learning-paths/server-and-cloud/mariadb/ec2_deployment#terraform-commands).

### Initialize Terraform

```bash
terraform init
```

### Create a Terraform execution plan (optional)

```bash
terraform plan
```

### Apply a Terraform execution plan

```bash
terraform apply
```      

{{% notice Note %}}
Creating the RDS database may take a few minutes.
{{% /notice %}}

                                                                                                           
### Verify RDS


To verify the setup on AWS console, go to **RDS » Databases**, you should see the instance running.  

![Screenshot (374)](https://user-images.githubusercontent.com/92315883/218340185-097c876e-2c3c-4630-adef-ac9b905c08ec.png)


## Connect to RDS 

To access the RDS instance, make sure that our instance is correctly associated with a security group and VPC. To access RDS outside the VPC, follow this [document](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.Connect.html).

To connect to the RDS instance, we need the **Endpoint** of the RDS instance. To find the Endpoint, go to **RDS »Dashboard » {{YOUR_RDS_INSTANCE}}**.

![Screenshot (372)](https://user-images.githubusercontent.com/92315883/218339661-0ac51c95-8789-42bc-962c-0b43fc64fb5b.png)


Now, we can connect to RDS by using the above **Endpoint**. Use the **user** and **password** mentioned in the `credential.tf` file.

```console
mariadb -h {{Endpoint}} -u {{user}} -p {{password}}
```
{{% notice Note %}} Replace **{{Endpoint}}**, **{{user}}** and **{{password}}** with your values.{{% /notice %}}
                   
```bash { output_lines="2-15"}
mariadb -h {{Endpoint}} -u admin -pArmtest
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 6
Server version: 10.6.12-MariaDB-0ubuntu0.22.04.1 Ubuntu 22.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]>
```

### Create Database and Table
To create database and table, follow this [document](/learning-paths/server-and-cloud/mariadb/ec2_deployment#access-database-and-create-table).

### Clean up resources

Run `terraform destroy` to delete all resources created.

```console
terraform destroy
```

