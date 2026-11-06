---
title: Validate the live camera and segmentation loop
description: Confirm camera startup, advancing frames, inference completion, and meaningful mask output on physical E8 hardware.
weight: 7
layout: learningpathall
---

## Establish each stage of execution

After flashing the final firmware and power-cycling the board, allow the sensor to stabilize. The sample includes a seven-second delay before its first camera stream. A slow first frame during this interval is expected.

The display should show the live camera scene, colored segmentation overlays, inference duration, and selected-object count. Move an object between quadrants and observe whether new frames and masks appear. A successful build or model-load message alone does not establish live segmentation.

Use these checkpoints in order:

1. OSPI is ready and the model opens at the configured address and size.
2. The method loads and exposes an int8 image input with the expected byte count.
3. The MT9M114 sensor initializes and the camera stream produces a frame.
4. `method.execute()` returns successfully.
5. Mask and quality tensors have the expected types and shapes.
6. The display updates, the frame counter advances, and buffers are requeued.

When an application console is routed and available, the source prints messages similar to:

```output
Camera ready: MT9M114 to planar RGB 384x384
Frame 9: 1340 ms, 2 objects
```

These are expected source-generated messages. The reference deployment was confirmed through debugger reads of diagnostic memory; these lines illustrate the console format.

## Inspect progress through the debugger

The supplied sample exposes a 32-bit `camera_diagnostics` array. Entries 19, 20, and 21 contain the frame number, inference milliseconds, and selected-mask count. The default build does not include GDB type information, so resolve the symbol from the exact ELF you flashed and read its words through J-Link Commander.

Use the `nm` executable from your Zephyr SDK to locate the symbol, then create a [J-Link command file](https://kb.segger.com/J-Link_Commander#Batch_processing):

```bash
(
set -e
diagnostic_symbol=$("$ZEPHYR_SDK_INSTALL_DIR/arm-zephyr-eabi/bin/arm-zephyr-eabi-nm" \
  --defined-only "$MOBILE_SAM_OUTPUT/build-mobilesam-live/zephyr/zephyr.elf" | \
  awk '$3 == "camera_diagnostics" {print $1}')
test -n "$diagnostic_symbol"
diagnostic_address=$((0x${diagnostic_symbol} + 19 * 4))
printf 'halt\nmem32 0x%x 3\ng\nexit\n' "$diagnostic_address" \
  > "$MOBILE_SAM_OUTPUT/read-camera.jlink"
)
```

Close other J-Link sessions and take a snapshot. The command file halts for the read and resumes with `g` before disconnecting; it does not reset or program the board:

```bash
"$JLINK_COMMANDER" -device "$ALIF_DEVICE" -if SWD -speed 4000 \
  -autoconnect 1 -ExitOnError 1 \
  -CommandFile "$MOBILE_SAM_OUTPUT/read-camera.jlink"
```

In the three-word `mem32` result, interpret the values in order as hexadecimal frame count, milliseconds, and mask count. For example, `00000004 0000053C 00000001` means frame 4, 1340 ms, and one mask. The address depends on your ELF; never reuse an address from a different build.

Let several more frames complete, run the snapshot command again, and confirm that the first word increases. The validated board run recorded:

| Snapshot | Frame number | Inference milliseconds | Selected masks |
| --- | ---: | ---: | ---: |
| First advancing live snapshot | 4 | 1340 | 1 |
| Later advancing live snapshot | 9 | 1340 | 2 |

The reference run used J-Link memory reads. The symbol lookup and generated command file have been checked against the retained ELF; a fresh board run remains pending.

The timer starts immediately before `method.execute()` and stops immediately after it. The 1340 ms excludes capture, camera quantization, mask selection, rendering, and frame requeue. Measure the complete loop separately if you need camera-to-display latency or throughput.

## Separate output agreement from scene accuracy

For a stored image, compare floating-point and quantized-host masks first, then compare target output with the matching quantized-host result. This separates quantization error from later deployment discrepancies.

For the live camera application, a changing overlay confirms that the pipeline runs, but it does not prove pixel accuracy. To evaluate accuracy, retain representative frames and compare masks with a reference or labels using the same preprocessing and prompt coordinates. Counted masks are prompt-selected regions, not semantic object classes, and the four-point grid can miss objects between prompts.

Do not use the `PTE flash verification: passed` startup string as a checksum result. In the final source it is printed without performing a full model checksum. The programming chapter's readback verification is the relevant byte-integrity evidence.

Before finishing, identify the evidence you have for each checkpoint and record your source revision, model hash, scene, prompt grid, and timing boundary with the result.

## What you've accomplished

You've checked the capture, inference, and display stages and identified what the timing and selected-mask count measure. Use the final lesson to diagnose a failed checkpoint or choose a follow-up experiment.
