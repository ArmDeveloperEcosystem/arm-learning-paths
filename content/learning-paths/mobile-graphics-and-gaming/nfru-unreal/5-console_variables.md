---
title: Understand console variables for NFRU
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Set console variables for NFRU

The following table summarizes key console variables for Neural Frame Rate Upscaling (NFRU) in Unreal Engine. These variables control enablement, debugging, performance tuning, and frame generation modes. Adjust them to optimize NFRU behavior for your development, testing, and performance needs.

| Console Variable                  | Type | Default Value           | Description                                                                                                  | Notes                   |
|-----------------------------------|------|-------------------------|---------------------------------------------------------------------------------------------------------------|-------------------------|
| r.NFRU.Enable                    | int  | 0                       | Enables NFRU features. To activate NFRU, set this variable to `1`.                                                                                       | —                       |
| r.NFRU.CaptureDebugUI            | int  | 1 (non-shipping builds) | Captures debug UI rendered on the first Slate DrawWindow call to help debug overlays                                              | Non-shipping builds only|
| r.NFRU.UpdateGlobalFrameTime     | int  | 0                       | Includes interpolated frames in global frame time and FPS calculations to ensure performance metrics reflect NFRU's impact                                   | —                       |
| r.NFRU.ModifySlateDeltaTime      | int  | 1                       | Sets Slate's delta time to `0.0` during UI redraws in Slate Redraw UI mode to avoid NativeTick side effects    | Slate Redraw UI mode    |
| r.NFRU.PaceAdjuster              | int  | 0                       | Enables FPS Pace Adjuster for dynamic target FPS adjustment based on real performance for smoother pacing                                           | —                       |
| r.NFRU.UpAdjustFrameCount        | int  | 40                      | Frames above target FPS needed to increase FPS when Pace Adjuster is active. Controls how quickly the Pace Adjuster responds to sustained FPS changes                                  | Requires Pace Adjuster  |
| r.NFRU.DownAdjustFrameCount      | int  | 20                      | Frames below target FPS needed to decrease FPS when Pace Adjuster is active. Controls how quickly the Pace Adjuster responds to sustained FPS changes                                | Requires Pace Adjuster  |
| r.NFRU.DataGraphOpticalFlow      | int  | 1                       | Selects optical flow method. Set the value as `0` for Data Graph to be the preferred method, `1` for Data Graph to be the only method, and `2` for a shader-based approach                 | Unreleased builds only  |
| r.NFRU.DataGraphFrameGeneration  | int  | 1                       | Selects frame generation method. Set the value as `0` for NFRU, `1` for Neural, and `2` for a shader-based approach                                   | Unreleased builds only  |
| r.NFRU.OnlyInterpolatedFrames    | int  | 0                       | Presents only interpolated frames for debugging and validating results                                                              | Dev/Test builds only    |
| r.NFRU.ShowDebugView             | int  | 0                       | Shows debug visualization of frame interpolation                                                             | Dev/Test builds only    |

## Monitor frame generation performance with STATGROUP_FrameGen

NFRU provides the `STATGROUP_FrameGen` statistics group to monitor frame generation performance at runtime. 

Run the following command in the Unreal Engine console:

```bash
stat FrameGen
```

![Screenshot of the Unreal Engine console showing the output of the `stat FrameGen` command, highlighting NFRU performance metrics#center](./images/stat_framegen.png "NFRU performance metrics from stat FrameGen")

This command displays runtime metrics such as generated frame rate, generation time, and pacing information. Use these values to assess both internal frame generation performance and final frame pacing.

| Stat Name       | Stat ID                      | Description |
|-----------------|-----------------------------|-------------|
| Generated FPS   | `STAT_FrameGen_GeneratedFPS` | Frames per second produced by the frame generator (interpolated or generated frames). Should match engine FPS from `stat FPS`. |
| Generated Ms    | `STAT_FrameGen_GeneratedMs`  | Average time (ms) to generate an interpolated frame. Should match the engine’s `FrameTime`. |
| Paced FPS       | `STAT_FrameGen_PacedFPS`     | Presentation-paced FPS, reflecting any swap chain pacing applied to generated frames. Useful for evaluating final upsampled frame rate. |
| Paced Ms        | `STAT_FrameGen_PacedMs`      | Average time (in milliseconds) between paced frame presentations, reflecting wall-clock intervals with pacing or VSync. |

### Interpret frame generation statistics

When reviewing statistics, consider the following:

- Generated FPS and Generated Ms show internal frame generation performance.
- Paced FPS and Paced Ms reflect actual presentation cadence after pacing or synchronization.

Typically, `Generated FPS` matches the engine FPS, while `Paced FPS` might differ if pacing or synchronization limits the display rate.

## What you've accomplished and what's next

You've now learned about the main console variables that control NFRU features in Unreal Engine, including enablement, debugging, and performance tuning. You know how to adjust these variables to optimize NFRU behavior and how to use the `STATGROUP_FrameGen` statistics group to monitor frame generation performance.

Next, you'll explore how to use the debug view to visualize frame interpolation and validate NFRU output during development and testing.
