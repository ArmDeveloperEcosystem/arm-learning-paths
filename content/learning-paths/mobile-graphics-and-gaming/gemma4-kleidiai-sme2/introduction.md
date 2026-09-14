---
title: Understand the benchmark workflow
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---



You'll complete the workflow in the following order:

Start by creating a workspace and cloning LiteRT-LM `v0.16.1`, KleidiAI `v1.30.0`, and upstream XNNPACK with the SME2 Int4 and Int2 support. 

1. Create a workspace and clone LiteRT-LM `v0.16.1`, KleidiAI `v1.30.0`, and
   upstream XNNPACK with the SME2 Int4 and Int2 support.
2. Create a historical XNNPACK baseline worktree from before the SME2 support.
3. Download the Gemma 4 E2B `.litertlm` model from Hugging Face.
4. Build and benchmark the baseline and upstream-optimized variants with
   identical settings at one and four CPU threads.
5. Compare steady-state prefill and decode throughput.



## What you've accomplished and what's next

You've learned about the benchmark workflow and confirmed that your device supports SME2. 

Next, you'll set up the benchmark workspace.
