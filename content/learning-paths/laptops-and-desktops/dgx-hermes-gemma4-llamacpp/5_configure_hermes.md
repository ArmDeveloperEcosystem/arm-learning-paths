---
title: Install and configure Nous Research Hermes Agent
description: Install Nous Research Hermes Agent on NVIDIA DGX Spark, point it at your local llama-server endpoint, and configure API timeouts for multi-step local tool loops.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Hermes Agent

With `llama-server` running in your first terminal, install Nous Research Hermes Agent in your second terminal:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

When the interactive **Hermes Agent Setup Wizard** prompts you to sign in or select a cloud provider, press **Ctrl+C** to exit the wizard. You'll configure the local `llama-server` provider directly with `hermes config set` in the next step.

The output is similar to:

```output
┌─────────────────────────────────────────────────────────┐
│             ☤ Hermes Agent Installer                    │
├─────────────────────────────────────────────────────────┤
│  An open source AI agent by Nous Research.              │
└─────────────────────────────────────────────────────────┘

✓ prerequisites ok (git, curl)
→ Installing the latest stable release (v0.23.4); --channel main follows every commit
✓ dependencies installed
✓ config prepared in /home/user/.hermes
✓ uv ready (uv 0.13.5 (aarch64-unknown-linux-gnu))
...
✓ Hermes Agent install complete. Run: hermes
```

If the installer updates your shell `PATH`, reload `~/.bashrc` (`source ~/.bashrc`) or open a new terminal, then verify the `hermes` Command-Line Interface (CLI) is available:

```bash
hermes --version
```

The output is similar to:

```output
Hermes Agent v0.23.4 (2026.9.24) · stable · local 8fc037444731
Install directory: /home/user/.hermes/hermes-agent
Install method: git
Python: 3.14.9
OpenAI SDK: 2.54.0
Up to date
```

## Point Hermes Agent to local llama-server

Configure Hermes Agent to use a custom OpenAI-compatible provider pointing to your local `llama-server` instance at `http://127.0.0.1:8080/v1`:

```bash
hermes config set model.provider local
hermes config set model.base_url http://127.0.0.1:8080/v1
hermes config set model.default ./models/gemma-4-E4B-it-Q4_0.gguf
```

Verify your active configuration:

```bash
hermes config show
```

The output is similar to:

```output
┌─────────────────────────────────────────────────────────┐
│              ☤ Hermes Configuration                    │
└─────────────────────────────────────────────────────────┘
...
◆ Model
  Model:        {'default': './models/gemma-4-E4B-it-Q4_0.gguf', 'provider': 'local', 'base_url': 'http://127.0.0.1:8080/v1'}
  Max turns:    500
```

## Increase the API timeout for local inference

Autonomous tool-calling loops can send large prompts containing thousands of tokens of file contents and tool outputs to `llama-server`. Setting `HERMES_API_TIMEOUT=1800` (30 minutes) in `~/.hermes/.env` ensures long multi-turn requests don't time out prematurely, even if you later switch to larger models such as Gemma 4 31B or run CPU-only fallback.

Update `~/.hermes/.env`:

```bash
mkdir -p ~/.hermes
grep -q '^HERMES_API_TIMEOUT=' ~/.hermes/.env 2>/dev/null \
  && sed -i 's/^HERMES_API_TIMEOUT=.*/HERMES_API_TIMEOUT=1800/' ~/.hermes/.env \
  || echo 'HERMES_API_TIMEOUT=1800' >> ~/.hermes/.env
```

Confirm the setting in `~/.hermes/.env`:

```bash
grep '^HERMES_API_TIMEOUT=' ~/.hermes/.env
```

The output is similar to:

```output
HERMES_API_TIMEOUT=1800
```

## Start an interactive session

After configuring `model.provider`, `model.base_url`, and `model.default`, you can launch Hermes Agent interactively with no arguments in any workspace directory:

```bash
hermes
```

Hermes opens its interactive terminal user interface (UI) connected directly to your local `llama-server` at `http://127.0.0.1:8080/v1`. For a classic line-based interface, use `hermes chat --cli` instead. Type `/exit` or press **Ctrl+C** when you're finished.

## What you've accomplished and what's next

You've installed Nous Research Hermes Agent on NVIDIA DGX Spark, connected it to your local `llama-server` endpoint, and configured `HERMES_API_TIMEOUT` for multi-step local inference.

Next, you'll test autonomous multi-step tool calling on a local code-fixing task with Gemma 4 E4B.
