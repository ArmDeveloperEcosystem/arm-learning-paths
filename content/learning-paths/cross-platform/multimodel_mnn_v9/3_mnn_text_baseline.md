---
title: Validate text-only inference with an Omni model on Armv9
weight: 4
layout: learningpathall
---

## Introduction

In this section, you run a **text-only baseline** using the Omni model on an Armv9 Linux system. Before adding image and audio inputs, this baseline helps you confirm that the core inference path is working correctly with a simple prompt and predictable output behavior.

By the end of this section, you will be able to:

- run a reproducible text-only inference baseline on an Armv9 CPU
- verify that the MNN runtime, prompt input path, and token generation are working correctly
- establish a text baseline that you can use to compare later vision, audio, and multimodal runs

## Create a baseline prompt

Create a small prompt file in your workspace:

```bash
cat > ~/mnn/text_baseline_prompt.txt <<'EOF'
You are an on-device inference assistant. In one short sentence, describe the benefits of multimodal on-device inference.
EOF
```

{{% notice Note %}}
`llm_demo` commonly treats each line in the file as a separate prompt. Keep each prompt on a single line.
{{% /notice %}}

## Run `llm_demo` with the prompt file

Run `llm_demo` from the MNN build directory and pass both the model configuration and prompt file:

```bash
cd ~/mnn/MNN/build
./llm_demo ~/mnn/Qwen2.5-Omni-7B-MNN/config.json ~/mnn/text_baseline_prompt.txt
```

A successful run should load the model, report the detected CPU features, and return a text response for the prompt.

Example output:

```text
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


{{% notice Note %}}
When you run `llm_demo`, you may see a line like:
`The device supports: i8sdot:1, fp16:1, i8mm: 1, sve2: 1, sme2: 0`
This line reports hardware feature support on your CPU: **i8sdot**, **fp16**, **i8mm**, **sve2**, and **sme2**.  
A value of `1` means the feature is supported in hardware, and `0` means it is not.
{{% /notice %}}

## Check how prompt files are processed

To verify that the prompt file is read line by line, append a second prompt:

```bash
cat >> ~/mnn/text_baseline_prompt.txt <<'EOF'
What is the Arm CPU architecture?
EOF
```

Run the same command again:
```bash
cd ~/mnn/MNN/build
./llm_demo ~/mnn/Qwen2.5-Omni-7B-MNN/config.json ~/mnn/text_baseline_prompt.txt
```
You should now see two responses, one for each line in the prompt file.

```text
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

{{% notice Note %}}
Output length and coherence can vary significantly without a generation length limit. If a response repeats itself, this is normal model behavior without a `max_new_tokens` constraint. Focus on confirming that two distinct responses appear, one for each prompt line.
{{% /notice %}}

If you want to quickly sanity-check interactive mode:

```bash
cd ~/mnn/MNN/build
./llm_demo ~/mnn/Qwen2.5-Omni-7B-MNN/config.json
```

Enter a short prompt and confirm that the model returns a reply. Type `exit` or press Ctrl+C to quit.

## Check your results

You have completed this section when:

- `llm_demo` loads `config.json` successfully
- the prompt file produces one response per line
- the model returns non-empty text output
- the runtime completes without crashes or missing-library errors

## Next steps

In the next section, you will add an image input and validate the vision path of the Omni model on Armv9.
