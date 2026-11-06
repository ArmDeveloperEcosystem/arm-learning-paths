---
title: Build the E8 Zephyr firmware
description: Embed the exported model and recording, link the CPU operators and Ethos-U delegate, and inspect the HP firmware memory use.
weight: 5
layout: learningpathall
---

## Inspect the application configuration

The application in `zephyr/samples/silero-vad-ethosu` runs once over the embedded recording. It loads `forward` once and preserves that method's recurrent state for every window. Resetting the board starts an independent stream.

The board-specific files select the HP Ethos-U85-256, enable its clock, and assign application SRAM beginning at `0x020C0000` with size `0x740000` bytes. This is a 7.25 MiB application region for the pinned E8 memory map. It is not portable to another board or a concurrently running application that owns the same SRAM.

The starting allocation capacities are:

| Allocation | Capacity or source |
| --- | --- |
| Method and planned buffers | 2 MiB static allocator pool |
| Temporary delegate allocations | 1 MiB static allocator pool |
| PTE copy | Exported PTE size, aligned to 16 bytes in SRAM |
| C/C++ heap | 64 KiB |
| Main stack | 16 KiB |
| Audio | Up to 40,000 normalized float32 samples generated from the PCM16 WAV |

These are configured capacities, not measurements of model demand. The generated audio array occupies 160,000 bytes for this clip. The PTE and audio begin in the firmware image; startup copies the PTE once to SRAM for NPU access. The linker report checks the static allocation footprint. A completed board run is still needed to verify allocator demand and NPU access.

## Build for the HP core

Keep the released Python environment active. Build with absolute paths to the exact PTE and WAV from the previous lesson:

```bash
cd "$EXECUTORCH_ROOT"
west build \
  -b alif_e8_dk/ae822fa0e5597xx0/rtss_hp \
  zephyr/samples/silero-vad-ethosu \
  -d "$SILERO_BUILD" -- \
  -DZEPHYR_EXTRA_MODULES="$EXECUTORCH_ROOT;$SDK_ALIF" \
  -DPython3_EXECUTABLE="$(command -v python)" \
  -DET_PTE_FILE_PATH="$SILERO_OUTPUT/silero_vad_ethos_u.pte" \
  -DAUDIO_PATH="$SILERO_OUTPUT/validation.wav"
```

The CMake application generates the model/audio headers and selects portable CPU operators from the PTE. It links those registrations, the quantized kernels, and the Ethos-U backend into the firmware. The app also rejects inputs that do not match the single float32 `[1,576]` audio tensor and single float32 probability output.

If you change the board, PTE, WAV, or allocation configuration, rebuild in a new directory or use `west build -p always` with the complete command. This avoids keeping headers or operator selections from an earlier model.

## Check the firmware and memory placement

Require the ELF and binary, then inspect the generated target and allocator configuration:

```bash
test -s "$SILERO_BUILD/zephyr/zephyr.elf"
test -s "$SILERO_BUILD/zephyr/zephyr.bin"
rg 'CONFIG_(RTSS_HP|ARM_ETHOS_U85_256|EXECUTORCH_.*ALLOCATOR_POOL_SIZE)=' \
  "$SILERO_BUILD/zephyr/.config"
rg -n 'app_sram|020c0000|20c0000|ethosu' \
  "$SILERO_BUILD/zephyr/zephyr.dts"
"$ZEPHYR_SDK_INSTALL_DIR/arm-zephyr-eabi/bin/arm-zephyr-eabi-size" \
  "$SILERO_BUILD/zephyr/zephyr.elf"
```

Require the HP target and `CONFIG_ARM_ETHOS_U85_256=y`. Keep the memory-usage report printed by the linker and inspect `zephyr.map` if a region is close to its limit. The `.bss` includes allocator capacities and the PTE copy; unused space inside a pool is still reserved in the linked firmware.

Successful linking proves that the firmware fits the configured static regions. It does not prove that `load_method()` or the largest delegate allocation fits at runtime. The application prints its planned buffer sizes during startup and reports allocation or execution failures; retain those messages during validation.

The local cross-build with the pinned source, vendor modules, Zephyr SDK 0.17.0, and released Python environment passed. Its linker report is:

| Region | Used | Available | Utilization |
| --- | --- | --- | --- |
| Flash application partition | 830,084 bytes | 3,584 KiB | 22.62% |
| Application RAM | 3,597,440 bytes | 7,424 KiB | 47.32% |

The binary is linked at `0x80200000`, including the vendor flash load offset. These are cross-build results, not measurements from a running E8. Physical execution and probability agreement remain to be checked.

Record the firmware identity alongside the model inputs:

```bash
shasum -a 256 "$SILERO_BUILD/zephyr/zephyr.elf" \
  "$SILERO_BUILD/zephyr/zephyr.bin" \
  > "$SILERO_OUTPUT/firmware.sha256"
```

## What you've accomplished

You have built one firmware image containing the recorded clip, exported program, CPU kernels, and U85 delegate, and checked its configured memory placement. Next, program this matching image onto the E8 HP core.
