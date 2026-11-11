---
title: Validate the E8 speech probabilities
description: Capture one board run and compare every speech probability with the quantized host reference.
weight: 7
layout: learningpathall
---

{{% notice Important %}}
Physical E8 execution remains unverified in this local draft. The steps below define the checks to perform on your board; they are not a record of a completed hardware run.
{{% /notice %}}

## Capture one complete application run

Use the UART4 connection and capture command from the programming lesson, with SW4 set to UART4 after programming. Save the output as `$SILERO_OUTPUT/alif-silero.log`.

Start capture before resetting or starting the application. Retain startup messages, every probability line, segment lines, and the completion message `Model executed successfully.`. Capture one run per log file. Concatenating multiple runs duplicates probabilities and invalidates the comparison.

The application emits one `PROB <seconds> <probability> speech|silence` entry per input window. It also reports `SEGMENT <start_seconds> <end_seconds> speech` for consecutive speech frames. Zephyr or ExecuTorch prefixes are acceptable: the comparison script searches within each line for `PROB`.

For the 40,000-sample validation clip, require all **79 probability entries** and a successful completion message. A detected NPU device, successful model load, or first probability alone does not establish completion. Preserve any allocation, missing-operator, or delegate errors instead of filtering them out of the captured log.

## Check the matching host reference

Use `expected_probs.bin` from the same export and validation clip used to build this firmware. It contains one little-endian float32 probability per window: 79 values occupy 316 bytes. Check that the reference is complete before comparing the board log:

```bash
python - "$SILERO_OUTPUT/expected_probs.bin" <<'PY'
from pathlib import Path
import math
import struct
import sys

path = Path(sys.argv[1])
data = path.read_bytes()
assert len(data) == 79 * 4, f"Expected 316 bytes, got {len(data)}"
values = struct.unpack("<79f", data)
assert all(math.isfinite(value) for value in values), "Non-finite reference value"
print(f"Reference contains {len(values)} finite probabilities")
PY
```

The expected output is:

```output
Reference contains 79 finite probabilities
```

Keep the PTE, validation WAV, host reference, firmware ELF, and board log together. Re-exporting a model while retaining an older reference or firmware creates a different test.

## Compare the probability sequence

Run the existing comparison script from the matching ExecuTorch checkout. These options require a maximum absolute probability error of `0.25`, a mean absolute error of `0.02`, and no changed speech/silence decisions at threshold `0.5`:

```bash
python "$EXECUTORCH_ROOT/examples/arm/silero_vad_example_ethos_u/runtime/compare_vad_probs.py" \
  --expected "$SILERO_OUTPUT/expected_probs.bin" \
  --actual-log "$SILERO_OUTPUT/alif-silero.log" \
  --threshold 0.5 \
  --atol 0.25 \
  --mean-atol 0.02 \
  --max-threshold-mismatches 0
```

A successful comparison reports `Compared 79 probability values`, zero threshold mismatches, and `Validation passed`. It also prints the maximum and mean errors measured from your run. Missing values, extra values, non-finite values, exceeded tolerances, or changed threshold decisions cause the command to fail.

The decision test uses `probability > 0.5`. A value equal to `0.5` is silence. The comparator checks probabilities and decisions; it does not compare `SEGMENT` lines or validate segment timestamps.

## Interpret failures before changing tolerances

| Failure | Check first |
| --- | --- |
| No `PROB` entries | Correct application UART, complete boot, successful model load, and first execution |
| Fewer than 79 entries | Truncated capture, reset during execution, inference error, or a shorter embedded clip |
| More than 79 entries | Repeated application runs in one log or a different embedded clip |
| Errors grow across successive windows | Method reloading, recurrent-state reinitialization, or incorrect 64-sample history |
| Only the tail differs | Final-window zero padding and the exact number of embedded samples |
| Small errors change speech labels | Values near the threshold; inspect the differing windows without relaxing the zero-mismatch check |
| Missing CPU operator | Selective portable or quantized operator registration from the exact PTE |

If the comparison fails, retain the failing log and verify the model, clip, initial state, and firmware inputs before trying a larger tolerance. A passing comparison establishes agreement with this quantized host reference on this clip. It does not establish accuracy against labeled speech, performance on other audio, or microphone behavior.

## Record the physical-board evidence

Record the E8 silicon revision, Cortex-M55 HP target, NPU configuration, vendor revisions, dependency versions, model and firmware hashes, linker memory report, and complete UART log. If you measure execution time, state whether it covers one `method.execute()` call or the complete application loop, and retain the clock configuration and measurement method.

Audio timestamps are not wall-clock measurements. Corstone-320 counter values are simulator measurements. Neither can be reported as E8 hardware latency. Confirm the delegated backend is linked and completes on the board before attributing results to NPU execution.

## What you've accomplished

After completing these checks on the E8, you have captured a complete 79-window run and compared every board probability and speech decision with the matching quantized host reference. You have also separated output agreement from accuracy and performance claims.

Next, diagnose any failed checkpoint using the troubleshooting lesson. For a later extension, use separate labeled validation recordings before evaluating a microphone input pipeline.
