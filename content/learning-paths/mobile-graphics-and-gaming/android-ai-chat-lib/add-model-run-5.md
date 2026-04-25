---
title: Download a model and run the app
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download a mobile-compatible GGUF model

Before running the app, download a GGUF model file compatible with mobile device memory constraints. To run on a typical Android phone with 8 GB RAM, the model size should be significantly smaller than 8 GB to leave room for the operating system and other apps. 

A good example model is [google_gemma-3-4b-it-Q4_0.gguf](https://huggingface.co/bartowski/google_gemma-3-4b-it-GGUF/blob/main/google_gemma-3-4b-it-Q4_0.gguf). Gemma 3 is a capable model, and this 4 billion parameter version has been quantized with the Q4_0 schema, which works particularly well with Arm's [KleidiAI library](https://developer.arm.com/ai/kleidi-libraries). This quantization enables speed-ups on phones with [SME2](https://www.arm.com/technologies/sme2), [SVE2](https://developer.arm.com/documentation/102340/0100/Introducing-SVE2), and [Neon](https://www.arm.com/technologies/neon) capabilities.

Download Gemma 3 or another suitable GGUF model to your phone's Downloads folder.

## Run the app
In Android Studio, if you connect your test Android phone with a USB cable to your computer, you should now be able to run your LLM chatbot app. Make sure when you connect the phone it is in Developer Mode and you allow USB debugging.

In the bottom right there is a button "Import model". Clicking this will take you to downloads to be able to select the model you've downloaded, so the app can download it. Once it has finished copying and loading the model it will say "Model ready" at the top of the screen. Now if you click the text entry area at the bottom, you can type your questions and chat with the LLM.

![Screenshot of the simple AI chat app showing a conversation with Gemma 3 4B model. The screen displays the model ready status at the top, chat messages in the middle showing user prompts and assistant responses, and the text input area with send button at the bottom#center](app_screenshot.jpg "AI Chat app running Gemma 3 4B")

You now have a working on-device LLM chatbot running on your Android phone. The AI Chat library handles model loading, tokenization, and inference, with optimizations for Arm CPUs automatically applied based on your device's capabilities.

## Troubleshooting

If the model fails to load:
- Verify the GGUF file is compatible and not corrupted
- Check that your device has sufficient available memory (the model size plus at least 1-2 GB for the app and system)
- Ensure the model file was completely downloaded before importing

If inference is slow:
- Smaller quantized models (Q4_0, Q4_K_M) generally run faster than larger quantizations
- Close background apps to free up memory and CPU resources
- Models optimized with KleidiAI-compatible quantization schemes perform best on modern Arm CPUs
