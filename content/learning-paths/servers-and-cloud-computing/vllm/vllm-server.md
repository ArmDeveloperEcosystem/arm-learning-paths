---
title: Run an OpenAI-compatible server
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Instead of a batch run from Python, you can create an OpenAI-compatible server. This allows you to leverage the power of Large Language Models without relying on external APIs. 

Running a local LLM offers several advantages:

* Cost-effective - it avoids the costs associated with using external APIs, especially for high-usage scenarios.   
* Privacy - it keeps your data and prompts within your local environment, which enhances privacy and security.
* Offline Capability - it enables operation without an internet connection, making it ideal for scenarios with limited or unreliable network access.

OpenAI compatibility means that you can reuse existing software which was designed to communicate with OpenAI and use it to communicate with your local vLLM service.

Run vLLM with the same `Qwen/Qwen2.5-0.5B-Instruct` model:

```bash
python3 -m vllm.entrypoints.openai.api_server --model Qwen/Qwen2.5-0.5B-Instruct --dtype float16
```

The server output displays that it is ready for requests:

```output
INFO 12-12 22:54:40 cpu_executor.py:186] # CPU blocks: 21845
INFO 12-12 22:54:40 llm_engine.py:447] init engine (profile, create kv cache, warmup model) took 0.26 seconds
INFO 12-12 22:54:41 api_server.py:560] Using supplied chat template:
INFO 12-12 22:54:41 api_server.py:560] None
INFO 12-12 22:54:41 launcher.py:19] Available routes are:
INFO 12-12 22:54:41 launcher.py:27] Route: /openapi.json, Methods: HEAD, GET
INFO 12-12 22:54:41 launcher.py:27] Route: /docs, Methods: HEAD, GET
INFO 12-12 22:54:41 launcher.py:27] Route: /docs/oauth2-redirect, Methods: HEAD, GET
INFO 12-12 22:54:41 launcher.py:27] Route: /redoc, Methods: HEAD, GET
INFO 12-12 22:54:41 launcher.py:27] Route: /health, Methods: GET
INFO 12-12 22:54:41 launcher.py:27] Route: /tokenize, Methods: POST
INFO 12-12 22:54:41 launcher.py:27] Route: /detokenize, Methods: POST
INFO 12-12 22:54:41 launcher.py:27] Route: /v1/models, Methods: GET
INFO 12-12 22:54:41 launcher.py:27] Route: /version, Methods: GET
INFO 12-12 22:54:41 launcher.py:27] Route: /v1/chat/completions, Methods: POST
INFO 12-12 22:54:41 launcher.py:27] Route: /v1/completions, Methods: POST
INFO 12-12 22:54:41 launcher.py:27] Route: /v1/embeddings, Methods: POST
INFO 12-12 22:54:41 launcher.py:27] Route: /v1/score, Methods: POST
INFO:     Started server process [12905]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

You can submit requests to the server using the `curl` command.

For example, run the command below using another terminal on the same server:

```bash
curl http://0.0.0.0:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer DUMMY" \
  -d '{
    "model": "Qwen/Qwen2.5-0.5B-Instruct",
    "messages": [
      {
        "role": "system",
        "content": "You are a helpful assistant."
      },
      {
        "role": "user",
        "content": "Write a hello world program in C"
      }
    ]
  }'
```

The server processes the request, and the output prints the results:

```output
"id":"chatcmpl-6677cb4263b34d18b436b9cb8c6a5a65","object":"chat.completion","created":1734044182,"model":"Qwen/Qwen2.5-0.5B-Instruct","choices":[{"index":0,"message":{"role":"assistant","content":"Certainly! Here is a simple \"Hello, World!\" program in C:\n\n```c\n#include <stdio.h>\n\nint main() {\n    printf(\"Hello, World!\\n\");\n    return 0;\n}\n```\n\nThis program defines a function called `main` which contains the body of the program. Inside the `main` function, it calls the `printf` function to display the text \"Hello, World!\" to the console. The `return 0` statement indicates that the program was successful and the program has ended.\n\nTo compile and run this program:\n\n1. Save the code above to a file named `hello.c`.\n2. Open a terminal or command prompt.\n3. Navigate to the directory where you saved the file.\n4. Compile the program using the following command:\n   ```\n   gcc hello.c -o hello\n   ```\n5. Run the compiled program using the following command:\n   ```\n   ./hello\n   ```\n   Or simply type `hello` in the terminal.\n\nYou should see the output:\n\n```\nHello, World!\n```","tool_calls":[]},"logprobs":null,"finish_reason":"stop","stop_reason":null}],"usage":{"prompt_tokens":26,"total_tokens":241,"completion_tokens":215,"prompt_tokens_details":null},"prompt_logprobs":null}
```

There are many other experiments you can try. Most Hugging Face models have a **Use this model** button on the top-right of the model card with the instructions for vLLM. You can now use these instructions on your Arm Linux computer.

You can also try out OpenAI-compatible chat clients to connect to the served model.
