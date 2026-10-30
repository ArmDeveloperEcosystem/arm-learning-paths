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

The output is similar to this captured excerpt, showing the featurizer operator breakdown and the complete scope summary. The first-call report and other operator tables are omitted:

```output
[TRANSCRIPTION]
Ever tried, ever failed. No matter. Try again. Fail again. Fail better.
...
All Calls
Scope: run() [total ms: 985.12]
Scope stats | calls: 30 | avg ms: 32.84 | min ms: 0.34 | max ms: 487.10
Model + Op Breakdown
runner          contributor                                              calls                                         %      total ms      avg ms      min ms      max ms
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
litert          featurizer
                  GATHER_ND                                                  4 [██████████████░░░░░░░░░░░░░░░░]  45.01%          7.86        1.96        1.94        1.98
                  Fully Connected (NC, QP8, F32, QC8W) GEMM                 12 [████████░░░░░░░░░░░░░░░░░░░░░░]  25.58%          4.46        0.37        0.18        0.49
                  ADD                                                        4 [██████░░░░░░░░░░░░░░░░░░░░░░░░]  19.29%          3.37        0.84        0.81        0.87
                  Multiply (ND)                                             24 [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]   1.27%          0.22        0.01        0.00        0.03
                  Log (NC)                                                   4 [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]   0.85%          0.15        0.04        0.03        0.05
                  Extra Ops                                                    [█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]   2.37%          0.41
                  Overhead                                                     [██░░░░░░░░░░░░░░░░░░░░░░░░░░░░]   5.64%          0.98
...
Scope Summary
runner          contributor                                              calls                                         %      total ms      avg ms      min ms      max ms
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
litert          encoder                                                      2 [█████████████████████████████░]  95.60%        941.76      470.88      469.83      471.93
litert          featurizer                                                   4 [█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]   1.77%         17.45        4.36        4.28        4.44
litert          joint_step                                                  42 [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]   1.43%         14.06        0.33        0.31        0.36
litert          decoder_step                                                30 [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]   1.12%         11.06        0.37        0.34        0.65
                Overhead                                                    30 [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]   0.08%          0.79        0.03
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                Scope Total                                                                                                     985.12
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

The output is similar to the following captured report. This ONNX Runtime runner reports model timings without operator details:

```output
[TRANSCRIPTION]
Ever tried ever failed, no matter try again fail again fail better.
----------------
Scope: run() [total ms: 290.30]
Scope stats | calls: 1 | avg ms: 290.30 | min ms: 290.30 | max ms: 290.30
Scope Summary
runner          contributor                                              calls                                         %      total ms      avg ms      min ms      max ms
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
onnxrt          encoder                                                      1 [██████████████████████░░░░░░░░]  74.69%        216.82      216.82      216.82      216.82
onnxrt          decoder                                                     15 [████████░░░░░░░░░░░░░░░░░░░░░░]  25.21%         73.19        4.88        3.23       25.37
                Overhead                                                     1 [░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]   0.10%          0.29        0.29
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                Scope Total                                                                                                     290.30
```
  {{< /tab >}}
{{< /tabpane-normal >}}

These timings are based on a single 9.963-second audio sample. The timings exclude setup and warmup and include profiling overhead. This isn't an assessment of changes to transcription accuracy. 

On an Apple M3 Pro, Moonshine takes 290.30 ms, while Parakeet takes 985.12 ms to process the audio sample. Compare total `run()` time: 30 Parakeet streaming calls complete one transcription, not 30 benchmark repetitions.

Pass your own representative audio samples in a JSON file with `-j runs.json` to evaluate more inputs. The shared Python API and CLI let you quickly profile models across different runtimes. You can find the most suitable model for your application by changing manifests.

## What you've accomplished

You've compared speech recognition performance between Parakeet and Moonshine. 

You can use the approach described in the Learning Path to combine other bricks and select compatible models for your own applications.
