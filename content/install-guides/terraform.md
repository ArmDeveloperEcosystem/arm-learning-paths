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
ecosystem_dashboard: https://developer.arm.com/ecosystem-dashboard/linux?package=terraform
test_images:
- ubuntu:latest
test_link: false
test_maintenance: true
title: Terraform
tool_install: true
weight: 1
---

[Terraform](https://www.terraform.io/) automates cloud infrastructure. It is an infrastructure as code (IaC) tool.

Terraform is available for Windows, macOS, Linux and supports the Arm architecture. For general installation information that covers all supported operating systems, see the [Terraform documentation](https://developer.hashicorp.com/terraform/downloads).

In this guide, you'll learn how to install Terraform for Ubuntu on Arm and macOS on Apple Silicon. 

## Before you begin

Confirm you are using an Arm machine by running:

```bash
uname -m
```

For Linux, the output should be:

```output
aarch64
```

For macOS, the output should be:

```output
arm64
```

## Download and install Terraform for Ubuntu

To install Terraform for Ubuntu on Arm, use a zip file and copy the executable.

<!-- The installation options with the Ubuntu package manager at time of writing don't work well, but please try them as they may improve. -->

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

## Download and install Terraform for macOS

If you have [brew](https://brew.sh/) installed, you can use it to install Terraform for macOS with the following commands:

```console
brew tap hashicorp/tap
brew install hashicorp/tap/terraform
```

If you don't have brew installed or prefer to directly install via binary, you can download [Terraform for ARM64](https://developer.hashicorp.com/terraform/install#darwin) directly from the Terraform website.

## Verify Terraform installation

After installing, you can enter the following command to verify the installation:

```bash { target="ubuntu:latest" }
terraform version
```

The output for Linux is similar to:

```output
Terraform v1.14.9
on linux_arm64
```

The output for macOS is similar to:

```output
Terraform v1.14.9
on darwin_arm64
```
## Next steps

You are now ready to use Terraform. You can explore Learning Paths to work with Terraform on Arm, such as [Deploy Arm virtual machines on Google Cloud Platform (GCP) using Terraform](/learning-paths/servers-and-cloud-computing/gcp/) and [Deploy Arm instances on AWS using Terraform](/learning-paths/servers-and-cloud-computing/aws-terraform/).
