---
title: Connect speech recognition to vLLM for real-time voice interaction
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Integrate STT with vLLM for voice interaction

Now that both faster-whisper and vLLM are working independently, it's time to connect them into a real-time speech-to-response pipeline. Your system will listen to live audio, transcribe it, and send the transcription to vLLM to generate an intelligent reply - all running locally without cloud services.

### Dual process architecture: vLLM and STT

For a robust and production-aligned architecture, separate the system into two independent processes:
- vLLM Server (in Docker): Hosts the large language model, optimized for GPU inference. It can run standalone and be reused across multiple services.
- STT Client (Python): A lightweight CPU-based process that captures microphone input, runs transcription, and sends queries to the vLLM server over HTTP.

This separation has several advantages:

- Modularity: STT and LLM logic can be developed, updated, or debugged independently.
- Flexibility: Restart or refine your STT pipeline without touching the model backend.
- Performance Isolation: GPU-heavy inference doesn't block audio input or local UI logic.
- Production Alignment: Mirrors real-world architectures like client-server or microservices.

### Launch vLLM and connect to STT

#### Launch vLLM (in Docker)

Separating container startup from model launch provides greater control and improves development experience.

By launching the container first, you can troubleshoot errors like model path issues or GPU memory limits directly inside the environment, without the container shutting down immediately. It also speeds up iteration: you avoid reloading the entire image each time you tweak settings or restart the model.

This structure also improves visibility. You can inspect files, monitor GPU usage, or run diagnostics like `curl` and `nvidia-smi` inside the container. Breaking these steps apart makes the process easier to understand, debug, and extend.

Start the Docker container:

```bash
export LATEST_VLLM_VERSION=25.11-py3
docker run --gpus all \
    -p 8000:8000 \
    -v $HOME/models:/models \
    -e NVIDIA_VISIBLE_DEVICES=all \
    -it nvcr.io/nvidia/vllm:${LATEST_VLLM_VERSION} bash
```

Inside the container, launch vLLM:

```bash
vllm serve /models/mistral-7b \
    --quantization gptq \
    --gpu-memory-utilization 0.9 \
    --max-num-seqs 8 \
    --dtype float16
```

Look for "Application startup complete." in the output:

```output
(APIServer pid=1) INFO:     Started server process [1]
(APIServer pid=1) INFO:     Waiting for application startup.
(APIServer pid=1) INFO:     Application startup complete.
```

The vLLM server is now live and ready to accept HTTP requests.

#### Extend STT Python to connect vLLM for instant AI responses

Now that you've implemented a real-time speech recognizer, extend the pipeline by connecting it to a local language model (LLM) powered by vLLM.

You'll convert the STT result into a message prompt, send it to the running vLLM server via HTTP, dynamically estimate max_tokens based on input length, and print the model's reply next to the transcribed speech.

Set up the LLM endpoint and model reference by adding the following variables at the top of your script:

```python
VLLM_ENDPOINT = "http://localhost:8000/v1/chat/completions"
MODEL_NAME = "/models/mistral-7b"
```

Make sure these match the vLLM server you launched in the previous step.

After transcribing the user's speech, send the result to the vLLM server by formatting it as a chat prompt.

```python
user_text = " ".join([seg.text.strip() for seg in segments]).strip()
```

Estimate token length and send the request:

```python
max_tokens = min(256, max(64, len(user_text.split()) * 5))
response = requests.post(VLLM_ENDPOINT, json={
    "model": MODEL_NAME,
    "messages": [{"role": "user", "content": user_text}],
    "max_tokens": max_tokens
})
```

Extract the assistant's reply from the vLLM API response:

```python
result = response.json()
reply = result["choices"][0]["message"]["content"].strip()
```

Display both the transcribed input and the model's response:

```python
...
print(f"\n User: {user_text}\n")
...
print(f" AI  : {reply}\n")
```

This architecture mirrors the OpenAI Chat API design, enabling future enhancements like system-level prompts, multi-turn history, or role-specific behavior.

{{% notice tip %}}
If you encounter a "model doesn't exist" error, double-check the model path you used when launching vLLM. It must match MODEL_NAME exactly.
{{% /notice %}}

Switch to another terminal and save the following Python code in a file named `stt-client.py`:

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

                    max_tokens = 128
                    response = requests.post(VLLM_ENDPOINT, json={
                        "model": MODEL_NAME,
                        "messages": [
                            {"role": "user", "content": user_text}
                        ],
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

Run the code using:

```bash
python3 ./stt-client.py
```

#### Interact with the chatbot

Once both your vLLM server and Python STT script are running correctly, you'll see output like the following in your terminal.

Each time you speak a full sentence (based on your silence and segment thresholds), the system transcribes your speech, displays the recognized text, and shows the model's reply in natural language.

If your input is too short (a false trigger or background noise spike), you'll see a message like:

```
Skipped short segment (1.32s < 2.0s)
```

This means your speech did not meet the MIN_SPEECH_SEC threshold. You can adjust this value to make the system more or less sensitive.

An example when asking the assistant for a joke:

```
 Listening... Press Ctrl+C to stop
 Skipped short segment (0.39s < 2.0s)
 Skipped short segment (1.44s < 2.0s)
 Skipped short segment (1.89s < 2.0s)
 Skipped short segment (1.77s < 2.0s)
 Skipped short segment (0.36s < 2.0s)
 Transcribing buffered speech...

 Listening... Press Ctrl+C to stop
 Transcribing buffered speech...

 User: Hello, please tell me the joke.

 AI  : Of course, I'd be happy to tell you a joke! Here's a classic one:

Why don't libraries smell like popcorn?

Because they are full of books, not movies!

I hope that brings a smile to your face. If you have any other requests, feel free to ask!
```

If your input is too short, you'll see:

```
Skipped short segment (1.32s < 2.0s)
```

{{% notice Tip %}}You can fine-tune these parameters in future sections to better fit your speaking style or environment.{{% /notice %}}

## What you've accomplished and what's next

You've successfully built a complete voice-to-AI-response loop: microphone input is captured in real time, transcribed locally using faster-whisper on CPU, forwarded to a local vLLM server running on GPU, and receives intelligent responses with low latency.

This foundation supports a wide range of customizations where you can build customer-specific workflows with prompt engineering and multi-turn memory.
