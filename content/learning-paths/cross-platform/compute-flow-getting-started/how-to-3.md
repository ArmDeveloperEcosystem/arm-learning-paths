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


## What you've accomplished

You've learned how brick types, implementations, model packages, and manifests fit together. You used Brick Manager to install models and build Compute Flow on your Apple silicon Mac, then connected speech recognition, translation, and speech synthesis in Python to turn an English recording into a French WAV file locally.

Finally, you replaced Parakeet with Moonshine by installing its brick and model package, rebuilding, and selecting a different manifest. The shared speech-to-text interface kept your Python script unchanged. You can use this approach to combine other bricks and select compatible models for your own applications.
