---
title: Run the example
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Start the level and verify NSS

Press the green **Play** button to start the level. To verify NSS is running, you can run this command in Unreal:
   ```
   ShowFlag.VisualizeTemporalUpscaler 1
   ```
You’ll see **NSS** listed in the rendering summary.

{{% notice %}}
In **Project Settings > Plugins > Neural Super Sampling**, you can view and configure the active neural network model being used.
{{% /notice %}}

Run `ShowFlag.VisualizeTemporalUpscaler 0` to disable the overview. To visualize the NSS model output in real-time, run the following command:
   ```
   r.NSS.Debug 1
   ```

This will add real-time views showing the model’s processed outputs, such as predicted filter coefficients and feedback, as below. In the [Wrapping up section](/learning-paths/mobile-graphics-and-gaming/nss-unreal/6-wrapping-up), you will find links to learn more about what the debug outputs mean.

![Debug view of Neural Super Sampling model output in Unreal Engine#center](./images/nss_debug.png "Figure 6: Visualize NSS model debug output in real time.")

## Troubleshooting tips

If the example does not behave as expected, check the following common issues before continuing.

### Check for build issues in Visual Studio
- Build failures related to `AutomationTool`, `Gauntlet`, or other `*.Automation` projects can be ignored.
- Focus on whether the project itself, named as `<Your Project Name>Editor`, builds successfully.

### Check you Unreal Engine configuration
- Verify that Vulkan is selected as the **Default RHI**.
- Confirm the NSS plugin is enabled and that Unreal Engine was restarted after enabling it.
- Check **Project Settings → Plugins → Neural Super Sampling** to confirm a model is selected and active.

If the NSS plugin is enabled but appears to have no effect:
- Ensure Vulkan Configurator is running.
- Verify that the correct layer configuration is selected and active.
- Double-check that:
  - The emulation layer path is correct
  - The Graph layer is ordered above the Tensor layer

Refer back to the [emulation layer section](/learning-paths/mobile-graphics-and-gaming/nss-unreal/2-emulation-layer/) for the full Vulkan Configurator setup and validation steps.

### Check the software and hardware setup
- Confirm that the plugin version exactly matches your Unreal Engine version.
- Verify that your GPU driver supports Vulkan.
- Verify that your Visual Studio version aligns with the Unreal Engine version you are using.
- Return to the Visual Studio build output and inspect the logs carefully to identify the first reported error

Build or startup failures are often caused by version mismatches or missing dependencies.

## NSS model on Hugging Face

The model that powers NSS is published on Hugging Face in the [VGF format](https://github.com/arm/ai-ml-sdk-vgf-library). This format is optimized for inference via ML extensions for Vulkan.

Visit the [NSS model page on Hugging Face](https://huggingface.co/Arm/neural-super-sampling/)

On this landing page, you can read more about the model, and learn how to run a test case - a _scenario_ - using the ML SDK for Vulkan.

## Result

You now have Neural Super Sampling integrated and running inside Unreal Engine. This setup provides a real-time testbed for neural upscaling.

Proceed to the next section to debug your frames using RenderDoc, or move on to the final section to explore more resources on the technology behind NSS.
