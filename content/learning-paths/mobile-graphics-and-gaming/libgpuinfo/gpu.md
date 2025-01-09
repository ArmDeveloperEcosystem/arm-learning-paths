---
# User change
title: "Build and run an example application to obtain Arm GPU configuration information"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

You may want to adjust application settings at runtime to deliver the best performance from device hardware. Querying the hardware configuration is the first step in making decisions which take advantage of available hardware features.

[libGPUInfo](https://github.com/ARM-software/libGPUInfo) is a C++ library which can be integrated into applications to easily gather information about Arm GPU hardware.

You can build an example application and run it on an Android device with an Arm GPU to read the hardware configuration information. This information identifies available features and performance levels.

## Download and install the Android NDK

The libGPUInfo library and example application is written in C++. You can build it with the Android NDK (Native Development Kit).

You can install the Android NDK on an `x86_64` Ubuntu or Debian machine using:

```console
sudo apt update
sudo apt install cmake google-android-ndk-installer -y
```

There are other ways to install the Android NDK and additional operating systems you can use. Refer to [NDK Downloads](https://developer.android.com/ndk/downloads) and [Install NDK and CMake](https://developer.android.com/studio/projects/install-ndk) for more options.

## Build the library and application

Retrieve the software using the `git` command below and change to the repository directory:

```console
git clone https://github.com/ARM-software/libGPUInfo.git
cd libGPUInfo
```

Set the Android NDK environment variable to the location where the NDK is installed:

```console
export ANDROID_NDK_HOME=/usr/lib/android-ndk
```

Build the application by running the script:

```console
bash ./android_build.sh
```

The `android_build.sh` script recognizes `Release` and `Debug` as arguments. The default is `Release` if no argument is supplied. Add `Debug` as a command line argument if you want to build a debug version.

Confirm the file exists using:

```console
ls bin/arm_gpuinfo
```

If there are no build errors and the file name is printed, the application is ready to use. 

## Run the example application on an Android device

To run the application on an Android device you need a computer with `adb` (Android Debug Bridge) installed. 

You can connect to the Android device using USB or Wi-Fi. You can use `adb` to copy `arm_gpuinfo` from your computer to the Android device.

If the computer you will use for `adb` is not the same one you used to build the application, you can copy the `arm_gpuinfo` application from the build computer to the `adb` computer. 

1. Install `adb` from Android Platform Tools

To install `adb` on Ubuntu or Debian run:

```console
sudo apt-get install android-sdk-platform-tools -y
```

{{% notice Note %}}
Android Platform Tools can be installed on `aarch64` Linux. The Android NDK requires `x86_64`, but Android Platform Tools supports Arm.
{{% /notice %}}

Refer to the [SDK Platform Tools release notes](https://developer.android.com/tools/releases/platform-tools) for installation information about other operating systems. 

2. Enable developer options

To enable debugging and other developer options visit the device settings on your Android device, find the Build Number under `About phone` or `About tablet`, and tap the `Build number` 7 times until you see a message `You are a developer!`

A new menu for `Developer options` is now visible and you can enable `USB debugging` and `Wireless debugging`. 

The instructions below use USB debugging. For more information about wireless debugging refer to the [ADB developer documentation](https://developer.android.com/tools/adb). You will use the `adb pair` command and a PIN to connect to the Android device over Wi-Fi.

3. Connect to Android 

Connect a USB cable between your computer with `adb` installed and the Android device. A prompt saying `Allow USB Debugging?` may appear on your device. If so, press `OK`.

Run the `devices` command:
```console
adb devices
```

If the Android device is found it will be listed with an ID number. The output will be similar to:

```output
List of devices attached
00000027A00013  device
```

If no devices are listed, there is something wrong with the connection between your computer and the Android device.

4. Copy the application to the Android device:

You are now ready to copy the application to the Android device and run it. 

Use `adb push` to copy the file to the device and give it execute permission:

```console
adb push ./bin/arm_gpuinfo /data/local/tmp
adb shell chmod u+x /data/local/tmp/arm_gpuinfo
```

Run the application:

```console
adb shell /data/local/tmp/arm_gpuinfo
```

The output will be similar to:

```output
Device configuration
  - Manufacturer: Khadas
  - Model: Edge2
  - Android version: 12
  - Kernel version: 5.10.110

GPU configuration
  - Name: Mali-G610
  - Architecture: Valhall
  - Model number: 0xa007
  - Core count: 4
  - L2 cache count: 4
  - Total L2 cache size: 1048576 bytes
  - Bus width: 128 bits

Per-core statistics
  - Engine count: 2
  - FP32 FMAs: 64/cy
  - FP16 FMAs: 128/cy
  - Texels: 8/cy
  - Pixels: 4/cy

Per-GPU statistics
  - FP32 FMAs: 256/cy
  - FP16 FMAs: 512/cy
  - Texels: 32/cy
  - Pixels: 16/cy

```

The configuration details will vary based on the Arm GPU and Android device you are using. The output above is from the [Khadas Edge 2](https://www.khadas.com/edge2) single-board computer running Android 12. It includes a 4-core Mali-G610 GPU. 

You have learned how to build and run a program to retrieve the hardware configuration details for Arm Mali and Immortalis GPUs.

