---
title: Prepare Llama models for ExecuTorch
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download and export the Llama 3 8B model

To get started with Llama 3, you obtain the pre-trained parameters by visiting [Meta's Llama Downloads](https://llama.meta.com/llama-downloads/) page. Request the access by filling out your details and read through and accept the Responsible Use Guide. This grants you a license and a download link which is valid for 24 hours. The Llama 3 8B model is used for this part, but the same instructions apply for other options as well with minimal modification.

Install the following requirements using a package manager of your choice, for example apt-get:
```bash
apt-get install md5sum wget
```

Clone the Llama models Git repository and install the dependencies:

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
You will be asked which models you would like to download. Enter `meta-llama-3.1-8b`.
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

Export model and generate `.pte` file. Run the Python command to export the model:

```bash
python -m examples.models.llama2.export_llama --checkpoint llama-models/models/llama3_1/Meta-Llama-3.1-8B/consolidated.00.pth -p llama-models/models/llama3_1/Meta-Llama-3.1-8B/params.json -kv --use_sdpa_with_kv_cache -X -qmode 8da4w  --group_size 128 -d fp32 --metadata '{"get_bos_id":128000, "get_eos_id":128001}' --embedding-quantize 4,32 --output_name="llama3_kv_sdpa_xnn_qe_4_32.pte"
```

Due to the larger vocabulary size of Llama 3, you should quantize the embeddings with `--embedding-quantize 4,32` to further reduce the model size.

## Optional: Evaluate Llama 3 model accuracy

You can evaluate model accuracy using the same arguments as above:

``` bash
python -m examples.models.llama2.eval_llama -c llama-models/models/llama3_1/Meta-Llama-3.1-8B/consolidated.00.pth -p llama-models/models/llama3_1/Meta-Llama-3.1-8B/params.json -t llama-models/models/llama3_1/Meta-Llama-3.1-8B/tokenizer.model -d fp32 --max_seq_len 2048 --limit 1000
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

2. Build the Llama runner:

{{% notice Note %}}
For Llama 3, add `-DEXECUTORCH_USE_TIKTOKEN=ON` option.
{{% /notice %}}

Run cmake:

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

3. Run the model:

    ``` bash
    cmake-out/examples/models/llama2/llama_main --model_path=llama3_kv_sdpa_xnn_qe_4_32.pte --tokenizer_path=llama-models/models/llama3_1/Meta-Llama-3.1-8B/tokenizer.model --prompt=<prompt>
    ```

    The run options are available on [GitHub](https://github.com/pytorch/executorch/blob/main/examples/models/llama2/main.cpp#L18-L40).
