---
# User change
title: "Debug primary compute and Linux"

weight: 8 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
## Debug primary compute

The Primary Compute application processors (`Cortex-A720AE`) are the final processors to be enabled.

As before, you can connect whilst powered down and monitor the point that they are enabled.

You can debug the initialization code and the final Linux Operating System (OS) threads.

## Connect debugger to target

Use the following debugger commands in the `Primary_init.launch` to load the symbols for the `BL2` initialization code, setting a breakpoint at `bl2_entrypoint`.

Note that an address offset is used to specify the Exception Level (EL) that the image is relevant to. If the processor changes Exception Level, the debug information would need to also be loaded to the corresponding EL address space.

For example the processors start in `EL3` and move to `EL2N` when the Linux kernel is enabled.

``` text
stop
add-symbol-file "/arm-auto-solutions/build/tmp_baremetal/work/fvp_rd_aspen-poky-linux/trusted-firmware-a/2.13.0+git/image/firmware/bl2.elf" EL3:0x0
tbreak bl2_entrypoint

```

{{% notice Note %}}
Exact paths might differ depending on your build output.
{{% /notice %}}

Run to **bl2_entrypoint** and step through as required.

{{% notice Tip %}}
Symbol loading is Exception Level–aware. If execution changes Exception Level, load symbols into the corresponding EL address space. For example, the processors start in EL3 and transition to EL2N when the Linux kernel is enabled.
{{% /notice %}}

## Debug the Linux kernel with OS awareness (symmetric multiprocessing)

{{% notice Note %}}
OS awareness for Linux Kernel 6.12 (as used with Reference Software Stack 2.1) is supported as of Arm Development Studio 2025.1 (and 2025.b).

Later versions of the stack may require later versions of Arm Development Studio.
{{% /notice %}}

Disconnect `Primary_init.launch` and use the `Primary_Linux.launch` connection you created earlier to enable Arm Development Studio OS awareness for the Linux kernel.

Load the kernel symbols and set source mapping if your kernel sources are located outside the default paths:

```text
stop
add-symbol-file "/arm-auto-solutions/build/tmp_baremetal/work/fvp_rd_aspen-poky-linux/linux-yocto-rt/6.12.30+git/linux-fvp_rd_aspen-preempt-rt-build/vmlinux" EL2N:0x0
set substitute-path "/usr/src/kernel/" "/arm-auto-solutions/build/tmp_baremetal/work-shared/fvp-rd-aspen/kernel-source/"
```

Run the FVP until the OS prompt appears.

{{% notice %}}
If you only need kernel debugging, start the model with the debug server **and** begin execution immediately by adding `--run`:

```command
kas shell -c "../layers/meta-arm/scripts/runfvp -t tmux --verbose -- --iris-server --iris-port 7100 --run"
```
{{% /notice %}}

## View Linux threads with OS awareness

Enable the **Threads** view to inspect kernel threads instead of raw CPUs:

In **Debug Control**, right-click the **Primary_Linux** connection and select **Display Threads**
2. Alternatively, enter `thread` in the **Command** pane.

The view changes from listing the 16 application processors to the active OS threads.

{{% notice Note %}}
You might see a warning like:
```text
WARNING(ROS60): Could not enable OS support as the OS does not appear to be initialized. This might be caused by a mismatch between the loaded symbols and the code on the target or because the OS is not up and running. Enabling OS support will be re-attempted when the target next stops.
```
This occurs if the OS has not completed boot when you connect; it is safe to ignore and will clear when stopping target after the OS has booted.
{{% /notice %}}

You have successfully learnt how to use Arm Development Studio to explore and debug the Arm Zena CSS Reference Software Stack.
