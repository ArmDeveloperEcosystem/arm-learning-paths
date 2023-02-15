---
# User change
title: "Configure and run WSL with various Linux distributions"

weight: 2

layout: "learningpathall"
---

## Prerequisites

This Learning Path assumes you have a  Windows on Arm computer such as [Windows Dev Kit 2023](https://learn.microsoft.com/en-us/windows/arm/dev-kit) or a Lenovo Thinkpad X13s laptop running Windows 11. 

All major cloud csp have introduced Arm virtual machine instances. For more information about how to get started refer to [Getting Started with Arm-based Cloud Services](/learning-paths/server-and-cloud/csp/). 

Using the same Arm architecture on a local development machine and on the cloud provides interoperability, consistency, and saves time. 

## Installing WSL 2

Software developers often use Linux for creating applications and containers. Windows on Arm includes the [Windows Subsystem for Linux 2](https://docs.microsoft.com/en-us/windows/wsl/about) (WSL 2). 

WSL 2 replaces the system call translation layer provided in WSL 1 with the latest virtualization technology to run a complete Linux kernel. WSL 2 running on a Windows on Arm computer provides a complete Linux kernel and supports many Arm Linux distributions. 

WSL 2 can also run containers for application development. WSL 2 provides much faster file I/O compared to WSL 1.

Installing WSL 2 requires Windows 11. A recent Windows 10 version is also possible, but these instructions were tested on Windows 11. Windows 11 is recommended to complete all of the examples in this Learning Path. All of the examples have been tested using WSL2. If only WSL is specified it means WSL2.

Below is the short version on how to install WSL2. Microsoft documentation provides a [Quickstart](https://docs.microsoft.com/en-us/windows/wsl/install-win10) with full details on how to install WSL 2. There are also numerous tutorials available (for non-Arm architectures).

There are three steps to setup WSL 2.

First, open “Turn Windows features on or off” in the Windows control panel and make sure “Virtual Machine Platform” and “Windows Subsystem for Linux” are checked. 

![Turn Windows features on or off](https://dev-to-uploads.s3.amazonaws.com/i/9kubnntqzsfq9lxfrfrk.PNG#center)

Next, download and install WSL 2 from the [Microsoft Store](https://apps.microsoft.com/store/detail/windows-subsystem-for-linux-preview/9P9TQF7MRM4R).

The last step is to set the default version to WSL 2 by running the following command at a PowerShell or Command Prompt.

```console
wsl --set-default-version 2
```

Once WSL 2 is installed, the Microsoft store is the easiest place to find a Linux distribution. [Installing Ubuntu 22.04](https://apps.microsoft.com/store/detail/ubuntu-22041-lts/9PN20MSR04DW) is quick and easy from the store. 

There are other Linux distributions available in the Microsoft Store. Make sure to select the ones that work on Arm. Some do not work and it may be some trial-and-error to identify those that work on Arm.

Another way to install Linux distributions is using the WSL command. 

Using a Windows Command Prompt list the distributions available.

```cmd 
wsl --list --online
```

Install a distribution from the list returned by the list online command.

Be patient, the progress may stay on 0 for a bit.

```cmd
wsl --install Ubuntu
```

After installation, each Linux distribution will have an icon on the Windows application menu. Use this icon to start WSL with the Linux distribution. 

A new window should open with a Linux shell. 

![Running Linux](wsl-linux.png)

## Use Windows terminal

Windows Terminal is a great way to use WSL. It can be installed from the [Microsoft Store](https://apps.microsoft.com/store/detail/windows-terminal/9N0DX20HK701). The [repository is on GitHub](https://github.com/microsoft/terminal). 

Windows Terminal supports multiple command lines: PowerShell, Command Prompt, and WSL Linux. It's also very configurable.

## Run bash.exe

From Windows, bash.exe (or just bash) can be used to run commands in WSL. 

The default WSL distribution can be entered by running bash from a Windows Command Prompt.

```cmd
bash.exe
```

The -c option to bash.exe can be used to run a command in WSL and collect the result. 

List the contents of /usr/bin in WSL from a Windows Command Prompt.

```cmd
bash.exe -c "ls /usr/bin"
```

## WSL command line options

Review the  WSL command line options.

```console
wsl --help
```

List the installed distributions. 

```console
wsl --list
```

List only the running distributions.

```console
wsl --list --running
```

Terminate a running distribution.

```console
wsl --terminate Ubuntu-22.04
```

Shutdown all running distributions.

```console
wsl --shutdown
```

Unregister the Linux distribution and delete the filesystem.

```console
wsl --unregister Ubuntu-22.04
```

To update WSL use the update flag.

```console
wsl --update
```

To start the default distribution.

```console
wsl
```



