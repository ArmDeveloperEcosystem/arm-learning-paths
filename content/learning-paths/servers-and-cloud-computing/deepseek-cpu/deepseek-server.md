---
title: Access the chatbot using the OpenAI-compatible API 
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

You can use the `llama.cpp` server program and submit requests using an OpenAI-compatible API.
This enables applications to be created which access the LLM multiple times without starting and stopping it. You can also access the server over the network to another machine hosting the LLM.

One additional software package is required for this section. Install `jq` on your computer using:

```bash
sudo apt install jq -y
```

The server executable has already compiled during the stage detailed in the previous section, when you ran `make`. 

Start the server from the command line, it listens on port 8080:

```bash
./llama-server -m DeepSeek-R1-Q4_0-00001-of-00010.gguf --port 8080
```

## Use curl

You can access the API using the `curl` command. 

In another terminal, use a text editor to create a file named `curl-test.sh` with the commands below: 

```bash
curl http://localhost:8080/v1/chat/completions -H "Content-Type: application/json"   -d '{
    "model": "any-model",
    "messages": [
      {
        "role": "system",
        "content": "You are a coding  assistant, skilled in programming."
      },
      {
        "role": "user",
        "content": "Write a hello world program in C++."
      }
    ]
  }' 2>/dev/null | jq -C
```

The `model` value in the API is not used, you can enter any value. This is because there is only one model loaded in the server. 

Run the script:

```bash
bash ./curl-test.sh
```

The `curl` command accesses the LLM and you see the output:

```output
{
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "<think>\nOkay, the user wants a \"hello world\" program in C++. Let me think. First, I remember that in C++, the standard way to output text is using cout from the iostream library. So I need to include the iostream header. Wait, should I use #include <iostream> without the .h? Yes, because modern C++ uses the standard headers without the .h extension.\n\nThen, the main function. In C++, the main function has to return an int. So the main function should be int main(), and then inside the curly braces. Some people might use void main(), but that's not standard. Better stick to int main() and return 0 at the end to indicate successful execution.\n\nNext, using namespace std; that way, we don't have to prefix cout and endl with std:: every time. But maybe some people argue against using namespace std in larger programs, but for a simple hello world, it's fine to keep it concise.\n\nThen, the actual output line: cout << \"Hello, World!\" << endl; The endl is for a newline and flushing the buffer. Alternatively, we could just use \\n in the string, like \"Hello, World!\\n\", but using endl is more proper here.\n\nPutting it all together. Let me double-check the syntax. The include statement, then using namespace std, then the main function with the cout line. Make sure the semicolons are in place. The return 0; at the end. Yes, that should do it.\n\nWait, maybe someone might forget the using namespace std line, but then they'd have to write std::cout and std::endl. But including the using directive makes the code shorter for the example. So that's better for a simple example.\n\nAlright, the code should look like this. Let me write it out step by step.\n</think>\n\nHere's a simple \"Hello, World!\" program in C++:\n\n```cpp\n#include <iostream>\n\nusing namespace std;\n\nint main() {\n    cout << \"Hello, World!\" << endl;\n    return 0;\n}\n```\n\n**Explanation:**\n1. `#include <iostream>` - Includes the Standard Input Output Stream library\n2. `using namespace std` - Allows using standard library names without `std::` prefix\n3. `int main()` - The main function where program execution begins\n4. `cout << \"Hello, World!\" << endl;` - Outputs the text to the console\n5. `return 0;` - Indicates successful program termination\n\nThis program will print \"Hello, World!\" to the console when compiled and executed."
      }
    }
  ],
  "created": 1742457902,
  "model": "any-model",
  "system_fingerprint": "b4879-f08f4b31",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 544,
    "prompt_tokens": 22,
    "total_tokens": 566
  },
  "id": "chatcmpl-2lgAaPCfnkBFmuUpdHoTrpZmhbmIrmm0",
  "timings": {
    "prompt_n": 22,
    "prompt_ms": 6162.413,
    "prompt_per_token_ms": 280.1096818181818,
    "prompt_per_second": 3.5700301164495145,
    "predicted_n": 544,
    "predicted_ms": 48960.946,
    "predicted_per_token_ms": 90.00173897058824,
    "predicted_per_second": 11.11089642753226
  }
}
```

In the returned JSON data you see the LLM output, including the content created from the prompt. 

## Use Python

You can also use a Python program to access the OpenAI-compatible API.

Create a Python `venv`:

```bash
python -m venv pytest
source pytest/bin/activate
```

Install the OpenAI Python package:
```bash
pip install openai==1.55.3
```

Use a text editor to create a file named `python-test.py` with the content below: 

```python
from openai import OpenAI

client = OpenAI(
        base_url='http://localhost:8080/v1',
        api_key='no-key'
        )

completion = client.chat.completions.create(
  model="not-used",
  messages=[
    {"role": "system", "content": "You are a coding assistant, skilled in programming.."},
    {"role": "user", "content": "Write a hello world program in C++."}
  ],
  stream=True,
)

for chunk in completion:
  print(chunk.choices[0].delta.content or "", end="")
```

Run the Python file (make sure the server is still running):

```bash
python ./python-test.py
```

You see the output generated by the LLM:

```output
<think>
Okay, the user wants a "hello world" program in C++. Let me think about how to approach this.

First, I remember that in C++, the standard way to output text is using the cout object from the iostream library. So I need to include the iostream header.

Wait, right, the code starts with #include <iostream> to get the input/output stream functionalities. Then, using namespace std; to avoid having to write std:: before cout and endl every time. Though, some people might argue against using namespace std in larger programs, but for a simple hello world, it's fine.

The main function is the entry point. In C++, the main function should return an int. So the main function would be int main() { ... }. Inside the main function, the cout line: cout << "Hello, World!" << endl; to print the message and add a newline.

Don't forget to return 0 at the end of main to indicate successful execution. So putting it all together:

Include the header, use the namespace, define main, output the message, return 0.

Wait, should I mention that using namespace std is optional? Maybe not necessary here, since the user just wants a simple program. The example is clearer with it.

Check for any possible mistakes. Forgetting the semicolons? Each statement ends with a semicolon. The cout line ends with one, the return statement too. Yes.

So the final code should look like:

#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}

That should work. Make sure to explain the parts briefly in case the user is a beginner. But the question just asks to write the program, so maybe the explanation is needed. Wait, the user's question says "write a hello world program in C++", so the answer is the code. But maybe the assistant usually provides a bit of explanation. Let me check.

The example answer includes the code with a brief explanation. So I'll present the code first and then explain each part step by step.
</think>

Here's a simple "Hello, World!" program in C++:

#include <iostream>

using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}

**Step-by-step explanation:**
1. `#include <iostream>` - Includes the input/output stream library for console operations
2. `using namespace std;` - Allows using standard library components (like `cout` and `endl`) without the `std::` prefix
3. `int main()` - The main function where program execution begins
4. `cout << "Hello, World!" << endl;` - Outputs the text to the console and adds a newline
5. `return 0;` - Indicates successful program termination

This program will compile and display "Hello, World!" in the console when executed.
```

You can continue to experiment with different large language models and write scripts to try them.
