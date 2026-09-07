---
title: Understand the Whisper Journal Android application
description: Review how Whisper Journal imports model packages, records audio, runs LiteRT and ExecuTorch, and decodes transcripts.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How Whisper Journal works

`MainActivity.java` connects the model selector, Android document picker, and microphone recorder. It also connects progress messages and journal entry. 

`MainActivity.java` moves model loading and inference onto a single background thread so the Android user interface remains responsive.

Whisper Journal supplies two adapters:

- `ExecuTorchWhisperAdapter.java` runs the optimized Whisper Tiny and Small packages.
- `LiteRtWhisperAdapter.java` has profiles for the Whisper Base, Medium, and Large V3 LiteRT packages.

`AdapterRegistry.java` selects the adapter registered for the current model. `MainActivity.java` supplies the recorded 16 kHz waveform and displays the returned `TranscriptionResult`.

### How Whisper Journal resolves and validates the model package

`ModelRegistry.java` contains one `WhisperModelDescriptor` for each registered package. A descriptor records the following:

- Model ID
- Display name
- Adapter ID
- Repository ID
- Suggested package filename
- Mel-bin count
- Vocabulary size

The importer doesn't require the outer ZIP to use that filename.

`ModelPackageImporter.java` receives the ZIP selected through Android's document picker. It looks for the files required by the descriptor's adapter:

| Adapter | Required files after import | Runtime contract |
| --- | --- | --- |
| ExecuTorch | `model.pte`, `whisper_preprocessor.pte`, `tokenizer.json` | Main program exposes `encoder` and `text_decoder` |
| LiteRT | `model.tflite`, `tokenizer.json` | Model exposes `encode` and `decode` signatures matching a registered decoder profile |

An ExecuTorch package on the AI Portal can contain baseline and optimized directories. The importer prefers files in an optimized directory, then stores the selected model, preprocessor, and tokenizer under fixed names. For LiteRT, the importer prefers a `.tflite` filename containing `int8`, ignores filenames containing `fp32` or `float`, and otherwise accepts a remaining `.tflite` candidate. 

These filename checks select package files. They don't prove that the runtime contract is compatible.

The importer extracts into a temporary directory and replaces the installed package only after the required files have been found and copied. The selected adapter then opens the normalized files. The ExecuTorch adapter checks its required model methods and parses the tokenizer. Preprocessor and tensor compatibility are exercised during transcription. The LiteRT adapter checks signatures, tensor shapes, its decoder profile, and the tokenizer when loading.

Models remain outside the Android application package (APK). This keeps builds small so you can import another package without recompiling the application. The document picker grants access only to the selected ZIP, so the application doesn't need broad storage permission. Clearing the application data or uninstalling it removes the imported models.

### How Whisper Journal records audio

`AudioRecorder.java` captures mono PCM audio at 16 kHz and converts it to a float waveform. Recording stops when the user selects **Stop recording** or after 30 seconds.

The application caps recordings at 30 seconds to match the registered Whisper input contracts: 3,000 feature frames at a 10 millisecond hop. LiteRT preprocessing pads or trims audio to that window. The ExecuTorch path delegates feature padding and trimming to `whisper_preprocessor.pte`. Whisper Journal rejects recordings shorter than half a second and recordings that are nearly silent before starting model inference.

### How the ExecuTorch adapter works

`ExecuTorchWhisperAdapter.java` memory-maps the main model with four CPU threads and the preprocessor with two. It checks that the main program contains `encoder` and `text_decoder`, then reads the backend reported by the encoder metadata.

The adapter runs the ExecuTorch package in four stages:

1. Pass the waveform to `whisper_preprocessor.pte` to create Whisper log-Mel features.
2. Call `encoder` once to create the encoder hidden state.
3. Call `text_decoder` one token at a time with the previous token, encoder output, and cache position.
4. Decode the generated token IDs using `tokenizer.json`.

The decoder applies the English transcription prefix and suppresses tokens that shouldn't be generated. It selects the highest-scoring token and stops at the end token, repetition guard, or generation limit.

### How the LiteRT adapter works

`LiteRtWhisperAdapter.java` opens the selected `.tflite` model with XNNPACK and up to four CPU threads. It requires `encode` and `decode` signatures, and it checks the following against the registered Base, Medium, or Large V3 profile:

- Inputs
- Outputs
- Attention caches
- Vocabulary size
- Model dimensions

The LiteRT path uses `WhisperFeatureExtractor.java` to convert the recorded waveform into log-Mel features. Base and Medium use 80 Mel bins, and Large V3 uses 128.

The adapter then peforms the following tasks:

1. Calls the `encode` signature once to create the cross-attention caches
2. Calls the `decode` signature repeatedly while carrying the self-attention caches forward
3. Applies the registered English prompt and token-suppression rules
4. Decodes the generated IDs with the tokenizer included in the package

### How adapters isolate model-specific code

The `SpeechToTextAdapter.java` interface is the boundary between the journal screen and a model runtime. An adapter identifies itself, loads a package, and reports whether it's ready. It transcribes a 16 kHz waveform and releases the waveform's native state.

This keeps runtime and decoding details out of `MainActivity.java`. `AdapterRegistry.java` contains one instance of each supplied adapter, and the application keeps only the selected model runtime loaded.

Importing a ZIP file doesn't add executable Java code to the application. An adapter is compiled into the APK. A model that needs another runtime library or a different execution sequence requires source changes and a rebuilt APK.

### How Whisper Journal uses optimized Arm CPU kernels

XNNPACK is the CPU backend that's used by the LiteRT adapter and the supplied ExecuTorch programs. XNNPACK integrates KleidiAI, which provides optimized compute kernels for Arm processors. On a compatible device, XNNPACK can select KleidiAI kernels supported by the CPU.

## What you've learned and what's next

You've learned how the sample application works and can now trace both supplied adapters from ZIP import to an English transcript. The ExecuTorch adapter runs separate preprocessing, encoder, and decoder programs. The LiteRT adapter prepares features in Java and runs the `encode` and `decode` signatures from one model file. Both connect to the same journal interface through `SpeechToTextAdapter.java`.

Next, you'll learn how to use models that aren't currently supported by the application.
