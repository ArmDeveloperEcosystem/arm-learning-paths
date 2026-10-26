---
title: Replace the speech recognition model
description: Replace Parakeet with Moonshine in your speech translation pipeline and verify both runs without changing your Python application.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand what changes when you replace a model

Speech-to-text (`stt`) is a brick type: audio and a sample rate go in, and text comes out. A brick implementation, such as `stt:parakeet-tdt`, provides the code that runs supported models. A model package supplies the trained weights and assets; its manifest selects the implementation and configures how those files are used.

You'll replace both the Parakeet implementation and its model package with `stt:moonshine` and `moonshine-base-en`. Both implementations follow `stt.v1`, even though Parakeet uses LiteRT and Moonshine uses ONNX Runtime.

Your Python script stays unchanged: `cf.load_manifest(args.stt_manifest)` reads the manifest supplied as an argument, `cf.load_brick(stt_manifest)` selects its implementation, and `stt.setup(stt_manifest, options)` prepares the models. No model name, weights path, or inference backend is hardcoded into these calls. The same `stt.run(stt_input)` loop returns text for the translation stage.

Moonshine Base English recognizes English only and expects 16 kHz audio, so keep using the same `beckett.wav` recording.

## Install Moonshine and rebuild Compute Flow

Use the same Compute Flow checkout and activated virtual environment as before. List Moonshine's models, install the English package, and inspect its manifest:

```bash
compute-flow model list stt:moonshine
compute-flow model install stt:moonshine moonshine-base-en
compute-flow model info stt:moonshine moonshine-base-en
```

The package contains `moonshine_manifest_base_en.json`. Build Compute Flow again to include the newly installed implementation:

```bash
compute-flow build native
```

This build adds the Moonshine implementation to the available bricks. You don't edit your Python application or replace the other models. Selecting a different manifest works only when its brick implementation has been built and its model assets are installed.

## Run the same application with Moonshine

Resolve the package paths again so this command also works in a fresh terminal with the environment activated. Keep using the Parakeet package's recording to hold the input constant:

```bash
MOONSHINE_PACKAGE="$(compute-flow model path stt:moonshine moonshine-base-en)"
PARAKEET_PACKAGE="$(compute-flow model path stt:parakeet-tdt parakeet-tdt-0-6b-v3-int8-dynamic)"
HY_MT2_PACKAGE="$(compute-flow model path lm_text:lm-text-generic hy-mt2-1-8b-2bit-translation)"
QWEN3_TTS_PACKAGE="$(compute-flow model path tts:qwen3-tts qwen3-tts-0-6b-custom-voice)"

python audio_translation_example/audio_translation.py \
  --stt-manifest "$MOONSHINE_PACKAGE/moonshine_manifest_base_en.json" \
  --translation-manifest "$HY_MT2_PACKAGE/hy_mt2_1_8b_manifest.json" \
  --tts-manifest "$QWEN3_TTS_PACKAGE/qwen3_tts_custom_voice_en_manifest.json" \
  --input "$PARAKEET_PACKAGE/samples/beckett.wav" \
  --source-language English \
  --destination-language French \
  --output translated_french_moonshine.wav
```

Only the `--stt-manifest` and output filename differ from your first run. The new manifest selects Moonshine while the same generation loop consumes its text output. The other two stages continue to receive text through the same interfaces.

If the manifest can't be loaded, check the path reported by `model info`. If the brick implementation is unavailable, confirm that the native build succeeded after installing Moonshine and that you're using the same virtual environment.


## Easily Compare speech recognition performance

Use the built STT CLI to compare the speech recognition stage. Changing the manifest lets you experiment quickly with another model.

Parakeet's model files total approximately 683 MB, with dynamic INT8 quantization for fully connected weights and FP32 external interfaces. Moonshine's FP32 model files total approximately 247 MB. These are different model families using LiteRT and ONNX Runtime respectively.

Use the package variables from the previous commands. Run both alternatives on the same mono 16 kHz recording, with one CPU thread and profiling enabled:

```bash
INPUT_AUDIO="$PARAKEET_PACKAGE/samples/beckett.wav"
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

The output is similar to this captured excerpt, showing the featurizer's operator breakdown and the complete scope summary. The first-call report and other operator tables are omitted:

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

The output is similar to this captured report. This ONNX Runtime runner reports model timings without operator details:

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

These timings exclude setup and warmup, include profiling overhead, and use a single 9.963-second audio sample. We haven't assessed changes in transcription accuracy. On an Apple M3 Pro, Moonshine takes 290.30 ms versus Parakeet's 985.12 ms. Compare total `run()` time: Parakeet's 30 streaming calls complete one transcription, not 30 benchmark repetitions.

Pass your own representative audio samples in a JSON file with `-j runs.json` to evaluate more inputs. The shared Python API and CLI let you quickly profile models across different runtimes and find the most suitable model for your application by changing manifests.

## What you've accomplished

You've learned how brick types, implementations, model packages, and manifests fit together. You used Brick Manager to install models and build Compute Flow on your Apple silicon Mac, then connected speech recognition, translation, and speech synthesis in Python to turn an English recording into a French WAV file locally.

Finally, you replaced Parakeet with Moonshine by installing its brick and model package, rebuilding, and selecting a different manifest. The shared speech-to-text interface kept your Python script unchanged. You can use this approach to combine other bricks and select compatible models for your own applications.
