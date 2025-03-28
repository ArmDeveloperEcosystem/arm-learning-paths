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
./llama-server -m DeepSeek-R1-Q4_0/DeepSeek-R1-Q4_0/DeepSeek-R1-Q4_0-00001-of-00010.gguf --port 8080
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
        "content": "<think>\nOkay, the user wants a \"Hello World\" program in C++. Let me think about how to approach this.\n\nFirst, I remember that in C++, the standard way to output text is using cout from the iostream library. So I'll need to include the iostream header. Wait, should I use #include <iostream> or <iostream.h>? Oh right, modern C++ uses <iostream> without the .h extension, and the .h ones are deprecated.\n\nNext, the main function. The entry point for a C++ program is int main(). Some older code might use void main(), but that's not standard. The correct return type is int. So I'll write int main().\n\nInside the main function, to output \"Hello World\", I'll use std::cout. But wait, using namespace std; can make it shorter. Should I include that line or qualify cout with std:: each time? If the user is a beginner, maybe using the namespace is simpler. So adding using namespace std; after the include would let them write cout directly instead of std::cout.\n\nThen the actual output line: cout << \"Hello World!\" << endl;. The endl is for a newline and flushing the buffer. Alternatively, they could use \\n in the string. But using endl is common in examples.\n\nFinally, return 0; to indicate successful execution. Yeah, that's necessary because main is declared as returning an int.\n\nWait, putting it all together: include iostream, use namespace std, main function with cout statement and return 0. That should work. Let me check for any syntax errors. Semicolon after the cout line, correct. Curly braces around main's body. Everything looks good.\n\nI should also explain the code in the answer. Break down each part so the user understands. Maybe mention the include directive, the using namespace, the main function, and the cout line. Explain that return 0 is the exit status.\n\nHmm, is there a simpler way without the namespace? Like using std::cout and std::endl instead. But including the using directive is more concise for a hello world example. It's standard practice in introductory examples to make the code less cluttered.\n\nI think that's all. The code should compile and run, printing Hello World! when executed.\n</think>\n\nHere's a simple \"Hello, World!\" program in C++:\n\n```cpp\n#include <iostream>\n\nusing namespace std;\n\nint main() {\n    cout << \"Hello, World!\" << endl;\n    return 0;\n}\n```\n\nLet's break down the components:\n1. `#include <iostream>` - Includes the standard input/output library\n2. `using namespace std` - Allows us to use standard library components without `std::` prefix\n3. `int main()` - The main function where program execution begins\n4. `cout << \"Hello, World!\" << endl` - Outputs the text to the console\n5. `return 0` - Indicates successful program termination\n\nTo run this program:\n1. Save it as `hello.cpp`\n2. Compile with `g++ hello.cpp -o hello`\n3. Run with `./hello` (Linux/Mac) or `hello.exe` (Windows)"
      }
    }
  ],
  "created": 1743105016,
  "model": "any-model",
  "system_fingerprint": "b4963-02082f15",
  "object": "chat.completion",
  "usage": {
    "completion_tokens": 672,
    "prompt_tokens": 22,
    "total_tokens": 694
  },
  "id": "chatcmpl-ZgBRsBdAdbS0XYsWdaUKydGBTCwqoCpy",
  "timings": {
    "prompt_n": 22,
    "prompt_ms": 473.018,
    "prompt_per_token_ms": 21.50081818181818,
    "prompt_per_second": 46.50985797580642,
    "predicted_n": 672,
    "predicted_ms": 59210.499,
    "predicted_per_token_ms": 88.11086160714287,
    "predicted_per_second": 11.349338569161526
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
Okay, the user wants a "Hello World" program in C++. Let me start by recalling the basic structure of a C++ program.

First, I know that in C++, you need to include the iostream header for input and output operations. So the first line should be #include <iostream>. That gives access to cout and other stream functions.

Then, the main function. The entry point of a C++ program is int main(). The function should return an integer, usually 0 to indicate success. So the main function structure would be int main() { ... }.

Inside the main function, to output "Hello World", I can use std::cout. The syntax would be std::cout << "Hello World!" << std::endl;. The << operator is used to chain the output. Using std::endl adds a newline and flushes the buffer, but just \n could also be used. But for a simple program, either works.

Alternatively, using the using namespace std; directive can simplify the code so that I don't have to prefix cout and endl with std::. But including that line is a matter of style. Some prefer not to use it to avoid namespace pollution, but in a simple program like this, it's probably okay. But maybe the example should be explicit to show the namespace, so using std::cout and std::endl without the using directive.

Putting it all together:

#include <iostream>

int main() {
    std::cout << "Hello World!" << std::endl;
    return 0;
}

Wait, is the return 0 necessary? In C++, if the main function doesn't have a return statement, it automatically returns 0 by default. So technically, I could omit it. But including it makes it explicit, which is better for clarity, especially for beginners who might not know that default.

So yes, including return 0 is good practice here.

Another thing to check: the << operator. Yes, that's correct. The message is in quotes, followed by std::endl. Alternatively, we could write "\n" instead of std::endl for a newline without flushing, but again, for a simple program, either is fine. Using endl is more standard in examples.

So the final code would look like that. Let me double-check for syntax. The #include should have angle brackets around iostream. The main function is correctly declared, and the cout statement is correctly formatted. The semicolons are in the right places.

Yes, this should compile and run, outputting "Hello World!" followed by a newline.
</think>

Here's a simple "Hello World" program in C++:

```cpp
#include <iostream>

int main() {
    std::cout << "Hello World!" << std::endl;
    return 0;
}


**Explanation:**
1. `#include <iostream>`: Includes the standard input/output stream library needed for output operations.
2. `int main()`: The main function where program execution begins.
3. `std::cout << "Hello World!" << std::endl;`: Outputs the text "Hello World!" followed by a newline.
4. `return 0;`: Indicates successful program termination to the operating system.

When compiled and run, this program will display:

Hello World!
```
You can continue to experiment with different large language models and write scripts to try them.
