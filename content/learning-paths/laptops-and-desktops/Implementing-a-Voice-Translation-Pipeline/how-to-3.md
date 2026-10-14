---
title: Translate text with Gemma 4 E2B
description: Use LiteRT-LM and Gemma 4 E2B on an Apple Silicon Mac to stream Spanish translations of English text.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure English-to-Spanish translation

With microphone transcription working, you'll build `translate.py` to translate English text into Spanish using Gemma 4 E2B and LiteRT-LM. The script will accept typed input and display the Spanish translation as the model generates it.

You'll first define the shared language settings in `languages.py`, then create and test the translation script. Using typed text will let you check translation independently of microphone quality and recognition errors. Later, the same translation function will receive the transcript from Sherpa-ONNX.

Return to the project directory and activate the virtual environment if it isn't already active:

```bash
cd ~/voice-translator
source .venv/bin/activate
```

Using a file editor of your choice, create a file named `languages.py` in `~/voice-translator`. Copy the shared language settings below into the file and save it. These include choices for the application's language selector. You'll use Spanish throughout the walkthrough:

```python
LANGUAGES = {
    "Spanish": "es",
    "French": "fr",
    "Hindi": "hi",
    "Italian": "it",
    "Brazilian Portuguese": "pt",
}


def translation_prompt(language):
    return f"Translate into {language}. Output only the translation."
```

The dictionary keys serve as command-line choices, interface labels, and language names in the Gemma prompt. The values are the codes passed to Supertonic: `Spanish` maps to `es`. You can add other target languages alongside Spanish, provided Supertonic 3 supports them. The speech recogniser still requires English input.

## Create the translation script

Using a file editor of your choice, create a file named `translate.py` in `~/voice-translator`. Copy the code below into the file and save it. `translation_chunks()` yields the text from each model response, whilst `stream_translation()` prints those chunks and collects the complete translation.

```python
import argparse
from pathlib import Path

import litert_lm

from languages import LANGUAGES, translation_prompt


MODEL_PATH = Path("models/gemma-4-E2B-it.litertlm")


def translation_chunks(conversation, text):
    for chunk in conversation.send_message_async(text):
        for item in chunk.get("content", []):
            if item.get("type") == "text":
                yield item["text"]


def stream_translation(conversation, text):
    translated_parts = []

    for text_part in translation_chunks(conversation, text):
        translated_parts.append(text_part)
        print(text_part, end="", flush=True)

    print()
    return "".join(translated_parts).strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("language", choices=LANGUAGES)
    args = parser.parse_args()

    system_message = litert_lm.Message.system(
        translation_prompt(args.language)
    )

    litert_lm.set_min_log_severity(litert_lm.LogSeverity.ERROR)
    print(f"Loading Gemma 4 for {args.language}...")

    with litert_lm.Engine(
        str(MODEL_PATH),
        backend=litert_lm.Backend.GPU(),
        enable_speculative_decoding=True,
    ) as engine:
        with engine.create_conversation(
            messages=[system_message]
        ) as conversation:
            while True:
                text = input("English (Enter to quit): ").strip()
                if not text:
                    break

                print(f"{args.language}: ", end="", flush=True)
                stream_translation(conversation, text)


if __name__ == "__main__":
    main()
```

`backend=litert_lm.Backend.GPU()` selects the Apple GPU for Gemma 4. `enable_speculative_decoding=True` enables multi-token prediction: the model proposes multiple tokens for verification together to accelerate text generation.

The target language is fixed for each command-line run. In the Gradio application, changing the target language will replace the conversation and its history while keeping the engine loaded.

## Translate an English sentence

Run the script with Spanish as the target language:

```bash
python translate.py Spanish
```

Model initialisation can take several seconds. At the prompt, enter:

```text
Where is the nearest train station?
```

The output is similar to:

```output
Loading Gemma 4 for Spanish...
English (Enter to quit): Where is the nearest train station?
Spanish: ¿Dónde está la estación de tren más cercana?
English (Enter to quit):
```

The wording may differ slightly, but the response should contain only a Spanish translation. You can cross-check the meaning with a translation tool such as Google Translate or DeepL. This optional check requires internet access.

## What you've accomplished and what's next

The terminal now shows Spanish translation chunks as Gemma generates them, using one loaded model for the session. Copy the complete Spanish translation for the next step, where Supertonic 3 will turn it into speech. Press **Enter** at an empty prompt to exit the script and return to the shell before continuing.
