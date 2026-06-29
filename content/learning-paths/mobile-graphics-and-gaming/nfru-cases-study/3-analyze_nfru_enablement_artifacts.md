---
title: Validate NFRU with Streamline and RenderDoc
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---
NFRU generates an intermediate frame between two rendered frames. In an ideal static scene, where the camera, objects, lighting, and post-processing remain unchanged, NFRU can produce an intermediate frame that closely matches the expected rendered result with little or no visible quality loss. Real game scenes are more complex. Camera movement, animated characters, particle effects, lighting changes, and fast object motion can affect the accuracy of the generated frame and introduce visible artifacts.

Use Streamline and RenderDoc to validate NFRU from two directions:

- Use Streamline to confirm that NFRU is active, measure the GPU and neural workload, and check whether frame generation fits within the frame budget.
- When visual artifacts appear, use RenderDoc to inspect the frame generation inputs, visible intermediate resources, and final interpolated frame.

## Prepare a repeatable test

Before collecting data, choose a short camera path or gameplay action that can be repeated with NFRU disabled and enabled. Keep the camera path, resolution, graphics settings, and test conditions as consistent as possible.

For Moku, multiple sequences are prepared for demonstration, including 30-second, 5-second, and fixed-camera sequences. Additional test sequences are also created for specific scenarios. Each sequence is treated as a reference cut so that the same content can be replayed consistently across test runs.

![Sample test sequence](./images/sample_test_sequence.gif)

Different device profiles are configured to control whether NFRU is enabled, disabled, or running in debug mode. For example:
```
[Moku_SM5_NoNeural DeviceProfile]
DeviceType=Android
BaseProfileName=Moku_SM5_Base
+CVars=r.NFRU.Enable=0

[Moku_SM5_NFRU DeviceProfile]
DeviceType=Android
BaseProfileName=Moku_SM5_Base
+CVars=r.NFRU.Enable=1

[Moku_SM5_NFRU_Debug DeviceProfile]
DeviceType=Android
BaseProfileName=Moku_SM5_Base
; Development/test builds only
+CVars=r.NFRU.OnlyInterpolatedFrames=1
+CVars=r.NFRU.Enable=1
```

With these profiles, the test can be launched through ADB using a fixed device profile and reference cut:

`
adb shell am start -S -n [package_name]/com.epicgames.unreal.GameActivity --es cmdline '-dp=Moku_SM5_NFRU -referenceCut=TestSequence'
`

For additional visual debugging, use `r.NFRU.ShowDebugView` to display the frame interpolation debug view. Use `r.NFRU.OnlyInterpolatedFrames` when you want to focus only on generated frames. Use `r.NFRU.CaptureDebugUI` when the debug UI or overlays need to be included in the captured path.

`r.NFRU.ShowDebugView` and `r.NFRU.OnlyInterpolatedFrames` are intended for development and test builds, and may not be available in shipping builds.

In NFRU debug resource names, `tm1` means time minus one (`t-1`) and `tp1` means time plus one (`t+1`) relative to the generated frame time. These names may not always match the simpler "previous/current" labels used in comparison images.


## Profile NFRU with Streamline

Use Streamline to compare the same scene with NFRU disabled and enabled. In the NFRU-enabled capture, confirm that the neural processing counters are active, and check that the additional GPU work, such as compute activity and memory bandwidth, fits within the frame budget.

As shown in the capture, counters such as Neural queue active and Neural Accelerator Unit Usage are active. This indicates neural accelerator activity during the NFRU workload. You can use the measured active time from these counters to evaluate the performance cost of NFRU. Moku also integrates the Streamline API, so Streamline captures can record both render FPS and present FPS at the same time.

![Moku Streamline FPS](./images/streamline/moku_streamline_fps.png)

On the timeline, the NFRU workload should complete cleanly between real rendered frames. If GPU or neural processing blocks become long, the cost of NFRU may limit the expected uplift. If the workload is light but idle gaps still appear, the limiting factor is more likely frame pacing or presentation behavior rather than NFRU execution cost. For a deeper explanation, see [NFRU performance](/learning-paths/mobile-graphics-and-gaming/nfru-cases-study/8-nfru_performance/).

![Moku Streamline neural usage](./images/streamline/moku_streamline_neural_usage.png)

For more information on performance profiling strategies, refer to the [Streamline](/learning-paths/mobile-graphics-and-gaming/ams/streamline/).

## Inspect NFRU frames with RenderDoc

Use RenderDoc when NFRU is active but the generated frames show visual artifacts. Capture a frame with NFRU enabled and inspect the frame generation area of the event list. Compare the real frame copies with the generated output, then review the bound frame-generation resources and debug-view tiles that expose motion, depth, disocclusion, and warped-color behavior. If the real frame inputs look correct but the generated output has artifacts, the issue is likely in frame generation, masking, disocclusion handling, or content such as fast alpha-blended effects.

For detailed guidance on using RenderDoc with NFRU in Unreal Engine, refer to the [RenderDoc integration guide](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/7-renderdoc/).

![Moku RenderDoc NFRU inspection](./images/moku_renderdoc.png)


This workflow is useful for the artifact scenarios in the following sections. Fast camera movement tends to expose disocclusion and edge reconstruction problems. Fast object motion stresses motion vectors and object boundaries. Occlusion changes stress depth history. Alpha-blended particles and VFX stress content that does not always have reliable depth or motion vector data.

## What you've learned and what's next

In this section, you learned how to validate NFRU using Streamline and RenderDoc. Streamline confirms whether NFRU is active, how much GPU and neural workload it adds, and whether pacing or processing cost limits the expected FPS uplift. RenderDoc lets you inspect the frame-generation event list, visible NFRU resources, real frame copies, debug-view output, and final generated output when visual artifacts need deeper analysis.

You are now prepared to evaluate NFRU performance and visual quality in representative gameplay scenarios.
