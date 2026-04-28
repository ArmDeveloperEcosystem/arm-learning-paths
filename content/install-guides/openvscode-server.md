---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: OpenVSCode Server

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- ide
- vs code
- vs
- visual studio

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 30

author: Jason Andrews

### Link to official documentation
official_docs: https://github.com/gitpod-io/openvscode-server/tree/docs

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

OpenVSCode Server is a version of VS Code which runs on any computer and can be accessed using a browser. The project was initiated by Gitpod and is available on [GitHub](https://github.com/gitpod-io/openvscode-server/).

OpenVSCode Server supports the Arm architecture and is useful for developing on a remote Arm machine. You can use it on cloud instances without needing to install a Linux desktop. It's also useful when developing on a local Arm machine with a Linux subsystem, such as Windows Subsystem for Linux (WSL), ChromeOS with Linux enabled, or Multipass.

In this guide, you'll learn how to install OpenVSCode Server natively on an Arm Linux machine. 

## Before you begin

Confirm you are using an Arm machine by running:
```bash
uname -m
```

The output should be:
```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## Download OpenVSCode Server

Download a release of OpenVSCode Server from [GitHub](https://github.com/gitpod-io/openvscode-server/releases). The releases are in sync with VS Code and change frequently. Make sure to download the `arm64` version.

For example, use `wget` to download.

{{% notice Note %}}
The following commands use OpenVSCode Server version 1.109.5. The same command works with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version, see [OpenVSCode Server releases](https://github.com/gitpod-io/openvscode-server/releases).
{{% /notice %}}

```bash
wget https://github.com/gitpod-io/openvscode-server/releases/download/openvscode-server-v1.109.5/openvscode-server-v1.109.5-linux-arm64.tar.gz
```

## Install OpenVSCode Server

Install the download by extracting the file

```bash 
tar xvfz openvscode-server-v1.109.5-linux-arm64.tar.gz
```

## Start OpenVSCode Server

To start OpenVSCode Server run:

```bash
./openvscode-server-v1.109.5-linux-arm64/bin/openvscode-server 
```

The server will print a URL to access VS Code in a browser. The URL is a localhost URL. If your machine is a remote system or a Linux subsystem, there are two options to connect using your local browser.

- Use SSH to forward port 3000 and connect using localhost
- Open port 3000 on the remote machine and use the public IP address instead of localhost

### Connect using SSH port forwarding

For more information about SSH, see [SSH](/install-guides/ssh/). 

Use the `-L` option of `ssh` to forward port 3000.

```bash
ssh -L 3000:localhost:3000 user@ip-address
```

After connecting with port forwarding, use the localhost link printed by `openvscode-server`. It includes a token for security and is similar to:

```output
http://localhost:3000/?tkn=40711257-5e5d-4906-b88f-fe13b1f317b7
```

Open the link in your local browser. VS Code will appear.

### Connect by opening a port on the remote machine

The second option is to open port `3000` for access. On a cloud instance, this involves changing the security group to open TCP port 3000. For best security, make sure to open the port for your IP address only, not from all IP addresses. 

Each cloud provider will have instructions on how to work with security group. For an example. see the [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#adding-security-group-rule).

With the port open, substitute the public IP address of the instance instead of localhost. 

On ChromeOS, you can use the Linux configuration settings to automatically do port forwarding. You don't need an SSH connection.

![Screenshot of the ChromeOS Linux port forwarding settings showing port 3000 forwarded to the Linux environment so you can open OpenVSCode Server from your local browser.#center](/install-guides/_images/chromeospf.png)

## Other available configuration options

There are command line options to change the port, the token, and other configuration options. To see the options, run:

```bash
./openvscode-server-v1.109.5-linux-arm64/bin/openvscode-server --help
```

If you are running entirely on a local machine, you can eliminate the token using the `--without-connection-token` option.

You can also run an existing Docker image which uses Ubuntu Linux for Arm and mounts your host directory to access files on your computer. For more information, see the [GitHub README](https://github.com/gitpod-io/openvscode-server#readme).

You're now ready to use OpenVSCode. You can install your favorite Extensions, select your favorite Color Theme, and enjoy VS Code in the browser.
