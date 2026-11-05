---
title: Replace the speech-to-text brick
description: Replace the Parakeet AI model with Moonshine in your speech-to-text brick
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand what changes when you replace a model

Now that you've built the audio-to-audio pipeline, you can make changes to the speech-to-text component.

Speech-to-text is a brick type: audio and a sample rate go in, and text comes out.

You'll replace both the Parakeet implementation and its model package with `stt:moonshine` and `moonshine-base-en`. Both implementations follow `stt.v1`, even though Parakeet uses LiteRT and Moonshine uses ONNX Runtime.

The Python script remains unchanged. `cf.load_manifest(args.stt_manifest)` reads the manifest supplied as an argument. `cf.load_brick(stt_manifest)` selects its implementation, and `stt.setup(stt_manifest, options)` prepares the models. No model name, weights path, or inference backend is hardcoded into these calls. The same `stt.run(stt_input)` loop returns text for the translation stage.

## Install Moonshine and rebuild Compute Flow

Using the same virtual environment as earlier, list Moonshine models, install the English package, and inspect its manifest:

```bash
compute-flow model list stt:moonshine
compute-flow model install stt:moonshine moonshine-base-en
compute-flow model info stt:moonshine moonshine-base-en
```

The package contains `moonshine_manifest_base_en.json`. 

Build Compute Flow again to include the newly installed implementation:

{{< tabpane code="true" >}}
{{< tab header="Native Arm64" >}}
compute-flow build native
{{< /tab >}}
{{< tab header="Cross-compile for Android Arm64" >}}
compute-flow build android_arm64
cmake --build build_audio_translation_android --parallel
{{< /tab >}}
{{< /tabpane >}}

This build adds the Moonshine implementation to the available bricks. Don't edit your Python application or replace the other models. 

Selecting a different manifest works only when its brick implementation has been built and its model assets are installed.

## Run the same application with Moonshine

Resolve the package paths again so that the command also works in a fresh terminal with the environment activated:

{{< tabpane-normal >}}
{{< tab header="Native Arm64" >}}
```bash
MOONSHINE_PACKAGE="$(compute-flow model path stt:moonshine moonshine-base-en)"
HY_MT2_PACKAGE="$(compute-flow model path lm_text:lm-text-generic hy-mt2-1-8b-2bit-translation)"
QWEN3_TTS_PACKAGE="$(compute-flow model path tts:qwen3-tts qwen3-tts-0-6b-custom-voice)"

python audio_translation_example/audio_translation.py \
  --stt-manifest "$MOONSHINE_PACKAGE/moonshine_manifest_base_en.json" \
  --translation-manifest "$HY_MT2_PACKAGE/hy_mt2_1_8b_manifest.json" \
  --tts-manifest "$QWEN3_TTS_PACKAGE/qwen3_tts_custom_voice_en_manifest.json" \
  --input "$MOONSHINE_PACKAGE/samples/beckett.wav" \
  --source-language English \
  --destination-language French \
  --output translated_french_moonshine.wav
```
{{< /tab >}}
{{< tab header="Cross-compile for Android Arm64" >}}
Push the moonshine model
```bash
adb shell mkdir -p /data/local/tmp/compute-flow/audio-translation/moonshine

adb push --sync "$(compute-flow model path stt:moonshine moonshine-base-en)"/. \
  /data/local/tmp/compute-flow/audio-translation/moonshine/
```

Rerun the application using moonshine. 

```bash
adb push --sync build_audio_translation_android/audio_translation \
  /data/local/tmp/compute-flow/audio-translation/

adb shell 'cd /data/local/tmp/compute-flow/audio-translation &&
  chmod +x audio_translation &&
  ./audio_translation \
    --stt-manifest moonshine/moonshine_manifest_base_en.json \
    --translation-manifest translation/hy_mt2_1_8b_manifest.json \
    --tts-manifest tts/qwen3_tts_custom_voice_en_manifest.json \
    --input stt/samples/beckett.wav \
    --source-language English --destination-language French \
    --output translated_french_moonshine.wav'
```

Retrieve the translated audio sample.

```bash
adb pull /data/local/tmp/compute-flow/audio-translation/translated_french_moonshine.wav \
  audio_translation_example/
```

{{< /tab >}}
{{< /tabpane-normal >}}

The Moonshine package includes the same `beckett.wav` recording that was used in the first run.

## What you've accomplished and what's next

You've replaced Parakeet with Moonshine by installing its brick and model package, rebuilding, and selecting a different manifest. The shared speech-to-text interface kept your application source code unchanged. 

Next, you'll compare performance between Parakeet and Moonshine.
