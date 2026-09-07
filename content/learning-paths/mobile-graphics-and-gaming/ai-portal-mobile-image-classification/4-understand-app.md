---
title: Understand the Photo Insight Android application
description: Review how the application imports models, prepares images, runs LiteRT and ExecuTorch, and displays ranked results.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How Photo Insight works

`MainActivity.java` connects the Android document pickers, selected image, current model, and result views. It discovers the available modes through `AdapterRegistry.java` and moves inference off the main Android user-interface thread so the screen remains responsive while a model runs.

An adapter is the application-side integration layer between the shared Android screen and one model workflow. The application needs more than one adapter because the runtime alone doesn't define the complete workflow. LiteRT and ExecuTorch use different model formats and APIs. CLIP also needs text input, tokenization, and image-to-text similarity scoring instead of a fixed ImageNet label lookup.

The application therefore supplies three adapters:

- `LiteRtImageClassificationAdapter.java` provides LiteRT Quick Identify for compatible `.tflite` classifiers.
- `ExecuTorchImageClassificationAdapter.java` provides ExecuTorch Quick Identify for compatible fixed-label `.pte` classifiers.
- `ExecuTorchClipAdapter.java` provides ExecuTorch CLIP Custom Match for the supplied `.pte` CLIP model.

Each adapter defines the following:

- Mode name
- Model-import button
- Run button
- Status messages
- Optional controls
- Model validation
- Runner creation

`MainActivity.java` supplies the selected image and displays the returned text. Only the result update returns to the main thread.

The adapters aren't model executables. Gradle adds the LiteRT and ExecuTorch Android libraries when it builds the application. Their prebuilt `arm64-v8a` native runtime libraries are packaged in the APK.

The imported `.tflite` or `.pte` file contains the model graph, parameters, and runtime program rather than new Android or Java code. The selected adapter prepares the inputs, calls the runtime already in the APK. The adapter converts its outputs into results that the shared screen can display.

### How Photo Insight resolves and validates the model

The `ModelRegistry.java` file contains one descriptor for each supported model. A descriptor records the following:

- Expected filename
- Display name
- Runtime label
- Adapter ID
- Adapter configuration

For the two classification adapters, the configuration selects a reusable preprocessing profile.

The `ModelImporter.java` file receives a URI from Android's document picker and resolves the original filename through the registry. It rejects files that haven't been registered and files larger than the import limit.

The importer copies the file to temporary application-private storage. It then asks the adapter named by the descriptor to create and close a runner before the file replaces the installed model.

This validation checks whether the packaged runtime and adapter can open the model and whether the structure visible at load time matches the adapter contract:

- A LiteRT classifier must have one supported float32 RGB input tensor and one supported output tensor containing 1,000 ImageNet scores.
- An ExecuTorch classifier must load a `forward` method and declare the XNNPACK backend. The application checks that `forward` returns one finite float32 tensor with shape `[1, 1000]` when you first run inference.
- The CLIP program must provide the image-encoding and text-encoding methods used by its runner.

This is a compatibility check rather than an accuracy test or proof that the filename describes the file contents. A model can still produce poor results if its weights, labels, or preprocessing requirements don't match the registered descriptor.


### How Photo Insight runs a LiteRT classifier

`LiteRtImageClassificationAdapter.java` selects the preprocessing profile registered for the model. It then creates `LiteRtClassifier.java`, which loads the selected `.tflite` model with four CPU threads and enables XNNPACK. The classifier inspects the input tensor to determine whether the model uses channel-first `NCHW` or channel-last `NHWC` layout.

Before inference, the classifier applies the reusable profile selected by the model descriptor:

| Profile | Resize and crop | Normalization | Current models |
| --- | --- | --- | --- |
| `IMAGENET_CROP_256` | Resize the shorter edge to 256, then center-crop to `224 × 224` | ImageNet mean and standard deviation | DEiT Tiny, MobileNetV3 Small, Swin Tiny |
| `SYMMETRIC_CROP_232` | Resize the shorter edge to 232, then center-crop to `224 × 224` | Mean `0.5`, standard deviation `0.5` | timm ViT |

For a quantized output, the classifier uses the tensor scale and zero point to convert each value to a float. It then applies softmax and selects the five highest scores. The corresponding names come from the ImageNet label file bundled with the application.

Model-specific preprocessing is important because a model can load and run with the wrong normalization values while returning poor classifications.

### How Photo Insight runs an ExecuTorch classifier

`ExecuTorchImageClassificationAdapter.java` selects one of three preprocessing profiles for the imported model. It creates `ExecuTorchImageClassifier.java`, which memory-maps the `.pte` file, loads the `forward` method, and checks that the program declares the XNNPACK backend.

The supported ExecuTorch classifiers share one execution contract: a float32 RGB tensor in `NCHW` layout and one float32 output tensor with shape `[1, 1000]`. Their preprocessing differs:

| Profile | Resize and crop | Normalization | Current models |
| --- | --- | --- | --- |
| `IMAGENET_CROP_256` | Resize the shorter edge to 256, then center-crop to `224 × 224` | ImageNet mean and standard deviation | DEiT Tiny, GoogLeNet, MobileNetV3 Small, ResNet-18, ResNet-50, ShuffleNet V2, SqueezeNet 1.1 |
| `IMAGENET_CROP_232` | Resize the shorter edge to 232, then center-crop to `224 × 224` | ImageNet mean and standard deviation | Swin Tiny |
| `SYMMETRIC_DIRECT_RESIZE` | Resize directly to `224 × 224` | Mean `0.5`, standard deviation `0.5` | ViT Base |

After one `forward` call, the classifier applies softmax, selects the five highest scores, and maps them to the ImageNet label file bundled with the application.

### How Photo Insight runs the CLIP image encoder

`ExecuTorchClipAdapter.java` provides the candidate-description input box and checks that at least two descriptions were entered. It creates `ClipModel.java`, which loads `clip-vit-base-patch32-int8-executorch.pte` with ExecuTorch. The program contains separate methods rather than a single image-to-label call.

For the selected photo, `ClipModel.java` resizes and normalizes the pixels with the CLIP values. It builds a tensor with shape `[1, 3, 224, 224]` and calls `encode_image`. The output is a 512-value image embedding.

The application calculates this image embedding once for each run, even when you enter several descriptions.

### How Photo Insight tokenizes and encodes each description

`ClipTokenizer.java` applies CLIP's byte-pair encoding vocabulary and merge rules. It adds the start and end tokens, pads each sequence to 77 tokens, and creates `int64` token and attention-mask tensors.

`ClipModel.java` calls `encode_text` once for each candidate description. Each call returns a 512-value text embedding in the same vector space as the image embedding.

CLIP is therefore a multi-stage workflow:

1. Encode the image once.
2. Tokenize each candidate description.
3. Encode each description.
4. Calculate the scaled cosine similarity between the image and text embeddings.
5. Apply softmax and rank the descriptions.

The application caches text embeddings during a run, so a repeated description doesn't need another `encode_text` call.

### How Photo Insight uses optimized Arm CPU kernels

XNNPACK is the CPU backend used by the LiteRT models and the supplied ExecuTorch programs. XNNPACK integrates KleidiAI, which supplies optimized matrix multiplication and other compute kernels for Arm processors. On a compatible phone, the runtime can select suitable Arm-optimized kernels automatically for individual operations.

Several models on the Arm AI Portal are optimized for [Scalable Matrix Extension 2 (SME2)](https://developer.arm.com/mobile-graphics-and-gaming/ai-mobile). SME2 is an Arm CPU instruction set extension for accelerating matrix-heavy operations used by AI and computer vision models. It extends the Arm matrix and vector processing capabilities with instructions that can improve operations such as matrix multiplication.

An SME2 optimization label means that the model package and its intended runtime provide an SME2-capable execution path. It doesn't mean that every Android device supports SME2 or that every operation uses an SME2 kernel. The selected path still depends on the model, operation, runtime build, and CPU features.

### How model-specific code is kept in adapters
 
`VisionAdapter.java` is the stable interface between the Android screen and a model workflow. An adapter provides its controls, checks the inputs, validates and loads its model, and creates a `ModelRunner` implementation. This prevents `MainActivity.java` from containing LiteRT, ExecuTorch, tokenizer, tensor, or preprocessing code.

`AdapterRegistry.java` registers the three supplied adapters in the order: LiteRT classification, ExecuTorch classification, then ExecuTorch CLIP. `CompatibleModelRegistry.java` lets another model reuse one of those adapters through a single descriptor entry. `GeneratedAdapterRegistry.java` provides a separate extension point for a model that needs a different adapter.

An adapter is compiled into the Android application. Importing a model file doesn't download or execute new Java code. If another adapter needs a new runtime library, that dependency must also be added before building a new APK.

## What you've learned and what's next

You can now trace all three supplied adapters from model import to ranked results. The LiteRT and ExecuTorch classification adapters each run one fixed-label classifier. The ExecuTorch CLIP adapter separately encodes an image and several text descriptions before comparing their embeddings. All three plug into the same Android activity through `VisionAdapter.java`.

Next, you'll learn how to use currently unsupported models with Photo Insight.
