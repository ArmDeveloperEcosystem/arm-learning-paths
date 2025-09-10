---
# User change
title: "Getting started"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Arm Zena Compute Subsystem

The Arm Zena Compute Subsystem (CSS) consists of a high-performance Arm Cortex-A720AE Application Processor (Primary Compute) system augmented with an Arm Cortex-R82AE based Safety Island (SI) and real-time domain to host additional system safety monitoring and real-time services.

The system additionally includes a Runtime Security Engine (RSE) used for the secure boot of the system elements and the runtime secure services.

The Arm Zena CSS software stack provides an open-source, integrated solution running on a Fixed Virtual Platform (FVP).

The reference software stack and the FVP are freely available.

For more information, see [Arm Zena Compute Subsystem (CSS)](https://developer.arm.com/Compute%20Subsystems/Arm%20Zena%20Compute%20Subsystem) and associated links.

## Build software stack

Follow the steps to download and build the software stack in the [User Guide](https://arm-auto-solutions.docs.arm.com/en/v2.0/rd-aspen/user_guide/reproduce.html).

The default `Arm Automotive Solutions Demo` build is used.

{{% notice Note %}}
The focus of this Learning Path is to demonstrate the **debug** of the software stack.
{{% /notice %}}

## Verify correct build and execution

Once the software stack has been built, you can verify that it runs successfully with the command:

``` command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose"
```

The system will run through the boot process until a Linux prompt is available (in `terminal_ns_uart0`).

Use `Ctrl+C` on the command terminal to terminate.

## Install FVP (optional)

The FVP is downloaded and installed as part of the build process above.

The `Arm-Zena-CSS-FVP` can also be independently downloaded from the Arm Developer [website](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms/Automotive%20FVPs).

See also the Arm Ecosystem FVPs and Architecture Envelope Models [Install Guide](/install-guides/fm_fvp/eco_fvp/).

{{% notice Note %}}
For legacy reasons the FVP is named is `FVP_RD_Aspen`.
{{% /notice %}}

# Arm Development Studio

Arm Development Studio is a software development solution with support of multicore debug for Arm CPUs. It provides the earliest support for the latest processors.

The CPUs implemented within Arm Zena CSS are supported by Arm Development Studio 2024.0 and later, though 2024.1 or later is recommended for appropriate Linux OS support. At time of writing the latest version available is 2025.0, and that is the version used for this learning path.

For more information see [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio).

Arm Development Studio is a commercial, license managed, product. For installation and set up instructions, see this [Install Guide](/install-guides/armds/).

Launch the IDE. It is recommended to create a new workspace folder.

If prompted by the launcher (this is disabled by default) create a new folder there, else select `File` > `Switch Workspace` > `Other...`.

{{% notice Note %}}
To enable this prompt by default, navigate to `Window` > `Preferences` > `General` > `Startup and Shutdown` > `Workspaces`, and enable `Prompt for workspace on startup`.
{{% /notice %}}
