---
title: Use the Neural Graphics Toolkit to build evidence
description: Use MLIA to assess supported models before deployment and Streamline to profile neural graphics workloads on NX hardware.
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Choose the tool for your next question

Your model toolkit connects model development to the integration decision. Model Gym supports the training, evaluation, quantization, and export workflow introduced in the previous chapter. ML Inference Advisor (MLIA) and Arm Streamline help you investigate whether a candidate fits your target and what happens when it runs in your application. Keep the released model as your baseline; profiling doesn't mean you need to train a replacement.

Use these two Learning Paths at different stages:

| Resource | Question it helps you answer | Evidence to keep |
| --- | --- | --- |
| [Estimate neural accelerator (NX) performance with ML Inference Advisor](/learning-paths/mobile-graphics-and-gaming/mlia-nx-performance-estimator/) | Is a supported model compatible with the selected target, and how do its estimated costs compare with another candidate? | Compatibility findings, performance reports, model identity, and target configuration |
| [Profile Arm Neural Technology workloads with Streamline](/learning-paths/mobile-graphics-and-gaming/streamline-nx/) | What executes on NX and shaders, and how does neural work relate to the rest of the application? | Saved captures, device and driver details, workload settings, and the interval you analyzed |

Keep estimates and measurements separate. Neither tool replaces the image-quality checks and whole-game evaluation you defined for your integration.

## Assess candidates with MLIA before deployment

Start with the MLIA Learning Path when you have a supported model input and want to investigate compatibility or compare model variants. Its development-host workflow uses public quantized MobileNet models to demonstrate conversion, operator compatibility checks, and the NX Performance Estimator. You don't need an NX device for those estimates.

The MobileNet examples teach the assessment workflow; they aren't NSS or NFRU models. Check the supported input formats and operators before applying that workflow to your own model. Don't assume every artifact exported by your training workflow is accepted directly.

Compare candidates under the same target profile and compiler configuration. Use the reports to select a change worth testing, not to claim a game-level speedup. A lower estimated cost doesn't prove that your model preserves quality or improves frame pacing.

If you have compatible NX hardware, the Learning Path also includes an optional device workflow using Scenario Runner and the Neural Statistics layer to return measured data to MLIA. That model-level check complements, rather than replaces, profiling your integrated game.

## Measure the integrated workload with Streamline

Use the Streamline Learning Path when you have a supported NX-capable Android device, a compatible driver, and a debuggable application using the ML extensions for Vulkan. It covers tool and device preparation, CLI or GUI capture, and interpretation of neural accelerator activity. Project Moku provides a representative workload for learning the process before you repeat it with your game.

A saved capture alone doesn't prove that you collected NX activity. Check the capture log, warnings, and relevant Timeline rows before drawing conclusions. Use Mali Timeline and Dispatch Graph Workloads to relate neural execution and shader work to the interval you're investigating.

Keep the scene, model, settings, and capture conditions repeatable. Compare the same interval after a change, then check image quality, presentation, power, and thermals against your original targets. A busy accelerator counter alone doesn't establish a bottleneck.

## Carry the evidence into your integration brief

Before choosing a candidate, check that your evidence answers four questions:

- Which model, target configuration, and application build produced each result?
- Which results are estimates, and which are device measurements?
- Does the candidate still meet your quality and integration targets?
- What remains untested, and who owns the next check?

If you don't yet have NX hardware, record the compatibility findings and estimates you have, and leave device validation open. Don't turn a promising estimate into a deployment claim.

## What you've learned

You can use MLIA to assess supported models before deployment and Streamline to investigate neural graphics execution in your application. You know which evidence each provides and where device and quality validation are still needed. Next, turn that evidence into your team's integration decision.
