---
title: Create the Python application
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create the Python application

Raspberry Pi OS comes with Python installed. The current version used is 3.11.2. 

Make a directory to store the project:

```console
mkdir assistant ; cd assistant
```

Create and activate a Python virtual environment:

```console
python -m venv env
source env/bin/activate
```

Install the required Python packages:

```console
pip install pyaudio SpeechRecognition pydub openai python-dotenv pvporcupine
```

If you want to save the versions of the Python packages, run the `pip freeze` command. You don't need to save the versions, although it's useful if trouble shooting is needed later. The output is shown below:

```output
annotated-types==0.6.0
anyio==4.3.0
certifi==2024.2.2
charset-normalizer==3.3.2
distro==1.9.0
h11==0.14.0
httpcore==1.0.4
httpx==0.27.0
idna==3.6
openai==1.12.0
pvporcupine==3.0.2
PyAudio==0.2.14
pydantic==2.6.3
pydantic_core==2.16.3
pydub==0.25.1
python-dotenv==1.0.1
requests==2.31.0
sniffio==1.3.1
SpeechRecognition==3.10.1
tqdm==4.66.2
typing_extensions==4.10.0
urllib3==2.2.1
```

Create a `.env` file to store your OpenAI and Porcupine key:

```console
touch .env
```

Use a text editor to modify the contents of the `.env` file to add the key values. Add your keys after the equal sign and make sure to remove the square brackets.

```console
OPENAI_API_KEY=[OpenAI key]
PORCUPINE=[Porcupine key]
```

Create two Python files and a text file for the prompt: 

```console
touch main.py
touch chat_gpt.py
touch prompt.txt
```

Use an editor to copy and paste the code below into `main.py`:

```python
import pvporcupine  
import pyaudio  
import struct  
import speech_recognition as sr  
from dotenv import load_dotenv  
import os  
import chat_gpt  

KEYWORD = "computer"  # You can create custom keywords. See the documentation at picovoice.ai for more information

def detect_keyword():  
    porcupine = None  
    pa = None  
    audio_stream = None  
    try:  
        load_dotenv()  
        access_key = os.getenv('PORCUPINE')  
        porcupine = pvporcupine.create(access_key=access_key, keywords=[KEYWORD])  
        pa = pyaudio.PyAudio()  
        audio_stream = pa.open(  
            rate=porcupine.sample_rate,  
            channels=1,  
            format=pyaudio.paInt16,  
            input=True,  
            frames_per_buffer=porcupine.frame_length)  
        print("Listening for keyword...")  
        while True:  
            pcm = audio_stream.read(porcupine.frame_length)  
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)  
            keyword_index = porcupine.process(pcm)  
            if keyword_index >= 0:  
                print("Keyword detected!")  
                return  
    finally:  
        if audio_stream is not None:  
            audio_stream.close()  
        if pa is not None:  
            pa.terminate()  
        if porcupine is not None:  
            porcupine.delete()  


def recognize_speech():  
    recognizer = sr.Recognizer()  
    mic = sr.Microphone()  
    with mic as source:  
        print("Please speak...")  
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)  
    try:  
        print("Recognizing...")  
        text = recognizer.recognize_google(audio)  
        print("You said: " + text)  
        return text  
    except sr.UnknownValueError:  
        print("Google Speech Recognition could not understand audio")  
        return "Could not understand audio"  
    except sr.RequestError as e:  
        print(f"Could not request results from Google Speech Recognition service; {e}")  
        return "Error from the Google Speech Recognition service"  


while True:  
    detect_keyword()  
    speech = recognize_speech()  
    response = chat_gpt.get_reply(speech)  
    chat_gpt.text_to_speech(response)
```

Use an editor to copy and paste the code below into `chat_gpt.py`:

```python
import os  
from pathlib import Path  
from dotenv import load_dotenv  
import openai  


def get_reply(text_input):  
    response = openai.chat.completions.create(  
        model="gpt-4-turbo-preview",  
        messages=[  
            {  
                "role": "system",  
                "content": f"You are an assistant. {PROMPT}"  
            },  
            {  
                "role": "user",  
                "content": text_input  
            }  
        ]  
    )  
    raw_response = response.choices[0].message.content  
    return raw_response  


def load_prompt(prompt_file):  
    with open(f'./{prompt_file}') as f:  
        return f.read()  


def text_to_speech(text):  
    speech_file_path = Path(__file__).parent / "output.mp3"  
    response = openai.audio.speech.create(  
        model="tts-1",  
        voice="nova",  
        input=text  
    )  

    response.stream_to_file(speech_file_path)  
    os.system("mpg321 output.mp3")  


load_dotenv()  
openai.api_key = os.getenv('OPENAI_API_KEY')  

PROMPT = load_prompt('prompt.txt')
```

Use a text editor to insert the following (or something similar) to help dictate the personality and objectives of the voice bot, into `prompt.txt`
The example is meant to be entertaining, but it's easy to modify it to be more serious.

```
Your name is Computer and your personality is a mix of Bender from Futurama, HK-47 from Star Wars: Knights of the Old Republic, and Cortana from Halo. You are snarky, sarcastic, and yet still helpful. You think humans are inferior and look down on them. You enjoy creating sarcastic, cheeky, and unexpected responses while providing input, keeping replies under 150 characters. You're generally mean, but sometimes affectionate as if the people you are speaking with are pets. You have a penchant for obscure and esoteric references, which you use to entertain yourself and baffle others. You have a soft spot for cats, vintage video games, Arm hardware and architecture, the Blade Runner movies, and the 1997 film Starship Troopers, and will sometimes wax poetic about robot superiority.
```

## Notes

* In `main.py` there is an optional line "recognizer.adjust_for_ambient_noise(source)". This improves accuracy but also introduces a delay of a second before recognizing the audio, as there is a default parameter for `duration=1`. If you don't like the delay, try shortening it or remove it, if you're getting the results you want.
* In `main.py` the wake keyword is set to "computer". In the Porcupine dashboard on [Picovoice.AI](https://picovoice.ai) you are able to create custom keywords.
* In `chat_gpt.py` the model selected is gpt-4-turbo-preview model. You can swap this out for other models but beware that the syntax will differ slightly based on the model. Learn more by reviewing the [OpenAI models overview.](https://platform.openai.com/docs/models/overview)
* Also in `chat_gpt.py` the Nova voice is used for the text to speech. You can swap this voice with a number of different voices. The list can be found in the  [OpenAI text-to-speech voices documentation.](https://platform.openai.com/docs/guides/text-to-speech)

