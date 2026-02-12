---
title: Install faster-whisper for local speech recognition
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

[faster-whisper](https://github.com/SYSTRAN/faster-whisper) is a high-performance reimplementation of OpenAI Whisper, designed to significantly reduce transcription latency and memory usage. It's well suited for local and real-time speech-to-text (STT) pipelines, especially when running on CPU-only systems or hybrid CPU/GPU environments.

You'll use faster-whisper as the STT engine to convert raw microphone input into structured text. At this stage, the goal is to install faster-whisper correctly and verify that it can transcribe audio reliably. Detailed tuning and integration are covered in later sections.

### Install build dependencies

While some Python packages such as sounddevice and webrtcvad previously had compatibility issues with newer Python versions, these have been resolved. Use Python 3.12, which has been tested and confirmed to work reliably with all required dependencies.

Install Python 3.12 and build dependencies:

```bash
sudo apt update
sudo apt install python3.12 python3.12-venv python3.12-dev -y
sudo apt install gcc portaudio19-dev ffmpeg -y
```

## Create and activate Python environment

In particular, [pyaudio](https://pypi.org/project/PyAudio/) (used for real-time microphone capture) depends on the PortAudio library and the Python C API. These must match the version of Python you're using.

Set up an isolated Python environment for your voice assistant project to prevent dependency conflicts and make your installation reproducible.

```bash
python3.12 -m venv va_env
source va_env/bin/activate
python3 -m pip install --upgrade pip
```

Before installing the package, check the Python version in your virtual environment.

```bash
python3 --version
```

Expected output is `3.12.x` or higher:
```log
Python 3.12.3
```

Install required Python packages:

```bash
pip install pyaudio numpy torch faster-whisper
pip install requests webrtcvad sounddevice==0.5.3
```

{{% notice Note %}}
While sounddevice==0.5.4 is available, it introduces callback-related errors during audio stream cleanup that can confuse beginners.
Use sounddevice==0.5.3, which is stable and avoids these warnings.
{{% /notice %}}

Verify the pyaudio version:
```bash
python -c "import pyaudio; print(pyaudio.__version__)"
```

Expected output:
```log
0.2.14
```

### Verify microphone input

Once your system dependencies are installed, you can test that your audio hardware is functioning properly. This ensures that your audio input is accessible by Python through the sounddevice module.

Now plug in your USB microphone and create a file named `microphone.py` with the following Python code to verify that it is detected and functioning correctly.

```python
import sounddevice as sd
import numpy as np

SAMPLE_RATE = 16000 
DURATION = 5

print(" Start recording for 5 seconds...")
with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype='float32') as stream:
    audio = stream.read(int(SAMPLE_RATE * DURATION))[0]
print(" Recording complete.")

print(" Playing back...")
sd.play(audio, samplerate=SAMPLE_RATE)
sd.wait()
print(" Playback complete.")
```

Run the example code to check the microphone.

```console
python3 ./microphone.py
```

DGX Spark will record the audio for 5 seconds and immediately play back the captured audio.

If you do not hear any playback, check your USB connection and verify the installation steps above.

Once you’ve confirmed that your microphone is working and your environment is set up, you’re ready to test real-time transcription and move on to the next phase.

### Sample: Real-time transcription with faster-whisper

Verify that your Whisper model works with live microphone input. This example records a 10-second audio clip using the system microphone, transcribes it using faster-whisper, and prints the transcribed text with timestamps. 

The code below records a fixed-duration mono audio clip using the sounddevice module and transcribes it using the faster-whisper model. The `record_audio()` function starts the microphone and records a 10-second audio segment, returning the data as a NumPy array. The `WhisperModel("small.en")` call loads the small English model from faster-whisper, using `compute_type="int8"` to ensure compatibility with CPU-only systems. The `transcribe_audio()` function processes the recorded audio and prints the transcription results along with start and end timestamps for each spoken segment. The while True loop continuously records and transcribes in real time until interrupted, allowing you to speak multiple utterances across iterations. The script continues running in 10-second cycles until stopped with Ctrl+C.

Copy the code to a file named `transcribe.py`. 

```python
import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
DURATION = 10  # seconds per loop

def record_audio():
    print(" Recording for 10 seconds...")
    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype='float32') as stream:
        audio = stream.read(int(SAMPLE_RATE * DURATION))[0]  # returns (data, overflow)
    sd.wait()
    print(" Recording complete.")
    return audio.flatten()

def transcribe_audio(audio):
    model = WhisperModel("small.en", device="cpu", compute_type="int8")
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

Run the example code.

```console
python3 ./transcribe.py
```

The output shows the main parts of the program;

```output
Recording for 10 seconds...
 Recording complete.
 Transcribing...
[0.00s - 10.00s] One, two, three, four, five, six, check,
 Done.
 ```

{{% notice Note %}}
To stop the script, press Ctrl+C during any transcription loop. The current 10-second recording completes and transcribes before the program exits cleanly.
Don't use Ctrl+Z, which suspends the process instead of terminating it.
{{% /notice %}}


### Troubleshooting

This section lists common issues you may encounter when setting up local speech-to-text, along with clear checks and fixes.

**Problem 1: Callback-related errors with sounddevice**

If you encounter errors like:

```log
AttributeError: '_CallbackContext' object has no attribute 'data'
```

**Cause:** This is a known issue introduced in sounddevice==0.5.4, related to internal callback cleanup.

**Fix:** Use the stable version:
```bash
pip install sounddevice==0.5.3
```

**Problem 2: No sound playback after recording**

You can record audio without errors, but nothing is played back.

Ensure that your USB microphone or headset is selected as the default input/output device. Also check that the system volume isn't muted.

**Fix:** List all available audio devices:

```bash
python -m sounddevice
```

The output is similar to:
```log
0 NVIDIA: HDMI 0 (hw:0,3), ALSA (0 in, 8 out)
  1 NVIDIA: HDMI 1 (hw:0,7), ALSA (0 in, 8 out)
  2 NVIDIA: HDMI 2 (hw:0,8), ALSA (0 in, 8 out)
  3 NVIDIA: HDMI 3 (hw:0,9), ALSA (0 in, 8 out)
  4 Plantronics Blackwire 3225 Seri: USB Audio (hw:1,0), ALSA (2 in, 2 out)
  5 hdmi, ALSA (0 in, 8 out)
  6 pipewire, ALSA (64 in, 64 out)
  7 pulse, ALSA (32 in, 32 out)
* 8 default, ALSA (64 in, 64 out)
```

If your microphone or headset is listed but not active, try explicitly selecting it in Python:

```bash
import sounddevice as sd
sd.default.device = 4 
```

Other things to try:
- Increase system volume
- Remove the device and plug it in again
- Reboot your system to refresh device mappings

## What you've accomplished and what's next

Once your transcription prints correctly in the terminal and playback works as expected, you’ve successfully completed the setup for local STT using faster-whisper. 

In the next section, you'll enhance this basic transcription loop by adding real-time audio segmentation, turn detection, and background threading to support natural voice interactions.