---
title: Launch LLM Service on Arm
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, we will build and launch the `llama.cpp` service on the Arm-based CPU.

### Llama 3.1 model & llama.cpp

The [Llama-3.1-8B model](https://huggingface.co/cognitivecomputations/dolphin-2.9.4-llama3.1-8b-gguf) from Meta belongs to the Llama 3.1 model family and is free to use for research and commercial purposes. Before you use the model, visit the Llama [website](https://llama.meta.com/llama-downloads/) and fill in the form to request access.

[llama.cpp](https://github.com/ggerganov/llama.cpp) is an open source C/C++ project that enables efficient LLM inference on a variety of hardware - both locally, and in the cloud. You can conveniently host a Llama 3.1 model using `llama.cpp`.


### Download and build llama.cpp

Run the following commands to install make, cmake, gcc, g++, and other essential tools required for building llama.cpp from source:

```bash
sudo apt install make cmake -y
sudo apt install gcc g++ -y
sudo apt install build-essential -y
```

You are now ready to start building `llama.cpp`. 

Clone the source repository for llama.cpp:

```bash
git clone https://github.com/ggerganov/llama.cpp
```

By default, `llama.cpp` builds for CPU only on Linux and Windows. You don't need to provide any extra switches to build it for the Arm CPU that you run it on.

Run `make` to build it:

```bash
cd llama.cpp
make GGML_NO_LLAMAFILE=1 -j$(nproc)
```

Check that `llama.cpp` has built correctly by running the help command:

```bash
./llama-cli -h
```

If `llama.cpp` has been built correctly, you will see the help option displayed. The output snippet looks like this:

```output
example usage:

  text generation:     ./llama-cli -m your_model.gguf -p "I believe the meaning of life is" -n 128

  chat (conversation): ./llama-cli -m your_model.gguf -p "You are a helpful assistant" -cnv
```


You can now download the model using the huggingface cli:

```bash
huggingface-cli download cognitivecomputations/dolphin-2.9.4-llama3.1-8b-gguf dolphin-2.9.4-llama3.1-8b-Q4_0.gguf --local-dir . --local-dir-use-symlinks False
```
The GGUF model format, introduced by the llama.cpp team, uses compression and quantization to reduce weight precision to 4-bit integers, significantly decreasing computational and memory demands and making Arm CPUs effective for LLM inference.


### Re-quantize the model weights

To re-quantize, run

```bash
./llama-quantize --allow-requantize dolphin-2.9.4-llama3.1-8b-Q4_0.gguf dolphin-2.9.4-llama3.1-8b-Q4_0_8_8.gguf Q4_0_8_8
```

This will output a new file, `dolphin-2.9.4-llama3.1-8b-Q4_0_8_8.gguf`, which contains reconfigured weights that allow `llama-cli` to use SVE 256 and MATMUL_INT8 support.

> This requantization is optimal specifically for Graviton3. For Graviton2, the optimal requantization should be performed in the `Q4_0_4_4` format, and for Graviton4, the `Q4_0_4_8` format is the most suitable for requantization.

### Start the LLM Service
You can utilize the llama.cpp server program and send requests via an OpenAI-compatible API. This allows you to develop applications that interact with the LLM multiple times without having to repeatedly start and stop it. Additionally, you can access the server from another machine where the LLM is hosted over the network.

Start the server from the command line, and it listens on port 8080:

```shell
./llama-server -m dolphin-2.9.4-llama3.1-8b-Q4_0_8_8.gguf -n 2048 -t 64 -c 65536  --port 8080
```
```text
'main: server is listening on 127.0.0.1:8080 - starting the main loop
```

You can also adjust the parameters of the launched LLM to adapt it to your server hardware to obtain ideal performance. For more parameter information, see the `llama-server --help` command.

If you struggle to perform this step, you can refer to the [this documents](https://learn.arm.com/learning-paths/servers-and-cloud-computing/llama-cpu/llama-chatbot/) for more information.

You have started the LLM service on your Arm-based CPU. Next, we directly interact with the service using the OpenAI SDK.


