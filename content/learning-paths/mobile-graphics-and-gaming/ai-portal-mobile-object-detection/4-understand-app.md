---
title: Understand the Scene Detector Android application
description: Review how the application imports object-detection models, supplies images, runs ExecuTorch, and displays bounding boxes.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How Scene Detector works

`MainActivity.java` connects the Android document pickers, saved-image and camera inputs, current model, confidence control, and result views. It discovers available detection modes through `AdapterRegistry.java` and moves model execution off the main Android user-interface thread so the screen remains responsive while a detector runs.

An adapter is the application-side integration layer between the shared Android screen and one model workflow. `ExecuTorchObjectDetectionAdapter.java` provides ExecuTorch detection for the supported YOLO models.

The models can share one adapter because they use the same runtime, import flow, confidence control, and per-frame object-detection interface. They need different YOLO profiles because their preprocessing, output tensors, score calculations, and postprocessing differ. The adapter selects a profile from the imported model's descriptor.

`MainActivity.java` supplies one bitmap at a time and displays the returned detections. Runtime-specific tensor and decoding code remains inside the adapter and detector.

### How Scene Detector resolves and validates the model

`ModelRegistry.java` records the exact filename, model name, and runtime label for each package. It also records adapter ID, detector configuration, and default confidence threshold. `ModelImporter.java` rejects unregistered filenames and files larger than 700 MB.

The importer copies the file to temporary application-private storage. It then asks the adapter named by the descriptor to create and close a runner before the file replaces the installed model. 

This validation checks the following:

- The packaged runtime can open the program
- The registered detector strategy is available
- The model provides a `forward` method
- The `forward` method declares the XNNPACK backend

Output tensor shapes and data types are checked during the first detection run because they aren't available until the model executes. This is a compatibility check rather than an accuracy test or proof that the filename describes the file contents. A model can still produce poor results if its preprocessing, labels, box decoder, or postprocessing doesn't match the registered strategy.

The adapters aren't model executables. Gradle adds the ExecuTorch Android library when it builds the application, and its prebuilt `arm64-v8a` native runtime libraries are packaged in the Android application package (APK). The imported `.pte` file contains the model program and parameters rather than new Android or Java code.

Keeping the model outside the APK lets you replace it without recompiling the application. Clearing the application data or uninstalling the application removes the imported copy.

### How Scene Detector supplies pixels from an image or camera

`MainActivity.java` sends an Android bitmap to the selected detector regardless of where the pixels came from:

- For the live camera, CameraX `ImageAnalysis` keeps only the latest frame while the previous frame is being processed.
- For a saved image, Android's document picker supplies one bitmap for an explicit detection run.

The camera and saved-image inputs use the same detector because both produce one bitmap per inference call. Temporal tracking or a model that consumes several frames together would require a different interface.

### How Scene Detector routes the model to a YOLO profile

`ExecuTorchObjectDetectionAdapter.java` receives the registered model descriptor and creates `ExecuTorchYoloDetector.java` with the matching profile. One adapter is appropriate because the supplied models share the ExecuTorch runtime, imported-file flow, object-detection task, and per-frame bitmap interface.

The detector profiles isolate the parts that differ:

| Strategy | Supplied models | Main responsibility |
| --- | --- | --- |
| `ExecuTorchYoloDetector.java` | YOLOv5s, YOLOv8s, and YOLOv9s | Select the matching YOLO input and output profile |

### How Scene Detector prepares and decodes YOLO models

`ExecuTorchYoloDetector.java` selects a profile from the descriptor. The three YOLO models share a float32 RGB tensor with shape `[1, 3, 640, 640]`, but they don't share the complete input and output contract. 

The following table compares output, score calculation, and non-maximum suppression (NMS) intersection-over-union (IoU) between the three YOLO models: 

| Profile | Image preparation | Output | Score calculation |  NMS IoU |
| --- | --- | --- | --- | --- |
| YOLOv5 | Resize directly to `640 × 640`, values in `[0, 1]` | `[1, 25200, 85]` | Objectness × best class score | `0.45` |
| YOLOv8 | Resize directly to `640 × 640`, values in `[0, 1]` | `[1, 84, N]` | Best class score | `0.45` |
| YOLOv9 | Letterbox to `640 × 640`, padding with `114/255` | `[1, 84, 8400]` | Every class score above the threshold | `0.70` |

Direct resizing changes the image aspect ratio. The application scales the decoded coordinates independently across width and height to return to the original image.

Letterboxing preserves the aspect ratio. The application records the resize scale and padding, subtracts the padding from each decoded box, then divides by the scale.

### How Scene Detector runs an ExecuTorch detector

The supplied YOLO detector memory-maps the imported `.pte` file, loads its `forward` method, and checks that the method declares the XNNPACK backend. It converts the prepared bitmap to a channels-first float array and runs one inference call.

The model packages use INT8-quantized operations internally, but their application input and output tensors are float32. Quantization is part of the exported graph rather than an instruction to pass an INT8 bitmap from Java.

### How Scene Detector decodes YOLO boxes and class scores

YOLO outputs box coordinates as center `x`, center `y`, width, and height. The detector converts these values to left, top, right, and bottom coordinates.

YOLOv5 includes a separate objectness value. YOLOv8 and YOLOv9 don't. YOLOv9 also uses multi-label decoding, so one candidate can produce more than one class entry before filtering.

The application applies a sigmoid only when a score falls outside `[0, 1]`, which indicates that the package returned logits rather than probabilities.

### How Scene Detector handles duplicate detections

Several candidates can describe the same object. The application sorts candidates by score and applies per-class NMS:

1. Keep the highest-scoring box.
2. Compare lower-scoring boxes for the same class.
3. Remove a box when its IoU with a kept box exceeds the model profile's threshold.
4. Continue until no candidates remain or the result reaches the maximum detection count.

`DetectionOverlayView.java` scales the retained boxes to the displayed bitmap or camera preview and draws the COCO label and confidence score.

### How Scene Detector uses optimized Arm CPU kernels

The supplied ExecuTorch programs use XNNPACK as their CPU backend. XNNPACK integrates KleidiAI, which supplies optimized matrix multiplication and other compute kernels for Arm processors. On a compatible phone, the runtime can select suitable Arm-optimized kernels automatically for individual operations.

Some models on the Arm AI Portal state that they are optimized for [Scalable Matrix Extension 2 (SME2)](https://developer.arm.com/mobile-graphics-and-gaming/ai-mobile). SME2 is an Arm CPU instruction set extension for accelerating matrix-heavy operations used by AI and computer vision models.

An SME2 optimization label means that the model package and intended runtime provide an SME2-capable execution path. It doesn't mean that every Android device supports SME2 or that every operation uses an SME2 kernel. The selected path still depends on the model, operation, runtime build, and CPU features.

### How model-specific code is kept in adapters

`DetectionAdapter.java` is the boundary between `MainActivity.java` and a detection workflow. `AdapterRegistry.java` registers the supplied ExecuTorch object-detection adapter and reads `GeneratedAdapterRegistry.java` for build-time extensions.

Add another strategy when a model can keep the same runtime, task, import flow, and per-frame UI. Add a separate adapter when the runtime or model interaction changes, such as LiteRT inference, temporal tracking, or a multi-frame input. A `.pte` filename alone doesn't prove that a model fits one of the supplied strategies.

## What you've learned and what's next

You can now trace the application from model import through image preprocessing, ExecuTorch inference, model-specific decoding, NMS, and annotated output.

Next, you'll learn how to extend Scene Detector to use an unsupported model.
