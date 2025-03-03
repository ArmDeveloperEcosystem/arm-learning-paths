---
title: Infrastructure Deployment
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How do I deploy my Copilot RAG Extension?

You can deploy your extension on whatever cloud infrastructure you prefer to use. These are the suggested requirements:

* A domain that you own with DNS settings that you control.
* A load balancer.
* An auto-scaling cluster in a private virtual cloud subnet that you can adjust the size of based on load.

For AWS users, Arm has provided a Copilot Extension deployment Learning Path to guide you through the process, called [Graviton Infrastructure for GitHub Copilot Extensions](../../copilot-extension-deployment/).

## Endpoints

Whatever method you use to deploy your Extension, make note of the final endpoint URLs:

* `/agent` - this is required for core functionality.
* `/marketplace` - this is optional, but necessary for receiving marketplace events.

Make sure you have the full URLs (including protocol and domain) for these endpoints to properly configure your GitHub application.
