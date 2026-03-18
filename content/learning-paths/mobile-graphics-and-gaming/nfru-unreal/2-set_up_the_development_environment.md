---
title: Set up the development environment
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Install the required tools and dependencies

To use **Neural Frame Rate Upscaling (NFRU)** in your Unreal Engine project, you need to install and configure several tools. These components provide the development environment and runtime support for building and testing NFRU with **ML extensions for Vulkan**.

Install the following:

- **Vulkan SDK** — Required for developing applications that use Vulkan. It includes the **Vulkan Configurator**, which you use to enable the emulation layers for running ML workloads through Vulkan ML extensions.
    https://vulkan.lunarg.com/

- **CMake** — A build system that configures and generates project build files. You use CMake to build the **Neural Graphics SDK**, which compiles the components and dependencies required by the neural graphics plugins and tools.
    https://cmake.org/

- **neural-graphics-for-unreal** — The Unreal Engine integration for the Neural Graphics Development Kit. This repository contains the **NFRU plugin** and resources you need to integrate neural graphics features into Unreal Engine.
    https://github.com/arm/neural-graphics-for-unreal/tree/main

- **ML Emulation Layer for Vulkan (optional)** — The *neural-graphics-for-unreal* repository includes prebuilt Vulkan ML emulation layers for supported Unreal Engine versions. If you need support for a different version, build the emulation layer from source:
    https://github.com/arm/ai-ml-emulation-layer-for-vulkan

## Install the Vulkan SDK

Download the **Vulkan SDK** from the [Vulkan SDK page](https://vulkan.lunarg.com/sdk/home). Install the version **1.4.321.0 or newer**.

## Install CMake

Download **CMake** from the [CMake website](https://cmake.org/download/). Install the version **3.21 to 3.31**.

## Set up neural-graphics-for-unreal

Clone and set up the **neural-graphics-for-unreal** repository and integrate it with your Unreal Engine project.

1. Clone the repository:

     ```bash
     git clone https://github.com/arm/neural-graphics-for-unreal.git
     cd neural-graphics-for-unreal
     ```

2. Initialize the submodules:

     ```bash
     git submodule update --init
     ```

3. Install Git LFS:

     ```bash
     git lfs install
     ```

4. Download the large files:

     ```bash
     git lfs pull
     ```

5. Select your Unreal Engine version and build the SDK:

     ```bash
     cd [UEVersion]
     BuildSDK.bat
     ```

## Configure Vulkan emulation layers

The **Vulkan Configurator (vkconfig-gui)** is a tool included with the LunarG Vulkan SDK. You use it to manage Vulkan layers and runtime settings. In this section, you enable the **ML emulation layers for Vulkan** to test neural graphics features like **NFRU** during development without hardware with a dedicated neural accelerator.

To emulate the ML extensions for Vulkan:

1. Launch the **Vulkan Configurator** from the Windows **Start** menu.

2. Add a **user-defined Vulkan layer path** to locate the prebuilt Vulkan emulation binaries.

     ![Add user-defined Vulkan layers path in Vulkan Configurator#center](./images/append_user_defined_layer_path.png "Figure 1: Add the prebuilt Vulkan emulation layer path.")

3. Select this folder:

     ```
     neural-graphics-for-unreal/[UEVersion]/Binaries/ThirdParty/VulkanMLEmulation/Win64
     ```

     A **Loading Layer Completed** dialog appears, showing that two layer manifests loaded successfully.

     ![Loading Layer Completed#center](./images/add_prebuilt_vulkan_emulation_layer_path.png "Figure 2: Vulkan emulation layers loaded successfully.")

4. Verify that these layers appear in the list:

     - `VK_LAYER_ML_Graph_Emulation`
     - `VK_LAYER_ML_Tensor_Emulation`

     ![Loaded Layer#center](./images/loaded_layers.png "Figure 3: Loaded Vulkan emulation layers.")

5. Switch to the **Vulkan Loader Management** tab. Ensure the **Graph** layer is listed *above* the **Tensor** layer and configure the layer scope as shown:

     ![Layer configuration showing Graph above Tensor#center](./images/verify_layers.png "Figure 4: Verify layer ordering.")

{{% notice Before you move on %}}
Keep the **Vulkan Configurator** running in the background while you complete the next steps.
{{% /notice %}}

With the ML emulation layers configured, Vulkan runs machine learning workloads using **ML extensions for Vulkan**. Neural inference runs alongside the graphics pipeline during development, even on systems without dedicated neural acceleration hardware.

In the next section, you integrate **NFRU** into an Unreal Engine project. You enable the neural graphics plugin and create a simple example scene to verify the setup and observe NFRU in action.
