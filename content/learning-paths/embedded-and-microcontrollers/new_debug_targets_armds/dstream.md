---
# User change
title: Debug connection with Arm DSTREAM

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
The [DSTREAM](https://developer.arm.com/Tools%20and%20Software/DSTREAM-ST#Editions) family of debug probes are a scalable solution for debug and trace of Arm based platforms. They are used in conjunction with the Arm Development Studio debugger. They can connect to the host machine over high speed USB or Ethernet connections.

The family consists of:
 - [DSTREAM-ST](https://developer.arm.com/Tools%20and%20Software/DSTREAM-ST)
 - [DSTREAM-PT](https://developer.arm.com/Tools%20and%20Software/DSTREAM-PT)
 - [DSTREAM-HT](https://developer.arm.com/Tools%20and%20Software/DSTREAM-HT)
 - [DSTREAM-XT](https://developer.arm.com/Tools%20and%20Software/DSTREAM-XT)

DSTREAM-ST provides full debug capability over JTAG and SWD interfaces, as well as on-chip and low bandwidth (4-bit) external trace. If higher bandwidth trace is necessary, then one of the other solutions can be used, provided the SoC (and platform) support such features.

 - DSTREAM-PT adds the capability to support (up to) 32-bit parallel trace output.
 - DSTREAM-HT adds the capability to support (up to) 6 lanes of High-Speed Serial Trace (HSST)
 - DSTREAM-XT adds the capability to support (debug and) trace over PCIe interface.

## Before you begin

You should have Arm Development Studio installed and your license configured. Refer to the [Arm Development Studio install guide](/install-guides/armds/) for more information.

It is assumed you have access to a DSTREAM unit, and an appropriate development board. For this example, you shall use an [MPS2+](https://developer.arm.com/Tools%20and%20Software/MPS2%20Plus%20FPGA%20Prototyping%20Board) programmed for Cortex-M3 (`AN385`), which is the same hardware as modeled by the FVPs in the previous section.

### Updating IP Address

By default, DSTREAM units are provided with DHCP enabled, allowing the network to specify the IP address. If you wish to set to a fixed IP address, in the Development Studio IDE open the `Debug Hardware Configure IP` view (`Windows > Open View`), Browse for your DSTREAM unit, and set as appropriate. Note if your network does not support DHCP you should use USB to connect to the unit for this step.

### Updating firmware

Firmware for the DSTREAM family is provided with Arm Development Studio, and generally needs to be updated when a new version of Development Studio is released. To manually update the firmware, open the `Debug Hardware Firmware Installer`. Browse for your DSTREAM, and install. The unit will reboot when complete.


## Create a Platform Configuration for your Hardware

Arm Development Studio is supplied with out-of-the-box configurations for many development boards. This step could be skipped as the MPS2+ platform is provided, but this example is to illustrate how to create a configuration for any board.

If not done previously, select `File` > `New` > `Other` > `Configuration Database` > `Configuration Database`, and give it a meaningful name. This is where the debugger stores all user-made configurations.

Then select `File` > `New` > `Other` > `Configuration Database` > `Platform Configuration`, which will be the actual configuration to create. When prompted, select the above `Configuration Database`.

You may then be prompted to ask how to generate such a configuration. Select Automatic, and click Next. Browse for your DSTREAM unit, which should be connected to your target hardware. The unit will interrogate the target and determine which Arm processors are present. Save the configuration with an appropriate name.

## Import Software example

If not previously imported, use `File` > `Import...` > `Arm Development Studio` > `Examples and Programming Libraries`, and browse for `startup_Cortex-M3_AC6` (use the text filter box to easily locate this).

## Create a Debug Configuration for your Platform

Now that the debugger is aware of your platform, you can now create a debug configuration to describe how the debugger will connect to that platform.

To start, select `File` > `New` > `Hardware Connection`, and give it a meaningful name. It is recommended to associate the connection with a specific project (`startup_Cortex-M3_AC6`) when available.

Select the `Platform Configuration` you created (the text filter can assist if many targets defined), and click Finish.

Ensure `DSTREAM family` is selected from the Target Connection pulldown, and Browse for your DSTREAM unit. The debugger will recognize the type of DSTREAM unit connected. Use the `DTSL Options` Edit button to specify additional settings (such as which processor(s) to trace).

To load an image, navigate to the `Files` tab, and browse to the appropriate ELF image. Then, in the `Debugger` tab, select `Debug from entry point`.

If the target is already running with an image you can also just the debug symbols from the `Files` tab. In that scenario, in the `Debugger` tab, select `Connect Only`.

Click `Debug` to connect to the platform, and commence your debug session.

## Troubleshooting

Arm platforms can be very complex, with multiple heterogeneous processors, on-chip power islands, and very high-speed interfaces. The below resources may be helpful if you are experiencing issues configuring for your hardware.

- [Troubleshooting DSTREAM-ST connections](https://developer.arm.com/documentation/100892/1-0/Troubleshooting/Troubleshoot-target-connections)
- [Troubleshooting DSTREAM-PT connections](https://developer.arm.com/documentation/102637)
- [Help with debugging and tracing targets](https://developer.arm.com/documentation/107551)
