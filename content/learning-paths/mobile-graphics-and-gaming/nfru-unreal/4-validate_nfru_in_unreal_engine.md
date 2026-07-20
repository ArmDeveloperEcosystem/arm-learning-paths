---
title: Validate NFRU in Unreal Engine
description: Run NFRU in Unreal Engine Standalone Game mode, confirm its debug output, and troubleshoot common Vulkan emulation and plugin issues.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Start the level and validate NFRU

Neural Frame Rate Upscaling (NFRU) isn't supported in the standard Unreal Engine viewport. Use **Standalone Game** mode or create a packaged build to activate NFRU in a runtime environment and test features.

![Standalone game mode in Unreal Engine editor showing the Play dropdown set to "Standalone Game"#center](./images/standalone_game.png "Use Standalone Game mode to test NFRU")

When you switch to **Standalone Game** mode, the **Play** button changes appearance.

![Green Play button in Unreal Engine editor, indicating Standalone Game mode is active#center](./images/play_in_new_window.png "Play button when Standalone Game mode is active")

Select the green **Play** button to launch the level in a new window.

To confirm NFRU is running, enter the following commands in Unreal:

```console
r.NFRU.Enable 1
r.NFRU.ShowDebugView 1
```

You'll see the NFRU debug visualization, which confirms the feature is active during gameplay.

![NFRU debug view in Standalone Game showing tiled depth, disocclusion, motion-warped, and optical-flow outputs, confirming that the debug visualization is active#center](./images/nfru_debug_runtime.png "NFRU debug output during runtime")

For more details about the debug outputs, see the [Debug view section](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/6-debug_view).

## Troubleshoot issues with the game

If the game doesn't behave as expected, consider the following:

### Game crash

A crash after enabling NFRU usually indicates a misconfigured Vulkan emulation layer.

![Unreal Engine Crash Reporter for NFRU_Sample showing stack entries from `UnrealEditor_NFRU` after launch#center](./images/nfru_play_crash.png "Crash Reporter after an NFRU launch failure")

Open the **Modules** window in Visual Studio while the game runs. Check that the emulation layer DLL loads from the correct path. If not, update your configuration and restart Unreal Engine.

### Unreal Engine configuration

If the plugin is enabled but not working:

- Start Vulkan Configurator and confirm it is running
- Ensure the correct layer configuration is active
- Check the emulation layer path
- Confirm the Graph layer comes before the Tensor layer

For detailed setup steps, see the [emulation layer section](/learning-paths/mobile-graphics-and-gaming/nfru-unreal/2-set_up_the_development_environment/).

### Software and hardware setup

If there are issues with software and hardware setup:

- Ensure the NFRU plugin version matches your Unreal Engine version
- Confirm your GPU driver supports Vulkan
- Verify Visual Studio is compatible with your Unreal Engine version
- Review build output and logs for errors

Version mismatches or missing dependencies cause most build or startup issues.

## What you've accomplished and what's next

You've now validated NFRU in a runtime environment using Unreal Engine, confirmed its activation, and learned how to resolve common troubleshooting scenarios. 

Next, you'll explore built-in NFRU console variables to further customize and analyze performance.
