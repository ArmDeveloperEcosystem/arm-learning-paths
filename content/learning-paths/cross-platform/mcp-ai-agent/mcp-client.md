---
title: Build and run an AI Agent on your development machine
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section you'll learn how to set up an AI Agent on your development machine. You will then connect your MCP server running on the Raspberry Pi 5 to it.

These commands were tested on a Linux Arm development machine. 

### Create an AI Agent and point it at your Pi's MCP Server
1. Install `uv` on your development machine:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
2. Create a directory for the Agent:
```bash
mkdir mcp-agent && cd mcp-agent
```
3. Setup the directory to use `uv`:
```bash
uv init
```

This command adds:
- .venv/ (auto-created virtual environment)
- pyproject.toml (project metadata & dependencies)
- .python-version (pinned interpreter)
- README.md, .gitignore, and a sample main.py

4. Install **OpenAI Agents SDK** + **dotenv**
```bash
uv add openai-agents python-dotenv
```
5. Create a `.env` file to securely store your OpenAI API key:

```bash
echo -n "OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>" > .env
```

### Write the Python script for the Agent Client

Use a file editor of your choice and replace the content of the sample `main.py` with the content shown below:

```python
import asyncio, os
from dotenv import load_dotenv

# disable Agents SDK tracing for cleaner output
os.environ["OPENAI_AGENTS_DISABLE_TRACING"] = "1"
load_dotenv()

from agents import Agent, Runner, set_default_openai_key
from agents.mcp import MCPServerSse
from agents.model_settings import ModelSettings

async def run(mcp_server: list[MCPServerSse]):
    set_default_openai_key(os.getenv("OPENAI_API_KEY"))

    agent = Agent(
        model="gpt-4.1-2025-04-14",
        name="Assistant",
        instructions="Use the tools to answer the user's query",
        mcp_servers=mcp_server,
        model_settings=ModelSettings(tool_choice="required"),
    )

    for message in ["What is the CPU temperature?", "How is the weather in Cambridge?"]:
        print(f"Running: {message}")
        result = await Runner.run(starting_agent=agent, input=message)
        print(f"Response: {result.final_output}")

async def main():
    # replace URL with your ngrok-generated endpoint
    url = "<YOUR_NGROK_URL>/sse"

    async with MCPServerSse(
        name="RPI5 MCP Server",
        params={"url": url},
        client_session_timeout_seconds=60,
    ) as server1:
        await run([server1])

if __name__ == "__main__":
    asyncio.run(main())
```

### Execute the Agent

You’re now ready to run the AI Agent and test its connection to your running MCP server on the Raspberry Pi 5.

Run the `main.py` python script:
```bash
uv run main.py
```md
The output should look something like this:
```output
Running: What is the CPU temperature?
Response: The current CPU temperature is 48.8°C.
Running: How is the weather in Cambridge?
The weather in Cambridge is currently partly cloudy with a temperature of around 10°C. The wind is blowing at approximately 17 km/h. Visibility is good at 10 km, and there is no precipitation expected at the moment. The weather should be pleasant throughout the day with temperatures rising to about 15°C by midday.
```

Congratulations! Your local AI Agent just called the MCP server on your Raspberry Pi and fetched the CPU temperature and the weather information.

This lightweight protocol isn’t just a game-changer for LLM developers—it also empowers IoT engineers to transform real-world data streams and give AI direct, reliable control over any connected device.

### Next Steps
- **Expand Your Toolset**  
   - Write additional `@mcp.tool()` functions for Pi peripherals (GPIO pins, camera, I²C sensors, etc.)  
   - Combine multiple MCP servers (e.g. filesystem, web-scraper, vector-store memory) for richer context  

- **Integrate with IoT Platforms**  
   - Hook into Home Assistant or Node-RED via MCP  
   - Trigger real-world actions (turn on LEDs, read environmental sensors, control relays)  
