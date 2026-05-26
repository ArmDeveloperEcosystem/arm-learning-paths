---
title: Run inference with vLLM
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run inference on LLama3.1-8B

vLLM serves an OpenAI-compatible API that you use to run inference on Llama3.1-8B. This confirms that the local environment is set up correctly.

Start vLLM’s OpenAI-compatible API server using Llama3.1-8B:
```bash
vllm serve meta-llama/Llama-3.1-8B
```

The server prints its available routes and then confirms it's ready:

```output
(APIServer pid=27612) INFO 05-18 15:00:06 [api_server.py:602] Starting vLLM server on http://0.0.0.0:8000
(APIServer pid=27612) INFO 05-18 15:00:06 [launcher.py:37] Available routes are:
(APIServer pid=27612) INFO 05-18 15:00:06 [launcher.py:46] Route: /openapi.json, Methods: HEAD, GET
(APIServer pid=27612) INFO 05-18 15:00:06 [launcher.py:46] Route: /v1/chat/completions, Methods: POST
(APIServer pid=27612) INFO 05-18 15:00:06 [launcher.py:46] Route: /v1/completions, Methods: POST
...
(APIServer pid=27612) INFO:     Application startup complete.
```

Wait until you see `Application startup complete` before continuing. The server is now listening on port 8000. Open a new terminal to run the client script while the server continues running in the first terminal.

Then create a test script that sends a request to the server using the OpenAI library. Copy the Python script below to a file named `llama_test.py`:

```python
import time
from openai import OpenAI
from transformers import AutoTokenizer

# vLLM's OpenAI-compatible server
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")  # api_key is required by the OpenAI client but not validated by vLLM

model = "meta-llama/Llama-3.1-8B"   # vllm server model

# Define a chat template for the model
# vLLM's /v1/completions endpoint does not auto-apply the model's chat template, so it must be applied manually
llama3_template = "{% set loop_messages = messages %}{% for message in loop_messages %}{% set content = '<|start_header_id|>' + message['role'] + '<|end_header_id|>\n\n'+ message['content'] | trim + '<|eot_id|>' %}{% if loop.first and message['role'] != 'system' %}{{ '<|start_header_id|>system<|end_header_id|>\n\n'+ 'You are a helpful assistant.' + '<|eot_id|>' }}{% endif %}{{ content }}{% endfor %}{{ '<|start_header_id|>assistant<|end_header_id|>\n\n' }}"

# Define your prompt
message = [{"role": "user", "content": "Explain Big O notation with two examples."}]

def run(prompt):
    resp = client.completions.create(
        model=model,
        prompt=prompt,
        max_tokens=128,  # The maximum number of tokens that can be generated in the completion
    )
    return resp.choices[0].text

def main():
    t0 = time.time()

    tokenizer = AutoTokenizer.from_pretrained(model)
    tokenizer.chat_template = llama3_template
    prompt = tokenizer.apply_chat_template(message, tokenize=False)
    result = run(prompt)

    print(f"\n=== Output ===\n{result}\n")
    print(f"Batch completed in : {time.time() - t0:.2f}s")

if __name__ == "__main__":
    main()
```

Now run the script with:
```bash
python llama_test.py
```

The output is similar to:

```output
=== Output ===
Big O notation is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity. It is a member of a family of notations invented by Paul Bachmann, Edmund Landau, and others, collectively called Bachmann–Landau notation or asymptotic notation.

In computer science, big O notation is used to classify algorithms according to how their run time or space requirements grow as the input size grows. In analytic number theory, big O notation is often used to express a bound on the difference between an arithmetical function and a better understood approximation; a famous example of such a difference

Batch completed in : 16.50s
```

The response is truncated at 128 tokens, which is why the explanation cuts off mid-sentence — this is controlled by the `max_tokens=128` parameter in the script. In the server terminal you can also see throughput metrics logged in tokens per second.

You can do the same for the pre-quantized model loaded directly from Hugging Face. Stop the running server first with Ctrl+C, then start the quantized model server:
```bash
vllm serve RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8
```

Wait for the same `Application startup complete` message before continuing:

```output
(APIServer pid=28847) INFO 05-18 15:11:31 [api_server.py:602] Starting vLLM server on http://0.0.0.0:8000
(APIServer pid=28847) INFO 05-18 15:11:31 [launcher.py:37] Available routes are:
(APIServer pid=28847) INFO 05-18 15:11:31 [launcher.py:46] Route: /v1/chat/completions, Methods: POST
(APIServer pid=28847) INFO 05-18 15:11:31 [launcher.py:46] Route: /v1/completions, Methods: POST
...
(APIServer pid=28847) INFO:     Application startup complete.
```

Update your test script `llama_test.py` to use the quantized model:
```python
model = "RedHatAI/Meta-Llama-3.1-8B-quantized.w8a8"  
```

Run inference on the quantized model:
```bash
python llama_test.py
```

The output is similar to:

```output
=== Output ===
$\begin{array}{l}{O}\left({n}^{2}\right)\\ {O}\left({n}^{3}\right)\end{array}$

Please help me with this problem. I don't know where to start. Thank you.

• Questions are typically answered in as fast as 30 minutes

### Plainmath recommends

• $${O}\left({n}^{2}\right)$$
• $${O}\left({n}^{3}\right)$$
###### Not exactly what you're looking for?

Expert community

• Live experts 24/7
• Questions are usually

Batch completed in : 7.93s
```

The quantized model completes the same request in roughly half the time of the non-quantized model — approximately a 2x speedup. The response quality differs between the two models because quantization reduces model precision, which can affect output style and coherence. The quantized model identified the Big O examples but formatted them as if pulling from a Q&A website rather than producing a clean explanation.

You have now run inference using both the non-quantized and quantized Llama3.1-8B models.

## Run inference on Whisper

Use a similar approach to test inference on Whisper models. Stop the running Llama server first with Ctrl+C, then install the required vLLM audio library and start the Whisper server:
```bash
pip install vllm[audio]
```

```bash
vllm serve openai/whisper-large-v3
```

Wait for the server to confirm it's ready. You'll notice the Whisper server exposes audio-specific routes:

```output
(APIServer pid=29957) INFO 05-18 15:21:01 [api_server.py:602] Starting vLLM server on http://0.0.0.0:8000
(APIServer pid=29957) INFO 05-18 15:21:01 [launcher.py:37] Available routes are:
...
(APIServer pid=29957) INFO 05-18 15:21:01 [launcher.py:46] Route: /v1/audio/transcriptions, Methods: POST
(APIServer pid=29957) INFO 05-18 15:21:01 [launcher.py:46] Route: /v1/audio/translations, Methods: POST
...
(APIServer pid=29957) INFO:     Application startup complete.
```

Open a new terminal once you see `Application startup complete`. Then create a test script that sends a request with an audio file to the server using the OpenAI library. Copy the Python script below to a file named `whisper_test.py`.

```python
import time
from openai import OpenAI
from vllm.assets.audio import AudioAsset

# vLLM's OpenAI-compatible server
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")

model = "openai/whisper-large-v3"   # vllm server model

# You can update the below with an audio file of your choosing
audio_filepath=str(AudioAsset("winning_call").get_local_path())

def transcribe_audio():
    with open(audio_filepath, "rb") as audio:
        transcription = client.audio.transcriptions.create(
            model=model, 
            file=audio,
            language="en",
            response_format="json",
            temperature=0.0,
        )
    return transcription.text

def main():
    t0 = time.time()
    out = transcribe_audio()
    print(f"\n=== Output ===\n{out}\n")
    print(f"Batch completed in : {time.time() - t0:.2f}s")

if __name__ == "__main__":
    main()
```

Now run the script with:
```bash
python whisper_test.py
```

The output is similar to:

```output
=== Output ===
 And the 0-1 pitch on the way to Edgar Martinez. Swung on the line. Now the left field line for a base hit. Here comes Joy. Here is Junior to third base. They're going to wave him in. The throw to the plate will be late. The Mariners are going to play for the American League Championship. I don't believe it. It just continues. My, oh, my.

Batch completed in : 31.85s
```

The script uses `AudioAsset("winning_call")`, a sample audio clip bundled with vLLM. The transcription confirms Whisper is processing audio correctly on Arm64.

You can do the same for the pre-quantized Whisper model loaded directly from Hugging Face. Start the server:
```bash
vllm serve RedHatAI/whisper-large-v3-quantized.w8a8
```

Wait for the same `Application startup complete` message before continuing:

```output
(APIServer pid=31658) INFO 05-18 15:27:09 [api_server.py:602] Starting vLLM server on http://0.0.0.0:8000
(APIServer pid=31658) INFO 05-18 15:27:09 [launcher.py:37] Available routes are:
...
(APIServer pid=31658) INFO 05-18 15:27:09 [launcher.py:46] Route: /v1/audio/transcriptions, Methods: POST
(APIServer pid=31658) INFO 05-18 15:27:09 [launcher.py:46] Route: /v1/audio/translations, Methods: POST
...
(APIServer pid=31658) INFO:     Application startup complete.
```

Update your test script `whisper_test.py` to use the quantized model:
```python
model = "RedHatAI/whisper-large-v3-quantized.w8a8"  
```

Run inference on the quantized model:
```bash
python whisper_test.py
```

The output is similar to:

```output
=== Output ===
 And the 0-1 pitch on the way to Edgar Martinez. Swung on the line. Now the left field line for a base hit. Here comes Joy. Here is Junior to third base. They're going to wave him in. The throw to the plate will be late. The Mariners are going to play for the American League Championship. I don't believe it. It just continues. My, oh, my.

Batch completed in : 8.14s
```

The quantized Whisper model completes the same transcription in roughly a quarter of the time — approximately a 4x speedup — while producing an identical transcription. 

## What you've accomplished and what's next

You have installed vLLM and demonstrated you can run inference on your models. Next, you'll benchmark the Llama models and compare their performance.
