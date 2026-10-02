---
title: Synthesise translated speech
description: Configure Supertonic 3 with Sherpa-ONNX to synthesise and play the Spanish translation locally on an Apple Silicon Mac.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure Supertonic 3

You'll create `tts.py` to turn the Spanish translation from the previous step into spoken audio. The script will use Supertonic 3 through Sherpa-ONNX to synthesise speech, then `sounddevice` to play it through your Mac's default output device.

You'll first check the output device and create the script. You'll then run it and paste in the Spanish text to test playback. The model will stay loaded so you can try several sentences in the same session.

Return to the project directory and activate the virtual environment if it isn't already active:

```bash
cd ~/voice-translator
source .venv/bin/activate
```

List the output devices visible to Python:

```bash
python -m sounddevice
```

Confirm that the list contains your Mac speakers, headphones, or another output device.

Create `tts.py`. `create_tts()` loads the model, `synthesise()` returns audio samples and their sample rate, and `speak()` plays them.

```python
import argparse
from pathlib import Path

import sherpa_onnx
import sounddevice as sd

from languages import LANGUAGES


MODEL = Path("models/sherpa-onnx-supertonic-3-tts-int8-2026-05-11")


def create_tts():
    config = sherpa_onnx.OfflineTtsConfig(
        model=sherpa_onnx.OfflineTtsModelConfig(
            supertonic=sherpa_onnx.OfflineTtsSupertonicModelConfig(
                duration_predictor=str(
                    MODEL / "duration_predictor.int8.onnx"
                ),
                text_encoder=str(MODEL / "text_encoder.int8.onnx"),
                vector_estimator=str(
                    MODEL / "vector_estimator.int8.onnx"
                ),
                vocoder=str(MODEL / "vocoder.int8.onnx"),
                tts_json=str(MODEL / "tts.json"),
                unicode_indexer=str(MODEL / "unicode_indexer.bin"),
                voice_style=str(MODEL / "voice.bin"),
            ),
            num_threads=8,
            debug=False,
            provider="cpu",
        ),
        max_num_sentences=1,
    )

    if not config.validate():
        raise ValueError("model path")

    return sherpa_onnx.OfflineTts(config)


def synthesise(tts, text, language_code):
    config = sherpa_onnx.GenerationConfig()
    config.sid = 6
    config.speed = 1.0
    config.num_steps = 8
    config.extra["lang"] = language_code

    audio = tts.generate(text, config)
    if len(audio.samples) == 0:
        raise RuntimeError("no audio generated")

    return audio


def speak(tts, text, language_code):
    audio = synthesise(tts, text, language_code)
    duration = len(audio.samples) / audio.sample_rate
    print(f"Playing {duration:.1f}s of audio...")
    sd.play(audio.samples, samplerate=audio.sample_rate)
    sd.wait()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("language", choices=LANGUAGES)
    args = parser.parse_args()

    print("Loading Supertonic 3")
    tts = create_tts()

    while True:
        text = input(
            f"{args.language} text (press Enter to quit): "
        ).strip()
        if not text:
            break

        speak(tts, text, LANGUAGES[args.language])


if __name__ == "__main__":
    main()
```

The model configuration will use the downloaded quantised files, selects the CPU with eight threads, and sets `max_num_sentences=1` to process one sentence at a time. `config.validate()` checks the configuration before the model is loaded.

The generation settings select voice preset `6` with `sid`, normal speed with `speed=1.0`, and eight generation steps with `num_steps`. `extra["lang"]` receives `es` from `LANGUAGES` when you select Spanish.

`speak()` uses the sample rate returned by Supertonic when calling `sd.play()`. It then waits for playback to finish before accepting another sentence.

## Generate and play translated speech

Run the script with Spanish as the target language:

```bash
python tts.py Spanish
```

At the prompt, paste the Spanish translation from the previous step:

```text
¿Dónde está la estación de tren más cercana?
```

The script reports the duration and plays the sentence through the default output device. The output is similar to:

```output
Loading Supertonic 3
Spanish text (press Enter to quit): ¿Dónde está la estación de tren más cercana?
Playing 2.8 seconds of audio...
Spanish text (press Enter to quit):
```

The duration varies with the generated speech. Confirm that you hear the complete sentence with Spanish pronunciation.

If you don't hear audio, you made need to run `python -m sounddevice` again and confirm that macOS has selected the intended output device.

## Wait for the complete translation

The desktop application will collect all translation chunks before calling `synthesise()`. This gives Supertonic the complete text, but it also means you wait for translation and synthesis before hearing any audio. Only the displayed translation text streams in this implementation.

## What you've accomplished and what's next

You can now test recording, translation, and playback separately with `stt.py`, `translate.py`, and `tts.py`. Next, import their functions into a Gradio application so one English recording produces a transcript, Spanish translation, and spoken Spanish result.
