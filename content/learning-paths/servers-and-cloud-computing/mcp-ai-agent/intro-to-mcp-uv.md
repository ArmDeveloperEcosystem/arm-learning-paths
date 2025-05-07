---
title: Introduction to Model Context Protocol and uv
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Model Context Protocol (MCP)

The **Model Context Protocol (MCP)** is an open specification for wiring Large-Language-Model (LLM) agents to the *context* they need — whether that context is a database, a local sensor, or a SaaS API.
Think of it as USB-C for AI: once a tool or data source speaks MCP, any compliant LLM client can “plug in” and start using it immediately.

### Why use MCP?
- **Plug-and-play integrations:** A growing catalog of pre-built MCP servers (filesystem, shell, vector stores, web-scraping, etc.) gives your agent instant super-powers with zero custom glue code.

- **Model/vendor agnostic:** Because the protocol lives outside the model, you can swap GPT-4, Claude, or your own fine-tuned model without touching the integration layer.

- **Security by design:** MCP encourages running servers inside your own infrastructure, so sensitive data never leaves the perimeter unless you choose.

- **Cross-ecosystem momentum:** Recent roll-outs—from an official C# SDK to Wix’s production MCP server and Microsoft’s Azure support—show the spec is gathering real-world traction.

### High-level architecture
![mcp server](./mcp.png)
- **MCP Host:** the LLM-powered application (Claude Desktop, an IDE plugin, OpenAI Agents SDK, etc.).
- **MCP Client:** the runtime shim that keeps a 1-to-1 connection with each server.
- **MCP Server:** a lightweight process that advertises tools (functions) over MCP.
- **Local data sources:** files, databases, or sensors your server can read directly.
- **Remote services:** external APIs the server can call on the host’s behalf.

{{% notice Note %}}
Learn more about AI Agents in the [AI Agent on CPU learning path](https://learn.arm.com/learning-paths/servers-and-cloud-computing/ai-agent-on-cpu/).
{{% /notice %}}

## UV: The Fast, All-in-One Python Package Manager

**uv** is a next-generation, Rust-based package manager that unifies pip, virtualenv, Poetry, and more—offering 10×–100× faster installs, built-in virtual environment handling, robust lockfiles, and full compatibility with the Python ecosystem.

### Install uv
- macOS / Linux  
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
- Windows
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Initialize a Project
1. Create & enter your project folder:
```bash
mkdir my-project && cd my-project
```
2. Run
```bash
uv init
```

This scaffolds:
- .venv/ (auto-created virtual environment)
- pyproject.toml (project metadata & dependencies)
- .python-version (pinned interpreter)
- README.md, .gitignore, and a sample main.py

### Install Dependencies
- Add one or more packages to your project:
```bash
uv add requests numpy pandas
```
> Updates both pyproject.toml and the lockfile (uv.lock)

- Remove a package (and its unused sub-deps):
```bash
uv remove numpy
```

- Install from an existing requirements.txt (e.g. when migrating):
```bash:
uv pip install -r requirements.txt
```

All installs happen inside your project’s .venv, and UV’s lockfile guarantees repeatable environments.