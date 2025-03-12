---
title: Using Arm ASR in a custom engine with the Universal SDK
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

Use the following steps to implement **Arm Accuracy Super-Resolution** in your own custome engine. Arm ASR is an optimized version of [Fidelity Super Resolution 2](https://github.com/GPUOpen-LibrariesAndSDKs/FidelityFX-SDK/blob/main/docs/techniques/super-resolution-temporal.md) that has been heavily modified to included many mobile-oriented optimizations to make the technique suited for mobile.

There are two ways you can integrate Arm ASR into your custom engine:

- [Quick integration](#quick-integration) - using the built-in standalone backend.
- [Tight integration](#tight-integration) - using your own backend/renderer.

## Quick integration

To quickly integrate Arm ASR, which means the built-in standalone backend is used, follow the steps below:

1. Get the Arm ASR package from GitHub:

    ```
    git clone https://github.com/arm/accuracy-super-resolution-universal-sdk
    ```
1. For the purposes of this tutorial, we will set a variable to identify the location of the Arm ASR package. This path will be used to refer to files in the repository throughout this learning path.

    ```
    export $ARMASR_DIR=$(pwd)
    ```

1. Copy the **Arm_ASR** directory into your project, and add **Arm_ASR/src/backends/shared/blob_accessors/prebuilt_shaders** in the incude path if you want to use prebuilt shaders.

1. Include the following header files in your codebase where you wish to interact with the technique:
    
    - `$ARMASR_DIR/include/host/ffxm_fsr2.h#L1`
    - `$ARMASR_DIR/include/host/backends/vk/ffxm_vk.h#L1`

1. Create a Vulkan backend.
    - Allocate a Vulkan scratch buffer of the size returned by `$ARMASR_DIR/include/host/backends/vk/ffxm_vk.h#L65`.
    - Create `FfxmDevice` via `$ARMASR_DIR/include/host/backends/vk/ffxm_vk.h#L65`.
    - Create `FfxmInterface` by calling `$ARMASR_DIR/include/host/backends/vk/ffxm_vk.h#L99`.

1. Create a context by calling `ffxmFsr2ContextCreate` accessed via `$ARMASR_DIR/include/host/ffxm_fsr2.h#L296`. The parameters structure should be filled out matching the configuration of your application.

1. Each frame call `ffxmFsr2ContextDispatch` via `$ARMASR_DIR/include/host/ffxm_fsr2.h#L337' to record/execute the technique's workloads. The parameters structure should be filled out matching the configuration of your application.

1. When your application is terminating (or you wish to destroy the context for another reason) you should call `ffxmFsr2ContextDestroy` accessed via `$ARMASR_DIR/include/host/ffxm_fsr2.h#L360`. The GPU should be idle before calling this function.

1. Sub-pixel jittering should be applied to your application's projection matrix. This should be done when performing the main rendering of your application. You should use the `ffxmFsr2GetJitterOffset` function accessed via `$ARMASR_DIR/include/host/ffxm_fsr2.h#L504` to compute the precise jitter offsets.

1. A global mip bias should be applied when texturing.

1. For the best upscaling quality it is strongly advised that you populate the Reactive mask according to our guidelines. You can also use `ffxmFsr2ContextGenerateReactiveMask` accessed via `$ARMASR_DIR/include/host/ffxm_fsr2.h#L348` as a starting point.

1. Finally, link the two built libraries (**Arm_ASR_api** and **Arm_ASR_backend**).

## Tight integration

If you wish to use your own backend/renderer, a tight integration with your engine is required. For this, a similar process to the [quick integration](#quick-integration) described above is required, but with the added requirement to fill the `FfxmInterface` accessed via `$ARMASR_DIR/include/host/ffxm_interface.h#L438` with functions implemented on your end.

In this approach the shaders are expected to be built by the engine. Arm ASR's shaders have been micro-optimized to use explicit 16-bit floating-point types so it is advisable that the shaders are built using such types (for example,  `min16float` in hlsl or `float16_t` in glsl). For this you should define the symbols `#define FFXM_HLSL_6_2 1` and `#define FFXM_HALF 1` (FFXM_HALF is already defined in the provided shader sources) enabled with a value of `1`.

1. Include the `ffxm_interface.h` header file from `$ARMASR_DIR/include/host/ffxm_interface.h#L1` in your codebase.

1. Implement your own functions (assume the names are `xxxGetInterfacexxx`, `xxxGetScratchMemorySizexxx`) and callbacks in `FfxmInterface` accessed via `$ARMASR_DIR/include/host/ffxm_interface.h#L438` to link Arm ASR with the engine's renderer.

1. Create your own backend by calling `xxxGetInterfacexxx`. A scratch buffer should be allocated of the size returned by calling `xxxGetScratchMemorySizexxx` and the pointer to that buffer passed to `xxxGetInterfacexxx`.

1. Now, you can follow the same steps from quick integration above, starting from step 6, creating a Arm ASR context. In the final step it is only necessary to link the **Arm_ASR_api** library.

### HLSL-based workflows

In an HLSL-based workflow using DirectX Shader Compiler to cross-compile to SPIRV do the following:

- Use the following flags when building:

    ```
    -fspv-target-env=vulkan1.1spirv1.4 -enable-16bit-types
    ```

- The extension **VK_KHR_shader_float16_int8** should be used at runtime.
