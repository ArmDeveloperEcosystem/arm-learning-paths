---
title: Serve a model locally with Ollama
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run AI models locally with Ollama

The agent's reasoning steps, such as choosing search terms, selecting URLs, and writing the final summary, are handled by a large language model. Instead of calling a cloud API, this Learning Path serves the model locally with [Ollama](https://ollama.com/).

Ollama is a lightweight runtime that downloads open models, loads them into memory, and exposes a local HTTP API at `http://localhost:11434`. When the agent calls that endpoint, the model runs directly on your machine: the CPU and GPU on your MacBook, Arm Linux laptop, or NVIDIA DGX Spark. Nothing is sent to an external service.

Running locally has three benefits that matter for an agent:

- **Privacy**: your prompts and the web content the agent reads stay on the device.
- **Cost**: there are no per-token API charges, so you can run many queries freely.
- **Control**: you choose the exact model and keep it resident in memory for fast repeated calls.

## Install Ollama

Install Ollama for your operating system.

{{< tabpane code=true >}}
{{< tab header="macOS" language="bash">}}
brew install ollama
{{< /tab >}}
{{< tab header="Linux" language="bash">}}
curl -fsSL https://ollama.com/install.sh | sh
{{< /tab >}}
{{< /tabpane >}}

{{% notice Note %}}
On macOS you can also download the Ollama desktop app from [ollama.com/download](https://ollama.com/download). On an NVIDIA DGX Spark, follow the Linux instructions; Ollama uses the Blackwell GPU for inference automatically.
{{% /notice %}}

## Start the Ollama server

Start the Ollama background service, which hosts the local API the agent connects to:

```bash
ollama serve
```

Leave this running in its own terminal. Open a second terminal for the remaining commands.

{{% notice Tip %}}
On macOS, starting the Ollama desktop app already runs the server in the background, so you can skip `ollama serve`.
{{% /notice %}}

## Pull the Gemma model

This Learning Path uses [Gemma 3](https://ai.google.dev/gemma), Google's family of open models, in its 4-billion-parameter size (`gemma3:4b`). This size is a good default: it's capable enough for the agent's reasoning steps and small enough to run on a laptop.

Download the model:

```bash
ollama pull gemma3:4b
```

Confirm the model is available:

```bash
ollama list
```

You'll see `gemma3:4b` in the list of installed models.

## Choose a different model (optional)

The agent reads the model name from the `OLLAMA_MODEL` environment variable, so you can switch models without editing the code. The default in the script is `gemma3:4b`.

| Model | Size | Best for |
|---|---|---|
| `gemma3:4b` | 4B | Laptops and modest hardware; the default |
| `gemma3:27b` | 27B | High-memory systems such as DGX Spark, for stronger reasoning |

To use a larger model on a DGX Spark, pull it and set the environment variable before running the agent:

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

With Ollama serving `gemma3:4b`, you're ready to look at how the agent code uses it.
