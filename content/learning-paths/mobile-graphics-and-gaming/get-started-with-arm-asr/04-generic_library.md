---
title: Using Arm ASR in a Custom Engine using the Generic Library
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction

Follow these steps to implement **Arm Accuracy Super Resolution (Arm ASR)** in your custom engine.

Arm ASR is an optimized variant of Fidelity Super Resolution 2 (FSR2) that includes extensive mobile-specific optimizations, ensuring high performance on mobile devices.

You can integrate Arm ASR into your custom engine using one of two methods:

1. [Quick Integration](#quick-integration) - use the standalone backend.
2. [Tight Integration](#tight-integration) - use your engine's backend/renderer.

See the following sections to learn how to configure Arm ASR:

- [Quality presets](#quality-presets).
- [Shader variants and extensions](#shader-variants-and-extensions).
- [Input resources](#input-resources).
- [Providing motion vectors](#providing-motion-vectors).
- [Reactive mask](#reactive-mask).
- [Automatically generating reactivity](#automatically-generating-reactivity).
- [Modular backend](#modular-backend).
- [Camera jitter](#camera-jitter).
- [Camera jump cuts](#camera-jump-cuts).
- [Mipmap biasing](#mipmap-biasing).
- [Frame time delta input](#frame-time-delta-input).
- [HDR support](#hdr-support).
- [API debug checker](#debug-checker).
- [Extended ffx_shader_compiler](#extended-ffx_shader_compiler).
- [Generate prebuilt shaders](#generate-prebuilt-shaders).

## Get the Arm ASR package

1. Get the Arm ASR package from GitHub:

    ```
    git clone https://github.com/arm/accuracy-super-resolution-generic-library
    cd accuracy-super-resolution-generic-library
    ```

2. Set a variable for the package location for easy reference.

    You will use this path to refer to files in the repository:

    ```
    export ARMASR_DIR=$(pwd)
    ```

## Quick Integration

To quickly integrate Arm ASR using the standalone backend, follow these steps below:

1. Copy the **Arm_ASR** directory into your project, and add `Arm_ASR/src/backends/shared/blob_accessors/prebuilt_shaders` to your include path to use prebuilt shaders.

2. Include the following header files in your code:
    - `$ARMASR_DIR/include/host/ffxm_fsr2.h`
    - `$ARMASR_DIR/include/host/backends/vk/ffxm_vk.h`



3. Create a Vulkan backend by:

    - Allocating a Vulkan scratch buffer of the size returned by `ffxmGetScratchMemorySizeVK` (defined in `$ARMASR_DIR/include/host/backends/vk/ffxm_vk.h`).
    - Creating a `FfxmDevice` using `ffxmGetDeviceVK`.
    - Creating a `FfxmInterface` using `ffxmGetInterfaceVK`.


4. Create a context by calling `ffxmFsr2ContextCreate` from `$ARMASR_DIR/include/host/ffxm_fsr2.h`. Ensure the parameters structure matches the configuration of your application.

5. Call `ffxmFsr2ContextDispatch` every frame to record and execute workloads. Again, the parameters structure should match the configuration of your application.

6. When your application is terminating (or you wish to destroy the context for another reason) you should call `ffxmFsr2ContextDestroy` accessed via `$ARMASR_DIR/include/host/ffxm_fsr2.h`. The GPU should be idle before calling this function.

7. Sub-pixel jittering should be applied to your application's projection matrix. This should be done when performing the main rendering of your application. You should use the `ffxmFsr2GetJitterOffset` function accessed via `$ARMASR_DIR/include/host/ffxm_fsr2.h` to compute the precise jitter offsets.

8. A global Mip bias should be applied when texturing. Applying a negative Mipmap biasing will typically generate an upscaled image with better texture detail. We recommend applying the following formula to your Mipmap bias:

    ``` cpp
    mipBias = log2(renderResolution/displayResolution) - 1.0;
    ```

9. For the best upscaling quality it is strongly advised that you populate the Reactive mask according to our guidelines. You can also use `ffxmFsr2ContextGenerateReactiveMask` accessed via `$ARMASR_DIR/include/host/ffxm_fsr2.h` as a starting point.

10. Finally, link the two built libraries (**Arm_ASR_api** and **Arm_ASR_backend**).

## Tight Integration

If you wish to use your own backend/renderer, a tight integration with your engine is required. For this, a similar process to the [Quick Integration](#quick-integration) described above is required, but with the added requirement to fill the `FfxmInterface` accessed via `$ARMASR_DIR/include/host/ffxm_interface.h` with functions implemented on your end.

In this approach the shaders are expected to be built by the engine. Arm ASR's shaders have been micro-optimized to use explicit 16-bit floating-point types. It is therefore advisable that the shaders are built using such types. For example,  `min16float` is used in High-level shader language (HLSL) and `float16_t` in OpenGL Shading Language (GLSL). If you are using HLSL, define the following symbol with a value of `1`:

```cpp
#define FFXM_HLSL_6_2 1
```

The `FFXM_HALF` symbol is enabled by default in the provided shader sources.

1. Include the following header in your codebase:

    - `$ARMASR_DIR/include/host/ffxm_interface.h`

2. Implement your own functions (assume the names are `xxxGetInterfacexxx`, `xxxGetScratchMemorySizexxx`) and callbacks in `FfxmInterface` in `$ARMASR_DIR/include/host/ffxm_interface.h` to link Arm ASR with the engine's renderer.

3. Create your own backend by calling `xxxGetInterfacexxx`. A scratch buffer should be allocated of the size returned by calling `xxxGetScratchMemorySizexxx` and the pointer to that buffer passed to `xxxGetInterfacexxx`.

4. Now, you can follow the same steps from the quick integration instructions above, starting from step 4, creating an Arm ASR context. In the final step it is only necessary to link the **Arm_ASR_api** library.

## Integration Guidelines

In the following section, additional details for integrating Arm ASR are listed.

{{% notice %}}
The `FfxmFsr2ContextDescription` from `$ARMASR_DIR/include/host/ffxm_fsr2.h` is referenced multiple times throughout the Integration Guidelines. You should configure the `flags` field of this structure when modifying those bits, by setting the variables in `FfxmFsr2InitializationFlagBits`.
{{% /notice %}}

### HLSL-Based Workflows

In an HLSL-based workflow using DirectX Shader Compiler to cross-compile to SPIR-V do the following:

- Use the following flags when building:

    ```
    -fspv-target-env=vulkan1.1spirv1.4 -enable-16bit-types
    ```

- The extension **VK_KHR_shader_float16_int8** should be used at runtime.

## Quality Presets

The Arm ASR API provides a set of shader quality presets, to select a version of the technique that balances  quality and performance:

| Preset      | Description |
|------------|-------------|
| **Quality**   | An optimized version of FSR2 that maintains the same image quality as the original technique. |
| **Balanced**  | Provides significant bandwidth savings and performance uplift while maintaining image quality close to the **Quality** preset. |
| **Performance** | A more aggressive preset that offers the highest performance with some quality sacrifices. |

When creating a context, a `FfxmFsr2ShaderQualityMode` accessed via `$ARMASR_DIR/include/host/ffxm_fsr2.h` needs to be provided as part of the input settings in `FfxmFsr2ContextDescription`.

## Upscaling Ratios

To enhance flexibility when using the technique, developers can specify both a shader quality preset and an upscaling ratio. They can select any combination of **FfxmFsr2ShaderQualityMode** and **FfxmFsr2UpscalingRatio** according to their requirements to adjust the balance between quality and performance of the application.


A couple of utilities are available to determine the source resolution the frame should use for rendering before upscaling. This calculation is based on the desired upscaling ratio, defined by `FfxmFsr2UpscalingRatio`. You can find this definition in `$ARMASR_DIR/include/host/ffxm_fsr2.h`.

``` cpp
float ffxmFsr2GetUpscaleRatioFactor(FfxmFsr2UpscalingRatio upscalingRatio)
FfxErrorCode ffxmFsr2GetRenderResolutionFromUpscalingRatio(
    uint32_t* renderWidth,
    uint32_t* renderHeight,
    uint32_t displayWidth,
    uint32_t displayHeight,
    FfxmFsr2UpscalingRatio upscalingRatio)
```

## Shader Variants and Extensions

**Unless you are using the prebuilt shaders with the standalone VK backend**, be aware of the following definitions when integrating Arm ASR shaders:

- **FFXM_GPU**. Needs to be defined globally when including the shader headers.
- **FFXM_HLSL**. If defined, the logic falls back to use the **HLSL**-specific syntax, such as types and resource declaration.
- **FFXM_GLSL**. If defined, the logic falls back to use the **GLSL**-specific syntax.

The following table shows the list of the different shader mutators that you can use. All of these must be defined with a value of 0 or 1. The shader variant to use is determined internally by the **getPipelinePermutationFlags(...)** function, based on factors such as user-defined flags and shader quality settings.

| Define | Description |
| -------- | ------- |
| FFXM_FSR2_OPTION_HDR_COLOR_INPUT | If **1**, assumes that the input color is in linear RGB. |
| FFXM_FSR2_OPTION_LOW_RESOLUTION_MOTION_VECTORS | If **1**, assumes the input motion vectors texture is in low resolution |
| FFXM_FSR2_OPTION_JITTERED_MOTION_VECTORS | If **1**, assumes jittered motion vectors using the same jitter offsets as the input color and depth. |
| FFXM_FSR2_OPTION_INVERTED_DEPTH | If **1**, assumes the input depth containing reversed depth values (far == 0.0f) |
| FFXM_FSR2_OPTION_APPLY_SHARPENING | If **1**, informs the shaders that RCAS (sharpening) pass will be used. |
| FFXM_FSR2_OPTION_SHADER_OPT_BALANCED | If **1**, enables a batch of optimizations when the **Balanced** quality preset is selected. |
| FFXM_FSR2_OPTION_SHADER_OPT_PERFORMANCE | If **1**,  enables a batch of optimizations when the **Performance** quality preset is selected. When this is enabled, then **FFXM_FSR2_OPTION_SHADER_OPT_BALANCED** is enabled too. |

Lastly, when using an HLSL-based workflow, you also have the **FFXM_HLSL_6_2** global define. If defined with a value of **1**, this will enable the use of explicit 16-bit types instead of relying on **half** (RelaxedPrecision). The **VK_KHR_shader_float16_int8** extension is required on Vulkan.

## Input Resources

Arm ASR is a temporal algorithm, and therefore requires access to data from both the current and previous frame. The following table enumerates all external inputs required by it, with most function names available in `$ARMASR_DIR/include/host/ffxm_fsr2.h`.

The resolution column indicates if the data should be at 'rendered' resolution or 'presentation' resolution. 'Rendered' resolution indicates that the resource should match the resolution at which the application is performing its rendering. Conversely, 'presentation' indicates that the resolution of the target should match that which is to be presented to the user. All resources are from the current rendered frame, for Vulkan applications all input resources should be transitioned to [`VK_ACCESS_SHADER_READ_BIT`](https://www.khronos.org/registry/vulkan/specs/1.3-extensions/man/html/VkAccessFlagBits.html) respectively before calling `ffxmFsr2ContextDispatch`.

| Name            | Resolution                   |  Format                            | Type      | Notes                                          |
| ----------------|------------------------------|------------------------------------|-----------|------------------------------------------------|
| Color buffer    | Render                       | `APPLICATION SPECIFIED`            | Texture   | The current frame's color data. If HDR, enable `FFXM_FSR2_ENABLE_HIGH_DYNAMIC_RANGE` in `FfxmFsr2ContextDescription`. |
| Depth buffer    | Render                       | `APPLICATION SPECIFIED (1x FLOAT)` | Texture   | The depth buffer for the current frame. The data should be provided as a single floating point value, the precision of which is under the application's control. Configure the depth through the `FfxmFsr2ContextDescription` when creating the `FfxmFsr2Context`. If the buffer is inverted, set `FFXM_FSR2_ENABLE_DEPTH_INVERTED` flag ([1..0] range). If the buffer has an infinite far plane, set the `FFXM_FSR2_ENABLE_DEPTH_INFINITE`. If the application provides the depth buffer in `D32S8` format, then it will ignore the stencil component of the buffer, and create an `R32_FLOAT` resource to address the depth buffer. |
| Motion vectors  | Render or presentation       | `APPLICATION SPECIFIED (2x FLOAT)` | Texture   | The 2D motion vectors for the current frame, in **[<-width, -height> ... <width, height>]** range. If your application renders motion vectors with a different range, you may use the `motionVectorScale` field of the `FfxmFsr2DispatchDescription` structure to adjust them to match the expected range for Arm ASR. Internally, Arm ASR uses 16-bit quantities to represent motion vectors in many cases, which means that while motion vectors with greater precision can be provided, Arm ASR will not benefit from the increased precision. The resolution of the motion vector buffer should be equal to the render resolution, unless the `FFXM_FSR2_ENABLE_DISPLAY_RESOLUTION_MOTION_VECTORS` flag is set when creating the `FfxmFsr2Context`, in which case it should be equal to the presentation resolution. |
| Reactive mask   | Render                       | `R8_UNORM`                         | Texture   | As some areas of a rendered image do not leave a footprint in the depth buffer or include motion vectors, Arm ASR provides support for a reactive mask texture.  This can be used to indicate to the technique where such areas are. Good examples of these are particles, or alpha-blended objects which do not write depth or motion vectors. If this resource is not set, then Arm ASR's shading change detection logic will handle these cases as best it can, but for optimal results, this resource should be set. For more information on the reactive mask please refer to the [Reactive mask](#reactive-mask) section.  |
| Exposure        | 1x1                          | `R32_FLOAT/ R16_FLOAT`                        | Texture   | The exposure value computed for the current frame. This resource may be omitted if the `FFXM_FSR2_ENABLE_AUTO_EXPOSURE` flag in the `FfxmFsr2ContextDescription` structure when creating `FfxmFsr2Context`.  |

All inputs that are provided at Render Resolution, except for motion vectors, should be rendered with jitter. By default, Motion vectors are expected to be unjittered unless the `FFXM_FSR2_ENABLE_MOTION_VECTORS_JITTER_CANCELLATION` flag is present.

## Providing Motion Vectors

### Space

A key part of a temporal algorithm (be it antialiasing or upscaling) is the provision of motion vectors. Arm ASR accepts motion vectors in 2D which encode the motion from a pixel in the current frame to the position of that same pixel in the previous frame. It expects that motion vectors are provided by the application in [**<-width, -height>**..**<width, height>**] range; this matches Screen-Space. For example, a motion vector for a pixel in the upper-left corner of the screen with a value of `<width, height>` would represent a motion that traversed the full width and height of the input surfaces, originating from the bottom-right corner.

If your application computes motion vectors in another space - for example normalized device coordinate space - then you may use the `motionVectorScale` (`$ARMASR_DIR/include/host/ffxm_fsr2.h`) field of the `FfxmFsr2DispatchDescription` structure to instruct the technique to adjust them to match the expected range. The code examples below illustrate how motion vectors may be scaled to screen space. The example HLSL and C++ code below illustrates how NDC-space motion vectors can be scaled using the Arm ASR host API.

GPU: Example of application NDC motion vector computation
```output
float2 motionVector = (previousPosition.xy / previousPosition.w) \
                    - (currentPosition.xy / currentPosition.w);
```

CPU: Matching Arm ASR motionVectorScale configuration
```output
dispatchParameters.motionVectorScale.x = (float)renderWidth;
dispatchParameters.motionVectorScale.y = (float)renderHeight;
```

### Precision and Resolution

Internally, Arm ASR uses 16-bit quantities to represent motion vectors in many cases, which means that while motion vectors with greater precision can be provided, it will not currently benefit from the increased precision. The resolution of the motion vector buffer should be equal to the render resolution. If the `FFXM_FSR2_ENABLE_DISPLAY_RESOLUTION_MOTION_VECTORS` flag is set in `FfxmFsr2ContextDescription` when creating the `FfxmFsr2Context`, it should be equal to the presentation resolution.

### Coverage

Arm ASR will perform better quality upscaling when more objects provide their motion vectors. It is therefore advised that all opaque, alpha-tested and alpha-blended objects should write their motion vectors for all covered pixels. If vertex shader effects are applied, such as scrolling UVs, these calculations should also be factored into the calculation of motion for the best results. For alpha-blended objects it is also strongly advised that the alpha value of each covered pixel is stored to the corresponding pixel in the [reactive mask](#reactive-mask). This will allow the technique to perform better handling of alpha-blended objects during upscaling. The reactive mask is especially important for alpha-blended objects where writing motion vectors might be prohibitive, such as particles.

## Reactive Mask

In the context of Arm ASR, the term "reactivity" means how much influence the samples rendered for the current frame have over the production of the final upscaled image. Typically, samples rendered for the current frame contribute a relatively modest amount to the result computed by the algorithm; however, there are exceptions. As there is no good way to determine from either color, depth or motion vectors which pixels have been rendered using alpha blending, Arm ASR performs best when applications explicitly mark such areas.

Therefore, it is strongly encouraged that applications provide a reactive mask as an input. The reactive mask guides Arm ASR on where it should reduce its reliance on historical information when compositing the current pixel, and instead allow the current frame's samples to contribute more to the final result. The reactive mask allows the application to provide a value from `[0.0..1.0]` where `0.0` indicates that the pixel is not at all reactive (and should use the default composition strategy), and a value of `1.0` indicates the pixel should be fully reactive. This is a floating point range and can be tailored to different situations.

While there are other applications for the reactive mask, the primary application for the reactive mask is producing better results of upscaling images which include alpha-blended objects. A good proxy for reactiveness is the alpha value used when compositing an alpha-blended object into the scene. Therefore, applications should write `alpha` to the reactive mask. It should be noted that it is unlikely that a reactive value of close to `1` will ever produce good results. Therefore, you should clamp the maximum reactive value to around `0.9`.

Provide a reactive mask by setting the `reactive` field of `FfxmFsr2DispatchDescription` to `NULL`.

If a reactive mask is not provided then an internally generated `1x1` texture with a cleared reactive value will be used.

## Automatically generating reactivity

To help applications generate the reactive mask, there is an optional utility pass. Under the hood, the API launches a fragment shader which computes these values for each pixel using a luminance-based heuristic.

To do this, the applications can call the `ffxmFsr2ContextGenerateReactiveMask` (`$ARMASR_DIR/include/host/ffxm_fsr2.h`) function and should pass two versions of the color buffer: one containing opaque only geometry, and the other containing both opaque and alpha-blended objects.

## Exposure

Arm ASR provides two values which control the exposure used when performing upscaling:

1. **Pre-exposure**: a value by which you can divide the input signal to get back to the original signal produced by the game before any packing into lower precision render targets.

2. **Exposure**: a value which is multiplied against the result of the pre-exposed color value.

The exposure value should match that which the application uses during any subsequent tonemapping passes performed by the application. This means Arm ASR will operate consistently with what is likely to be visible in the final tonemapped image.

{{%notice%}}
In various stages of the algorithm, the technique will compute its own exposure value for internal use. It is worth noting that all outputs will have this internal tonemapping reversed before the final output is written. Meaning that Arm ASR returns results in the same domain as the original input signal.
{{%/notice%}}

Poorly selected exposure values can have a drastic impact on the final quality of Arm ASR's upscaling. Therefore, it is recommended that `FFXM_FSR2_ENABLE_AUTO_EXPOSURE` is used by the application, unless there is a particular reason not to. When `FFXM_FSR2_ENABLE_AUTO_EXPOSURE` is set in the `FfxmFsr2ContextDescription` structure, the exposure calculation in `ComputeAutoExposureFromLavg` (`$ARMASR_DIR/include/gpu/fsr2/ffxm_fsr2_common.h`) is used to compute the exposure value, which matches the exposure response of ISO 100 film stock.

## Modular backend

The design of the Arm ASR API means that the core implementation of the algorithm is unaware of which rendering API it sits upon. Instead, it calls functions provided to it through an interface, allowing different backends to be used with the technique. Applications which have their own rendering abstractions can implement their own backend, taking control of all aspects of Arm ASR's underlying function. This includes memory management, resource creation, shader compilation, shader resource bindings, and the submission of the workloads to the graphics device.

Out of the box, the API will compile into multiple libraries following the separation already outlined between the core API and the backends. This means if you wish to use the backends provided, you should link both the core API lib **Arm_ASR_api** as well the backend **Arm_ASR_backend** matching your requirements.

Arm ASR only provides a built-in Vulkan backend as it targets Vulkan mobile apps.

## Camera jitter

Arm ASR relies on the application to apply sub-pixel jittering while rendering - this is typically included in the projection matrix of the camera. To make the application of camera jitter simple, the API provides a small set of utility function which computes the sub-pixel jitter offset for a particular frame within a sequence of separate jitter offsets.

``` CPP
int32_t ffxmFsr2GetJitterPhaseCount(int32_t renderWidth, int32_t displayWidth);
FfxErrorCode ffxmFsr2GetJitterOffset(float* outX, float* outY, int32_t jitterPhase, int32_t sequenceLength);
```

Internally, these functions implement a **Halton[2,3]** sequence. The goal of the Halton sequence is to provide spatially separated points, which cover the available space.

It is important to understand that the values returned from the `ffxmFsr2GetJitterOffset` (`$ARMASR_DIR/include/host/ffxm_fsr2.h`) are in unit pixel space, and in order to composite this correctly into a projection matrix you have to convert them into projection offsets. The code below shows how to correctly composite the sub-pixel jitter offset value into a projection matrix.

``` cpp
const int32_t jitterPhaseCount = ffxmFsr2GetJitterPhaseCount(renderWidth, displayWidth);

float jitterX = 0;
float jitterY = 0;
ffxmFsr2GetJitterOffset(&jitterX, &jitterY, index, jitterPhaseCount);

// Calculate the jittered projection matrix.
const float jitterX = 2.0f * jitterX / (float)renderWidth;
const float jitterY = -2.0f * jitterY / (float)renderHeight;
const Matrix4 jitterTranslationMatrix = translateMatrix(Matrix3::identity, Vector3(jitterX, jitterY, 0));
const Matrix4 jitteredProjectionMatrix = jitterTranslationMatrix * projectionMatrix;
```

Jitter should be applied to *all* rendering. This includes opaque, alpha transparent, and raytraced objects. For rasterized objects, the sub-pixel jittering values calculated by the `ffxmFsr2GetJitterOffset` (`$ARMASR_DIR/include/host/ffxm_fsr2.h`) function can be applied to the camera projection matrix which is ultimately used to perform transformations during vertex shading. For raytraced rendering, the sub-pixel jitter should be applied to the ray's origin - often the camera's position.

Whether you decide whether to use the recommended `ffxmFsr2GetJitterOffset` function or your own sequence generator, you must set the `jitterOffset` field of the `FfxmFsr2DispatchDescription` structure to inform the algorithm of the jitter offset that has been applied in order to render each frame. Moreover, if not using the recommended `ffxmFsr2GetJitterOffset` function, care should be taken that your jitter sequence never generates a null vector; that is value of 0 in both the X and Y dimensions.

## Camera jump cuts

Most applications with real-time rendering have a large degree of temporal consistency between any two consecutive frames. However, there are cases where a change to a camera's transformation might cause an abrupt change in what is rendered. In such cases, Arm ASR is unlikely to be able to reuse any data it has accumulated from previous frames, and should clear this data in order to exclude it from consideration in the compositing process. In order to indicate that a jump cut has occurred with the camera you should set the `reset` field of the `FfxmFsr2DispatchDescription` structure to `true` for the first frame of the discontinuous camera transformation.

Rendering performance may be slightly less than typical frame-to-frame operation when using the reset flag, as Arm ASR will clear some additional internal resources.

## Mipmap biasing

Applying a negative mipmap biasing will typically generate an upscaled image with better texture detail. It is recommended that you apply the following formula to your Mipmap bias:

``` CPP
mipBias = log2(renderResolution/displayResolution) - 1.0;
```

## Frame Time Delta Input

The API requires `frameTimeDelta` be provided by the application through the `FfxmFsr2DispatchDescription` structure. This value is in milliseconds. If running at 60fps, the value passed should be around `16.6f`.

The value is used within the temporal component of the auto-exposure feature. This allows for tuning of the history accumulation for quality purposes.

## HDR support

High dynamic range images are supported. To enable this, you should set the `FFXM_FSR2_ENABLE_HIGH_DYNAMIC_RANGE` flag in the `FfxmFsr2ContextDescription` structure. Provide the input color image in linear RGB color space.

## Debug Checker

The context description structure can be provided with a callback function for passing textual warnings from the runtime to the underlying application. The `fpMessage` member of the description is of type `FfxmFsr2Message` which is a function pointer for passing string messages of various types. Assigning this variable to a suitable function, and passing the `FFXM_FSR2_ENABLE_DEBUG_CHECKING` flag within `FfxmFsr2ContextDescription` will enable the feature. It is recommended this is enabled only in debug development builds.

## Extended ffx_shader_compiler

Most of the workloads in the upscalers have been converted to fragment shaders. Since the workflow using the standalone VK backend relies on reflection data generated with [`AMD's Shader Compiler`](https://github.com/GPUOpen-LibrariesAndSDKs/FidelityFX-SDK/), it becomes necessary to do an improvised extension of the tool to provide reflection data for the RenderTargets so resources could be resolved automatically in the backend. Users might want to evolve the algorithm potentially changing the RenderTargets in the process. Thus, a diff file is provided with the changes that were applied locally `ffx_shader_compiler` (`$ARMASR_DIR/tools/ffx_shader_compiler.diff`) for the latest version of the technique.

## Generate prebuilt shaders

There is a helper script provided to generate prebuilt shaders which are used for standalone backend. Make sure python is installed, and run it with the following command:

```bash
python $ARMASR_DIR/tools/generate_prebuilt_shaders.py
```

You will find the output from the script in `$ARMASR_DIR/src/backends/shared/blob_accessors/prebuilt_shaders`.

## Targeting GLES 3.2

Running Arm ASR on GLES is possible when using the [Tight Integration](#tight-integration) approach. In this scenario, you have to apply two changes:

1. When creating the context, the user has to specify the flag `FFXM_FSR2_OPENGL_ES_3_2` in the `FfxmFsr2ContextDescription`. This triggers changes internally so that Arm ASR adapts to a GLES- friendly approach.

2. The `permutationOptions` (`$ARMASR_DIR/include/host/ffxm_interface.h`) provided when creating the pipelines now includes the new permutation option `FSR2_SHADER_PERMUTATION_PLATFORM_GLES_3_2` (`$ARMASR_DIR/src/components/fsr2/ffxm_fsr2_private.h`). This is a hint that you need to use the shader variants for the technique with the following symbol defined:

    ```
    #define FFXM_SHADER_PLATFORM_GLES_3_2 1
    ```

## Next steps

You are now ready to use Arm ASR in your game engine projects. Go to the next section to explore further resources on Arm ASR.
