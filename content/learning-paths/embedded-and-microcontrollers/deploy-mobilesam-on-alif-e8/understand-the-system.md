---
title: Understand the camera and NPU segmentation pipeline
description: Trace live camera frames through MobileSAM and mask selection, with UART reporting and an optional dashboard.
weight: 2
layout: learningpathall
---

## Run camera inference on the E8

You'll deploy MobileSAM on an Alif Ensemble E8 Development Kit to capture camera frames, run segmentation, and report advancing frames and selected-mask counts through UART4. The prompts are fixed during export; the camera image changes at runtime. You'll export the model, build the application, and program model data and firmware separately.

Zephyr and ExecuTorch run on the Cortex-M55 High-Performance (HP) core, with MobileSAM computation delegated to the Ethos-U85-256 NPU. An MT9M114 selfie camera supplies images. The default build leaves the display and DSI host disabled and keeps the external MIPI selector on the camera after initialization. A blank display is expected in this mode.

{{% notice Important %}}
The default camera-and-UART firmware passed two independent reset-pin runs on E8 A0: 9 frames in a 35-second observation and 40 frames in a 120-second observation, with no reported errors. The optional dashboard has known DSI errors. The validation lesson separates this runtime result, integer TOSA agreement, and the failed original strict PT2E comparison; none establishes general scene accuracy.
{{% /notice %}}

## Follow one frame through the application

The model uses a 384 × 384 image, four independent positive prompts, three candidate masks per prompt, and int8 input and outputs. The public-image export is 13,317,584 bytes in external Octal SPI (OSPI) flash, mapped at `0xC0000000`. Its `.pte` is stored separately from firmware.

1. **Capture and prepare the image.** The camera pipeline writes planar RGB into the input buffer. The CPU normalizes each channel using the exported pixel mean and standard deviation, then applies the exported scale and zero point to produce a `[1, 3, 384, 384]` int8 tensor. Raw camera bytes and quantized inputs have different meanings, even though both occupy one byte per value.
2. **Execute MobileSAM.** The image encoder produces embeddings, and the mask decoder combines them with prompt embeddings prepared during export. Quantization uses A8W8 globally and A16W8 in the image encoder's attention modules. The external tensor interface remains int8.
3. **Select distinct masks.** Positive prompts sit at `(96, 96)`, `(288, 96)`, `(96, 288)`, and `(288, 288)`. Each requests three candidates. The CPU chooses the highest-quality candidate per point, requires quality at least `0.8`, and rejects masks covering less than roughly 0.5% or more than 85% of the mask image. It sorts survivors by quality and removes proposals whose intersection over union with an already selected mask exceeds `0.75`. At most four masks survive; they have no semantic object categories.
4. **Report and capture again.** UART prints the advancing frame number, time around `method.execute()`, and selected-mask count. The application requeues the camera buffer without switching the MIPI route to the display.

## Keep export and firmware inputs together

Keep the `.pte` and exporter JSON together. CMake generates `model_metadata.h` from the JSON. Image dimensions, preprocessing, quantization parameters, prompt count, and quality threshold form the firmware contract. Prompt embeddings are constants in the PTE; editing JSON coordinates cannot move them. Re-export to change prompts or resolution, regenerate firmware metadata, and program the matching model.

The matching source is `zephyr/samples/mobilesam-ethosu`, including `src/main.cpp`, `src/camera.cpp`, and the optional `src/display.cpp`. Use its supplied exporter throughout this Learning Path. The separate FVP example uses a 448 × 448 image, floating-point input/output, and one prompt.

## Treat the dashboard as an optional extension

The build lesson provides a separate dashboard configuration. It adds a 480 × 800 display with the camera image and colored masks, and alternates the shared MIPI route between camera and display. The tested dashboard advanced frames and visibly updated, but continued reporting DSI acknowledgment and packet errors. It is an experimental extension with a known unresolved link lifecycle.

The default camera-and-UART build avoids that display path. It still captures images, executes the same PTE, selects masks, and reports progress. UART counts establish liveness; they do not show whether the masks match objects in a scene. The validation lesson separates liveness, exact integer execution, and image accuracy.

## Interpret inference time

The reported milliseconds cover `method.execute()` only. Capture, normalization, quantization, mask selection, UART printing, and buffer requeue are outside that interval. Measure the complete loop separately before reporting camera-to-result latency. Results from the optional dashboard must identify that configuration.

## What you've learned and what's next

You know how camera data reaches the NPU, why prompt coordinates are fixed, and which model and metadata files must agree. Before continuing, explain why int8 camera input still needs preprocessing and why four prompts can yield fewer than four selected masks.

Next, prepare the matching source and tools and check the board's programming connection.
