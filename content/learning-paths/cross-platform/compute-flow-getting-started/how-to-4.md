---
title: Compare speech-to-text performance
description: Compare Parakeet and Moonshine speech-to-text performance using the same audio sample.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Compare speech recognition performance

Use the built speech-to-text CLI to compare the speech recognition stage. Changing the manifest lets you experiment quickly with another model.

The Parakeet model files total approximately 683 MB, with dynamic INT8 quantization for fully connected weights and FP32 external interfaces. The Moonshine FP32 model files total approximately 247 MB. These are different model families using LiteRT and ONNX Runtime respectively.

### Compare on an Arm64 device

Resolve the Parakeet package path for its manifest. Run both alternatives on the same mono 16 kHz recording, with one CPU thread and profiling enabled:

```bash
PARAKEET_PACKAGE="$(compute-flow model path stt:parakeet-tdt parakeet-tdt-0-6b-v3-int8-dynamic)"
INPUT_AUDIO="$MOONSHINE_PACKAGE/samples/beckett.wav"
```

The operator breakdowns have been omitted for brevity.


{{< tabpane-normal >}}
  {{< tab header="Parakeet dynamic INT8" >}}
Run the Parakeet manifest:

```bash
./build_native/stt_cli \
  -m "$PARAKEET_PACKAGE/parakeet_tdt_0_6b_v3_manifest.json" \
  -a "$INPUT_AUDIO" \
  -t 1 --enable-op-profiling
```

The output is similar to:

```output
[TRANSCRIPTION]
Ever tried, ever failed. No matter. Try again. Fail again. Fail better.
...
All Calls
Scope: run() [total ms: 985.12]
Scope stats | calls: 30 | avg ms: 32.84 | min ms: 0.34 | max ms: 487.10
```
  {{< /tab >}}
  {{< tab header="Moonshine FP32" >}}
Run the Moonshine manifest:

```bash
./build_native/stt_cli \
  -m "$MOONSHINE_PACKAGE/moonshine_manifest_base_en.json" \
  -a "$INPUT_AUDIO" \
  -t 1 --enable-op-profiling
```

The output is similar to:

```output
[TRANSCRIPTION]
Ever tried ever failed, no matter try again fail again fail better.
----------------
Scope: run() [total ms: 290.30]
Scope stats | calls: 1 | avg ms: 290.30 | min ms: 290.30 | max ms: 290.30
```
  {{< /tab >}}
{{< /tabpane-normal >}}

Compare the total `run()` time. 30 Parakeet streaming calls complete one transcription compared with a single call for Moonshine.

These results are one example of how to compare the models. Your timings will vary with your hardware and setup. On an Apple M3 Pro, Moonshine took 290.30 ms and Parakeet took 985.12 ms to process a single 9.963-second audio sample. The timings exclude setup and warmup, include profiling overhead, and don't assess transcription accuracy.

Pass your own representative audio samples in a JSON file with `-j runs.json` to evaluate more inputs. The shared Python API and CLI let you quickly profile models across different runtimes. You can find the most suitable model for your application by changing manifests.

### Compare on an Android Arm64 phone

Use the Android build and model packages from earlier. Run both models on the same mono 16 kHz recording, with one CPU thread and profiling enabled.

From the Compute Flow repository root, transfer the speech-to-text CLI and make it executable:

```bash
adb push --sync build_android_arm64/stt_cli /data/local/tmp/compute-flow/audio-translation/
adb shell chmod +x /data/local/tmp/compute-flow/audio-translation/stt_cli
```

The following results were measured on a Pixel 8 running Android 16. The operator breakdowns have been omitted for brevity.

{{< tabpane-normal >}}
  {{< tab header="Parakeet dynamic INT8" >}}
Run the Parakeet manifest:

```bash
adb shell 'cd /data/local/tmp/compute-flow/audio-translation &&
  ./stt_cli \
    -m stt/parakeet_tdt_0_6b_v3_manifest.json \
    -a stt/samples/beckett.wav \
    -t 1 --enable-op-profiling'
```

The output is similar to:

```output
[TRANSCRIPTION]
Ever tried, ever failed. No matter. Try again. Fail again. Fail better.
...
All Calls
Scope: run() [total ms: 1154.04]
Scope stats | calls: 30 | avg ms: 38.47 | min ms: 0.36 | max ms: 565.70
```
  {{< /tab >}}
  {{< tab header="Moonshine FP32" >}}
Run the Moonshine manifest with the same input recording:

```bash
adb shell 'cd /data/local/tmp/compute-flow/audio-translation &&
  ./stt_cli \
    -m moonshine/moonshine_manifest_base_en.json \
    -a stt/samples/beckett.wav \
    -t 1 --enable-op-profiling'
```

The output is similar to:

```output
[TRANSCRIPTION]
Ever tried ever failed, no matter try again fail again fail better.
----------------
Scope: run() [total ms: 552.39]
Scope stats | calls: 1 | avg ms: 552.39 | min ms: 552.39 | max ms: 552.39
```
  {{< /tab >}}
{{< /tabpane-normal >}}

Compare the total `run()` time across all calls. On the Pixel 8, Moonshine took 552.39 ms and Parakeet took 1154.04 ms to process the same 9.963-second sample. These are single-run measurements. Your timings will vary with device load, temperature, and hardware. The timings exclude setup and warmup, include profiling overhead, and don't assess transcription accuracy.

## What you've accomplished

You've compared speech recognition performance between Parakeet and Moonshine. 

You can extend the Learning Path to combine other bricks and select compatible models for your own applications.
