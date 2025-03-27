---
title: Inference with Vision Chatbot
weight: 6

layout: learningpathall
---

## Access the Web Application

Open the web application in your browser using the external URL:

```bash
http://[your instance ip]:8501
```

{{% notice Note %}}

To access the links you might need to allow inbound TCP traffic in your instance's security rules. Always review these permissions with caution as they might introduce security vulnerabilities.

For an Axion instance, you can do this from the gcloud cli:

gcloud compute firewall-rules create allow-my-ip \
    --direction=INGRESS \
    --network=default \
    --action=ALLOW \
    --rules=tcp:8501 \
    --source-ranges=[your IP]/32 \
    --target-tags=allow-my-ip

For this to work, you must ensure that the allow-my-ip tag is present on your Axion instance.

{{% /notice %}}
## Interact with the LLM

You can upload an image and enter the prompt in the UI to generate response.

You should see LLM generating response based on the prompt considering image as the context as shown in the image below:
![browser_output](browser_output.png)

## Further Interaction and Custom Applications

You can continue to query on different images with prompts and observe the response of Vision model on Arm Neoverse based CPUs.

This setup demonstrates how you can create various applications and configure your vision based LLMs. This Learning Path serves as a guide and example to showcase the LLM inference of vision models on Arm CPUs, highlighting the optimized inference on CPUs.