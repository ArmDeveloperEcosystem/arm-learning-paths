---
title: Translate text with Gemma 4 E2B
description: Use LiteRT-LM and Gemma 4 E2B on an Apple silicon Mac to stream Spanish translations of English text.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Configure English-to-Spanish translation

With microphone transcription working, you'll build `translate.py` to translate English text into Spanish using Gemma 4 E2B and LiteRT-LM. The script will accept typed input and display the Spanish translation as the model generates it.

You'll first define the shared language settings in `languages.py`, then create and test the translation script. Using typed text will let you check translation independently of microphone quality and recognition errors. Later, the same translation function will receive the transcript from Sherpa-ONNX.

Using a file editor of your choice, create a file named `languages.py` in the `~/voice-translator` directory. Copy and paste the following shared language settings into the file and save it:

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

These settings include choices for the application's language selector. You'll use Spanish to complete the Learning Path.

The dictionary keys serve as command-line choices, interface labels, and language names in the Gemma prompt. The values are the codes passed to Supertonic: `Spanish` maps to `es`. You can add other target languages alongside Spanish, provided Supertonic 3 supports them. The speech recognizer still requires English input.

## Create the translation script

Using a file editor of your choice, create a file named `translate.py` in the `~/voice-translator` directory. Copy and paste the following code into the file and save it:

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
`translation_chunks()` yields the text from each model response, while `stream_translation()` prints those chunks and collects the complete translation.

`backend=litert_lm.Backend.GPU()` selects the Apple GPU for Gemma 4. `enable_speculative_decoding=True` enables multi-token prediction: the model proposes multiple tokens for verification together to accelerate text generation.

The target language is fixed for each command-line run. In the Gradio application, changing the target language will replace the conversation and its history while keeping the engine loaded.

## Translate an English sentence

Continuing in the `~/voice-translator` directory with the active virtual environment, run the script with Spanish as the target language:

```bash
python translate.py Spanish
```

Model initialization can take several seconds. At the prompt, enter:

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

The wording might differ slightly, but the response should contain only a Spanish translation. You can cross-check the meaning with a translation tool such as Google Translate or DeepL. 

Press **Enter** at an empty prompt to exit the script and return to the shell before continuing. Copy the complete Spanish translation for conversion to speech.

## What you've accomplished and what's next

You've set up translation with Gemma 4 E2B. The terminal now shows Spanish translation chunks as Gemma generates them, using one loaded model for the session. 

Next, you'll use Supertonic 3 to convert the Spanish translation into speech.
