---
title: Serve Muse Glimmer locally on the GPU
description: Connect over SSH, build the ExecuTorch CUDA worker, and start a localhost model endpoint.
weight: 2
layout: learningpathall
---

## Build a local agent on DGX Spark

[Hermes Agent](https://hermes-agent.nousresearch.com/docs) is an open-source agent framework from Nous Research, [first released on February 25, 2026](https://nousresearch.com/releases). It sends model requests to tools and returns their results. Hermes runs on the Arm CPU of the DGX Spark and executes shell commands in a restricted Docker container.

[Muse Glimmer](https://huggingface.co/meta-models/Muse-Glimmer-30B) is an open-weight, approximately 30-billion-parameter model designed by Meta for local agent tasks. These tasks include multi-step reasoning, tool use, and code repair. Meta [released Muse Glimmer on August 10, 2026](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model). The model supports text and image inputs. Muse Glimmer chooses the commands and code changes, while Hermes executes the requested tools and returns their output.

[ExecuTorch](https://pytorch.org/projects/executorch/) is the PyTorch framework for running AI models locally on devices, including laptops, mobile phones, and embedded systems. It was [first introduced on October 17, 2023](https://pytorch.org/blog/pytorch-edge-enabling-on-device-inference-across-mobile-and-edge-devices-with-executorch/). ExecuTorch loads and runs the exported Muse Glimmer model. The ExecuTorch CUDA backend runs Muse Glimmer on the NVIDIA Blackwell GPU of the DGX Spark. Its server exposes a local endpoint for Hermes.

[CUDA](https://developer.nvidia.com/cuda-toolkit) is the NVIDIA platform for GPU computing. The CUDA toolkit provides compilers and libraries for building GPU code. The NVIDIA driver lets applications run that code on the GPU. Here, CUDA accelerates the tensor operations used for Muse Glimmer inference.

You'll use the Hermes Agent framework and the Muse Glimmer 30B model to create a local agent running on DGX Spark. The agent will be capable of a variety of tasks, such as debugging and coding. You'll test this agent by tasking it to repair a broken Python release checker, verifying through tests that the Python code is corrected.

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

Run all remaining commands on the DGX Spark.

You'll need Ubuntu 24.04-based DGX OS, Python 3.12, CUDA 13.0, and NVIDIA driver 580 or later. The [NVIDIA CUDA compatibility table](https://docs.nvidia.com/deploy/cuda-compatibility/minor-version-compatibility.html) lists the driver requirement.

If the standard Linux tools are missing, install them before proceeding:

```bash
sudo apt update
sudo apt install build-essential cmake git curl python3.12-venv
```

Ensure that Docker Engine is running and accessible to your SSH account. For install instructions, see the [Docker Engine install guide](/install-guides/docker/docker-engine/). Reconnect after changing group membership.

Download the following files into `~/muse-agent`:

- The code archive from the Arm Learning Code Examples GitLab repository
- The release-summary image from the Learning Path repository

The archive contains the following files: 

- Prerequisite checker
- Dependency constraints
- Hermes setup helper
- Broken release checker
- Acceptance tests
- README
- A licence


Download these files before downloading source or model weights:

```bash
mkdir -p ~/muse-agent
cd ~/muse-agent
(
  set -e
  EXAMPLES_REV=d0905fd84ac1e23c8c0ecb5c8052bc6ac06523ce
  EXAMPLES_PATH=learning-paths/laptops-and-desktops/dgx_spark_muse_glimmer_executorch_hermes
  EXAMPLES_URL="https://gitlab.arm.com/learning-code-examples/code-examples/-/archive/$EXAMPLES_REV/code-examples-$EXAMPLES_REV.tar.gz?path=$EXAMPLES_PATH"
  LP_FILES=https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/laptops-and-desktops/dgx_spark_muse_glimmer_executorch_hermes/files
  download_dir=$(mktemp -d)
  trap 'rm -rf "$download_dir"' EXIT
  curl --fail --location --remove-on-error "$EXAMPLES_URL" -o "$download_dir/examples.tar.gz"
  tar -xzf "$download_dir/examples.tar.gz" -C "$download_dir"
  checker=$(find "$download_dir" -type f -name check-prereqs.sh -print -quit)
  test -n "$checker"
  cp "$(dirname "$checker")"/* .
  curl --fail --location --remove-on-error "$LP_FILES/release-summary.png" -o release-summary.png
  for file in check-prereqs.sh executorch-constraints.txt setup-hermes-cli.sh release_tool.py test_release_tool.py release-summary.png; do
    test -s "$file"
  done
)
```

The parenthesized block stops at the first failed download or extraction without closing your SSH session. The archive is pinned to a tested commit. 

Ensure that all files download successfully. Resolve any error and retry the download before continuing.

Run the prerequisite checker:

```bash
cd ~/muse-agent
bash check-prereqs.sh "$HOME/muse-agent"
```

Expect `PASS`. Resolve any reported failure before continuing. Reserve 100 GiB of free disk and 80 GiB of available memory for the build and export. Other model services can consume most of the unified memor of the Spark.

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

Ensure that the revision is `0a4a05e84d9642460d87ec2bbbd0e397667ec9c8`. The environment is in `~/muse-agent/executorch-venv`.

If the clone succeeded but a later command failed, resume from that command inside `~/muse-agent/executorch`. Don't clone again into the existing directory. You can rerun `git submodule update --init --recursive` after an interrupted submodule download.

## Install dependencies and verify CUDA

Activate the environment and use the dependency constraints that you downloaded earlier:

```bash
export PATH=/usr/local/cuda/bin:$PATH
source ../executorch-venv/bin/activate
export PIP_CONSTRAINT="$HOME/muse-agent/executorch-constraints.txt"
CMAKE_BUILD_PARALLEL_LEVEL=4 ./install_executorch.sh --use-pt-pinned-commit
python -m pip install huggingface_hub
python -m pip install -r examples/llm_server/python/requirements.txt
```

The installation builds the ExecuTorch Python package with four parallel jobs. The build might take a few minutes. 

Wait for the build to finish without errors, then check PyTorch:

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

Ensure that the build finishes without errors, and the executable check returns exit code `0`. If compilation fails, fix the reported error and rerun the same `make` command. The command reuses completed build work.

## Export the model to ExecuTorch

Download the quantized language model and vision checkpoint in `GGUF` format, then export and lower both to ExecuTorch on DGX Spark. The vision checkpoint adds an image encoder and projector. These are used to turn image patches into embeddings that the language model can use.

{{% notice Note %}}
Optionally, sign in to Hugging Face with `hf auth login` before downloading. Authentication provides higher [Hugging Face request limits](https://huggingface.co/docs/hub/main/en/rate-limits). Higher limits can help avoid rate-limit interruptions, especially on shared networks.
{{% /notice %}}

Download the language-model checkpoint (approximately 17 GB) and vision checkpoint (approximately 1.4 GB):

```bash
hf download meta-models/Muse-Glimmer-30B-GGUF \
  --revision 70bf1b61ac09f91b24d39038091b41c582bc5d7a \
  --include Muse-Glimmer-30B-KQuant-17GB-Q4_K_M.gguf \
  --include mmproj-Muse-Glimmer-30B-Q4_K_M.gguf \
  --local-dir assets/quant
```

Wait for the download to complete. If the download is interrupted, rerun the same `hf download` command.

Export, partition, and compile the model for CUDA:

```bash
MAX_JOBS=4 TORCHINDUCTOR_COMPILE_THREADS=4 \
python -m executorch.examples.models.muse_glimmer.export.export_solo \
  --gguf assets/quant/Muse-Glimmer-30B-KQuant-17GB-Q4_K_M.gguf \
  --mmproj assets/quant/mmproj-Muse-Glimmer-30B-Q4_K_M.gguf \
  --backend cuda --max-seq-len 65536 --output-dir exports/spark-native-vision-64k
```

The [export script](https://github.com/pytorch/executorch/blob/0a4a05e84d9642460d87ec2bbbd0e397667ec9c8/examples/models/muse-glimmer/export/export_solo.py) performs three steps:

1. Loads the GGUF weights and captures the inference methods of the model as graphs with `torch.export.export()`.
2. Calls `executorch.exir.to_edge_transform_and_lower()` with `CudaPartitioner` to select and delegate supported graph regions to `CudaBackend`. That backend uses [AOTInductor](https://docs.pytorch.org/docs/stable/torch.compiler_aot_inductor.html), the PyTorch ahead-of-time compiler, to turn the exported computation into compiled CUDA code during setup. ExecuTorch loads that code for inference.
3. Calls `.to_executorch()` to prepare the runtime program and memory plan. It then saves `model.pte`, its external delegate data in `aoti_cuda_blob.ptd`, and the vision position-embedding table in `pos_embed.bin`.

`--mmproj` adds the exported `vision_encoder` method. `--max-seq-len 65536` sets the exported context limit. `MAX_JOBS` and `TORCHINDUCTOR_COMPILE_THREADS` limit build parallelism.

Wait for the export to print `Done.` and return to the shell without an error. If export fails, resolve the reported error and rerun only the export command. The checkpoint and worker don't need to be downloaded or built again.

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

Start an OpenAI-compatible HTTP server and launch the CUDA worker for inference:

```bash
python -m executorch.examples.models.muse_glimmer.serving.serve \
  --model-path exports/spark-native-vision-64k/model.pte \
  --data-path exports/spark-native-vision-64k/aoti_cuda_blob.ptd \
  --pos-embed-path exports/spark-native-vision-64k/pos_embed.bin \
  --tokenizer-path exports/tokenizer.json \
  --hf-tokenizer exports \
  --worker-bin cmake-out/examples/models/muse-glimmer/muse_glimmer_worker \
  --model-id muse-glimmer-30B \
  --tool-parser atem \
  --max-context 65536 --host 127.0.0.1 --port 8000
```

The command uses the exported model, external data, and tokenizer files. It exposes the model as `muse-glimmer-30B` with a 65,536-token context at `http://127.0.0.1:8000` on the DGX Spark.

The Python server formats chat requests and passes them to the C++ worker. Its [inference engine](https://github.com/pytorch/executorch/blob/0a4a05e84d9642460d87ec2bbbd0e397667ec9c8/examples/models/muse-glimmer/runtime/engine/muse_glimmer_engine.cpp) uses the ExecuTorch `executorch::extension::Module` API and `load_method()` to load the exported inference methods. During generation, the ExecuTorch runtime runs those methods through the compiled CUDA delegate. The server returns the generated text and tool calls over HTTP.

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

Expect the model ID in `/v1/models` and an answer of `391` in the chat response. Reasoning might appear separately from the answer.

If an endpoint check fails, inspect the server terminal for the error. Correct missing paths or port conflicts, then rerun the server command.

## What you've accomplished and what's next

You've built the CUDA worker and exported Muse Glimmer 30B with text and image capability. You've started a local model endpoint.

Next, you'll set up Hermes Agent on the Arm-based CPU.
