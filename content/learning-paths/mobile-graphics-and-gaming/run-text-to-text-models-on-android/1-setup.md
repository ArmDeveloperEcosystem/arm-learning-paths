---
title: Prepare the Android command-line tools
description: Install and verify the Android command-line tools needed to build and deploy the text-to-text application.
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check the host development tools

You'll use a terminal and a physical Arm-based Android phone. First, you'll build the application with the Gradle wrapper, then use Android Debug Bridge (`adb`) to install and start it on the phone.

The setup commands install the Android SDK. Before you run them, ensure that your development machine has the prerequisite tools installed.

Open a terminal. On Windows, use PowerShell.

Check the installed versions of required tools:

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

Install any missing host tools before continuing. Use JDK 17 for this Learning Path. The starter application pins Android and Kotlin build plugins that are validated with JDK 17. Newer JDK releases aren't validated for this workflow and can fail during Android lint analysis.

If your machine has multiple JDK versions, set `JAVA_HOME` to the JDK 17 installation before continuing. Confirm that both `java -version` and `javac -version` report version 17. See [Java versions in Android builds](https://developer.android.com/build/jdks) for JDK selection options.

{{% notice Note %}}
You can open the cloned project in Android Studio and run it on a connected phone or an Android Virtual Device (AVD). If you use an AVD, select a recent system image compatible with the application's arm64 runtime libraries. An emulator is useful for functional testing, but its performance and memory behavior aren't representative of a physical Arm-based phone.
{{% /notice %}}

## Install the Android command-line tools

Run the following commands to download Google's [Android SDK Command-Line Tools](https://developer.android.com/tools), verify the pinned archive checksum, and place the tools under `ANDROID_HOME`:

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

Continue in the same terminal so that the environment variables remain set. If you use a new terminal, you'll need to set `ANDROID_HOME` to the same directory and add `cmdline-tools/latest/bin` and `platform-tools` to `PATH` again.

## Install and verify the required SDK packages

Review and accept the Android SDK licenses when prompted. After accepting licenses, install Platform-Tools, Android SDK Platform 35, and Build-Tools 35.0.0:

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

The final two checks return no output on macOS or Linux when the directories exist. On Windows, both checks should return `True`.

## What you've accomplished and what's next

You've now installed and verified the Android command-line tools required to build and deploy the application. 

Next, you'll build and run the default application.
