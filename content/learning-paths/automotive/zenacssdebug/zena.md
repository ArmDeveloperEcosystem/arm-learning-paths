---
# User change
title: "Getting started"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Arm Zena Compute Subsystem

The Arm Zena Compute Subsystem (CSS) consists of a high-performance Arm Cortex-A720AE application processor system (primary compute), augmented with an Arm Cortex-R82AE–based Safety Island (SI) and a real-time domain to host additional system-safety monitoring and real-time services.

The system also includes a Runtime Security Engine (RSE), which is used for secure boot of the system elements and to provide runtime secure services.

The Arm Zena CSS Reference Software Stack provides an open-source, integrated solution running on a Fixed Virtual Platform (FVP). Both the reference software stack and the FVP are freely available.

For more information, see [Arm Zena Compute Subsystem (CSS)](https://developer.arm.com/Compute%20Subsystems/Arm%20Zena%20Compute%20Subsystem).

## Build the software stack

Follow the steps to download and build the software stack in the [Arm Automotive Solutions Software Reference Stack User Guide](https://arm-auto-solutions.docs.arm.com/en/latest/rd-aspen/user_guide/reproduce.html).

The default **Cfg1, Arm Automotive Solutions Demo, Bare Metal** build is used in this learning path.

Software build will usually take at least one hour to complete, depending on host machine.

{{% notice Note %}}
The primary focus of this Learning Path is to demonstrate how to debug the software stack.

The latest version of software tested at time of writing is `2.1`. Screenshots show previous versions.
{{% /notice %}}

## Verify the build and execution

After you build the software stack, verify that it runs successfully:

```bash
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose"
```

The system runs through the boot process until a Linux prompt is available (in `terminal_ns_uart0`).

Press **Ctrl+C** in the command terminal (use `Ctrl+B` > `0` to swap to that terminal) to terminate the process.

## Install FVP (optional)

The FVP is downloaded and installed as part of the build process.

You can also separately download either `Arm-Zena-CSS-FVP` (`Cfg1` or `Cfg2`) from the Arm Developer [website](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms/Automotive%20FVPs).

See also the Arm Ecosystem FVPs and Architecture Envelope Models [Install Guide](/install-guides/fm_fvp/eco_fvp/).

{{% notice Note %}}
For legacy reasons, the FVP was previously named `FVP_RD_Aspen`.
{{% /notice %}}

## Arm Development Studio

Arm Development Studio is a software development environment with multicore debug support for Arm CPUs. It provides early support for the latest processors and works seamlessly with FVPs.

The CPUs implemented within Arm Zena CSS are supported by Arm Development Studio 2024.0 and later; however, 2024.1 or later is recommended for Linux OS debug support. At the time of writing, the latest version is 2025.0, which is used for this Learning Path.

For more information, see [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio).

Arm Development Studio is a commercial, license-managed product. For installation and setup instructions, see the [Arm Development Studio Install Guide](/install-guides/armds/).

Launch the IDE and create a new workspace folder.

If you’re prompted by the launcher (this prompt is disabled by default), create a new folder there. 

Otherwise, select **File** > **Switch Workspace** > **Other**.

{{% notice Note %}}
To enable the workspace prompt, go to **Window** > **Preferences** > **General** > **Startup and Shutdown** > **Workspaces**, and enable **Prompt for workspace on startup**.
{{% /notice %}}
