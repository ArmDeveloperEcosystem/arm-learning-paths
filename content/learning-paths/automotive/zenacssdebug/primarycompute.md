---
# User change
title: "Debug Primary Compute and Linux"

weight: 8 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Debug Primary Compute

The Primary Compute application processors (`Cortex-A720AE`) are the final processors to be enabled.

As before, you can connect whilst powered down and monitor the point that they are enabled.

You can debug the initialization code and the final Linux Operating System (OS) threads.

### Connect debugger to target

Use the following debugger commands in the `Primary_init.launch` to load the symbols for the `BL2` initialization code, setting a breakpoint at `bl2_entrypoint`.

Note that an address "offset" is used to specify the exception level that the image is relevant to. If the processor changes exception level, the debug information would need to also be loaded to the corresponding EL address space.

For example the processors start in `EL3` and move to `EL2N` when the Linux kernel is enabled.

``` text
stop
add-symbol-file /arm-auto-solutions/build/tmp_baremetal/work/fvp_rd_aspen-poky-linux/trusted-firmware-a/2.11.0+git/image/firmware/bl2.elf EL3:0x0
tbreak bl2_entrypoint
```
{{% notice Note %}}
Exact paths may differ for your set up.
{{% /notice %}}

Run the code to the `bl2_entrypoint` and you can debug as expected.

### Debug Linux kernel modules

To make use of the OS awareness feature, disconnect `Primary_init` and connect to `Primary_Linux` as created previously. Load the symbols from the `vmlinux` image.

``` text
stop
add-symbol-file /arm-auto-solutions/build/tmp_baremetal/work/fvp_rd_aspen-poky-linux/linux-yocto/6.6.54+git/linux-fvp_rd_aspen-standard-build/vmlinux EL2N:0x0
set substitute-path /usr/src/kernel/ /arm-auto-solutions/build/tmp_baremetal/work-shared/fvp-rd-aspen/kernel-source/
```
Run the FVP until the OS prompt appears.

{{% notice %}}
If you are only interested in kernel debug, modify the launch command for the FVP to include `--run` to start execution immediately.

``` command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose -- --iris-server --iris-port 7100 --run"
```
{{% /notice %}}

You can now enable the `Threads` view in the `Debug Control` pane.

Right-click on the connection, and select `Display Threads`. You can also do this by entering `thread` in the `Command` pane.

The view will then change from listing the 16 application processors to the OS threads.

{{% notice Note %}}
A warning of the form:
``` text
WARNING(ROS60): Could not enable OS support as the OS does not appear to be initialized. This might be caused by a mismatch between the loaded symbols and the code on the target or because the OS is not up and running. Enabling OS support will be re-attempted when the target next stops.
```
may be emitted if the OS is not booted when you connect. It can safely be ignored.
{{% /notice %}}

You have successfully learnt how to use Arm Development Studio to explore and debug the Arm Zena CSS Reference Software Stack.
