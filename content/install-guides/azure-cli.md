---
additional_search_terms:
- cloud
- azure
- 
layout: installtoolsall
minutes_to_complete: 15
author_primary: Jason Andrews
multi_install: false
multitool_install_part: false
official_docs: https://learn.microsoft.com/en-us/cli/azure
test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true
test_status:
- passed
title: Azure CLI
tool_install: true
weight: 1
---

[Azure CLI](https://learn.microsoft.com/en-us/cli/azure/) is a cross-platform command-line tool that can be installed locally on development computers. Azure CLI is used to connect to Azure and execute administrative commands on Azure resources. 

It is available for a variety of operating systems and Linux distributions and has multiple ways to install it. 

## Introduction

[General installation information](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt) is available which covers all supported Linux distributions. The instructions state that Azure CLI doesn't support Linux on Arm. 

It's likely Arm support will come soon, monitor the [GitHub issue](https://github.com/Azure/azure-cli/issues/7368) for new details. 

This article provides a quick solution to install Azure CLI for Ubuntu on Arm.

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

The easiest way to install Azure CLI for Ubuntu on Arm is to use Python pip. 

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

After a successful log in, you will be able to use the [Azure CLI](../azure-cli) and automation tools like [Terraform](../terraform) from the terminal.