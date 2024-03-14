---
title: Profiling best practice
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Capturing reliable performance data
Here are a few things you can do to improve the reliability of performance data you capture from the Profiler:

1. Try to capture representative and repeatable captures

1. Turn off performance scaling if you can (which may involve root permissions on your device) as the device may be varying the CPU frequency to adapt to varying loads and temperatures

1. Use the same (or matching) device(s) when capturing and comparing multiple datasets

1. Performance data can be logged outside of the Unity Editor - you can log data from within your own C# scripts

1. Make use of profiling markers to highlight the code you want to measure in the Profiler and Analyzer
