---
# User change
title: "Arm Performance Advisor"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Performance Advisor is a tool that provides a report showing how your Android application performs on a mobile device.

## Prerequisites

Performance Advisor uses a Python script to connect to your device. You will need `Python 3.5` or later installed on your host machine.

Build your application, and setup Android device as per Streamline instructions.

## Connect to the device

Open a terminal or command prompt, and navigate to the `Arm Mobile Studio` install directory. Therein, locate the `lwi_me.py` script:
```console
cd <installation_directory>/performance_advisor/bin/android
```
To run the script, use:
```console
python3 lwi_me.py <options>
```
The available options are documented [here](https://developer.arm.com/documentation/102009/latest/Command-line-options/The-lwi-me-py-script-options), else can be seen with:
```console
python3 lwi_me.py -h
```
The script returns a numbered list of the Android package names for the debuggable applications that are installed on your device. Enter the number of the application you want to profile.

Leave the script running (do not close terminal).

## Profile application (with Streamline)

In Streamline, click on `Start capture` to start capturing profile data from the target.

Start the application on the device, and interact as desired for the profiling run you wish to do.

When satisfied, click on `Stop capture`. Note the location where the captured data is stored.

Return to your terminal, and terminate the `lwi_me.py` script.

## Generate a HTML performance report

In the terminal window, navigate to the stored data folder. List contents with `dir` or `ls` depending on host. The Streamline data will be in a `.apc` directory.

Run Performance Analyzer on the appropriate folder to generate the report which can then be opened with any browser. The default name is `report.html`.
```console
pa <options> my_capture.apc
```
The available options are documented [here](https://developer.arm.com/documentation/102009/latest/Command-line-options/The-pa-command), else can be seen with:
```console
pa -h
```
They can also be passed within an [options file](https://developer.arm.com/documentation/102009/latest/Command-line-options/The-pa-command/pa-command-line-options-file).

### Performance budget

You can specify a performance budget which will be reflected in the Performance Advisor report. For more information, see [here](https://developer.arm.com/documentation/102687).

## Generate a JSON performance report

This feature is particularly useful when used within a [CI workflow](https://developer.arm.com/documentation/102543).

In the terminal window, navigate to the stored data folder. List contents with `dir` or `ls` depending on host. The Streamline data will be in a `.apc` directory.

Run Performance Analyzer on the appropriate folder to generate the report (named `report.json` in below):
```console
pa --type=json:report.json <other_options> my_capture.apc
```
