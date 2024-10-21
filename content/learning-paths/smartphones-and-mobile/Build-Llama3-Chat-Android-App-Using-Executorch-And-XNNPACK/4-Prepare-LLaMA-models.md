---
title: Prepare Llama models for ExecuTorch
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download and export the Llama 3.2 1B model

To get started with Llama 3, you obtain the pre-trained parameters by visiting [Meta's Llama Downloads](https://llama.meta.com/llama-downloads/) page. Request the access by filling out your details and read through and accept the Responsible Use Guide. This grants you a license and a download link which is valid for 24 hours. The Llama 3.2 1B model is used for this part, but the same instructions apply for other options as well with minimal modification.

Install the `llama-stack` package from `pip`.
```bash
pip install llama-stack
```
Run the command to download, and paste the download link from the email when prompted.
```bash
llama model download --source meta --model-id Llama3.2-1B
```

When the download is finished, the installation path is printed as output.
```output
Successfully downloaded model to /<path-to-home>/.llama/checkpoints/Llama3.2-1B
```

Verify by viewing the downloaded files under this path:

```bash
ls $HOME/.llama/checkpoints/Llama3.2-1B
checklist.chk           consolidated.00.pth     params.json             tokenizer.model
```

{{% notice Working Directory %}}
The rest of the instructions should be executed from the ExecuTorch base directory.
{{% /notice %}}

Export model and generate `.pte` file. Run the Python command to export the model to your current directory.

```bash
python3 -m examples.models.llama.export_llama \
--checkpoint $HOME/.llama/checkpoints/Llama3.2-1B/consolidated.00.pth \
--params $HOME/.llama/checkpoints/Llama3.2-1B/params.json \
-kv --use_sdpa_with_kv_cache -X --xnnpack-extended-ops -qmode 8da4w \
--group_size 256 -d fp32 \
--metadata '{"get_bos_id":128000, "get_eos_ids":[128009, 128001, 128006, 128007]}' \
--embedding-quantize 4,32 \
--output_name="llama3_1B_kv_sdpa_xnn_qe_4_128_1024_embedding_4bit.pte" \
--max_seq_length 1024
```

Due to the larger vocabulary size of Llama 3, you should quantize the embeddings with `--embedding-quantize 4,32` to further reduce the model size.

## Optional: Evaluate Llama 3 model accuracy

You can evaluate model accuracy using the same arguments as above:

``` bash
python -m examples.models.llama2.eval_llama \
-c $HOME/.llama/checkpoints/Llama3.2-1B/consolidated.00.pth \
-p $HOME/.llama/checkpoints/Llama3.2-1B/params.json \
-t $HOME/.llama/checkpoints/Llama3.2-1B/tokenizer.model \
-d fp32 --max_seq_len 2048 --limit 1000
```

{{% notice Warning %}}
Model evaluation without a GPU will take a long time. On a MacBook with an M3 chip and 18GB RAM this took 10+ hours.
{{% /notice %}}

## Validate models on the development machine

Before running models on a smartphone, you can validate them on your development computer.

Follow the steps below to build ExecuTorch and the Llama runner to run models.

1. Build executorch with optimized CPU performance:

    ``` bash
    cmake -DPYTHON_EXECUTABLE=python \
    -DCMAKE_INSTALL_PREFIX=cmake-out \
    -DEXECUTORCH_ENABLE_LOGGING=1 \
    -DCMAKE_BUILD_TYPE=Release \
    -DEXECUTORCH_BUILD_EXTENSION_DATA_LOADER=ON \
    -DEXECUTORCH_BUILD_EXTENSION_MODULE=ON \
    -DEXECUTORCH_BUILD_EXTENSION_TENSOR=ON \
    -DEXECUTORCH_BUILD_XNNPACK=ON \
    -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_OPTIMIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_CUSTOM=ON \
    -Bcmake-out .

cmake --build cmake-out -j16 --target install --config Release
    ```

    The CMake build options are available on [GitHub](https://github.com/pytorch/executorch/blob/main/CMakeLists.txt#L59).

2. Build the Llama runner:

{{% notice Note %}}
For Llama 2, remove the `-DEXECUTORCH_USE_TIKTOKEN=ON` option.
{{% /notice %}}

Run cmake:

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

cmake --build cmake-out/examples/models/llama2 -j16 --config Release
```

3. Run the model:

    ``` bash
    cmake-out/examples/models/llama2/llama_main --model_path=llama3.2_bl256_maxlen1024.pte --tokenizer_path=$HOME/.llama/checkpoints/Llama3.2-1B/tokenizer.model --prompt=<prompt>
    ```

    The run options are available on [GitHub](https://github.com/pytorch/executorch/blob/main/examples/models/llama2/main.cpp#L18-L40).
