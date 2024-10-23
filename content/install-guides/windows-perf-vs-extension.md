---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: WindowsPerf Visual Studio Extension
draft: true
cascade:
    draft: true

minutes_to_complete: 10

official_docs: https://github.com/arm-developer-tools/windowsperf-vs-extension

author_primary: Nader Zouaoui

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
  - perf
  - profiling
  - profiler
  - windows
  - woa
  - windows on arm
  - visual studio
### FIXED, DO NOT MODIFY
weight: 1 # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true # Set to true to be listed in main selection page, else false
multi_install: FALSE # Set to true if first page of multi-page article, else false
multitool_install_part: false # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall # DO NOT MODIFY. Always true for tool install articles
---

## Introduction

WindowsPerf is a lightweight performance profiling tool inspired by Linux Perf, and specifically tailored for Windows on Arm. It leverages the ARM64 PMU (Performance Monitor Unit) and its hardware counters to offer precise profiling capabilities. 

Recognizing the complexities of command-line interaction, the WindowsPerf GUI is a Visual Studio 2022 extension created to provide a more intuitive, integrated experience within the integrated development environment (IDE). This tool enables developers to interact with WindowsPerf, adjust settings, and visualize performance data seamlessly in Visual Studio.

## A Glimpse of the available features

The WindowsPerf GUI extension is composed of several key features, each designed to streamline the user experience:

- **WindowsPerf Configuration**: Connect directly to `wperf.exe` for a seamless integration. Configuration is accessible via `Tools -> Options -> Windows Perf -> WindowsPerf Path`.
- **Host Data**: Understand your environment with `Tools -> WindowsPerf Host Data`, offering insights into tests run by WindowsPerf.
- **Output Logging**: All commands executed through the GUI are logged, ensuring transparency and aiding in performance analysis.
- **Sampling UI**: Customize your sampling experience by selecting events, setting frequency and duration, choosing programs for sampling, and comprehensively analyzing results.

![Sampling preview #center](../_images/wperf-vs-extension-sampling-preview.png "Sampling settings UI Overview")


- **Counting Settings UI**: Build a `wperf stat` command from scratch using the configuration interface, then view the output in the IDE or open it with Windows Performance Analyzer (WPA)


![Counting preview #center](../_images/wperf-vs-extension-counting-preview.png "_Counting settings UI Overview_")


## Getting Started

### Prerequisites

- **Visual Studio 2022**: Ensure you have Visual Studio 2022 installed on your Windows on Arm device.
- **WindowsPerf**: Download and install WindowsPerf by following the [WindowsPerf install guide](/install-guides/wperf/).
- **LLVM** (Recommended): You can install the LLVM toolchain by following the [LLVM toolchain for Windows on Arm install guide](/install-guides/llvm-woa).

{{% notice llvm-objdump %}}
The disassembly feature needs to have `llvm-objdump` available at `%PATH%` to work properly.
{{% /notice %}}

### Installation from Visual Studio Extension Manager

To install the WindowsPerf Visual Studio Extension from Visual Studio:

1. Open Visual Studio 2022
2. Go to the `Extensions` menu
3. Select **Manage Extensions**
4. Click on the search bar ( or tap `Ctrl` + `L` ) and type `WindowsPerf`
5. Click on the install button and restart Visual Studio

![WindowsPerf install page #center](../_images/wperf-vs-extension-install-page.png)

### Installation from GitHub

You can also install the WindowsPerf Visual Studio Extension from GitHub. 

Download the installation file directly from the [GitHub release page](https://github.com/arm-developer-tools/windowsperf-vs-extension/releases).

Unzip the downloaded file and double click on the `WindowsPerfGUI.vsix` file

{{% notice Note %}}
Make sure that any previous version of the extension is uninstalled and that Visual Studio is closed before installing the extension.
{{% /notice %}}

### Build from source

To build the source code, clone [the repository](https://github.com/arm-developer-tools/windowsperf-vs-extension) and build the `WindowsPerfGUI` solution using the default configuration in Visual Studio. 

Building the source is not required, but offered as an alternative installation method if you want to customize the extension. 

### WindowsPerf Setup

To get started, you must link the GUI with the executable file `wperf.exe` by navigating to `Tools -> Options -> WindowsPerf -> WindowsPerf Path`. This step is crucial for utilizing the GUI, and the extension will not work if you don't do it.

## Uninstall the WindowsPerfGUI extension

In Visual Studio go to `Extensions` -> `Manage Extensions` -> `Installed` -> `All` -> `WindowsPerfGUI` and select "Uninstall". 

Please note that this will be scheduled by Visual Studio. You may need to close VS instance and follow uninstall wizard to remove the extension.
