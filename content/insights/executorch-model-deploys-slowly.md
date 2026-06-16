---
title: Why is my ExecuTorch model slow on device?
question: Why is my ExecuTorch model slow on device?
description: Placeholder troubleshooting insight for ExecuTorch model performance.
summary: Slowness can come from model operators, unsupported acceleration paths, memory layout, or build configuration.
layout: insightall
date: 2026-06-16
lastmod: 2026-06-16
minutes_to_complete: 6
insight_type: Problem Solution
platform: Mobile
operatingsystems:
  - Android
goal: Optimize
tags_general:
  - ExecuTorch
  - ML
  - Performance
---

Check whether the model uses operators that map well to the target backend and whether the runtime was built with the expected acceleration options.

This placeholder answer should eventually include profiling steps and links to Arm ML optimization guidance.
