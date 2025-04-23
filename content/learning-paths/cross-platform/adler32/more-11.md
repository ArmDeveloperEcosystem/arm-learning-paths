---
title: Other ideas for GitHub Copilot
weight: 11

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What else can I do with GitHub Copilot on this project?

You can investigate more topics using GitHub Copilot.

- Direct GitHub Copilot to try different compiler flags and use Agent mode to iterate through the options to find the best solution. 
- Add support for the Clang compiler to the Makefile and compare the results to GCC. Depending on the application code, changing the compiler can result in improved performance.
- Use GitHub Copilot to generate different data sizes and random data patterns to further investigate correct functionality and performance.
- Try different algorithm implementations that use compiler autovectorization instead of NEON intrinsics or break down the Adler32 checksum into smaller blocks of data. It may be possible to get even better performance without NEON using the compiler and a better structure for the C code.

While AI tools do not create performance code for every programming problem, they can be a big help to get you started in a new area of programming such as performance optimization using NEON intrinsics.