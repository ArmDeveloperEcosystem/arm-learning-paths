---
layout: installtoolsall
minutes_to_complete: 10
author_primary: Jason Andrews
multi_install: false
multitool_install_part: false
official_docs: https://learn.microsoft.com/en-us/dotnet/
additional_search_terms:
- .NET SDK
test_images:
- ubuntu:latest
test_link: null
test_maintenance: true
test_status:
- passed
title: .NET SDK
tool_install: true
weight: 1
---

The [.NET SDK](https://dotnet.microsoft.com/en-us/) is a free, open-source, and cross-platform development environment that provides a broad set of tools and libraries for building applications. You can use it to create a variety of applications including web apps, mobile apps, desktop apps, and cloud services.

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

Use `apt` to install .NET SDK on Ubuntu and Debian:

```bash
sudo apt-get install -y dotnet-sdk-8.0
```

Use `dnf` to install .NET SDK on Fedora:

```console
sudo dnf install dotnet-sdk-8.0
```

If the .NET SDK is not found in your package manager, you can install it using a script.

### How can I install .NET SDK using a script?

To install the .NET SDK using a script, follow the instructions below:

1.	Download the install script:

```bash 
wget https://dot.net/v1/dotnet-install.sh
```

2.	Run the script (it will install .NET SDK 8 under the folder .dotnet): 

You have some options to specify the version you want to install.

To install the latest long term support (LTS) version, run:

```bash
bash ./dotnet-install.sh
```

To install the latest version, run:

```bash
bash ./dotnet-install.sh --version latest
```

To install a specific version, run:

```bash
bash ./dotnet-install.sh --channel 8.0
```

3.	Add the .dotnet folder to the PATH environment variable:

```bash
export PATH="$HOME/.dotnet/:$PATH"
```

You can also add the search path to your `$HOME/.bashrc` so it is set for all new shells.

## How do I verify the .NET SDK installation?

To check that the installation was successful, type: 

```bash 
dotnet --list-sdks
```

The output is printed:

```output
8.0.105 [/usr/lib/dotnet/sdk]
```

To print more information, run the following command:

```bash
dotnet --info
```

More details about your installation are printed:

```output
.NET SDK:
 Version:           8.0.105
 Commit:            eae90abaaf
 Workload version:  8.0.100-manifests.796a77f8

Runtime Environment:
 OS Name:     ubuntu
 OS Version:  24.04
 OS Platform: Linux
 RID:         ubuntu.24.04-arm64
 Base Path:   /usr/lib/dotnet/sdk/8.0.105/

.NET workloads installed:
 Workload version: 8.0.100-manifests.796a77f8
There are no installed workloads to display.

Host:
  Version:      8.0.5
  Architecture: arm64
  Commit:       087e15321b

.NET SDKs installed:
  8.0.105 [/usr/lib/dotnet/sdk]

.NET runtimes installed:
  Microsoft.AspNetCore.App 8.0.5 [/usr/lib/dotnet/shared/Microsoft.AspNetCore.App]
  Microsoft.NETCore.App 8.0.5 [/usr/lib/dotnet/shared/Microsoft.NETCore.App]

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

## How can I run a simple example to confirm the .NET SDK is working?

To test the .NET SDK installation, create a new hello world console application:

```bash
dotnet new console -o myapp
```

Change to the new directory and run:

```bash
cd myapp
dotnet run
```

The expected output in the console is:

```output
Hello World!
```

You are ready to use the .NET SDK on Arm Linux. 

You can find more information about .NET on Arm in the [AWS Graviton Technical Guide](https://github.com/aws/aws-graviton-getting-started/blob/main/dotnet.md).

Explore .NET examples by visiting the [Learning Center](https://dotnet.microsoft.com/en-us/learn).
