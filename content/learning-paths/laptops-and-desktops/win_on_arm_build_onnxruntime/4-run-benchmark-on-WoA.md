---
title: Run Phi3 model on a Windows on Arm machine
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run the Phi-3 model on your Windows on Arm machine

In this section, you'll download the Phi-3 Mini model and run it on your Windows on Arm machine, which can be a physical or virtual machine. You'll be use a simple model runner program which provides performance metrics

The Phi-3 Mini (3.3B) model has a short (4k) context version and a long (128k) context version. The long context version can accept much longer prompts and produces longer output text, but it consumes more memory.

In this learning path, you'll use the short context version, which is quantized to 4-bits.

The Phi-3 Mini model used here is in ONNX format.

### Setup

[Phi-3 ONNX models](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx) are hosted on HuggingFace.
Hugging Face uses Git for both version control and to download the ONNX model files, which can be quite large.

You'll first need to install the Git Large File Storage (LFS) extension:

``` bash
winget install -e --id GitHub.GitLFS
git lfs install
```
If you don’t have winget, download and run the exe from the [official source](https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage?platform=windows).

If the extension is already installed for you when you run the above ``git`` command it will say ``Git LFS initialized``.

You then need to install the ``HuggingFace CLI``.

``` bash
pip install huggingface-hub[cli]
```

### Download the Phi-3-Mini-4K model

``` bash
cd C:\Users\%USERNAME%
cd repos\lp
huggingface-cli download microsoft/Phi-3-mini-4k-instruct-onnx --include cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4/* --local-dir .
```
This command downloads the model into a folder called `cpu_and_mobile`.

### Build model runner (ONNX Runtime GenAI C Example)

In the previous section you built ONNX Runtime Generate() API from source. The headers and dynamic linked libraries that are built need to be copied over to appropriate folders (``lib`` and ``inclue``).

Building from source is a better practice because the examples usually are updated to run with the latest changes.

``` bash
copy onnxruntime\build\Windows\Release\Release\onnxruntime.* onnxruntime-genai\examples\c\lib
cd onnxruntime-genai
copy build\Windows\Release\Release\onnxruntime-genai.* examples\c\lib
copy src\ort_genai.h examples\c\include\
copy src\ort_genai_c.h examples\c\include\
```

You can now build the model runner executable in the ''onnxruntime-genai'' folder using the commands below:

``` bash
cd examples/c
cmake -A arm64 -S . -B build -DPHI3=ON
cd build
cmake --build . --config Release
```

After a successful build, a binary program called `phi3` will be created in the ''onnxruntime-genai'' folder:

```output
dir Release\phi3.exe
```

#### Run the model

Use the runner you just built to execute the model with the following commands:

``` bash
cd C:\Users\%USERNAME%
cd repos\lp
.\onnxruntime-genai\examples\c\build\Release\phi3.exe .\cpu_and_mobile\cpu-int4-rtn-block-32-acc-level-4\ cpu
```

This will allow the runner program to load the model. It will then prompt you to input the text prompt to the model as shown:

```output
-------------
Hello, Phi-3!
-------------
C++ API
Creating config...
Creating model...
Creating tokenizer...
Prompt: (Use quit() to exit) Or (To terminate current output generation, press Ctrl+C)
``` 

After you enter your input prompt, the text output by the model will be displayed. On completion, performance metrics similar to those shown below should be displayed:

```
Prompt length: 64, New tokens: 931, Time to first: 1.79s, Prompt tokens per second: 35.74 tps, New tokens per second: 6.34 tps
```
You have successfully run the Phi-3 model on your Windows device powered by Arm.
