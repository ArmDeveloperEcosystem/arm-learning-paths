---
title: Deploy a compatible containerized workload with Topo
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose a starter template and clone it

In this Learning Path, you'll use the LLM chatbot template to explore the workflow. The same steps apply to all Topo templates.

To clone the template onto your host device, run:

```bash
topo clone https://github.com/Arm-Examples/topo-cpu-ai-chat.git
```

If a template asks for build arguments, Topo prompts you interactively.

For this template, accept the defaults for each prompt by pressing Enter. The default configuration uses the `bartowski/Qwen_Qwen3.5-0.8B-GGUF` model and builds with Neon optimizations. SVE — Arm's Scalable Vector Extension, which provides wider vector operations than Neon's fixed 128-bit width — is disabled by default. If `topo describe` shows your target supports SVE, you can enable it by setting `ENABLE_SVE` to `ON`, or edit `compose.yaml` to change it later.

The output is similar to:
```output
┌─ Copy files ──────────────────────────────────────────
Cloning into 'topo-cpu-ai-chat'...
remote: Enumerating objects: 21, done.
remote: Counting objects: 100% (21/21), done.
remote: Compressing objects: 100% (17/17), done.
remote: Total 21 (delta 0), reused 11 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (21/21), 17.43 KiB | 8.72 MiB/s, done.

┌─ Input args ──────────────────────────────────────────
Provide: Hugging Face model repo ID containing a supported single-file GGUF model
Example: unsloth/SmolLM2-135M-Instruct-GGUF
Default: bartowski/Qwen_Qwen3.5-0.8B-GGUF
HF_MODEL> 

Provide: Exact supported GGUF filename to download; sharded and mmproj files are rejected
Example: Qwen_Qwen3.5-0.8B-Q4_0.gguf
HF_MODEL_FILE> 

Provide: Enables building with SVE instructions (OFF/ON)
Example: ON
Default: OFF
ENABLE_SVE> 

┌─ Project ready ───────────────────────────────────────
Created in 'topo-cpu-ai-chat'

Now run:
  cd topo-cpu-ai-chat
  topo deploy
```

This creates a project directory using the template. The directory will contain template source files and `compose.yaml`.

The following is an example `compose.yaml` file for the LLM chatbot application:

```yaml
services:
  llama-server:
    platform: linux/arm64
    build:
      context: ./llama-inference
      args:
        ENABLE_SVE: OFF
        HF_MODEL: bartowski/Qwen_Qwen3.5-0.8B-GGUF
        HF_MODEL_FILE: ""
    ports:
      - "8080:8080"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 10s
      timeout: 5s
      retries: 3
      start_period: 60s
  chat-ui:
    platform: linux/arm64
    build:
      context: ./simple-chat
      args:
        ENABLE_SVE: OFF
    depends_on:
      llama-server:
        condition: service_healthy
    ports:
      - "3000:3000"
x-topo:
  name: "Topo CPU AI Chat"
  description: "Complete LLM chat application optimized for Arm CPU inference.\n\nThis project demonstrates running large language models on CPU\nusing llama.cpp compiled with Arm baseline optimizations and \naccelerated using NEON SIMD and SVE (when supported and enabled).\n\nThe stack includes:\n- llama.cpp server with Arm NEON optimizations (SVE optional)\n- Quantized Qwen3.5-0.8B model bundled in the image\n- Simple web-based chat interface\n- No GPU required - pure CPU inference\n\nPerfect for demos and testing! The bundled Qwen3.5-0.8B model allows the\nproject to run immediately without downloading additional models.\n\nIdeal for testing LLM workloads on Arm hardware without GPU dependencies,\nshowcasing how far you can push NEON acceleration. Rebuild with SVE enabled\nwhen wider vectors are available.\n"
  features:
    - "SVE"
    - "NEON"
  args:
    HF_MODEL:
      description: "Hugging Face model repo ID containing a supported single-file GGUF model"
      default: "bartowski/Qwen_Qwen3.5-0.8B-GGUF"
      example: "unsloth/SmolLM2-135M-Instruct-GGUF"
    HF_MODEL_FILE:
      description: "Exact supported GGUF filename to download; sharded and mmproj files are rejected"
      default: ""
      example: "Qwen_Qwen3.5-0.8B-Q4_0.gguf"
    ENABLE_SVE:
      description: "Enables building with SVE instructions (OFF/ON)"
      default: "OFF"
      example: "ON"
```

You can edit `compose.yaml` at any time to adjust build arguments such as enabling or disabling SVE, or switching to a different LLM model.

## Deploy the app on the target

On your host device, enter the project directory created by the `topo clone` command. In the case of the LLM chatbot, this directory is `topo-cpu-ai-chat`:

```bash
cd topo-cpu-ai-chat/
```

Then, use `topo deploy` to build the container images on the host, transfer them to the target over SSH, and start the application on the target:

```bash
topo deploy --target user@my-target
```

The output is similar to:

```output
┌─ Start services ──────────────────────────────────────
[+] up 3/3
 ✔ Network topo-cpu-ai-chat_default          Created                                                                                               0.0ss
 ✔ Container topo-cpu-ai-chat-llama-server-1 Healthy                                                                                               10.6s
 ✔ Container topo-cpu-ai-chat-chat-ui-1      Started                                                                                               5.9ss
```

After deployment is complete, access the web application by opening a browser and navigating to `http://<ip_address_of_target>:<port_number>`, where `<port_number>` matches the port exposed by your template. For the LLM chatbot, this is `3000`. You can find the port in the `compose.yaml` file for your template.

{{< notice Important >}}
If your target is a Linux virtual machine (for example, on a cloud provider), ensure that the chosen port (such as 3000) is open as an inbound rule in your virtual machine's firewall or security group. Otherwise, you won't be able to access the application from your browser.
{{< /notice >}}

The LLM chatbot application appears as follows:


![Screenshot of the LLM Chatbot web interface running on an Arm-based target, showing a chat window and model response. This confirms successful deployment and provides a visual reference for the expected result.#center](llm_chatbot.png "LLM Chatbot web interface on Arm target")

If the target is not directly accessible from your browser (for example, if it is behind a NAT or you prefer not to open inbound firewall ports), use SSH port forwarding to tunnel the connection to your local machine:

```bash
ssh -L <port_number>:localhost:<port_number> user@my-target
```

Then, open `http://localhost:<port_number>` in your browser.

To stop a deployed Topo application on the target, run `topo stop` on the host:

```bash
topo stop --target user@my-target
```

## (Optional) Deploy with a CLI agent

Topo is well-suited for use with CLI agents. It ships as a single executable alongside a `README.md` that describes all commands and flags. You can also pass `--output json` to any Topo command for machine-readable output that agents can parse reliably.

Before starting, confirm that your host and target are set up with the required dependencies as described in the previous sections.

If you don't already have a CLI agent installed, see one of these install guides:

- [Install Claude Code](/install-guides/claude-code/)
- [Install Codex CLI](/install-guides/codex-cli/)
- [Install Gemini CLI](/install-guides/gemini/)

With your agent ready, you can delegate the full workflow using a prompt. For example:

```text
Use Topo to deploy a containerized workload to my Arm target at user@my-target. Run a health check first, list compatible templates, choose a suitable one, clone it, and deploy it.
```

The agent reads the Topo `README.md`, runs health checks, selects a template, and deploys it end-to-end with minimal manual input.

## What you've accomplished

You have now deployed a containerized workload to your Arm-based Linux target using Topo. You validated the deployment by accessing the application in a web browser. You also learned how to stop the deployment and forward ports if needed.