---
title: Measure and accelerate the inference performance of PyTorch models on Arm servers
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin
These instructions apply to any Arm server running Ubuntu 22.04 LTS. For this example, you need an Arm server instance with at least four cores and 8GB of RAM. The instructions have been tested on AWS Graviton3 (c7g.4xlarge) instances.

## Overview
PyTorch is a widely-used Machine Learning framework for Python. In this learning path, you will explore how to measure the inference time of PyTorch models running on your Arm-based server using [PyTorch Benchmarks](https://github.com/pytorch/benchmark), a collection of open-source benchmarks for evaluating PyTorch performance. Understanding inference latency is crucial for optimizing machine learning applications, especially in production environments where performance can significantly impact user experience and resource utilization. 

You will learn how to install the PyTorch benchmark suite and compare inference performance using PyTorch's two modes of execution; eager Mode and `torch.compile` mode.

To begin, set up your environment by installing the required dependencies and PyTorch. Follow these steps:

## Set up Environment

First, install python and the required system packages:

```bash
sudo apt update
sudo apt install python-is-python3 python3-pip python3-venv -y
sudo apt-get install -y libgl1-mesa-glx
```

Next, use a virtual environment to manage your Python packages. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

With your virtual environment active, install PyTorch and its related libraries:

```bash
pip install torch torchvision torchaudio
```

## Clone the PyTorch Benchmark Repository

Clone the PyTorch Benchmark repository and check out a specific commit you will use for performance evaluation:

```bash
git clone https://github.com/pytorch/benchmark.git
cd benchmark
git checkout 9a5e4137299741e1b6fb7aa7f5a6a853e5dd2295
```
Install the PyTorch models you would like to benchmark. Here, let's install a variety of NLP, computer vision, and recommender models:

```bash
python3 install.py alexnet BERT_pytorch dlrm hf_Albert hf_Bart hf_Bert hf_Bert_large hf_BigBird \
hf_DistilBert hf_GPT2 hf_Longformer hf_Reformer hf_T5 mobilenet_v2 mobilenet_v3_large resnet152 \
resnet18 resnet50 timm_vision_transformer
```

{{% notice Note %}}
If you are using Python 3.12, the install script might fail with the following error:
```output
AttributeError: module 'pkgutil' has no attribute 'ImpImporter'.
Did you mean: 'zipimporter'
```

This issue can occur because `requirements.txt` installs a version of `numpy` that is incompatible with Python 3.12. To resolve it, change the pinned `numpy` version in `requirements.txt`.

```
numpy~=1.26.4
```
{{% /notice %}}

If you don't specify a model list for `install.py`, the script downloads all the models included in the benchmark suite.

Before running the benchmarks, configure your AWS Graviton3 instance to leverage available optimizations for improved PyTorch inference performance. 

This configuration includes settings to:

* Enable bfloat16 GEMM kernel support to accelerate fp32 inference.
* Set LRU cache capacity to an optimal value to avoid redundant primitive creation latency overhead.
* Enable Linux Transparent Huge Page (THP) allocations to reduce tensor memory allocation latency.
* Set the number of threads to use to match the number of cores on your system.

```bash
export DNNL_DEFAULT_FPMATH_MODE=BF16
export THP_MEM_ALLOC_ENABLE=1
export LRU_CACHE_CAPACITY=1024
export OMP_NUM_THREADS=16
```

With the environment set up and models installed, you're ready to run the benchmarks to measure your model inference performance.

Starting with PyTorch 2.0, there are two main execution modes: eager mode and `torch.compile` mode. The default mode of execution in PyTorch is eager mode, where operations are executed immediately as they are defined. In contrast, `torch.compile` transforms PyTorch code into graphs which can be executed more efficiently. This mode can improve model inferencing performance, particularly for models with repetitive computations.

Using the scripts included in the PyTorch Benchmark suite, you will now measure the model inference latencies in both eager mode and `torch.compile` mode to compare their performance.

### Measure Eager Mode Performance

Run the following command to collect performance data in eager mode for the downloaded models:

```bash
python3 run_benchmark.py cpu --model alexnet,BERT_pytorch,dlrm,hf_Albert,hf_Bart,hf_Bert,hf_Bert_large,hf_BigBird,hf_DistilBert,hf_GPT2,hf_Longformer,hf_Reformer,hf_T5,mobilenet_v2,mobilenet_v3_large,resnet152,resnet18,resnet50,timm_vision_transformer \
--test eval --metrics="latencies"
```
The benchmark results for all the models run are stored in the `.userbenchmark/cpu/` directory. The `cpu` user benchmark creates a timestamped folder `cpu-YYmmddHHMMSS` for each test, and aggregates all test results into a JSON file `metrics-YYmmddHHMMSS.json`, where `YYmmddHHMMSS` is the time you started the test. The metrics file shows the model inference latency, in milliseconds (msec) for each model you downloaded and ran. 

The results with eager mode should appear as follows:

```output
{
    "name": "cpu",
    "environ": {
        "pytorch_git_version": "2236df1770800ffea5697b11b0bb0d910b2e59e1"
    },
    "metrics": {
        "mobilenet_v3_large-eval_latency": 115.3942605,
        "mobilenet_v2-eval_latency": 99.127155,
        "resnet152-eval_latency": 1115.0839365,
        "hf_Albert-eval_latency": 134.34109999999998,
        "hf_Bert_large-eval_latency": 295.00577799999996,
        "hf_Bart-eval_latency": 149.313368,
        "resnet50-eval_latency": 469.561532,
        "hf_GPT2-eval_latency": 185.68859650000002,
        "hf_Longformer-eval_latency": 215.187826,
        "hf_DistilBert-eval_latency": 72.3893025,
        "dlrm-eval_latency": 21.344289500000002,
        "hf_BigBird-eval_latency": 367.279237,
        "BERT_pytorch-eval_latency": 67.36218,
        "resnet18-eval_latency": 42.107551,
        "hf_T5-eval_latency": 83.166863,
        "alexnet-eval_latency": 170.11994449999997,
        "hf_Reformer-eval_latency": 81.8123215,
        "timm_vision_transformer-eval_latency": 258.6363415,
        "hf_Bert-eval_latency": 118.3291215
    }
}
```
### Measure torch.compile Mode Performance

In PyTorch, `torch.compile` uses Inductor as its default backend. For execution on the cpu, the inductor backend leverages C++/OpenMP to generate highly optimized kernels for your model. Run the following command to collect performance data in `torch.compile` mode for the downloaded models.

```bash
python3 run_benchmark.py cpu --model alexnet,BERT_pytorch,dlrm,hf_Albert,hf_Bart,hf_Bert,hf_Bert_large,hf_BigBird,hf_DistilBert,hf_GPT2,hf_Longformer,hf_Reformer,hf_T5,mobilenet_v2,mobilenet_v3_large,resnet152,resnet18,resnet50,timm_vision_transformer \
--test eval --torchdynamo inductor --metrics="latencies"
```

The results for all the models run will be stored in the `.userbenchmark/cpu/` directory. The `cpu` user benchmark creates a folder `cpu-YYmmddHHMMSS` for the test, and aggregates all test results into a JSON file `metrics-YYmmddHHMMSS.json`.`YYmmddHHMMSS` is the time you started the test. The metrics file show the model inference latency, in milliseconds (msec) for each model you downloaded and ran. The results with `torch.compile` mode should look like:

```output
{
    "name": "cpu",
    "environ": {
        "pytorch_git_version": "2236df1770800ffea5697b11b0bb0d910b2e59e1"
    },
    "metrics": {
        "mobilenet_v3_large-eval_latency": 47.909326,
        "mobilenet_v2-eval_latency": 35.976583,
        "resnet152-eval_latency": 596.8526609999999,
        "hf_Albert-eval_latency": 87.863602,
        "hf_Bert_large-eval_latency": 282.57478649999996,
        "hf_Bart-eval_latency": 137.8793465,
        "resnet50-eval_latency": 245.21206,
        "hf_GPT2-eval_latency": 94.8732555,
        "hf_Longformer-eval_latency": 213.98017049999999,
        "hf_DistilBert-eval_latency": 65.187752,
        "dlrm-eval_latency": 18.2130865,
        "hf_BigBird-eval_latency": 281.18494050000004,
        "BERT_pytorch-eval_latency": 71.429891,
        "resnet18-eval_latency": 30.945619,
        "hf_T5-eval_latency": 124.513945,
        "alexnet-eval_latency": 123.83680100000001,
        "hf_Reformer-eval_latency": 58.992528,
        "timm_vision_transformer-eval_latency": 267.533416,
        "hf_Bert-eval_latency": 102.096192
    }
}
```
You will notice that most of these models achieve a performance improvement in model inference latency when run with the `torch.compile` model using the inductor backend.

You have successfully run the PyTorch Benchmark suite on a variety of different models. You can experiment with the two different execution modes and different optimization settings, check the performance, and choose the right settings for your model and use case.



