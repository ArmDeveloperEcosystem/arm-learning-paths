---
title: Transcribe microphone audio
description: Record English microphone audio with sounddevice and transcribe it locally with Sherpa-ONNX for the voice translation pipeline.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Capture speech with Sherpa-ONNX

With your environment and models ready, you'll create `stt.py`, a Python script that records English speech and prints a transcript. The script will use `sounddevice` to capture five seconds of microphone audio, then Sherpa-ONNX to transcribe it with the downloaded Zipformer model.

You'll first check your microphone and create the script, then run it to record a sentence. By testing transcription on its own, you will be able to identify recording or recognition problems before adding translation.

Return to the project directory and activate the virtual environment if it isn't already active:

```bash
cd ~/voice-translator
source .venv/bin/activate
```

List the audio devices visible to Python:

```bash
python -m sounddevice
```

Confirm that the list contains an input device, such as `MacBook Pro Microphone` or your external microphone. 

## Create the transcription script

Create `stt.py` in `~/voice-translator`. `create_recogniser()` loads the model and `transcribe()` accepts recorded samples and returns text. By keeping the recording in `main()`, we let the Gradio application reuse these functions with browser audio.

```python
from pathlib import Path

import numpy as np
import sherpa_onnx
import sounddevice as sd


MODEL = Path("models/sherpa-onnx-streaming-zipformer-en-2023-06-26")
RECORDING_SECONDS = 5


def create_recogniser():
    return sherpa_onnx.OnlineRecognizer.from_transducer(
        tokens=str(MODEL / "tokens.txt"),
        encoder=str(
            MODEL
            / "encoder-epoch-99-avg-1-chunk-16-left-128.int8.onnx"
        ),
        decoder=str(
            MODEL / "decoder-epoch-99-avg-1-chunk-16-left-128.onnx"
        ),
        joiner=str(
            MODEL
            / "joiner-epoch-99-avg-1-chunk-16-left-128.int8.onnx"
        ),
        num_threads=2,
        sample_rate=16000,
        feature_dim=80,
        decoding_method="greedy_search",
        provider="cpu",
    )


def transcribe(recogniser, samples, sample_rate):
    stream = recogniser.create_stream()
    stream.accept_waveform(sample_rate, samples)

    tail_padding = np.zeros(int(0.5 * sample_rate), dtype=np.float32)
    stream.accept_waveform(sample_rate, tail_padding)
    stream.input_finished()

    while recogniser.is_ready(stream):
        recogniser.decode_stream(stream)

    return recogniser.get_result(stream).strip()


def main():
    recogniser = create_recogniser()
    microphone = sd.query_devices(kind="input")
    sample_rate = int(microphone["default_samplerate"])

    print(f"Using microphone: {microphone['name']}")
    print(f"Recording for {RECORDING_SECONDS} seconds...")

    samples = sd.rec(
        int(RECORDING_SECONDS * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="float32",
    )
    sd.wait()

    transcript = transcribe(recogniser, samples.reshape(-1), sample_rate)
    print(f"Transcript: {transcript or '[null]'}")


if __name__ == "__main__":
    main()
```

`sounddevice` records one channel of `float32` samples at the microphone's sample rate. `sd.wait()` will then wait for the 5 second recording to finish before moving on to the transcription. 


Sherpa-ONNX resamples the audio to the model's 16 kHz input rate. `transcribe()` creates a new stream for each recording, appends half a second of silence to flush the final words, and marks the input as finished. The decode loop then consumes the available frames and returns the transcript.

The encoder and joiner use the `int8` files, whilst the decoder uses the separate file named in the configuration. `provider="cpu"` and `num_threads=2` select CPU execution with two threads. The loaded recogniser can be reused, while each recording has its own stream.

## Record and transcribe an utterance

Run the script:[^microphone-permission]

```bash
python stt.py
```

After the recording message appears, say:

```text
Where is the nearest train station?
```

The output is similar to:

```output
Using microphone: MacBook Pro Microphone
Recording for 5 seconds...
Transcript: WHERE IS THE NEAREST TRAIN STATION
```

Capitalisation and punctuation may differ, but the transcript should contain the words you spoke. 


If the transcript is empty, run `python -m sounddevice` again. Check that the `>` marker is beside the microphone you spoke into, and confirm the terminal application's microphone permission in System Settings.

If the script remains at `Recording for 5 seconds...`, check the same device and permission settings, restart the terminal application, and run it again.

## What you've accomplished and what's next

`stt.py` now records one utterance and prints its transcript. The application will pass that text to Gemma only after recognition finishes.

Next, test Gemma's translation with typed text before connecting it to the recogniser.

[^microphone-permission]: The first recording can trigger a macOS permission request. Select **Allow**. If recording fails, open **System Settings**, select **Privacy & Security**, select **Microphone**, and enable access for your terminal application.
