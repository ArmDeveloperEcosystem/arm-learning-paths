---
title: Understand the TinySD Studio Android application
description: Review how TinySD Studio imports the model package, tokenizes prompts, runs ExecuTorch, and displays generated images.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How TinySD Studio works

`MainActivity.java` connects the Android document picker, prompt and seed controls, and current model. It also connects generation progress, generated image, and save action. It discovers the image-generation workflow through `AdapterRegistry.java` and moves model import and generation off the main Android user-interface thread so the screen remains responsive.

An adapter is the application-side integration layer between the shared Android screen and one model workflow. `TinySdImageGenerationAdapter.java` provides ExecuTorch image generation for the supported TinySD package.

`MainActivity.java` supplies the model descriptor, prompt, and seed and displays the returned bitmap. Runtime-specific tokenization, tensor, scheduler, and decoding code remains inside the adapter and its supporting classes.

The adapter isn't a model executable. Gradle adds the ExecuTorch Android library when it builds the application, and its prebuilt `arm64-v8a` native runtime libraries are packaged in the Android application package (APK).

The imported ZIP contains the model program, tokenizer, and scheduler data rather than new Android or Java code. The selected adapter prepares the inputs, calls the ExecuTorch runtime already in the APK, and converts the output into an image the shared screen can display.

### How TinySD Studio resolves and validates the model package

`CompatibleModelRegistry.java` contains the descriptor for the supported TinySD package. The descriptor records the following:

- Expected archive name
- Display name
- Adapter ID
- Imported-file names
- Storage directory
- Runtime label
- Output dimensions
- Minimum memory

`MainActivity.java` selects the descriptor and asks `AdapterRegistry.java` for the adapter named by its adapter ID.

`ModelImporter.java` receives the package URI from Android's document picker through the adapter. It checks that the ZIP contains the required ExecuTorch program, scheduler, and tokenizer entries and that they are stored without compression.

The importer copies the files to temporary application-specific storage and verifies each size and ZIP checksum. It rejects a model program smaller than 100 MB and empty scheduler or tokenizer files. The temporary directory replaces the installed model directory only after those checks succeed.

This import-time validation checks package structure and transfer integrity. When you first generate an image, `TinySdRunner.java` checks that the ExecuTorch program provides `text_encoder`, `unet`, and `vae_decoder`. The tokenizer, scheduler data, and returned tensor lengths are also checked when the application first uses them.

This is a compatibility check rather than an image-quality test or proof that the package name describes its contents. A model can still produce poor or corrupted images if its tokenizer, scheduler, tensors, denoising requirements, or output decoder don't match the supplied adapter.

The model remains outside the APK in application-specific storage. Clearing the application data or uninstalling the application removes the imported copy.

### How TinySD Studio tokenizes and encodes the prompt

`ClipTokenizer.java` reads the vocabulary and byte-pair encoding rules from `tokenizer.json`. It normalizes the prompt, applies the merge rules, adds the start and end tokens, and pads the result to 77 values.

The adapter also tokenizes an empty prompt to produce the unconditional input used for classifier-free guidance. `TinySdRunner.java` passes both `[1, 77]` token tensors to the program's `text_encoder` method. Each returned embedding must contain `77 × 768` floating-point values.

### How TinySD Studio runs the ExecuTorch program

`TinySdRunner.java` memory-maps `optimized.pte` and checks that the program exposes `text_encoder`, `unet`, and `vae_decoder`. All three methods run through the same ExecuTorch `Module` object.

The application creates the runner when you generate the first image, reuses it for later generations, and closes it through the adapter lifecycle.

### How TinySD Studio handles denoising

`ScheduleData.java` loads the denoising constants from `schedule_data.json`. The supplied schedule contains 25 steps. The optimized program has a static UNet batch size of one, so each step runs `unet` twice: once with the unconditional embedding and once with the prompt embedding.

The application combines the two predictions with a guidance scale of `7.5`. It then applies the precomputed DPM-Solver++ values to update the latent tensor. One image uses 25 scheduler steps and 50 UNet executions.

Generation runs on a background executor. Progress updates return to the Android main thread before changing the screen.

### How TinySD Studio decodes, displays, and saves the image

After denoising, `vae_decoder` converts the `[1, 4, 64, 64]` latent tensor into `[1, 3, 512, 512]` floating-point RGB values. `TinySdRunner.java` converts those values into an Android bitmap, and `MainActivity.java` displays the result.

The VAE decoder increases peak memory use. `MainActivity.java` compares Android's reported total memory with the descriptor's 7 GB minimum and prevents generation when the device doesn't meet it.

The **Save image** action opens Android's document picker with the `image/png` MIME type. The application writes the displayed bitmap to the location that you select without needing broad shared-storage permission.

### How TinySD Studio uses optimized Arm CPU kernels

The supplied ExecuTorch program uses XNNPACK as its CPU backend. XNNPACK integrates KleidiAI, which supplies optimized matrix multiplication and other compute kernels for Arm processors. On a compatible phone, the runtime can select suitable Arm-optimized kernels automatically for individual operations.

The selected path depends on the model program, operation, runtime build, data type, and CPU features. The Android application doesn't select individual XNNPACK or KleidiAI kernels in Java.

### How model-specific code is kept in adapters

`ImageGenerationAdapter.java` is the stable interface between the Android screen and a model workflow. An adapter checks package readiness, imports the package, validates and loads the model, runs generation, reports progress, and releases runtime resources. This prevents `MainActivity.java` from containing ExecuTorch, tokenizer, tensor, scheduler, or decoding code.

`AdapterRegistry.java` registers the supplied TinySD adapter and reads `GeneratedAdapterRegistry.java` for build-time extensions. `CompatibleModelRegistry.java` lets another package reuse the supplied adapter through its descriptor.

An adapter is compiled into the Android application. Importing a model package doesn't download or execute new Java code. If another adapter needs a new runtime library, that dependency must also be added before building a new APK.

Use the supplied adapter only when another package has the same methods, tensors, tokenizer, scheduler, denoising behavior, and output decoding. Use a separate adapter or extend the shared application interface when those requirements change.

## What you've learned and what's next

You can now trace the application from package import through tokenization, ExecuTorch inference, denoising, VAE decoding, and image output. The TinySD workflow plugs into the Android activity through `ImageGenerationAdapter.java`.

Next, you'll learn how to extend TinySD Studio to use an unsupported model.
