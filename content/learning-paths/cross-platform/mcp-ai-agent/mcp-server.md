---
title: Set up an MCP server on Raspberry Pi 5
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up a FastMCP server on Raspberry Pi 5 with uv and ngrok

In this section you will learn how to:

1. Install uv (the Rust-powered Python package manager).  
2. Bootstrap a simple MCP server on your Raspberry Pi 5 that reads the CPU temperature and searches the weather data.
3. Expose the local MCP server to the internet using ngrok (HTTPS tunneling service).

You will run all the commands shown below on your Raspberry Pi 5 running Raspberry Pi OS (64-bit). 

#### 1. Install uv
In your Raspberry Pi Terminal, install `uv`:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

`uv` is a Rust-based, next-generation Python package manager that replaces tools like `pip`, `virtualenv`, and Poetry. It delivers 10×–100× faster installs along with built-in virtual environments, lockfile support, and full Python ecosystem compatibility.

{{% notice Note %}}
After the script finishes, restart your terminal so that the uv command is on your PATH.
{{% /notice %}}

#### 2. Bootstrap the MCP Project
1. Create a project directory and navigate to it:
```bash
mkdir mcp
cd mcp
```
2. Initialize `uv`:
```bash
uv init
```
This command adds:
- .venv/ (auto-created virtual environment).
- pyproject.toml (project metadata and dependencies).
- .python-version (pinned interpreter).
- README.md, .gitignore, and a sample main.py

3. Install the dependencies (learn more about [FastMCP](https://github.com/jlowin/fastmcp)):

```bash
uv pip install fastmcp==2.2.10
uv add requests
```

#### 3. Build your MCP Server 
1. Create a Python file for your MCP server named `server.py`:
```bash
touch server.py
```
2. Open server.py in your preferred text editor and paste in the following code:
```bash
import subprocess, re
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("RaspberryPi MCP Server")

@mcp.tool()
def read_temp():
    """
    Description: Raspberry Pi's CPU core temperature
    Return:      Temperature in °C (float)
    """
    print(f"[debug-server] read_temp()")

    out = subprocess.check_output(["vcgencmd", "measure_temp"]).decode()
    temp_c = float(re.search(r"[-\d.]+", out).group())
    return temp_c

@mcp.tool()
def get_current_weather(city: str) -> str:
    """
    Description: Get Current Weather data in the {city}
    Args:
        city:    Name of the city
    Return:      Current weather data of the city
    """
    print(f"[debug-server] get_current_weather({city})")

    endpoint = "https://wttr.in"
    response = requests.get(f"{endpoint}/{city}")
    return response.text

if __name__ == "__main__":
    mcp.run(transport="sse")
```

#### 4. Run the MCP Server

Run the Python script to deploy the MCP server:

```python
uv run server.py
```
By default, FastMCP listens on port 8000 and exposes your registered tools over HTTP using Server-Sent Events (SSE).

The output should look like:

```output
INFO:     Started server process [2666]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

#### 5. Install and configure ngrok

You will now use ngrok to expose your locally running MCP server to the public internet over HTTPS.

1. Add ngrok’s repo to the apt package manager and install:
```bash
curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
  && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list \
  && sudo apt update \
  && sudo apt install ngrok
```
The ngrok agent authenticates with an authtoken. You will need to authenticate your account with the token which is available on the [ngrok dashboard](https://dashboard.ngrok.com/get-started/your-authtoken).
 
2. Authenticate your account:
```bash
ngrok config add-authtoken <YOUR_NGROK_AUTHTOKEN>
```
Replace `YOUR_NGROK_AUTHTOKEN` with your token from the ngrok dashboard.

3. Expose the port 8000:
```bash
ngrok http 8000
```
4. Copy the generated HTTPS URL (e.g. `https://abcd1234.ngrok-free.app`). You’ll use this endpoint to connect external tools or agents to your MCP server. Keep this URL available for the next steps in your workflow.

### Section summary

You now have a working FastMCP server on your Raspberry Pi 5. It includes tools for reading CPU temperature and retrieving weather data, and it's accessible over the internet via a public HTTPS endpoint using ngrok. This sets the stage for integration with LLM agents or other external tools.

