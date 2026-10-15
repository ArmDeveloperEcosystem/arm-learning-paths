---
title: Understand on-device ASR and prepare your host
description: Understand the offline Conformer speech recognition workflow and prepare the development host for deployment on an Alif E8 board.
weight: 2

layout: "learningpathall"
---

## What you will run

You will capture a spoken phrase on an Alif Ensemble E8 board, run a Conformer model through ExecuTorch on its Ethos-U85 NPU, and read the transcription on the connected display. Speech processing runs locally on the board.

## What is automatic speech recognition?

Automatic speech recognition (ASR) converts speech audio into text. The application you will run reads fixed 16 kHz audio, converts the samples into Mel spectrogram features, runs a Conformer model, and decodes the output tokens into text.

[Conformer](https://github.com/sooftware/conformer/) is a transformer-based neural network architecture used for speech tasks. It combines attention layers, which help the model use context from different parts of an utterance, with convolution layers, which help capture local audio patterns.

The Conformer model in this flow does not take raw audio directly. The preprocessing code creates an 80-bin Mel spectrogram using a 512-sample window and 160-sample hop. The postprocessing code then removes repeated tokens and maps token IDs to text using the SentencePiece vocabulary.

The [SentencePiece vocabulary](https://github.com/google/sentencepiece/blob/master/README.md#what-is-sentencepiece) is the token list used by the decoder. The model outputs token IDs, not finished words, and the vocabulary maps each ID to a text piece such as a letter, word fragment, or word-start marker.

## The ML Evaluation Kit

The Machine Learning Evaluation Kit (MLEK) is a set of embedded machine learning examples, build scripts, model resources, and deployment flows for Arm-based microcontroller systems. You will use Alif's MLEK application, `alif_asr`, which adds the E8 microphone, display, and memory configuration to this deployment flow.

Ethos-U85 is an Arm NPU for accelerating neural networks in high-performance microcontroller designs, and is a primary target for the MLEK. Conformer is a good fit for this target because ASR depends on both local sound patterns and longer-range speech context. In this flow, the model is exported as an ExecuTorch `.pte` file using the Ethos-U ExecuTorch backend, so supported operations can run on the Ethos-U85 NPU instead of only on the Cortex-M CPU.

## Set expectations for recognition quality

The [Conformer model](https://huggingface.co/Arm/stt_en_conformer_executorch_small/blob/87d021a59a62a4c9640b5b568067ae8063550d26/README.md) has about 10 million parameters and was trained on English LibriSpeech audio. The deployment uses INT8 quantization and a lightweight decoder that selects the most likely tokens without an additional language model. These choices keep memory and computation manageable for embedded deployment.

Recognition also depends on the training data, speaker, and recording conditions. You might see substituted or missing words, or unusual word boundaries. Completed inference demonstrates that the deployment works; comparing the transcription with what you said is a separate accuracy check. You will check both when you test the board.

## Prepare your development host

{{% notice Important %}}
Use Linux on an x86_64 or aarch64 host, or use an **Apple Silicon Mac** running macOS 15 or later. 

The commands have not been validated on native Windows. WSL with USB passthrough can work with the E8 AppKit, but that configuration is outside the scope of this Learning Path.
{{% /notice %}}

Use Python 3.12 for the tested setup. Install the host packages for your operating system. The macOS commands assume you have already installed [Homebrew](https://brew.sh/).

{{< tabpane code=true >}}
  {{< tab header="Ubuntu Linux" language="bash">}}
sudo apt update
sudo apt install -y \
  build-essential \
  git \
  ninja-build \
  python3 \
  python3-dev \
  python3-pip \
  python3-venv \
  unzip \
  curl \
  libsndfile1
  {{< /tab >}}
  {{< tab header="macOS" language="bash">}}
xcode-select --install
brew install git python@3.12 libsndfile
alias python3=/opt/homebrew/bin/python3.12
  {{< /tab >}}
{{< /tabpane >}}

Install the `arm-none-eabi` distribution of the [Arm GNU Toolchain](/install-guides/gcc/arm-gnu/). The board build was verified with Arm GNU Toolchain 15.3.Rel1 (GCC 15.3.1). Ensure `arm-none-eabi-gcc` is on your `PATH`.

Verify the host and toolchain:

```bash
python3 --version
make --version
arm-none-eabi-gcc --version
```


{{% notice Note %}}
A Corstone-320 Fixed Virtual Platform (FVP) provides a virtual-hardware alternative for model development. For a related audio workflow using ExecuTorch and Ethos-U85, see [Deploy Silero VAD on Arm Ethos-U with ExecuTorch](/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/), which detects speech activity. For Conformer transcription on the FVP, see [Arm's Conformer FVP example](https://developer.arm.com/community/arm-community-blogs/b/internet-of-things-blog/posts/end-to-end-int8-conformer-on-arm-training-quantization-and-deployment-on-ethos-u85). Follow those resources' host and simulator requirements if you choose that route.
{{% /notice %}}

## What you've learned and what's next

You know how the board converts speech into text, what affects recognition quality, and which host tools the deployment needs.

Next, you will connect the E8, install its programming tools, and prepare the Alif MLEK model resources.
