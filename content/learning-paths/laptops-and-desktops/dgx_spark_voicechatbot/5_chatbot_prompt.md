---
title: Specializing Offline Voice Assistants for Customer Service
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Specializing Offline Voice Assistants for Customer Service

In the previous module, you built a fully offline voice assistant by combining local speech-to-text (STT) with ***vLLM*** for language generation.

Now, we’ll focus on transforming that general-purpose chatbot into a task-specific customer service agent—designed to deliver fast, focused, and context-aware assistance.

### Why Adapt for Customer Support?

Unlike open-domain chatbots, customer-facing assistants must meet stricter communication standards:

- ***Quick Responses***: Each voice input must trigger a fast and relevant reply—no long pauses or uncertainty.

- ***Clear and Concise Output***: Users expect direct answers, not verbose or vague explanations.

- ***Context Awareness***: The assistant should remember previous questions or actions to support multi-turn interactions.

These needs are especially relevant for questions like:

* “Hi, I forgot my account password and need help resetting it.”
* “Can you track my recent order and tell me when it will arrive?”
* “I’d like to speak to a live agent about a billing issue.”
* “Why was I charged twice this month?”
* “I want to cancel my subscription and avoid future charges.”

Such queries require more than just language generation—they demand structured behavior and task memory.

### What You’ll Build in This Module

You’ll enhance your assistant with three critical upgrades:

1. ***Role-Specific System Prompts***

Define your assistant’s personality and responsibilities (e.g., support agent, coach, guide) through system messages. Learn how prompt engineering influences tone, detail level, and actionability.

2. ***Multi-Turn Memory***

Enable the assistant to recall recent interactions and respond within context. You’ll manage a rolling history of messages while avoiding token overflow.

3. ***(Optional) Secure Knowledge Retrieval***

Explore how to integrate local company data using vector search—allowing the assistant to answer questions based on private documents, without ever sending data to the cloud.

This prepares your system for high-trust environments like:
- Enterprise customer support
- Internal help desks
- Regulated industries (healthcare, finance, legal)

By the end of this module, your assistant will behave more like a real support agent—able to respond quickly, maintain context, and optionally access internal knowledge to resolve complex requests.


## Controlling AI Behavior with System Prompts

To make your AI assistant behave like a domain expert—such as a support agent or tour guide—you need more than just language generation. You need instructional control.

In OpenAI-compatible APIs (like vLLM), you can provide a special message with the role set to ***"system"***. This message defines the behavior and tone of the assistant before any user input is processed.

A system prompt is like giving your assistant a role to play — such as:

- A polite and helpful customer service agent
- A knowledgeable tour guide
- A motivational fitness coach

By customizing the system prompt, you can:

- Shape the assistant’s language and tone
- Restrict or expand the type of information it shares
- Align responses with business needs (e.g., short and precise for help desks)


### Step 1: Define the System Prompt Behavior

To turn your general-purpose voice assistant into a focused role-specific agent, you must guide the language model’s behavior. This is done by defining a system prompt that acts as a task instruction.

For example: 
***Support Agent***
```bash
You are a professional customer support assistant. Always prioritize clarity and solve customer issues politely and efficiently.
```

***Fitness Coach***
```bash
You are a friendly and motivational fitness coach. Offer helpful workout tips and health advice.
```

***Tour Guide***
```bash
You are an enthusiastic travel guide. Recommend popular tourist destinations and answer cultural questions clearly.
```

In this learning path, we use customer service as an example.
Add the following at the top of your script:

```bash
SYSTEM_PROMPT = """You are a professional customer support assistant.
Respond politely, clearly, and concisely.
Focus on solving the user's issue.
Do not include unnecessary apologies or long explanations.
If required information is missing, ask a clear follow-up question."""
```

This prompt guides the model to respond clearly—even when the user’s input is vague—by reducing ambiguity, maintaining a consistent tone, and helping the assistant stay on topic, concise, and solution-oriented.

### Step 2: Inject the Role Instruction into the User Message

Instead of sending a separate "system" role—which may cause vLLM to return a formatting error—you can prepend the role instruction directly into the user’s message.

This lets you keep control over the assistant’s behavior, while maintaining compatibility with vLLM’s expected message format.

Locate the following code in previous Python code.
```bash
"messages": [
    {"role": "user", "content": user_text}
]
```

Add ***SYSTEM_PROMPT*** begin of the messages. 

```python
messages = [
    {"role": "user", "content": SYSTEM_PROMPT + "\n\n" + user_text}
]
```

This line does two things:
1. It embeds your desired assistant role (e.g., customer support) directly into the input.
2. It ensures that vLLM treats the message as valid—alternating roles correctly between user and assistant.

By combining prompt and question, the assistant behaves like a helpful agent without triggering message formatting errors.


### Step 3: Choosing the Right Response Length for Each Role

Different assistant roles require different response styles. A customer service agent should be concise and focused, while a tour guide or teacher may need to provide more elaboration.

To control the response length dynamically, we calculate max_tokens using this formula:

```python
max_tokens = min(512, max(64, len(user_text.split()) * 5))
```

Let’s break it down:
- ***len(user_text.split()):*** counts how many words the user spoke
- * 5: estimates about 5 tokens per word (a rough average)
- ***max():*** ensures a minimum of 64 tokens to avoid overly short responses
- ***min():*** caps the response length to 512 tokens to avoid delays or exceeding model limits

This gives you a balanced reply size that grows with input length but stays within safe bounds.

{{% notice tip %}}
You can reference this formula based on role:
Customer support: shorter replies, use max_tokens = 256 for snappy responses
Tour guide / teacher: more verbose, try max_tokens = 384 or higher
FAQ retrieval: adjust based on expected answer complexity
{{% /notice %}}


The full version of code will be:

```python
import pyaudio
import numpy as np
import webrtcvad
import time
import torch
import threading
import queue
import requests
from faster_whisper import WhisperModel
from collections import deque

# --- Parameters ---
SAMPLE_RATE = 16000
FRAME_DURATION_MS = 30
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION_MS / 1000)
VAD_MODE = 3
SILENCE_LIMIT_SEC = 1.0
MIN_SPEECH_SEC = 2.0
VLLM_ENDPOINT = "http://localhost:8000/v1/chat/completions"
MODEL_NAME = "/models/mistral-7b"

# --- Init VAD and buffers ---
vad = webrtcvad.Vad(VAD_MODE)
speech_buffer = deque()
speech_started = False
last_speech_time = time.time()

# --- Init Thread and Queue ---
audio_queue = queue.Queue()
stop_event = threading.Event()

# --- Init Whisper model ---
device = "cpu"  # "cpu" or "gpu"
compute_type = "int8"  # "int8" or "float16", "int8", "int4"
model = WhisperModel("medium.en", device=device, compute_type=compute_type)

# --- System Prompt ---
SYSTEM_PROMPT = """ You are a professional customer support assistant.
Respond politely, clearly, and concisely.
Focus on solving the user's issue.
Do not include unnecessary apologies or long explanations.
If required information is missing, ask a clear follow-up question."""

# --- Audio capture thread ---
def audio_capture():
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paInt16,
                     channels=1,
                     rate=SAMPLE_RATE,
                     input=True,
                     frames_per_buffer=FRAME_SIZE)
    print(" Listening... Press Ctrl+C to stop")
    try:
        while not stop_event.is_set():
            frame = stream.read(FRAME_SIZE, exception_on_overflow=False)
            audio_queue.put(frame)
    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()

# --- Start audio capture thread ---
threading.Thread(target=audio_capture, daemon=True).start()

# --- Main loop: process queue and transcribe ---
try:
    while True:
        if audio_queue.empty():
            time.sleep(0.01)
            continue

        frame = audio_queue.get()
        is_speech = vad.is_speech(frame, SAMPLE_RATE)

        if is_speech:
            speech_buffer.append(frame)
            speech_started = True
            last_speech_time = time.time()
        elif speech_started:
            speech_duration = len(speech_buffer) * (FRAME_DURATION_MS / 1000.0)
            silence_duration = time.time() - last_speech_time

            if silence_duration > SILENCE_LIMIT_SEC:
                if speech_duration >= MIN_SPEECH_SEC:
                    print(" Transcribing buffered speech...")
                    audio_bytes = b"".join(speech_buffer)
                    audio_np = np.frombuffer(audio_bytes, dtype=np.int16).astype(np.float32) / 32768.0

                    segments, _ = model.transcribe(audio_np, language="en")
                    user_text = " ".join([seg.text.strip() for seg in segments]).strip()
                    print(f"\n User: {user_text}\n")

                    max_tokens = min(512, max(64, len(user_text.split()) * 5))

                    messages = [
                        {"role": "user", "content": SYSTEM_PROMPT + "\n\n" + user_text}
                    ]

                    response = requests.post(VLLM_ENDPOINT, json={
                        "model": MODEL_NAME,
                        "messages": messages,
                        "max_tokens": max_tokens
                    })

                    result = response.json()                    
                    if "choices" not in result:
                        print(" Error from vLLM:", result.get("error", "Unknown error"))
                        continue
                    reply = result["choices"][0]["message"]["content"].strip()
                    print(f" AI  : {reply}\n")
                else:
                    print(f" Skipped short segment ({speech_duration:.2f}s < {MIN_SPEECH_SEC}s)")

                speech_buffer.clear()
                speech_started = False
except KeyboardInterrupt:
    print(" Stopped")
finally:
    stop_event.set()
```

This approach works well for single-turn interactions.
In the next section, you’ll extend this pattern to multi-turn conversations, storing and managing multiple rounds of user and assistant prompts.
