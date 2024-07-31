---
title: Set up Llama 3
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Overview

Llama is a family of publicly available large language models (LLMs). Llama models have shown to perform well on a variety of natural language processing tasks, such as:

The models are subject to the [acceptable use policy](https://github.com/facebookresearch/llama/blob/main/USE_POLICY.md) and the [responsible use guide](https://ai.meta.com/static-resource/responsible-use-guide/).

### Quantization

If you are not familiar with the topic of quantization, take a minute to read a few sentences describing why it matters when you are working with LLMs.

Given the large size of many neural networks, a technique called quantization is often used to reduce the memory footprint. It allows large models to be run in memory constrained environments. In a nutshell, quantization takes floating point tensors in a neural network and converts it into data format with a smaller bit-width. It is possible to go from the FP32 data format to INT8 without seeing significant loss in model accuracy. *Dynamic quantization* is when the quantization happens at runtime.

The Llama model requires at least 4-bit quantization to fit into smaller devices, such as the Raspberry Pi 5. Read more about quantization in [the PyTorch Quantization documentation](https://pytorch.org/docs/stable/quantization.html).

Let's move on to getting, compiling and running the Llama model.

## Download and export the Llama 3 8B model

To get started with Llama 3, you obtain the pre-trained parameters by visiting [Meta's Llama Downloads](https://llama.meta.com/llama-downloads/) page. Request the access by filling out your details and read through and accept the Responsible Use Guide. This grants you a license and a download link which is valid for 24 hours. The Llama 3 8B model is used for this part, but the same instructions apply for other options as well with minimal modification.



Install the following requirements using a package manager of your choice, for example apt-get:
```bash
apt-get install md5sum wget
```

Clone the Llama 3 Git repository and install the dependencies in the Docker container:

```bash
git clone https://github.com/meta-llama/llama-models
cd llama-models
pip install -e .
pip install buck
```
Run the script to download, and paste the download link from the email when prompted.
```bash
cd models/llama3_1
./download.sh
```
You will be asked which models you would like to download. Enter `meta-llama-3.1-8b` to get the model used for this learning path.
```output
 **** Model list ***
 -  meta-llama-3.1-405b
 -  meta-llama-3.1-70b
 -  meta-llama-3.1-8b
 -  meta-llama-guard-3-8b
 -  prompt-guard
```
When the download is finished, you should see the following files in the new folder

```bash
$ ls Meta-Llama-3.1-8B
consolidated.00.pth  params.json  tokenizer.model
```


{{% notice Note %}}
1. If you encounter the error "Sorry, we could not process your request at this moment", it might mean you have initiated two license processes simultaneously. Try modifying the affiliation field to work around it.
2. You may have to run the `download.sh` script as root, or modify the execution privileges with `chmod`.
{{% /notice %}}

## Compile model file

The next step is to generate a `.pte` file that can be used for prompts. From the `executorch` directory, compile the model executable. Note the quantization option, which reduces the model size significantly.

If you've followed the tutorial, this should now take you to the `executorch` base directory.
```bash {cwd="executorch"}
cd ../../../
```
```bash
python -m examples.models.llama2.export_llama --checkpoint llama-models/models/llama3_1/Meta-Llama-3.1-8B/consolidated.00.pth \
-p llama-models/models/llama3_1/Meta-Llama-3.1-8B/params.json -kv --use_sdpa_with_kv_cache -X -qmode 8da4w \
--group_size 128 -d fp32 --metadata '{"get_bos_id":128000, "get_eos_id":128001}' \
--embedding-quantize 4,32 --output_name="llama3_kv_sdpa_xnn_qe_4_32.pte"
```

Where `<consolidated.00.pth>` and `<params.json>` are the paths to the downloaded model files, found in llama3/Meta-Llama-3-8B by default. This step might take some time.


## Optional: Evaluate Llama 3 model accuracy

You can evaluate model accuracy using the same arguments as above:

``` bash
python -m examples.models.llama2.eval_llama -c <consolidated.00.pth> \
-p <params.json> -t <tokenizer.model> -d fp32 --max_seq_len 2048 --limit 1000
```

{{% notice Warning %}}
Model evaluation without a GPU will take a long time, therefore this step is optional.
{{% /notice %}}

## Compile and build the executable

Follow the steps below to build ExecuTorch and the Llama runner to run models.

The final step for running the model is to build the `llama_runner` which is the executable to interact with the model. Compile and build ExecuTorch with `cmake`:

{{% notice Note %}}
Omit the `-DEXECUTORCH_USE_TIKTOKEN=ON` option if you are building Llama 2.
{{% /notice %}}

``` bash
cmake -DPYTHON_EXECUTABLE=python \
    -DCMAKE_INSTALL_PREFIX=cmake-out \
    -DEXECUTORCH_ENABLE_LOGGING=1 \
    -DCMAKE_BUILD_TYPE=Release \
    -DEXECUTORCH_BUILD_EXTENSION_MODULE=ON \
    -DEXECUTORCH_BUILD_EXTENSION_DATA_LOADER=ON \
    -DEXECUTORCH_BUILD_XNNPACK=ON \
    -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_OPTIMIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_CUSTOM=ON \
    -Bcmake-out .
```
```bash
cmake --build cmake-out -j16 --target install --config Release
```

The CMake build options are available on [GitHub](https://github.com/pytorch/executorch/blob/main/CMakeLists.txt#L59).

Similarly, compile and build the `llama_runner`:

``` bash
cmake -DPYTHON_EXECUTABLE=python \
    -DEXECUTORCH_USE_TIKTOKEN=ON \
    -DCMAKE_INSTALL_PREFIX=cmake-out \
    -DCMAKE_BUILD_TYPE=Release \
    -DEXECUTORCH_BUILD_KERNELS_CUSTOM=ON \
    -DEXECUTORCH_BUILD_KERNELS_OPTIMIZED=ON \
    -DEXECUTORCH_BUILD_XNNPACK=ON \
    -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
    -Bcmake-out/examples/models/llama2 \
    examples/models/llama2
```
```bash
cmake --build cmake-out/examples/models/llama2 -j16 --config Release
```


Now you know how to compile an LLM with ExecuTorch. At this point, you have everything you need to put the model to the test.

## Run the model

``` bash
cmake-out/examples/models/llama2/llama_main --model_path=<model pte file> --tokenizer_path=<tokenizer.model> \
--prompt="Write a python script that prints the first 15 numbers in the Fibonacci series. Annotate the script with comments explaining what the code does."
```

The run options are available on [GitHub](https://github.com/pytorch/executorch/blob/main/examples/models/llama2/main.cpp#L18-L40).

{{% notice Note %}}
If you are not running Llama 3, you must convert the `tokenizer.model` to a `.bin` file. This step is described in the [ExecuTorch examples guide](https://github.com/pytorch/executorch/blob/main/examples/models/llama2/README.md#option-a-download-and-export-llama-2-7b-model).
{{% /notice %}}

If all goes well, you will see the model output along with some memory statistics. Some output has been omitted for better readability.
```console
pi@raspberrypi5:~ $ ./llama_main  \
    --model_path=./llama3_kv_sdpa_xnn_qe_4_32.pte  \
    --tokenizer_path=./tokenizer.model \
    --cpu_threads=4 \
    --prompt="Write a python script that prints the first 15 numbers in the Fibonacci series. Annotate the script with comments explaining what the code does."

I 00:00:00.000242 executorch:main.cpp:64] Resetting threadpool with num threads = 4
I 00:00:00.000715 executorch:runner.cpp:50] Creating LLaMa runner: model_path=./llama3_kv_sdpa_xnn_qe_4_32.pte, tokenizer_path=./tokenizer.model
I 00:00:46.844266 executorch:runner.cpp:69] Reading metadata from model
I 00:00:46.844363 executorch:runner.cpp:134] get_vocab_size: 128256
I 00:00:46.844371 executorch:runner.cpp:134] get_bos_id: 128000
I 00:00:46.844375 executorch:runner.cpp:134] get_eos_id: 128001
I 00:00:46.844378 executorch:runner.cpp:134] get_n_bos: 1
I 00:00:46.844382 executorch:runner.cpp:134] get_n_eos: 1
I 00:00:46.844386 executorch:runner.cpp:134] get_max_seq_len: 128
I 00:00:46.844392 executorch:runner.cpp:134] use_kv_cache: 1
I 00:00:46.844396 executorch:runner.cpp:134] use_sdpa_with_kv_cache: 1
I 00:00:46.844400 executorch:runner.cpp:134] append_eos_to_prompt: 0
```

You now know how to run a Llama model in RaspBerry Pi OS using ExecuTorch. If you have access to the RPi 5, move on to deploy it in the next section.

