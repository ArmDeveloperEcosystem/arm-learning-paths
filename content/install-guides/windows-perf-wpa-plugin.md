---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Windows Performance Analyzer (WPA) Plugin
minutes_to_complete: 15

official_docs: https://github.com/arm-developer-tools/windowsperf-wpa-plugin

author_primary: Alaaeddine Chakroun 

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
  - perf
  - profiling
  - profiler
  - windows
  - woa
  - windows on arm
  - windows performance analyzer
  - wpa
  
### FIXED, DO NOT MODIFY
weight: 1 # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true # Set to true to be listed in main selection page, else false
multi_install: FALSE # Set to true if first page of multi-page article, else false
multitool_install_part: false # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall # DO NOT MODIFY. Always true for tool install articles
---

## What is the Windows Performance Analyzer plugin?

The Windows Performance Analyzer plugin connects Windows Perf to the Windows Performance Analyzer (WPA).

[WindowsPerf](https://github.com/arm-developer-tools/windowsperf) is a lightweight performance profiling tool inspired by Linux Perf and designed for Windows on Arm.

Windows Performance Analyzer (WPA) is a tool that creates graphs and data tables of Event Tracing for Windows (ETW) events that are recorded by Windows Performance Recorder (WPR), Xperf, or an assessment that is run in the Assessment Platform. WPA opens event trace log (ETL) files for analysis.

The WPA plugin is built using the [Microsoft Performance Toolkit SDK](https://github.com/microsoft/microsoft-performance-toolkit-sdk), a collection of tools to create and extend performance analysis applications. The plugin parses json output from WidowsPerf so that it can be visualized in WPA. 

## What are some of the features of the WPA plugin? 

The WindowsPerf GUI extension is composed of several key features, each designed to streamline the user experience:

### What is the timeline view?

The timeline view visualizes the `wperf stat` timeline data plotted by event group.

![Timeline By Core Table](/install-guides/_images/wpa-timeline-by-core.png)

### What is the telemetry view?

The telemetry view displays telemetry events grouped by unit.

![Telemetry Table](/install-guides/_images/wpa-telemetry-table.png)

## How do I install the WPA plugin?

Before using the WPA plugin, make sure you have installed WPA.

### Windows Performance Analyzer

WPA is included in the Windows Assessment and Deployment Kit (Windows ADK) that can be downloaded from [Microsoft](https://go.microsoft.com/fwlink/?linkid=2243390).

{{% notice Note %}}
The WPA plugin requires WPA version `11.0.7.2` or higher.
{{% /notice %}}

Run the downloaded `adksetup.exe` program. 

Specify the default installation location and accept the license agreement. 

Make sure that "Windows Performance Toolkit" is checked under "Select the features you want to install".

![WPA Installation](/install-guides/_images/wpa-installation.png)

Finally, click Install.

### Windows Performance Analyzer plugin

The plugin is a single `.dll` file.

Download a `.zip` file from the [GitHub releases page](https://github.com/arm-developer-tools/windowsperf-wpa-plugin/releases).

To download the latest version from the command prompt:

```console
mkdir wpa-plugin
cd wpa-plugin
curl -L -O https://github.com/arm-developer-tools/windowsperf-wpa-plugin/releases/download/1.0.2/wpa-plugin-1.0.2.zip
```

Extract the `.dll` file from the downloaded `.zip` file. 

```console
tar -xmf wpa-plugin-1.0.2.zip
```

You now have the file `WPAPlugin.dll` in your `wpa-plugin` directory. 

There are three ways you can install the `WPAPlugin.dll` file: 

###### 1. Copy the plugin dll to the CustomDataSources directory next to the WPA executable.

The default location is: 
        `C:\\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\CustomDataSources`

###### 2. Set an environment variable

Set the `WPA_ADDITIONAL_SEARCH_DIRECTORIES` environment variable to the location of the DLL file.

###### 3. Start WPA from the command line and pass the plugin directory location using a flag.

Use the `-addsearchdir` flag for `wpa`:

```bash
wpa -addsearchdir "%USERPROFILE%\plugins"
```
        
## How can I verify the WPA plugin is installed?

To verify the plugin is loaded, launch WPA and the plugin should appear under `Help > About Windows Performance Analyzer`

![WPA installation confirmation](/install-guides/_images/about-wpa.png)

## How can I run the WPA plugin from the command line?

To open a json file directly from the command line, you can use the `-i` flag to specify the file path to open.

For example: to open `timeline_long.json` in your downloads directory, run the command:

```console
wpa -i "%USERPROFILE%\\Downloads\\timeline_long.json"
```
## How do I uninstall the WPA plugin?

To uninstall the plugin simply delete the `WPAPlugin.dll` file.

