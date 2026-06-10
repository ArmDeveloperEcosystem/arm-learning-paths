---
title: Models in practice
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

Up to this point, the focus has been on evaluating neural graphics from a rendering and integration perspective. But if you've decided to give this a go, there's another layer you might need to think about: models.

If you’re working with technologies such as NSS or NFRU, model support is already handled for you. The models are provided, integrated, and ready to use through the Unreal Engine plugins. In practice, this means you can approach them much like any other engine feature: enable them, test them in your project, and decide if they fit.

If you want to go deeper, leading with NSS and with NFRU following shortly, Arm’s model development tools are a good place to start.

For most game teams, this is new ground. It raises questions such as:

- Where does the model come from?
- When is a prebuilt model enough?
- When do you need to adapt or retrain? What does that process actually look like in practice?

Instead, a good way to think about it is in stages.

Start with what's readily available — NSSD or NFRU — and use that to build intuition. Validate the results in your game. Use the available tools for fine-tuning and data collection for NSSD. Get a feel for how these techniques behave in your pipeline.

From there, if you’re interested in pushing further, this is where model work starts to become relevant. This section focuses on that path — how to take what’s available and make it work for your game.

If you decide to go beyond that, you’re stepping into more open-ended territory, where you’ll likely need to build and train models from the ground up (this is the case with NSSD).

## Stages

### Prove the runtime path with prebuilt models

The quickest way to get signal is to enable NSS in Unreal using Arm’s integration path, and learn about the lower-level Vulkan ML execution using the sample apps. At this stage, you’re checking that the data flows correctly through the pipeline and that the outputs behave as expected.

A strong baseline flow is:

- [Enable Neural Super Sampling in Unreal Engine with ML Extensions](/learning-paths/mobile-graphics-and-gaming/nss-unreal/)
- [Validate the lower-level Vulkan data graph path using sample appsn](/learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/)


### Capture your game before changing the model

After the baseline is stable, the next step is to look at your own content. Before touching the model, capture data that reflects how your game actually behaves — camera motion, lighting changes, particles, UI, scene cuts. This is where a lot of issues show up, and you need something repeatable to work from.

The Unreal data capture plugin enables this workflow for NSSD. You run the game, capture specific sequences, and export them into a dataset that can be reused for testing and training with NSSD.

[Use the dedicated Neural Graphics Data Capture app workflow in Unreal](/learning-paths/mobile-graphics-and-gaming/neural-graphics-data-capture-unreal/)

This creates a data contract for model iteration: when artifacts appear, you can tie them to repeatable gameplay windows instead of anecdotal visual checks. This step is what turns “that looks off” into something you can actually debug.

### Fine-tune only when issues are reproducible

Move into model tuning only after you can clearly reproduce a problem. At this stage, Model Gym becomes useful. You can target specific issues you’re seeing: ghosting in motion, instability in certain lighting conditions, or loss of detail in specific scenes.

When baseline integration is stable and issues are reproducible, move into Model Gym:

[Fine-tune neural graphics models using Model Gym](/learning-paths/mobile-graphics-and-gaming/model-training-gym/)

The important part is having a clear definition of what you’re trying to fix, and what “good enough” looks like. Without that, it’s easy to spend time training models without actually improving the result in a meaningful way.

### Optimize for runtime cost

When the output looks right, the focus shifts to model optimization. Going further than just using pre-built models — capturing data, tuning, optimizing, and validating — takes longer, but it’s still manageable if you approach it step by step.

Quantization is usually the first step here. Post-training quantization is quick and often good enough, but if it introduces visible issues — banding, ringing, loss of detail — you might need to move to quantization-aware training.

[Quantize neural upscaling models with ExecuTorch](/learning-paths/mobile-graphics-and-gaming/quantize-neural-upscaling-models/)

Before bringing anything back into your game, it’s worth validating the exported model and checking that it behaves as expected in the runtime environment. This avoids chasing issues that come from the deployment path rather than the model itself.

This also isn’t owned by a single role. Graphics or engine engineers typically handle integration and validation, while model work sits with someone comfortable working with data and training loops. Content owners play a role as well, because they define what “looks right” in the context of the game.

## Practical takeaway

Treat model customization as something you earn, not something you start with. Get a baseline working, capture real data from your game, and only then decide if tuning is worth it. In many cases, the default models will already get you most of the way there. When they don’t, you’ll have the data you need to fix the right problem.
