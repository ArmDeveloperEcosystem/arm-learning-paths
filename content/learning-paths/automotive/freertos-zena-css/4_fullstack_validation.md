---
title: Add FreeRTOS to the Zena CSS SW stack boot flow
description: Replace the default Zephyr Cluster 1 firmware with a FreeRTOS Multi View 2 image and verify that it runs correctly through the standard Zena CSS secure boot flow.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Run FreeRTOS in Zena CSS SW stack

## Objective

In the previous Learning Path, you validated the FreeRTOS using direct image loading on the Zena FVP.

In this Learning Path, you will validate the same application in the complete Zena CSS software stack by replacing the default Zephyr Cluster 1 firmware with a FreeRTOS image.

After completing this section, you will have verified that:

- FreeRTOS can replace the default Zephyr Cluster 1 firmware.
- The normal Zena CSS secure boot flow remains functional.
- RSE image authentication still succeeds.
- SCP firmware initialization remains unchanged.
- GIC Multi-View interrupts continue to work correctly regarding view 2.

This exercise uses a manually substituted binary. Yocto recipe integration is covered in the next Learning Path.

## Before you begin

Make sure that you have completed:

- Standalone FVP validation
- Zena FVP validation

You should also have:

- A working Zena CSS build environment
- A working Zena CSS Configuration 2 FVP platform
- A FreeRTOS binary built for the `zena-css` target

## Build the FreeRTOS image

### Update the GIC configuration for Multi View 2

The direct-loading workflow used during bring-up doesn't follow the normal Zena CSS boot sequence. In that environment, the SCP firmware is not running and the GIC remains in its default configuration.

As described in the previous chapter, the initial FreeRTOS port therefore uses GIC View 0 to simplify platform bring-up and debugging.

In the standard Zena CSS boot process, SCP firmware configures the GIC multi-view topology before releasing the Safety Island software. Safety Island Cluster 1 is assigned to View 2, which is the same view used by the default Zephyr RTOS.

To validate FreeRTOS as a drop-in replacement for the Cluster 1 Zephyr image, FreeRTOS must use the same GIC view and redistributor addresses as the original firmware. Otherwise, interrupt configuration no longer matches the platform state.

For more information, see [GIC Multiple Views in the Arm Zena CSS documentation](https://arm-zena-css.docs.arm.com/en/latest/design/components.html#gic-multiple-views).

The published demo already defines both configurations. Selecting `zena_css_fvp` configures the GIC distributor and redistributor base addresses for GIC View 2 in `FreeRTOSConfig.h`:

```c
#elif defined( R82AE_PLATFORM_ZENA_CSS_FVP )
    #define configINTERRUPT_CONTROLLER_BASE_ADDRESS    0x30200000UL
    #define configGIC_REDISTRIBUTOR_BASE_ADDRESS       0x30260000UL
    #define configINTERRUPT_PRIORITY_REGISTER_ADDRESS  ( configGIC_REDISTRIBUTOR_BASE_ADDRESS + 0x10400UL )
    #define configPL011_UART0_BASE_ADDRESS             0x2A410000UL
    #define configGIC_SGI_AFF2                         1U
    #define configGENERIC_TIMER_INTERRUPT_ID           29U
```


## Build the FreeRTOS application

Build with either GCC or Arm Compiler for Embedded and configure the exact full-stack platform target, `zena_css_fvp`:

{{< tabpane code=true >}}
  {{< tab header="GCC" language="bash" >}}
cd FreeRTOS-Partner-Supported-Demos/CORTEX_R82AE_SMP_FVP_MPU_GCC_ARMCLANG
cmake -S . -B build/zena_css \
  -DCMAKE_TOOLCHAIN_FILE=gnu_toolchain.cmake \
  -DCMAKE_BUILD_TYPE=Debug \
  -DKERNEL_DIR_PATH=../../FreeRTOS-Kernel \
  -DR82AE_PLATFORM=zena_css_fvp
cmake --build build/zena_css --parallel
aarch64-none-elf-objcopy -O binary \
  build/zena_css/r82ae_smp_fvp_gcc_armclang.elf \
  build/zena_css/r82ae_smp_fvp_gcc_armclang.bin
  {{< /tab >}}
  {{< tab header="Arm Compiler for Embedded" language="bash" >}}
cd FreeRTOS-Partner-Supported-Demos/CORTEX_R82AE_SMP_FVP_MPU_GCC_ARMCLANG
cmake -S . -B build/zena_css \
  -DCMAKE_TOOLCHAIN_FILE=armclang_toolchain.cmake \
  -DCMAKE_BUILD_TYPE=Debug \
  -DKERNEL_DIR_PATH=../../FreeRTOS-Kernel \
  -DR82AE_PLATFORM=zena_css_fvp
cmake --build build/zena_css --parallel
fromelf --bincombined \
  --output=build/zena_css/r82ae_smp_fvp_gcc_armclang.bin \
  build/zena_css/r82ae_smp_fvp_gcc_armclang.elf
  {{< /tab >}}
{{< /tabpane >}}


The generated binary will be located in:

```output
build/zena_css/r82ae_smp_fvp_gcc_armclang.bin
```

Record the full path to this file.


## Understand how the firmware is packaged

If you are already familiar with the Zena CSS firmware packaging flow, you can skip this section and proceed directly to **Replace the Cluster 1 firmware** section.

Before replacing the Cluster 1 firmware, it is useful to understand how the firmware is packaged into the final Zena CSS image.
The goal of this section is not to teach Yocto in depth. Instead, it demonstrates a simple investigation process that can be applied when integrating software into any Yocto-based platform.

### Review the Zena CSS software architecture

Before examining the Yocto build system, review the Zena CSS architecture and identify the software running on each processing element.

For this Learning Path, the important components are:

- Runtime Security Engine (RSE)
- System Control Processor (SCP)
- Application Processing (AP) subsystem
- Safety Island Cluster 1 (SI CL1)

By default, SI CL1 runs a Zephyr image.

The goal of this exercise is to replace the SI CL1 Zephyr image with a FreeRTOS image while leaving all other software components unchanged.


### Safety Island CL1 firmware loading

The Zena CSS documentation indicates that the SI CL1 firmware is loaded by the RSE [boot flow](https://arm-zena-css.docs.arm.com/en/v2.2.1/design/boot_process.html#boot-flow).

The [Zena CSS RSE image layout](https://arm-zena-css.docs.arm.com/en/v2.2.1/design/boot_process.html#images-layout) indicates where the SI CL1 image is packaged.

The SI CL1 image in `rse-flash-image.img` is signed, so replacing the image within the binary is not sufficient.

The next step is to identify the Yocto recipe responsible for creating this image.

### Locate the recipe responsible for the RSE image

Because the Zephyr image is packaged in `rse-flash-image.img`, search for recipes related to firmware image generation.

From the `arm-zena-css` directory, find the RSE image definition:

```bash
grep -nr "rse-flash-image" yocto/
```

The result identifies [`firmware.cfg`](https://gitlab.arm.com/automotive-and-industrial/arm-auto-solutions/arm-zena-css/-/blob/release-v2.2/yocto/meta-zena-css-bsp/recipes-bsp/images/files/fvp-rd-aspen/firmware.cfg?ref_type=heads#L31):

```output
yocto/meta-zena-css-bsp/recipes-bsp/images/files/fvp-rd-aspen/firmware.cfg:31:image rse-flash-image.img {
```

Find the recipe that uses this configuration:

```bash
grep -nr "firmware.cfg" yocto/
```

The result links it to the image recipe:

```output
yocto/meta-zena-css-bsp/recipes-bsp/images/firmware-fvp-rd-aspen.bb:40:GENIMAGE_CONFIG = "firmware.cfg"
```

This establishes the link between the image definition and the recipe that generates it.

Open [firmware-fvp-rd-aspen.bb](https://gitlab.arm.com/automotive-and-industrial/arm-auto-solutions/arm-zena-css/-/blob/release-v2.2/yocto/meta-zena-css-bsp/recipes-bsp/images/firmware-fvp-rd-aspen.bb?ref_type=heads#L40) and inspect its tasks. In the next section, you'll modify this recipe to replace the default Cluster 1 firmware with the FreeRTOS image while preserving the normal Zena CSS boot flow.

### Identify where the SI CL1 firmware enters the image

The objective is to determine where the Zephyr SI CL1 firmware is added to the image packaging flow.

Because the target component is SI CL1, search the recipe for terms such as `cl1` and `safety_island`:

Inside the image-signing logic you will find commands similar to:

```bash
cp ${RECIPE_SYSROOT}/firmware/${SI_CL1_FIRMWARE_BINARY} \
   ${B}/safety_island_cl1.bin
```
<!--
and:

```bash
cp ${RECIPE_SYSROOT}/firmware/${SI_CL1_FIRMWARE_BINARY} \
   ${B}/capsule_safety_island_cl1.bin
```
-->
This is the point where the default SI CL1 firmware enters the image packaging workflow.

### Choose the fastest validation strategy

A production integration would provide FreeRTOS through its own Yocto recipe. However, this adds complexity to source management, recipe maintenance, dependency tracking, and build integration.

For an initial platform validation, none of that is required.

The FreeRTOS binary has already been built externally:

```output
build/zena_css/r82ae_smp_fvp_gcc_armclang.bin
```

The quickest way to validate functionality is therefore to replace the SI CL1 payload at the image-packaging stage.

This approach keeps the existing Zena CSS build flow unchanged while allowing the FreeRTOS image to pass through the normal signing and boot process.

In the next section, you will replace the default Zephyr SI CL1 firmware with the FreeRTOS binary and rebuild the platform image.

## Replace the Cluster 1 firmware

Open the file `yocto/meta-zena-css-bsp/recipes-bsp/images/firmware-fvp-rd-aspen.bb`.

Locate the following command in the `do_sign_images()` function:

```bash
cp ${RECIPE_SYSROOT}/firmware/${SI_CL1_FIRMWARE_BINARY} \
   ${B}/safety_island_cl1.bin
```

Replace it with:

```bash
cp /absolute/path/to/build/zena_css/r82ae_smp_fvp_gcc_armclang.bin \
   ${B}/safety_island_cl1.bin
```
<!--
Locate the capsule image copy command:

```bash
cp ${RECIPE_SYSROOT}/firmware/${SI_CL1_FIRMWARE_BINARY} \
   ${B}/capsule_safety_island_cl1.bin
```

Replace it with:

```bash
cp /absolute/path/to/build/zena_css/r82ae_smp_fvp_gcc_armclang.bin \
   ${B}/capsule_safety_island_cl1.bin
```
-->

This replaces the default Zephyr Cluster 1 firmware while leaving the remainder of the Zena CSS software stack unchanged.

## Rebuild the firmware image

Force regeneration of the signed images:

```bash
kas shell -c 'bitbake firmware-fvp-rd-aspen -C sign_images'
```

Build the updated firmware package:

```bash
kas build --target firmware-fvp-rd-aspen
```

The generated flash image is:

```output
build/tmp_baremetal/deploy/images/fvp-rd-aspen/rse-flash-image.img
```

## Boot the platform

Launch the Zena CSS FVP in a tmux session:

```bash
kas shell -c '../layers/meta-arm/scripts/runfvp -t tmux'
```

Wait for the platform to complete boot, and then access the Safety Island Cluster 1 console.

Execute:

```console
ping
```

Expected output:

```output
Ping from Core 0
Pong response from Core 1
Pang response from Core 2
Pung response from Core 3
```

Successful execution confirms that:

- The FreeRTOS image was authenticated and loaded by RSE.
- The image packaging process completed successfully.
- SCP firmware initialized the platform correctly.
- GIC Multi View 2 has been configured by the Safety Island CL0 (SCP).
- FreeRTOS can replace Zephyr in the complete Zena CSS software stack.

## What you've accomplished and what's next

You have validated a FreeRTOS image in the complete Zena CSS software stack.

By manually replacing the default Zephyr Cluster 1 firmware, you verified that the application works correctly with the standard secure boot, image signing, and firmware packaging flow.

The next Learning Path shows how to automate this process using Yocto integration.
