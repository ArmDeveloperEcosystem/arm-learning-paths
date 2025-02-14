---
additional_search_terms:
- cloud
- vm
- virtual machine
- deploy


layout: installtoolsall
minutes_to_complete: 30
author: Jason Andrews
multi_install: false
multitool_install_part: false
official_docs: https://developer.hashicorp.com/terraform/docs
test_images:
- ubuntu:latest
test_link: false
test_maintenance: true
test_status:
- passed
title: Terraform
tool_install: true
weight: 1
---

[Terraform](https://www.terraform.io/) automates cloud infrastructure. It is an infrastructure as code tool.

Terraform is available for Windows, macOS, Linux and supports the Arm architecture.

## Before you begin

[General installation information](https://developer.hashicorp.com/terraform/downloads) is available which covers all supported operating systems.

This article provides a quick solution to install Terraform for Ubuntu on Arm.

Confirm you are using an Arm machine by running:
```bash
uname -m
```
The output should be:
```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## Download and Install

The easiest way to install Terraform for Ubuntu on Arm is to use the zip file and copy the executable.

The installation options with the Ubuntu package manager at time of writing do not work well, but please try them as they may improve.

Make sure `unzip`, `curl`, and `wget` are available.

```bash { target="ubuntu:latest" }
sudo apt install -y unzip curl wget
```

Download and install the latest version. There is just one executable to copy to the desired location.

```bash { target="ubuntu:latest" }
TER_VER=`curl -s https://api.github.com/repos/hashicorp/terraform/releases/latest | grep tag_name | cut -d: -f2 | tr -d \"\,\v | awk '{$1=$1};1'`
wget https://releases.hashicorp.com/terraform/${TER_VER}/terraform_${TER_VER}_linux_arm64.zip
unzip terraform_${TER_VER}_linux_arm64.zip
sudo cp terraform /usr/local/bin/
```

Confirm the executable is available.

```bash { target="ubuntu:latest" }
terraform version
```
