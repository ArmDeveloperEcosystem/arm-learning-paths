---
layout: installtoolsall
minutes_to_complete: 10
author: Jason Andrews
multi_install: false
multitool_install_part: false
official_docs: https://learn.microsoft.com/en-us/dotnet/
ecosystem_dashboard: https://developer.arm.com/ecosystem-dashboard/linux?package=.net
additional_search_terms:
- .NET SDK
test_images:
- ubuntu:latest
test_link: null
test_maintenance: true
title: .NET SDK
tool_install: true
weight: 1
---

The [.NET SDK](https://dotnet.microsoft.com/en-us/) is a free, open-source, cross-platform development environment that provides tools and libraries for building applications. You can use it to create web apps, mobile apps, desktop apps, cloud services, and more.

.NET 10 is the latest Long Term Support (LTS) release. .NET 9 (Standard Term Support) and .NET 8 (LTS) are also available. This guide defaults to .NET 10, with instructions for selecting an alternative version.

The .NET SDK is available for Linux distributions on Arm-based systems.

## What should I do before installing the .NET SDK on Arm Linux?

Confirm you are using an Arm machine by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

## How do I install the .NET SDK on my Arm Linux system?

There are two ways to install the .NET SDK on your computer:
- Using the Linux package manager.
- Using the install script.

Select the one that works best for you.

### How can I install .NET SDK using the Linux package manager?

Use `apt` to install the .NET 10 SDK on Ubuntu and Debian:

```bash
sudo apt-get update && sudo apt-get install -y dotnet-sdk-10.0
```

Use `dnf` to install the .NET 10 SDK on Fedora:

```console
sudo dnf install dotnet-sdk-10.0
```

To install a different version, replace `10.0` with the version you need. For example, use `dotnet-sdk-9.0` for .NET 9 or `dotnet-sdk-8.0` for .NET 8.

If the .NET SDK is not found in your package manager, you can install it using a script.

### How can I install .NET SDK using a script?

To install the .NET SDK using a script, follow the instructions below:

1.	Download the install script:

```bash
wget https://dot.net/v1/dotnet-install.sh
```

2.	Run the script to install the .NET SDK under the `$HOME/.dotnet` folder.

You have several options for specifying the version.

To install the latest LTS version (.NET 10), run:

```bash
bash ./dotnet-install.sh
```

To install the latest available version (including STS releases), run:

```bash
bash ./dotnet-install.sh --version latest
```

To install a specific version channel, use the `--channel` flag. For example, to install .NET 10:

```bash
bash ./dotnet-install.sh --channel 10.0
```

You can also use `--channel 9.0` for .NET 9 or `--channel 8.0` for .NET 8.

3.	Add the .dotnet folder to the PATH environment variable:

```bash
export PATH="$HOME/.dotnet/:$PATH"
```

You can also add the search path to your `$HOME/.bashrc` so it is set for all new shells.

## How do I verify the .NET SDK installation?

To check that the installation was successful, run:

```bash
dotnet --list-sdks
```

The output is similar to:

```output
10.0.103 [/usr/lib/dotnet/sdk]
```

For more detailed information about your installation, run:

```bash
dotnet --info
```

The output is similar to:

```output
.NET SDK:
 Version:           10.0.103
 Commit:            c2435c3e0f
 Workload version:  10.0.100-manifests.a62d7899
 MSBuild version:   18.0.11+c2435c3e0

Runtime Environment:
 OS Name:     ubuntu
 OS Version:  24.04
 OS Platform: Linux
 RID:         linux-arm64
 Base Path:   /home/ubuntu/.dotnet/sdk/10.0.103/

.NET workloads installed:
There are no installed workloads to display.
Configured to use workload sets when installing new manifests.
No workload sets are installed. Run "dotnet workload restore" to install a workload set.

Host:
  Version:      10.0.3
  Architecture: arm64
  Commit:       c2435c3e0f

.NET SDKs installed:
  10.0.103 [/home/ubuntu/.dotnet/sdk]

.NET runtimes installed:
  Microsoft.AspNetCore.App 10.0.3 [/home/ubuntu/.dotnet/shared/Microsoft.AspNetCore.App]
  Microsoft.NETCore.App 10.0.3 [/home/ubuntu/.dotnet/shared/Microsoft.NETCore.App]

Other architectures found:
  None

Environment variables:
  Not set

global.json file:
  Not found

Learn more:
  https://aka.ms/dotnet/info

Download .NET:
  https://aka.ms/dotnet/download
```

The exact version numbers depend on when you install and which updates are available.

## How can I run a simple example to confirm the .NET SDK is working?

Create a new console application to verify that the .NET SDK works correctly:

```bash
dotnet new console -o myapp
```

Change to the new directory and run the application:

```bash
cd myapp
dotnet run
```

The expected output is:

```output
Hello, World!
```

You are ready to use the .NET SDK on Arm Linux.

Explore more .NET examples by visiting the [Learning Center](https://dotnet.microsoft.com/en-us/learn).
