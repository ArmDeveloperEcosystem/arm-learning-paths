---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Perf for Windows on Arm (WindowsPerf)

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

WindowsPerf is an open-source command line tool for performance analysis on Windows on Arm devices.

WindowsPerf consists of a kernel-mode driver and a user-space command-line tool, or [VS Code Extension](#vscode). The command-line tool is modeled after the Linux `perf` command. 

WindowsPerf includes a **counting model** for counting events such as cycles, instructions, and cache events and a **sampling model** to understand how frequently events occur.

{{% notice  Virtual Machines%}}
WindowsPerf cannot be used on virtual machines, such as cloud instances.
{{% /notice %}}

You can interact with the 

## Visual Studio and the Windows Driver Kit (WDK)

WindowsPerf relies on `dll` files installed with Visual Studio (Community Edition or higher) and (optionally) installers from the Windows Driver Kit extension.

[Download the Windows Driver Kit (WDK)](https://learn.microsoft.com/en-us/windows-hardware/drivers/download-the-wdk) explains the WDK installation process.

See also the [Visual Studio for Windows on Arm install guide](/install-guides/vs-woa/).

## Download WindowsPerf

The latest release package `windowsperf-bin-<version>.zip` can be downloaded from the Linaro GitLab repository:
```url
https://gitlab.com/Linaro/WindowsPerf/windowsperf/-/releases
```
To download directly from command prompt, use:

```console
mkdir windowsperf-bin-3.8.0
cd windowsperf-bin-3.8.0
curl https://gitlab.com/api/v4/projects/40381146/packages/generic/windowsperf/3.8.0/windowsperf-bin-3.8.0.zip --output windowsperf-bin-3.8.0.zip
```

Unzip the package:

```console
tar -xmf windowsperf-bin-3.8.0.zip
```

## Install VS Code Extension (optional) {#vscode}

In addition to the command-line tools, `WindowsPerf` is available on the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=Arm.windowsperf).

Install by opening the `Extensions` view (`Ctrl`+`Shift`+`X`) and searching for `WindowsPerf`.　Click `Install`.

Open `Settings` (`Ctrl`+`,`) > `Extensions` > `WindowsPerf`, and specify the path to the `wperf` executable.

{{% notice Non-Windows on Arm host%}}
You can only generate reports from a Windows on Arm device.

If using a non-Windows on Arm host, you can import and analyze `WindowsPerf` JSON reports from such devices.

You do not need to install `wperf` on non-Windows on Arm devices.
{{% /notice %}}


## Install wperf driver

You can install the kernel driver using either the Visual Studio [devcon](#devcon_install) utility or the supplied [installer](#devgen_install).

{{% notice  Note%}}
You must install the driver as `Administrator`.
{{% /notice %}}

Open a `Windows Command Prompt` terminal with `Run as administrator` enabled.

Navigate to the `windowsperf-bin-<version>` directory.
```command
cd windowsperf-bin-3.8.0
```

### Install with devcon {#devcon_install}

Navigate into the `wperf-driver` folder, and use `devcon` to install the driver:

```command
cd wperf-driver
devcon install wperf-driver.inf Root\WPERFDRIVER
```
You will see output similar to:

```output
Device node created. Install is complete when drivers are installed...
Updating drivers for Root\WPERFDRIVER from <path>\wperf-driver.inf.
Drivers installed successfully.
```

### Install with wperf-devgen {#devgen_install}

Navigate to the `wperf-driver` folder and run the installer:
```command
cd wperf-driver
wperf-devgen install
```
You will see output similar to:
```output
Executing command: install.
Install requested.
Waiting for device creation...
Device installed successfully.
Trying to install driver...
Success installing driver.
```
## Verify install

You can check everything is working by running the `wperf` executable.

{{% notice  Note%}}
Once the above driver is installed, you can use `wperf` without `Administrator` privileges.
{{% /notice %}}

For example:
```command
cd ..
wperf --version
```
You should see output similar to:
```output
        Component     Version  GitVer    FeatureString
        =========     =======  ======    =============
        wperf         3.8.0    6d15ddfc  +etw-app
        wperf-driver  3.8.0    6d15ddfc  +etw-drv

```

## Uninstall wperf driver

You can uninstall (aka "remove") the kernel driver using either the Visual Studio [devcon](#devcon_uninstall) utility or the supplied [installer](#devgen_uninstall).

{{% notice  Note%}}
You must uninstall the driver as `Administrator`.
{{% /notice %}}

### Uninstall with devcon {#devcon_uninstall}

Below command removes the device from the device tree and deletes the device stack for the device. As a result of these actions, child devices are removed from the device tree and the drivers that support the device are unloaded. See [DevCon Remove](https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/devcon-remove) article for more details.

```command
devcon remove wperf-driver.inf Root\WPERFDRIVER
```
You should see output similar to:
```output
ROOT\SYSTEM\0001                                            : Removed
1 device(s) were removed.
```

### Uninstall with wperf-devgen {#devgen_uninstall}

```command
wperf-devgen uninstall
```
You should see output similar to:
```console
Executing command: uninstall.
Uninstall requested.
Waiting for device creation...
Device uninstalled successfully.
Trying to remove driver <path>\wperf-driver.inf.
Driver removed successfully.
```

## Further reading

[Announcing WindowsPerf: Open-source performance analysis tool for Windows on Arm](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/announcing-windowsperf)
