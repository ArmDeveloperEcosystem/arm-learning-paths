---
# User change
title: "Performance Advisor with your application"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Now that you have seen an example Performance Advisor report, you can use it with your own application.

## Before you begin

Performance Advisor uses a Python script to connect to your device. You will need `Python 3.6` or later installed on your host machine.

Build your application, and setup Android device as per previous [instructions](../streamline).

## Connect to the device

Open a terminal or command prompt, and navigate to the `Arm Mobile Studio` install directory. Therein, locate the `streamline_me.py` script:

```console
cd <installation_directory>/streamline/bin/android
```
Run the script, enabling frame boundaries, with:
```console
python3 streamline_me.py --lwi-mode=counters
```

To see all available options, use:
```console
python3 streamline_me.py --help
```
See the [Get started with Performance Advisor Tutorial](https://developer.arm.com/documentation/102478/latest/Run-the-streamline-me-py-script) for full instructions.

The script returns a numbered list of the Android package names for the debuggable applications that are installed on your device. Enter the number of the application you want to profile.

Leave the script running (do not close terminal).

## Profile application (with Streamline)

In Streamline, click on `Start capture` to start capturing profile data from the target.

Start the application on the device, and interact as desired for the profiling run you wish to do.

When satisfied, click on `Stop capture`. Note the location where the captured data is stored.

Return to your terminal, and terminate the `streamline_me.py` script.

## Generate a HTML performance report

In the terminal window, navigate to the stored data folder. List contents with `dir` or `ls` depending on host. The Streamline data will be in a `.apc` directory.

Run `Performance Advisor` on the appropriate folder to generate the report which can then be opened with any browser. The default name is `report.html`.
```console
streamline-cli -pa <options> my_capture.apc
```
The available options are documented in the [Performance Advisor User Guide](https://developer.arm.com/documentation/102009/latest/Command-line-options/The-pa-command), else can be seen with:
```console
streamline-cli -pa -h
```
They can also be passed within an [options file](https://developer.arm.com/documentation/102009/latest/Command-line-options/The-pa-command/pa-command-line-options-file).

## Generate a JSON performance report

This feature is particularly useful when used within a [CI workflow](https://developer.arm.com/documentation/102543).

In the terminal window, navigate to the stored data folder. List contents with `dir` or `ls` depending on host. The Streamline data will be in a `.apc` directory.

Run Performance Advisor on the appropriate folder to generate the report (named `report.json` in below):
```console
streamline-cli -pa --type=json:report.json <other_options> my_capture.apc
```

## Performance budget

You can specify a performance budget which will be reflected in the Performance Advisor report. For more information, refer to the [Performance Advisor User Guide](https://developer.arm.com/documentation/102009/latest/Quick-start-guide/Setting-performance-budgets) section on performance budgets.
