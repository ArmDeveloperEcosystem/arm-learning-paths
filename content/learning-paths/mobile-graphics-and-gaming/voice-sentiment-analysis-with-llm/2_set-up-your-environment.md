---
title: Set up your environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Before building the voice assistant, create a project workspace and set up an isolated `UV` environment. This keeps project dependencies separate from your system installation and makes it easier to reproduce the steps in the rest of the Learning Path.

These instructions support Ubuntu, macOS, and Windows, with Python 3.9 or later and a working microphone.

Install required system tools first. `ffmpeg` is required by Whisper for audio decoding.

{{< tabpane code=true >}}
  {{< tab header="Ubuntu/macOS" language="bash">}}
# Ubuntu
sudo apt update
sudo apt install -y ffmpeg git cmake

# macOS
brew install ffmpeg git cmake
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
# Install via WinGet
winget install -e --id Gyan.FFmpeg
winget install -e --id Git.Git
winget install -e --id Kitware.CMake
  {{< /tab >}}
{{< /tabpane >}}

Check your Python version before continuing:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu/macOS" language="bash">}}
python3 --version
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
py -3 --version
  {{< /tab >}}
{{< /tabpane >}}

## Set up the Python environment with UV

Install `UV` first so the `uv` command is available in your terminal. `UV` is a fast Python package and environment manager that you will use throughout this Learning Path to create the project environment and install dependencies.

{{< tabpane code=true >}}
  {{< tab header="Ubuntu/macOS" language="bash">}}
curl -LsSf https://astral.sh/uv/install.sh | sh
# Start a new shell, or source your shell rc file so `uv` is on PATH.
uv --version
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
# Open a new PowerShell window so `uv` is on PATH.
uv --version
  {{< /tab >}}
{{< /tabpane >}}

Create and activate the project virtual environment:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu/macOS" language="bash">}}
mkdir -p ~/voice-sentiment-assistant
cd ~/voice-sentiment-assistant
uv venv .venv
source .venv/bin/activate
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
mkdir $HOME\voice-sentiment-assistant -Force
cd $HOME\voice-sentiment-assistant
uv venv .venv
.\.venv\Scripts\Activate.ps1
  {{< /tab >}}
{{< /tabpane >}}

Keep this virtual environment activated while you complete the rest of the Learning Path.

Create a `requirements.txt` file for the packages used across the rest of the Learning Path:

```txt
gradio
openai-whisper
requests
torch
transformers
pandas
numpy
librosa
scikit-learn
onnx
onnxscript
onnxruntime
```

Install the dependencies into your active `UV` virtual environment:

```console
uv pip install -r requirements.txt
```

This installs the libraries needed for the Gradio interface, Whisper transcription, model training, and ONNX Runtime inference. Some packages in this list are used later in the Learning Path when you optimize and export the sentiment model.

## Download, build, and run llama.cpp

Next, clone the [llama.cpp GitHub repository](https://github.com/ggml-org/llama.cpp), build the local inference server, and start it. This server exposes an OpenAI-compatible API that the Python application will call later in the Learning Path.

{{< tabpane code=true >}}
  {{< tab header="Ubuntu/macOS" language="bash">}}
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build
cmake --build build --config Release
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
git clone https://github.com/ggml-org/llama.cpp
cd llama.cpp
cmake -B build
cmake --build build --config Release
  {{< /tab >}}
{{< /tabpane >}}

When the build completes, the `llama-server` executable should be available in the build output directory. 

```
ls ./build/bin/llama-server
```

{{% notice Note %}}
The file verification commands in this Learning Path uses syntax for Ubuntu and macOS. If you're on Windows, adjust the commands to use PowerShell equivalents like `Test-Path .\build\bin\llama-server.exe` or `dir .\build\bin\`. The file location remains the same across all platforms.
{{% /notice %}}

This Learning Path uses a quantized [Gemma 3 1B instruction-tuned model](https://huggingface.co/google/gemma-3-1b-it) served locally through `llama.cpp`.

The first time you run this command, `llama.cpp` will download the model from Hugging Face. This can take several minutes depending on your network connection.

Run the following command from the `llama.cpp` directory:

{{< tabpane code=true >}}
  {{< tab header="Ubuntu/macOS" language="bash">}}
./build/bin/llama-server -hf ggml-org/gemma-3-1b-it-GGUF
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell">}}
.\build\bin\Release\llama-server.exe -hf ggml-org/gemma-3-1b-it-GGUF
  {{< /tab >}}
{{< /tabpane >}}

Leave this terminal running while you test the application in later steps. The server listens on a local OpenAI-compatible endpoint that your app will call to generate responses.

At this point, your development environment is ready. You have installed the required audio and build tools, created a `UV` environment, installed the Python dependencies, and started a local `llama.cpp` server. In the next section, you will use this setup to build the baseline voice-to-LLM pipeline by creating a simple Gradio interface, transcribing microphone input with Whisper, and sending the transcript to the local LLM.
