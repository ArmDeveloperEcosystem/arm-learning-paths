---
title: How to run the code examples
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How to run the code examples

This Learning Path assumes you are already familiar with the Vulkan API and have an application that uses it to create and render images on Android. If that is the case, you may skip this step.

Otherwise, you may use a test application like those provided by the [Khronos Vulkan Samples repository](https://github.com/KhronosGroup/Vulkan-Samples).

{{% notice Note %}}
You do not need to create a new Vulkan Sample to complete this Learning Path but you can familiarize yourself with the code examples and save them as a reference.
The Vulkan Sample provided in the previous step allows you to experiment with AFRC without any coding required.
{{% /notice %}}

### Build Khronos' Vulkan Samples

[Download](https://github.com/KhronosGroup/Vulkan-Samples?tab=readme-ov-file#setup) the repository:

```bash
git clone --recurse-submodules https://github.com/KhronosGroup/Vulkan-Samples.git
cd vulkan-samples
python ./scripts/generate.py android
```

And follow the build instructions to run the example applications on an Android device.

{{% notice  %}}
You can use [Android Studio](https://github.com/KhronosGroup/Vulkan-Samples/blob/main/docs/build.adoc#build-with-android-studio) to build and run the samples (the build instructions explain how to do this).
{{% /notice %}}

### Create a test sample

If you are coding an example, rather than following along with the existing [Image Compression Control](https://github.com/KhronosGroup/Vulkan-Samples/blob/main/samples/performance/image_compression_control/README.adoc) sample, we need to first create a test sample.
We can use the default [API sample template](https://github.com/KhronosGroup/Vulkan-Samples/blob/main/scripts/README.adoc#generate-api-sample) to write and run the code snippets presented in this Learning Path.

To create a new sample:

```bash
python ./scripts/generate.py sample_api --name afrc --category extensions
```

The necessary files will have been created in `samples/extensions/afrc/`.

### View the sample logs

The screen output will not be relevant for the code we will write in this Learning Path.
Instead, we will be focusing on the output of Android's logcat, which can be printed using the [Android Debug bridge (adb)](https://developer.android.com/studio/command-line/adb) included in the [Android SDK Platform tools](https://developer.android.com/studio/releases/platform-tools.html):

```bash
# Clear the log and stop the sample if it is already running
adb logcat -c
adb shell am force-stop com.khronos.vulkan_samples

# Start the sample
adb shell am start --esa cmd "sample,afrc" com.khronos.vulkan_samples/com.khronos.vulkan_samples.SampleLauncherActivity

# Filter logcat to show sample messages only
adb logcat -s VulkanSamples
```

The output should start with:
```output
I VulkanSamples: [info] Logger initialized
I VulkanSamples: [info] Waiting on window surface to be ready
I VulkanSamples: [info] ContentRectChanged: 0xb4000079e82e6cd0
I VulkanSamples:
I VulkanSamples: [info] Initializing Vulkan sample
```

### Modify the sample

The code snippets shown so far can be added anywhere within the `afrc::prepare_pipelines()` function in the `afrc.cpp` file.

To add a log, use the `LOGI`, `LOGW` and `LOGE` functions, for example:

```C
void afrc::prepare_pipelines()
{
	LOGI("Hello world!");

    ...
}
```

This will result in the following line being added to logcat:

```output
I VulkanSamples: [info] Hello world!
```
