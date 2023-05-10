---
title: "Install Nginx from the package manager"
weight: 2
layout: "learningpathall"
---

## Before you begin

Install Nginx on an [Arm based instance](/learning-paths/server-and-cloud/csp/) from a cloud service provider.

This Learning Path has been verified on AWS EC2 and Oracle cloud services, running `Ubuntu Linux 20.04` and `Ubuntu Linux 22.04`.

You can install Nginx either by using the package manager or build it from source. In this section, installation using the package manager is shown.

## Install Nginx using the package manager

You can refer to the [official documentation](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#installing-a-prebuilt-ubuntu-package-from-an-ubuntu-repository) for details on how to install Nginx or follow the quick start steps below.

### Quick start installation 

Update the Ubuntu repository information:

```bash
sudo apt-get update
```

Install the package:

```bash
sudo apt-get install nginx -y 
```

Verify the installation:

```bash
nginx -v
```
The output from this command should look like:

```output
nginx version: nginx/1.18.0 (Ubuntu)
```

