---
title: Validate the live camera and NPU loop
description: Check advancing UART frames, camera and NPU errors, and the limits of numerical and scene-accuracy evidence.
weight: 7
layout: learningpathall
---

## Establish each stage of execution

The default camera-and-UART application leaves its display disabled. After the verified MRAM install, capture UART4 before a probe-only reset-pin boot. The sample waits seven seconds before its first camera stream, so allow startup to complete.

{{% notice Important %}}
The final default build passed two independent reset-pin runs on E8 A0 with no reported errors: 9 advancing frames during a 35-second observation and 40 during a 120-second observation. The optional dashboard retains known DSI acknowledgment and packet errors. The original strict PT2E comparison failed and remains recorded separately from integer TOSA agreement.
{{% /notice %}}

Check these stages in order:

1. OSPI is ready and the model opens at the configured address and size.
2. The method loads and exposes the expected int8 image input and outputs.
3. The MT9M114 initializes and the camera stream produces a frame.
4. `method.execute()` returns successfully and mask selection completes.
5. UART reports strictly increasing frame numbers and the buffer is requeued for the next capture.
6. The complete log contains no camera, CSI, NPU, or execution failure for the recorded run.

A model-load message or one frame alone is insufficient. The default build prints `Camera + NPU mode; on-board dashboard disabled`; it should not initialize a DSI host or switch the MIPI route to the display. A blank screen is expected.

## Capture UART before boot

With board power disconnected, select **UART4 on SW4**, then reconnect PRG USB. The onboard bridge carries the HP console at 115200 baud, 8N1. Find the serial device and capture the complete output:

```bash
python -m serial.tools.list_ports
export ALIF_CONSOLE=/dev/cu.replace-with-your-application-uart
python -u -m serial.tools.miniterm "$ALIF_CONSOLE" 115200 --raw \
  2>&1 | tee "$MOBILE_SAM_OUTPUT/mobilesam-uart.log"
```

With capture running, use the programming terminal and its selected-probe wrapper to run the verified live package's `03-reset-probe-only.jlink`. That script pulses the reset pin without attaching a CPU. Keep startup and all error messages in one log. Exit capture with **Ctrl+]** after the observation period.

Return SW4 to SEUART only for SETOOLS ISP. J-Link SWD works with SW4 left on UART4. Disconnect power before changing the switch. The source prints messages similar to:

```output
Camera + NPU mode; on-board dashboard disabled
Camera ready: MT9M114 to planar RGB 384x384
Frame 9: 1338 ms, 1 objects
```

The frame line above illustrates the format; record the values from your build. Require at least three strictly increasing frame numbers, then retain a longer uninterrupted run to check for later failures. A selected-mask count of zero is valid when no proposal passes the quality, area, and overlap rules. Counts are selected prompt regions, not semantic classes.

## Inspect the recorded default-build result

The verified firmware used the raw build hash `3be06219380e7d2444d0b18bef8ebaa42284f401aed2d8e3e5d720c50edc4a36` and the padded programming hash `6d782da186b607a815f7b4d3e4bed8dd0bb6bc1d6ca8c1a630fed4120472e25a`. Fresh debugger processes read back both the staged firmware and signed AToC package exactly before reset-pin boot.

| Independent reset-pin run | UART observation | Completed frames | Reported execution time | Reported errors |
| --- | ---: | ---: | ---: | ---: |
| 1 | 35 seconds | 1–9 | 1338 ms per frame | 0 |
| 2 | 120 seconds | 1–40 | 1338 ms per frame | 0 |

All 49 frame numbers advanced within their own boot epoch. The complete logs contained no CSI, DSI, NPU, or execution error reports. These are bounded observations on the tested A0 board, not an indefinite reliability or cold-power-cycle test. The milliseconds cover `method.execute()`; the observation windows are not measurements of complete-loop latency.

The same default firmware was also paused after frame 23 completed inference and mask selection, before the next camera requeue. Its exact 442,368-byte int8 input was supplied to the retained post-lowering TOSA graph. All 110,592 mask codes and 12 quality codes matched the NPU outputs exactly. Input and outputs were stable across the capture stops, and the debugger-visible planned outputs agreed with the NPU scratch outputs. This is separate evidence from the uninterrupted UART observations above.

## Inspect diagnostics only when needed

UART is the primary liveness evidence. For developer diagnosis, the sample exposes `camera_diagnostics`: entries 19, 20, and 21 hold the frame number, inference milliseconds, and selected-mask count. Resolve its address from the exact flashed ELF; the default build need not contain GDB type information.

```bash
(
set -e
diagnostic_symbol=$("$ZEPHYR_SDK_INSTALL_DIR/arm-zephyr-eabi/bin/arm-zephyr-eabi-nm" \
  --defined-only "$MOBILE_SAM_OUTPUT/build-mobilesam-live/zephyr/zephyr.elf" | \
  awk '$3 == "camera_diagnostics" {print $1}')
test -n "$diagnostic_symbol"
diagnostic_address=$((0x${diagnostic_symbol} + 19 * 4))
printf 'H\nMem32 0x%x 3\nG\nExit\n' "$diagnostic_address" \
  > "$MOBILE_SAM_OUTPUT/read-camera.jlink"
)
```

Close other J-Link sessions, then use the selected-probe wrapper from the programming lesson:

```bash
"$JLINK_COMMANDER" -Device "$ALIF_DEVICE" -If SWD -Speed 4000 \
  -AutoConnect 1 -NoGui 1 -ExitOnError 1 \
  -CommandFile "$MOBILE_SAM_OUTPUT/read-camera.jlink"
```

The script briefly halts, reads three words, and resumes. It does not reset or program the board. Interpret the words as hexadecimal frame count, milliseconds, and mask count. The address changes with the ELF, and cached CPU writes can make a debugger view stale. A long halt during capture can cause a later camera timeout.

Full tensor capture is a separate developer check. Stop only at a verified post-inference point with capture already complete, derive addresses and sizes from that exact ELF and model schema, and preserve the input with both outputs. The default build excludes `display_result`; a breakpoint from the dashboard's display function is invalid here. Do not reuse old PCs, tensor addresses, or framebuffers.

The reported milliseconds time `method.execute()` only. Capture, normalization, quantization, mask selection, UART printing, and buffer requeue are excluded; measure those separately before reporting complete-loop latency.

## Separate output agreement from scene accuracy

Check image quality against FP32 and integer execution against the retained TOSA graph. Use the same preprocessing, prompt coordinates, and int8 input for each comparison. A PT2E quantized-host reference and an integer TOSA reference can produce different results: PT2E uses floating-point operations between quantizers, while TOSA specifies integer convolution and fixed-point rescaling. The [TOSA rescale specification](https://www.mlplatform.org/tosa/tosa_spec_1_0_1.html#_rescale) defines the `SINGLE_ROUND` arithmetic used by this export.

The public dog image, final default-build frame 23, and an earlier dashboard-frame comparison produced these results for the same public PTE:

| Check | Measured result | Outcome |
| --- | --- | --- |
| Public dog: FP32 versus PT2E | Selected IoU 0.975632; pixel agreement 0.991916 | Original image-quality gate passed |
| Public dog: FP32 versus retained TOSA | Selected IoU 0.974156; pixel agreement 0.991428 | Same gate passed unchanged |
| Final camera-and-UART build, frame 23: NPU versus retained TOSA | All 110,592 mask codes and 12 quality codes identical; zero maximum and mean code error | Bit-exact for this input |
| Earlier dashboard frame: NPU versus PT2E | Mask error: maximum 13 codes, mean 2.08688; quality error: maximum 37 codes | Original strict protocol failed |

Both public-image checks reused the pinned dog image, preprocessing, prompts, and exporter metric function. The unchanged gate requires selected mean IoU at least 0.90 **or** pixel agreement at least 0.96, on prompts with selected quality at least 0.90. The evaluated prompts are zero-based indices 2 and 3. These results establish image quality for that image only.

The final camera comparison used ELF SHA256 `a378d4acd6e52d597303f90d4494e4bbcdf43e91b8d74911a4f5a4dcd8841834` and the raw/staged firmware identities recorded above. Frame 23's int8 input has SHA256 `4fffc6e9c91ae0041cb532354df491bc7e3b34ebb5189ed630662236412116c5`. The matching outputs establish integer execution agreement for this input, not all camera scenes. Target model readback matched the public PTE, and captured planned outputs matched the NPU scratch bytes after a controlled cache clean. After the debugger resumed and disconnected, a separate 20-second observation recorded seven further frames, 53–59, with no reported errors and no intervening reset.

The earlier strict PT2E protocol remains failed: its limits were maximum/mean mask error of 2/0.25 codes and maximum quality error of 2 codes. Two prompts also missed its 0.995 pixel-agreement limit, although candidate choices and quality decisions matched. This is an earlier captured input, not a new strict PT2E test of frame 23. Keep that failed verdict with the successful final TOSA comparison.

The first localized numerical difference was four one-code discrepancies among 1,179,648 first-convolution outputs. Independent integer convolution, fixed-point rescaling, and float64 rounding agreed with TOSA; PT2E FP32 arithmetic crossed four rounding boundaries. This explains the first difference, rather than all final output drift. Preserve each comparison’s ELF, model, metadata, and input identities. A successful final TOSA comparison does not change the failed original strict PT2E verdict.

Advancing UART frames establish progress, not pixel accuracy. An optional dashboard overlay also does not prove pixel accuracy. To evaluate accuracy, retain representative frames and compare masks with a reference or labels using the same preprocessing and prompt coordinates. Counted masks are prompt-selected regions, not semantic object classes, and the four-point grid can miss objects between prompts.

Use the programming chapter's per-chunk CRC and complete flash-readback verification as the model byte-integrity evidence. Model loading and completed inference are separate runtime checks; neither substitutes for verification of all programmed bytes.

Before finishing, identify the evidence you have for each checkpoint and record your source revision, model hash, scene, prompt grid, and timing boundary with the result.

## What you've accomplished

You can distinguish camera/NPU progress, model-transfer integrity, integer execution agreement, and scene accuracy. Record the default-build evidence with its exact artifacts, retain the failed strict PT2E verdict, and treat the dashboard as an optional extension with unresolved DSI errors.
