---
title: Benchmark the Vision Transformer performance with KleidiAI
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up development environment
In this learning path, you will learn how to build and deploy a Vision Transformer(ViT) chat command line Demo to an Android device using MNN-LLM. You will learn how to build the MNN-LLM with cross-compile and how to run the Qwen model for the Android application.

The first step is to prepare a development environment with the required software:

- Linux ubuntu (20.04 or higher)
- Android NDK (tested with version 28.0.12916984)
- CMake (4.0.0-rc1)
- Python3 (Optional)
- Git

## Build and run command-line demo

Push the Model to device, how to obtain model is mention on last page.
```shell
$ adb shell mkdir /data/local/tmp/models/
$ adb push <path to the model folder> /data/local/tmp/models
``` 

```shell
# Download a ndk file from https://developer.android.com/ndk/downloads/
$ upzip android-ndk-r27d-linux.zip
$ export ANDROID_NDK=./android-ndk-r27d-linux/

$ git clone https://github.com/alibaba/MNN.git
% cd MNN/project/android
$ mkdir build_64 && cd build_64
$ ../build_64.sh "-DMNN_LOW_MEMORY=true -DLLM_SUPPORT_VISION=true -DMNN_KLEIDIAI=true  -DMNN_CPU_WEIGHT_DEQUANT_GEMM=true -DMNN_BUILD_LLM=true -DMNN_SUPPORT_TRANSFORMER_FUSE=true -DMNN_ARM82=true -DMNN_OPENCL=true -DMNN_USE_LOGCAT=true -DMNN_IMGCODECS=true -DMNN_BUILD_OPENCV=true"
$ adb push *so llm_demo tools/cv/*so /data/local/tmp/
```

The Build parameter above ```-DMNN_KLEIDIAI ```is to enable the kleidiAI on the MNN, it can be set to false to disable the KleidiAi.

## Test the performance within/without kleidiAi

Here switch to android adb shell environment.

```shell
$ adb shell
$ cd /data/local/tmp/
$ chmod +x llm_demo
$ export LD_LIBRARY_PATH=./   
# <img>./example.png</img> get your image here
$ echo " <img>./example.png</img>Describe the content of the image." >prompt  
$ ./llm_demo models/Qwen-VL-2B-convert-4bit-per_channel/config.json prompt  
```

Here is an example image: 

![example image](example.png)

If the launch is success, you can see the output

```shell
config path is models/Qwen-VL-2B-convert-4bit-per_channel/config.json
tokenizer_type = 3
prompt file is prompt
The image features a tiger standing in a grassy field, with its front paws raised and its eyes fixed on something or someone behind it. The tiger's stripes are clearly visible against the golden-brown background of the grass. The tiger appears to be alert and ready for action, possibly indicating a moment of tension or anticipation in the scene.

#################################
prompt tokens num = 243
decode tokens num = 70
 vision time = 5.96 s
  audio time = 0.00 s
prefill time = 1.80 s
 decode time = 2.09 s
prefill speed = 135.29 tok/s
 decode speed = 33.53 tok/s
##################################
```

Here is my performance comparation within/without kleidiAI

| | KleidiAI OFF | KleidiAi ON |
|----------|----------|----------|
| Vision Process Time | 5.45s | 5.43 s |
| Prefill Speed | 132.35 tok/s | 148.30 tok/s |
| Decode Speed |  21.61 tok/s | 33.26 tok/s |