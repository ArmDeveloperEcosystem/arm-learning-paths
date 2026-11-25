---
title: Build the Zephyr firmware within the E8 memory budget
description: Build for the correct HP and U85 target and check model metadata, scratch capacity, and linker memory usage.
weight: 5
layout: learningpathall
---

## Build the camera and UART application

The default build captures camera frames, executes MobileSAM, selects masks, and reports progress through UART4. `CONFIG_MOBILESAM_DISPLAY=n` leaves CDC, DSI, and the panel disabled; the camera route stays selected after initialization. Build with the pinned Alif SDK and the matching PTE/metadata pair:

```bash
cd "$EXECUTORCH_ROOT"
west build \
  -d "$MOBILE_SAM_OUTPUT/build-mobilesam-live" \
  -p always \
  -b alif_e8_dk/ae822fa0e5597xx0/rtss_hp \
  "$EXECUTORCH_ROOT/zephyr/samples/mobilesam-ethosu" -- \
  -DZEPHYR_EXTRA_MODULES="$EXECUTORCH_ROOT;$SDK_ALIF" \
  -DSDK_ALIF="$SDK_ALIF" \
  -DET_PTE_FILE_PATH="$MOBILE_SAM_OUTPUT/mobilesam_live_384_grid4_multimask.pte" \
  -DMODEL_METADATA_PATH="$MOBILE_SAM_OUTPUT/mobilesam_live_384_grid4_multimask.json" \
  -DPython3_EXECUTABLE="$(command -v python)"
```

The board identifier is tied to the pinned vendor tree. Replacing it with a similar identifier from a newer Zephyr tutorial can select a different configuration. This sample sets `CONFIG_ARM_ETHOS_U85_256=y` and `ETHOSU_TARGET_NPU_CONFIG=ethos-u85-256` explicitly.

CMake finds the official `serial_camera_mt9m114_selfie.overlay` in `sdk-alif` and adds the sample's deferred-initialization overlay. It generates model metadata, inspects the PTE for unsupported CPU operators, and extracts the Ethos-U scratch requirement. The default target excludes `display.cpp` and its logo from the linked application.

Check the generated configuration before programming:

```bash
rg 'CONFIG_(RTSS_HP|ARM_ETHOS_U85_256|MOBILESAM_DISPLAY|DISPLAY|MIPI_DSI)' \
  "$MOBILE_SAM_OUTPUT/build-mobilesam-live/zephyr/.config"
! rg -q '^CONFIG_(MOBILESAM_DISPLAY|DISPLAY|MIPI_DSI)=y$' \
  "$MOBILE_SAM_OUTPUT/build-mobilesam-live/zephyr/.config"
```

Require the HP/U85-256 target and no enabled display or DSI option. A display that stays blank is expected for this configuration.

## Understand the three allocator pools

The supplied `prj.conf` sets:

| Setting | Bytes | Purpose |
| --- | ---: | --- |
| `CONFIG_EXECUTORCH_METHOD_ALLOCATOR_POOL_SIZE` | 655,360 | Method state and planned buffers allocated by the sample |
| `CONFIG_EXECUTORCH_TEMP_ALLOCATOR_POOL_SIZE` | 6,488,064 | Main Ethos-U tensor/scratch arena |
| `CONFIG_EXECUTORCH_FAST_TEMP_ALLOCATOR_POOL_SIZE` | 393,216 | Fast scratch arena |

CMake rejects a PTE whose extracted scratch requirement exceeds the configured main scratch pool. Passing that check does not prove the complete application fits: camera buffers, stacks, method allocations, and linker regions also consume memory. The optional dashboard adds display buffers and drivers.

The clean default build with the pinned source, public-image export, and independently cloned vendor workspace reported:

| Linker region | Used bytes | Capacity bytes | Remaining bytes |
| --- | ---: | ---: | ---: |
| Application RAM | 7,580,640 | 7,602,176 | 21,536 |
| SRAM0 | 64 | 786,432 | 786,368 |

It used **171,192 bytes** of FLASH, with raw binary SHA256 `3be06219380e7d2444d0b18bef8ebaa42284f401aed2d8e3e5d720c50edc4a36`. The build checks confirmed disabled display/DSI nodes, no linked display or diagnostic-trace functions, matching model metadata, and hard-float Cortex-M55/MVE settings. Read your own linker report and `zephyr.map`: application RAM remains close to its limit even though SRAM0 no longer holds the dashboard framebuffer. Changing the model, toolchain, logging, or buffer placement requires another memory and execution check.

## Keep model storage separate from firmware storage

The PTE remains in memory-mapped external OSPI flash at `0xC0000000`. The firmware records its size and address and opens it with `BufferDataLoader`. It does not link the 13 MB model into the firmware image.

Changing the external-flash address alone does not enlarge RAM or fix a linker overflow. Changing the model size also requires rebuilding the firmware so its compiled PTE size and generated metadata remain consistent.

Before flashing, locate `build-mobilesam-live/zephyr/zephyr.elf`, inspect the linker report, and confirm that the build accepted your PTE. The next lesson programs model data and application firmware as separate operations.

## Build the optional dashboard separately

The dashboard is an experimental extension: earlier physical runs displayed advancing camera frames and masks but retained DSI acknowledgment and packet errors. Keep the default build and its evidence intact. To investigate the extension, build into a different directory with both its configuration and overlay:

```bash
west build \
  -d "$MOBILE_SAM_OUTPUT/build-mobilesam-dashboard" \
  -p always \
  -b alif_e8_dk/ae822fa0e5597xx0/rtss_hp \
  "$EXECUTORCH_ROOT/zephyr/samples/mobilesam-ethosu" -- \
  -DZEPHYR_EXTRA_MODULES="$EXECUTORCH_ROOT;$SDK_ALIF" \
  -DSDK_ALIF="$SDK_ALIF" \
  -DEXTRA_CONF_FILE="$EXECUTORCH_ROOT/zephyr/samples/mobilesam-ethosu/dashboard.conf" \
  -DEXTRA_DTC_OVERLAY_FILE="$EXECUTORCH_ROOT/zephyr/samples/mobilesam-ethosu/boards/dashboard.overlay" \
  -DET_PTE_FILE_PATH="$MOBILE_SAM_OUTPUT/mobilesam_live_384_grid4_multimask.pte" \
  -DMODEL_METADATA_PATH="$MOBILE_SAM_OUTPUT/mobilesam_live_384_grid4_multimask.json" \
  -DPython3_EXECUTABLE="$(command -v python)"
```

Both files are required: they enable `CONFIG_MOBILESAM_DISPLAY=y` and the matching display devicetree nodes. This optional configuration cross-built successfully, but has not been accepted as a clean physical output path. It switches the shared MIPI route between capture and display and retains the known unresolved DSI limitation. A successful build or updating screen does not establish an error-free run. The remaining programming and primary validation commands use `build-mobilesam-live`, the default camera-and-UART build.

## What you've accomplished

You've built the default HP camera/NPU application, generated matching model metadata, and checked its scratch and linker capacity. Next, program the model and firmware as separate artifacts.
