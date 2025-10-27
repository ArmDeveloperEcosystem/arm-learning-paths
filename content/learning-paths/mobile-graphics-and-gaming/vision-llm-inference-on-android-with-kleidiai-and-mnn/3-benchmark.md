---
title: Build the MNN Command-line ViT Demo
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Prepare an Example Image

In this section, you'll benchmark model performance with and without KleidiAI kernels. To run optimized inference, you'll first need to compile the required library files. You'll also need an example image to run command-line prompts. 

You can use the provided image of the tiger below that this Learning Path uses, or choose your own. 

Whichever you select, rename the image to `example.png` to use the commands in the following sections.

![example image](example.png)

Use ADB to load the image onto your phone:

```bash
adb push example.png /data/local/tmp/
```

## Build Binaries for Command-line Inference

Run the following commands to clone the MNN repository and checkout the source tree:

```bash
cd $HOME
git clone https://github.com/alibaba/MNN.git
cd MNN
git checkout fa3b2161a9b38ac1e7dc46bb20259bd5eb240031
```

Create a build directory and run the build script. 

The first time that you do this, build the binaries with the `-DMNN_KLEIDIAI` flag set to `FALSE`.

```bash
cd $HOME/MNN/project/android
mkdir build_64 && cd build_64

../build_64.sh "-DMNN_BUILD_LLM=true -DMNN_BUILD_LLM_OMNI=ON -DLLM_SUPPORT_VISION=true \
-DMNN_BUILD_OPENCV=true -DMNN_IMGCODECS=true -DMNN_LOW_MEMORY=true \
-DMNN_CPU_WEIGHT_DEQUANT_GEMM=true -DMNN_BUILD_LLM=true -DMNN_SUPPORT_TRANSFORMER_FUSE=true"
```
{{% notice Note %}}
If your NDK toolchain isn't set up correctly, you might run into issues with the above script. Make a note of where the NDK was installed - this will be a directory named after the version you downloaded earlier. Try exporting the following environment variables before re-running `build_64.sh`:

```bash
export ANDROID_NDK_HOME=<path-to>/ndk/28.0.12916984

export CMAKE_TOOLCHAIN_FILE=$ANDROID_NDK_HOME/build/cmake/android.toolchain.cmake
export ANDROID_NDK=$ANDROID_NDK_HOME
```
{{% /notice %}}

## Push Files and Run Inference via ADB

Push the required files to your Android device, then enter a shell on the device using ADB:

```bash
adb push *so llm_demo tools/cv/*so /data/local/tmp/
adb shell
```

Run the following commands in the ADB shell. Navigate to the directory you pushed the files to, add executable permissions to the `llm_demo` file and export an environment variable for it to run properly. After this, use the example image you transferred earlier to create a file containing the text content for the prompt.

```bash
cd /data/local/tmp/
chmod +x llm_demo
export LD_LIBRARY_PATH=$PWD
echo "<img>./example.png</img>Describe the content of the image." > prompt
```

Finally, run an inference on the model with the following command:

```bash
./llm_demo models/Qwen2.5-VL-3B-Instruct-MNN/config.json prompt
```

If the launch is successful, you should see the following output, with the performance benchmark at the end:

```output
config path is models/Qwen-VL-2B-convert-4bit-per_channel/config.json
tokenizer_type = 3
prompt file is prompt
The image features a tiger standing in a grassy field, with its front paws raised and its eyes fixed on something or someone behind it. The tiger's stripes are clearly visible against the golden-brown background of the grass. The tiger appears to be alert and ready for action, possibly indicating a moment of tension or anticipation in the scene.

#################################
prompt tokens num = 243
decode tokens num = 70
 vision time = 5.76 s
  audio time = 0.00 s
prefill time = 1.26 s
 decode time = 2.02 s
prefill speed = 192.28 tok/s
 decode speed = 34.73 tok/s
##################################
```

## Enable KleidiAI and Re-run Inference

The next step is to re-generate the binaries with KleidiAI activated. This is done by inserting a hint into the code. 

From the `MNN` directory, run:
```bash
sed -i '/void Llm::setRuntimeHint(std::shared_ptr<Express::Executor::RuntimeManager> &rtg) {/a\
    rtg->setHint(MNN::Interpreter::CPU_ENABLE_KLEIDIAI, 1);' transformers/llm/engine/src/llm.cpp
```

From the `build_64` directory, run:
```bash
../build_64.sh "-DMNN_BUILD_LLM=true -DMNN_BUILD_LLM_OMNI=ON -DLLM_SUPPORT_VISION=true \
-DMNN_BUILD_OPENCV=true -DMNN_IMGCODECS=true -DMNN_LOW_MEMORY=true \
-DMNN_CPU_WEIGHT_DEQUANT_GEMM=true -DMNN_BUILD_LLM=true -DMNN_SUPPORT_TRANSFORMER_FUSE=true"
```
## Update Files on the Device

First, remove existing binaries from your Android device, then push the updated files:

```bash
adb shell "cd /data/local/tmp; rm -rf *so llm_demo tools/cv/*so"
adb push *so llm_demo tools/cv/*so /data/local/tmp/
adb shell
```

With the new ADB shell, run the following commands:

```bash
cd /data/local/tmp/
chmod +x llm_demo
export LD_LIBRARY_PATH=$PWD
./llm_demo models/Qwen2.5-VL-3B-Instruct-MNN/config.json prompt
```
## Benchmark Results

After running with KleidiAI enabled, you should see improved benchmarks. Example results:

```output
#################################
prompt tokens num = 243
decode tokens num = 70
 vision time = 2.91 s
  audio time = 0.00 s
prefill time = 0.91 s
 decode time = 1.56 s
prefill speed = 266.13 tok/s
 decode speed = 44.96 tok/s
##################################
```

This time, you should see an improvement in the benchmark. Below is an example table showing the uplift on three relevant metrics after enabling the KleidiAI kernels:

| Benchmark           | Without KleidiAI | With KleidiAI |
|---------------------|------------------|---------------|
| Vision Process Time | 5.76 s           | 2.91 s        |
| Prefill Speed       | 192.28 tok/s     | 266.13 tok/s  |
| Decode Speed        | 34.73 tok/s      | 44.96 tok/s   |

**Prefill speed** describes how fast the model processes the input prompt. 

**Decode Speed** indicates how quickly the model generates new tokens after the input is processed.

These benchmarks clearly demonstrate the performance advantages of using Arm-optimized KleidiAI kernels for vision transformer (ViT) workloads.