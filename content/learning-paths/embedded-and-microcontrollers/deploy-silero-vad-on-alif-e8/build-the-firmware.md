---
title: Build validation and live microphone firmware
description: Build two E8 configurations from one application, preserve the SRAM NPU route, and inspect model and framebuffer memory use.
weight: 5
layout: learningpathall
---

## Inspect the shared application

The application in `zephyr/samples/silero-vad-ethosu` defaults to `CONFIG_SILERO_LIVE_AUDIO=y` and `CONFIG_SILERO_MIC_GAIN=50`. It captures the on-board microphone, preserves one loaded method's recurrent state, and updates the live dashboard. Adding `validation.conf` disables microphone capture and selects the embedded recording instead.

Both configurations use the HP Ethos-U85-256 and keep the display route selected continuously. They enable the CDC200, MIPI DSI host, and MW405 panel. The 480 × 800 RGB565 framebuffer uses 768,000 bytes in SRAM0. No camera is initialized.

Application SRAM starts at `0x020C0000` with size `0x740000` bytes, a 7.25 MiB region in this pinned memory map. It is separate from SRAM0 and must not overlap another application. The starting allocation capacities are:

| Allocation | Capacity or source |
| --- | --- |
| Method and planned buffers | 2 MiB static allocator pool |
| Temporary delegate allocations | 1 MiB static allocator pool |
| PTE copy | Exported PTE size, aligned to the 32-byte CPU cache line |
| C/C++ heap and main stack | 64 KiB and 16 KiB |
| Validation audio only | 40,000 normalized float32 samples, 160,000 bytes |
| Live capture only | Eight 1,024-byte PCM16 slab blocks |

These are reserved capacities rather than measurements of model demand. Startup copies the PTE to cache-line-aligned SRAM and cleans it for NPU access. `NPU_QCONFIG=0` and `NPU_REGIONCFG_0=0` route command and weight reads to that SRAM. Retain these settings; the driver's default external-memory command route cannot fetch this copy.

## Build the deterministic configuration first

Keep the released Python environment active. Use a fresh build directory with the exact PTE and WAV from the export lesson:

```bash
cd "$EXECUTORCH_ROOT"
west -z "$ZEPHYR_BASE" build \
  -b alif_e8_dk/ae822fa0e5597xx0/rtss_hp \
  zephyr/samples/silero-vad-ethosu \
  -d "$SILERO_VALIDATION_BUILD" -- \
  -DZEPHYR_EXTRA_MODULES="$EXECUTORCH_ROOT;$SDK_ALIF" \
  -DPython3_EXECUTABLE="$(command -v python)" \
  -DUSER_CACHE_DIR="$SILERO_OUTPUT/cache" \
  -DEXTRA_CONF_FILE=validation.conf \
  -DET_PTE_FILE_PATH="$SILERO_OUTPUT/silero_vad_ethos_u.pte" \
  -DAUDIO_PATH="$SILERO_OUTPUT/validation.wav"
```

This configuration runs the original 79-window model test once and emits its `PROB`, `SEGMENT`, and completion records. Afterward, the dashboard loops cached results under **PRERECORDED CLIP** and **LOOPING RESULTS / NO MICROPHONE**. That replay does not call the model again or produce another probability sequence.

## Build the default microphone configuration

Build the same source in a separate directory. Omit `EXTRA_CONF_FILE` and `AUDIO_PATH`: the default application captures live audio and does not embed the recording.

```bash
west -z "$ZEPHYR_BASE" build \
  -b alif_e8_dk/ae822fa0e5597xx0/rtss_hp \
  zephyr/samples/silero-vad-ethosu \
  -d "$SILERO_LIVE_BUILD" -- \
  -DZEPHYR_EXTRA_MODULES="$EXECUTORCH_ROOT;$SDK_ALIF" \
  -DPython3_EXECUTABLE="$(command -v python)" \
  -DUSER_CACHE_DIR="$SILERO_OUTPUT/cache" \
  -DET_PTE_FILE_PATH="$SILERO_OUTPUT/silero_vad_ethos_u.pte"
```

The application generates the model header and registers the portable CPU operators, quantized kernels, and Ethos-U backend required by the PTE. Both branches require one float32 `[1,576]` input and one float32 probability output. Use a fresh directory or `west build -p always` with the full command after changing the model, configuration, or audio.

## Check both configurations and memory reports

Verify both ELFs and binaries, then inspect the selected modes:

```bash
for build in "$SILERO_VALIDATION_BUILD" "$SILERO_LIVE_BUILD"; do
  test -s "$build/zephyr/zephyr.elf"
  test -s "$build/zephyr/zephyr.bin"
  rg 'CONFIG_(RTSS_HP|ARM_ETHOS_U85_256|SILERO_LIVE_AUDIO|SILERO_MIC_GAIN|AUDIO|AUDIO_DMIC|DISPLAY|MIPI_DSI|FPU_SHARING|EXECUTORCH_.*ALLOCATOR_POOL_SIZE)=' \
    "$build/zephyr/.config"
  "$ZEPHYR_SDK_INSTALL_DIR/arm-zephyr-eabi/bin/arm-zephyr-eabi-size" \
    "$build/zephyr/zephyr.elf"
done
```

Require the HP target, U85-256, display, and MIPI DSI in both builds. The live configuration must have `CONFIG_SILERO_LIVE_AUDIO=y`, `CONFIG_SILERO_MIC_GAIN=50`, microphone audio enabled, and floating-point context sharing enabled. The validation configuration must have `CONFIG_SILERO_LIVE_AUDIO` disabled. Reusing a build directory can retain the wrong input mode, so check `.config` before programming.

The source builds reported these footprints:

| Configuration | Flash application partition (3,584 KiB) | Application RAM (7,424 KiB) | SRAM0 framebuffer (768 KiB) |
| --- | --- | --- | --- |
| Deterministic validation | 846,396 bytes | 3,597,600 bytes | 768,000 bytes |
| Live microphone | 690,312 bytes | 3,611,176 bytes | 768,000 bytes |

The smaller live binary does not embed the 160,000-byte float32 recording. Both images link at `0x80200000`, including the vendor flash offset. SRAM0 has 18,432 bytes remaining after the framebuffer; application RAM is a different region. Retain each linker report and `zephyr.map` rather than adding these regions together.

Successful linking proves static fit. Runtime planned-buffer allocation, completed inference, microphone capture, and display updates still require the board checks. Keep the complete allocation and delegate messages.

Record separate firmware identities:

```bash
for mode in validation live; do
  build="$SILERO_OUTPUT/build-$mode"
  shasum -a 256 "$build/zephyr/zephyr.elf" "$build/zephyr/zephyr.bin" \
    > "$SILERO_OUTPUT/firmware-$mode.sha256"
done
export SILERO_MODE=validation
export SILERO_BUILD="$SILERO_VALIDATION_BUILD"
```

## What you've accomplished

You have built a known-input test and a live microphone application from the same source and model. The selected configuration is initially `validation`. Next, program it, verify its 79 probabilities, then repeat programming with the live image.
