---
title: Diagnose export and E8 execution failures
description: Locate failures at the package, export, firmware, programming, and streaming-output checkpoints.
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
| Toolkit cannot find the E8 | Check PRG USB data connectivity, SEUART switch position, serial-port ownership, and the toolkit's silicon revision. |
| Boot succeeds but inference faults or hangs | Check NPU power/clock, U85 driver selection, SRAM placement/access, and model/runtime compatibility. Retain the complete fault and delegate logs. |
| Only silence or no `SEGMENT` lines | First require all 79 `PROB` values and compare them. A segment is conditional on the probabilities; its absence alone is not a capture failure. |

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

Finish the probability comparison before measuring latency or extending input capture. The application reports an inference-loop duration that includes frame preparation, method execution, and output retrieval, while probability printing happens afterward. That duration is not an NPU-only measurement, and 32 ms is the audio-window step rather than measured execution time.

The local port has no retained physical-board probability or timing result yet. Record the first successful E8 run with its firmware/model hashes and clocks before adding hardware claims to this Learning Path. The existing FVP evidence remains useful for the export and reference flow, but does not substitute for the E8 checks.

## What you've learned

You can locate a failure in the host environment, export, firmware, board connection, or streaming contract. After the E8 comparison passes, the next extension is to replace the prerecorded input with a microphone pipeline that supplies the same 512-sample step and preserves both forms of state.
