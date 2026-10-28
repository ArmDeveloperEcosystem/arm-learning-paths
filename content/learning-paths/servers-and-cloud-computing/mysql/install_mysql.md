---
title: Install MySQL on an Arm-based Linux server
weight: 2
layout: "learningpathall"
---

## MySQL installation options

If you're using a cloud service like Amazon Relational Database Service (RDS), the installation of MySQL is handled by those services. However, if you're working with a bare metal or cloud node, there are a few different installation options. You'll configure MySQL on an Arm Linux server using a container image.

For other installation approaches, see [Chapter 2 Installing MySQL](https://dev.mysql.com/doc/refman/8.1/en/installing.html) in the MySQL documentation.

## Before you begin

You need an Arm-based Linux server with Docker Engine installed and running. Follow the [Docker install guide](https://learn.arm.com/install-guides/docker/) to choose an installation path, or use the [Docker Engine install guide](https://learn.arm.com/install-guides/docker/docker-engine/) for an Arm Linux server.

Check the server architecture:

```bash
uname -m
```

On a 64-bit Arm server, the output is:

```output
aarch64
```

Check that the Docker client can reach Docker Engine:

```bash
docker info
```

If the command reports a connection error, follow the [Docker Engine install guide](https://learn.arm.com/install-guides/docker/docker-engine/) before continuing.

## Start a MySQL container

The [official MySQL container image](https://hub.docker.com/_/mysql) supports Arm64. Create a Docker volume to keep the database files when the container is replaced:

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

Docker selects the Arm64 image for the server. The port binding makes MySQL available on the server's loopback interface. The volume stores the database outside the container.

Check that the container is running:

```bash
docker ps --filter name=mysql-arm
```

MySQL needs time to initialize on its first start. Check the logs and wait until they report that the server is ready for connections:

```bash
docker logs mysql-arm
```

## What you've accomplished and what's next

You can now connect to MySQL and create a database in the running container.
