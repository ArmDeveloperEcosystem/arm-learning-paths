---
title: Integrate the FreeRTOS image with Yocto
description: Define a Yocto recipe and image-selection flow that builds, signs, and packages FreeRTOS as the Zena CSS Safety Island firmware.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Move from direct loading to an integrated image

The direct-load workflow bypasses the normal Zena CSS boot chain. A deployable implementation needs Yocto to build or import FreeRTOS, package it in `rse-flash-image.img`, and include the metadata required for RSE authentication and loading.

{{% notice Note %}}
This part documents the intended integration and validation gates. The recipe, Kconfig option, and secure-boot changes are not yet implemented in the source project. Keep this Learning Path in draft until those changes are tested together.
{{% /notice %}}

Integrate the port in three increments. Validate each increment before changing how the source is obtained or compiled.
<!--
## Package the validated binary

First, create a recipe that installs the binary validated in the previous part. This separates Yocto packaging and secure-boot work from compiler differences.

The initial recipe must:

- Take the known-good `r82ae_smp_fvp_gcc_armclang.bin` as an input artifact
- Install it into the recipe deploy directory
- Expose the file under the name expected by the Safety Island image packaging
- Replace the Zephyr payload only when the FreeRTOS selection is enabled
- Declare the correct license and checksum metadata

Add a configuration choice that selects either Zephyr or FreeRTOS for Safety Island cluster 1. Keep Zephyr as the default until the FreeRTOS path passes the complete boot test.

Build the stack with the FreeRTOS selection and inspect the deploy directory. Confirm that `rse-flash-image.img` is regenerated and that its build dependencies include the FreeRTOS recipe.

## Build the port with devtool

After binary packaging works, use `devtool` to add the port source and iterate on the recipe in a workspace. Configure the recipe to run the port's CMake build with the same GCC target, linker layout, and build type used during standalone validation.

Compare these inputs between the manual and Yocto builds:

| Input | Manual build | Yocto build requirement |
| --- | --- | --- |
| Compiler target | `aarch64-none-elf` | Equivalent bare-metal target and flags |
| CPU | `cortex-r82ae` | Preserve CPU selection |
| Build system | CMake | Use the CMake class and explicit toolchain settings |
| Image format | Raw `.bin` | Deploy the same raw image format |
| Link address | Zena cluster 1 LLRAM | Preserve the validated memory map |
| Kernel version | Pinned submodule | Pin the same revision and patches |

Re-run the direct-load test with the Yocto-built `.bin` before adding it to the signed image. If the manually built image works and the Yocto-built image doesn't, compare ELF headers, map files, compiler options, and binary sizes.

## Split the recipe sources

When the Yocto build is stable, replace the temporary source archive with explicit sources:

- Fetch the pinned FreeRTOS Kernel revision
- Fetch or include the Zena CSS board support and application sources
- Apply the Cortex-R82AE kernel patches from the recipe
- Keep platform-specific patches separate from application code
- Pin every source revision and checksum

This layout makes the upstream kernel version, local port, and patch series visible to maintainers. It also allows automated license and source-revision checks.

## Integrate secure boot and flashing

Connect the selected FreeRTOS artifact to the same signing and packaging stages used for the Zephyr Safety Island image. Verify all of the following outcomes:

1. The FreeRTOS binary is present in `rse-flash-image.img`.
2. The image manifest describes the correct cluster, destination address, size, and entry point.
3. The existing signing step signs the FreeRTOS payload.
4. RSE authenticates and copies the payload to Safety Island cluster 1 LLRAM.
5. RSE releases the cluster without `core_power_on_by_default` or an FVP `--data` override.
6. The Safety Island UART shows the FreeRTOS banner and four-core ping/pong exchange.

Finally, build and boot both menu selections. The Zephyr selection must retain its original behavior, while the FreeRTOS selection must boot through the normal RSE flow.

## What you've accomplished

You've defined an incremental route from a manually loaded FreeRTOS binary to a reproducible Yocto build and signed Zena CSS flash image. The validation gates preserve a working reference at each stage and distinguish port, toolchain, packaging, and secure-boot failures.

After the integrated boot flow is stable, add the MHUv3 mailbox driver and then evaluate HIPC support for communication with the primary compute domain.

-->
