---
title: Serve Muse Glimmer locally on the GPU
description: Connect over SSH, build the ExecuTorch CUDA worker, and start a localhost model endpoint.
weight: 2
layout: learningpathall
---

## Build a local agent on DGX Spark

In this Learning Path, you'll use the Hermes Agent framework and the Muse Glimmer 30B model to create a local agent, running on DGX Spark, capable of a variety of tasks, such as debugging and coding. You will test this agent by tasking it to repair a broken Python release checker, verifying through tests that the Python code is corrected.

[Hermes Agent](https://hermes-agent.nousresearch.com/docs) is an open-source agent framework from Nous Research, [first released on 25 February 2026](https://nousresearch.com/releases). It sends the model's requests to tools and returns their results. Hermes runs on the DGX Spark's Arm CPU and executes shell commands in a restricted Docker container.

[Muse Glimmer](https://huggingface.co/meta-models/Muse-Glimmer-30B) is Meta's open-weight, approximately 30-billion-parameter model designed for local agent tasks, including multi-step reasoning, tool use, and code repair. Meta [released it on 10 August 2026](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model). It supports text and image inputs, though this Learning Path uses text only. Muse Glimmer chooses the commands and code changes, while Hermes executes the requested tools and returns their output.

[ExecuTorch](https://pytorch.org/projects/executorch/) is PyTorch’s framework for running AI models locally on devices, including laptops, mobile phones, and embedded systems. It was [first introduced on 17 October 2023](https://pytorch.org/blog/pytorch-edge-enabling-on-device-inference-across-mobile-and-edge-devices-with-executorch/). ExecuTorch loads and runs the exported Muse Glimmer model. ExecuTorch's CUDA backend runs Muse Glimmer on the DGX Spark's NVIDIA Blackwell GPU, and its server exposes a local endpoint for Hermes.

[CUDA](https://developer.nvidia.com/cuda-toolkit) is NVIDIA's platform for GPU computing. The CUDA toolkit provides compilers and libraries for building GPU code, while the NVIDIA driver lets applications run that code on the GPU. Here, CUDA accelerates the tensor operations used for Muse Glimmer inference.

```text
Laptop --SSH--> DGX Spark
                 Hermes on Arm-based CPU
                   |-- localhost HTTP --> ExecuTorch --> NVIDIA GPU
                   `-- terminal tools --> Docker sandbox (no network)
```

## Connect and check the system

From your laptop, replace `spark-user` and `spark-host` with your SSH account and IP address:

```bash
ssh spark-user@spark-host
```

Run all remaining commands on the Spark.

You need Ubuntu 24.04-based DGX OS, Python 3.12, CUDA **13.0**, and NVIDIA driver **580 or newer**. The [NVIDIA CUDA compatibility table](https://docs.nvidia.com/deploy/cuda-compatibility/minor-version-compatibility.html) gives the driver requirement.

If the standard Linux tools are missing, install them before proceeding:

```bash
sudo apt update
sudo apt install build-essential cmake git curl python3.12-venv
```

Docker Engine must already be running and accessible to your SSH account. Follow the [Docker Engine install guide](/install-guides/docker/docker-engine/) if needed, and reconnect after changing group membership.

Download the five Learning Path files from the Arm Learning Paths GitHub repository once into `~/muse-agent`: the prerequisite checker, dependency constraints, Hermes setup helper, broken release checker, and acceptance tests. Download these files before downloading source or model weights:

```bash
mkdir -p ~/muse-agent
cd ~/muse-agent
LP_FILES=https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/laptops-and-desktops/dgx_spark_muse_glimmer_executorch_hermes/files
(
  set -e
  for file in check-prereqs.sh executorch-constraints.txt setup-hermes-cli.sh release_tool.py test_release_tool.py; do
    curl --fail --location --remove-on-error "$LP_FILES/$file" -o "$file"
    test -s "$file"
  done
)
```

The parenthesized block stops at the first failed download or empty file without closing your SSH session. All five downloads must finish successfully. If a download fails, resolve the error and retry this download step before continuing.

Run the prerequisite checker:

```bash
cd ~/muse-agent
bash check-prereqs.sh "$HOME/muse-agent"
```

Expect `PASS`. Resolve any reported failure before continuing. Reserve 100 GiB of free disk and 80 GiB of available memory for the build and export; other model services can consume most of the Spark's unified memory.

## Download the ExecuTorch source and create the environment

Download the pinned ExecuTorch source and its submodules, then create a Python environment:

```bash
cd ~/muse-agent
git clone https://github.com/pytorch/executorch.git
cd executorch
git checkout 0a4a05e84d9642460d87ec2bbbd0e397667ec9c8
git submodule update --init --recursive
git rev-parse HEAD > ../executorch-revision.txt
python3 -m venv ../executorch-venv
cat ../executorch-revision.txt
```

The revision must be `0a4a05e84d9642460d87ec2bbbd0e397667ec9c8`. The environment is in `~/muse-agent/executorch-venv`.

If the clone succeeded but a later command failed, resume from that command inside `~/muse-agent/executorch`. Do not clone again into the existing directory. You can rerun `git submodule update --init --recursive` after an interrupted submodule download.

## Install dependencies and verify CUDA

Activate the environment and use the dependency constraints downloaded earlier:

```bash
export PATH=/usr/local/cuda/bin:$PATH
source ../executorch-venv/bin/activate
export PIP_CONSTRAINT="$HOME/muse-agent/executorch-constraints.txt"
CMAKE_BUILD_PARALLEL_LEVEL=4 ./install_executorch.sh --use-pt-pinned-commit
python -m pip install huggingface_hub
python -m pip install -r examples/llm_server/python/requirements.txt
```

The installation builds the ExecuTorch Python package with four parallel jobs. It may take a few minutes. Wait for it to finish without errors, then check PyTorch:

```bash
python -c 'import torch; print(torch.__version__); print(torch.cuda.is_available()); print(torch.cuda.get_device_name(0))'
```

Expect `2.15.0+cu130`, `True`, and the GB10 GPU name. Stop if any value differs.

If installation fails, resolve the reported error and rerun the failed installation command with the same environment and constraints. Keep the source and environment directories. Use the [ExecuTorch source-build instructions](https://github.com/pytorch/executorch/blob/main/docs/source/using-executorch-building-from-source.md) for build troubleshooting.

## Build the CUDA worker

Build the executable that runs Muse Glimmer on the GPU:

```bash
CMAKE_BUILD_PARALLEL_LEVEL=4 make muse-glimmer-cuda
test -x cmake-out/examples/models/muse-glimmer/muse_glimmer_worker
```

The build must finish without errors, and the executable check must return exit code 0. If compilation fails, fix the reported error and rerun the same `make` command. It reuses completed build work.

## Export the model to ExecuTorch

You will start from a `GGUF` format quantized model checkpoint, and export and lower to ExecuTorch on the DGX Spark.

{{% notice Note %}}
Optionally, sign in to Hugging Face with `hf auth login` before downloading. Authentication provides higher [Hugging Face request limits](https://huggingface.co/docs/hub/main/en/rate-limits) and can help avoid rate-limit interruptions, especially on shared networks.
{{% /notice %}}

Download the quantized checkpoint (approximately **17 GB**):

```bash
hf download meta-models/Muse-Glimmer-30B-GGUF \
  --revision 70bf1b61ac09f91b24d39038091b41c582bc5d7a \
  --include Muse-Glimmer-30B-KQuant-17GB-Q4_K_M.gguf \
  --local-dir assets/quant
```

Wait for the download to complete. If it is interrupted, rerun the same `hf download` command.

Export, partition, and compile the model for CUDA:

```bash
MAX_JOBS=4 TORCHINDUCTOR_COMPILE_THREADS=4 \
python -m executorch.examples.models.muse_glimmer.export.export_solo \
  --gguf assets/quant/Muse-Glimmer-30B-KQuant-17GB-Q4_K_M.gguf \
  --backend cuda --max-seq-len 65536 --output-dir exports/spark-native-64k
```

The [export script](https://github.com/pytorch/executorch/blob/0a4a05e84d9642460d87ec2bbbd0e397667ec9c8/examples/models/muse-glimmer/export/export_solo.py), used by the command above, performs three steps:

1. Loads the GGUF weights and captures the model's inference methods as graphs with `torch.export.export()`.
2. Calls `executorch.exir.to_edge_transform_and_lower()` with `CudaPartitioner` to select and delegate supported graph regions to `CudaBackend`. That backend uses [AOTInductor](https://docs.pytorch.org/docs/stable/torch.compiler_aot_inductor.html), PyTorch's ahead-of-time compiler, to turn the exported computation into compiled CUDA code during setup. ExecuTorch loads that code for inference.
3. Calls `.to_executorch()` to prepare the runtime program and memory plan, then saves `model.pte` and its external delegate data in `aoti_cuda_blob.ptd`.

`--max-seq-len 65536` sets the exported context limit. `MAX_JOBS` and `TORCHINDUCTOR_COMPILE_THREADS` limit build parallelism.

Wait for the export to print `Done.` and return to the shell without an error. If export fails, resolve the reported error and rerun only the export command. The checkpoint and worker do not need to be downloaded or built again.

The server uses `tokenizer.json` to convert text into token IDs and generated tokens back into text. `tokenizer_config.json` and `chat_template.jinja` define tokenizer settings and how conversations and tool calls are formatted for Muse Glimmer.

Download the tokenizer files:

```bash
hf download meta-models/Muse-Glimmer-30B-ExecuTorch-PTE \
  --revision fc6fa93cdefeddc93abd7abf883e99279af7ea51 \
  --include tokenizer.json --include tokenizer_config.json \
  --include chat_template.jinja --local-dir exports
```

Wait for the tokenizer download to finish without an error. If it fails, rerun that download without repeating the export.

## Start the local server

This command starts an OpenAI-compatible HTTP server and launches the CUDA worker for inference. It uses the exported model, external data, and tokenizer files, and exposes the model as `muse-glimmer-30B` with a 65,536-token context at `http://127.0.0.1:8000` on the DGX Spark:

```bash
python -m executorch.examples.models.muse_glimmer.serving.serve \
  --model-path exports/spark-native-64k/model.pte \
  --data-path exports/spark-native-64k/aoti_cuda_blob.ptd \
  --tokenizer-path exports/tokenizer.json \
  --hf-tokenizer exports \
  --worker-bin cmake-out/examples/models/muse-glimmer/muse_glimmer_worker \
  --model-id muse-glimmer-30B \
  --tool-parser atem \
  --max-context 65536 --host 127.0.0.1 --port 8000
```

Under the hood, the Python server formats chat requests and passes them to the C++ worker. Its [inference engine](https://github.com/pytorch/executorch/blob/0a4a05e84d9642460d87ec2bbbd0e397667ec9c8/examples/models/muse-glimmer/runtime/engine/muse_glimmer_engine.cpp) uses ExecuTorch's `executorch::extension::Module` API and `load_method()` to load the exported inference methods. During generation, the ExecuTorch runtime executes those methods through the compiled CUDA delegate; the server returns the generated text and tool calls over HTTP.

`--tool-parser atem` converts native model tool calls into the OpenAI-compatible format Hermes expects.

Keep the server running in this SSH session. Open a second terminal on your laptop and connect to the DGX Spark. Replace `spark-user` and `spark-host` with your SSH account and IP address:

```bash
ssh spark-user@spark-host
```

Run the endpoint checks in this second SSH session:

```bash
curl --fail http://127.0.0.1:8000/health
curl --fail http://127.0.0.1:8000/v1/models
curl --fail http://127.0.0.1:8000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"muse-glimmer-30B","messages":[{"role":"user","content":"What is 17 times 23?"}],"max_tokens":2048}'
```

Expect the model ID in `/v1/models` and an answer of `391` in the chat response. Reasoning may appear separately from the answer.

If an endpoint check fails, inspect the server's terminal for the error. Correct missing paths or a port conflict, then rerun the server command.

## What you've accomplished

You've built the CUDA worker, exported Muse Glimmer 30B to ExecuTorch with the CUDA backend, and started a local model endpoint. Next, you will set up Hermes Agent on the Arm CPU.
