---
title: Install MySQL with Docker on an Arm-based Linux server
description: Install MySQL 8.4 in a Docker container on an Arm-based Linux server and check that the service is running.
weight: 2
layout: "learningpathall"
---

## MySQL installation options

Cloud services such as Amazon Relational Database Service (RDS) handle MySQL installation for you. On a bare-metal or cloud server, you can install MySQL in several ways.

You'll install MySQL on an Arm-based Linux server using a container image. For other installation approaches, see [Chapter 2 Installing MySQL](https://dev.mysql.com/doc/refman/8.1/en/installing.html) in the MySQL documentation.

## Before you begin

You need an Arm-based Linux server with Docker Engine installed and running. For Docker Engine installation instructions, see the [Docker Engine install guide](/install-guides/docker/docker-engine/).

Check the server architecture:

```bash
uname -m
```

The expected output on a 64-bit Arm server is:

```output
aarch64
```

Check that the Docker client can reach Docker Engine:

```bash
docker info
```

## Start a MySQL container

The [official MySQL container image](https://hub.docker.com/_/mysql) supports arm64. Create a Docker volume to keep the database files when the container is replaced:

```bash
docker volume create mysql-data
```

Start MySQL 8.4. Replace `change-me` with a strong password of your choice:

```bash
docker run -d \
  --name mysql-arm \
  --restart unless-stopped \
  -p 127.0.0.1:3306:3306 \
  -v mysql-data:/var/lib/mysql \
  -e MYSQL_ROOT_PASSWORD='change-me' \
  mysql:8.4
```

Docker selects the arm64 image for the server. The port binding makes MySQL available on the loopback interface of the server. The volume stores the database outside the container.

Check that the container is running:

```bash
docker ps --filter name=mysql-arm
```

MySQL needs time to initialize on its first start. Check the logs and wait until they report that the server is ready for connections:

```bash
docker logs mysql-arm
```
Ensure that the output includes ` MySQL init process done. Ready for start up.`

## What you've accomplished and what's next

You've used a container image to install MySQL on your Arm-based Linux instance. 

Next, you'll connect to MySQL and create a database in the running container.
