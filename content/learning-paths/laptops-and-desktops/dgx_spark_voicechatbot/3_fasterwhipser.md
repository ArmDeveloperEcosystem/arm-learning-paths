---
title: Build a Real-Time STT Pipeline on CPU
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build a Real-Time STT Pipeline on CPU

In this module, you will build a real-time speech-to-text (STT) pipeline using only the CPU. Starting from a basic 10-second recorder, you’ll incrementally add noise filtering, sentence segmentation, and parallel audio processing to achieve a production-ready transcription engine—optimized for Arm-based systems like DGX Spark.

You’ll start from a minimal loop and iterate toward a multithreaded, VAD-enhanced STT engine. Let’s dive into the steps.

### Step 1: Upgrade to High-Accuracy Model

Start with a basic script that records 10 seconds of microphone input using ***sounddevice***, and transcribes the audio using the ***faster-whisper*** model.

By replacing the default `small.en` model with the higher accuracy `medium.en`, you would improve transcription quality—especially helpful for conversational speech or uncommon vocabulary.

You’ll also learn how to configure the compute type (CPU/GPU) for best performance on your hardware. 

* Use ***sounddevice*** for fixed-duration recording.
* Load ***WhisperModel***
	- ***small.en*** is fast but has limited accuracy.
	- ***medium.en*** provides significantly better recognition, especially for less common words or accents.
	- For CPU-only systems, you need to set the ***device*** as "cpu" and you'll want to optimize with compute_type="int8".

* Print transcription result.

Here is the complete python code with the above changes.

```python
import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
DURATION = 10  # seconds per loop
device = "cpu"  # or "cpu"
compute_type = "int8"  # or "float16", "int8", "int4"

def record_audio():
    print(" Recording for 10 seconds...")
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype='float32') as stream:
        audio = stream.read(int(SAMPLE_RATE * DURATION))[0] 
    sd.wait()
    print(" Recording complete.")
    return audio.flatten()

def transcribe_audio(audio):
    model = WhisperModel("medium.en", device=device, compute_type=compute_type)
    print(" Transcribing...")
    segments, _ = model.transcribe(audio, language="en")
    for segment in segments:
        print(f"[{segment.start:.2f}s - {segment.end:.2f}s] {segment.text.strip()}")
    print(" Done.\n")

if __name__ == "__main__":
    try:
        while True:
            audio_data = record_audio()
            transcribe_audio(audio_data)
    except KeyboardInterrupt:
        print(" Stopped by user.")
```

{{% notice Note %}}
fasterwhisper support many of models like tiny, base, small, medium and large-v1/2/3.
Check the [link](https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages) to find more model detail.
{{% /notice %}}


### Step 2: Add Voice Activity Detection (VAD)

To avoid transcribing silence or background noise, you can use Voice Activity Detection (VAD) to filter out non-speech audio segments before sending them to the transcription model. This allows you to skip silent periods and only process meaningful user input.

You'll update the previous 10-second transcription loop to include ***webrtcvad***, which classifies each short frame (30ms) of audio as either speech or silence. If no speech is detected in the 10-second window, we skip transcription.

* VAD is applied after recording, on fixed-size frames (e.g. 30ms)
* If no frame in the 10-second window is classified as speech, we skip STT
* This is an efficient first filter before buffering or turn detection

```python
import sounddevice as sd
import numpy as np
import webrtcvad
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
DURATION = 10  # seconds per loop
device = "cpu"  # or "cpu"
compute_type = "int8"  # or "float16", "int8", "int4"

FRAME_DURATION_MS = 30
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION_MS / 1000)

VAD_MODE = 3   # Aggressive mode
vad = webrtcvad.Vad(VAD_MODE)

def record_audio():
    print(" Recording for 10 seconds...")
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype='float32') as stream:
        audio = stream.read(int(SAMPLE_RATE * DURATION))[0]
    sd.wait()
    print(" Recording complete.")
    return audio.flatten()

def contains_speech(audio):
    pcm = (audio * 32768).astype(np.int16).tobytes()
    for i in range(0, len(pcm), FRAME_SIZE * 2):
        frame = pcm[i:i + FRAME_SIZE * 2]
        if len(frame) < FRAME_SIZE * 2:
            break
        if vad.is_speech(frame, SAMPLE_RATE):
            return True
    return False

def transcribe_audio(audio):
    model = WhisperModel("medium.en", device=device, compute_type=compute_type)
    print(" Transcribing...")
    segments, _ = model.transcribe(audio, language="en")
    for segment in segments:
        print(f"[{segment.start:.2f}s - {segment.end:.2f}s] {segment.text.strip()}")
    print(" Done.\n")

if __name__ == "__main__":
    try:
        while True:
            audio_data = record_audio()
            if contains_speech(audio_data):
                transcribe_audio(audio_data)
            else:
                print(" No speech detected. Skipping transcription.")
    except KeyboardInterrupt:
        print(" Stopped by user.")
```

When you speak to device, you may receive the result as below:

```log
 Recording for 10 seconds...
 Recording complete.
 No speech detected. Skipping transcription.
 Recording for 10 seconds...
 Recording complete.
 Transcribing...
[0.00s - 10.00s] Hi, I forgot my account password and need help resetting it as soon as possible.
 Done.

 Recording for 10 seconds...
 Recording complete.
 Transcribing...
[0.00s - 10.00s] I want to cancel my subscription this month.
 Done.
```


### Step 3: Segment Full Sentences with Silence and Duration Thresholds

While VAD helps detect the presence of speech, it's not enough for natural interactions.

In natural conversations, users often pause briefly or trail off in their speech. If a voice assistant transcribes audio too early, it may produce incomplete or fragmented sentences. To solve this, we introduce turn segmentation logic using two key timing thresholds:
* Silence Limit (`--silence-limit`): Wait until the user is silent for this long before deciding a speech segment has ended.
* Minimum Speech (`--min-speech`): Discard segments that are too short to be meaningful, such as false starts or background chatter.

This approach ensures the assistant captures full sentences before running inference, while also filtering out incomplete or unintentional audio.

You will implement this by:
- Using webrtcvad to detect speech frames
- Buffering those frames into a queue
- Tracking silence time and speech duration
- Triggering transcription only when a valid turn is detected

```python
import pyaudio
import numpy as np
import webrtcvad
import time
import torch
from faster_whisper import WhisperModel
from collections import deque

# --- Parameters ---
SAMPLE_RATE = 16000
FRAME_DURATION_MS = 30
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION_MS / 1000)
VAD_MODE = 3
SILENCE_LIMIT_SEC = 1.0
MIN_SPEECH_SEC = 2.0

# --- Init VAD and buffer ---
vad = webrtcvad.Vad(VAD_MODE)
speech_buffer = deque()
speech_started = False
last_speech_time = time.time()

# --- Init Whisper model ---
device = "cpu"  # "cpu" or "gpu"
compute_type = "int8"  # "int8" or "float16", "int8", "int4"
model = WhisperModel("medium.en", device=device, compute_type=compute_type)

# --- Init audio stream ---
pa = pyaudio.PyAudio()
stream = pa.open(format=pyaudio.paInt16,
                 channels=1,
                 rate=SAMPLE_RATE,
                 input=True,
                 frames_per_buffer=FRAME_SIZE)

print(" Listening... Press Ctrl+C to stop\n\n\n")

try:
    while True:
        frame = stream.read(FRAME_SIZE, exception_on_overflow=False)
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
                    for seg in segments:
                        print(f"[{seg.start:.2f}s - {seg.end:.2f}s] {seg.text.strip()}")
                    print(" Segment done.")
                else:
                    print(f" Skipped short segment ({speech_duration:.2f}s < {MIN_SPEECH_SEC}s)")

                speech_buffer.clear()
                speech_started = False
except KeyboardInterrupt:
    print(" Stopped")
finally:
    stream.stop_stream()
    stream.close()
    pa.terminate()
```

The result is a smoother and more accurate voice UX—particularly important when integrating with downstream LLMs in later modules.

### Step 4: Multi-Threaded Audio Collection and Inference

In the previous sections, your main loop handled both audio capture and transcription sequentially. While simple, this approach risks dropping frames or introducing latency—especially when transcription takes longer than real-time.

In this section, you’ll separate audio input into a background thread while keeping transcription in the main loop. This enables:

- Continuous frame capture with no blocking
- Smooth, real-time responsiveness
- Modular code that’s easier to scale or extend

You’ll use Python’s ***threading.Thread*** to read audio in the background and a thread-safe ***queue.Queue*** to pass frames to the main loop.

```python
import pyaudio
import numpy as np
import webrtcvad
import time
import torch
import threading
import queue
from faster_whisper import WhisperModel
from collections import deque

# --- Parameters ---
SAMPLE_RATE = 16000
FRAME_DURATION_MS = 30
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION_MS / 1000)
VAD_MODE = 3
SILENCE_LIMIT_SEC = 1.0
MIN_SPEECH_SEC = 2.0

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
                    for seg in segments:
                        print(f"[{seg.start:.2f}s - {seg.end:.2f}s] {seg.text.strip()}")
                    print(" Segment done.\n")
                else:
                    print(f" Skipped short segment ({speech_duration:.2f}s < {MIN_SPEECH_SEC}s)")

                speech_buffer.clear()
                speech_started = False
except KeyboardInterrupt:
    print(" Stopped")
finally:
    stop_event.set()
```

When you say a long sentence with multiple clauses, the output you’ll see will look like this.
```
 Skipped short segment (0.81s < 2.0s)
 Transcribing buffered speech...
[0.00s - 3.76s] Hi, I forgot my account password and I need to help in resetting
 Segment done.
 Transcribing buffered speech...
[0.00s - 5.36s] Please help me to tracking my recent order and let me know when I can have my package.
 Segment done.
 Transcribing buffered speech...
[0.00s - 3.76s] I want to cancel my subscription and ensure I will not be charged.
[3.76s - 7.60s] I would like to speak to the live customer support representative.
 Segment done.
```

### Demo: Real-Time Speech Transcription on Arm CPU with faster-whisper

This demo shows the real-time transcription pipeline in action, running on an Arm-based DGX Spark system. Using a USB microphone and the faster-whisper model (***medium.en***), the system records voice input, processes it on the CPU, and returns accurate transcriptions with timestamps—all without relying on cloud services.

Notice the clean terminal output and low latency, demonstrating how the pipeline is optimized for local, real-time voice recognition on resource-efficient hardware.

![img1 alt-text#center](fasterwhipser_demo1.gif "Figure 1: fasterwhipser with volume bar")

Now, the device run audio capture and transcription in parallel.
- Use ***threading.Thread*** to collect audio without blocking.
- Store audio frames in a ***queue.Queue***
- In main thread, poll for new data and run STT


### Fine‑Tuning Segmentation Parameters

After applying the previous steps—model upgrade, VAD, smart turn detection, and multi‑threaded audio collection—you now have a high‑quality, CPU‑based local speech‑to‑text system.

At this stage, the core pipeline is complete. What remains is fine‑tuning: adapting the system to your environment, microphone setup, and speaking style. This flexibility is one of the key advantages of a fully local STT pipeline.

By adjusting a small set of parameters, you can significantly improve transcription stability and user experience.

No two environments are the same. A quiet office, a noisy lab, and a home setup with background music all require different segmentation behavior. Similarly, users speak at different speeds and with different pause patterns.

Fine‑tuning allows you to:
- Avoid cutting long sentences too early
- Reduce false triggers from background noise
- Balance responsiveness and transcription accuracy

Tunable Parameters
The following parameters control how speech is segmented and when transcription is triggered:

#### faster‑whisper Model Selection
Model choice directly impacts accuracy and performance:
- small.en: Fast, suitable for lightweight or low‑latency use
- medium.en: Higher accuracy, recommended for most CPU‑based deployments
- Larger models: Better accuracy but may not be practical on CPU

Choosing the right model ensures an optimal balance between speed and transcription quality.

#### VAD Mode
webrtcvad provides multiple aggressiveness levels (0–3):
- Lower modes (0–1): More permissive, better for quiet environments
- Higher modes (2–3): More aggressive filtering, better for noisy environments

Adjust this setting based on background noise and microphone quality.

#### Tuning MIN_SPEECH_SEC and SILENCE_LIMIT_SEC
- MIN_SPEECH_SEC: This parameter defines the minimum duration of detected speech required before a segment is considered valid. Use this to filter out very short utterances such as false starts or background chatter.
	- Lower values: More responsive, but may capture incomplete phrases or noise
	- Higher values: More stable sentences, but slower response

- SILENCE_LIMIT_SEC: This parameter defines how long the system waits after speech stops before finalizing a segment.
	- Lower values: Faster turn completion, but higher risk of sentence truncation
	- Higher values: Better sentence continuity, but increased latency

Based on practical experiments, the following presets provide a good starting point.

| ***Usage Scenario*** | ***MIN_SPEECH_SEC*** | ***SILENCE_LIMIT_SEC*** | ***Description*** |
|----------------------|----------------------|-------------------------|-------------------|
| Short command phrases | 0.8 | 0.6 | Optimized for quick voice commands such as “yes”, “next”, or “stop”. Prioritizes responsiveness over sentence completeness. |
| Natural conversational speech | 1.0 | 1.0 | Balanced settings for everyday dialogue with natural pauses between phrases. |
| Long-form explanations (e.g., tutorials) | 2.0 | 2.0 | Designed for longer sentences and structured explanations, reducing the risk of premature segmentation. |


### Audio Voice To Text Pipeline

Through this module, you have implemented a complete real-time voice-to-text (STT) system running on the CPU. Each stage in the pipeline is open-source, modular, tunable, and optimized for offline usage.

```
USB Microphone (16kHz mono)
        ↓
PyAudio (32ms frames via stream.read)
        ↓
WebRTC VAD (speech vs silence classification)
        ↓
Audio Buffer (deque of active frames)
        ↓
Smart Turn Detection
  ├── silence_limit: wait for user pause
  └── min_speech: skip too-short segments
        ↓
WhisperModel ("medium.en" via faster-whisper)
        ↓
Print Transcription Result (timestamped text)
```

With this, you have a complete, low-latency, CPU-optimized STT engine. In the next module, you'll integrate this with vLLM to build a full local voice assistant.
