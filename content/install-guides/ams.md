---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Arm Performance Studio

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- Gaming
- Graphics
- Android
- profiling
- mali
- immortalis
- cortex-a
- Install Arm Mobile Studio
- Streamline
- Performance Advisor
- RenderDoc
- Frame Advisor


### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 15

author: Ronan Synnott

### Link to official documentation
official_docs: https://developer.arm.com/documentation/107649

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
test_maintenance: true
test_images:
  - ubuntu:latest
---
[Arm Performance Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio) is a performance analysis tool suite for Android and Linux application developers

It comprises of a suite of easy-to-use tools that show you how well your game or app performs on production devices, so that you can identify problems that might cause slow performance, overheat the device, or drain the battery.

| Component | Functionality |
|----------|-------------|
| [Streamline](https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer) with [Performance Advisor](https://developer.arm.com/Tools%20and%20Software/Performance%20Advisor)| Capture a performance profile that shows all the performance counter activity from the device. Generate an easy-to-read performance summary from an annotated Streamline capture, and get actionable advice about where you should optimize. |
| [Frame Advisor](https://developer.arm.com/Tools%20and%20Software/Frame%20Advisor) | Capture the API calls and rendering from a problem frame and get comprehensive geometry metrics to discover what might be slowing down your application. |
| [Mali Offline Compiler](https://developer.arm.com/Tools%20and%20Software/Mali%20Offline%20Compiler) | Analyze how efficiently your shader programs perform on a range of Mali GPUs. |
| [RenderDoc for Arm GPUs](https://developer.arm.com/Tools%20and%20Software/RenderDoc%20for%20Arm%20GPUs) | The industry-standard tool for debugging Vulkan graphics applications, including early support for Arm GPU extensions and Android features. |


All features of Arm Performance Studio are available free of charge without any additional license.

## Download Arm Performance Studio

Arm Performance Studio is supported on Windows, Linux, and macOS hosts. Download the appropriate installer from [Arm Performance Studio Downloads](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio#Downloads).

Full details about the supported OS and Android versions are given in the Arm Performance Studio [Release Notes](https://developer.arm.com/documentation/107649).

## Install Arm Performance Studio on Windows

Arm Performance Studio is provided as an installer executable. Double-click the `.exe` file and follow the instructions in the setup wizard.

Open the Performance Studio Hub from the **Windows Start** menu, or by double-clicking the shortcut in the installation directory. You can read a description of the tools and launch them from the Hub.

### Install Arm Performance Studio on macOS

Arm Performance Studio is provided as a `.dmg` package. To mount it, double-click the `.dmg` package and follow the instructions. The Arm Performance Studio directory tree is copied to the Applications directory on your local file system for easy access.

Arm recommends that you set the permissions for the installation directory to prevent other users from writing to it. This is typically achieved with the `chmod` command. For example,

```
chmod go-w <dest_dir>
```

To get started, navigate to the Arm Performance Studio installation directory in your `Applications` directory. Open the `Performance Studio.app` file to launch the **Arm Performance Studio Hub**. You can read a description of the tools and launch them from the Hub.

### Install Arm Performance Studio on Linux

Arm Performance Studio is provided as a gzipped tar archive. Extract this tar archive to your preferred location, using a recent version (1.13 or later) of GNU tar:

```
tar xvzf Arm_Performance_Studio_2025.1_linux.tgz
```

Arm recommends that you set the permissions for the installation directory to prevent other users from writing to it. This is typically achieved with the `chmod` command. For example:

```
chmod go-w <dest_dir>
```

{{% notice Tip %}}
You might find it useful to edit your `PATH` environment variable to add the paths to the `Streamline-cli` and `malioc` executables so that you can run them from any directory. Add the following commands to the .bashrc file in your home directory, so that they are set whenever you initialize a shell session:

```
PATH=$PATH:/<installation_directory>/streamline
PATH=$PATH:/<installation_directory>/mali_offline_compiler
```

{{% /notice %}}

Inside the installation directory is a shortcut called **Performance Studio**. Double-click on the shortcut to launch the Performance Studio Hub. You can read a description of the tools and launch them from the Hub.

Alternatively, to open Streamline, Frame Advisor or RenderDoc for Arm GPUs directly, go to the installation directory, open the folder for the tool you want to open and run the application file. For example:

```
cd <installation_directory>/streamline
./Streamline
```

## How do I get started with Arm Performance Studio?

See the [Get started with Arm Performance Studio](/learning-paths/mobile-graphics-and-gaming/ams/) learning path for an overview of how to run each tool in Arm Performance Studio.
