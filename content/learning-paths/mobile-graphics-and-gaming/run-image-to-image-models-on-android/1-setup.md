---
title: Prepare the Android command-line tools
description: Install and verify the Android command-line tools needed to build and deploy the image-segmentation application.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Arm AI Portal

The [Arm AI Portal](https://developer.arm.com/ai/models) provides a catalog of AI models across different runtimes, use cases, optimization profiles, and Arm-based targets. It includes benchmarking and compatibility information, code examples, and deployment guidance.

You'll use an Android example application to run MobileSAM, an image-segmentation model from the Arm AI Portal, on a physical Arm-based Android phone. MobileSAM receives an image and a box prompt, then returns masks that identify an object inside the box.

The application includes one validated model adapter for MobileSAM with ExecuTorch. An adapter is application code that does the following:

- Validates the model package
- Prepares the image and prompt tensors
- Calls the runtime
- Decodes the output masks
- Converts the selected mask into a visual overlay

## Check the host development tools

You'll use a terminal and a physical Arm-based Android phone. First, you'll build the application with the Gradle wrapper, then use Android Debug Bridge (`adb`) to install and start it on the phone.

Open a terminal. On Windows, use PowerShell.

Check the installed tools:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
git --version
java -version
javac -version
python3 --version
python3 -m pip --version
curl --version
unzip -v
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
git --version
java -version
javac -version
python --version
python -m pip --version
$PSVersionTable.PSVersion
  {{< /tab >}}
{{< /tabpane >}}

Install any missing tools before continuing. Ensure the Java compiler version is 17 or later.

{{% notice Note %}}
You can open the cloned project in Android Studio and run it on a connected phone or an Android Virtual Device (AVD). For an AVD, select a recent system image compatible with the application's `arm64-v8a` native libraries. An emulator is useful for functional testing, but its performance and memory behavior aren't representative of a physical Arm-based phone.
{{% /notice %}}

## Install the Android command-line tools

The following commands download Google's [Android SDK Command-Line Tools](https://developer.android.com/tools), verify the pinned archive checksum, and place the tools under `ANDROID_HOME`:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
if [ -z "${ANDROID_HOME:-}" ]; then
    case "$(uname -s)" in
        Darwin) export ANDROID_HOME="$HOME/Library/Android/sdk" ;;
        Linux) export ANDROID_HOME="$HOME/Android/Sdk" ;;
        *) printf 'Unsupported operating system.\n' >&2; false ;;
    esac
fi

case "$(uname -s)-$(uname -m)" in
    Darwin-arm64)
        android_cli_archive="commandlinetools-mac_arm64-15859902_latest.zip"
        android_cli_sha256="835b62a26162b229b441d1f6d4680383815a270809eb33522c0d480fa5002c4e"
        ;;
    Darwin-x86_64)
        android_cli_archive="commandlinetools-mac_x86_64-15859902_latest.zip"
        android_cli_sha256="c5a6378ab5cf7e0d5701921405115befff13e9ff7417fb588389338f8bd050f3"
        ;;
    Linux-*)
        android_cli_archive="commandlinetools-linux-15859902_latest.zip"
        android_cli_sha256="4e4c464f145a7512b57d088ac6c278c03c9eea610886b35a5e0804e74eedf583"
        ;;
    *) printf 'No Android command-line archive is configured for this computer.\n' >&2; false ;;
esac

android_cli_temp="$(mktemp -d)"
curl --fail --location \
    "https://dl.google.com/android/repository/$android_cli_archive" \
    --output "$android_cli_temp/$android_cli_archive"

if command -v sha256sum >/dev/null 2>&1; then
    printf '%s  %s\n' "$android_cli_sha256" "$android_cli_temp/$android_cli_archive" |
        sha256sum --check
else
    printf '%s  %s\n' "$android_cli_sha256" "$android_cli_temp/$android_cli_archive" |
        shasum -a 256 -c
fi

unzip -q "$android_cli_temp/$android_cli_archive" -d "$android_cli_temp"
mkdir -p "$ANDROID_HOME/cmdline-tools/latest"
cp -R "$android_cli_temp/cmdline-tools/." "$ANDROID_HOME/cmdline-tools/latest/"

export PATH="$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$PATH"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
if (-not $env:ANDROID_HOME) {
    $env:ANDROID_HOME = "$env:LOCALAPPDATA\Android\Sdk"
}

$androidCliArchive = "commandlinetools-win-15859902_latest.zip"
$androidCliSha256 = "90ae805d20434428bffcb699c290860f19bb5f66a67e6b330067e3de801fb04a"
$androidCliTemp = Join-Path $env:TEMP "android-cli-$([guid]::NewGuid())"
$androidCliZip = Join-Path $androidCliTemp $androidCliArchive

New-Item -ItemType Directory -Path $androidCliTemp | Out-Null
Invoke-WebRequest `
    -Uri "https://dl.google.com/android/repository/$androidCliArchive" `
    -OutFile $androidCliZip

$downloadedSha256 = (Get-FileHash $androidCliZip -Algorithm SHA256).Hash
if ($downloadedSha256 -ne $androidCliSha256) {
    throw "Android command-line tools checksum verification failed."
}

Expand-Archive -Path $androidCliZip -DestinationPath $androidCliTemp
$latestTools = Join-Path $env:ANDROID_HOME "cmdline-tools\latest"
New-Item -ItemType Directory -Force -Path $latestTools | Out-Null
Copy-Item -Path "$androidCliTemp\cmdline-tools\*" `
    -Destination $latestTools -Recurse -Force

$env:Path = "$latestTools\bin;$env:ANDROID_HOME\platform-tools;$env:Path"
  {{< /tab >}}
{{< /tabpane >}}

If you already have an SDK in `ANDROID_HOME`, the commands reuse that location.

Continue in the same terminal so that the environment variables remain set.

## Install the required SDK packages

Review and accept the Android SDK licenses when prompted. After accepting licenses, install and verify the required packages:

{{< tabpane code=true >}}
  {{< tab header="macOS or Linux" language="bash" >}}
sdkmanager --sdk_root="$ANDROID_HOME" --licenses
sdkmanager --sdk_root="$ANDROID_HOME" \
    "platform-tools" \
    "platforms;android-35" \
    "build-tools;35.0.0"

sdkmanager --version
adb version
test -d "$ANDROID_HOME/platforms/android-35"
test -d "$ANDROID_HOME/build-tools/35.0.0"
  {{< /tab >}}
  {{< tab header="Windows PowerShell" language="powershell" >}}
sdkmanager.bat "--sdk_root=$env:ANDROID_HOME" --licenses
sdkmanager.bat "--sdk_root=$env:ANDROID_HOME" `
    "platform-tools" `
    "platforms;android-35" `
    "build-tools;35.0.0"

sdkmanager.bat --version
adb version
Test-Path "$env:ANDROID_HOME\platforms\android-35"
Test-Path "$env:ANDROID_HOME\build-tools\35.0.0"
  {{< /tab >}}
{{< /tabpane >}}

## What you've accomplished and what's next

You've installed and verified the Android command-line tools needed to build and deploy the application. 

Next, you'll build and install the application on your Android phone.
