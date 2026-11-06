---
title: Diagnose flashing, memory, and camera failures
description: Diagnose model programming, tensor contracts, memory capacity, and camera routing on the Alif E8.
weight: 8
layout: learningpathall
---

## Find the last stage that completed

Start with the last confirmed checkpoint: model transfer, model load, camera initialization, capture, inference, or display. Repeating a successful export cannot fix a camera routing problem; replacing camera hardware cannot fix an invalid model tensor contract.

| Symptom | Likely cause or relevant behavior | Next check |
| --- | --- | --- |
| Export stops at the mask-quality check | Calibration input and candidate selection affect FP32/quantized agreement. | Inspect the generated masks and metrics, correct the calibration input, and require the existing quality gate to pass. |
| SETOOLS cannot access SEUART | An attached terminal can own the programming port. | Close the terminal and keep the board's setup consistent with the vendor workflow. |
| Generic J-Link OSPI programming fails | The large final live model needed the custom board-side writer. | Verify the writer mailbox and complete all block readbacks before flashing the final application. |
| Flash operations conflict with a running application | An application using memory-mapped OSPI can hold the controller. | Run the idle or recovery-writer firmware before modifying the model region. |
| Model load stalls or fails | Earlier variants exposed inappropriate model verification/startup behavior. | Check actual programmed bytes, compiled size, readable mapped address, and matching source/metadata. |
| CMake rejects CPU operators | The configure step finds `aten::` or `dim_order_ops::` entries in the PTE operator list. | Re-export from the supplied source with `--quantized-io` and inspect delegation; preserve both model outputs. |
| Firmware rejects input type, byte count, or output tensors | The model interface does not match the sample and generated metadata. | Run the export lesson's PTE and JSON checks, rebuild firmware with the matching pair, and program the complete matching PTE. |
| Scratch-capacity configuration error | The compiled PTE requires more scratch than the configured arena. | Compare the extracted requirement with the configured pool; inspect linker capacity before increasing it. |
| Planned-buffer or method allocation fails | Scratch capacity and method/planned memory are separate budgets. | Inspect the failed allocation and the method pool rather than enlarging only fast scratch. |
| Sensor identification returns `0x0000` or error 19 | Sensor power/reset/sleep and camera/display routing were not yet correct. | Reuse the pinned MT9M114 selfie overlay and explicit startup sequence. |
| MT9M114 is detected as `0x2481` but capture still fails | Detection established the sensor's presence; it did not establish streaming. | Check deferred initialization, RAW10 input format, planar RGB output, routing, and first-stream stabilization. |
| No camera frames after initialization | Camera and display share an external MIPI route controlled through GPIO14.2. | Inspect camera-select state and the capture/display alternation in the sample. |
| First frame takes several seconds | The final code waits seven seconds before starting the sensor stream. | Wait for startup to complete before diagnosing a persistent capture failure. |
| Objects are missing or duplicated | Fixed prompts, quality filtering, area filtering, and duplicate suppression determine the displayed subset. | Inspect candidate masks and prompt coverage before changing model precision. |

The GPIO14.2 MIPI selector is separate from SW4's serial routing. The successful live-camera fix was implemented in firmware; it did not require repeatedly moving SW4.

## Retain the final camera configuration

The final code chooses the MT9M114 selfie sensor, performs its board-specific power/reset/sleep sequence, initializes the sensor late, configures RAW10 capture and planar RGB output, and waits before streaming. After a frame is dequeued, it routes MIPI to the display. Before requeueing, it routes back to the camera and restarts the stream.

Use the supplied sample and pinned SDK overlay together. A successful chip-ID probe confirms only the sensor connection; capture still requires the complete initialization and routing sequence.

## Keep future ports consistent

Treat a dependency or source refresh as a new configuration to validate. The separate public FVP example has a different model interface and newer Arm backend passes; its successful execution does not validate this board application.

The supplied patch selects released PyTorch and TorchAO packages by default. Keep its installer and source checkout together when recreating the environment, and record the resolved versions with your validation results. Re-export the model and rebuild firmware together after changing dependencies.

Zero or unavailable counters in fast FVP mode do not prove CPU fallback. Inspect delegation and completed execution separately. Compiler cycle estimates, timed simulator counters, and physical-device inference duration describe different measurements; retain that distinction when comparing changes.

## What you've accomplished

You've exported a quantized MobileSAM program, built its Zephyr application, and programmed the model and firmware on an Alif Ensemble E8. You've also checked the camera, inference, and display stages separately, so you can identify where a later deployment stops making progress.

## Extend the application

Choose one change for your next experiment:

- Change the prompt grid, re-export, and compare mask coverage on representative scenes
- Change input resolution and repeat the quality, scratch-capacity, linker, and target-output checks
- Measure capture, preprocessing, inference, mask selection, and display separately to locate the largest part of the frame time
- Refresh dependencies or vendor revisions in a separate workspace and repeat export, build, model readback, and live execution

Keep the resolved dependencies, model and firmware hashes, programming log, memory report, and output comparisons with each run. Record the scene, prompt grid, and timing boundary so you can compare results after a change.
