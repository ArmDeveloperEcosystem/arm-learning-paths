---
title: PowerShell
minutes_to_complete: 10
official_docs: https://learn.microsoft.com/en-us/powershell/
ecosystem_dashboard: https://developer.arm.com/ecosystem-dashboard/linux?package=powershell
author: Jason Andrews
additional_search_terms:
- pwsh
- linux

test_images:
- ubuntu:latest

### FIXED, DO NOT MODIFY
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: FALSE            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

PowerShell is a cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework. It runs on a variety of operating systems, including Windows, Linux, and macOS. 

There are multiple ways to install PowerShell. In this guide, you'll learn how to install PowerShell on an Arm Linux computer.

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

## Install PowerShell on Arm Linux

{{% notice Note %}}
The PowerShell installation documentation for Linux package managers does not work for the Arm architecture because there is no Arm support in the repositories. This may change for future versions of PowerShell.
{{% /notice %}}

You can download a release file for the Arm architecture from GitHub and install it using the steps below:

{{% notice Note %}}
The following commands use PowerShell version 7.6.1. The same commands work with other versions. Replace the file used in these steps with the file for your version of choice. To find the latest version, see [PowerShell releases](https://github.com/PowerShell/PowerShell/releases).
{{% /notice %}}

1. Copy and paste the commands below to your Linux shell prompt:

```bash { target="ubuntu:latest" }
# Download the powershell '.tar.gz' archive
curl -L -o /tmp/powershell.tar.gz https://github.com/PowerShell/PowerShell/releases/download/v7.6.1/powershell-7.6.1-linux-arm64.tar.gz

# Create the target folder where powershell will be placed
sudo mkdir -p /opt/microsoft/powershell/7

# Expand powershell to the target folder
sudo tar zxf /tmp/powershell.tar.gz -C /opt/microsoft/powershell/7

# Set execute permissions
sudo chmod +x /opt/microsoft/powershell/7/pwsh

# Create the symbolic link that points to pwsh
sudo ln -s /opt/microsoft/powershell/7/pwsh /usr/bin/pwsh
```

2. Confirm the `pwsh` executable is in the search path:

```bash { target="ubuntu:latest" }
which pwsh
```

The path is printed:

```output
/usr/bin/pwsh
```

3. Verify the installed version: 

```bash { target="ubuntu:latest" }
pwsh --version
```

The output is similar to:

```output
PowerShell 7.6.1
```

## Verify PowerShell installation

To verify your installation of PowerShell, print a hello world message using `pwsh`:

```bash { target="ubuntu:latest" }
pwsh -c Write-Host Hello Arm Linux world! 
```

The output is similar to:

```output
Hello Arm Linux world!
```
You are now ready to use PowerShell on your Arm Linux computer.