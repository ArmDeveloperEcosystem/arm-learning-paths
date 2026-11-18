---
title: Diagnose export and E8 execution failures
description: Locate failures at the package, export, firmware, programming, and streaming-output, microphone, and display checkpoints.
weight: 8
layout: learningpathall
---

## Start with the first failed checkpoint

Keep the exporter log, frozen west manifest, resolved Python requirements, model hashes, ELF/map, and complete UART capture. Work from the earliest failing step before changing the model or numerical tolerances.

| Symptom | Likely checkpoint and next action |
| --- | --- |
| Export import or native-library error | Activate the Python 3.12 environment from preparation. Check the released package versions and avoid mixing another checkout's editable installation with this environment. |
| WAV rejected | Require uncompressed mono PCM16 at 16 kHz. Generate `validation.wav` from the pinned `test.wav` using the supplied helper. |
| Export fails during state-buffer handling | Use the exact pinned exporter and ExecuTorch package. The serialized quantized initial state is part of the model contract. |
| Board qualifier or devicetree property missing | Check both vendor commits and the full `rtss_hp` target. This sample depends on the vendor fork's E8 bindings. |
| U55 selected or driver configuration conflict | Use the supplied E8 board configuration and U85-256 target. Clean the build directory after changing an NPU selection. |
| CPU operator missing at load or execution | Rebuild registrations from the exact PTE, including portable and quantized kernels. CPU state updates are required. |
| Linker RAM overflow | Inspect `zephyr.map`, the PTE-copy size, and static allocator pools. Check the intended `APP_RAM` region before changing capacities. |
| `load_method` or temporary allocation failure | Retain the reported planned sizes and allocator error. Linking alone does not establish runtime pool sufficiency. Increase only the relevant pool within the verified SRAM budget, then rebuild. |
| Neither J-Link nor the UART appears | With power disconnected, verify SW3 JLOB=EN. Use PRG USB with a known data-capable cable; try a direct Mac connection to isolate a hub. A power LED alone does not prove USB data connectivity. See the [official E8 User Guide](https://alifsemi.com/download/AUGD0023). |
| SETOOLS ISP cannot find the E8 | Check SW4 SEUART, serial-port ownership, and the A0 toolkit configuration. SWD uses the separate debug route and can leave SW4 on UART4. |
| Wrong probe selected | Set the intended numeric JLINK_SERIAL and use the executable wrapper from the programming lesson. The serial number is not the UART device path. |
| HP reports no AHB ROM | Try the documented fresh HE read check before preparing the package. Keep the image targeted to HP; stop if neither core can read MRAM. |
| Preparation helper rejects alignment or map | Pad the raw firmware before signing, regenerate its own package, and pass the matching staged binary and APP Package Summary map. Never pad a signed artifact. |
| Readback differs or the old image boots | Require both fresh-process readbacks to pass before boot. Use the probe-only R0/R1 reset script; do not substitute a CPU-connected generic r reset. |
| First invocation reports NPU status `0x804`, `qread=0`, then ExecuTorch `0x23` | This was the initial SRAM-routing failure. Use the corrected application: command fetch and weight region 0 select SRAM, and the cache-line-aligned PTE copy is cleaned before loading. Rebuild and reprogram the matching firmware. Do not relax probability tolerances to address a bus abort. |
| Boot succeeds but inference faults or hangs | Check NPU power/clock, U85 driver selection, SRAM placement/access, and model/runtime compatibility. Retain the complete fault and delegate logs. |
| No `PROB` or completion records, but `LIVE frame=...` advances | The default microphone configuration is running. Use `validation.conf` in a fresh validation build for the 79-value comparison. Live mode does not produce that sequence or a completion message. |
| **PRERECORDED CLIP** loops while speaking has no effect | The deterministic configuration is installed. Build and program the default live image with its own package and readbacks; do not add microphone assumptions to cached replay. |
| PDM device is not ready or startup fails | Require the supplied overlay with `pdm` enabled, default `CONFIG_SILERO_LIVE_AUDIO=y`, and the pinned vendor drivers. Retain the exact configure/start error. |
| Wrong capture rate despite `pcm_rate=16000` | Keep `PDM_MODE_HIGH_QUALITY_512_CLK_FRQ` (mode 2). This pinned driver does not derive its clock from the requested PCM rate. Verify frame progress against wall time. |
| PDM read timeout or block/latency error | Stop and retain the full log. Blocks must be 1,024 bytes; the app stops when seven or more of eight slabs are in use. Check execution rate and scheduling before increasing buffers. |
| Finite probabilities but captured time falls behind wall time | Inspect LIVE frame/elapsed differences and buffered maximum. The vendor driver may handle a FIFO overflow without reporting an application error; finite output and a low buffer count alone cannot establish continuous capture. |
| Microphone level does not change with sound | Check that live mode is installed and PDM channel 4 is selected. Verify sound reaches the microphones on the board's bottom side, identified in the [E8 User Guide](https://alifsemi.com/download/AUGD0023). Keep the supplied phase, FIR, DC-blocking, and default 50× gain settings; inspect RMS/peak response before changing the threshold. |
| Flat probability with very low microphone levels | Check acoustic input, orientation, and reported gain. The supplied PTE input quantizer has scale about `0.0037879`; low-amplitude signals can fall below its resolution. This application uses a locally calibrated 50× hardware gain, matching the SDK source fallback rather than its configured 20× LE-audio default. Keep the PTE and threshold unchanged while checking the input path. |
| Nonzero or increasing `clipped` count | Exact PCM16 extrema indicate saturation. Check sound level and microphone gain, then repeat quiet and speech tests with a new log. A model probability is not a clipping detector. |
| Loud sound has energy but no speech decision | VAD detects speech patterns, not a generic amplitude trigger. Test ordinary speech and quiet, then use labeled recordings for accuracy evaluation. |
| Display is blank or stops updating | Keep panel/CDC/DSI and cache-flush errors. Require display nodes and the static display route from the application overlay. Check the physical panel as well as framebuffer pixels; this app never switches to a camera. |
| Only silence or no `SEGMENT` records in validation mode | First require all 79 `PROB` values and compare them. Segments depend on the probabilities. Live mode instead counts speech transitions on its dashboard. |

## Check the Python environment

Print the host package versions using the active interpreter:

```bash
python - <<'PY'
from importlib.metadata import version

for package in ("torch", "torchao", "executorch", "ethos-u-vela", "west"):
    print(f"{package}=={version(package)}")
PY
```

Require PyTorch `2.14.0`, TorchAO `0.18.0`, ExecuTorch `1.5.1`, and west `1.5.0`. Record the Vela version resolved by the released Ethos-U extra. If these differ from the saved requirements, recreate the isolated environment using the preparation lesson before debugging the export.

## Check state and framing before tolerances

If probabilities differ, verify the exact PTE, reference, and audio hashes first. Then check that the firmware:

1. Loads the method once for the recording.
2. Starts waveform history at zero and retains the last 64 actual samples between calls.
3. Preserves the model's initialized hidden/cell state between invocations.
4. Divides PCM16 samples by 32,768 and zero-pads the final incomplete window.
5. Captures exactly one 79-window run in the log.

The final frame contains only 64 new samples. A tail-only difference often points to padding or history handling. Divergence that grows over the recording can indicate recurrent-state resets or incorrect initialization. Replacing serialized int8 initial values with literal zero bytes changes the quantized state when its zero point is nonzero.

## Separate validation from performance work

Finish the probability comparison before measuring latency or extending input capture. Validation mode reports a complete inference-loop duration including preparation, execution, and output retrieval, before printing probabilities. Live mode reports per-window execution plus output retrieval, excluding input preparation and microphone waiting. Neither is an NPU-only duration. The 32 ms audio step and the display refresh interval are not measured execution times.

The source-ZIP validation configuration passed its complete 79-window E8 comparison, and the 50× gain live configuration demonstrated microphone response with the observed capture rate. Keep each configuration's source, firmware/model hashes, complete logs, and evidence separate. The sparse live diagnostics are a functional health check rather than a labeled accuracy benchmark.

## What you've learned

You can locate a failure in the host environment, export, firmware, board connection, or streaming contract. Complete the known-input comparison before diagnosing live microphone behavior. Preserve the 512-sample step and both forms of streaming state when extending the pipeline.
