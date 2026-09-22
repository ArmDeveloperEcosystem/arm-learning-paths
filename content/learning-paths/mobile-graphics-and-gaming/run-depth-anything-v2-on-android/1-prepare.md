---
title: Prepare the Android command-line tools
description: Verify the host development tools, then install Android CLI and the required SDK packages.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Arm AI Portal

The [Arm AI Portal](https://developer.arm.com/ai/models) provides a catalog of AI models across different runtimes, use cases, optimization profiles, and Arm-based targets. It includes benchmarking and compatibility information, code examples, and deployment guidance.

You'll use an application called Image Analysis to run Depth Anything V2 Small, a monocular depth-estimation model from the Arm AI Portal, on a physical Arm-based Android phone. The application includes a validated ExecuTorch adapter that prepares the image, runs the model, validates its relative-disparity output, and renders a grayscale depth map.

## Check the existing development tools

Image Analysis builds with Android SDK 35 and Java 17. Before installing anything, display the versions already available on your development computer:

{{< tabpane code=true >}}
  {{< tab header="macOS" language="bash" >}}
git --version
java -version
javac -version
python3 --version
python3 -m pip --version
brew --version
  {{< /tab >}}
  {{< tab header="Linux x86_64" language="bash" >}}
git --version
java -version
javac -version
python3 --version
python3 -m pip --version
curl --version
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
git --version
java -version
javac -version
py --version
py -m pip --version
$PSVersionTable.PSVersion
winget --version
  {{< /tab >}}
{{< /tabpane >}}

You need Git, Python 3 with `pip`, and Java Development Kit (JDK) 17 or later. You also need Homebrew on macOS, `curl` on Linux, or `winget` on Windows to install Android CLI. A `command not found` or `is not recognized` message identifies a host tool you need to install.

Install any missing host prerequisites before continuing, then rerun the version checks. Ensure `java` and `javac` report version 17 or later. The application configures Gradle to provision its JDK 17 build toolchain automatically during the first build.

## Install Android CLI

Install Android CLI for your development computer:

{{< tabpane code=true >}}
  {{< tab header="macOS with Homebrew" language="bash" >}}
brew tap android/tap
brew install android-cli
  {{< /tab >}}
  {{< tab header="Linux x86_64" language="bash" >}}
curl -fsSL https://dl.google.com/android/cli/latest/linux_x86_64/install.sh |
    bash
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
winget install --exact --id Google.AndroidCLI
  {{< /tab >}}
{{< /tabpane >}}

Close and reopen the terminal after installation if the `android` command isn't immediately available. Then update Android CLI and confirm its version:

```console
android update
android -V
```

## Install the Android SDK packages

Set the SDK location, add Platform Tools to `PATH`, and install the packages. Review and accept the Android SDK licenses when prompted.

{{< tabpane code=true >}}
  {{< tab header="macOS" language="bash" >}}
export ANDROID_HOME="$HOME/Library/Android/sdk"
export PATH="$ANDROID_HOME/platform-tools:$PATH"

android --sdk="$ANDROID_HOME" sdk install \
    platform-tools \
    platforms/android-35 \
    build-tools/35.0.0
  {{< /tab >}}
  {{< tab header="Linux" language="bash" >}}
export ANDROID_HOME="$HOME/Android/Sdk"
export PATH="$ANDROID_HOME/platform-tools:$PATH"

android --sdk="$ANDROID_HOME" sdk install \
    platform-tools \
    platforms/android-35 \
    build-tools/35.0.0
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
$env:ANDROID_HOME = "$env:LOCALAPPDATA\Android\Sdk"
$env:Path = "$env:ANDROID_HOME\platform-tools;$env:Path"

android "--sdk=$env:ANDROID_HOME" sdk install `
    platform-tools `
    platforms/android-35 `
    build-tools/35.0.0
  {{< /tab >}}
{{< /tabpane >}}

Verify Android CLI, `adb`, Android SDK Platform 35, and Android SDK Build Tools 35.0.0:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
android -V
android --sdk="$ANDROID_HOME" sdk list \
    'platform-tools|platforms/android-35|build-tools/35.0.0'
adb version
test -d "$ANDROID_HOME/platforms/android-35"
test -d "$ANDROID_HOME/build-tools/35.0.0"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
android -V
android "--sdk=$env:ANDROID_HOME" sdk list `
    'platform-tools|platforms/android-35|build-tools/35.0.0'
adb version
Test-Path "$env:ANDROID_HOME\platforms\android-35"
Test-Path "$env:ANDROID_HOME\build-tools\35.0.0"
  {{< /tab >}}
{{< /tabpane >}}

The final two checks have no output on macOS or Linux when the directories exist. Both checks return `True` on Windows.

## What you've accomplished and what's next

You've verified the host tools and prepared Android CLI, Platform Tools, Android SDK Platform 35, and Android SDK Build Tools 35.0.0. Next, you'll connect an Arm-based Android phone, then build and install Image Analysis.
