---
# User change
title: "Debug Connections"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Debug Connections

You are now ready to create debug connections for each of the sub-systems within Zena CSS. This section will create the connections, which will be subsequently enhanced in the following section. You may prefer to fully set up one such connection before moving to others.

Development Studio has full support for Heterogeneous systems such as Zena CSS, and so you can connect to all processors simultaneously.

### Debug connection project

It may be sensible to create a project to store these connections (`.launch` files) in.

Select `File` > `New...` > `Project` > `General` > `Project`, and give it a meaningful name (`Connections`).

### RSE (Cortex-M55)

Runtime Security Engine (RSE) is based on [Cortex-M55](https://developer.arm.com/Processors/Cortex-M55) core and is a security subsystem fulfilling the role of Root of Trust.

Select `File` > `New` > `Model Connection`.

{{% notice Note %}}
You can also use `File` > `New` > `Other` > `Arm Debugger` > `Model Connection`, or

`Create a debug connection...` shortcut in the `Debug Control` pane.
{{% /notice %}}

Specify a connection name (`RSE`), and associate with the above `Connections` project. Click `Next`.

Locate the FVP based on the name you gave it previously (`Zena_CSS_FVP`). The text filter can help locate easily.

You will then be presented with the `Edit configuration` pane. In the `Connection` tab, scroll down to locate `Bare Metal Debug` > `Arm_Cortex-M55`.

As we shall be later launching the FVP with the software stack loaded, select `Connect to an already running model`.

Assuming the same host will be running both the FVP and the debugger, specify the `Connection address` as the default `127.0.0.1:7100`.

{{% notice Note %}}
`127.0.0.1` is the same as `localhost`, that is the same host machine as is running the FVP.

It is also possible to connect to a remote host by specifying appropriate IP address, and launching FVP with the `-A` option.

`7100` is the default port number. You may need to change this if necessary.
{{% /notice %}}

Click `Apply` to save the connection information, and `Close`. Observe that `RSE.launch` is created inside the `Connections` project.

### Safety Island (Cortex-R82AE)

The Safety Island is a subsystem based on [Cortex-R82AE](https://developer.arm.com/Processors/Cortex-R82AE) core. The software running on the Safety Island is responsible for power, clock and CMN control.

The procedure to create this connection is very similar to the above, other than to select `Bare Metal Debug` > `Arm_Cortex-R82AE` from the pull down.

{{% notice %}}
For convenience you can copy-and-paste `RSE.launch` as `SI.launch` and simply modify the CPU.
{{% /notice %}}

### Primary Compute (Cortex-A720AE)

The Primary Compute consists of four processor clusters to run a rich OS such as Linux. Each processor cluster includes four [Cortex-A720AE](https://developer.arm.com/Processors/Cortex-A720AE) cores and a [DSU-120AE](https://developer.arm.com/Processors/DSU-120AE) DynamIQ Shared Unit.

The application processors will be debugged in an SMP configuration with Linux Kernel awareness.

As above, create `Primary_init.launch` connection and scroll to `Bare Metal Debug` > `ARM_Cortex-A720AE_0`. This will connect to just CPU0, leaving the other CPUs free to run.

To debug the Linux kernel we can make use of the [OS awareness](https://developer.arm.com/documentation/101470/latest/Debugging-Embedded-Systems/About-OS-awareness) feature of the Arm Debugger.

Create `Primary_Linux.launch` connection and scroll to `Linux Kernel Debug` > `ARM_Cortex-A720AEx16 SMP Cluster 1`. This will connect to all 16 `Cortex-A720AE` processors present in the FVP, though only cores 0-3 are used.
