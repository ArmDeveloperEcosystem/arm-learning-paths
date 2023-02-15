---
title: "Install Nginx from the package manager"
weight: 2
layout: "learningpathall"
---

## Prerequisites

An [Arm based instance](/learning-paths/server-and-cloud/csp/) from an appropriate cloud service provider.

This learning path has been verified on AWS EC2 and Oracle cloud services, running `Ubuntu Linux 20.04` and `Ubuntu Linux 22.04`.

## Install Nginx using the package manager

Refer to the [documentation](https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/#installing-a-prebuilt-ubuntu-package-from-an-ubuntu-repository) for more details on how to install Nginx.

### Quick start 

Follow these steps to quickly install Nginx. 

Update the Ubuntu repository information.

```bash
sudo apt-get update
```

Install the package.

```bash
sudo apt-get install nginx -y 
```

Verify the installation.

```bash
nginx -v
```
