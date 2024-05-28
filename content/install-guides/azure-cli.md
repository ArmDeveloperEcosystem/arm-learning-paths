---
additional_search_terms:
- cloud
- azure
author_primary: Jason Andrews
layout: installtoolsall
minutes_to_complete: 15
multi_install: false
multitool_install_part: false
official_docs: https://learn.microsoft.com/en-us/cli/azure
test_images:
- ubuntu:latest
test_link: null
test_maintenance: true
test_status:
- passed
title: Azure CLI
tool_install: true
weight: 1
---

[Azure CLI](https://learn.microsoft.com/en-us/cli/azure/) is a cross-platform command-line tool that can be installed locally on development computers. Azure CLI is used to connect to Azure and execute administrative commands on Azure resources. 

It is available for a variety of operating systems and Linux distributions and has multiple ways to install it. 

## Before you begin

[General installation information](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt) is available which covers all supported Linux distributions. Starting with version 2.46.0, Azure CLI supports Arm64 Linux distributions. The 'apt' package manager contains both x86_64 and Arm64 packages for the following linux distributions

```output
Ubuntu 20.04, Ubuntu 22.04, Ubuntu 24.04
```

## Install via Azure CLI script

Confirm you are using an Arm machine by running:

```bash { target="ubuntu:latest" }
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

You can install Azure CLI using the following script. This script pulls required Arm64 packages and installs those on the system

```bash { target="ubuntu:latest" }
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

Execute the following command to verify the Azure CLI is installed correctly

```bash { target="ubuntu:latest" }
az version
```

You should see an output similar to below

```output
{
  "azure-cli": "2.61.0",
  "azure-cli-core": "2.61.0",
  "azure-cli-telemetry": "1.1.0",
  "extensions": {}
}
```

If you prefer installing the Azure CLI using Python3, follow the instructions below.

## Download and Install using pip

Another way to install Azure CLI for Ubuntu on Arm is to use Python pip. 

Install Python pip. 

```bash { target="ubuntu:latest" }
sudo apt install python3-pip python-is-python3 -y
```

Download and install Azure CLI.

```bash { target="ubuntu:latest" }
pip install azure-cli
```

The pip install updates $HOME/.profile with the path the `az` executable. Check the executable is available by printing the version.

```bash { target="ubuntu:latest" }
source $HOME/.profile
az version
```
You should see an output similar to below

```output
{
  "azure-cli": "2.61.0",
  "azure-cli-core": "2.61.0",
  "azure-cli-telemetry": "1.1.0",
  "extensions": {}
}
```

After a successful log in, you can use the [Azure CLI](../azure-cli) and automation tools like [Terraform](../terraform) from the terminal.
