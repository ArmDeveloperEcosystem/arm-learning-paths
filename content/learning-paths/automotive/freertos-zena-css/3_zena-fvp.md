---
title: Direct loading FreeRTOS on the Zena CSS Safety Island Cluster 1
description: Adapt the Cortex-R82AE FreeRTOS port to the Zena CSS memory map and load it directly into the Safety Island cluster on the FVP.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Direct load FreeRTOS on the Zena CSS FVP

## Objective

In the previous chapter, FreeRTOS ran on `FVP_BaseR_Cortex-R82AE`. In this chapter, you will investigate the changes required to run the same software on the R82AE cores in Safety Island Cluster 1 of `FVP_Zena_CSS_Cfg2`.
You will learn how to retrieve information from the Zena CSS software stack and identify the additional porting requirements, particularly the differences in peripheral base addresses.
For the initial bring-up, you will boot only the software for Safety Island Cluster 1. Keeping the other platform cores inactive shortens the development cycle and simplifies debugging.

After completing this section, you will have verified that:

- The UART and GIC base addresses are correctly configured for Zena CSS, using GIC Multi-View 0 during initial bring-up.
- The FreeRTOS raw binary can be loaded directly into Safety Island Cluster 1 LLRAM.
- Safety Island Cluster 1 can be started independently of the standard Zena CSS secure boot flow.
- FreeRTOS starts successfully on all four R82AE cores in Safety Island Cluster 1 of FVP_Zena_CSS_Cfg2.
- UART output, SMP scheduling, core affinity, shared memory, and interprocessor interrupts operate correctly.


## Building the Zena CSS SW stack

Build and run the Arm Zena CSS Reference Software Stack before you replace its Safety Island software. Follow the [build instructions in the Zena CSS user guide](https://arm-zena-css.docs.arm.com/en/latest/user_guide/reproduce.html).

Verify that the unmodified stack boots. This baseline separates FreeRTOS porting errors from build or FVP installation errors.

The Zena CSS Runtime Security Engine (RSE) normally authenticates, decrypts, loads, and starts the Safety Island image. During initial porting, bypass this flow and load the FreeRTOS binary directly into Safety Island Cluster 1 low-latency RAM (LLRAM). Direct loading shortens the debug cycle before you add image signing and flash-image packaging.

{{% notice Warning %}}
The executable and image paths in this direct-load workflow were recorded during bring-up. Confirm their names and locations in your Zena CSS release before running the commands.
{{% /notice %}}

## Adapt the platform configuration

### Identify the platform-specific configuration

The binary built for the standalone Fixed Virtual Platform (FVP) doesn't use the Zena CSS memory map. Create a Zena CSS target in the port and update these platform-dependent elements:

1. Set the linker code and data regions to the Safety Island cluster 1 LLRAM addresses.
2. Make the startup code enter Exception Level 1 (EL1) in the execution state expected by the FreeRTOS Cortex-R82 port.
3. Configure the Cluster 1 Generic Interrupt Controller (GIC) interfaces and interprocessor interrupt IDs.
4. Update the core-affinity decoding for the Safety Island cluster.
5. Set the PL011 base address to the Zena CSS Safety Island UART.
6. Keep the LLRAM attributes and Memory Protection Unit (MPU) regions consistent across all participating cores.

You can obtain the UART and GIC addresses from the Zephyr device tree in the Zena CSS Reference Software Stack.

{{% notice Warning %}}
Safety Island Cluster 1 is available only in FVP Configuration 2. Its registers and dedicated IP registers aren't included in the public [Programmer's model for Zena CSS](https://support.arm.com/documentation/110125/0100/Programmer-s-model-for-Zena-CSS).
{{% /notice %}}

The [Cluster 1 Zephyr device tree](https://gitlab.arm.com/automotive-and-industrial/arm-auto-solutions/arm-zena-css/-/blob/release-v2.2/components/safety_island/zephyr/src/boards/arm/fvp_rd_aspen_safety_island/fvp_rd_aspen_safety_island_c1.dts) contains the following definitions:

```dts
gic: interrupt-controller@30200000 {
    compatible = "arm,gic-v3", "arm,gic";
    redistributor-regions = <4>;
    reg = <0x0 0x30200000 0x10000>,   /* GICD */
          <0x0 0x30260000 0x20000>,   /* GICR - CPU 0 */
          <0x0 0x30280000 0x20000>,   /* GICR - CPU 1 */
          <0x0 0x302a0000 0x20000>,   /* GICR - CPU 2 */
          <0x0 0x302c0000 0x20000>;   /* GICR - CPU 3 */
    interrupt-controller;
    #interrupt-cells = <4>;
    status = "okay";
};

uart0: uart@2a410000 {
    compatible = "arm,pl011";
    reg = <0x0 0x2a410000 0x10000>;
    status = "disabled";
    interrupts = <GIC_SPI 7 IRQ_TYPE_LEVEL IRQ_DEFAULT_PRIORITY>;
    interrupt-names = "irq_0";
    clocks = <&uartclk>;
};
```

### Adapt the FreeRTOS code

Set the PL011 UART base address to `0x2a410000`.

The device tree uses `0x30200000` for the GIC distributor. This address is the distributor base for view 2 of the multi-view GIC, not the base of the complete GIC. See [GIC multiple views](https://arm-zena-css.docs.arm.com/en/v2.2/design/components.html#gic-multiple-views) in the Zena CSS documentation.

{{% notice Warning %}}
Don't use `GICR_TYPER.Last` to discover all Cluster 1 redistributors. In GIC views 1, 2, and 3, this bit always reads as `1` when `GICD_CFGID.VIEW` is `1`. Define the four redistributor regions explicitly, as shown in the Zephyr device tree. See the [`GICR_TYPER` register description](https://support.arm.com/documentation/102666/0201/Programmers-model-for-GIC-720AE/Redistributor-registers-for-control-and-physical-LPIs-summary/GICR-TYPER--Redistributor-Type-Register?lang=en).
{{% /notice %}}

To inspect the GIC address map exposed by the model, run:

```bash
build/tmp/sysroots-components/x86_64/fvp-rd-aspen-native/usr/lib/fvp/fvp-rd-aspen/bin/FVP_Zena_CSS_Cfg2 \
  -C css.smb.si.gic.print-memory-map=1
```

The output includes the distributor and redistributor regions for each view:

```output
Info: RD_ASD: terminal_uart: Listening for serial connection on port 5000
INFO: Multiple views bits are bit number '20' and bit number '21'.
GICv3 map: 0x30010000--0x3001ffff: GICD message based SPI signalling registers aliases
GICv3 map: 0x30110000--0x3011ffff: GICD message based SPI signalling registers aliases
GICv3 map: 0x30210000--0x3021ffff: GICD message based SPI signalling registers aliases
GICv3 map: 0x30310000--0x3031ffff: GICD message based SPI signalling registers aliases
GICv3 map: 0x30000000--0x3000ffff: GICD registers for view 0
GICv3 map: 0x30100000--0x3010ffff: GICD registers for view 1
GICv3 map: 0x30200000--0x3020ffff: GICD registers for view 2
GICv3 map: 0x30300000--0x3030ffff: GICD registers for view 3
GICv3 map: 0x30020000--0x3002ffff: GICT registers.
GICv3 map: 0x30040000--0x3005ffff: GICR registers for 0.0.0.0 for View 0.
GICv3 map: 0x30140000--0x3015ffff: GICR registers for 0.0.0.0 for View 1.
GICv3 map: 0x30240000--0x3025ffff: GICR registers for 0.0.0.0 for View 2.
GICv3 map: 0x30340000--0x3035ffff: GICR registers for 0.0.0.0 for View 3.
GICv3 map: 0x30060000--0x3007ffff: GICR registers for 0.1.0.0 for View 0.
GICv3 map: 0x30160000--0x3017ffff: GICR registers for 0.1.0.0 for View 1.
GICv3 map: 0x30260000--0x3027ffff: GICR registers for 0.1.0.0 for View 2.
GICv3 map: 0x30360000--0x3037ffff: GICR registers for 0.1.0.0 for View 3.
GICv3 map: 0x30080000--0x3009ffff: GICR registers for 0.1.1.0 for View 0.
GICv3 map: 0x30180000--0x3019ffff: GICR registers for 0.1.1.0 for View 1.
GICv3 map: 0x30280000--0x3029ffff: GICR registers for 0.1.1.0 for View 2.
GICv3 map: 0x30380000--0x3039ffff: GICR registers for 0.1.1.0 for View 3.
GICv3 map: 0x300a0000--0x300bffff: GICR registers for 0.1.2.0 for View 0.
GICv3 map: 0x301a0000--0x301bffff: GICR registers for 0.1.2.0 for View 1.
GICv3 map: 0x302a0000--0x302bffff: GICR registers for 0.1.2.0 for View 2.
GICv3 map: 0x303a0000--0x303bffff: GICR registers for 0.1.2.0 for View 3.
GICv3 map: 0x300c0000--0x300dffff: GICR registers for 0.1.3.0 for View 0.
GICv3 map: 0x301c0000--0x301dffff: GICR registers for 0.1.3.0 for View 1.
GICv3 map: 0x302c0000--0x302dffff: GICR registers for 0.1.3.0 for View 2.
GICv3 map: 0x303c0000--0x303dffff: GICR registers for 0.1.3.0 for View 3.
```

In the normal boot flow, the System Control Processor (SCP) firmware on Safety Island Cluster 0 configures the GIC views. The direct-load workflow starts only Cluster 1, so this configuration doesn't occur. Use view 0 for the initial FreeRTOS bring-up:

| Interface | Core | Base address |
| --- | ---: | ---: |
| GIC distributor (GICD) | All | `0x30000000` |
| GIC redistributor (GICR) | 0 | `0x30060000` |
| GIC redistributor (GICR) | 1 | `0x30080000` |
| GIC redistributor (GICR) | 2 | `0x300a0000` |
| GIC redistributor (GICR) | 3 | `0x300c0000` |

## Run FreeRTOS on the Zena CSS FVP

Start with a single-core application that prints a banner. This reduces the initial validation surface to reset, exception-level transition, memory, and UART. Enable the other cores and the ping/pong tasks only after the banner works.

Build the Zena CSS target to produce a raw binary. Record the linked load address because the `--data` offset and the image's link address must describe the same memory layout.


### Compile

Return to the Cortex-R82AE demo directory used in the previous section. Configure the exact direct-load platform target, `zena_css_fvp_direct_load`, and use the adjacent kernel clone:

```bash
cd FreeRTOS-Partner-Supported-Demos/CORTEX_R82AE_SMP_FVP_MPU_GCC_ARMCLANG
cmake -S . -B build/zena_css_direct_load \
  -DCMAKE_TOOLCHAIN_FILE=gnu_toolchain.cmake \
  -DCMAKE_BUILD_TYPE=Debug \
  -DKERNEL_DIR_PATH=../../FreeRTOS-Kernel \
  -DR82AE_PLATFORM=zena_css_fvp_direct_load
cmake --build build/zena_css_direct_load --parallel
aarch64-none-elf-objcopy -O binary \
  build/zena_css_direct_load/r82ae_smp_fvp_gcc_armclang.elf \
  build/zena_css_direct_load/r82ae_smp_fvp_gcc_armclang.bin
```



### Load the binary into Cluster 1 LLRAM

From the Zena CSS `yocto_project` directory, start the Safety Island cluster and load a binary directly. First, check the workflow with the stack's `si-hello-world.bin`:

```bash
build/tmp/sysroots-components/x86_64/fvp-rd-aspen-native/usr/lib/fvp/fvp-rd-aspen/bin/FVP_Zena_CSS_Cfg2 \
  -C css.smb.si.cluster1.core_power_on_by_default=1 \
  --data "css.smb.si.cluster1_llram=build/tmp/deploy/images/aspen/si-hello-world.bin@0x0000"
```

The `core_power_on_by_default` parameter starts Cluster 1 without waiting for the normal RSE release sequence. The `--data` parameter writes the binary at offset `0x0000` in Cluster 1 LLRAM.

After the baseline binary boots, run the FreeRTOS image with the additional model configuration needed for the FreeRTOS timer and SMP operation:

```console
build/tmp/sysroots-components/x86_64/fvp-rd-aspen-native/usr/lib/fvp/fvp-rd-aspen/bin/FVP_Zena_CSS_Cfg2 \
  -C css.smb.si.cluster1.core_power_on_by_default=1 \
  -C css.smb.si.CL1_LLRAM_config=15 \
  -C css.smb.smd.ref_counter.non_arch_start_at_default=1 \
  --data "css.smb.si.cluster1_llram=/absolute/path/to/FreeRTOS-Partner-Supported-Demos/CORTEX_R82AE_SMP_FVP_MPU_GCC_ARMCLANG/build/zena_css_direct_load/r82ae_smp_fvp_gcc_armclang.bin@0x0000"
```

Each `-C component.parameter=value` argument overrides an FVP model parameter. In this command, the value `1` enables a Boolean option. The three overrides change the FVP startup behavior as follows:

- `css.smb.si.cluster1.core_power_on_by_default=1` powers on Cluster 1 without an RSE request.
- `css.smb.si.CL1_LLRAM_config=15` applies the Cluster 1 LLRAM configuration used by [Zena CSS FVP Configuration 2](https://gitlab.arm.com/automotive-and-industrial/arm-auto-solutions/arm-zena-css/-/blob/release-v2.2/yocto/meta-zena-css-bsp/conf/machine/include/fvp/fvp-rd-aspen-cfg2.inc#L20).
- `css.smb.smd.ref_counter.non_arch_start_at_default=1` starts the FVP reference counter during model initialization.

### Understand the reference-counter override

The reference counter supplies the free-running system count used by the Arm Generic Timer. FreeRTOS programs a timer deadline against this count to generate the periodic interrupt that drives the scheduler tick.

In the normal Zena CSS boot flow, platform firmware starts and configures the counter. Direct loading bypasses that firmware, so `non_arch_start_at_default=1` tells the model to start the counter automatically at reset. The parameter doesn't set the counter frequency or the FreeRTOS tick rate.

Without this override, the image might print its startup messages because the processors and UART are running. However, the system count doesn't advance, timer deadlines aren't reached, and the scheduler doesn't switch tasks as expected. The `non_arch` name identifies this as an FVP startup control rather than an Arm architectural register. Remove the override during full-stack integration only after the platform firmware starts the counter.

Use an absolute image path during bring-up so that the FVP doesn't resolve it relative to an unexpected working directory.

### Validate in stages

Use the Safety Island UART output to validate each milestone:

1. Print a startup banner from the reset path.
2. Reach `main()` at EL1 and print the current core identifier.
3. Start the FreeRTOS scheduler on one core.
4. Start all four cores and reach the command prompt.
5. Run `ping` and observe one response from each fixed-affinity task.

If execution stops before the first UART message, attach Arm Development Studio and load the matching ELF symbols. Use Tarmac Trace to inspect synchronous exceptions, as described in the standalone FVP part.

The port is ready for integration when it starts without debugger intervention and repeatedly completes the four-core exchange.

## What you've accomplished and what's next

You've mapped the standalone port onto the Zena CSS Safety Island, loaded it directly into Cluster 1 LLRAM, and validated single-core and SMP execution in stages.

Next, you'll replace the manual `--data` workflow with a Yocto-built, signed image selected as part of the full software stack.
