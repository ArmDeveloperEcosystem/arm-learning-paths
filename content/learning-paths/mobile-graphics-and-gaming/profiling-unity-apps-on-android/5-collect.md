---
title: Collect performance data
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Collect data from the Profiler
In this section, you will collect data from the Profiler that can be used later in the Profile Analyzer. You will record data from two different versions of the collision sample; unoptimized (or plain) and optimized (using Neon). Later on you will load the data into the Analyzer to visualize and compare the datasets.

The sample app works best on Android when in landscape orientation. Information will be displayed in the bottom right.

### Collect data from unoptimized version
You will now collect some data from the unoptimized version of the code. To do this, save the data from the two builds first and then later load the data into the Analyzer to visualize, and compare the two data sets.

1. Open the script *Assets/BurstNeonCollisions/Scripts/CollisionCalculationScript.cs*.

2. Find line 66. Change it to look like this:

    ```
    public const Mode codeMode = Mode.Plain;
    ```

3. Build and deploy to your Android device:

    - Open _File/Build Profiles_

    - Ensure the following options are ticked:

        - _Development Build_

        - _Autoconnect Profiler_

    - Ensure your device is selected in _Run Device_ drop-down menu

    - Select _Build and Run_

    - Enter a path and filename for your Android package (e.g., `plain.apk`)

    - When the app starts on your device, ensure it says Standard Mode in the bottom right. If not, start again from step 1.

4. The Profiler window will open

    - Ensure the record button is enabled (it will be red)

    - Let the Profiler record - a few hundred frames or so will be enough for this tutorial

5. Save the performance data

    - Select the disk icon in the top right of the Profiler window

    - Enter filename by clicking on the name in the file list on the left of the screen
    
        ```
        plain.data
        ```

    - Save to disk

### Collect data for the optimized version

Let's repeat the above process but this time build and deploy the optimized version of the code.

1. Open the script *Assets/BurstNeonCollisions/Scripts/CollisionCalculationScript.cs*

    - Find line 66. Change it to look like this:

        ```
        public const Mode codeMode = Mode.Neon;
        ```

    - Build and deploy to your Android device:

        1. Open _File/Build Profiles_

        2. Ensure the following options are ticked:

           - _Development Build_

           - _Autoconnect Profiler_

    - Ensure your device is selected in _Run Device_ drop-down menu

    - Select Build and Run

    - Enter a path and filename for your Android package (e.g., `neon.apk`)

    - When the app starts on your device, ensure it says Neon Mode in the bottom right. If not, start again from step 1.

2. The Profiler window will open

    - Ensure the record button is enabled (it will be red)

    - Let the Profiler record; again, a few hundred frames or so will be enough for this comparison

3. Save the performance data

    - Select the disk icon in the top right of the Profiler window

    - Enter filename

        ```
        neon.data
        ```

    - Save to disk

### Profiler summary

You have now collected performance data for two versions of the build; essentially "pre" and "post" optimization. The optimizations (Burst and Neon) made in this sample will be covered in the next Learning Path in this series.

`Plain.data` contains performance data from the unoptimized version. `Neon.data` contains data from the optimized version.

You now know how to use the Profiler tool to analyze specific frames of performance data and save data for later.

In the next section, you will use the Analyzer tool to visualize and compare the data you have collected.
