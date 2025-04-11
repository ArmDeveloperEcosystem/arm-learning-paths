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
| [Streamline](https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer) | Capture a performance profile that shows all the performance counter activity from the device. |
| [Performance Advisor](https://developer.arm.com/Tools%20and%20Software/Performance%20Advisor) | Generate an easy-to-read performance summary from an annotated Streamline capture, and get actionable advice about where you should optimize. |
| [Frame Advisor](https://developer.arm.com/Tools%20and%20Software/Frame%20Advisor) | Capture the API calls and rendering from a problem frame and get comprehensive geometry metrics to discover what might be slowing down your application. |
| [Mali Offline Compiler](https://developer.arm.com/Tools%20and%20Software/Mali%20Offline%20Compiler) | Analyze how efficiently your shader programs perform on a range of Mali GPUs. |
| [RenderDoc for Arm GPUs](https://developer.arm.com/Tools%20and%20Software/RenderDoc%20for%20Arm%20GPUs) | The industry-standard tool for debugging Vulkan graphics applications, including early support for Arm GPU extensions and Android features. |


All features of Arm Performance Studio are available free of charge without any additional license.

## Installation

Arm Performance Studio is supported on Windows, Linux, and macOS hosts. Download the appropriate installer from [Arm Performance Studio Downloads](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio#Downloads).

Full details about the supported OS and Android versions are given in the Arm Performance Studio [Release Notes](https://developer.arm.com/documentation/107649).

### Windows

Run the supplied `Arm_Performance_Studio_<version>_windows_x86-64.exe` installer, and follow the on-screen instructions.

To open Streamline, Frame Advisor or RenderDoc for Arm GPUs, go to the Windows Start menu and search for the name of the tool you want to open.

Performance Advisor is a feature of the Streamline command-line application. To generate a performance report, you must first run the provided Python script to enable Streamline to collect frame data from the device. This process is described in detail in the [Get started with Performance Advisor tutorial](https://developer.arm.com/documentation/102478/latest). After you have captured a profile with Streamline, run the `Streamline-cli -pa` command on the Streamline capture file. This command is added to your `PATH` environment variable during installation, so it can be used from anywhere.

  ```console
  Streamline-cli.exe -pa <options> my_capture.apc
  ```

To run Mali Offline Compiler, open a command terminal, navigate to your work directory, and run the `malioc` command on a shader program. The malioc command is added to your `PATH` environment variable during installation, so can be used from anywhere

  ```console
  malioc.exe <options> my_shader.frag
  ```

### macOS

Arm Performance Studio is provided as a `.dmg` package. To mount it, double-click the `.dmg` package and follow the instructions. The Arm Performance Studio directory tree is copied to the Applications directory on your local file system for easy access.

Arm recommends that you set the permissions for the installation directory to prevent other users from writing to it. This is typically achieved with the `chmod` command. For example,

```
chmod go-w <dest_dir>
```

Open Streamline, Frame Advisor or RenderDoc for Arm GPUs directly from the Arm Performance Studio directory in your Applications directory. For example, to open Streamline, go to the `<installation_directory>/streamline directory` and open the `Streamline.app` file.

To run Performance Advisor, go to the `<installation_directory>/streamline` directory, and double-click the `Streamline-cli-launcher` file. Your computer will ask you to allow Streamline to control the Terminal application. Allow this. The Performance Advisor launcher opens the Terminal application and updates your `PATH` environment variable so you can run Performance Advisor from any directory.

Performance Advisor is a feature of the Streamline command-line application. To generate a performance report, you must first run the provided Python script to enable Streamline to collect frame data from the device. This process is described in detail in the [Get started with Performance Advisor tutorial](https://developer.arm.com/documentation/102478/latest) tutorial. After you have captured a profile with Streamline, run the `Streamline-cli -pa` command on the Streamline capture file to generate a performance report:

```
Streamline-cli -pa <options> my_capture.apc
```

To run Mali Offline Compiler, go to the `<installation_directory>/mali_offline_compiler` directory, and double-click the `mali_offline_compiler_launcher` file. The Mali Offline Compiler launcher opens the Terminal application and updates your `PATH` environment variable so you can run the `malioc` command from any directory. To generate a shader analysis report, run the `malioc` command on a shader program:

```
malioc <options> my_shader.frag
```

On some versions of macOS, you might see a message that Mali Offline Compiler is not recognized as an application from an identified developer. To enable Mali Offline Compiler, cancel this message, then open **System Preferences > Security and Privacy** and select **Allow Anyway** for the `malioc` application.

### Linux

Arm Performance Studio is provided as a gzipped tar archive. Extract this tar archive to your preferred location, using a recent version (1.13 or later) of GNU tar:

```
tar xvzf Arm_Performance_Studio_2025.1_linux.tgz
```

Arm recommends that you set the permissions for the installation directory to prevent other users from writing to it. This is typically achieved with the `chmod` command. For example:

```
chmod go-w <dest_dir>
```

You might find it useful to edit your `PATH` environment variable to add the paths to the `Streamline-cli` and `malioc` executables so that you can run them from any directory. Add the following commands to the .bashrc file in your home directory, so that they are set whenever you initialize a shell session:

```
PATH=$PATH:/<installation_directory>/streamline
PATH=$PATH:/<installation_directory>/mali_offline_compiler
```

To open Streamline, Frame Advisor or RenderDoc for Arm GPUs, go to the installation directory, open the folder for the tool you want to open  and run the application file. For example:

```
cd <installation_directory>/streamline
./Streamline
```

Performance Advisor is a feature of the Streamline command-line application. To use it to generate a performance report, you must first run the provided Python script to enable Streamline to collect frame data from the device. This process is described in detail in the Get started with Performance Advisor tutorial. After you have captured a profile with Streamline, go to the `installation_directory>/streamline` directory and run the `Streamline-cli -pa` command on the Streamline capture file to generate a performance report:

```
cd <installation_directory>/performance_advisor
./Streamline-cli -pa <options> my_capture.apc
```

To run Mali Offline Compiler, go to the `installation_directory>/mali_offline_compiler` directory and run the `malioc` command on a shader program:

```
cd <installation_directory>/mali_offline_compiler
./malioc <options> my_shader.frag
```

## Get started

See the [Get started with Arm Performance Studio](/learning-paths/mobile-graphics-and-gaming/ams/) learning path for an overview of how to run each tool in Arm Performance Studio.
