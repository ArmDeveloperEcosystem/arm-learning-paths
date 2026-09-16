---
title: Prepare and connect an Arm-based Android phone
description: Verify the Android build tools, enable USB debugging, and confirm that an Arm-based Android phone is authorized.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check the existing development tools

The sample application builds with Android SDK 35 and Java 17. Before installing anything, display the versions already available on your development computer:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
git --version
java -version
javac -version
python3 --version
python3 -m pip --version
curl --version
android -V
android info
android sdk list 'platform-tools|platforms/android-35|build-tools/35.0.0'
adb version
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
git --version
java -version
javac -version
py --version
py -m pip --version
$PSVersionTable.PSVersion
android -V
android info
android sdk list 'platform-tools|platforms/android-35|build-tools/35.0.0'
adb version
  {{< /tab >}}
{{< /tabpane >}}

You need Git, Python 3 with `pip`, Java Development Kit (JDK) 17 or later, and `curl`. You also need Android CLI, Android Debug Bridge (`adb`), Platform Tools, Android SDK Platform 35, and Android SDK Build Tools 35.0.0. A `command not found` or `is not recognized` message identifies a tool you need to install. In the Android SDK package listing, verify that all three packages are marked as installed.

## Optional: install or update the host tools

Skip this section when the version checks meet the requirements. If a host tool is missing or Java is older than version 17, install or update the prerequisites for your development computer:

{{< tabpane code=true >}}
  {{< tab header="macOS with Homebrew" language="bash" >}}
brew install git python openjdk@17
export PATH="$(brew --prefix openjdk@17)/bin:$PATH"
  {{< /tab >}}
  {{< tab header="Ubuntu or Debian" language="bash" >}}
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip openjdk-17-jdk curl
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
winget install --exact --id Git.Git
winget install --exact --id Python.Python.3.13
winget install --exact --id Microsoft.OpenJDK.17
  {{< /tab >}}
{{< /tabpane >}}

On macOS, install [Homebrew](https://brew.sh/) first if the `brew` command isn't available. On another Linux distribution, install equivalent packages with its package manager. Restart PowerShell after a Windows installation so the updated `PATH` is available.

Run the version checks again. Ensure `java` and `javac` report version 17 or later.

## Optional: install or update Android CLI

Google has deprecated `sdkmanager` in favor of [Android CLI](https://developer.android.com/tools/agents/android-cli). Skip this section when `android -V` already reports a version. Otherwise, install Android CLI for your development computer:

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

## Optional: install or update the Android SDK packages

Skip this section when the package listing marks all three required packages as installed. Otherwise, set the SDK location, add Platform Tools to `PATH`, and install the packages. Review and accept the Android SDK licenses when prompted.

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

## Connect the phone

Enable **Developer options** and **USB debugging** on the Arm-based Android phone. Connect it with a data-capable USB cable, unlock it, and accept the debugging authorization prompt.

Verify the connection and architecture:

```console
adb devices -l
adb shell getprop ro.product.cpu.abi
```

The first command lists the phone as `device`. The second command returns `arm64-v8a`.

If the phone is `unauthorized`, unlock it and accept the prompt. On Windows, you might also need the manufacturer's USB driver.

### What you've accomplished

You've verified the build tools and connected an authorized Arm-based Android phone. Next, you'll build and install the sample application.
