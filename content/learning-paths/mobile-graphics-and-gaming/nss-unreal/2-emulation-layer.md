---
title: Setting up the emulation layers
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install dependencies

To run NSS in your Unreal Engine project, you will need to install and configure the following:

- **Vulkan SDK**: Required for development of applications that use Vulkan, and to enable the Vulkan Configurator. The latter sets up the emulation layers used for running ML extensions for Vulkan workloads.
- **ML Emulation Layer for Vulkan**: These layers allows neural inference to run in emulation through Vulkan’s compute backend. They are activated by Vulkan Configurator to run with the Unreal Engine plugin. The Vulkan layer configuration activates the ML Emulation Layer for Vulkan, which implements the ML extensions for Vulkan.
- **NSS for Unreal Engine plugin**: You will download and integrate the plugin in the next section.

These components allow you to run NSS in Unreal Engine, using ML emulation layers for Vulkan for development and testing.

## Install Vulkan Software Development Kit

Go to the [Vulkan SDK landing page](https://vulkan.lunarg.com/sdk/home) and download the SDK Installer for Windows. After you have run the installer, you can move on to the next step.

## Download the emulation layers

For this Learning Path, a pre-built of package of the emulation layers is available. Download them by clicking the link.

[**ML Emulation Layer for Vulkan** → Arm Developer Downloads](https://www.arm.com/-/media/Files/developer/MLEmulationLayerForVulkan20251107)

Extract the downloaded file in a location of your choice.


## Configure Vulkan Layers

Vulkan Configurator is a program that will run the emulation layers in the background when you want to utilize them with Unreal Engine.

To emulate the ML extensions for Vulkan:
1. Launch the **Vulkan Configurator** (bundled with the Vulkan SDK) from the Windows **Start** menu.
2. In the **Apply a Vulkan Loader Configuration** list, right-click and choose **Create a new Configuration**. You can give the new configuration any name, for example `NSS`.
3. Navigate to the **Vulkan Layers Location** tab.
4. Append a user-defined path pointing to the emulation layers you downloaded in the previous step:
   ```
   <download-path>/MLEmulationLayerForVulkan20251107
   ```
![Add user-defined Vulkan layers path in Vulkan Configurator#center](./images/load_layers.png "Figure 1: Add Vulkan layer path.")

5. Switch back to the **Vulkan Loader Management** tab. Ensure the Graph layer is listed *above* the Tensor layer, and that you've set up the configuration scope as shown in the image.

![Layer configuration showing Graph above Tensor#center](./images/verify_layers.png "Figure 2: Verify layer ordering and scope.")

{{% notice Before you move on %}}
Make sure you keep Vulkan Configurator running in the background as you go through the next steps.
{{% /notice %}}

With the ML emulation layers configured, Vulkan is now able to run machine learning workloads through the ML extensions for Vulkan. This enables neural inference to execute alongside the graphics pipeline during development, without requiring access to hardware with dedicated neural accelerators.

The next step is to integrate Neural Super Sampling into an Unreal Engine project. You’ll do this by installing the NSS plugin and creating a simple example game that lets you verify the setup and visualize the upscaling in action.