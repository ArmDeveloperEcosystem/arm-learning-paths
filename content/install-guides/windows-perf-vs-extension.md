---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: WindowsPerf Ecosystem - the Visual Studio Extension
minutes_to_complete: 5

official_docs: https://github.com/nader-zouaoui/windowsperf-vs-extension

author_primary: Nader Zouaoui

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
  - perf
  - profiling
  - profiler
  - windows
  - woa
  - windows on arm
  - open source windows on arm
  - visual studio
### FIXED, DO NOT MODIFY
weight: 1 # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true # Set to true to be listed in main selection page, else false
multi_install: FALSE # Set to true if first page of multi-page article, else false
multitool_install_part: false # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall # DO NOT MODIFY. Always true for tool install articles
---

## Introduction

**WindowsPerf** is a lightweight performance profiling tool inspired by Linux perf, specifically tailored for Windows on ARM. It leverages the ARM64 PMU (Performance Monitor Unit) and its hardware counters to offer precise profiling capabilities. Recognizing the complexities of command-line interaction, the WindowsPerf GUI project is a Visual Studio 2022 extension that was initiated to provide a more intuitive, integrated within the development environment (IDE) experience. This tool enables developers to interact with WindowsPerf, adjust settings, and visualize performance data seamlessly within the IDE.

## A Glimpse of the UI

The WindowsPerf GUI extension is composed of several key features, each designed to streamline the user experience:

![Sampling preview #center](../_images/wperf-vs-extension-sampling-preview.png)

- **WindowsPerf Configuration**: Connect directly to `wperf.exe` for a seamless integration. Configuration is accessible via `Tools -> Options -> Windows Perf -> WindowsPerf Path`.
- **Host Data**: Understand your environment with `Tools -> WindowsPerf Host Data`, offering insights into tests run by WindowsPerf and their outcomes.
- **Output Logging**: All commands executed through the GUI are meticulously logged, ensuring transparency and aiding in performance analysis.
- **Sampling UI**: Customize your sampling experience by selecting events, setting frequency and duration, choosing programs for sampling, and comprehensively analyzing results.
- **Counting Settings UI**: Build a `wperf stat` command from scratch using our configurator, then view the output on the IDE or open it on WPA

![Counting preview #center](../_images/wperf-vs-extension-counting-preview.png)

## Getting Started

### Prerequisites

- **Visual Studio 2022**: Ensure you have Visual Studio 2022 installed on your Windows on Arm device.
- **WindowsPerf**: Download and install WindowsPerf. You can follow this [learning path](../wperf) for further details
- **LLVM** (Optional): You can install the LLVM toolchain by following this [guide](../llvm-woa).

{{% notice llvm-objdump %}}
The disassembly feature needs to have `llvm-objdump` available at `%PATH%` to work properly.
{{% /notice %}}

### Installation (Option 1)

To install WindowsPerf Visual Studio Extension you can do that from Visual Studio itself.

1. Open Visual Studio 2022
2. Go to `Extensions` menu
3. Select **Manage Extensions**
4. Click on the search bar ( or tap `Ctrl` + `L` ) and type `WindowsPerf`
5. Click on the install button and restart Visual Studio

![WindwosPerf install page #center](../_images/wperf-vs-extension-install-page.png)

### Installation (Option 2)

To install WindowsPerf Visual Studio Extension you can download the installation file directly from our [GitHub release page](https://github.com/arm-developer-tools/windowsperf-vs-extension/releases).

Unzip the downloaded file and double click on the `WindowsPerfGUI.vsix` file

{{% notice Note %}}
You need to make sure that any previous version of the extension is uninstalled and that Visual Studio is closed before installing the extension.
{{% /notice %}}

### Build from source

For those preferring to build from the source, simply clone [the repository](https://github.com/arm-developer-tools/windowsperf-vs-extension) and build the `WindowsPerfGUI` solution using the default configuration on Visual Studio. This alternative installation method offers flexibility and customization.

### Setup

To get started, you must link the GUI with the executable file `wperf.exe` by navigating to `Tools -> Options -> Windows Perf -> WindowsPerf Path`. This step is crucial for utilizing the GUI. The extension **will not work** without it!

## How to uninstall old WindowsPerfGUI extension

In Visual Studio go to `Extensions` -> `Manage Extensions` -> `Installed` -> `All` -> `WindowsPerfGUI` and select "Uninstall". Please note that this will be scheduled by VS. You may need to close VS instance and follow uninstallation wizard to remove extension.
