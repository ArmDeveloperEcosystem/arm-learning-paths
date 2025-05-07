---
title: Set Up an MCP Server on Your Raspberry Pi
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Expose Raspberry Pi MCP Server via ngrok

This guide shows you how to:

1. Install **uv** (the Rust-powered Python manager)  
2. Bootstrap a simple **MCP** server on your Raspberry Pi that reads the CPU temperature  
3. Expose it to the internet with **ngrok**

### Prerequisites

- A **Raspberry Pi 5** (or other ARMv8 Pi) running Raspberry Pi OS (64-bit)  
- Basic familiarity with Python and the terminal  


#### 1. Install `uv`
On Raspberry Pi Terminal:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

{{% notice Note %}}
After the script finishes, restart your terminal so that the uv command is on your PATH.
{{% /notice %}}

#### 2. Bootstrap the MCP Project
1. Create a project directory and enter it:
```bash
mkdir mcp
cd mcp
```
2. Initialize with uv (this creates pyproject.toml, .venv/, etc.):
```bash
uv init
```
3. Install the FastMCP library:
```uv
uv pip install fastmcp
```

#### 3. Write Your MCP Server (server.py)
1. Create the server file:
```bash
touch server.py
```
2. Edit `server.py` with the following contents:
```bash
import subprocess, re
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Echo Server")

@mcp.tool()
def read_temp():
    """
    Description: Raspberry Pi's CPU core temperature
    Return:      Temperature in °C (float)
    """
    out = subprocess.check_output(["vcgencmd", "measure_temp"]).decode()
    temp_c = float(re.search(r"[-\d.]+", out).group())
    return temp_c

if __name__ == "__main__":
    mcp.run(transport="sse")
```

#### 4. Run the MCP Server
```python
uv run server.py
```
By default, FastMCP will listen on port **8000** and serve your `read_temp` tool via **Server-Sent Events (SSE)**.

#### 5. Install & Configure ngrok
1. Add ngrok’s APT repo and install:
```bash
curl -sSL https://ngrok-agent.s3.amazonaws.com/ngrok.asc \
  | sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null \
  && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" \
  | sudo tee /etc/apt/sources.list.d/ngrok.list \
  && sudo apt update \
  && sudo apt install ngrok
```
2. Authenticate your account:
```bash
ngrok config add-authtoken <YOUR_NGROK_AUTHTOKEN>
```
3. Expose port 8000:
```bash
ngrok http 8000
```
4. Copy the generated HTTPS URL (e.g. `https://abcd1234.ngrok-free.app`)—you’ll use this as your MCP endpoint.