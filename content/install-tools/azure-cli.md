---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Microsoft Azure CLI

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- cloud

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs: https://learn.microsoft.com/en-us/cli/azure

### TEST SETTINGS
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

[Azure CLI](https://learn.microsoft.com/en-us/cli/azure/) is a cross-platform command-line tool that can be installed locally on development computers. Azure CLI is used to connect to Azure and execute administrative commands on Azure resources. 

It is available for a variety of operating systems and Linux distributions and has multiple ways to install it. 

## Introduction

[General installation information](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt) is available which covers all supported Linux distributions. The instructions state that Azure CLI doesn't support Linux on Arm. 

It's likely Arm support will come soon, monitor the [GitHub issue](https://github.com/Azure/azure-cli/issues/7368) for new details. 

This article provides a quick solution to install Azure CLI for Ubuntu on Arm.

Confirm you are using an Arm machine by running:

```bash { command_line="user@localhost | 2" }
uname -m
aarch64
```

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
