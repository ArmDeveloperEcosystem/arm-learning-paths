---
# User change
title: "Deploy MySQL via Docker"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Deploy MySQL via Docker
Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly.
To deploy the MySQL container, we have to create a `main.tf` Terraform file.


### Here is the main.tf file.
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
**NOTE:**- Replace `{{your_mysql_password}}` with your MySQL password.

Use the below Terraform commands to deploy the `main.tf` file.

**NOTE:**- We are running this Terraform file directly on the host (where we want to deploy MySQL).

## Terraform Commands

### Initialize Terraform

Run `terraform init` to initialize the Terraform deployment. This command is responsible for downloading all the dependencies which are required for the AWS provider.

```console
terraform init
```
    
![Screenshot (249)](https://user-images.githubusercontent.com/92315883/209109372-34a05d22-097e-4018-97c5-ef072d9b0e20.png)

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

![Screenshot (247)](https://user-images.githubusercontent.com/92315883/209082799-476b17f1-6851-4f93-b8db-287daddc52d3.png)
   

## Check the deployment of MySQL container

After applying the Terraform file with the `terraform apply` command, a MySQL container will be created. Follow below steps to verify the creation of a container.

### Check container deplyoment
Use the `docker ps` command to list out all running containers in Docker engine.

![Screenshot 2022-12-22 131700](https://user-images.githubusercontent.com/92315883/209083915-cf7100d1-d26a-4aad-8239-d3e75cd01c62.png)

As we can see in the above image, our container has been created with `Mysql:8` image.

### Access the docker container
To connect to the MySQL container, we need to use the MySQL client to interact with the database.

```console
apt install mysql-client
```
```console
mysql -h 127.0.0.1 -P3306 -uroot -p
```

![Screenshot (248)](https://user-images.githubusercontent.com/92315883/209085632-6dff8769-6d81-4bfc-a0a2-ce1b352aebac.png)

