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

Resolve the Parakeet package path for its manifest. Run both alternatives on the same mono 16 kHz recording, with one CPU thread and profiling enabled:

```bash
PARAKEET_PACKAGE="$(compute-flow model path stt:parakeet-tdt parakeet-tdt-0-6b-v3-int8-dynamic)"
INPUT_AUDIO="$MOONSHINE_PACKAGE/samples/beckett.wav"
```

{{< tabpane-normal >}}
  {{< tab header="Parakeet dynamic INT8" >}}
Run the Parakeet manifest:

```bash
./build_native/stt_cli \
  -m "$PARAKEET_PACKAGE/parakeet_tdt_0_6b_v3_manifest.json" \
  -a "$INPUT_AUDIO" \
  -t 1 --enable-op-profiling
```

The output is similar to the following. The operator breakdown has been omitted for brevity.

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

The output is similar to the following. The operator breakdown has been omitted for brevity.


```output
[TRANSCRIPTION]
Ever tried ever failed, no matter try again fail again fail better.
----------------
Scope: run() [total ms: 290.30]
Scope stats | calls: 1 | avg ms: 290.30 | min ms: 290.30 | max ms: 290.30
```
  {{< /tab >}}
{{< /tabpane-normal >}}

Compare the total `run()` time. Parakeet's 30 streaming calls complete one transcription compared with a single call for Moonshine.

These results are one example of how to compare the models; your timings will vary with your hardware and setup. On an Apple M3 Pro, Moonshine took 290.30 ms and Parakeet took 985.12 ms to process a single 9.963-second audio sample. The timings exclude setup and warmup, include profiling overhead, and do not assess transcription accuracy.

Pass your own representative audio samples in a JSON file with `-j runs.json` to evaluate more inputs. The shared Python API and CLI let you quickly profile models across different runtimes and find the most suitable model for your application by changing manifests.

## What you've accomplished

You've compared speech recognition performance between Parakeet and Moonshine. 

You can extend the Learning Path to combine other bricks and select compatible models for your own applications.
