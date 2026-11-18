---
title: Validate probabilities and the live microphone
description: Check all 79 deterministic probabilities, then test live speech response, capture rate, buffering, and the on-board display.
weight: 7
layout: learningpathall
---

{{% notice Important %}}
The source-ZIP validation configuration passed all 79 reference checks on E8 A0 `AE822FA0E5597LS0`. The default 50× gain microphone configuration also demonstrated acoustic speech/quiet response while maintaining the observed capture rate. These are separate checks; repeat both for your build.
{{% /notice %}}

## Capture the deterministic configuration

Use the UART4 connection and capture command from the programming lesson, with SW4 set to UART4. J-Link SWD programming can use the same UART4 switch position. Select `SILERO_MODE=validation` and save the output as `$SILERO_OUTPUT/validation/alif-silero.log`.

Start capture before resetting or starting the application. Retain startup messages, every probability line, segment lines, and the completion message `Model executed successfully.`. Capture one reset per log file. Concatenating runs duplicates probabilities and invalidates the comparison. After completion the display loops a cached visualization; keep capture running through several replays and confirm that no additional `PROB` sequence appears. This configuration does not start the microphone.

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

The fresh host reference has **56 speech values strictly above `0.5` and 23 silence values at or below `0.5`**. This is a host result, not a physical-board measurement. Its SHA256 is `b3866370da8e6e7bfbfb38c5bef9aac3a367f69bc402c8a1e4ce342cda91ca8c`; retain your own export hash if reproducing a later artifact.

Keep the PTE, validation WAV, host reference, firmware ELF, and board log together. Re-exporting a model while retaining an older reference or firmware creates a different test.

## Compare the probability sequence

Run the existing comparison script from the matching ExecuTorch checkout. These options require a maximum absolute probability error of `0.25`, a mean absolute error of `0.02`, and no changed speech/silence decisions at threshold `0.5`:

```bash
python "$EXECUTORCH_ROOT/examples/arm/silero_vad_example_ethos_u/runtime/compare_vad_probs.py" \
  --expected "$SILERO_OUTPUT/expected_probs.bin" \
  --actual-log "$SILERO_OUTPUT/validation/alif-silero.log" \
  --threshold 0.5 \
  --atol 0.25 \
  --mean-atol 0.02 \
  --max-threshold-mismatches 0
```

A successful comparison reports `Compared 79 probability values`, zero threshold mismatches, and `Validation passed`. It also prints the maximum and mean errors measured from your run. Missing values, extra values, non-finite values, exceeded tolerances, or changed threshold decisions cause the command to fail.

The decision test uses `probability > 0.5`. A value equal to `0.5` is silence. The comparator checks probabilities and decisions; it does not compare `SEGMENT` lines or validate segment timestamps.

## Inspect the recorded-clip comparison evidence

The source-ZIP validation build completed one captured reset-pin run with **79 probabilities**, **56 speech frames**, **23 silence frames**, two `SEGMENT` records, and exactly one `Model executed successfully.` message, with no reported errors. The original comparator passed with zero threshold-decision mismatches. The staged 846,400-byte firmware and its signed package both matched fresh physical MRAM readbacks before boot.

Comparing the six-decimal UART values with the float32 reference gave a maximum absolute error of approximately **4.70 × 10⁻⁷** and a mean error of **3.17 × 10⁻⁷**. Both print as `0.000000` at the comparator's precision. This compares rounded console values, not raw binary outputs, so it does not establish bit-identical floating-point results.

This test checks the supplied recording and initialized streaming state. It does not measure microphone accuracy or cold power-up behavior.

## Program the live configuration

After the deterministic comparison passes, select and program the microphone image using the full programming procedure:

```bash
export SILERO_MODE=live
export SILERO_BUILD="$SILERO_LIVE_BUILD"
export SILERO_RUN_DIR="$SILERO_OUTPUT/live"
mkdir -p "$SILERO_RUN_DIR"
```

Regenerate the signed package for this binary, prepare a new `mram-silero` directory, and require both fresh physical readbacks before the probe-only reset. Set `SILERO_MODE=live` in the capture terminal too, saving startup and diagnostics as `$SILERO_OUTPUT/live/alif-silero.log`.

Live mode identifies the input as `PDM channel 4, 16000 Hz mono PCM16, 512 samples/window`. It continuously reports `LIVE frame=...` once every 32 windows. It does not emit the recording's `PROB` sequence, replay label, or a final `Model executed successfully.` message.

## Check speech response and the visible display

Observe the physical display while alternating several seconds of quiet with ordinary speech near the board. Use the default 50× hardware gain. Repeat the pattern and keep UART capture running for at least one minute:

1. Require an advancing frame count and **LIVE VOICE ACTIVITY / ON-BOARD MICROPHONE**. **PRERECORDED CLIP** means the validation image is still installed.
2. Speak toward the on-board microphones on the bottom side, shown in the [E8 User Guide](https://alifsemi.com/download/AUGD0023). Check that microphone RMS/peak levels change with sound. Quiet-room probability should settle, while speech should produce speech probabilities and a **SPEECH** indicator. A loud non-speech sound is not guaranteed to count as speech.
3. Check that the recent-probability graph advances, speech activity accumulates, and segment count increases on quiet-to-speech transitions. These are raw threshold decisions, with no additional hangover smoothing.
4. Check `gain=50x` and cumulative `clipped=...` diagnostics. Nonzero clipped counts identify PCM saturation; reduce excessive acoustic level or retest an appropriate hardware gain before claiming clean capture.
5. Retain capture, buffer, NPU, display, and fault messages. A single probability or a static framebuffer is insufficient to establish sustained operation.

The display is an on-board live visualization. No host audio stream, microphone application, network service, or audio playback is required. A debugger framebuffer capture records the board's rendered pixels; direct panel observation is still needed to establish visible updates.

See the [actual E8 framebuffer capture](../understand-the-system/#read-the-live-dashboard) for the live layout. The capture proves the rendered pixels; direct observation of physical panel updates was not part of that captured evidence.

## Check live capture progress

At 16 kHz, 512 samples represent 32 ms and 32 windows represent 1.024 seconds. Compare differences between diagnostics: healthy sustained processing should be close to **31.25 windows per wall-clock second**. The displayed captured time is calculated from processed samples and cannot independently prove the capture rate.

Summarize the saved live log without discarding its original contents:

```bash
python - "$SILERO_OUTPUT/live/alif-silero.log" <<'PY'
from pathlib import Path
import math
import re
import sys

text = Path(sys.argv[1]).read_text(errors="replace")
pattern = (
    r"LIVE frame=(\d+) elapsed_ms=(\d+) p=([0-9.eE+-]+) (speech|quiet) "
    r"rms=([0-9.eE+-]+) peak=([0-9.eE+-]+) "
    r"inference_ms=(\d+) buffered_max=(\d+) gain=(\d+)x clipped=(\d+)"
)
rows = re.findall(pattern, text)
assert len(rows) >= 30, "Capture at least 30 LIVE diagnostics"
frames = [int(row[0]) for row in rows]
times = [int(row[1]) for row in rows]
assert all(b > a for a, b in zip(frames, frames[1:])), "Repeated/reset frame counter"
assert all(b > a for a, b in zip(times, times[1:])), "Repeated/reset elapsed time"
assert not re.search(r"<err>|ERROR|NPU error|HardFault|fatal error|failed|\btimeout\b|\boverflow\b", text, re.I)
for row in rows:
    probability, rms, peak = (float(row[i]) for i in (2, 4, 5))
    assert all(math.isfinite(value) for value in (probability, rms, peak))
    assert 0.0 <= probability <= 1.0 and 0.0 <= rms <= peak <= 1.0
    assert int(row[7]) < 7, "Near-exhausted capture slab"
    assert 1 <= int(row[8]) <= 255, "Unexpected microphone gain"
clipped = [int(row[9]) for row in rows]
assert all(b >= a for a, b in zip(clipped, clipped[1:])), "Clipping counter reset"
seconds = (times[-1] - times[0]) / 1000.0
processed = frames[-1] - frames[0]
print(f"{processed} windows in {seconds:.3f} wall seconds")
print(f"Capture progress: {processed / seconds:.3f} windows/s; expected about 31.25")
print(f"Processed audio / wall time: {processed * 0.032 / seconds:.4f}")
print(f"Maximum reported buffered blocks: {max(int(row[7]) for row in rows)} / 8")
print(f"Hardware gain: {sorted({int(row[8]) for row in rows})}x")
print(f"Clipped PCM samples since boot: {clipped[-1]} / {frames[-1] * 512}")
print(f"New clips between first and last diagnostic: {clipped[-1] - clipped[0]}")
print(f"Reported inference range: {min(int(row[6]) for row in rows)}.."
      f"{max(int(row[6]) for row in rows)} ms")
PY
```

Inspect the reported rate alongside the full log and physical response. A lower sustained rate or growing backlog needs investigation even if probabilities remain finite. The unmodified vendor driver does not expose a complete FIFO-overflow count to this application, so this telemetry is a health check rather than proof that every microphone sample was preserved. The app stops explicitly on a read timeout, wrong block size, or near-exhausted slab.

The inference field measures model execution plus output retrieval. Compare it with the 32 ms audio step, but also check end-to-end capture progress: a short model call alone does not establish that the complete pipeline keeps up.

## Inspect the live E8 result

The 50× gain firmware was tested with speech played acoustically toward the on-board microphone, separated by three quiet intervals. Across **49 sampled UART diagnostics**, 1,536 windows advanced over **49.152 seconds**: **31.25 windows/s**, or 16,000 processed samples/s against the target clock. The maximum reported slab occupancy was **2 of 8**, the sampled execution/output time was **1 ms**, and the complete capture contained no reported errors.

The three quiet intervals each had **0 speech decisions among 8 telemetry samples**. The two voice intervals had **3 of 9** and **6 of 10** sampled speech decisions, reaching probabilities **0.662438** and **0.881944**. Microphone levels increased during voice playback. These are sparse observations, one sampled 32 ms window per 32 invocations, and are not speech accuracy, recall, or false-positive rates over every window.

The cumulative PCM-rail counter was **36 at the first diagnostic and 36 at the last**, so there were **zero new clipped samples between those diagnostics**. The total since boot was not zero. This counter detects exact PCM16 rails, not saturation inside the model's narrower input quantizer.

The captured E8 framebuffer showed the live layout, rolling probability history, microphone level, and accumulated statistics after a checked cache clean. Direct observation of physical panel updates was not part of that captured evidence. The test establishes the observed microphone-to-model response and capture progress; it does not establish microphone frequency response or accuracy on unseen labeled speech.

After the numerical test, the same live image was restored, both payloads were read back again, and a fresh reset was captured for 20 seconds. Its 18 diagnostics advanced from frame 32 to 576 at the expected rate, with maximum occupancy 2 of 8, sampled execution/output times of 1–2 ms, and no reported errors. This separate boot's cumulative clipping counter increased from **38 to 41**, or **three new clipped PCM samples**. Keep this observation separate from the controlled test's unchanged 36-count interval; clipping must be monitored for the actual acoustic level and gain.

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

If the comparison fails, retain the failing log and verify the model, clip, initial state, and firmware inputs before trying a larger tolerance. A passing deterministic comparison establishes agreement with this quantized host reference on this clip. It does not establish accuracy on unseen speech. The live checks establish the separately observed microphone/display behavior and capture health; a labeled accuracy study requires separate recordings.

## Record the physical-board evidence

Record the E8 silicon revision, Cortex-M55 HP target, NPU configuration, vendor revisions, dependency versions, model and firmware hashes, linker memory report, and complete UART log. If you measure execution time, state whether it covers one `method.execute()` call or the complete application loop, and retain the clock configuration and measurement method.

Audio timestamps are not wall-clock measurements. Corstone-320 counter values are simulator measurements. Neither can be reported as E8 hardware latency. Confirm the delegated backend is linked and completes on the board before attributing results to NPU execution.

## What you've accomplished

After completing both configurations, you have compared every known-input probability and speech decision, then checked microphone response, visible dashboard updates, and sustained capture progress on the E8.

Next, diagnose any failed checkpoint using the troubleshooting lesson. For an accuracy study, retain microphone recordings with independent speech labels and evaluate them separately from the calibration clip.
