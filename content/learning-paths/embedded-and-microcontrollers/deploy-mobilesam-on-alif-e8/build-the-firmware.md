---
title: Build the Zephyr firmware within the E8 memory budget
description: Build for the correct HP and U85 target and check model metadata, scratch capacity, and linker memory usage.
weight: 5
layout: learningpathall
---

## Build the matching application

Build the supplied Zephyr sample with the pinned Alif SDK and the PTE/metadata pair from your export:

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

CMake finds the official `serial_camera_mt9m114_selfie.overlay` in `sdk-alif` and adds the sample's deferred-initialization overlay. It generates model metadata and display-logo headers, inspects the PTE for unsupported CPU operators, and extracts the Ethos-U scratch requirement.

## Understand the three allocator pools

The supplied `prj.conf` sets:

| Setting | Bytes | Purpose |
| --- | ---: | --- |
| `CONFIG_EXECUTORCH_METHOD_ALLOCATOR_POOL_SIZE` | 655,360 | Method state and planned buffers allocated by the sample |
| `CONFIG_EXECUTORCH_TEMP_ALLOCATOR_POOL_SIZE` | 6,488,064 | Main Ethos-U tensor/scratch arena |
| `CONFIG_EXECUTORCH_FAST_TEMP_ALLOCATOR_POOL_SIZE` | 393,216 | Fast scratch arena |

CMake rejects a PTE whose extracted scratch requirement exceeds the configured main scratch pool. Passing that check does not prove the complete application fits: camera, display, stacks, method allocations, and linker regions also consume memory.

The final documented clean build reported:

| Linker region | Used bytes | Capacity bytes | Remaining bytes |
| --- | ---: | ---: | ---: |
| Application RAM | 7,580,784 | 7,602,176 | 21,392 |
| SRAM0 | 768,064 | 786,432 | 18,368 |

These figures describe the reference build. Read your own build's memory report and `zephyr.map`; changing toolchains, model shape, prompt count, logging, or buffer placement can exhaust the remaining space.

## Keep model storage separate from firmware storage

The PTE remains in memory-mapped external OSPI flash at `0xC0000000`. The firmware records its size and address and opens it with `BufferDataLoader`. It does not link the 13 MB model into the firmware image.

Changing the external-flash address alone does not enlarge RAM or fix a linker overflow. Changing the model size also requires rebuilding the firmware so its compiled PTE size and generated metadata remain consistent.

Before flashing, locate `build-mobilesam-live/zephyr/zephyr.elf`, inspect the linker report, and confirm that the build accepted your PTE. The next lesson programs model data and application firmware as separate operations.

## What you've accomplished

You've built the HP-core application for Ethos-U85-256, generated matching model metadata, and checked scratch and linker capacity. Next, program the model and firmware as separate artifacts.
