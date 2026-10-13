---
title: Set up the voice translation project
description: Set up Python and download Sherpa-ONNX, Gemma 4 E2B, and Supertonic 3 models for an on-device English-to-Spanish voice translator on an Apple Silicon Mac.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare an Apple Silicon Mac

You will build a Python app that records an English text input, translates it into Spanish, and plays the Spanish speech. A local Gradio page provides the recording and playback controls. Three seperate models handle inference:

| Stage | Model and runtime | Processor | Input and output |
| --- | --- | --- | --- |
| Transcription | English Zipformer with Sherpa-ONNX | CPU | Recorded audio to English text |
| Translation | Gemma 4 E2B with LiteRT-LM | Apple GPU | English text to Spanish text |
| Speech synthesis | Supertonic 3 with Sherpa-ONNX | CPU | Spanish text to Spanish audio |

The Gemma model receives the transcript, rather than the recording itself. Translation text will appear as Gemma generates it, followed by speech synthesis starting after the translation finishes. All three models run locally after you download them, so this pipeline will work fully offline once built.

Before starting, quickly check that macOS reports the Apple Silicon architecture and that a version of Python 3.10 through 3.13 is available:

```bash
uname -m
python3 --version
```

The expected output from `uname -m` is:

```output
arm64
```

macOS uses the name `arm64` for the 64-bit Arm architecture. If `uname -m` reports `x86_64`, you are either using an Intel-based Mac or running the terminal through Rosetta.

Use Python 3.10 through 3.13 for the pinned packages in this Learning Path. If `python3` reports another version, install and select a supported version before you create the virtual environment.

Note that packages used in this Learning Path may not support versions of Python later than 3.14.
## Create the Python environment

Create a project directory and a virtual environment:

```bash
mkdir -p ~/voice-translator/models
cd ~/voice-translator
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Keep this environment active while you complete the Learning Path. Make sure to run the scripts from `~/voice-translator` since their model paths are relative to that directory.

Create a `requirements.txt` file in `~/voice-translator` with the following contents:

```text
gradio==6.22.0
litert-lm-api==0.17.1
numpy==2.2.6
sherpa-onnx==1.13.3
sherpa-onnx-bin==1.13.3
sounddevice==0.5.6
```

Install all the packages:

```bash
python -m pip install -r requirements.txt
```

Verify that the native packages load and that Python is running as `arm64`:

```bash
python -c "import platform, litert_lm, sherpa_onnx, sounddevice; print(platform.machine())"
```

The expected output is:

```output
arm64
```

The prebuilt LiteRT-LM and Sherpa-ONNX packages mean that you don't need to compile either runtime from source.

## Download the speech recognition model

Download and extract the quantised English streaming Zipformer model:

```bash
cd ~/voice-translator
curl -L -o models/sherpa-asr.tar.bz2 https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-streaming-zipformer-en-2023-06-26.tar.bz2
tar -xjf models/sherpa-asr.tar.bz2 -C models
rm models/sherpa-asr.tar.bz2
```



## Download Gemma 4 E2B

Download the instruction-tuned Gemma 4 E2B model packaged for LiteRT-LM. The file is about 2.6 GB, so the download can take several minutes.

```bash
curl -L -o models/gemma-4-E2B-it.litertlm https://huggingface.co/litert-community/gemma-4-E2B-it-litert-lm/resolve/main/gemma-4-E2B-it.litertlm
```

Keep the filename `gemma-4-E2B-it.litertlm`: the translation script uses this path when it opens the model.

## Download the speech synthesis model

Download and extract the quantised Supertonic 3 model:

```bash
curl -L -o models/supertonic.tar.bz2 https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/sherpa-onnx-supertonic-3-tts-int8-2026-05-11.tar.bz2
tar -xjf models/supertonic.tar.bz2 -C models
rm models/supertonic.tar.bz2
```

You will use Supertonic 3 to turn the Spanish translation into speech. The model also supports other languages.[^supertonic-languages]

## Verify the model files

Check that one required file from each model is present:

```bash
ls models/gemma-4-E2B-it.litertlm \
   models/sherpa-onnx-streaming-zipformer-en-2023-06-26/encoder-epoch-99-avg-1-chunk-16-left-128.int8.onnx \
   models/sherpa-onnx-supertonic-3-tts-int8-2026-05-11/duration_predictor.int8.onnx
```

Confirm that all three filenames are listed. If `ls` reports a missing file, check that model's download and extraction before continuing.

## What you've accomplished and what's next

The Python imports and file checks confirm that the dependencies load and the expected model paths exist.

Start with the microphone and speech recogniser in the next step.

[^supertonic-languages]: Supertonic 3 supports speech synthesis in 31 languages: Arabic, Bulgarian, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, German, Greek, Hindi, Hungarian, Indonesian, Italian, Japanese, Korean, Latvian, Lithuanian, Polish, Portuguese, Romanian, Russian, Slovak, Slovenian, Spanish, Swedish, Turkish, Ukrainian, and Vietnamese. See the [Supertonic 3 language documentation](https://k2-fsa.github.io/sherpa/onnx/tts/supertonic.html).
