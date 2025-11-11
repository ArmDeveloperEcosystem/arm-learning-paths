---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Visual Studio Extension for WindowsPerf

minutes_to_complete: 10

official_docs: https://gitlab.com/Linaro/WindowsPerf/vs-extension

author: Nader Zouaoui

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
  - perf
  - profiling
  - profiler
  - windows
  - windows on arm
  - visual studio

### FIXED, DO NOT MODIFY
weight: 1 # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true # Set to true to be listed in main selection page, else false
multi_install: FALSE # Set to true if first page of multi-page article, else false
multitool_install_part: false # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall # DO NOT MODIFY. Always true for tool install articles
---

WindowsPerf is a lightweight performance profiling tool inspired by Linux Perf, and designed specifically for Windows on Arm. 

The WindowsPerf GUI is a Visual Studio 2022 extension that provides an intuitive, integrated experience within the Visual Studio Integrated Development Environment (IDE). The extension enables developers to interact with WindowsPerf, adjust settings, and visualize performance data seamlessly in Visual Studio.

## What steps must I complete before installing the Visual Studio Extension for WindowsPerf?

Before installing the Visual Studio Extension for WindowsPerf, complete the following steps:

1. Install [Visual Studio 2022](/install-guides/vs-woa/) on your Windows on Arm device.
2. Install WindowsPerf using the [WindowsPerf install guide](/install-guides/wperf/).
3. Install the LLVM toolchain using the [LLVM toolchain for Windows on Arm install guide](/install-guides/llvm-woa/).

{{% notice llvm-objdump %}}
The disassembly feature requires `llvm-objdump` in the search path. Verify that your `%PATH%` variable includes the location of `llvm-objdump` to ensure proper functionality. 
{{% /notice %}}

### How do I install the extension using the Visual Studio Extension Manager?

To install the Visual Studio extension for WindowsPerf from Visual Studio, use the Extension Manager:

1. Open Visual Studio 2022.
2. Navigate to the `Extensions` menu, and select `Manage Extensions`.
3. Select the `Search (Ctrl+L)` bar, and type `WindowsPerf`.
4. Select the `Install` button. 
5. Restart Visual Studio to complete installation.

![Install #center](/install-guides/_images/wperf-vs-extension-install-page.png)

### How do I install the extension from GitLab?

You can also install the WindowsPerf Visual Studio Extension from GitLab. 

Using a browser, visit the [Releases](https://gitlab.com/Linaro/WindowsPerf/vs-extension/-/releases) page and download the latest file. For example, `windowsperf-gui-3.1.3.zip`.

Unzip the downloaded file and double click on the `WindowsPerfGUI.vsix` file.

Follow the prompts to install the Visual Studio extension.

![VSIX Install #center](/install-guides/_images/vs-ext-install.png)

{{% notice Note %}}
Ensure that any previous version of the extension is uninstalled and that Visual Studio is closed before installing the extension.
{{% /notice %}}

### How do I build and install the extension from source code?

Building the source is not required, but is an alternative installation method if you want to customize the extension. 

To build the source code, clone [the repository](https://gitlab.com/Linaro/WindowsPerf/vs-extension.git) using Git. 

```console
git clone https://gitlab.com/Linaro/WindowsPerf/vs-extension.git
```

Double click the `WindowsPerfGUI.sln` solution file to open the project Visual Studio. 

{{% notice Note %}}
Visual Studio may prompt you to install additional components required to build the project, install these components. 
{{% /notice %}}

Open the `Build` menu and select `Build Solution` to create `WindowsPerfGUI.dll` and `WindowsPerfGUI.vsix`. You can replace the currently installed files with these files to try any changes you have made.

### How do I set up WindowsPerf in Visual Studio?

After the extension is installed, you must link the extension with the `wperf.exe` file by navigating to `Tools > Options > WindowsPerf > WindowsPerf Path` in Visual Studio.

Use the `Select` button to navigate to your `wperf.exe` and the `Validate` button to confirm the executable is found. 

![Validate #center](/install-guides/_images/wperf-validate.png)

This step is crucial for utilizing the extension, and the extension will not work without this configuration.

## What are the key features of the WindowsPerf extension?

The WindowsPerf extension is composed of several key features, each designed to streamline the user experience:

* WindowsPerf Configuration: Connect directly to `wperf.exe` for a seamless integration. 
* Host Data: Understand your environment by selecting `Tools` then `WindowsPerf Host Data`. 
* Output Logging: All commands executed through the GUI are logged, ensuring transparency and aiding with performance analysis.
* Sampling UI: Customize your sampling experience by selecting events, setting frequency and duration, choosing programs for sampling, and comprehensively analyzing results. 

The sampling interface is shown below:

![Sampling preview #center](/install-guides/_images/wperf-vs-extension-sampling-preview.webp)

* Counting Settings UI: Build a `wperf stat` command from scratch using the configuration interface, then view the output in VS Code or open it with Windows Performance Analyzer (WPA). 
The interface to configure counting is shown below:

![Counting preview #center](/install-guides/_images/wperf-vs-extension-counting-preview.png)

## How do I uninstall the WindowsPerf extension?

To uninstall the extension in Visual Studio:

Go to `Extensions > Manage Extensions > Installed > All > WindowsPerfGUI` and select `Uninstall`. 

Visual Studio will schedule the uninstallation. To complete the process, close Visual Studio and follow the uninstall dialog prompts.
