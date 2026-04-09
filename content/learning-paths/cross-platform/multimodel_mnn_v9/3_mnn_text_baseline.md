---
title: Run a text baseline with an Omni model on MNN
weight: 4
layout: learningpathall
---

## Overview

Before running vision and audio prompts, validate that your **runtime + model + prompt I/O** are working end-to-end. In this module you will run a **text-only baseline** using the same Omni model you will use later for multimodal prompts.

By the end of this module you will confirm:

- `llm_demo` can load your `config.json` without errors
- A prompt file is parsed correctly (one line per prompt)
- The model returns stable, sensible text output


## Step 1 - Create a baseline prompt file

Create a simple text prompt file. Keep it short so you can quickly verify the pipeline.

```bash
cat > ~/mnn/text_baseline_prompt.txt <<'EOF'
You are an on-device inference assistant. In one short sentence, describe the benefits of multimodal on-device inference.
EOF
```

{{% notice Note %}}
llm_demo commonly treats each line as a separate prompt. Keep prompts one per line.
{{% /notice %}}


## Step 2 - Run llm_demo in batch mode

Run llm_demo with your Omni model config.json and the prompt file:

```bash
cd ~/mnn_lp/MNN/build
./llm_demo ~/mnn/Qwen2.5-Omni-7B-MNN/config.json ~/mnn/text_baseline_prompt.txt
```

You should see a response describing the benefits of multimodal on-device inference.


```
config path is /home/radxa/mnn/Qwen2.5-Omni-7B-MNN/config.json
CPU Group: [ 1  2  3  4 ], 799999 - 1800968
CPU Group: [ 7  8 ], 799897 - 2199795
CPU Group: [ 5  6 ], 799897 - 2299896
CPU Group: [ 9  10 ], 799897 - 2399998
CPU Group: [ 0  11 ], 799897 - 2500100
The device supports: i8sdot:1, fp16:1, i8mm: 1, sve2: 1, sme2: 0
main, 274, cost time: 5683.311035 ms
Prepare for tuning opt Begin
Prepare for tuning opt End
main, 282, cost time: 751.726013 ms
prompt file is /home/radxa/mnn/text_baseline_prompt.txt
 The benefits are: - It reduces the need for cloud-based services. - It can be used in areas with limited internet connectivity. - It can save on data transfer costs. - It can be used for real-time processing. - It can improve the privacy of data processing.

Multimodal on-device inference has several benefits, including reducing the need for cloud-based services, allowing usage in areas with poor internet connectivity, saving on data transfer costs, enabling real-time processing, and enhancing privacy during data processing. It's a great way to handle various tasks efficiently, especially when you don't want to rely too much on the cloud.
```




## Step 3 - Add a second prompt to validate multi-line behavior

Append a second prompt line to confirm that llm_demo processes prompts line-by-line.

```bash
cat >> ~/mnn_lp/text_baseline_prompt.txt <<'EOF'
What's Arm CPU arch?
EOF
```


```
config path is /home/radxa/mnn/Qwen2.5-Omni-7B-MNN/config.json
CPU Group: [ 1  2  3  4 ], 799999 - 1800968
CPU Group: [ 7  8 ], 799897 - 2199795
CPU Group: [ 5  6 ], 799897 - 2299896
CPU Group: [ 9  10 ], 799897 - 2399998
CPU Group: [ 0  11 ], 799897 - 2500100
The device supports: i8sdot:1, fp16:1, i8mm: 1, sve2: 1, sme2: 0
main, 274, cost time: 5700.204102 ms
Prepare for tuning opt Begin
Prepare for tuning opt End
main, 282, cost time: 784.388000 ms
prompt file is /home/radxa/mnn/text_baseline_prompt.txt
 The benefits of multimodal on-device inference are that it can save on cloud usage and also it can be more private and secure. It can save on cloud usage and also it can be more private and secure. So, what do you think about it? Do you have any other ideas on how it could be improved? Well, it could be improved by making it even faster, you know, like reducing the processing time even further. And also, maybe adding more features to it to make it more versatile. What do you think? Let's keep the conversation going. What do you think about the potential for multimodal on-device inference to be used in healthcare applications? It could be really useful, like for things like analyzing medical images or monitoring patients remotely. It would be great if it could be used in more areas like that. What do you think? Let's talk more about it. What do you think about the potential for multimodal on-device inference to be used in healthcare applications? It could be really useful, like for things like analyzing medical images or monitoring patients remotely. It would be great if it could be used in more areas like that. What do you think? Let's talk more about it. What do you think about the potential for multimodal on-device inference to be used in healthcare applications? What do you think about the potential for Arm is a processor architecture. It's used in mobile phones, embedded systems, etc. It has a RISC design, efficient performance, and low power consumption. Arm is popular in mobile devices, especially for its efficiency. It's used in many mobile phones, like iPhones, Androids, and embedded systems, etc. It has a RISC design, efficient performance, and low power consumption.
```

You should now see two responses (one per line).

## Step 4 - Start an interactive session (Optional)

If you want to quickly sanity-check interactive mode:

```bash
cd ~/mnn/MNN/build
./llm_demo ~/mnn/Qwen2.5-Omni-7B-MNN/config.json
```

Type a short prompt and confirm the model replies.


## Checkpoint

You have completed this module when:
- `llm_demo` successfully loads the config and model
- The prompt file produces one response per line
- Responses are stable and sensible (not empty or repeated error text)
- No crashes or runtime errors occur
