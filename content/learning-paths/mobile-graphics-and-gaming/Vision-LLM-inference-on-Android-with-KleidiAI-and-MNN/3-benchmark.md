---
title: Build the MNN Command-line ViT Demo
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section, you will use the model to benchmark performance with and without KleidiAI kernels. You will need to compile library files to run the optimized inference.

## Prepare an example image

You will use an image to run a command-line prompt. In this learning path, the tiger below will be used as an example. You can save this image or provide one of your own. Re-name the image to `example.png` in order to use the commands in the following sections.

![example image](example.png)

Use adb to load the image onto your phone:

```bash
adb push example.png /data/local/tmp/
```

## Build binaries for command-line inference

Navigate to the MNN project you cloned in the previous section. Create a build directory and run the script. The first time, you will build the binaries with the `-DMNN_KLEIDIAI` flag set to `FALSE`.

```bash
cd $HOME/MNN/project/android
mkdir build_64 && cd build_64

../build_64.sh "-DMNN_LOW_MEMORY=true -DLLM_SUPPORT_VISION=true -DMNN_KLEIDIAI=FALSE  \
  -DMNN_CPU_WEIGHT_DEQUANT_GEMM=true -DMNN_BUILD_LLM=true \
  -DMNN_SUPPORT_TRANSFORMER_FUSE=true -DMNN_ARM82=true -DMNN_OPENCL=true \
  -DMNN_USE_LOGCAT=true -DMNN_IMGCODECS=true -DMNN_BUILD_OPENCV=true"
```
{{% notice Note %}}
If your NDK toolchain isn't set up correctly, you may run into issues with the above script. Make note of where the NDK was installed - this will be a directory named after the version you downloaded earlier. Try exporting the following environment variables before re-running `build_64.sh`.

```bash
export ANDROID_NDK_HOME=<path-to>/ndk/25.2.9519653

export CMAKE_TOOLCHAIN_FILE=$ANDROID_NDK_HOME/build/cmake/android.toolchain.cmake
export ANDROID_NDK=$ANDROID_NDK_HOME
```
{{% /notice %}}

Push the files to your mobile device. Then, enter a shell on the phone using ADB.

```bash
adb push *so llm_demo tools/cv/*so /data/local/tmp/
adb shell
```

The following commands should be run in the ADB shell. Navigate to the directory you pushed the files to, add executable permissions to the `llm_demo` file and export an environment variable for it to run properly. After this, use the example image you transferred earlier to create a file containing the text content for the prompt.

```bash
cd /data/local/tmp/
chmod +x llm_demo
export LD_LIBRARY_PATH=$PWD
echo "<img>./example.png</img>Describe the content of the image." > prompt
```

Finally, run an inference on the model with the following command.

```bash
./llm_demo models/Qwen-VL-2B-convert-4bit-per_channel/config.json prompt
```

If the launch is successful, you should see the following output, with the performance benchmark at the end.

```output
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

## Enable KleidiAI and re-run inference

The next step is to re-generate the binaries with KleidiAI activated. This is done by updating the flag `-DMNN_KLEIDIAI` to `TRUE`. From the `build_64` directory, run:
```bash
../build_64.sh "-DMNN_LOW_MEMORY=true -DLLM_SUPPORT_VISION=true -DMNN_KLEIDIAI=TRUE \
-DMNN_CPU_WEIGHT_DEQUANT_GEMM=true -DMNN_BUILD_LLM=true \
-DMNN_SUPPORT_TRANSFORMER_FUSE=true -DMNN_ARM82=true -DMNN_OPENCL=true \
-DMNN_USE_LOGCAT=true -DMNN_IMGCODECS=true -DMNN_BUILD_OPENCV=true"
```

The next step is to update the files on your phone. Start by removing the ones used in the previous step. Then, push the new ones with the same command as before.

```bash
adb shell "cd /data/local/tmp; rm -rf *so llm_demo tools/cv/*so"
adb push *so llm_demo tools/cv/*so /data/local/tmp/
adb shell
```

In the new ADB shell, preform the same steps as in the previous section.

```bash
cd /data/local/tmp/
chmod +x llm_demo
export LD_LIBRARY_PATH=$PWD
./llm_demo models/Qwen-VL-2B-convert-4bit-per_channel/config.json prompt
```

This time, you should see an improvement in the benchmark. Below is an example table showing the uplift on three relevant metrics after enabling the KleidiAI kernels.

| Benchmark           | Without KleidiAI | With KleidiAI |
|---------------------|------------------|---------------|
| Vision Process Time | 5.45s            | 5.43 s        |
| Prefill Speed       | 132.35 tok/s     | 148.30 tok/s  |
| Decode Speed        | 21.61 tok/s      | 33.26 tok/s   |

The prefill speed describes how fast the model processes the input prompt. The decode speed corresponds to the rate at which the model generates new tokens one at a time after the input is processed

This shows the advantages of using Arm optimized kernels for your ViT use-cases.