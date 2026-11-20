---
title: Environment setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Create a working directory
Create a working directory to store the Learning Path files:
```bash
mkdir -p "$HOME/Work"
export WORK="$HOME/Work"
```

Set the base URL for the scripts and configuration files you'll download later:
```bash
export BASE_URL=https://raw.githubusercontent.com/dylree01/arm-learning-paths/refs/heads/androidRuntime/content/learning-paths/mobile-graphics-and-gaming/android_runtime_performance_adb
```
<!-- ```bash
export BASE_URL=https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/mobile-graphics-and-gaming/android_runtime_performance_adb
``` -->
Run the commands in the same terminal session, or set `WORK` and `BASE_URL` again if you open a new one.

# Install Android SDK
Install Java 17 and the Android command-line tools with Homebrew, followed by the SDK Platform Tools:
``` bash
brew install --cask temurin@17 android-commandlinetools

# Use a consistent, user-owned location for downloaded SDK packages.
export ANDROID_HOME="$HOME/Library/Android/sdk"
export PATH="$PATH:$ANDROID_HOME/platform-tools"
mkdir -p "$ANDROID_HOME"

# Homebrew provides this command; --sdk selects the package destination.
android --sdk="$ANDROID_HOME" sdk install platform-tools
```
The `platform-tools` package contains `adb` which you will use later to connect and interact with your Android device.

Verify the installation:
``` bash
android --sdk="$ANDROID_HOME" sdk list
command -v adb
adb --version
```

# Install Perfetto tools for profiling
Perfetto is an open-source system tracing and performance analysis platform. You'll use it as part of your performance analysis to capture kernel-level events, process statistics and hardware activity.

Trace Processor is a C++ library that loads Perfetto traces and provides an SQL interface for querying them.

Download this tool into your working directory:
```bash
mkdir -p "$WORK/tools/perfetto"
curl -fL https://raw.githubusercontent.com/google/perfetto/v59.0/tools/trace_processor \
  -o "$WORK/tools/perfetto/trace_processor"
chmod +x "$WORK/tools/perfetto/trace_processor"

export PERFETTO_TRACE_PROCESSOR="$WORK/tools/perfetto/trace_processor"
```

# Install Jupyter Notebook
To create a Jupyter Notebook, install JupyterLab if it is not already:
``` bash
brew install jupyterlab
```
Verify the installation:
```bash
jupyter --version
```

With the `jupyter lab` command, you can run a locally hosted web UI for developing Jupyter Notebook files. You will use this to create your analysis pipeline.

# Install Hugging Face Hub
Install the Hugging Face Hub CLI where you will download the LiteRT-LM model from:
```bash
brew install hf
hf version
```

# What you've accomplished
So far, you have installed all the necessary environment tools and packages which you will need to complete the Learning Path. In the next section you'll use the Android Platform tools to wirelessly connect to a device.
