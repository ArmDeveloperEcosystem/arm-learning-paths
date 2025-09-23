---
# User change
title: "Create debug connections"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Debug Connections

You are now ready to create debug connections for each of the sub-systems within Zena CSS. In this section you will create the connections, which will be subsequently enhanced in the following section. You may prefer to fully set up one such connection before moving to others.

Arm Development Studio has full support for heterogeneous systems such as Zena CSS, and so you can connect to all processors simultaneously.

## Create a project for connection files

First, create a project to store these connections (`.launch` files).

Select **File** > **New...** > **Project** > **General** > **Project**, and give it a meaningful name (for example, `Connections`).

## Create an RSE (Cortex-M55) model connection

Runtime Security Engine (RSE) is based on the [Cortex-M55](https://developer.arm.com/Processors/Cortex-M55) core and is a security subsystem fulfilling the role of Root of Trust.

Select **File** > **New** > **Model Connection**.

{{% notice Note %}}
You can also use **File** > **New** > **Other** > **Arm Debugger** > **Model Connection**, or the **Create a debug connection**... shortcut in the **Debug Control** pane.
{{% /notice %}}

Specify a connection name (`RSE`), and associate with the above `Connections` project. Click **Next**.

Locate the FVP based on the name you gave it previously (`Zena_CSS_FVP`). You can use the text filter to locate it quickly.

You will then be presented with the **Edit configuration** pane. In the **Connection** tab, scroll down to locate **Bare Metal Debug** > **Arm_Cortex-M55**.

As you will be later launching the FVP with the software stack loaded, select **Connect to an already running model**.

Assuming the same host will be running both the FVP and the debugger, specify the **Connection address** as the default `127.0.0.1:7100`.

{{% notice Note %}}
`127.0.0.1` is the same as `localhost`, which targets the host running the FVP. For a remote FVP, specify the remote IP address and start the FVP with `-A`. Port `7100` is the default Iris port and can be adjusted if needed.
{{% /notice %}}

Arm Development Studio creates `RSE.launch` inside the **Connections** project.

## Create a Safety Island (Cortex-R82AE) model connection

The Safety Island is based on the [Cortex-R82AE](https://developer.arm.com/Processors/Cortex-R82AE) core and manages power, clocks, and CMN control.

Follow the same steps as for RSE, with this change:

In **Edit configuration**, expand **Bare Metal Debug** and select **Arm_Cortex-R82AE**.

{{% notice Tip %}}
To save time, copy `RSE.launch` to `SI.launch` and update the CPU selection to **Arm_Cortex-R82AE**.
{{% /notice %}}

## Create Primary compute (Cortex-A720AE) connections

Primary compute comprises four clusters intended to run a rich OS such as Linux. Each cluster has four [Cortex-A720AE](https://developer.arm.com/Processors/Cortex-A720AE) cores alongside a [DSU-120AE](https://developer.arm.com/Processors/DSU-120AE) DynamIQ Shared Unit.

You will create two connections: one for bare-metal initialization and one with Linux kernel awareness for SMP debug.

### Primary init (bare metal, CPU0 only)

Create `Primary_init.launch`:

- Select **File > New > Model Connection**.
- Select your `Zena_CSS_FVP` model.
- In **Edit configuration**, expand **Bare Metal Debug** and select **ARM_Cortex-A720AE_0** to attach to CPU0 only. This leaves other CPUs running.

### Primary Linux (SMP, OS awareness)

Create **Primary_Linux.launch** for Linux kernel debug with OS awareness:

- Use **File > New > Model Connection**.
- Select your **Zena_CSS_FVP** model.
- In **Edit configuration**, expand **Linux Kernel Debug** and choose **ARM_Cortex-A720AEx16 SMP Cluster 1**.  
  This connects to all 16 Cortex-A720AE processors described in the FVP. Only cores 0 to 3 are used by the default Linux configuration

To learn more about OS awareness in Arm Debugger, see the [OS awareness documentation](https://developer.arm.com/documentation/101470/latest/Debugging-Embedded-Systems/About-OS-awareness).

## Next steps: enhance connections (symbols, reset, semihosting)

{{% notice Next %}}
In the next section, you will enhance these connections with symbol loading, reset behavior, semihosting, and Linux kernel awareness settings.
{{% /notice %}}
