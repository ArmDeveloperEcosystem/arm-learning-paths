---
title: Serve a model locally with Ollama
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run AI models locally with Ollama

The agent's reasoning steps, such as choosing search terms, selecting URLs, and writing the final summary, are handled by an LLM. Instead of calling a cloud API, you'll serve the model locally with [Ollama](https://ollama.com/).

Ollama is a lightweight runtime that downloads open models, loads them into memory, and exposes a local HTTP API at `http://localhost:11434`. When the agent calls that endpoint, the model runs directly on your machine: the CPU and GPU on your MacBook, Arm Linux laptop, or NVIDIA DGX Spark. Nothing is sent to an external service or cloud.

Running locally has three benefits that matter for an agent:

- Privacy: your prompts and the web content the agent reads stay on the device.
- Cost: there are no per-token API charges, so you can run many queries freely.
- Control: you choose the exact model and keep it resident in memory for fast repeated calls.

## Install and start Ollama

Install [Ollama](https://ollama.com/) and start its server using one of the following options. The server exposes a local API at `http://localhost:11434` that the agent connects to.

{{< tabpane code=true >}}
{{< tab header="Homebrew (Recommended)" language="bash">}}
# Install Ollama
brew install ollama

# Start the server as a background service (no terminal to keep open)
brew services start ollama
{{< /tab >}}
{{< tab header="Install script" language="bash">}}
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Start the server (leave this running, and open a second terminal)
ollama serve
{{< /tab >}}
{{< /tabpane >}}

With [Homebrew](https://brew.sh/), `brew services` runs Ollama in the background, so you can use the same terminal throughout. With the install script, `ollama serve` runs in the foreground, so keep that terminal open and use a second terminal for the remaining commands.

## Pull the Gemma model

You'll use [Gemma 3](https://ai.google.dev/gemma), Google's family of open models. The 4-billion-parameter size (`gemma3:4b`) is a good default: it's capable enough for the agent's reasoning steps and small enough to run on a laptop.

Download the model:

```bash
ollama pull gemma3:4b
```

Confirm the model is available:

```bash
ollama list
```

You'll see `gemma3:4b` in the list of installed models.

## (Optional) Choose a different model

The agent reads the model name from the `OLLAMA_MODEL` environment variable, so you can switch models without editing the code. The default in the script is `gemma3:4b`.

| Model | Size | Best for |
|---|---|---|
| `gemma3:4b` | 4B | Laptops and modest hardware; the default |
| `gemma3:27b` | 27B | High-memory systems such as DGX Spark, for stronger reasoning |

To use a larger model on a DGX Spark, pull it and set the environment variable before running the agent. 

For example, to use a model with 27 billion parameters:

```bash
ollama pull gemma3:27b
export OLLAMA_MODEL="gemma3:27b"
```

{{% notice Note %}}
Larger models produce stronger summaries but use more memory and generate tokens more slowly. Start with `gemma3:4b` to confirm everything works, then experiment with larger models if your hardware allows.
{{% /notice %}}

## Test the model

Before wiring it into the agent, confirm the model responds:

```bash
ollama run gemma3:4b
```

Enter a short prompt:

```text
Summarize what a local AI agent does in one sentence.
```

Type `/bye` to exit the model session.

## What you've accomplished and what's next

You've now set up Ollama and served a Google `gemma3:4b` model locally. 

Next, you'll look at how the agent code uses the model.
