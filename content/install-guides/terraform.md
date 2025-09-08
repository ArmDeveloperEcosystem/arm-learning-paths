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
<<<<<<< HEAD
=======
test_status:
- passed
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)
title: Terraform
tool_install: true
weight: 1
---

[Terraform](https://www.terraform.io/) automates cloud infrastructure. It is an infrastructure as code tool.

Terraform is available for Windows, macOS, Linux and supports the Arm architecture.

<<<<<<< HEAD
## What do I need before installing Terraform?

[General installation information](https://developer.hashicorp.com/terraform/downloads) is available which covers all supported operating systems.

This guide provides a quick solution to install Terraform for Ubuntu on Arm and macOS on Apple Silicon.

Confirm you are using an Arm machine by running:

```bash
uname -m
```

For Linux, the output should be:

=======
## Before you begin

[General installation information](https://developer.hashicorp.com/terraform/downloads) is available which covers all supported operating systems.

This article provides a quick solution to install Terraform for Ubuntu on Arm.

Confirm you are using an Arm machine by running:
```bash
uname -m
```
The output should be:
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)
```output
aarch64
```

<<<<<<< HEAD
For macOS, the output should be:

```output
arm64
```

## How do I download and install Terraform for Ubuntu?
=======
If you see a different result, you are not using an Arm computer running 64-bit Linux.

## Download and Install
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

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

<<<<<<< HEAD
## How do I download and install Terraform for macOS?

If you have [brew](https://brew.sh/) installed, installing Terraform for macOS is simple as:

```console
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

If you don't have brew installed or prefer to directly install via binary, you can download [Terraform for ARM64](https://developer.hashicorp.com/terraform/install#darwin) directly from the Terraform website.

## How do I verify Terraform installation?

After installing, you can enter the following command to verify the installation:
=======
Confirm the executable is available.
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)

```bash { target="ubuntu:latest" }
terraform version
```
<<<<<<< HEAD

The output will be similar to the output shown below.

For Linux:

```output
Terraform v1.10.5
on linux_arm64
```

For macOS:

```output
Terraform v1.10.5
on darwin_arm64
```

You are now ready to use Terraform.
=======
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)
