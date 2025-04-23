---
title: Build the MNN Android Demo with GUI
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Install Required Software

In this section, you'll set up your development environment by installing dependencies and preparing the Qwen vision model.

Install the Android NDK (Native Development Kit) and git-lfs. This Learning Path was tested with NDK version `28.0.12916984` and CMake version `4.0.0-rc1`.

For Ubuntu or Debian systems, install CMake and git-lfs with the following commands:

```bash
sudo apt update
sudo apt install cmake git-lfs -y
```

You can use Android Studio to obtain the NDK. 

Click **Tools > SDK Manager** and navigate to the **SDK Tools** tab. 

Select the **NDK (Side by side)** and **CMake** checkboxes, as shown below:

![Install NDK](./install_ndk.png)

See [Install NDK and CMake](https://developer.android.com/studio/projects/install-ndk) for other installation methods.

Ensure that Python and pip are installed by verifying the version with these commands:

```bash
python --version
pip --version
```

You see the versions printed:

```output
Python 3.12.3
pip 24.0 from /usr/lib/python3/dist-packages/pip (python 3.12)
```

{{% notice Note %}}
If Python 3.x is not the default version, try running `python3 --version` and `pip3 --version`.
{{% /notice %}}

## Set up Phone Connection

You need to set up an authorized connection with your phone. The Android SDK Platform Tools package, included with Android Studio, provides Android Debug Bridge (ADB) for transferring files. 

Connect your phone to your computer using a USB cable, and enable USB debugging on your phone. To do this, tap the **Build Number** in your **Settings** app 7 times, then enable **USB debugging** in **Developer Options**.

Verify the connection by running:

```console
adb devices
```

If your device is connected you see it listed with your device id:

```output
List of devices attached
<DEVICE ID>     device
```

## Download and Convert the Model

The following commands download the model from Hugging Face, and clone a tool for exporting the LLM model to the MNN framework.

```bash
cd $HOME
pip install -U huggingface_hub
huggingface-cli download Qwen/Qwen2-VL-2B-Instruct --local-dir ./Qwen2-VL-2B-Instruct/
git clone https://github.com/wangzhaode/llm-export
cd llm-export && pip install .
```
Use the `llm-export` repository to quantize the model with these options:

```bash
llmexport --path ../Qwen2-VL-2B-Instruct/ --export mnn --quant_bit 4 \
    --quant_block 0 --dst_path Qwen2-VL-2B-Instruct-convert-4bit-per_channel --sym
```

The table below gives you an explanation of the different arguments:

| Parameter        | Description | Explanation |
|------------------|-------------|--------------|
| `--quant_bit` | MNN quant bit, 4 or 8, default is 4. | `4` represents q4 quantization. |
| `--quant_block` | MNN quant block, default is 0. | `0` represents per-channel quantization; `128` represents 128 per-block quantization. |
| `--sym` | Symmetric quantization (without zeropoint); default is False. | The quantization parameter that enables symmetrical quantization. |

To learn more about the parameters, see the [transformers README.md](https://github.com/alibaba/MNN/tree/master/transformers).

Verify that the model was built correctly by checking that the `Qwen2-VL-2B-Instruct-convert-4bit-per_channel` directory is at least 1 GB in size.

Push the model onto the device:

```shell
adb shell mkdir /data/local/tmp/models/
adb push Qwen2-VL-2B-Instruct-convert-4bit-per_channel /data/local/tmp/models
```

With the model set up, you're ready to use Android Studio to build and run an example application.
