---
title: Validate the voice translation pipeline
description: Validate English transcription, Spanish translation and speech, and offline operation in the completed voice translator on an Apple Silicon Mac.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Test the complete workflow

You'll validate the application you built by checking its English transcript, Spanish translation, and spoken output. You'll then test a new recording with the Mac disconnected from the network to confirm offline operation.

You'll check the transcript first because a recognition error changes the text Gemma receives and can affect the translation and speech.

Keep `app.py` running and 'Translate to' set to Spanish. Use the browser to check each result in sequence.

Record the following English sentence in a quiet environment:

```text
Could you show me the way to the city centre?
```

Select **Translate** and verify the results in this order:

1. 'Transcript' contains the sentence you spoke.
2. The translation appears progressively in Spanish, preserves the sentence's meaning, and contains no explanation or formatting.
3. The status changes to `Synthesising...` after translation finishes.
4. Translated speech appears and plays the complete translated sentence with Spanish pronunciation.
5. The status returns to 'Ready'.

A suitable Spanish translation is "¿Podría indicarme el camino al centro de la ciudad?" Minor differences in punctuation or wording are expected.

## Verify on-device operation

Keep the browser tab and `app.py` running, then temporarily disconnect the Mac from Wi-Fi/Ethernet. Record another English sentence and translate it into Spanish.

The transcript, translation, and speech should still complete because all model files and inference runtimes are local. Reconnect the Mac after the test.

## Stop the application

Return to the terminal running the application and press `Ctrl+C`. The `finally` block closes the active conversation, and the engine context releases the Gemma resources.

## What you've accomplished

You have connected English speech recognition, English-to-Spanish translation with Gemma 4 E2B, and Spanish speech synthesis with Supertonic 3 in a local Python application.

To try another voice or adjust speech generation, see the [Sherpa-ONNX Supertonic documentation](https://k2-fsa.github.io/sherpa/onnx/tts/supertonic.html). Test your changes with `tts.py` before running the full application with `app.py`.
