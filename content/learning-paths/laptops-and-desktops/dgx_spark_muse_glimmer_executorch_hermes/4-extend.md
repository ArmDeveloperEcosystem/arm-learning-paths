---
title: Extend your local agent
description: Add vision, faster decoding, voice interaction, custom tools, or scheduled tasks to your local Hermes and Muse Glimmer agent.
weight: 5
layout: learningpathall
---

## Extend your local agent

Use your Hermes–Muse Glimmer coding agent to help build its next capability. Choose one extension, provide the relevant documentation, and ask it to propose a small implementation and tests. Review the generated code and verify the result independently. You can develop code in this sandbox. Set up any extra dependencies or device access separately.

### Explore Muse Glimmer capabilities

Try one of these extensions:

- **Add image input.** Extend the text-only endpoint with vision artifacts so the agent can investigate a screenshot or interpret a diagram alongside your request. Follow [Meta's Muse Glimmer ExecuTorch guide](https://dev.meta.ai/docs/muse-glimmer/executorch) for vision-enabled serving. Adding an image to a prompt alone does not enable vision in the current export.
- **Explore DFlash speculative decoding.** DFlash uses a draft model to propose tokens that Muse Glimmer verifies. Export and serve the draft model, then compare response latency on the same coding task. See the [ExecuTorch Muse Glimmer example](https://github.com/pytorch/executorch/blob/main/examples/models/muse-glimmer/README.md) for the required artifacts and configuration.
- **Improve prompts and tool definitions.** Design a small tool with clear arguments and test whether the model calls it correctly. Use the [Muse Glimmer prompting guide](https://dev.meta.ai/docs/muse-glimmer/prompting) as a reference. Test any changes to the API settings against your endpoint.

### Extend Hermes with tools and interfaces

Choose a tool or interface to add:

- **Add voice interaction.** Explore [Hermes Voice Mode](https://hermes-agent.nousresearch.com/docs/user-guide/features/voice-mode) for speech recognition and spoken replies. Choose local speech providers to keep processing on your hardware. With SSH, use a microphone attached to Spark or build a laptop-side audio interface; SSH does not forward your laptop's microphone. The [offline voice chatbot Learning Path](/learning-paths/laptops-and-desktops/dgx_spark_voicechatbot/) provides a speech pipeline you can adapt to send transcribed requests to Hermes.
- **Build a document-search tool.** Use [Hermes plugins](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins) to add a tool that searches a dedicated folder of project documentation. Start with synthetic documents and test that answers identify their source files.
- **Connect existing tools.** Follow [Hermes MCP integration](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp) to connect a local tool server. Enable only the tools your task needs and check where the server runs: MCP tools do not automatically inherit the terminal container's restrictions.
- **Schedule a project check.** Use [Hermes scheduled tasks](https://hermes-agent.nousresearch.com/docs/user-guide/features/cron) to run a recurring check and save a report. Start with reporting only, and explicitly configure the scheduled agent's tool access.

Check that an extension supports the Hermes version pinned here. Skills contain reusable instructions; tools and plugins run code. Add one extension at a time and check which files, networks, devices, and credentials it can access.
