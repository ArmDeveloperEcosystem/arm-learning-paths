---
title: Verify ASR inference on the E8 AppKit
description: Capture a spoken phrase on the E8 AppKit and verify the ASR transcription on its connected display.
weight: 6

layout: "learningpathall"
---

## Start the application

Keep the **PRG USB** cable connected.

Close J-Flash and SETOOLS, then press and release **RESET**. Wait for the display to show **Conformer ASR (ExecuTorch)** before testing audio.

![E8 display showing Conformer ASR (ExecuTorch) with an empty spectrogram, ready for speech capture.#center](e8-ready-to-capture.jpg "Conformer ASR ready to record")

## Speak a short phrase

Locate the joystick as shown in the [E8 AppKit User Guide](https://alifsemi.com/download/AUGD0028).

1. Press straight down on the centre of the joystick and hold it.
2. Say a short phrase while holding it.
3. Release the joystick to finish recording.
4. Wait for the transcription to appear on the display.

The display also shows the spectrogram, input duration, and processing times. The exact transcription depends on your speech and background noise. Repeat with a different phrase to check that another recording works.

![E8 display showing a speech spectrogram, processing times, and the transcription hallo after a recording.#center](e8-inference-complete.jpg "Example transcription after releasing the joystick")

## If the test does not work

- **Blank display:** power off before checking the display ribbon cable. Confirm that both images were programmed successfully and that the final MRAM write used the ASR package, not the CPU stubs.
- **Empty or incorrect transcription:** keep the microphones unobstructed, hold the joystick centre throughout the phrase, and try again in a quiet setting.

## What you have accomplished

You have programmed the E8 AppKit, captured live speech, and read the Conformer ASR transcription on its display.
