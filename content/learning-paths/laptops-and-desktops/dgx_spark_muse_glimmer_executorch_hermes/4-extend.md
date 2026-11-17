---
title: Extend your local Hermes and Muse Glimmer agent
description: Explore image input, faster decoding, voice interaction, custom tools, or scheduled tasks with your local Hermes and Muse Glimmer agent.
weight: 5
layout: learningpathall
---

## Extend your local agent

Use your Hermes–Muse Glimmer coding agent to help build its next capability. Provide the relevant documentation and ask the agent to propose a small implementation and tests. Review the generated code and verify the result independently. 

You can develop code in the sandbox that you used for the Learning Path. Set up any extra dependencies or device access separately.

### Explore Muse Glimmer capabilities

You can extend the agent by adding Muse Glimmer capabilities:

- Try other images: Give the agent a screenshot from a small project or a diagram and ask it to explain what it sees. For supported image inputs and serving options, see the [Meta Muse Glimmer ExecuTorch guide](https://dev.meta.ai/docs/muse-glimmer/executorch).
- Explore DFlash speculative decoding: DFlash uses a draft model to propose tokens that Muse Glimmer verifies. Export and serve the draft model, then compare response latency on the same coding task. For the required artifacts and configuration, see the [ExecuTorch Muse Glimmer example](https://github.com/pytorch/executorch/blob/main/examples/models/muse-glimmer/README.md).
- Improve prompts and tool definitions: Design a small tool with clear arguments and test whether the model calls it correctly. Use the [Muse Glimmer prompting guide](https://dev.meta.ai/docs/muse-glimmer/prompting) as a reference. Test any changes to the API settings against your endpoint.

### Extend Hermes with tools and interfaces

Choose a tool or interface to add to Hermes:

- Add voice interaction: Explore [Hermes Voice Mode](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode) for speech recognition and spoken replies. Choose local speech providers to keep processing on your hardware. With SSH, use a microphone attached to Spark or build a laptop-side audio interface. SSH doesn't forward your laptop's microphone. The [offline voice chatbot Learning Path](/learning-paths/laptops-and-desktops/dgx_spark_voicechatbot/) provides a speech pipeline that you can adapt to send transcribed requests to Hermes.
- Build a document-search tool: Use [Hermes plugins](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins) to add a tool that searches a dedicated folder of project documentation. Start with synthetic documents and test that answers identify their source files.
- Connect existing tools: Follow [Hermes MCP integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) to connect a local tool server. Enable only the tools that your task needs, and check where the server runs. MCP tools don't automatically inherit the restrictions of the terminal container.
- Schedule a project check: Use [Hermes scheduled tasks](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) to run a recurring check and save a report. Start with reporting only, and explicitly configure tool access for the scheduled agent.

Check that any capability you want to add is supported by the Hermes version pinned in the Learning Path. Skills contain reusable instructions, while tools and plugins run code. Add one capability at a time and check which files, networks, devices, and credentials it can access.

## What you've learned

You've identified possible extensions for the Hermes-Muse Glimmer coding agent.

To use the agent for your own project, mount a dedicated working directory. Keep acceptance tests outside the writable area of the agent.