---
title: Setup
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up the host tools

Use the command for your host operating system to set `ANDROID_HOME` to your Android SDK directory. Update the default path to match the actual SDK and tools installation location on your system.

{{< tabpane-normal >}}
{{< tab header="MacOS" >}}
```bash
export ANDROID_HOME="$HOME/Library/Android/sdk"
export PATH="$ANDROID_HOME/platform-tools:$ANDROID_HOME/cmdline-tools/latest/bin:$PATH"
```
{{< /tab >}}
{{< tab header="Linux x86" >}}
```bash
export ANDROID_HOME="$HOME/Android/Sdk"
export PATH="$ANDROID_HOME/platform-tools:$ANDROID_HOME/cmdline-tools/latest/bin:$PATH"
```
{{< /tab >}}
{{< /tabpane-normal >}}

Install the Android NDK and Platform-Tools using your existing Android CLI and set the `ANDROID_NDK_HOME` environment variable which is required at a later step:

```bash
android --sdk="$ANDROID_HOME" sdk install platform-tools ndk/30.0.16248370
export ANDROID_NDK_HOME="$ANDROID_HOME/ndk/30.0.16248370"
```

{{% notice Please Note %}}
This guide uses NDK r30 (`30.0.16248370`), the [2026 LTS release](https://github.com/android/ndk/wiki). Other NDK versions have not been tested with this guide but are expected to work.
{{%/ notice %}}



Install Bazelisk using the commands for your host operating system. On macOS, [install Homebrew](https://brew.sh/) first if it is not already available.

{{< tabpane >}}
{{< tab header="MacOS" >}}
brew install bazelisk
{{< /tab >}}
{{< tab header="Linux x86" >}}

curl -fL -o bazelisk https://github.com/bazelbuild/bazelisk/releases/latest/download/bazelisk-linux-amd64
mkdir -p "$HOME/.local/bin"
install -m 755 bazelisk "$HOME/.local/bin/bazel"
echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
source "$HOME/.bashrc"
bazel --version

{{< /tab >}}
{{< /tabpane >}}


## Check your Android device

Connect one Android device and authorize debugging from your host computer. Check the ADB connection, GPU model, and driver:

```bash
adb devices
adb shell 'dumpsys SurfaceFlinger | grep GLES'
```

The output should resemble the example below, showing the connected device and its GPU. ML Drift supports different OpenCL backends, but profiling with Arm Streamline requires a device with a Mali GPU.

```output
10.1.16.154:5555        device

 ------------RE GLES (Ganesh)------------
GLES: ARM, Mali-G1-Ultra MC12, OpenGL ES 3.2 v1.r54p1-11eac0.5ac4efe.15f36b8c6518df15cadf5aced2a1638a.1c3d0d1d631f33b0b8a673ce08c68e340f851541
```

## Get the source

Clone ML Drift and enter the repository directory using the commands for your host operating system. The macOS commands also select the revision used for the validated Android build:

```bash
git clone https://github.com/google-ai-edge/ml-drift.git
cd ml-drift
```

Your environment is ready. Next, build and run the sample.