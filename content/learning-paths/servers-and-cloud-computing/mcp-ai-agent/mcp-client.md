---
title: Build & Run an AI Agent on Your Workstation
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Create an AI Agent and point it at your Pi's MCP Server
1. Bootstrap the Agent Project
```bash
# create & enter folder
mkdir mcp-agent && cd mcp-agent
```
2. scaffold with **uv**
```bash
uv init
```
3. install **OpenAI Agents SDK** + **dotenv**
```bash
uv add openai-agents python-dotenv
```
4. Create a `.env` file with your OpenAI key:
```bash
echo -n "OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>" > .env
```

### Write the Agent Client (main.py)
```python
import asyncio, os
from dotenv import load_dotenv

# disable Agents SDK tracing for cleaner output
os.environ["OPENAI_AGENTS_DISABLE_TRACING"] = "1"
load_dotenv()

from agents import Agent, Runner, set_default_openai_key
from agents.mcp import MCPServerSse
from agents.model_settings import ModelSettings

async def run(mcp_server):
    set_default_openai_key(os.getenv("OPENAI_API_KEY"))

    agent = Agent(
        model="gpt-4.1-2025-04-14",
        name="Assistant",
        instructions="Use the tools to answer the user's query",
        mcp_servers=[mcp_server],
        model_settings=ModelSettings(tool_choice="required"),
    )

    question = "What is the CPU temperature?"
    print("Running:", question)
    result = await Runner.run(starting_agent=agent, input=question)
    print("Response:", result.final_output)

async def main():
    # replace URL with your ngrok-generated endpoint
    url = "<YOUR_NGROK_URL>/sse"

    async with MCPServerSse(
        name="RPI5 MCP Server",
        params={"url": url},
        client_session_timeout_seconds=30,
    ) as server:
        await run(server)

if __name__ == "__main__":
    asyncio.run(main())
```

### Execute the Agent
```bash
uv run main.py
```
You should see output like:
```output
Running: What is the CPU temperature?
Response: The current CPU temperature is 48.8°C.
```

Congratulations! Your local AI Agent just called the MCP server on your Raspberry Pi and fetched the CPU temperature.

This lightweight protocol isn’t just a game-changer for LLM developers—it also empowers IoT engineers to transform real-world data streams and give AI direct, reliable control over any connected device.

### Next Steps
- **Expand Your Toolset**  
   - Write additional `@mcp.tool()` functions for Pi peripherals (GPIO pins, camera, I²C sensors, etc.)  
   - Combine multiple MCP servers (e.g. filesystem, web-scraper, vector-store memory) for richer context  

- **Integrate with IoT Platforms**  
   - Hook into Home Assistant or Node-RED via MCP  
   - Trigger real-world actions (turn on LEDs, read environmental sensors, control relays)  
