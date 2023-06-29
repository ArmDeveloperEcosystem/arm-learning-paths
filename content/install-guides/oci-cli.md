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

The Oracle Cloud Infrastructure Command Line Interface (OCI CLI) is a cross-platform command-line tool that can be installed locally on development computers. OCI CLI is used to connect to OCI and execute administrative commands on OCI resources. 

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

The easiest way to install OCI CLI for Ubuntu on Arm is to use the install script. 

You can run an automated install with default values or an interactive install to change the default values.

To run an an automated install with default values run: 

```bash { target="ubuntu:latest" }
curl -o install.sh https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh
bash ./install.sh --accept-all-defaults
```

To run an interactive install that allows you to change default values run: 

```console
bash -c "$(curl -L https://raw.githubusercontent.com/oracle/oci-cli/master/scripts/install/install.sh)"
```

Run the command below to add the `oci` command to your search path: 

```bash { target="ubuntu:latest" }
source $HOME/.bashrc
```

Verify OCI CLI is installed using the `--version` option:

```bash { target="ubuntu:latest", env_source="~/.bashrc" }
oci --version
```

Configure OCI CLI using the `setup config` command: 

```console
oci setup config
```

To complete the setup you will need your OCID and API key. 

Log in to the OCI web console to access your OCID and API key.

Open the Profile menu and click Tenancy: <your_tenancy_name> to locate your OCID. 

![alt-text #center](https://user-images.githubusercontent.com/89662128/249609571-34848e91-c4a5-4266-b5e3-45d48f797de9.png)

To locate your API KEYS open your profile and click API KEYS:

![alt-text #center](https://user-images.githubusercontent.com/89662128/249819544-faa03f40-6d4f-448a-aaef-25870cf3a48c.jpeg "Click add API key, from there generate your API key pair")

After a successful log in, you can use the OCI CLI and automation tools like [Terraform](../terraform) from the terminal.
