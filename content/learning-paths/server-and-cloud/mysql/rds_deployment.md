---
# User change
title: "Deploy MySQL using RDS(AWS)"

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Deploy MySQL using Amazon RDS (Relational Database Service)

RDS is a Relational database service provided by AWS. More information can be found [here](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html). To deploy a MySQL RDS instance, we need to create a `main.tf` Terraform file.
To generate and configure the Access key ID and Secret access key, follow the instructions mentioned in this [guide](/install-guides/aws_access_keys).

Here is the complete main.tf file:

```console
provider "aws" {
  region = "us-east-2"
}

resource "aws_db_instance" "Testing_Mysql" {
  identifier           = "mysqldatabase"
  allocated_storage    = 10
  db_name              = "mydb"
  engine               = "mysql"
  engine_version       = "8.0.28"
  instance_class       = "db.t3.micro"
  parameter_group_name = "default.mysql8.0"
  skip_final_snapshot  =  true
  username              = var.username
  password              = var.password
  availability_zone     = "us-east-2a"
  publicly_accessible  = true
  deletion_protection   = false

  tags = {
        name                 = "TEST MYSQL"
  }
}
``` 

To find the correct instance type for RDS, Check the [list](https://aws.amazon.com/rds/mysql/instance-types/) of supported instance types. We selected a Graviton (Arm) based instance type.

![Screenshot (260)](https://user-images.githubusercontent.com/92315883/209249327-3755d7ef-581b-456c-a64b-e2167080dd59.png)

We also need to create a `credential.tf` file, for passing our secret keys and password. Here is the file content:

```console
variable "username"{
      default  = "admin"
}

variable "password"{
      default  = "Arm4test"    #we_can_choose_any_password, except special_characters.
}

```

Now, use the below Terraform commands to deploy the `main.tf` file.

## Terraform commands

Same instructions as on the [previous page](/learning-paths/server-and-cloud/mysql/ec2_deployment#terraform-commands).

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

### Verify the RDS setup

To verify the setup on AWS console. Go to **RDS » Databases**, you should see the instance running.  

![Screenshot (257)](https://user-images.githubusercontent.com/92315883/209247626-2df854ca-a781-46b0-aeba-076a23b0c1fb.png)

## Connect to RDS using EC2 instance

To access the RDS instance, we need to make sure that our instance is correctly associated with a security group and VPC. To access RDS outside the VPC, Follow this [document](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.Connect.html).

To connect to the RDS instance, we need the `Endpoint` of the RDS instance. To find the Endpoint, Go to **RDS » Dashboard » {{YOUR_RDS_INSTANCE}}**.

![Screenshot (280)](https://user-images.githubusercontent.com/92315883/209741254-55b40b52-1c56-482a-ab48-e33f510a1cf6.png)


Now, we can connect to RDS with the MySQL Client installed locally using the above Endpoint. Use the `username` and `password` mentioned in the `credential.tf` file.

```bash { output_lines="2-15"}
mysql -h {{Endpoint}} -u admin -pArm4test
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 32
Server version: 8.0.28 Source distribution

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```
{{% notice Note %}}
Replace `{{Endpoint}}`, user name and password with your values.
{{% /notice %}}


### Create Database and Table
Use the below command to list, create and use database.

```console { output_lines="2-11" }
show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mydb               |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.10 sec)
```

```console { output_lines="2" }
create database arm_test;
Query OK, 1 row affected (0.11 sec)
```

```console { output_lines="2-12" }
show databases;
+--------------------+
| Database           |
+--------------------+
| arm_test           |
| information_schema |
| mydb               |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.10 sec)
```

```console { output_lines="2" }
use arm_test;
Database changed
```

To create and access a table, follow this [document](/learning-paths/server-and-cloud/mysql/ec2_deployment#access-database-and-create-table).

