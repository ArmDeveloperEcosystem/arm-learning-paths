---
title: Understand the Speech Journal Android application
description: Review how Speech Journal imports model packages, records audio, runs LiteRT and ExecuTorch, and decodes transcripts.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How Speech Journal works

`MainActivity.java` connects the model selector, Android document picker, and microphone recorder. It also connects progress messages and journal entry. 

`MainActivity.java` moves model loading and inference onto a single background thread so the Android user interface remains responsive.

Speech Journal supplies four adapters:

- `ExecuTorchWhisperAdapter.java` runs the optimized ExecuTorch Whisper Tiny and Small packages.
- `ExecuTorchSplitWhisperAdapter.java` runs an ExecuTorch Whisper Base model split across three `.pte` files: encoder, prefill, and decode.
- `LiteRtWhisperAdapter.java` has profiles for the Whisper Base, Medium, and Large V3 LiteRT packages.
- `ExecuTorchCtcAdapter.java` runs the Conformer CTC package with ExecuTorch, using waveform input and CTC decoding.

`AdapterRegistry.java` selects the adapter registered for the current model. `MainActivity.java` supplies the recorded 16 kHz waveform and displays the returned `TranscriptionResult`.

### How Speech Journal resolves and validates the model package

`ModelRegistry.java` contains one `SpeechModelDescriptor` for each registered package. A descriptor records the following:

- Model ID
- Display name
- Adapter ID
- Repository ID
- Suggested package filename
- Mel-bin count
- Vocabulary size
- Configuration ID for the adapter profile

A Mel-bin count of `0` identifies a model that takes waveform input directly, as Conformer does.

`ModelPackageImporter.java` receives the ZIP selected through Android's document picker. It looks for the files required by the descriptor's adapter:

| Adapter | Required files after import | Runtime contract |
| --- | --- | --- |
| ExecuTorch Tiny and Small | `model.pte`, `whisper_preprocessor.pte`, `tokenizer.json` | Main program exposes `encoder` and `text_decoder` |
| ExecuTorch Base | `encoder.pte`, `decoder_prefill.pte`, `decoder_decode.pte`, `whisper_preprocessor.pte`, `tokenizer.json` | Each program exposes `forward`; decoder caches match the split adapter's expected layout |
| LiteRT | `model.tflite`, `tokenizer.json` | Model exposes `encode` and `decode` signatures matching a registered decoder profile |
| ExecuTorch Conformer CTC | `model.pte`, `config.json`, `preprocessor_config.json`, `tokenizer_config.json`, `vocab.json` | Program exposes `forward` with a fixed waveform input and CTC frame-score output |

For the Tiny and Small ExecuTorch packages, the importer prefers files in an optimized directory, then stores the selected model, preprocessor, and tokenizer under fixed names. For LiteRT, the importer prefers a `.tflite` filename containing `int8`, ignores filenames containing `fp32` or `float`, and otherwise accepts a remaining `.tflite` candidate.

For Conformer, the importer requires one `model.pte` and the four configuration and vocabulary files listed in the table. It also preserves `special_tokens_map.json` and `metadata.yaml` when present. It rejects duplicate required files and additional model programs.

These filename checks select package files. They don't prove that the runtime contract is compatible.

The importer extracts into a temporary directory and replaces the installed package only after the required files have been found and copied. The selected adapter then opens the normalized files. The ExecuTorch Whisper adapters check their required model methods and parse the tokenizer. Preprocessor and tensor compatibility are exercised during transcription. The LiteRT adapter checks signatures, tensor shapes, its decoder profile, and the tokenizer when loading. The Conformer adapter checks its waveform preprocessing configuration, vocabulary, and `forward` method when loading, then validates the output tensor during transcription.

Models remain outside the Android application package (APK). This keeps builds small so you can import another package without recompiling the application. The document picker grants access only to the selected ZIP, so the application doesn't need broad storage permission. Clearing the application data or uninstalling it removes the imported models.

### How Speech Journal records audio

`AudioRecorder.java` captures mono PCM audio at 16 kHz and converts it to a float waveform. Recording stops when the user selects **Stop recording** or after 30 seconds.

The application caps recordings at 30 seconds to match the supplied model profiles. Whisper uses 3,000 feature frames at a 10 millisecond hop. LiteRT preprocessing pads or trims audio to that window, and the ExecuTorch Whisper adapters use `whisper_preprocessor.pte` to prepare the features. Conformer takes 480,000 waveform samples at 16 kHz and pads shorter recordings with zeros. Speech Journal rejects recordings shorter than half a second and recordings that are nearly silent before starting model inference.

### How the Tiny and Small ExecuTorch adapter works

`ExecuTorchWhisperAdapter.java` memory-maps the main model with four CPU threads and the preprocessor with two. It checks that the main program contains `encoder` and `text_decoder`, then reads the backend reported by the encoder metadata.

The adapter runs the ExecuTorch package in four stages:

1. Pass the waveform to `whisper_preprocessor.pte` to create Whisper log-Mel features.
2. Call `encoder` once to create the encoder hidden state.
3. Call `text_decoder` one token at a time with the previous token, encoder output, and cache position.
4. Decode the generated token IDs using `tokenizer.json`.

The decoder applies the English transcription prefix and suppresses tokens that shouldn't be generated. It selects the highest-scoring allowed token, with repetition detection and a generation limit to bound the output.

### How the split ExecuTorch adapter works

`ExecuTorchSplitWhisperAdapter.java` runs the encoder, prefill, and decode programs from one Whisper Base model. A separate `whisper_preprocessor.pte` program prepares the audio features. Each program exposes a `forward` method.

The adapter runs the package in five stages:

1. Pass the waveform to the preprocessor to create log-Mel features.
2. Run the encoder once to create the encoder hidden state.
3. Run prefill once with the English transcription prompt and encoder output. This initializes the attention caches and produces scores for the first generated token.
4. Run decode one token at a time, passing the attention caches between calls.
5. Convert the generated token IDs into text using `tokenizer.json`.

The adapter maps the prefill caches into the order expected by decode. It selects the highest-scoring allowed token and stops at the end token, repetition guard, or generation limit. All four modules use the same four-thread setting because ExecuTorch shares a worker thread pool.

### How the LiteRT adapter works

`LiteRtWhisperAdapter.java` opens the selected `.tflite` model with XNNPACK and up to four CPU threads. It requires `encode` and `decode` signatures, and it checks the following against the registered Base, Medium, or Large V3 profile:

- Inputs
- Outputs
- Attention caches
- Vocabulary size
- Model dimensions

The LiteRT path uses `WhisperFeatureExtractor.java` to convert the recorded waveform into log-Mel features. Base and Medium use 80 Mel bins, and Large V3 uses 128.

The adapter then performs the following tasks:

1. Calls the `encode` signature once to create the cross-attention caches
2. Calls the `decode` signature repeatedly while carrying the self-attention caches forward
3. Applies the registered English prompt and token-suppression rules
4. Decodes the generated IDs with the tokenizer included in the package

### How the Conformer CTC adapter works

`ExecuTorchCtcAdapter.java` runs one `model.pte` program with four CPU threads. Conformer uses connectionist temporal classification (CTC) to turn audio-frame predictions into text.

The adapter runs the package in four stages:

1. Normalize the recorded samples and pad the waveform with zeros to 480,000 samples.
2. Call `forward` once with a `float32[1,480000]` tensor. The model returns `float32[1,1499,32]` scores for audio frames and vocabulary symbols.
3. Keep only the output frames corresponding to the original recording length.
4. Select the highest-scoring symbol for each frame, collapse consecutive repeated symbols, remove blank symbols, and convert word delimiters to spaces.

`CtcAudioProcessor.java` handles normalization and valid frame lengths. `CtcDecoder.java` converts the scores into text. Collapsing repetitions before removing blanks preserves repeated letters separated by a blank prediction.

The vocabulary produces uppercase text, with an apostrophe as its only punctuation. The adapter preserves this output. Cropping the output happens after inference, so shorter recordings still run the full padded input window.

### How adapters isolate model-specific code

The `SpeechToTextAdapter.java` interface is the boundary between the journal screen and a model runtime. An adapter identifies itself, loads a package, and reports whether it's ready. It transcribes a 16 kHz waveform and releases its runtime resources when closed.

This keeps runtime and decoding details out of `MainActivity.java`. `AdapterRegistry.java` contains one instance of each supplied adapter, and the application keeps only the selected model runtime loaded.

Importing a ZIP file doesn't add executable Java code to the application. An adapter is compiled into the APK. A model that needs another runtime library or a different execution sequence requires source changes and a rebuilt APK.

### How Speech Journal uses optimized Arm CPU kernels

XNNPACK is the CPU backend that's used by the LiteRT adapter and the supplied ExecuTorch programs. XNNPACK integrates KleidiAI, which provides optimized compute kernels for Arm processors. On a compatible device, XNNPACK can select KleidiAI kernels supported by the CPU.

## What you've learned and what's next

You can now trace all four adapters from ZIP import to an English transcript. Tiny and Small use encoder and decoder methods in one main ExecuTorch program. Base with ExecuTorch uses three model programs. Both ExecuTorch Whisper adapters use a separate preprocessor. LiteRT prepares features in Java and runs two signatures from one model file. Conformer takes a waveform, runs one model program, and uses CTC decoding. All four connect to the journal interface through `SpeechToTextAdapter.java`.

Next, you'll learn how to use models that aren't currently supported by the application.
