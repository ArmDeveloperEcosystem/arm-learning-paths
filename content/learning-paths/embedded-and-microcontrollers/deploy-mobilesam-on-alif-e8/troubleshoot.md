---
title: Diagnose flashing, memory, and camera failures
description: Diagnose model programming, tensor contracts, memory capacity, and camera routing on the Alif E8.
weight: 8
layout: learningpathall
---

## Find the last stage that completed

Start with the last confirmed checkpoint: model transfer, model load, camera initialization, capture, inference, or advancing UART frames. Identify the build first: the default application uses camera/NPU/UART, while the optional dashboard adds the display and shared-route lifecycle.

| Symptom | Likely cause or relevant behavior | Next check |
| --- | --- | --- |
| Export stops at the mask-quality check | Calibration input and candidate selection affect FP32/quantized agreement. | Inspect the generated masks and metrics, correct the calibration input, and require the existing quality gate to pass. |
| Neither the J-Link probe nor a USB modem serial port appears | The host has not enumerated the programming/debug USB connection. | Follow the USB visibility checks below before retrying SETOOLS. |
| SETOOLS cannot open the programming port | An attached terminal can own the port. | Close the terminal before programming. |
| SETOOLS times out while the USB bridge shows application boot or frame messages | SW4 is routing the bridge to UART4 rather than the Security Enclave programming UART. | Disconnect board power, select SEUART on SW4, reconnect PRG USB, and retry the toolkit. Use UART4 afterward for the application console. |
| Generic J-Link OSPI programming fails | The large final live model needed the custom board-side writer. | Verify the writer mailbox and complete all block readbacks before flashing the final application. |
| Model transfer prints only the initial erase message for six minutes or longer | The writer erases 3,252 sectors before printing transfer progress. | Keep the process running until completion or a specific error; do not interrupt merely because progress is silent. |
| A successful MRAM download still boots the previous image | A generic HP reset can leave the Security Enclave's boot selection unchanged. | Require fresh-process payload readbacks, then run the separate probe-only `R0`/`R1` reset-pin sequence from the programming lesson. |
| Same-process MRAM readback matches after a download | Commander can return its flash-download cache. | Repeat `SaveBin` in a new process with no preceding downloads and compare both payloads with the helper. |
| Flash operations conflict with a running application | An application using memory-mapped OSPI can hold the controller. | Run the idle or recovery-writer firmware before modifying the model region. |
| Model load stalls or fails | Earlier variants exposed inappropriate model verification/startup behavior. | Check actual programmed bytes, compiled size, readable mapped address, and matching source/metadata. |
| CMake rejects CPU operators | The configure step finds `aten::` or `dim_order_ops::` entries in the PTE operator list. | Re-export from the supplied source with `--quantized-io` and inspect delegation; preserve both model outputs. |
| Firmware rejects input type, byte count, or output tensors | The model interface does not match the sample and generated metadata. | Run the export lesson's PTE and JSON checks, rebuild firmware with the matching pair, and program the complete matching PTE. |
| Scratch-capacity configuration error | The compiled PTE requires more scratch than the configured arena. | Compare the extracted requirement with the configured pool; inspect linker capacity before increasing it. |
| Planned-buffer or method allocation fails | Scratch capacity and method/planned memory are separate budgets. | Inspect the failed allocation and the method pool rather than enlarging only fast scratch. |
| Sensor identification returns `0x0000` or error 19 | Sensor power/reset/sleep and camera/display routing were not yet correct. | Reuse the pinned MT9M114 selfie overlay and explicit startup sequence. |
| MT9M114 is detected as `0x2481` but capture still fails | Detection established the sensor's presence; it did not establish streaming. | Check deferred initialization, RAW10 input format, planar RGB output, routing, and first-stream stabilization. |
| No camera frames after initialization | GPIO14.2 selects the external MIPI route. | The default build must keep the camera selected after initialization. Verify the headless configuration, pinned camera overlay, and complete startup log. |
| First frame takes several seconds | The final code waits seven seconds before starting the sensor stream. | Wait for startup to complete before diagnosing a persistent capture failure. |
| Display stays blank in the default build | The dashboard is disabled intentionally. | Require `Camera + NPU mode; on-board dashboard disabled` and advancing UART frames. Use the optional dashboard build only when investigating its known DSI limitation. |
| DSI messages appear in the default camera-and-UART run | A dashboard-enabled or older firmware may be installed. | Check the exact ELF/bin and fresh readbacks. Require `CONFIG_MOBILESAM_DISPLAY`, `CONFIG_DISPLAY`, and `CONFIG_MIPI_DSI` to be disabled in the default build. |
| Optional dashboard reports DSI ACK or packet errors | The shared camera/display link lifecycle remains unresolved. | Retain the full UART log and exact artifacts. Global frame-ACK disabling left the physical display blank in a prior experiment. The dashboard is an experimental extension, not an error-free supported output path. |
| Strict PT2E comparison fails while integer TOSA matches | Quantized-host floating-point arithmetic and integer lowering have different rounding behavior. | Retain both verdicts and exact input/output tensors. Use the validation lesson's integer execution contract; do not relabel or relax the failed original PT2E limits. |
| Selected-mask count is zero or lower than expected | Fixed prompts, quality filtering, area filtering, and duplicate suppression determine the selected subset. | Inspect retained input/masks and prompt coverage before changing model precision. UART counts alone do not establish scene accuracy. |

The GPIO14.2 MIPI selector is separate from SW4's UART routing. The default firmware keeps the camera selected; changing SW4 cannot repair its camera path.

## Check a missing programming USB connection

If both the J-Link probe and the macOS `/dev/cu.usbmodem...` serial device are absent, check the host connection before retrying programming:

- Use **PRG USB**, the USB-C connector on the underside near the board corner. MCU USB can supply power without providing this programming/debug connection.
- Check for the green power LED near the E1 device and SW4. Illumination confirms power, not USB data connectivity.
- Verify **SW3 (JLOB) is EN**. This is separate from **SW4**, which must select SEUART for SETOOLS. Compare the labels with Figure 1 of the [official Alif DK-E8 User Guide (AUGD0023)](https://alifsemi.com/download/AUGD0023). Disconnect board power before adjusting the configuration.
- Test a known USB data cable connected directly to the Mac to isolate a cable, adapter, or hub problem.

Require the probe for the SWD programming lesson and the serial device when using SETOOLS ISP or the application console. SW4 selects the UART signal routed to the bridge; a missing USB connection requires checking the steps above rather than repeatedly changing the UART selection.

## Retain the final camera configuration

The code chooses the MT9M114 selfie sensor, performs its board-specific power/reset/sleep sequence, initializes the sensor late, configures RAW10 capture and planar RGB output, and waits before streaming. In the default build, dequeuing and requeueing do not change the MIPI selector. The camera receiver starts before the upstream sensor, and a completed buffer is returned only after the capture pipeline stops.

Use the supplied sample and pinned SDK overlay together. A successful chip-ID probe confirms only the sensor connection; capture still requires the complete initialization and routing sequence.

## Keep future ports consistent

Treat a dependency or source refresh as a new configuration to validate. The separate public FVP example has a different model interface and newer Arm backend passes; its successful execution does not validate this board application.

The supplied patch selects released PyTorch and TorchAO packages by default. Keep its installer and source checkout together when recreating the environment, and record the resolved versions with your validation results. Re-export the model and rebuild firmware together after changing dependencies.

Zero or unavailable counters in fast FVP mode do not prove CPU fallback. Inspect delegation and completed execution separately. Compiler cycle estimates, timed simulator counters, and physical-device inference duration describe different measurements; retain that distinction when comparing changes.

## What you've accomplished

You can check model-transfer integrity, tensor contracts, camera initialization, and advancing NPU execution separately. Keep the default camera-and-UART evidence distinct from the optional dashboard's DSI errors and the failed strict PT2E comparison.

## Extend the application

Choose one change for your next experiment:

- Change the prompt grid, re-export, and compare mask coverage on representative scenes
- Change input resolution and repeat the quality, scratch-capacity, linker, and target-output checks
- Measure capture, preprocessing, inference, mask selection, and UART reporting separately
- Investigate the optional dashboard's DSI lifecycle in a separate build while preserving the working camera-and-UART firmware
- Refresh dependencies or vendor revisions in a separate workspace and repeat export, build, model readback, and live execution

Keep the resolved dependencies, model and firmware hashes, programming log, memory report, and output comparisons with each run. Record the scene, prompt grid, and timing boundary so you can compare results after a change.
