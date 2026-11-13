---
title: Set up Google Developer Device Platform
description: Install the local tools and configure a Google Cloud project and credentials for a Google Developer Device Platform session.
weight: 2
layout: learningpathall
---

## About Google Developer Device Platform

Google Developer Device Platform (DDP) gives you access to physical Android devices through Google Cloud, without buying and maintaining your own device farm. 

You can use DDP to accomplish the following tasks:

- Test a new feature across different phone models and Android versions.
- Compare performance across devices.
- Evaluate how games and other graphics applications look and respond on different devices.

You can use the Google [DDP agent skill](https://docs.cloud.google.com/developer-device-platform/agent-skill) to describe that work in natural language. Your coding agent can use the skill to perform the following tasks:

- Device configuration selection
- Phone reservation
- Connection through Android Debug Bridge (`adb`)
- Installation of tools required for your experiment

The agent handles the commands and connection details. You choose what to test, and approve access and spending.

The agent sends commands to the remote phone, where the commands run on real hardware. It can inspect the screen, interact with your app, and collect screenshots and measurements for you to review.

The Device Catalog helps you or your agent find an available device and confirm streaming support. Device Streaming provides the interactive connection, and Device Run supports automated tests and executables. For more information about these capabilities, see [DDP overview](https://docs.cloud.google.com/developer-device-platform/overview).

You'll prepare your workstation and benchmark a small language model trained on the TinyStories dataset on a remote Pixel 11. The agent checks Arm Scalable Vector Extension 2 (SVE2) support. It compares a CPU baseline with an optimized kernel path, and reports the measured performance.

{{% notice Note %}}
The example coding agent for this Learning Path is [Antigravity CLI](/install-guides/antigravity/). Other agents that support Agent Skills might also work.
{{% /notice %}}

## Understand the local development tools

Your development computer runs the Antigravity CLI and the Google Cloud CLI. The Google DDP skill is invoked on the development computer.

Python and `adb` keep the agent connected to the phone, and `scrcpy` opens the phone screen in a desktop window. Screenshots, logs, and the final report are saved on your computer.

The remote Google Pixel runs Termux, an Android terminal environment. Antigravity uses Termux to download llama.cpp and the TinyStories model. It builds the code with Clang, checks the Arm architecture features of the phone, and runs the benchmark.

## Check and install the local tools

With the Google Cloud CLI and Antigravity CLI (`agy`) already installed, check the other tools in your terminal:

```bash
python3 --version
node --version
npm --version
npx --version
curl --version
adb version
```

You need Python 3.10 or later, a supported Node.js LTS release with `npm` and `npx`, `curl`, and Android platform-tools (`adb`). Python runs the Google `adb` forwarder, and `npx` installs the agent skill. `curl` downloads files, and `adb` runs commands on the remote phone.

Use the instructions for your operating system to install or update any tools that are old or not available. Run the installation steps only for the tools that you need. A full Android Studio installation or host NDK isn't required.

{{< tabpane-normal >}}
  {{< tab header="Ubuntu 26.04" >}}
  
Install Python with virtual-environment support, `curl`, and `adb`. Git is used by the Node Version Manager (`nvm`) and to install `scrcpy`:

```bash
sudo apt update
sudo apt install -y python3 python3-venv curl adb ca-certificates git
```

If you need Node.js, install [nvm](https://github.com/nvm-sh/nvm#installing-and-updating). Load it into this terminal, and install the current LTS release. This also installs `npm` and `npx`:

```bash
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.41.0/install.sh | bash
export NVM_DIR="$HOME/.nvm"
. "$NVM_DIR/nvm.sh"
nvm install --lts
```

On other Linux distributions, install the equivalent tools with the package manager for your distribution.

  {{< /tab >}}
  {{< tab header="macOS" >}}

Use [Homebrew](https://brew.sh/) to install any missing tools. If Homebrew isn't installed, follow its installation instructions first. Complete the steps that it prints to add `brew` to your `PATH`.

Install Python, Node.js, and `curl`:

```bash
brew install python node curl
```
Node.js includes `npm` and `npx`.

Install `android-platform-tools` to provide `adb`:

```bash
brew install --cask android-platform-tools
```

  {{< /tab >}}
{{< /tabpane-normal >}}

Repeat the version checks after installation. Each command should print a version and exit successfully. If you installed Node.js with `nvm`, restart `agy` from a terminal that can find `node`, `npm`, and `npx`.

Google DDP CLI commands use the beta component. You don't need to install the beta component on newer versions of `gcloud` because it's already available.

Test if the beta command is already available:

```bash
gcloud beta help
```

If you see a help message, it's installed. You can continue. 

If you don't see a help message, install the beta component before continuing:

```bash
gcloud components install beta
```

If your package-managed CLI disables the component manager, follow [Google component installation instructions](https://docs.cloud.google.com/sdk/docs/components) for your installation method.

## Install `scrcpy` to view and control the phone

[scrcpy](https://github.com/Genymobile/scrcpy) displays an Android device in a desktop window and lets you control it with your keyboard and mouse. Install it on your development computer before reserving a phone. Use a local desktop session so that the viewer can open a window.

{{< tabpane-normal >}}
  {{< tab header="Ubuntu 26.04" >}}

The following commands build `scrcpy` 5.0.1 using the [scrcpy Linux installation instructions](https://github.com/Genymobile/scrcpy/blob/v5.0.1/doc/linux.md). These commands use Ubuntu 26.04, which provides the required SDL3 packages. For another distribution or release, follow the upstream instructions for its dependencies.

Install the viewer runtime and build dependencies:

```bash
sudo apt update
sudo apt install -y ffmpeg libsdl3-0 adb wget va-driver-all \
  gcc git pkg-config meson ninja-build libsdl3-dev \
  libavcodec-dev libavdevice-dev libavformat-dev libavutil-dev \
  libswresample-dev libusb-1.0-0 libusb-1.0-0-dev libv4l-dev libdrm-dev
```

Clone the release into a dedicated directory and run its installer. The script downloads and verifies a prebuilt Android server, builds the desktop client, and uses `sudo` to install it:

```bash
mkdir -p "$HOME/ddp-tools"
git clone --branch v5.0.1 --depth 1 https://github.com/Genymobile/scrcpy.git "$HOME/ddp-tools/scrcpy"
cd "$HOME/ddp-tools/scrcpy"
./install_release.sh
```

  {{< /tab >}}
  {{< tab header="macOS" >}}

Install the viewer using the [scrcpy macOS installation instructions](https://github.com/Genymobile/scrcpy/blob/master/doc/macos.md). It uses the `adb` installation:

```bash
brew install scrcpy
```

  {{< /tab >}}
{{< /tabpane-normal >}}

Confirm that the viewer is available:

```bash
scrcpy --version
```

You'll open the viewer after Antigravity connects to the reserved phone and returns its `adb` serial.

## Create the agent workspace

Create a directory for Antigravity and the benchmark evidence:

```bash
mkdir -p "$HOME/ddp-first-device/results"
cd "$HOME/ddp-first-device"
```

You'll run Antigravity CLI from this directory. Antigravity will run the local tools, discover the project skill, and save screenshots and reports under `results/`.

## Prepare the Google Cloud project

Using the Google account associated with your CLI setup, open the [Google Cloud console](https://console.cloud.google.com/). Select a development project with billing enabled.

{{% notice Note %}}
- DDP Device Streaming requires project access beyond signing in to Google Cloud. Before reserving a phone, confirm that your account has the roles described in the [Google DDP quickstart](https://docs.cloud.google.com/developer-device-platform/quickstart#required-roles). 

  The roles include Viewer, Device Run Admin, Device Streaming Admin, and Service Usage Consumer, or equivalent permissions supplied by your administrator. Enabling APIs also requires `serviceusage.services.enable`, for example through Service Usage Admin.
- Device Streaming sessions incur charges. Review the current price before approving a reservation.
{{% /notice %}}


In your workspace terminal, replace the example project ID:

```bash
export PROJECT_ID="YOUR_PROJECT_ID"
gcloud auth login
gcloud config set project "$PROJECT_ID"
gcloud auth application-default login
gcloud auth application-default set-quota-project "$PROJECT_ID"
```

Complete the sign-in and consent steps. The CLI uses its signed-in account for catalog requests. The Google Python streaming client uses Application Default Credentials (ADC), which are configured separately. Use the intended account for both.

Enable the services required by the quickstart:

```bash
gcloud services enable \
  devicerun.googleapis.com \
  devicestreaming.googleapis.com \
  testing.googleapis.com \
  --project="$PROJECT_ID"
```

The command waits for API activation to finish. 

On success, the output is similar to:

```output
Operation "operations/OPERATION_ID" finished successfully.
```

The operation ID varies. If the APIs are already enabled, the command returns successfully without printing a message. You'll confirm the enabled-service list later.

The Cloud Testing API is required by Device Streaming during preview. If your organization manages API activation centrally, ask the administrator to enable them.

## What you've accomplished and what's next

You've identified DDP capabilities, prepared the workstation tools, and configured a Google Cloud project and credentials.

Next, you'll verify that the CLI can reach the platform. You'll inspect a device configuration without reserving it.
