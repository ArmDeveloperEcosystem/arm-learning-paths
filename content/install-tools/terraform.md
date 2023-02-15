---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Terraform

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 30

### Link to official documentation
official_docs: https://developer.hashicorp.com/terraform/docs

### Test setup
test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-software-developers-ads/actions/runs/3540052189
test_maintenance: true
test_status:
- passed

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

[Terraform](https://www.terraform.io/) automates cloud infrastructure. It is an infrastructure as code tool. 

Terraform is available for Windows, macOS, Linux and supports the Arm architecture. 

## Introduction

[General installation information](https://developer.hashicorp.com/terraform/downloads) is available which covers all supported operating systems. 

In some cases the instructions don't work well for Arm platforms. 

This article provides a quick solution to install Terraform for Ubuntu on Arm.

Confirm you are using an Arm machine by running:

```bash { command_line="user@localhost | 2" }
uname -m
aarch64
```

## Download and Install

The easiest way to install Terraform for Ubuntu on Arm is to use the zip file and copy the executable. 

The installation options with the Ubuntu package manager don't work well, but feel free to try them as they may improve. 

Make sure unzip, curl, wget are available. If not, install it. 

```bash { target="ubuntu:latest" }
sudo apt install -y unzip curl wget
```

Download and install the latest version. There is just 1 executable to copy to the desired location.

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
