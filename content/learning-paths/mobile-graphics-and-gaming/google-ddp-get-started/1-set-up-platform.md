---
title: Set up Google Developer Device Platform
description: Install the local tools and configure a Google Cloud project and credentials for a Google Developer Device Platform session.
weight: 2
layout: learningpathall
---

## About the platform

Google Developer Device Platform (DDP) gives you access to physical Android devices through Google Cloud, without buying and maintaining your own device farm. You can try a new feature across different phone models and Android versions, compare performance, and check how games and other graphics applications look and respond on each device.

Google's [DDP agent skill](https://docs.cloud.google.com/developer-device-platform/agent-skill) lets you describe that work in natural language. Your coding agent can select a device configuration, reserve a phone, connect through Android Debug Bridge (ADB), and install the tools your experiment needs. It handles the commands and connection details while you choose what to test and approve access and spending.

The agent sends commands to the remote phone, where they run on real hardware. It can inspect the screen, interact with your app, and collect screenshots and measurements for you to review.

The Device Catalog helps you or your agent find an available device and confirm streaming support. Device Streaming provides the interactive connection, and Device Run supports automated tests and executables. See the [DDP overview](https://docs.cloud.google.com/developer-device-platform/overview) for more about these capabilities.

You'll prepare your workstation and benchmark a small language model trained on the TinyStories dataset on a remote Pixel 11. The agent checks Arm SVE2 support, compares a CPU baseline with an optimized kernel path, and reports the measured performance.

{{% notice Note %}}
The examples use [Antigravity CLI](/install-guides/antigravity/) as the coding agent. Other agents that support Agent Skills may also work.
{{% /notice %}}

## Understand the local development tools

Your development computer runs the Antigravity CLI, Google's DDP skill, and the Google Cloud CLI.

Python and ADB keep it connected to the phone, and `scrcpy` opens the phone's screen in a desktop window. Screenshots, logs, and the final report are saved on your computer.

The remote Pixel runs Termux, an Android terminal environment. Antigravity uses Termux to download llama.cpp and the TinyStories model, build the code with Clang, check the phone's Arm architecture features, and run the benchmark.

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

You need Python 3.10 or later, a supported Node.js LTS release with `npm` and `npx`, `curl`, and Android platform-tools (`adb`). Python runs Google's ADB forwarder, `npx` installs the agent skill, `curl` downloads files, and ADB runs commands on the remote phone.

If a command isn't found or its version is too old, use the instructions for your operating system to install or update the tool. Run the installation steps only for the tools you need. A full Android Studio installation or host NDK isn't required.

{{< tabpane-normal >}}
  {{< tab header="Ubuntu 26.04" >}}
  
Install Python with virtual-environment support, `curl`, and ADB. Git is used by the Node Version Manager and `scrcpy` installation steps:

```bash
sudo apt update
sudo apt install -y python3 python3-venv curl adb ca-certificates git
```

If you need Node.js, install [Node Version Manager (nvm)](https://github.com/nvm-sh/nvm#installing-and-updating), load it into this terminal, and install the current LTS release. This also installs npm and npx:

```bash
curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.41.0/install.sh | bash
export NVM_DIR="$HOME/.nvm"
. "$NVM_DIR/nvm.sh"
nvm install --lts
```

On other Linux distributions, install the equivalent Python, virtual-environment, curl, and ADB packages with your distribution's package manager.

  {{< /tab >}}
  {{< tab header="macOS" >}}

Use [Homebrew](https://brew.sh/) to install any missing tools. If Homebrew isn't installed, follow its installation instructions first and complete the steps it prints to add `brew` to your `PATH`.

Install Python, Node.js (which includes npm and npx), and curl:

```bash
brew install python node curl
```

Install Android platform-tools to provide ADB:

```bash
brew install --cask android-platform-tools
```

  {{< /tab >}}
{{< /tabpane-normal >}}

Repeat the version checks after installation. Each command should print a version and exit successfully. If you installed Node.js with `nvm`, restart `agy` from a terminal that can find `node`, `npm`, and `npx`.

DDP's CLI commands use the beta component. Newer versions of `gcloud` don't require the beta component to be installed; it's already available.

You can test if the beta command is already available by running:

```bash
gcloud beta help
```

If you see a help message, it's installed and you are ready to go. If not, you should install it before continuing:

```bash
gcloud components install beta
```

If your package-managed CLI disables the component manager, follow [Google's component installation instructions](https://docs.cloud.google.com/sdk/docs/components) for your installation method.

## Install scrcpy to view and control the phone

[scrcpy](https://github.com/Genymobile/scrcpy) displays an Android device in a desktop window and lets you control it with your keyboard and mouse. Install it on your development computer before reserving a phone. Use a local desktop session so the viewer can open a window.

{{< tabpane-normal >}}
  {{< tab header="Ubuntu 26.04" >}} The following commands build scrcpy 5.0.1 using its [upstream Linux installation procedure](https://github.com/Genymobile/scrcpy/blob/v5.0.1/doc/linux.md). These commands use Ubuntu 26.04, which provides the required SDL3 packages. For another distribution or release, follow the upstream instructions for its dependencies.

Install the viewer's runtime and build dependencies:

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

Install the viewer using the [upstream Homebrew instructions](https://github.com/Genymobile/scrcpy/blob/master/doc/macos.md). It uses the ADB installation from the previous section:

```bash
brew install scrcpy
```

  {{< /tab >}}
{{< /tabpane-normal >}}

Confirm that the viewer is available:

```bash
scrcpy --version
```

You'll open the viewer after Antigravity connects to the reserved phone and returns its ADB serial.

## Create the agent workspace

Create a directory for Antigravity and the benchmark evidence:

```bash
mkdir -p "$HOME/ddp-first-device/results"
cd "$HOME/ddp-first-device"
```

You'll run Antigravity CLI from this directory so it can run the local tools, discover the project skill, and save screenshots and reports under `results/`.

## Prepare the Google Cloud project

Using the Google account associated with your CLI setup, open the [Google Cloud console](https://console.cloud.google.com/) and select a development project with billing enabled.

{{% notice Note %}}
DDP Device Streaming requires project access beyond signing in to Google Cloud. Before reserving a phone, confirm that your account has the roles in [Google's DDP quickstart](https://docs.cloud.google.com/developer-device-platform/quickstart#required-roles): Viewer, Device Run Admin, Device Streaming Admin, and Service Usage Consumer, or equivalent permissions supplied by your administrator. Device Streaming sessions incur charges; review the current price before approving a reservation.
{{% /notice %}}

Enabling APIs also requires `serviceusage.services.enable`, for example through Service Usage Admin. Having permission to view a project doesn't establish permission to reserve a device or edit IAM.

In your workspace terminal, replace the example project ID:

```bash
export PROJECT_ID="YOUR_PROJECT_ID"
gcloud auth login
gcloud config set project "$PROJECT_ID"
gcloud auth application-default login
gcloud auth application-default set-quota-project "$PROJECT_ID"
```

Complete the sign-in and consent steps yourself. The CLI uses its signed-in account for catalog requests. Google's Python streaming client uses Application Default Credentials (ADC), which are configured separately. Use the intended account for both.

Enable the services required by the quickstart:

```bash
gcloud services enable \
  devicerun.googleapis.com \
  devicestreaming.googleapis.com \
  testing.googleapis.com \
  --project="$PROJECT_ID"
```

The command waits for API activation to finish. On success, the output is similar to:

```output
Operation "operations/OPERATION_ID" finished successfully.
```

The operation ID varies. If the APIs are already enabled, the command can return successfully without printing a message. You'll confirm the enabled-service list on the next page.

The Cloud Testing API is required by Device Streaming during Preview. If your organization manages API activation centrally, ask the administrator to enable them.

## What you've accomplished and what's next

You've identified DDP's capabilities, prepared the workstation tools, and configured a Google Cloud project and credentials. Next, you'll verify that the CLI can reach the platform and inspect a device configuration without reserving it.
