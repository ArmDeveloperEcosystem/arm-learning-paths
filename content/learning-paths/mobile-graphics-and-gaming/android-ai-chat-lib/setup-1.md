---
title: Project Setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Objective
In this learning path you will create a small chatbot Android app from scratch. The app will load a GGUF model of your choosing, and then run it in a chatbot format.

The app will use Arm's AI Chat library available from Maven Central, which provides an Android wrapper around llama.cpp, providing high-performance running of LLM models in the GGUF format.

For other examples of chatbots using this library you can use:
- the fully featured [Arm AI Chat app on Google Play](https://play.google.com/store/apps/details?id=com.arm.aichat), which can be used to test the performance and capabilities of mobile models, or
- the [AI Chat library GitHub example](https://github.com/arm/ai-chat/tree/use-maven-library/examples/llama.android), which is only slightly more complicated than this Learning Path.

## Project Setup 
Open Android Studio and create a new project of the type "Empty Views Activity". Name it however you like, and leave other options on default - for instance Minimum SDK will be 33.

