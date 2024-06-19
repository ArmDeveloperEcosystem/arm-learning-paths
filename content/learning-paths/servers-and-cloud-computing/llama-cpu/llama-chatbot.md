---
title: Run a Large Language model (LLM) chatbot on Arm servers
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin
The instructions in this Learning Path are for any Arm server running Ubuntu 22.04 LTS. You need an Arm server instance with at least four cores and 8GB of RAM to run this example. The instructions have been tested on AWS Graviton3 (c7g) instances. 

## Overview

Arm CPUs are widely used in traditional ML and AI use cases. In this Learning Path, you learn how to run generative AI inference-based use cases like a LLM chatbot on Arm-based CPUs. You do this by deploying the [Llama-2-7B-Chat model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF) on your Arm-based CPU using `llama.cpp`. 

[llama.cpp](https://github.com/ggerganov/llama.cpp) is an open source C/C++ project developed by Georgi Gerganov that enables efficient LLM inference on a variety of hardware - both locally, and in the cloud. 

## About the Llama 2 model and GGUF model format

The [Llama-2-7B-Chat model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF) from Meta belongs to the Llama 2 model family and is free to use for research and commercial purposes. Before you use the model, visit the Llama [website](https://llama.meta.com/llama-downloads/) and fill in the form to request access.


Llama 2 collection of models perform general natural language processing (NLP) tasks such as text generation. You can access the base foundation Llama 2 model or select the specialized chat Llama 2 version that is already optimized for back-and-forth dialogue. In this Learning Path, you run the specialized chat model.
The Llama 2 family of models range in size from 7 billion to 70 billion parameters. The greater the number of parameters, the more information the model can store. This directly affects how well the model understands language and the model's general capabilities. LLMs that run efficiently on CPUs typically have lower numbers of parameters. For this example, the 7 billion (7b) model is ideal for retaining quality chatbot capability while also running efficiently on your Arm-based CPU. 

Traditionally, the training and inference of LLMs has been done on GPUs using full-precision 32-bit (FP32) or half-precision 16-bit (FP16) data type formats for the model parameter and weights. Recently, a new binary model format called GGUF was introduced by the `llama.cpp` team. This new GGUF model format uses compression and quantization techniques that remove the dependency on using FP32 and FP16 data type formats. For example, GGUF supports quantization where model weights that are generally stored as FP16 data types are scaled down to 4-bit integers. This significantly reduces the need for computational resources and the amount of RAM required. These advancements made in the model format and the data types used make Arm CPUs a great fit for running LLM inferences.   
 
## Install dependencies 

Install the following packages on your Arm based server instance:

```bash
sudo apt update
sudo apt install make cmake -y
```

You also need to install `gcc` on your machine:

```bash
sudo apt install gcc g++ -y
sudo apt install build-essential -y
```

## Download and build llama.cpp

You are now ready to start building `llama.cpp`. 

Clone the source repository for llama.cpp:

```bash
git clone https://github.com/ggerganov/llama.cpp
```

By default, `llama.cpp` builds for CPU only on Linux and Windows. You don't need to provide any extra switches to build it for the Arm CPU that you run it on.

Run `make` to build it:

```bash
cd llama.cpp
make -j$(nproc)
```

Check that `llama.cpp` has built correctly by running the help command:

```bash
./llama-cli -h
```

If `llama.cpp` has built correctly on your machine, you will see the help options being displayed. A snippet of the output is shown below:

```output
usage: ./llama-cli [options]

general:

  -h,    --help, --usage          print usage and exit
         --version                show version and build info
  -v,    --verbose                print verbose information
         --verbosity N            set specific verbosity level (default: 0)
         --verbose-prompt         print a verbose prompt before generation (default: false)
         --no-display-prompt      don't print prompt at generation (default: false)
  -co,   --color                  colorise output to distinguish prompt and user input from generations (default: false)
  -s,    --seed SEED              RNG seed (default: -1, use random seed for < 0)
  -t,    --threads N              number of threads to use during generation (default: 4)
  -tb,   --threads-batch N        number of threads to use during batch and prompt processing (default: same as --threads)
  -td,   --threads-draft N        number of threads to use during generation (default: same as --threads)
  -tbd,  --threads-batch-draft N  number of threads to use during batch and prompt processing (default: same as --threads-draft)
         --draft N                number of tokens to draft for speculative decoding (default: 5)
  -ps,   --p-split N              speculative decoding split probability (default: 0.1)
  -lcs,  --lookup-cache-static FNAME
                                  path to static lookup cache to use for lookup decoding (not updated by generation)
  -lcd,  --lookup-cache-dynamic FNAME
                                  path to dynamic lookup cache to use for lookup decoding (updated by generation)
  -c,    --ctx-size N             size of the prompt context (default: 0, 0 = loaded from model)
  -n,    --predict N              number of tokens to predict (default: -1, -1 = infinity, -2 = until context filled)
  -b,    --batch-size N           logical maximum batch size (default: 2048)
```


## Install Hugging Face Hub

There are a few different ways you can download the Llama-2-7B Chat model. In this Learning Path, you download the model from Hugging Face.

{{% notice Note %}} Use of Llama-2-7B-Chat model is governed by the Meta license. Before you proceed to download the model, please visit the Llama [website](https://llama.meta.com/llama-downloads/) and fill in the form. {{% /notice %}}

[Hugging Face](https://huggingface.co/) is an open source AI community where you can host your own AI models, train them and collaborate with others in the community. You can browse through the thousands of models that are available for a variety of use cases like NLP, audio, and computer vision.

The `huggingface_hub` library provides APIs and tools that let you easily download and fine-tune pre-trained models. You will use `huggingface-cli` to download the [Llama-2-7B-Chat model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF).

Install the required Python packages:

```bash
sudo apt install python-is-python3 python3-pip python3-venv -y
```

Create and activate a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Your terminal prompt now has the `(venv)` prefix indicating the virtual environment is active. Use this virtual environment for the remaining commands.

Install the `huggingface_hub` python library using `pip`:

```bash
pip install huggingface_hub
```

You can now download the model using the huggingface cli:

```bash
huggingface-cli download TheBloke/Llama-2-7b-Chat-GGUF llama-2-7b-chat.Q4_K_M.gguf --local-dir . --local-dir-use-symlinks False
```
Before you proceed and run this model, take a quick look at what `Q4_K_M` in the model name denotes.

## Quantization format

`Q4_K_M` in the model name refers to the quantization method the model uses. The goal of quantization is to reduce the size of the model (to reduce the memory space required) and faster (to reduce memory bandwidth bottlenecks transferring large amounts of data from memory to a processor). The primary trade-off to keep in mind when reducing a model's size is maintaining quality of performance. Ideally, a model is quantized to meet size and speed requirements while not having a negative impact on performance. 

Llama 2 was originally trained and published using the bfloat16 data type, meaning that each of the 7 billion model parameters takes up 16 bits of memory to store. Putting that into real terms, multiplying 16 bits per parameter by 7 billion parameters, the base foundation llama-2-7b model is just over 13Gb in size. 

This model is `llama-2-7b-chat.Q4_K_M.gguf`, so what does each component mean in relation to the quantization level? The main thing to note is the number of bits per parameter, which is denoted by 'Q4' in this case or 4-bit integer. As a result, by only using 4 bits per parameter for 7 billion parameters, the model drops to be 3.6Gb in size.

Here is a quick lookup to the rest of the quantization parts for the Llama-2 model family as it exists today:

| quantization-method | # of bits per parameter | quantization format (does not apply to quantization method 'IQ') | quantization method specifics |
| ------------------- | ----------------------- | ---------------------------------------------------------------- | ------------------ |
| Q, IQ, F, FP        | 2,3,4,5,6,7,8,16,32     | _0, _1, _K                                                       | _XXS, _XS, _S, _M, _L    |

Some examples:

* Q8_0 --> Straightforward quantization method (indicated with _0 or _1), with an 8 bit integer per parameter.
* Q4_K_M --> K-quant method (indicated with _K), with a 4 bit integer per parameter, with the _M quantization mix type used.
* IQ2_XXS --> I-quant method (indicated with _IQ), with the _XXS quantization mix type used.
* F16  --> Using a 16 bit floating point number per parameter (no other quantization method used, only rounding a number if starting from a 32 bit floating point number).

Each quantization method has a unique approach to quantizing parameters. The deeper technical details of different quantization methodologies are outside the scope of this guide. The main takeaway is that selecting the right model quantization is critical to running an LLM effectively on your hardware, and the most impactful quantization decision is the number of bits per parameter. You can try switching out different quantization levels of the same model and observe how the model size, response speed, and quality change.


## Run the Llama-2-7B-Chat LLM model 

Now run the llama-2-7b-chat model in interactive mode:

```bash
./llama-cli  -m llama-2-7b-chat.Q4_K_M.gguf --color -c 4096 --temp 0.7 --repeat_penalty 1.1 -n -1 -if 
```

You will see lots of interesting statistics being printed from llama.cpp about the model and the system, followed by a prompt where you can start your chat style dialogue with the model. A snippet of the output from running this model on an AWS Graviton3 c7g.xlarge instance is shown below:

```output
llm_load_tensors: ggml ctx size =    0.15 MiB
llm_load_tensors:        CPU buffer size =  3891.24 MiB
..................................................................................................
llama_new_context_with_model: n_ctx      = 4096
llama_new_context_with_model: n_batch    = 2048
llama_new_context_with_model: n_ubatch   = 512
llama_new_context_with_model: flash_attn = 0
llama_new_context_with_model: freq_base  = 10000.0
llama_new_context_with_model: freq_scale = 1
llama_kv_cache_init:        CPU KV buffer size =  2048.00 MiB
llama_new_context_with_model: KV self size  = 2048.00 MiB, K (f16): 1024.00 MiB, V (f16): 1024.00 MiB
llama_new_context_with_model:        CPU  output buffer size =     0.12 MiB
llama_new_context_with_model:        CPU compute buffer size =   296.01 MiB
llama_new_context_with_model: graph nodes  = 1030
llama_new_context_with_model: graph splits = 1

system_info: n_threads = 4 / 4 | AVX = 0 | AVX_VNNI = 0 | AVX2 = 0 | AVX512 = 0 | AVX512_VBMI = 0 | AVX512_VNNI = 0 | AVX512_BF16 = 0 | FMA = 0 | NEON = 1 | SVE = 1 | ARM_FMA = 1 | F16C = 0 | FP16_VA = 1 | WASM_SIMD = 0 | BLAS = 0 | SSE3 = 0 | SSSE3 = 0 | VSX = 0 | MATMUL_INT8 = 1 | LLAMAFILE = 1 |
main: interactive mode on.
sampling:
        repeat_last_n = 64, repeat_penalty = 1.100, frequency_penalty = 0.000, presence_penalty = 0.000
        top_k = 40, tfs_z = 1.000, top_p = 0.950, min_p = 0.050, typical_p = 1.000, temp = 0.700
        mirostat = 0, mirostat_lr = 0.100, mirostat_ent = 5.000
sampling order:
CFG -> Penalties -> top_k -> tfs_z -> typical_p -> top_p -> min_p -> temperature
generate: n_ctx = 4096, n_batch = 2048, n_predict = -1, n_keep = 1


== Running in interactive mode. ==
 - Press Ctrl+C to interject at any time.
 - Press Return to return control to the AI.
 - To return control without starting a new line, end your input with '/'.
 - If you want to submit another line, end your input with '\'.

Write a C program to add 2 floating point numbers

Write a C program to add two floating point numbers using the `+` operator.

For example, if you enter:

`float1 = 3.5; float2 = 4.8;`

The program should print:

`Addition result: 8.3`

Explanation:

In C, floating point numbers are represented as a binary representation of the number. The `+` operator performs an addition by converting both operands to a binary representation and then adding them together.

Note: The output is rounded to 2 decimal places.

Write a program to test this functionality.

Here is an example of how you could do this:

#include <stdio.h>

int main() {
    float float1 = 3.5;
    float float2 = 4.8;
    float result = float1 + float2;
    printf("Addition result: %f\n", result);
    return 0;
}

This program defines two floating point variables `float1` and `float2`, initializes them to the values 3.5 and 4.8 respectively, and then adds them together using the `+` operator. Finally, it prints the result to the console using `printf()`.
Note that the output is rounded to 2 decimal places.
I hope this helps! Let me know if you have any questions.
```

The `system_info` printed from llama.cpp highlights important architectural features present on your hardware that improve the performance of the model execution. In the output shown above from running on an AWS Graviton3 instance, you will see:

  * NEON = 1 This flag indicates support for Arm's Neon technology which is an implementation of the Advanced SIMD instructions
  * ARM_FMA = 1 This flag indicates support for Arm Floating-point Multiply and Accumulate instructions 
  * MATMUL_INT8 = 1 This flag indicates support for Arm int8 matrix multiplication instructions


To exit and stop using the model, use Ctrl+C. At exit, a few timing parameters are printed by llama.cpp from the execution of the model on your Arm CPU. 

For example, you might see something similar to below:

```output
llama_print_timings:        load time =     854.62 ms
llama_print_timings:      sample time =      76.88 ms /   368 runs   (    0.21 ms per token,  4786.49 tokens per second)
llama_print_timings: prompt eval time =   12220.83 ms /    56 tokens (  218.23 ms per token,     4.58 tokens per second)
llama_print_timings:        eval time =   43196.33 ms /   366 runs   (  118.02 ms per token,     8.47 tokens per second)
llama_print_timings:       total time =   70607.67 ms /   422 tokens
```

* load time refers to the time taken to load the model.
* prompt eval time refers to the time taken to process the prompt before generating the new text. In this example, it shows that it evaluated 56 tokens in 12220.83 ms. 
* eval time refers to the time taken to generate the output. Generally anything above 10 tokens per second is faster than what humans can read. 

You have successfully run a LLM chatbot, all running on your Arm AArch64 CPU on your server. You can continue experimenting and trying out the model with different prompts.

