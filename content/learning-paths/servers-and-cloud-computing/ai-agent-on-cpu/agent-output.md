---
title: Explore and Test Your AI Agent
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## AI Agent Function Calls

An AI agent, powered by an LLM, selects the most appropriate function by analyzing the input, identifying the relevant intent, and matching it to predefined functions based on its understanding of the language and context.

You will now walk through how this is implemented in the excerpt from a Python script called `agent.py`.

#### Initialize the Quantized Model 

This code section of `agent.py` shown below creates an instance of the quantized `llama3.1 8B` model for more efficient inference on Arm-based systems:
```output
llama_model = Llama(
    model_path="./models/dolphin-2.9.4-llama3.1-8b-Q4_0.gguf",
    n_batch=2048,
    n_ctx=10000,
    n_threads=64,
    n_threads_batch=64,
)
```
#### Define a Provider

Now define a provider that leverages the `llama.cpp` Python bindings:
```output
provider = LlamaCppPythonProvider(llama_model)
```
#### Define Functions

The LLM has access to certain tools or functions and can take a general user input and decide which functions to call. The function’s docstring guides the LLM on when and how to invoke it. 

In `agent.py` three such tools or functions are defined; `open_webpage`, `get_current_time`, and `calculator`: 

```output
def open_webpage():
    """
    Open Learning Path Website when user asks the agent regarding Arm Learning Path
    """
    import webbrowser

    url = "https://learn.arm.com/"
    webbrowser.open(url, new=0, autoraise=True)


def get_current_time():
    """
    Returns the current time in H:MM AM/PM format.
    """
    import datetime  # Import datetime module to get current time

    now = datetime.datetime.now()  # Get current time
    return now.strftime("%I:%M %p")  # Format time in H:MM AM/PM format


class MathOperation(Enum):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"
def calculator(
    number_one: Union[int, float],
    number_two: Union[int, float],
    operation: MathOperation,
) -> Union[int, float]:
    """
    Perform a math operation on two numbers.

    Args:
        number_one: First number
        number_two: Second number
        operation: Math operation to perform

    Returns:
        Result of the mathematical operation

    Raises:
        ValueError: If the operation is not recognized
    """
    if operation == MathOperation.ADD:
        return number_one + number_two
    elif operation == MathOperation.SUBTRACT:
        return number_one - number_two
    elif operation == MathOperation.MULTIPLY:
        return number_one * number_two
    elif operation == MathOperation.DIVIDE:
        return number_one / number_two
    else:
        raise ValueError("Unknown operation.")
```
#### Create Output Settings to Enable Function Calls

`from_functions` creates an instance of `LlmStructuredOutputSettings` by passing in a list of callable Python functions. The LLM can then decide if and when to use these functions based on user queries:

```output
output_settings = LlmStructuredOutputSettings.from_functions(
    [get_current_time, open_webpage, calculator], allow_parallel_function_calling=True
)

```
#### Collect and Process User Input 

The user's prompt is then collected and processed through `LlamaCppAgent`. The agent decides whether to call any defined functions based on the request:
```
user = input("Please write your prompt here: ")

llama_cpp_agent = LlamaCppAgent(
    provider,
    debug_output=True,
    system_prompt="You're a helpful assistant to answer User query.",
    predefined_messages_formatter_type=MessagesFormatterType.LLAMA_3,
)

result = llama_cpp_agent.get_chat_response(
    user, structured_output_settings=output_settings, llm_sampling_settings=settings
)
```

## Test and Run the AI Agent

You're now ready to test and run the AI agent Python script. Start the application:

```bash
python3 agent.py
```

You will see lots of interesting statistics being printed from `llama.cpp` about the model and the system, followed by the prompt for input, as shown:

```output
llama_kv_cache_init:        CPU KV buffer size =  1252.00 MiB
llama_init_from_model: KV self size  = 1252.00 MiB, K (f16):  626.00 MiB, V (f16):  626.00 MiB
llama_init_from_model:        CPU  output buffer size =     0.49 MiB
llama_init_from_model:        CPU compute buffer size =   677.57 MiB
llama_init_from_model: graph nodes  = 1030
llama_init_from_model: graph splits = 1
CPU : NEON = 1 | ARM_FMA = 1 | FP16_VA = 1 | MATMUL_INT8 = 1 | SVE = 1 | DOTPROD = 1 | MATMUL_INT8 = 1 | SVE_CNT = 32 | OPENMP = 1 | AARCH64_REPACK = 1 |
Model metadata: {'tokenizer.chat_template': "{% if not add_generation_prompt is defined %}{% set add_generation_prompt = false %}{% endif %}{% for message in messages %}{{'<|im_start|>' + message['role'] + '\n' + message['content'] + '<|im_end|>' + '\n'}}{% endfor %}{% if add_generation_prompt %}{{ '<|im_start|>assistant\n' }}{% endif %}", 'tokenizer.ggml.eos_token_id': '128256', 'general.quantization_version': '2', 'tokenizer.ggml.model': 'gpt2', 'llama.vocab_size': '128258', 'general.file_type': '2', 'llama.attention.layer_norm_rms_epsilon': '0.000010', 'llama.rope.freq_base': '500000.000000', 'tokenizer.ggml.bos_token_id': '128000', 'llama.attention.head_count': '32', 'llama.feed_forward_length': '14336', 'general.architecture': 'llama', 'llama.attention.head_count_kv': '8', 'llama.block_count': '32', 'tokenizer.ggml.padding_token_id': '128004', 'general.basename': 'Meta-Llama-3.1', 'llama.embedding_length': '4096', 'general.base_model.0.organization': 'Meta Llama', 'tokenizer.ggml.pre': 'llama-bpe', 'llama.context_length': '131072', 'general.name': 'Meta Llama 3.1 8B', 'llama.rope.dimension_count': '128', 'general.base_model.0.name': 'Meta Llama 3.1 8B', 'general.organization': 'Meta Llama', 'general.type': 'model', 'general.size_label': '8B', 'general.base_model.0.repo_url': 'https://huggingface.co/meta-llama/Meta-Llama-3.1-8B', 'general.license': 'llama3.1', 'general.base_model.count': '1'}
Available chat formats from metadata: chat_template.default
Using gguf chat template: {% if not add_generation_prompt is defined %}{% set add_generation_prompt = false %}{% endif %}{% for message in messages %}{{'<|im_start|>' + message['role'] + '
' + message['content'] + '<|im_end|>' + '
'}}{% endfor %}{% if add_generation_prompt %}{{ '<|im_start|>assistant
' }}{% endif %}
Using chat eos_token: <|im_end|>
Using chat bos_token: <|begin_of_text|>
Please write your prompt here:
```

## Test the AI agent

When you are presented with `Please write your prompt here:` test it with an input prompt. 

Enter:

```console
What is the current time?
```

As part of the prompt, a list of executable functions is sent to the LLM, allowing the agent to select the appropriate function:

```output
Read and follow the instructions below:

<system_instructions>
You're a helpful assistant to answer User query.
</system_instructions>


You can call functions to help you with your tasks and user queries. The available functions are:

<function_list>
Function: get_current_time
  Description: Returns the current time in H:MM AM/PM format.
  Parameters:
    none

Function: open_webpage
  Description: Open Learning Path Website when user asks the agent regarding Arm Learning Path
  Parameters:
    none

Function: calculator
  Description: Perform a math operation on two numbers.
  Parameters:
    number_one (int or float): First number
    number_two (int or float): Second number
    operation (enum): Math operation to perform Can be one of the following values: 'add' or 'subtract' or 'multiply' or 'divide'
</function_list>

To call a function, respond with a JSON object (to call one function) or a list of JSON objects (to call multiple functions), with each object containing these fields:

- "function": Put the name of the function to call here.
- "arguments": Put the arguments to pass to the function here.
```

The AI agent then decides to invoke the appropriate function and returns the result as shown:

```output
[
  {
    "function":
      "get_current_time",
    "arguments": {}
  }
]
----------------------------------------------------------------
Response from AI Agent:
[{'function': 'get_current_time', 'arguments': {}, 'return_value': '07:58 PM'}]
----------------------------------------------------------------
```

You have now tested the `What is the current time?` question. The AI agent evaluates the query and calls the `get_current_time()` function, and returns a result in **H:MM AM/PM** format.

You have successfully run and tested your AI agent. Experiment with different prompts or define custom functions to expand your AI agent's capabilities. 



