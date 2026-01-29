---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: WindowsPerf (wperf)

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- perf
- profiling
- profiler
- windows
- woa
- windows on arm
- open source windows on arm


### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

### Link to official documentation
official_docs: https://gitlab.com/Linaro/WindowsPerf/windowsperf/blob/main/INSTALL.md

author: Jason Andrews

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

WindowsPerf is a Linux Perf-inspired Windows on Arm performance profiling tool. Profiling is based on the Arm AArch64 PMU and its hardware counters. WindowsPerf supports the counting model for obtaining aggregate counts of occurrences of PMU events, and the sampling model for determining the frequencies of event occurrences produced by program locations at the function, basic block, and instruction levels.  WindowsPerf is an open-source project hosted on [GitLab](https://gitlab.com/Linaro/WindowsPerf/windowsperf/)

WindowsPerf consists of a kernel-mode driver and a user-space command-line tool. You can seamlessly integrate the WindowsPerf command line tool with both the [WindowsPerf Visual Studio Extension](#vs2022) and the [WindowsPerf VS Code Extension](#vscode). These extensions, which you can download from the Visual Studio Marketplace, enhance the functionality of WindowsPerf by providing a user-friendly interface, and additional features for performance analysis and debugging. This integration allows developers to efficiently analyze and optimize their applications directly within their preferred development environment.

{{% notice  Note%}}
You cannot use WindowsPerf on virtual machines, such as cloud instances.
{{% /notice %}}

## How do I install WindowsPerf using winget?

You can now install WindowsPerf directly from [winget](https://learn.microsoft.com/en-us/windows/package-manager/). Open an `Administrator` terminal on PowerShell and type

```console
winget install WindowsPerf
```

The output should look like:

```output
Found WindowsPerf [Arm.WindowsPerf] Version 4.3.1.0
This application is licensed to you by its owner.
Microsoft is not responsible for, nor does it grant any licenses to, third-party packages.
Downloading https://developer.arm.com/-/cdn-downloads/permalink/WindowsPerf/Installer/windowsperf-4.3.1.msi
  3.07 MB
Successfully verified installer hash
Starting package install...
Successfully installed
```

![Winget installation video](/install-guides/_images/wperf-winget-installation.gif)

It will install the latest available WindowsPerf along with the [WPA plugins](/learning-paths/laptops-and-desktops/windowsperf_wpa_plugin/). To check that the installation was done correctly open a new terminal tab or window and follow the instructions under the [verify installation section](/install-guides/wperf/#verify-install).

### How do I uninstall WindowsPerf using winget?

If you need to uninstall WindowsPerf, open an `Administrator` terminal on PowerShell and run:

```console
winget uninstall WindowsPerf
```

The output from a successful uninstallation will look like:

```output
Found WindowsPerf [Arm.WindowsPerf]
Starting package uninstall...
Successfully uninstalled
```

{{% notice  Note%}}
WinPerf is an open-source project. If you would like to develop WindowsPerf yourself, you may also need to install the Windows Driver Kit (WDK). Please refer to this link for more details.
https://learn.microsoft.com/en-us/windows-hardware/drivers/wdk-release-notes
{{% /notice %}}

## How do I verify that WindowsPerf is installed correctly? {#verify-install}

You can check everything is working by running the `wperf` executable.

{{% notice  Note%}}
Once you have installed the driver, you can use `wperf` without `Administrator` privileges.
{{% /notice %}}

For example:

```command
wperf --version
```

You see output similar to:

```output
        Component     Version  GitVer    FeatureString
        =========     =======  ======    =============
        wperf         4.0.0    b18197bd  +etw-app
        wperf-driver  4.0.0    b18197bd  +etw-drv

```

## How do I install the WindowsPerf Virtual Studio Extension? {#vs2022}

WindowsPerf GUI (Graphical User Interface) is a Visual Studio 2022 extension designed to bring a seamless UI experience to WindowsPerf, the command-line performance profiling tool for Windows on Arm. It is available on the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Arm.WindowsPerfGUI).

Install by opening **Extensions** menu, click **Manage Extensions**, and click **Browse**. Type `WindowsPerf` to search for Arm WindowsPerf GUI extension. Click **Install**.

{{% notice How to set up wperf.exe path in the extension%}}
In order to set the path to the `wperf.exe` executable, go to **Tools** -> **Options** -> **WindowsPerf** -> **WindowsPerf Path** and set the absolute path to the wperf.exe executable and then click on the **Validate** button.
{{% /notice %}}

Also, visit WindowsPerf GUI project website on [GitLab](https://gitlab.com/Linaro/WindowsPerf/vs-extension) for more details and latest updates.

## How do I install the WindowsPerf VS Code Extension? {#vscode}

In addition to the command-line tools, `WindowsPerf` is available on the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Arm.windowsperf).

Install by opening the **Extensions** view (Ctrl+Shift+X) and searching for `WindowsPerf`. Click **Install**.

Open **Settings** (Ctrl+,) > **Extensions** > **WindowsPerf**, and specify the path to the `wperf` executable.

{{% notice Non-Windows on Arm host%}}
You can only generate reports from a Windows on Arm device.

If using a non-Windows on Arm host, you can import and analyze `WindowsPerf` JSON reports from such devices.

You do not need to install `wperf` on non-Windows on Arm devices.
{{% /notice %}}

## What related resources are available for WindowsPerf?

### WindowsPerf

- [WindowsPerf Release 3.7.2 blog post](https://www.linaro.org/blog/expanding-profiling-capabilities-with-windowsperf-372-release)
- [WindowsPerf Release 3.3.0 blog post](https://www.linaro.org/blog/windowsperf-release-3-3-0/)
- [WindowsPerf Release 3.0.0 blog post](https://www.linaro.org/blog/windowsperf-release-3-0-0/)
- [WindowsPerf Release 2.5.1 blog post](https://www.linaro.org/blog/windowsperf-release-2-5-1/)
- [WindowsPerf release 2.4.0 introduces the first stable version of sampling model support](https://www.linaro.org/blog/windowsperf-release-2-4-0-introduces-the-first-stable-version-of-sampling-model-support/)
- [Announcing WindowsPerf: Open-source performance analysis tool for Windows on Arm](https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/announcing-windowsperf)

### WindowsPerf GUI

- [Introducing the WindowsPerf GUI: the Visual Studio 2022 extension](https://www.linaro.org/blog/introducing-the-windowsperf-gui-the-visual-studio-2022-extension/)
- [Introducing 1.0.0-beta release of WindowsPerf Visual Studio extension](https://www.linaro.org/blog/introducing-1-0-0-beta-release-of-windowsperf-visual-studio-extension/)
- [New Release: WindowsPerf Visual Studio Extension v1.0.0](https://www.linaro.org/blog/new-release-windowsperf-visual-studio-extension-v1000/)
- [Launching WindowsPerf Visual Studio Extension v2.1.0](https://www.linaro.org/blog/launching--windowsperf-visual-studio-extension-v210/)
