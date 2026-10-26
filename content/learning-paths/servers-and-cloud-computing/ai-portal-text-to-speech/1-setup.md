---
title: Set up Qwen3-TTS on Arm Neoverse
description: Prepare an Arm Neoverse-based Linux machine and download the Qwen3-TTS ONNX package.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Arm AI Portal

The [Arm AI Portal](https://developer.arm.com/ai/models) is a catalog of AI models optimized for Arm-based targets across different runtimes, use cases, and profiles. The AI Portal provides benchmarking and compatibility data, code examples, and deployment methods.

You'll use [the Qwen3-TTS package](https://developer.arm.com/ai/models/hugging-face/Arm/qwen3-tts-0-6b-int8-onnx-graviton-g4/qwen3-tts-0.6b-int8--onnx-cascade-graviton-g4-onnx) from the Arm AI Portal to clone a voice on an Arm Neoverse-based machine.

## What you'll build

Qwen3-TTS voice cloning takes text and a reference recording, then synthesizes the text in the reference speaker's voice at 24 kHz.

The server workflow uses Python and ONNX Runtime to run a cascade of ONNX models. The provided application and runner are specific to this Qwen3-TTS package.

For the server workflow, you'll:

1. Connect to an Arm Neoverse-based Linux machine. The workflow was validated with an AWS Graviton4-based instance running Ubuntu.
2. Create a Python virtual environment for ONNX Runtime.
3. Download the supported ONNX model package from Hugging Face.
4. Start the web application and connect to it through an SSH tunnel.
5. Record or upload reference audio, generate speech, and play or download the result in your browser.
6. Optionally run the same model from the terminal with the supplied `onnx_tts_runner.py` script.

{{% notice Warning %}}
Clone a voice only when you have the speaker's permission. Don't use generated speech to impersonate or mislead others.
{{% /notice %}}

## Confirm the machine architecture

The server package contains a cascade of ONNX models optimized for AWS Graviton4-based instances. You can also use other Arm Neoverse-based Linux machines running locally or through a cloud provider.

The following cloud instance types provide a suitable starting configuration with four vCPUs and 32 GB of memory:

| Cloud provider | Suggested instance | Arm processor | vCPUs | Memory |
| --- | --- | --- | ---: | ---: |
| AWS | [`r8g.xlarge`](https://aws.amazon.com/ec2/instance-types/memory-optimized/) | AWS Graviton4 | 4 | 32 GiB |
| Google Cloud | [`c4a-highmem-4`](https://cloud.google.com/compute/docs/general-purpose-machines#c4a_machine_series) | Google Axion | 4 | 32 GB |
| Microsoft Azure | [`Standard_E4ps_v6`](https://learn.microsoft.com/azure/virtual-machines/sizes/memory-optimized/epsv6-series) | Azure Cobalt 100 | 4 | 32 GiB |

Instance availability varies by region. Select a larger memory configuration for larger models or longer context lengths.

Use an `arm64` image of Ubuntu 24.04 LTS for the recommended environment. Other Arm Neoverse Linux distributions can work, but their package installation commands might differ.

On your Neoverse-based machine, confirm that the operating system reports the `aarch64` architecture:

```bash
uname -m
```

The expected output is:

```output
aarch64
```

## Create the Python environment

Install the required system packages:

```bash
sudo apt update
sudo apt install -y \
  python3 \
  python3-venv \
  python3-pip \
  libsndfile1 \
  libgomp1 \
  ffmpeg \
  wget
```

Create the working directory and Python virtual environment:

```bash
mkdir -p ~/qwen3-tts
cd ~/qwen3-tts
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install the Qwen3-TTS server dependencies:

```bash
python -m pip install \
  "onnxruntime==1.26.0" \
  "transformers==4.57.3" \
  numpy \
  soundfile \
  librosa \
  torch \
  "huggingface_hub[cli]" \
  fastapi \
  uvicorn \
  python-multipart
```

<!-- ONNX Runtime executes the speech-synthesis models. Transformers and PyTorch support the text processor used by the example; the model cascade itself runs through ONNX Runtime. FastAPI and Uvicorn provide the browser application, and `python-multipart` supports reference-audio uploads. -->

## Download the web application and runner

Download the browser application and ONNX Runtime runner:

```bash
BASE_URL=https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/servers-and-cloud-computing/ai-portal-text-to-speech

for FILE in onnx_tts_runner.py tts_web.py; do
  if ! wget -nv "$BASE_URL/files/$FILE" -O "$FILE.tmp"; then
    rm -f "$FILE.tmp"
    echo "Failed to download $FILE" >&2
    break
  fi
  mv "$FILE.tmp" "$FILE"
done
```

Confirm that the files are present and have sizes greater than zero bytes:

```bash
for FILE in onnx_tts_runner.py tts_web.py; do
  if [ -s "$FILE" ]; then
    echo "Present: $FILE"
  else
    echo "Missing or zero size: $FILE"
  fi
done
```

## Download the server model

Open the [Qwen3-TTS ONNX package in the Arm AI Portal](https://developer.arm.com/ai/models/hugging-face/Arm/qwen3-tts-0-6b-int8-onnx-graviton-g4/qwen3-tts-0.6b-int8--onnx-cascade-graviton-g4-onnx) and inspect the model card. Select **Use this Model**, then **Open on Hugging Face** to reach the [`Arm/qwen3-tts-0-6b-int8-onnx-graviton-g4`](https://huggingface.co/Arm/qwen3-tts-0-6b-int8-onnx-graviton-g4) repository.

Set `QWEN_MODEL_ID` to the complete repository ID and download the model:

```bash
QWEN_MODEL_ID=Arm/qwen3-tts-0-6b-int8-onnx-graviton-g4
hf download "$QWEN_MODEL_ID" --local-dir .
```

Confirm that the ONNX models and text-path artifacts are present and have sizes greater than zero bytes:

```bash
for FILE in \
  onnx_cascade_driver.py \
  sample_input.wav \
  text_path_config.json \
  text_path_weights.npz; do
  if [ -s "$FILE" ]; then
    echo "Present: $FILE"
  else
    echo "Missing or zero size: $FILE"
  fi
done
find . -maxdepth 1 -type f -name "*.onnx" -size +0c | wc -l
```

You should expect 10 `*.onnx` files. 

The output is similar to:

```output
Present: onnx_cascade_driver.py
Present: sample_input.wav
Present: text_path_config.json
Present: text_path_weights.npz
10
```

## What you've accomplished and what's next

You've prepared an Arm Neoverse-based machine and downloaded the Qwen3-TTS ONNX package, browser application, and terminal runner. 

Next, you'll start the web application and generate speech without manually copying audio files between your computer and the cloud instance.
