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
Hit return for the first prompt then run accept all. To run a 'silent' install that accepts all default values with no prompts, use the --accept-all-defaults parameter. 


```bash { target="ubuntu:latest" }
 --accept-all-defaults
```

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


After 'oci setup config' login to the OCI web console to access your OCID and API key you will need this later.

To locate your OCID you open the Profile menu and click Tenancy: <your_tenancy_name>.

![alt-text #center](https://user-images.githubusercontent.com/89662128/249609571-34848e91-c4a5-4266-b5e3-45d48f797de9.png)


To locate your API KEYS open your profile and click API KEYS:

![alt-text #center](https://user-images.githubusercontent.com/89662128/249819544-faa03f40-6d4f-448a-aaef-25870cf3a48c.jpeg "Click add API key, from there generate your API key pair")


After a successful log in, you can use the [OCI CLI](../oci-cli) and automation tools like [Terraform](../terraform) from the terminal.
