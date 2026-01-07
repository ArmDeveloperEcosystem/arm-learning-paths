---
title: Build and run on macOS
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you will build and run the audio generation application on macOS. The application uses ExecuTorch with XNNPack and Arm KleidiAI for optimized inference on Arm CPUs.

## Set up the environment

Start a fresh virtual environment:

```bash
cd $WORKSPACE/ML-examples/kleidiai-examples/audiogen-et/
python3.10 -m venv new-venv
source new-venv/bin/activate
```

If you haven't already installed ExecuTorch, install it now:

```bash
pip install executorch==1.0.0
```

## Set model path

Set the `EXECUTORCH_MODELS_PATH` environment variable to the directory containing your exported ExecuTorch models:

```bash
export EXECUTORCH_MODELS_PATH=$WORKSPACE/ML-examples/kleidiai-examples/audiogen-et
```

This should be the directory where the `.pte` model files were created during the conversion step.

## Build the application

Navigate to the `app` directory and create a build directory:

```bash
cd app
mkdir build && cd build
```

Run CMake to configure the build:

```bash
cmake ..
```

Build the application:

```bash
make -j8
```

The build process creates an `audiogen` executable in the `build` directory.

## Download the tokenizer model

The audio generation application uses a SentencePiece-based tokenizer. Download the `spiece.model` file from HuggingFace:

```bash
curl -L https://huggingface.co/google-t5/t5-base/resolve/main/spiece.model -o $EXECUTORCH_MODELS_PATH/spiece.model
```

Verify the file was downloaded:

```bash
ls -lh $EXECUTORCH_MODELS_PATH/spiece.model
```

## Run the application

Run the `audiogen` application with three required arguments:

- Model Path (`-m`): Directory containing your ExecuTorch models and `spiece.model` files
- Prompt (`-p`): Text description of the desired audio
- CPU Threads (`-t`): Number of CPU threads to use

Run the application with an example prompt:

```bash
./audiogen -m $EXECUTORCH_MODELS_PATH -p "warm arpeggios on house beats 120BPM with drums effect" -t 4
```

The application processes the prompt through the three model submodules and generates audio.

The output should look like:

```output
I 00:00:00.002858 executorch:main.cpp:280] Resetting threadpool with num threads = 4
I 00:00:00.003228 executorch:threadpool.cpp:48] Resetting threadpool to 4 threads.
I 00:00:00.003543 executorch:main.cpp:288] Using 4 threads
I 00:00:00.003620 executorch:main.cpp:294] Model (/Users/parver01/my-workspace/ML-examples/kleidiai-examples/audiogen-et/conditioners_model.pte) loaded
I 00:00:00.003627 executorch:main.cpp:298] Model (/Users/parver01/my-workspace/ML-examples/kleidiai-examples/audiogen-et/dit_model.pte) loaded
I 00:00:00.003629 executorch:main.cpp:302] Model (/Users/parver01/my-workspace/ML-examples/kleidiai-examples/audiogen-et/autoencoder_model.pte) loaded
I 00:00:04.723761 executorch:main.cpp:478] Output saved to warm_arpeggios_on_house_beats_120bpm_with_drums_effect_99.wav
I 00:00:04.723770 executorch:main.cpp:487] T5: 72 ms
I 00:00:04.723771 executorch:main.cpp:488] DiT: 1474 ms
I 00:00:04.723772 executorch:main.cpp:489] DiT Avg per step: 184.250000 ms
I 00:00:04.723784 executorch:main.cpp:490] AutoEncoder: 3127 ms
I 00:00:04.723785 executorch:main.cpp:491] Total execution time: 4673 ms
```
## Verify the output

If successful, the generated audio is saved as a `.wav` file in the current directory. The filename is based on the prompt text:

```bash
ls -lh warm_arpeggios_on_house_beats_120bpm_with_drums_effect_99.wav
```

You can play the audio file using any audio player on your macOS system:

```bash
open warm_arpeggios_on_house_beats_120bpm_with_drums_effect_99.wav
```

In this section:
- You built the audio generation application for macOS
- You downloaded the required tokenizer model
- You generated audio from a text prompt using ExecuTorch
- You verified the generated audio output

You can now experiment with different prompts to generate various audio samples. The application uses Arm KleidiAI optimizations to accelerate inference on Arm CPUs.

If you want to deploy to Android instead, proceed to the next section.
