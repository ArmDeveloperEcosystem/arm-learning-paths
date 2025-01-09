---
title: Collecting performance data
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Measure and compare
As with any typical software development, once you have reached an optimization cycle, you will want to measure existing performance, make modifications to code, structures or data and then measure again and compare the results.

To keep this learning path a reasonable length, we will just measure and compare the final optimized versions against the original. We’ll collect data for plain, Burst and neon modes. This section will cover this using the Profiler and Analyzer tools in Unity.

For more detail regarding the Profiler and Analyzer, please read the previous learning path in this series, [Profiling Unity apps on Android](/learning-paths/mobile-graphics-and-gaming/profiling-unity-apps-on-android).

## Create a consistent scenario
First, you will need a consistent scenario in which you can reliably compare the three modes. We need to compare the data when all the versions are processing the same amount of data. It’s important to note that the randomness of the scene can make it harder to pick representative frames but we can wait until the number of characters is the same in each run.

The sample generates new characters every frame up to a maximum of 2401. This maximum is reached in a couple of minutes or so.

Unfortunately, the sample code doesn’t display the character count but it can be added easily.

### Display character count
First, pass the character count to the `ScreenWriteout` function call in _Update_. Line 265 becomes:

```
ScreenWriteout(numChar);
```

Now add the `numChar` parameter to the function. Line 497 becomes:

```
private void ScreenWriteout(int numChar)
```

Now display the character count in the `ScreenWriteout` function. Lines 506 and 507 become:

```
+ "Character Collisions: " + radiusCollideFrameTime().ToString("N3") + "ms\n"
+ "Characters: " + numChar.ToString();
```

## Record performance data for plain mode
You will need to ensure plain (unoptimized) mode is active:

1. Open _Assets/BurstNeonCollisions/Scripts/CollisionCalculationScript.cs_

2. Go to line 66

3. Edit the line to match the following:

```
public const Mode codeMode = Mode.Plain;
```

4. Open _Build Settings_ from the _File_ menu

5. Ensure the following options:

    1. _Development build_ is ticked

    1. _Autoconnect Profiler_ is ticked

    1. _Run Device_ is set to your Android device

6. Select _Build and Run_

7. Choose a filename, e.g., _plain.apk_

8. The application will build and deploy to your Android device

9. The Profiler will start collecting data automatically

10. Wait until the character count hits 2401 and then make sure to record for another 300 frames. If you prefer, you could clear the results as soon as the character count hits 2401, or not tick _Autoconnect Profiler_ and start recording manually.

11. Select the disk icon in the top-right and save the data as _plain.data_

## Record performance data for Burst mode
Repeat the above process to record performance data for Burst mode. All of the steps are the same except that we set the mode in _CollisionCalculationScript.cs_ as follows:

```
public const Mode codeMode = Mode.Burst;
```

Name your apk _burst.apk_ and your saved performance data as _burst.data_.

## Record performance data for Neon mode
Repeat the above process again to record performance data for Neon mode. Again, the steps are the same except that we set the mode in _CollisionCalculationScript.cs_ as follows:

```
public const Mode codeMode = Mode.Neon;
```

Name your apk _neon.apk_ and your saved performance data as _neon.data_.
