---
additional_search_terms:
- cloud
- OCI
- Oracle 
- infrastructure

layout: installtoolsall
minutes_to_complete: 10
author_primary: Daniel Gubay
multi_install: false
multitool_install_part: false
official_docs: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm
test_images:
- ubuntu:latest

test_maintenance: true
test_status:
- passed
title: Oracle Cloud Infrastructure (OCI) CLI
tool_install: true
weight: 1
---

[OCI CLI](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm) is a cross-platform command-line tool that can be installed locally on development computers. OCI CLI is used to connect to OCI and execute administrative commands on OCI resources. 

It is available for a variety of operating systems and Linux distributions and has multiple ways to install it. 

## Before you begin

[General installation information](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/cliinstall.htm#InstallingCLI__linux_and_unix) is available which covers all supported Linux distributions. 
 
This install guide provides a quick solution to install OCI CLI for Ubuntu on Arm.

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

The easiest way to install OCI CLI for Ubuntu on Arm is to use the installer script. 

Install OCI using the command below. 

```bash { target="ubuntu:latest" }
bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"
```
To run a 'silent' install that accepts all default values with no prompts, use the --accept-all-defaults parameter.

Otherwise respond to the Installation Script Prompts if you wish to make a change.
 


Verify OCI CLI installed. 

```bash { target="ubuntu:latest" }
oci --version
```

 Run the command below to have OCI work after the initial install.

```bash { target="ubuntu:latest" }
source $HOME/.bashrc
```


Run the command below to get started on OCI.
```bash { target="ubuntu:latest" }
oci setup config
```

After a successful log in, you can use the [OCI CLI](../oci-cli) and automation tools like [Terraform](../terraform) from the terminal.
