---
# User change
title: Set up Arm Performance Studio 

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## What is Arm Performance Studio?

[Arm Performance Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio) is a performance analysis tool suite for developers to performance test their applications on devices with Mali-based GPUs. It consists of four easy-to-use tools that show you how well your application performs either on off-the-shelf Android devices, or Linux targets. The tools help you to identify problems that might slow down performance, overheat the device, or drain the battery.

| Component | Functionality |
|----------|-------------|
| [Streamline](https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer) with [Performance Advisor](https://developer.arm.com/Tools%20and%20Software/Performance%20Advisor) | Capture a performance profile that shows all the performance counter activity from the device. Generate an easy-to-read performance summary from an annotated Streamline capture, and get actionable advice about where you should optimize. |
| [Frame Advisor](https://developer.arm.com/Tools%20and%20Software/Frame%20Advisor) | Capture the API calls and rendering from a problem frame and get comprehensive geometry metrics to discover what might be slowing down your application. |
| [Mali Offline Compiler](https://developer.arm.com/Tools%20and%20Software/Mali%20Offline%20Compiler) | Analyze how efficiently your shader programs perform on a range of Mali GPUs. |
| [RenderDoc for Arm GPUs](https://developer.arm.com/Tools%20and%20Software/RenderDoc%20for%20Arm%20GPUs) | The industry-standard tool for debugging Vulkan graphics applications, including early support for Arm GPU extensions and Android features. |

## Download and install Arm Performance Studio

Arm Performance Studio is supported on Windows, Linux, and macOS hosts. To download Arm Performance Studio, see the [Arm Performance Studio downloads page](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio#Downloads).

For installation instructions, see the [Arm Performance Studio install guide](/install-guides/ams/).

## Update your PATH environment variable (Linux and macOS)

Edit your `PATH` environment variable to add the paths to the Streamline and Mali Offline Compiler executables. This is so that you can run Streamline's `Streamline-cli -pa` command and Mali Offline Compiler's `malioc` command from any directory. This step is not necessary on Windows, as this is done automatically when Arm Performance Studio is installed.

On macOS, edit your `/etc/paths` file to add the following paths:

```
/<installation_directory>/streamline
/<installation_directory>/mali_offline_compiler
```

On Linux, edit your `PATH` environment variable to add the paths to the Performance Advisor executable. Add this command to the `.bashrc` file in your home directory, so that this environment variable is set whenever you initialize a shell session.

```
 PATH=$PATH:/<installation_directory>/streamline
 PATH=$PATH:/<installation_directory>/mali_offline_compiler
```

## Launch the tools

To open the tools, launch the Performance Studio Hub:

- On Windows, search for Performance Studio.
- On macOS and Linux, open the Performance Studio application file from the install directory.

![Performance Studio Hub](images/ps_hub.png)

## What you've accomplished and what's next

You've now set up Arm Performance Studio and updated your PATH environment variable so you can use suite of available tools to profile applications. 

Next, you'll set up the application that you'll profile in this Learning Path.