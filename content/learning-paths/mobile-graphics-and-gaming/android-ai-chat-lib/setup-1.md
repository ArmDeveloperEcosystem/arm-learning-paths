---
title: Create the Android project
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this Learning Path you will create a chatbot Android app from scratch that loads a GGUF model and runs it in a conversational format.

The app uses Arm's AI Chat library, available from Maven Central. The library provides an Android wrapper around llama.cpp with optimizations for Arm CPUs, delivering high-performance execution of LLM models in the GGUF format.

## Reference implementations

For additional examples of chatbots using this library, you can explore:
- The [Arm AI Chat app on Google Play](https://play.google.com/store/apps/details?id=com.arm.aichat), which demonstrates the performance and capabilities of mobile LLM models
- The [AI Chat library GitHub example](https://github.com/arm/ai-chat/tree/use-maven-library/examples/llama.android), which provides a slightly more feature-rich implementation

## Create the project

Open Android Studio and create a new project of the type "Empty Views Activity". Name it `simpleaichat`, and set the Minimum SDK to 33 (Android 13).

You now have an empty Android project ready for development. In the next section, you'll add the AI Chat library dependency and configure the project to load the required native libraries.

