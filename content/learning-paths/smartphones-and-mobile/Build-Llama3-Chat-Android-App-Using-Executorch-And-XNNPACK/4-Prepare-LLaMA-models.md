---
title: Prepare LLaMA models for ExecuTorch
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download and Export LLaMA models

There are multiple options available to download models. Select the one that works best for you.

### Option A: download and export Llama 2 7B model

For Llama 2 7B, your device may require at least 32GB RAM.

1. Llama2 pretrained parameters can be downloaded from [Meta's official website](https://ai.meta.com/resources/models-and-libraries/llama-downloads/) or from [Hugging Face](https://huggingface.co/meta-llama/Llama-2-7b).

2. Edit `params.json` file. Replace `"vocab_size": -1` with `"vocab_size": 32000`. This is a short-term workaround.

3. Export the model and generate a `.pte` file:

    ``` bash
    python -m examples.models.llama2.export_llama --checkpoint <checkpoint.pth> --params <params.json> -kv --use_sdpa_with_kv_cache -X -qmode 8da4w --group_size 128 -d fp32
    ```

4. Create a `tokenizer.bin` file:

    ``` bash
     python -m examples.models.llama2.tokenizer.tokenizer -t tokenizer.model -o tokenizer.bin
    ```

### Option B: download and export stories110M model

If you want to deploy and run a smaller model for educational purposes. 

From the `executorch` root directory follow these steps:

1. Download `stories110M.pt` and `tokenizer.model` from Github.

    ``` bash
    wget "https://huggingface.co/karpathy/tinyllamas/resolve/main/stories110M.pt"
    wget "https://raw.githubusercontent.com/karpathy/llama2.c/master/tokenizer.model"
    ```

2. Create params file.

    ``` bash
    echo '{"dim": 768, "multiple_of": 32, "n_heads": 12, "n_layers": 12, "norm_eps": 1e-05, "vocab_size": 32000}' > params.json
    ```

3. Export model and generate `.pte` file.

    ``` bash
    python -m examples.models.llama2.export_llama -c stories110M.pt -p params.json -X
    ```

4. Create tokenizer.bin.

    ``` bash
    python -m examples.models.llama2.tokenizer.tokenizer -t tokenizer.model -o tokenizer.bin
    ```

### Option C: download and export Llama 3 8B model

You can export and run the original Llama 3 8B model.

1. Download Llama3 pretrained parameters from [Meta's official llama3 repository](https://github.com/meta-llama/llama3/).

2. Clone the Llama 3 Git repository

    ```bash
    git clone https://github.com/meta-llama/llama3.git
     ```

3. Navigate to [llama-downloads](https://llama.meta.com/llama-downloads/), enter your e-mail address and accept the license to receive the URL for Llama 3 model downloads.

4. Download required models

    ```bash
    cd llama3
    ./download.sh
    # Enter the URL and desired model
    ```

5. Export model and generate `.pte` file

    Run the Python command to export the model:

    ```bash
    python -m examples.models.llama2.export_llama --checkpoint <consolidated.00.pth> -p <params.json> -kv --use_sdpa_with_kv_cache -X -qmode 8da4w  --group_size 128 -d fp32 --metadata '{"get_bos_id":128000, "get_eos_id":128001}' --embedding-quantize 4,32 --output_name="llama3_kv_sdpa_xnn_qe_4_32.pte"
    ```

    Due to the larger vocabulary size of Llama 3, you should quantize the embeddings with `--embedding-quantize 4,32` to further reduce the model size.

## Evaluate model accuracy

You can evaluate model accuracy using the same arguments from above:

``` bash
python -m examples.models.llama2.eval_llama -c <checkpoint.pth> -p <params.json> -t <tokenizer.model> -d fp32 --max_seq_len <max sequence length> --limit <number of samples>
```

The Wikitext results generated above used: `{max_seq_len: 2048, limit: 1000}`

{{% notice Warning %}}
Model evaluation without a GPU may take a long time, especially on larger models.
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
        -DEXECUTORCH_BUILD_EXTENSION_MODULE=ON \
        -DEXECUTORCH_BUILD_EXTENSION_DATA_LOADER=ON \
        -DEXECUTORCH_BUILD_XNNPACK=ON \
        -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
        -DEXECUTORCH_BUILD_KERNELS_OPTIMIZED=ON \
        -DEXECUTORCH_BUILD_KERNELS_CUSTOM=ON \
        -Bcmake-out .

    cmake --build cmake-out -j16 --target install --config Release
    ```

    The CMake build options are available on [GitHub](https://github.com/pytorch/executorch/blob/main/CMakeLists.txt#L59).

2. Build Llama runner:

    ``` bash
    cmake -DPYTHON_EXECUTABLE=python \
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

{{% notice Note %}}
For Llama3, add `-DEXECUTORCH_USE_TIKTOKEN=ON` option when building the Llama runner.
{{% /notice %}}

3. Run the model: 

    ``` bash
    cmake-out/examples/models/llama2/llama_main --model_path=<model pte file> --tokenizer_path=<tokenizer.bin> --prompt=<prompt>
    ```

    The run options are available on [GitHub](https://github.com/pytorch/executorch/blob/main/examples/models/llama2/main.cpp#L18-L40).

    For Llama3, you can pass the original `tokenizer.model` (without converting to `.bin` file).
