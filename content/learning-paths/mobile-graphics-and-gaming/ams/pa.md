---
# User change
title: "Performance Advisor with your application"

weight: 7 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
Now that you have seen an example Performance Advisor report, you can use it with your own application. Performance Advisor runs on a Streamline capture file, so the first step is to take a capture with Streamline. Streamline must capture extra frame data from the device, which Performance Advisor needs to generate a report. To capture the extra frame data, you must first run the provided Python script, `streamline_me.py`.

This script does the following:

* Temporarily installs a daemon application on your device, called `gatord`, which Streamline uses to collect counter data.
* Temporarily installs the OpenGL ES or Vulkan layer library file on your device, which is needed to collect frame data.
* Enables you to specify options for the capture, such as whether to collect screenshots when the FPS drops below a certain threshold.

## Before you begin

Performance Advisor uses a Python script to connect to your device. You will need `Python 3.6` or later installed on your host machine.

Build your application, and setup the Android device as described in [Setup tasks](/learning-paths/mobile-graphics-and-gaming/ams/setup_tasks/).


## Connect to the device

1. Open a terminal or command prompt, navigate to the `Arm Performance Studio` install directory and locate the `streamline_me.py` script:

    ```console
    cd <installation_directory>/streamline/bin/android
    ```

1. Run the script, enabling frame boundaries, with:
    ```console
    python3 streamline_me.py --lwi-mode=counters 
    ```
    To capture the Vulkan API, you also need to include the `--lwi-api=vulkan` option.

{{% notice Tip %}}
To see all available options, use `python3 streamline_me.py --help`
{{% /notice %}}

1. The script returns a numbered list of the Android package names for the debuggable applications that are installed on your device. Enter the number of the application you want to profile.
    ```python
    Searching for devices:
    RZ8MC03VVEW / SM-A505FN found

    Select a device:
    Auto-selected RZ8MC03VVEW / SM-A505FN

    Searching for debuggable packages:
    5 debuggable packages found         

    Select a debuggable packages:
     1) com.Arm.DarkArms
     2) com.UnityTechnologies.BoatAttack
     3) com.arm.malideveloper.openglessdk.occlusionculling
     4) com.arm.pa.paretrace
     5) com.sample.texturedteapot
     0) Exit script
    ```
    The script identifies the GPU in the device, installs the daemon application and layer library, then waits for you to complete the capture in Streamline.

1. Leave the terminal window open, as you need to come back to it after the capture is complete, to stop the script. When the script ends, any captured screenshots are saved to the directory you specified, and the daemon application and layer library are uninstalled from the device. Do not unplug the device until the script has ended.

See the [Get started with Performance Advisor Tutorial](https://developer.arm.com/documentation/102478/latest/Run-the-streamline-me-py-script) for full instructions.

## Capture data with Streamline

1. Open Streamline and select the device and application on the `Start` tab.

1. Click `Start capture` to start capturing profile data from the target. Enter a name and location for the capture file that Streamline creates.

1. The application starts automatically on the device. Interact with the application as required.

1. When you have collected enough data, click the `Stop capture` button.

1. Return to your terminal, and press `ENTER` to terminate the `streamline_me.py` script.

## Generate an HTML performance report

1. In the terminal window, navigate to the location where you stored the Streamline capture file (`.apc`).

1. Run Streamline's  `streamline-cli` command with the `-pa` option on the Streamline capture file to generate the report. The default name is `report.html`.
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

1. In the terminal window, navigate to the location where you stored the Streamline capture file (`.apc`).

1. Run Streamline's  `streamline-cli` command with the `-pa` and `--type=json` options on the Streamline capture file to generate the report (named `report.json` in below):
    ```console
    streamline-cli -pa --type=json:report.json <other_options> my_capture.apc
    ```

## Performance budgets

You can specify a performance budget which will be reflected in the Performance Advisor report. For more information, refer to the [Performance Advisor User Guide](https://developer.arm.com/documentation/102009/latest/Quick-start-guide/Setting-performance-budgets) section on performance budgets.
