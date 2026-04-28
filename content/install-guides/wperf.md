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

WindowsPerf is a Linux Perf-inspired performance profiling tool for Windows on Arm. Profiling is based on the Arm AArch64 PMU and its hardware counters. WindowsPerf supports the counting model for obtaining aggregate counts of occurrences of PMU events, and the sampling model for determining the frequencies of event occurrences produced by program locations at the function, basic block, and instruction levels.  WindowsPerf is an open-source project hosted on [GitLab](https://gitlab.com/Linaro/WindowsPerf/windowsperf/).

WindowsPerf consists of a kernel-mode driver and a user-space command-line tool. You can seamlessly integrate the WindowsPerf command line tool with both the [WindowsPerf Visual Studio Extension](#vs2022) and the [WindowsPerf VS Code Extension](#vscode). These extensions, which you can download from the Visual Studio Marketplace, enhance the functionality of WindowsPerf by providing a user-friendly interface, and additional features for performance analysis and debugging. This integration allows developers to efficiently analyze and optimize their applications directly within their preferred development environment.

{{% notice  Note%}}
You can't use WindowsPerf on virtual machines, such as cloud instances.
{{% /notice %}}

## Install WindowsPerf using winget

You can now install WindowsPerf directly from [winget](https://learn.microsoft.com/en-us/windows/package-manager/). Open an `Administrator` terminal on PowerShell and run:

```console
winget install WindowsPerf
```

The output is similar to:

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

![Animated terminal output showing winget installing WindowsPerf, including package download, hash verification, and Successfully installed status to confirm installation completion.#center](/install-guides/_images/wperf-winget-installation.gif)

The command will install the latest available WindowsPerf along with the [WPA plugins](/learning-paths/laptops-and-desktops/windowsperf_wpa_plugin/). To check that the installation was successful, open a new terminal tab or window and follow the instructions under the [verify installation section](/install-guides/wperf/#verify-install).

### Uninstall WindowsPerf using winget

If you need to uninstall WindowsPerf, open an `Administrator` terminal on PowerShell and run:

```console
winget uninstall WindowsPerf
```

The output from a successful uninstallation is similar to:

```output
Found WindowsPerf [Arm.WindowsPerf]
Starting package uninstall...
Successfully uninstalled
```

{{% notice  Note%}}
WinPerf is an open-source project. If you'd like to develop WindowsPerf yourself, you may also need to install the Windows Driver Kit (WDK). For more information, see [WDK release notes](https://learn.microsoft.com/en-us/windows-hardware/drivers/wdk-release-notes).
{{% /notice %}}

## Verify that WindowsPerf is installed correctly {#verify-install}

You can check everything is working by running the `wperf` executable.

{{% notice  Note%}}
After you've installed the driver, you can use `wperf` without `Administrator` privileges.
{{% /notice %}}

For example:

```command
wperf --version
```

The output is similar to:

```output
        Component     Version  GitVer    FeatureString
        =========     =======  ======    =============
        wperf         4.0.0    b18197bd  +etw-app
        wperf-driver  4.0.0    b18197bd  +etw-drv

```

## Install the WindowsPerf Virtual Studio Extension? {#vs2022}

WindowsPerf GUI (Graphical User Interface) is a Visual Studio 2022 extension designed to bring a seamless UI experience to WindowsPerf, the command-line performance profiling tool for Windows on Arm. It is available on the [Visual Studio Marketplace](https://marketplace.visualstudio.com/).

To install the extension:

1. Open the **Extensions** menu in Visual Studio.
2. Select **Manage Extensions**, then select **Browse**.
3. Search for `WindowsPerf`.
4. Select **Install** for the Arm WindowsPerf GUI extension.

{{% notice How to set up wperf.exe path in the extension%}}
To set the path to the `wperf.exe` executable, go to **Tools** -> **Options** -> **WindowsPerf** -> **WindowsPerf Path** and set the absolute path to the wperf.exe executable and then click on the **Validate** button.
{{% /notice %}}

Also, for more details and latest updates, see the WindowsPerf GUI project website on [GitLab](https://gitlab.com/Linaro/WindowsPerf/vs-extension).

## Install the WindowsPerf VS Code Extension {#vscode}

In addition to the command-line tools, `WindowsPerf` is available on the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Arm.windowsperf).

To install and configure the extension:

1. Open the **Extensions** view in VS Code using **Ctrl+Shift+X**.
2. Search for `WindowsPerf`.
3. Select **Install**.
4. Open **Settings** using **Ctrl+,**.
5. Go to **Extensions** > **WindowsPerf**.
6. Set the path to the `wperf` executable.

{{% notice Non-Windows on Arm host%}}
You can generate reports only from a Windows on Arm device.

If you're using a non-Windows on Arm host, you can import and analyze `WindowsPerf` JSON reports from such devices.

You don't need to install `wperf` on non-Windows on Arm devices.
{{% /notice %}}

## Related resources 

You're now ready to use WindowsPerf. For more information about WindowsPerf, see the following links:

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
