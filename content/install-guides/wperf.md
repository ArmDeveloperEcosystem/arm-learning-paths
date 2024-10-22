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
official_docs: https://github.com/arm-developer-tools/windowsperf/blob/main/INSTALL.md

author_primary: Jason Andrews

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

WindowsPerf is a Linux Perf-inspired Windows on Arm performance profiling tool. Profiling is based on the Arm AArch64 PMU and its hardware counters. WindowsPerf supports the counting model for obtaining aggregate counts of occurrences of PMU events, and the sampling model for determining the frequencies of event occurrences produced by program locations at the function, basic block, and instruction levels.  WindowsPerf is an open-source project hosted on [GitHub](https://github.com/arm-developer-tools/windowsperf).

WindowsPerf consists of a kernel-mode driver and a user-space command-line tool. You can seamlessly integrate the WindowsPerf command line tool with both the [WindowsPerf Visual Studio Extension](#vs2022) and the [WindowsPerf VS Code Extension](#vscode). These extensions, which you can download from the Visual Studio Marketplace, enhance the functionality of WindowsPerf by providing a user-friendly interface, and additional features for performance analysis and debugging. This integration allows developers to efficiently analyze and optimize their applications directly within their preferred development environment.


{{% notice  Note%}}
You cannot use WindowsPerf on virtual machines, such as cloud instances.
{{% /notice %}}

## Visual Studio and the Windows Driver Kit (WDK)

WindowsPerf relies on `dll` files installed with Visual Studio, from the Community Edition or higher and, optionally, installers from the Windows Driver Kit extension.

For information about the WDK installation process, see [Download the Windows Driver Kit (WDK)](https://learn.microsoft.com/en-us/windows-hardware/drivers/download-the-wdk).

See also the [Visual Studio for Windows on Arm install guide](/install-guides/vs-woa/).

## Download WindowsPerf

You can download the latest release package, `windowsperf-bin-<version>.zip` from the Arm GitHub repository:
```url
https://github.com/arm-developer-tools/windowsperf/releases
```

To download directly from command prompt, use:

```console
mkdir windowsperf-bin-3.8.0
cd windowsperf-bin-3.8.0
curl -L -O https://github.com/arm-developer-tools/windowsperf/releases/download/3.8.0/windowsperf-bin-3.8.0.zip
```

Unzip the package:

```console
tar -xmf windowsperf-bin-3.8.0.zip
```

## Install wperf driver

You can install the kernel driver using the supplied `wperf-devgen` installer.

The [wperf-devgen](https://github.com/arm-developer-tools/windowsperf/blob/main/wperf-devgen/README.md) tool has been designated as the preferred installer and uninstaller for the WindowsPerf Kernel Driver in the latest release. This tool offers a simple process for managing the installation and removal of the driver.

{{% notice  Note%}}
You must install the driver as `Administrator`.
{{% /notice %}}

Open a **Windows Command Prompt** terminal with **Run as administrator** selected.

Make sure you are in the `windowsperf-bin-<version>` directory:

```command
cd windowsperf-bin-3.8.0
```

### Install with wperf-devgen {#devgen_install}

Navigate to the `wperf-driver` folder and run the installer:

```command
cd wperf-driver
wperf-devgen install
```

The output should be similar to:

```output 
Executing command: install.
Install requested.
Device installed successfully
```

## Verify install

You can check everything is working by running the `wperf` executable.

{{% notice  Note%}}
Once you have installed the driver, you can use `wperf` without `Administrator` privileges.
{{% /notice %}}

For example:

```command
cd ..\wperf
wperf --version
```

You see output similar to:

```output
        Component     Version  GitVer    FeatureString
        =========     =======  ======    =============
        wperf         3.8.0    6d15ddfc  +etw-app
        wperf-driver  3.8.0    6d15ddfc  +etw-drv

```
## Uninstall wperf driver

You can uninstall (or *remove*) the kernel driver using supplied [wperf-devgen](#devgen_uninstall) uninstaller.

{{% notice  Note%}}
You must uninstall the driver as `Administrator`.
{{% /notice %}}

### Uninstall with wperf-devgen {#devgen_uninstall}

```command
cd windowsperf-bin-3.8.0\wperf-driver
wperf-devgen uninstall
```

The output is similar to:

```console
Executing command: uninstall.
Uninstall requested.
Root\WPERFDRIVER
Device found
Device uninstalled successfully
```

## Install WindowsPerf Virtual Studio Extension (optional) {#vs2022}

WindowsPerf GUI (Graphical User Interface) is a Visual Studio 2022 extension designed to bring a seamless UI experience to WindowsPerf, the command-line performance profiling tool for Windows on Arm. It is available on the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Arm.WindowsPerfGUI).

Install by opening **Extensions** menu, click **Manage Extensions**, and click **Browse**. Type `WindowsPerf` to search for Arm WindowsPerf GUI extension. Click **Install**.

{{% notice How to set up wperf.exe path in the extension%}}
In order to set the path to the `wperf.exe` executable, go to **Tools** -> **Options** -> **WindowsPerf** -> **WindowsPerf Path** and set the absolute path to the wperf.exe executable and then click on the **Validate** button.
{{% /notice %}}

Also, visit WindowsPerf GUI project website on [GitHub](https://github.com/arm-developer-tools/windowsperf-vs-extension) for more details and latest updates.

## Install WindowsPerf VS Code Extension (optional) {#vscode}

In addition to the command-line tools, `WindowsPerf` is available on the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Arm.windowsperf).

Install by opening the **Extensions** view (Ctrl+Shift+X) and searching for `WindowsPerf`. Click **Install**.

Open **Settings** (Ctrl+,) > **Extensions** > **WindowsPerf**, and specify the path to the `wperf` executable.

{{% notice Non-Windows on Arm host%}}
You can only generate reports from a Windows on Arm device.

If using a non-Windows on Arm host, you can import and analyze `WindowsPerf` JSON reports from such devices.

You do not need to install `wperf` on non-Windows on Arm devices.
{{% /notice %}}

## Further reading

### WindowsPerf

- [WindowsPerf Release 3.7.2 blog post](https://www.linaro.org/blog/expanding-profiling-capabilities-with-windowsperf-372-release)
- [WindowsPerf Release 3.3.0 blog post](https://www.linaro.org/blog/windowsperf-release-3-3-0/)
- [WindowsPerf Release 3.0.0 blog post](https://www.linaro.org/blog/windowsperf-release-3-0-0/)
- [WindowsPerf Release 2.5.1 blog post](https://www.linaro.org/blog/windowsperf-release-2-5-1/)
- [WindowsPerf release 2.4.0 introduces the first stable version of sampling model support](https://www.linaro.org/blog/windowsperf-release-2-4-0-introduces-the-first-stable-version-of-sampling-model-support/)
- [Announcing WindowsPerf: Open-source performance analysis tool for Windows on Arm](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/announcing-windowsperf)

### WindowsPerf GUI

- [Introducing the WindowsPerf GUI: the Visual Studio 2022 extension](https://www.linaro.org/blog/introducing-the-windowsperf-gui-the-visual-studio-2022-extension/)
- [Introducing 1.0.0-beta release of WindowsPerf Visual Studio extension](https://www.linaro.org/blog/introducing-1-0-0-beta-release-of-windowsperf-visual-studio-extension/)
- [New Release: WindowsPerf Visual Studio Extension v1.0.0](https://www.linaro.org/blog/new-release-windowsperf-visual-studio-extension-v1000/)
- [Launching WindowsPerf Visual Studio Extension v2.1.0](https://www.linaro.org/blog/launching--windowsperf-visual-studio-extension-v210/)
