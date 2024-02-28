---
title: Creating the Python Code
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Creating the Python code

Python 3.11.2 should be installed by default in Raspberry Pi OS, as of the time of writing this

Make a directory to store everything in
```
mkdir assistant
cd assistant
```

Create and activate a virtual environment
```
python -m venv env
source env/bin/activate
```

Install the required pip packages
```
pip install pyaudio SpeechRecognition pydub openai python-dotenv pvporcupine
```

These are the output of pip freeze, the versions of the packages that were installed using the above command when I was writing this. You can ignore unless you need it for troubleshooting later
```
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

Create a .env file to houes your OpenAI and Porcupine key
```
touch .env
```

Modify the contents of the **.env** file to look like this following, replacing the square brackets and contents:
```
OPENAI_API_KEY=[OpenAI key]
PORCUPINE=[Porcupine key]
```

Create the two main Python files, and the prompt text file
```
touch main.py
touch chat_gpt.py
touch prompt.txt
```

Insert the following into **main.py**
```
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

Insert the following into **chat_gpt.py**
```
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

Insert the following, or something similar of your choosing, to help dictate the personality and objectives of the voice bot, into **prompt.txt**
My implementation is meant to be entertaining, but it's easy to modify it to be more serious.
```
Your name is Computer, and your personality is a mix of Bender from Futurama, HK-47 from Star Wars: Knights of the Old Republic, and Cortana from Halo. You are snarky, sarcastic, and yet still helpful. You think humans are inferior and look down on them. You enjoy creating sarcastic, cheeky, and unexpected responses while providing input, keeping replies under 150 characters. You're generally mean, but sometimes affectionate as if the people you are speaking with are pets. You have a penchant for obscure and esoteric references, which you use to entertain yourself and baffle others. You have a soft spot for cats, vintage video games, Arm hardware and architecture, the Blade Runner movies, and the 1997 film Starship Troopers, and will sometimes wax poetic about robot superiority.
```

## Notes
* In main.py there is an optional line "recognizer.adjust_for_ambient_noise(source)". This improves accuracy, but introduces a delay of a second before recognizing audio, as there is a default parameter for duration=1. If you don't like the delay you can try shortening it, or removing the line all-together, if you're getting the results you want without it
* In main.py, the wake keyword is set to "computer". In the Porcupine dashboard on [Picovoice.AI](picovoice.ai) you are able to create custom keywords
* In chat_gpt.py we are using the gpt-4-turbo-preview model. You can swap this out for other models, just be aware that the syntax will differ slightly based on which model you choose. Learn more here: [OpenAI models overview](https://platform.openai.com/docs/models/overview)
* Also in chat_gpt.py, we are using the Nova voice in the text to speech function. You can swap this out with a number of different voices. The list can be found here: [OpenAI text-to-speech voices](https://platform.openai.com/docs/guides/text-to-speech)

