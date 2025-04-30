---
title: Other ideas for GitHub Copilot
weight: 11

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What else can I do with GitHub Copilot on this project?

GitHub Copilot can help you explore additional performance and optimization ideas:

- Test different compiler flags using Agent mode to automate iteration and identify the best combinations.
- Add Clang support to your Makefile and compare performance against GCC — performance can differ significantly depending on your code structure.
- Generate a wider range of data sizes and random patterns to stress-test functionality and measure performance under varied conditions.
- Explore alternative algorithm structures that rely on compiler autovectorization instead of NEON intrinsics — you might discover better performance simply by restructuring the C code.

AI tools won’t always generate high-performance code out of the box, but they can rapidly accelerate your experimentation and learning — especially in new areas of programming like NEON-based performance optimization.
