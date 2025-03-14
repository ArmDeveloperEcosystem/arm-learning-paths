---
title: AI Agent Application
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Python Script for executing an AI Agent application
With `llama.cpp` built and the Llama3.1 8B model downloaded, you are now ready to create a Python script to execute an AI Agent Application:

Create a Python file named `agent.py` with the content shown below:
```bash
from enum import Enum
from typing import Union
from pydantic import BaseModel, Field
from llama_cpp_agent import MessagesFormatterType
from llama_cpp_agent.chat_history.messages import Roles
from llama_cpp_agent.llm_output_settings import LlmStructuredOutputSettings
from llama_cpp_agent import LlamaCppFunctionTool
from llama_cpp_agent import FunctionCallingAgent
from llama_cpp_agent import MessagesFormatterType
from llama_cpp_agent import LlamaCppAgent
from llama_cpp_agent.providers import LlamaCppPythonProvider
from llama_cpp import Llama
# import os
# from dotenv import load_dotenv
# from langchain_community.tools import TavilySearchResults # Uncomment this to enable search function


# load_dotenv()

# os.environ.get("TAVILY_API_KEY")

llama_model = Llama(
    model_path="./models/dolphin-2.9.4-llama3.1-8b-Q4_0.gguf", # make sure you use the correct path for the quantized model
    n_batch=2048,
    n_ctx=10000,
    n_threads=64,
    n_threads_batch=64,
)

provider = LlamaCppPythonProvider(llama_model)


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

# Uncomment the following function to enable web search functionality (You will need to install langchain-community)
# def search_from_the_web(content: str):
#     """
#     Search useful information from the web to answer User's question

#     Args:
#         content: Useful question to retrieve data from the web to answer user's question
#     """
#     tool = TavilySearchResults(
#         max_results=1,
#         search_depth="basic"
#     )
#     result = tool.invoke({"query":content})
#     return result

settings = provider.get_provider_default_settings()

settings.temperature = 0.65
# settings.top_p = 0.85
# settings.top_k = 60
# settings.tfs_z = 0.95
settings.max_tokens = 4096

output_settings = LlmStructuredOutputSettings.from_functions(
    [get_current_time, open_webpage, calculator], allow_parallel_function_calling=True
)


def send_message_to_user_callback(message: str):
    print(message)


def run_web_search_agent():
    user = input("Please write your prompt here: ")
    if user == "exit":
        return

    llama_cpp_agent = LlamaCppAgent(
        provider,
        debug_output=True,
        system_prompt="You're a helpful assistant to answer User query.",
        predefined_messages_formatter_type=MessagesFormatterType.LLAMA_3,
    )

    result = llama_cpp_agent.get_chat_response(
        user, structured_output_settings=output_settings, llm_sampling_settings=settings
    )

    print("----------------------------------------------------------------")
    print("Response from AI Agent:")
    print(result)
    print("----------------------------------------------------------------")

if __name__ == '__main__':
    run_web_search_agent()
```
In the next section, you will inspect this script to understand how the LLM is configured and used to execute Agent tasks using this script. You will then proceed to executing and testing the AI Agent.

