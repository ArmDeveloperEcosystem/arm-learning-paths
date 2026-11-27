---
title: Build the inspection application with CMake
weight: 4
layout: learningpathall
---

## Get the example

In the **Zena dashboard terminal**, clone the example repository and enter the demo directory.

```sh
cd /root
git clone https://gitlab.arm.com/learning-code-examples/code-examples.git &&
cd code-examples/learning-paths/automotive/visual-inspection-with-siemens-ana
```

## How the inspection works

![The worker sends each gear crop and inspection prompt to Qwen. The dashboard serves the saved prediction. Codex ImageGen prompt: Draw four connected blocks on a transparent background showing V4L2 camera input, JPEG gear capture, Qwen inference over HTTP, and results from GET /api/results.#center](inspection-pipeline.png "ImageGen prompt (abridged): Draw four connected blocks on a transparent background showing V4L2 camera input, JPEG gear capture, Qwen inference over HTTP, and results from GET /api/results.")

This minimal example captures one gear at a time. The task-specific code in `inspection/gear_capture.cpp` detects a gear on the belt and crops its image. The Python worker sends the JPEG crop and inspection prompt over HTTP to Qwen running on the llama.cpp server. The source build enables Arm KleidiAI support for CPU inference. The worker saves the prediction in `result.json`, and the dashboard serves it through `GET /api/results`. To adapt the inspection criteria, edit the prompt and accepted conditions in `dashboard/qwen_worker.py`.

## Install CMake for AArch64

In the **Zena dashboard terminal**, check which version is available. Include `/usr/local/bin` so the shell can find an existing installation there.

```sh
export PATH="/usr/local/bin:$PATH"
cmake --version
```

If the version is 3.20 or later, continue to **Build the application**. If CMake is missing or older, install version 3.28.6 as follows.

In the same terminal, start Bash with `bash` if you are using another shell, then run the following block. It installs CMake under `/opt`, makes it available in this shell, and returns you to the demo directory.

```bash
pushd /tmp &&
wget https://github.com/Kitware/CMake/releases/download/v3.28.6/cmake-3.28.6-linux-aarch64.tar.gz &&
mkdir -p /opt /usr/local/bin &&
tar -xzf cmake-3.28.6-linux-aarch64.tar.gz -C /opt &&
ln -sfn /opt/cmake-3.28.6-linux-aarch64/bin/cmake /usr/local/bin/cmake &&
popd
```

Verify the installation:

```sh
cmake --version
```

The first line should read:

```text
cmake version 3.28.6
```

## Build the application

From the demo directory, configure and build the application. CMake uses an existing working `llama-server` or downloads and builds the runtime when needed. Allow about 2–3 minutes for a fresh build on a 16-vCPU vSoC.

```sh
cmake -S . -B build && cmake --build build --parallel "$(nproc)"
```

When CMake builds the runtime from source, successful output ends with lines like these:

```text
[100%] Completed 'llama_runtime'
[100%] Built target llama_runtime
```
