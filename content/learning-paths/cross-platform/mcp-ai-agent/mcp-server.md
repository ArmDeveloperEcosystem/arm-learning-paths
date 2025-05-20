---
title: Set Up an MCP Server on Your Raspberry Pi
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Setup an MCP Server on Raspberry Pi 5

In this section you will learn how to:

1. Install uv (the Rust-powered Python package manager)  
2. Bootstrap a simple MCP server on your Raspberry Pi 5 that reads the CPU temperature and searches the weather data
3. Expose the MCP server to the internet with **ngrok**

You will run all the commands shown below on your Raspberry Pi 5 running Raspberry Pi OS (64-bit)  

#### 1. Install uv
On Raspberry Pi Terminal, install `uv`:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**uv** is a next-generation, Rust-based package manager that unifies pip, virtualenv, Poetry, and more—offering 10×–100× faste
r installs, built-in virtual environment handling, robust lockfiles, and full compatibility with the Python ecosystem.

{{% notice Note %}}
After the script finishes, restart your terminal so that the uv command is on your PATH.
{{% /notice %}}

#### 2. Bootstrap the MCP Project
1. Create a project directory and enter it:
```bash
mkdir mcp
cd mcp
```
2. Initialize with `uv`:
```bash
uv init
```
This command adds:
- .venv/ (auto-created virtual environment)
- pyproject.toml (project metadata & dependencies)
- .python-version (pinned interpreter)
- README.md, .gitignore, and a sample main.py

3. Install the dependencies:
```bash
uv pip install fastmcp==2.2.10
uv add requests
```

#### 3. Build your MCP Server 
1. Create a python file for your MCP server named `server.py`:
```bash
touch server.py
```
2. Use a file editor of your choice and copy the following content into `server.py`:
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

Run the python script to deploy the MCP server:

```python
uv run server.py
```
By default, FastMCP will listen on port 8000 and serve your tools via Server-Sent Events (SSE).

The output should look like:

```output
INFO:     Started server process [2666]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

#### 5. Install & Configure ngrok

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
4. Copy the generated HTTPS URL (e.g. `https://abcd1234.ngrok-free.app`)—you’ll use this as your MCP endpoint.
