---
# User change
title: "Measure ML Inference Performance on Arm servers"

weight: 2

layout: "learningpathall"
 

---


## Prerequisites

* An [Arm based instance](/learning-paths/server-and-cloud/csp/) from an appropriate cloud service provider running `Ubuntu Linux 20.04`.

This learning path has been tested on AWS and Oracle platforms.


## Install necessary software and packages required by MLPerf Inference Suite

Launch an Arm-based instance running `Ubuntu 20.04`.

Install build-essential and Python3 package dependencies

```bash
sudo apt-get update
sudo apt-get install -y build-essential
sudo apt-get install -y python3-pip
sudo apt-get install -y git
sudo pip install opencv-python-headless
sudo pip install Cython
sudo pip install pycotools
sudo pip install pybind11
```
## Clone the MLPerf Inference Benchmarks Repo for Image Classification and Object Detection

We use the MLPerf Inference benchmark suite from MLCommons to benchmark models for a widely used ML use-case such as Image classification and Object detection. 
Start by cloning the repository below.

```bash
git clone --recurse-submodules https://github.com/mlcommons/inference.git mlperf_inference
```

## Build and Install the MLPerf Inference Benchmark

Next, build and install the MLPerf Inference Benchmark for the image classification and object detection use case using the steps below.

```bash
cd mlperf_inference/loadgen/
CFLAGS="-std=c++14" sudo python3 setup.py develop --user
cd ../vision/classification_and_detection/
sudo python3 setup.py develop
```

## Install Tensorflow

MLPerf Inference Benchmark suite can use different backends such as onnx or tensorflow. We will install Tensorflow as the backend. Install tensorflow using the commands below.

```bash
pip install tensorflow
pip install tensorflow-io
```
We set 2 environment variables:
* Enable oneDNN, an open-source cross-platform performance library for deep learning applications
* Use 16-bit floating-point storage format (BF16) to accelerate performance

```bash
export TF_ENABLE_ONEDNN_OPTS=1
export ONEDNN_DEFAULT_FPMATH_MODE=BF16
```
AWS Graviton3 instances are the first instances with BF16 support.

## Download the ML Model 

Next, download the ML model you want to run the benchmark with. In this example, we download the resnet50-v1.5 model.

```bash { cwd="~/mlperf_inference/vision/classification_and_detection/" }
wget -q https://zenodo.org/record/2535873/files/resnet50_v1.pb
```

## Download the dataset 

You will also need to download a dataset for the ML model you want to benchmark. The imagenet2012 validation dataset is best used with this ML model. You can download the dataset after you register on the site [here](http://image-net.org/challenges/LSVRC/2012/)

For this example, we will generate a fake image dataset using the tooling included in the repo. Use the command below

```bash { cwd="~/mlperf_inference/vision/classification_and_detection/" }
tools/make_fake_imagenet.sh
```

## Setup Environment Variables

Finally, before you run the benchmark you will need to setup the environment variables below to point to the location of the ML model and dataset.

```bash
export MODEL_DIR=`pwd`
export DATA_DIR=`pwd`/fake_imagenet
```

## Now run the benchmark on your Arm machine

You can now launch the benchmark on your Arm machine, using the command below. 

```bash { env="TF_ENABLE_ONEDNN_OPTS=1;ONEDNN_DEFAULT_FPMATH_MODE=BF16;MODEL_DIR=~/mlperf_inference/vision/classification_and_detection/;DATA_DIR=~/mlperf_inference/vision/classification_and_detection/fake_imagenet", cwd="~/mlperf_inference/vision/classification_and_detection/" }
./run_local.sh tf resnet50 cpu
```

This command runs the benchmark with the "tf" tensorflow backend on the "resnet50" ML model with the device set to "cpu".

The minimal arguments that you need to pass to the benchmark are shown below

```console
./run_local.sh backend model device

backend is one of [tf|onnxruntime|pytorch|tflite]
model is one of [resnet50|mobilenet|ssd-mobilenet|ssd-resnet34]
device is one of [cpu|gpu]
```

For all other options, run help as shown below

```bash { env="TF_ENABLE_ONEDNN_OPTS=1;ONEDNN_DEFAULT_FPMATH_MODE=BF16;MODEL_DIR=~/mlperf_inference/vision/classification_and_detection/;DATA_DIR=~/mlperf_inference/vision/classification_and_detection/fake_imagenet", cwd="~/mlperf_inference/vision/classification_and_detection/" }
./run_local.sh --help
```

## View Results

At the end of the benchmark run, the aggregated ML performance results are printed on the console. For example, using the command above, the output will be similar to:
```
INFO:main:starting TestScenario.SingleStream
TestScenario.SingleStream qps=13.88, mean=0.0719, time=600.153, queries=8333, tiles=50.0:0.0718,80.0:0.0731,90.0:0.0738,95.0:0.0743,99.0:0.0755,99.9:0.0771

```
Detailed results with breakdowns are available in the `output/tf-cpu/resnet50` folder. The folder name is dependent on the arguments passed to the benchmark script.

