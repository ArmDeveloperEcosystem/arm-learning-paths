---
title: Understand the Arm ML Inference Advisor

description: Understand where MLIA fits in model preparation and how Vela, Corstone FVP, Model Explorer, and runtime profiling tools support different checks.

weight: 2

### FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Why use MLIA 

Use Arm ML Inference Advisor (MLIA) to evaluate whether a machine learning model is suitable for a target inference platform.

You'll use MLIA from the command line to check model compatibility, estimate performance, and read advice that points toward useful model changes. Arm Ethos-U is the example target in the Learning Path.

MLIA is most useful before full deployment or runtime profiling, when you're asking questions such as:

- Will this model map cleanly to my target?
- Which operators or layers are likely to matter most for performance?
- Is the model compute-bound, memory-bound, or affected by low MAC utilization?
- Is the model well-optimized for my Arm target hardware?
- What should I investigate before building firmware or running on a board?

MLIA doesn't make the final optimization decision for you. It gives target-aware evidence so that you can decide what to change, what to measure next, and which workflow stage deserves attention.

The MLIA CLI is the primary workflow in this Learning Path. You'll use the CLI to complete the following tasks:

- Discover installed targets, target profiles, and backends
- Run compatibility checks
- Run performance analysis
- Inspect advice and metrics

If you want to automate the same checks, you can optionally use the Python API. The API is useful when you want to embed MLIA results in another product, dashboard, CI job, or tool.

## How you should use MLIA

MLIA isn't a replacement for graph visualization or runtime profiling. It's an advisory layer that helps earlier in the model preparation workflow. The following table demonstrates the questions that you can answer by using MLIA with other tools:

| Tool or backend | Use it to answer |
| --- | --- |
| MLIA | Is this model suitable for my target, and what should I change? |
| Vela | Which operators are supported, and which layers dominate compiler-estimated cycles? |
| Corstone FVP | What NPU performance counters does a packaged `.pte` artifact produce for the whole model run on a virtual platform? |
| Model Explorer | What does the generated model artifact graph look like? |
| Runtime-specific profiling tools | What happened when the model ran? For example, use ETRecord, ETDump, and ExecuTorch Inspector for ExecuTorch deployments. Use LiteRT benchmark and profiling tools for LiteRT deployments. |

Vela-backed MLIA checks use compiler estimates. The checks can include operator-level breakdowns, such as which layers dominate estimated cycles or have low MAC utilization. 

Corstone-backed MLIA checks run a packaged `.pte` file on an FVP and report NPU performance counters for the whole model run. The checks don't provide per-layer estimates or operator breakdowns.

Model Explorer can show how an ExecuTorch `.pte` artifact is partitioned into delegate regions. Runtime-specific profiling tools can show behavior after you have a runnable deployment.

Use the following tools together:

- Use MLIA before or during model preparation.
- Use Model Explorer to inspect generated artifacts and delegation structure.
- Use runtime profiling tools after you can execute the model.

## Supported model formats

MLIA can analyze different kinds of model artifacts depending on what workflow you are using and the stage you want to analyze.

| Format | Where it fits |
| --- | --- |
| `.pte` | Serialized ExecuTorch program. Ethos-U `.pte` performance analysis uses Corstone backends. |
| `.tflite` | LiteRT model format used in many Ethos-U and embedded ML workflows. |
| `.tosa` | Intermediate representation consumed by compiler/backend flows such as Ethos-U Vela. |

## What you've learned and what's next

You've learned what MLIA does, what you use it for, and how MLIA fits alongside other tools.

Next, you'll install MLIA and inspect the capabilities available in your environment.
