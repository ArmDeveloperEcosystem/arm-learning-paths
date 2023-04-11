---
# User change
title: "Deploy MySQL via Docker"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Deploy MySQL via Docker
Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.
To deploy the MySQL container, we have to create a `main.tf` Terraform file. Here is the file content:

```console
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.23.1"
    }
  }
}

provider "docker" {
}

resource "docker_image" "mysql" {
  name = "mysql:8"
}


resource "docker_container" "mysql" {
  name = "mysql"
  image = "${docker_image.mysql.name}"
  env = ["MYSQL_ROOT_PASSWORD={{your_mysql_password}}"]
  ports {
    internal = 3306
    external = 3306
    ip       = "127.0.0.1"
  }
}
```
{{% notice Note %}}
Replace `{{your_mysql_password}}` with your MySQL password.
{{% /notice %}}

Use the below Terraform commands to deploy the `main.tf` file.

{{% notice Note %}}
We are running this Terraform file directly on the host (where we want to deploy MySQL).
{{% /notice %}}

## Terraform Commands

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

## Check the deployment of MySQL container

After applying the Terraform file with the `terraform apply` command, a MySQL container will be created. Follow below steps to verify the creation of a container.

### Check container deployment
Use the `docker ps` command to list out all running containers in Docker engine.

```bash { output_lines="2-4" }
docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                                 NAMES
4b627bd94296   mysql:8   "docker-entrypoint.s…"   About a minute ago   Up About a minute   127.0.0.1:3306->3306/tcp, 33060/tcp   mysql
```

As we can see in the above image, our container has been created with `mysql:8` image.

### Access the docker container
To connect to the MySQL container, we need to use the MySQL client installed locally to interact with the database.

```bash { output_lines="2-24" }
mysql -h 127.0.0.1 -P3306 -uroot -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.32 MySQL Community Server - GPL

Copyright (c) 2000, 2023, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
4 rows in set (0.00 sec)
```
