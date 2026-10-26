---
title: What's next?
description: Review what you can integrate now and see how the final playbook will move from prepared content to deployment on NX devices.
weight: 9
aliases:
    - /learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-integrate/07-commit-next-move/

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Key takeaways

You now have a route from interest to evidence. Neural Frame Rate Upscaling (NFRU) provides the most direct starting point, through the Unreal Engine plugin or the open SDK for other engines. Neural Super Sampling and Denoising (NSSD) offers a more ambitious path for teams ready to explore new rendering workflows with Arm. Custom model work comes later, when repeatable testing shows that the released model doesn't meet your needs.

Carry the following decisions forward:

- Let your game content and target measurements determine the route.
- Start with the released integration and model before you customize either one.
- Test image quality, performance, frame pacing, power, and thermals together.
- Keep a fallback for devices or content that cannot use the neural path.

Capture the result in a short integration brief. Record the chosen route, representative test content, measurable targets, and named owners.

Include the [model toolkit evidence](/learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-integrate/07-model-toolkit/) relevant to your route. Evidence can include ML Inference Advisor (MLIA) compatibility findings and estimates for supported models. It can also include Streamline captures when you have a supported neural accelerator (NX) target. 

Label estimates and measurements separately, record any outstanding device validation, and define the fallback.

## The next chapter: deploy

The next turning point comes when NX devices reach the market. The question will change from *can this work for your game?* to *how do you deploy it on the devices players use?*

The third and final playbook will follow that path from a proven integration to a shipping build. The playbook will cover how to deploy the content prepared here and validate it on NX hardware. It will also include guidance to measure production performance and power, and plan support across devices with different capabilities.

Until then, complete your chosen integration route. Preserve the models, captures, measurements, and decisions behind it. Those artifacts become the starting point for deployment.
