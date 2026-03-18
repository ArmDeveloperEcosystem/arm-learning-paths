---
title: Console Variables for NFRU
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Available console variables

The following table summarizes key console variables for NFRU (Neural Frame Rate Upscaling) in Unreal Engine. These variables control enablement, debugging, performance tuning, and frame generation modes. Adjust them to optimize NFRU behavior for your development, testing, and performance needs.

| Console Variable                  | Type | Default Value           | Description                                                                                                   | Notes                   |
|-----------------------------------|------|-------------------------|---------------------------------------------------------------------------------------------------------------|-------------------------|
| r.NFRU.Enable                    | int  | 0                       | Enables NFRU features.                                                                                        | —                       |
| r.NFRU.CaptureDebugUI            | int  | 1 (non-shipping builds) | Captures debug UI rendered on the first Slate DrawWindow call.                                                | Non-shipping builds only|
| r.NFRU.UpdateGlobalFrameTime     | int  | 0                       | Includes interpolated frames in global frame time and FPS calculations.                                       | —                       |
| r.NFRU.ModifySlateDeltaTime      | int  | 1                       | Sets Slate's delta time to 0.0 during UI redraws in Slate Redraw UI mode to avoid NativeTick side effects.    | Slate Redraw UI mode    |
| r.NFRU.PaceAdjuster              | int  | 0                       | Enables FPS Pace Adjuster for dynamic target FPS adjustment.                                                  | —                       |
| r.NFRU.UpAdjustFrameCount        | int  | 40                      | Frames above target FPS needed to increase FPS when Pace Adjuster is active.                                  | Requires Pace Adjuster  |
| r.NFRU.DownAdjustFrameCount      | int  | 20                      | Frames below target FPS needed to decrease FPS when Pace Adjuster is active.                                  | Requires Pace Adjuster  |
| r.NFRU.DataGraphOpticalFlow      | int  | 1                       | Selects optical flow method: 0 = Data Graph preferred, 1 = Data Graph only, 2 = Shader-based.                 | Unreleased builds only  |
| r.NFRU.DataGraphFrameGeneration  | int  | 1                       | Selects frame generation: 0 = NFRU preferred, 1 = Neural, 2 = Shader-based.                                   | Unreleased builds only  |
| r.NFRU.OnlyInterpolatedFrames    | int  | 0                       | Presents only interpolated frames for debugging.                                                              | Dev/Test builds only    |
| r.NFRU.ShowDebugView             | int  | 0                       | Shows debug visualization of frame interpolation.                                                             | Dev/Test builds only    |

### Variable details

Set `r.NFRU.Enable` to `1` to activate NFRU. Use `r.NFRU.CaptureDebugUI` to capture debug UI elements during the first Slate DrawWindow call, which helps you debug overlays in non-shipping builds.

Enable `r.NFRU.UpdateGlobalFrameTime` to ensure performance metrics reflect NFRU's impact by including interpolated frames in calculations. In Slate Redraw UI mode, `r.NFRU.ModifySlateDeltaTime` prevents unwanted side effects by setting Slate's delta time to zero during UI updates.

Use `r.NFRU.PaceAdjuster` to dynamically adjust target FPS based on real-time performance for smoother pacing. Tune `r.NFRU.UpAdjustFrameCount` and `r.NFRU.DownAdjustFrameCount` to control how quickly the Pace Adjuster responds to sustained FPS changes.

`r.NFRU.DataGraphOpticalFlow` and `r.NFRU.DataGraphFrameGeneration` let you choose between optical flow and frame generation methods. These variables are intended for unreleased builds only.

Set `r.NFRU.OnlyInterpolatedFrames` to present only interpolated frames, which helps you debug and validate your results. Use `r.NFRU.ShowDebugView` to display a debug visualization of frame interpolation in development or test builds.

## Using STAT_FrameGen

NFRU provides the `STATGROUP_FrameGen` statistics group to monitor frame generation performance at runtime. Enter the following command in the Unreal Engine console:

```bash
stat FrameGen
```

![Screenshot of the Unreal Engine console showing the output of the `stat FrameGen` command, highlighting NFRU performance metrics#center](./images/stat_framegen.png "Figure 1: NFRU performance metrics using stat FrameGen")

This command displays runtime metrics such as generated frame rate, generation time, and pacing information. These values help you assess both internal frame generation performance and final frame pacing.

| Stat Name       | Stat ID                      | Description |
|-----------------|-----------------------------|-------------|
| Generated FPS   | `STAT_FrameGen_GeneratedFPS` | Frames per second produced by the frame generator (interpolated/generated frames). Should match engine FPS from `stat FPS`. |
| Generated Ms    | `STAT_FrameGen_GeneratedMs`  | Average time (ms) to generate an interpolated frame. Should match the engine’s `FrameTime`. |
| Paced FPS       | `STAT_FrameGen_PacedFPS`     | Presentation-paced FPS, reflecting any swap chain pacing applied to generated frames. Useful for evaluating final upsampled frame rate. |
| Paced Ms        | `STAT_FrameGen_PacedMs`      | Average time (ms) between paced frame presentations, reflecting wall-clock intervals with pacing or VSync. |

### Interpreting statistics

- **Generated FPS / Generated Ms**: Show internal frame generation performance.
- **Paced FPS / Paced Ms**: Reflect actual presentation cadence after pacing or synchronization.

Typically, `Generated FPS` matches the engine FPS, while `Paced FPS` may differ if pacing or synchronization limits the display rate.


## What you've accomplished and what's next

You've learned about the main console variables that control NFRU features in Unreal Engine, including enablement, debugging, and performance tuning. You now know how to adjust these variables to optimize NFRU behavior and how to use the `STAT_FrameGen` statistics group to monitor frame generation performance.

Next, you'll explore how to use the debug view to visualize frame interpolation and validate NFRU output during development and testing.

