---
title: Interact with the Phi-3.5 Chatbot 
weight: 4

layout: learningpathall
---

## Try a text-only prompt

To begin, skip the image prompt and input the text prompt as shown in the example below:
![output](output.png)

Now exit the server.

Next, download a sample image from the internet using the following `wget` command:
```bash
wget https://cdn.pixabay.com/photo/2020/06/30/22/34/dog-5357794__340.jpg
```

## Try an image and text prompt

After downloading the image, provide the image file name when prompted, followed by the text prompt, as demonstrated in the example below:
![image_output](image_output.png)

## Observe Performance Metrics

As shown in the example above, the LLM Chatbot performs inference at a speed of **44 tokens/second**, with the time to first token being approximately **1 second**. This highlights the efficiency and responsiveness of the LLM Chatbot in processing queries and generating outputs.

## Further Interaction and Custom Applications

You can continue interacting with the chatbot by asking follow-up prompts and observing the performance metrics displayed in the terminal.

This setup shows how to build applications using the Phi-3.5 model for multimodal generation from text and image inputs. It also highlights the performance benefits of running Phi models on Arm CPUs.
