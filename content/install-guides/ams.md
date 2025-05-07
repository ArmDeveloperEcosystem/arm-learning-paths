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
[Arm Performance Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio) is a performance analysis tool suite for Android and Linux application developers.

It helps analyze how your game or app performs on production devices, so you can identify issues that affect performance, cause overheating, or drain battery life.

The following table lists the tools and describes their functions:

| Component | Functionality |
|----------|-------------|
| [Streamline](https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer) | Captures a performance profile with hardware counter activity from the device. |
| [Performance Advisor](https://developer.arm.com/Tools%20and%20Software/Performance%20Advisor) | Generates an easy-to-read performance summary from an annotated Streamline capture, and provides actionable optimization suggestions. |
| [Frame Advisor](https://developer.arm.com/Tools%20and%20Software/Frame%20Advisor) | Captures API calls and rendering details from a specific frame and provides detailed geometry metrics to help identify rendering bottlenecks. |
| [Mali Offline Compiler](https://developer.arm.com/Tools%20and%20Software/Mali%20Offline%20Compiler) | Analyzes how efficiently your shader programs perform on a range of Mali GPUs. |
| [RenderDoc for Arm GPUs](https://developer.arm.com/Tools%20and%20Software/RenderDoc%20for%20Arm%20GPUs) | Debugs Vulkan graphics applications with support for Arm GPU extensions and Android features. |


All features of Arm Performance Studio are available free of charge without a license.

## How do I install Arm Performance Studio?

Arm Performance Studio is supported on Windows, Linux, and macOS hosts. Download the appropriate installer from [Arm Performance Studio Downloads](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio#Downloads).

Full details about the supported OS and Android versions are given in the Arm Performance Studio [Release Notes](https://developer.arm.com/documentation/107649).

### How do I install Arm Performance Studio on Windows?

Run the downloaded `Arm_Performance_Studio_<version>_windows_x86-64.exe` installer, and follow the on-screen instructions.

To open Streamline, Frame Advisor, or RenderDoc for Arm GPUs, go to the Windows **Start** menu and search for the name of the tool you want to open.

Performance Advisor is a feature of the Streamline command-line application. To generate a performance report, you must first run the provided Python script to enable Streamline to collect frame data from the device. [Get started with Performance Advisor tutorial](https://developer.arm.com/documentation/102478/latest) describes this process in detail. After you have captured a profile with Streamline, run `Streamline-cli` on the Streamline capture file. This command is added to your `PATH` environment variable during installation, so it can be used from anywhere.

```console
Streamline-cli.exe -pa <options> my_capture.apc
```

To run Mali Offline Compiler, open a command terminal, navigate to your work directory, and run the `malioc` command on a shader program. The malioc command is added to your `PATH` environment variable during installation, so it can be used from anywhere.

```console
malioc.exe <options> my_shader.frag
```

### How do I install Arm Performance Studio on macOS?

Arm Performance Studio is provided as a `.dmg` package. To mount it, double-click the `.dmg` package and follow the instructions. The Arm Performance Studio directory tree is copied to the Applications directory on your local file system for easy access.

You can remove write permission from the installation directory to prevent other users from writing to it. This is done with the `chmod` command. For example:

```
chmod go-w <dest_dir>
```

Open Streamline, Frame Advisor or RenderDoc for Arm GPUs directly from the Arm Performance Studio directory in your Applications directory. For example, to open Streamline, go to the `<installation_directory>/streamline` directory and open the `Streamline.app` file.

To run Performance Advisor, go to the `<installation_directory>/streamline` directory, and double-click the `Streamline-cli-launcher` file. Your computer will ask you to allow Streamline to control the Terminal application. Allow this. The Performance Advisor launcher opens the Terminal application and updates your `PATH` environment variable so you can run Performance Advisor from any directory.

Performance Advisor is a feature of the Streamline command-line application. To generate a performance report, you must first run the provided Python script to enable Streamline to collect frame data from the device. This process is described in detail in the [Get started with Performance Advisor tutorial](https://developer.arm.com/documentation/102478/latest). After you have captured a profile with Streamline, run the `Streamline-cli` command on the Streamline capture file to generate a performance report:

```
Streamline-cli -pa <options> my_capture.apc
```

To run Mali Offline Compiler, go to the `<installation_directory>/mali_offline_compiler` directory, and double-click the `mali_offline_compiler_launcher` file. The Mali Offline Compiler launcher opens the Terminal application and updates your `PATH` environment variable so you can run the `malioc` command from any directory. To generate a shader analysis report, run the `malioc` command on a shader program:

```
malioc <options> my_shader.frag
```

On some versions of macOS, you might see a message that Mali Offline Compiler is not recognized as an application from an identified developer. To enable Mali Offline Compiler, cancel this message, then open **System Preferences > Security & Privacy** and select **Allow Anyway** for the `malioc` application.

### How do I install Arm Performance Studio on Linux?

Arm Performance Studio is provided as a gzipped tar archive. Extract this tar archive to your preferred location, using version 1.13 or later of GNU tar:

```
tar xvzf Arm_Performance_Studio_<version>_linux.tgz
```

You can remove write permission from the installation directory to prevent other users from writing to it. This is done with the `chmod` command. For example:

```
chmod go-w <dest_dir>
```

You might find it useful to edit your `PATH` environment variable to add the paths to the `Streamline-cli` and `malioc` executables so that you can run them from any directory. Add the following commands to the .bashrc file in your home directory, so that they are set whenever you initialize a shell session:

```
PATH=$PATH:<installation_directory>/streamline
PATH=$PATH:<installation_directory>/mali_offline_compiler
```

## How do I get started with Arm Performance Studio?

Refer to [Get started with Arm Performance Studio](/learning-paths/mobile-graphics-and-gaming/ams/) for an overview of how to run each tool in Arm Performance Studio.
