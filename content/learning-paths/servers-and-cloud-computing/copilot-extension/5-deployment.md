---
title: Infrastructure Deployment
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How do I deploy my Copilot RAG Extension?

You can deploy on whatever cloud infrastructure you'd like to use. These are the suggested requirements:

1. A domain that you own with DNS settings that you control
2. A load balancer
3. An auto-scaling cluster in a private virtual cloud subnet that you can adjust the size of based on load

Arm has provided a Copilot Extension deployment Learning Path for AWS, called [Graviton Infrastructure for GitHub Copilot Extensions](../copilot-extension-deployment/).

Whatever method you use to deploy your Extension, make note of the final endpoint URLs, specifically

* `/agent` (required)
* `/marketplace` (optional, but needed to obtain marketplace events)

These are the endpoints that you will need full URLs for to configure your GitHub application.
