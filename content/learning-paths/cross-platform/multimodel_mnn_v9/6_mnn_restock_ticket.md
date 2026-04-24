---
title: Build a single-shot multimodal restock ticket with MNN Omni
weight: 7
layout: learningpathall
---

## Combine image and audio inputs for multimodal inference

In the previous sections, you validated text, vision, and audio inference in isolation. This final section brings those three inputs together into a single prompt that combines a shelf image and a voice note to produce one structured restock ticket.

By the end of this section, you will have completed a full end-to-end multimodal workflow on an Armv9 CPU: shelf coverage from an image, tasks and deadlines from audio, and a combined ticket from one inference call.

## Create the single-shot multimodal prompt (image + audio)

In this final section, you combine image and audio inputs into a single multimodal prompt and generate one operational restock ticket on an Armv9 system.

This section demonstrates end-to-end multimodal task synthesis on an Armv9 CPU. Instead of testing a single modality in isolation, you combine image and audio inputs to produce one structured restocking ticket that can support a store action.

You will combine:
- A **shelf image** to estimate shelf coverage and select a priority zone
- A **voice note** to extract tasks, quantities, zones, deadlines, and substitution policy

into **one multimodal inference** using MNN Omni.

This mirrors a practical retail workflow. A store associate captures a shelf photo, records a short voice note, and the system produces a structured ticket that can be acted on immediately.

## Reuse the local assets

This section reuses the same assets from the previous examples:

- shelf image: `~/mnn/assets/Pet_Food_Aisle.jpg`
- voice note: `~/mnn/assets/restock_note.wav`

{{% notice Note %}}
Using local files keeps the example reproducible and avoids downloader or redirect issues.
{{% /notice %}}

## Define the ticket structure

To keep the output readable and easy to validate, request a single-line ticket with semicolon-separated fields.

The ticket should include:

- shelf coverage derived from the image
- a priority zone derived from the image
- tasks, quantities, and zones derived from the audio
- a deadline and substitution policy derived from the audio
- a short note and a confidence value

The goal is not perfect retail planning. The goal is to show that one prompt can combine visual context and spoken instructions into a compact result.

## Create the multimodal prompt

Create the prompt file and keep the full prompt on one line:

```bash
cat > ~/mnn/prompt_final_multimodal.txt <<EOF
<img>$HOME/mnn/assets/Pet_Food_Aisle.jpg</img> <audio>$HOME/mnn/assets/restock_note.wav</audio> You are an on-device retail replenishment assistant. Use the IMAGE to estimate facing coverage for the main LEFT shelf by level as high|medium|low and pick a priority zone. Use the AUDIO to extract item requests including quantities, zones, deadline, and substitution policy. Output EXACTLY ONE line using bullet-style segments separated by semicolons: Restock ticket; - Location: pet food aisle left shelf; - Coverage: top=<high|medium|low>, middle=<high|medium|low>, bottom=<high|medium|low>; - Priority zone: <top|middle|bottom>-<left|center|right>; - Task 1: <generic item> | qty <number or NOT_SURE> | zone <top|middle|bottom>-<left|center|right or NOT_SURE>; - Task 2: <generic item> | qty <number or NOT_SURE> | zone <top|middle|bottom>-<left|center|right or NOT_SURE>; - Deadline: <time or NOT_SURE>; - Substitution: <use similar substitute|no substitute|NOT_SURE>; - Notes: <short operational note>; - Confidence: <high|medium|low>. Rules: Qty/Deadline/Substitution must come from audio; if audio contains explicit numbers you must output them.
EOF
```

## Run the multimodal demo

Run `llm_demo` with the model configuration and the multimodal prompt:

```bash
cd ~/mnn/MNN/build
./llm_demo ~/mnn/Qwen2.5-Omni-7B-MNN/config.json ~/mnn/prompt_final_multimodal.txt
```

The output is similar to:

```text
config path is /home/radxa/mnn/Qwen2.5-Omni-7B-MNN/config.json
CPU Group: [ 1  2  3  4 ], 799999 - 1800968
CPU Group: [ 7  8 ], 799897 - 2199795
CPU Group: [ 5  6 ], 799897 - 2299896
CPU Group: [ 9  10 ], 799897 - 2399998
CPU Group: [ 0  11 ], 799897 - 2500100
The device supports: i8sdot:1, fp16:1, i8mm: 1, sve2: 1, sme2: 0
main, 274, cost time: 5781.158203 ms
Prepare for tuning opt Begin
Prepare for tuning opt End
main, 282, cost time: 787.130981 ms
prompt file is /home/radxa/mnn/prompt_final_multimodal.txt
Restock the bottom left large pet food bag, add 10 bags; also restock the middle left canned food, add 24 cans. Finish before 3 PM today. If something is out of stock, use a similar substitute.- Restock ticket: Location: pet food aisle left shelf, Coverage: top=low, middle=low, bottom=high, Priority zone: bottom-left, Task 1: pet food | qty 10 | zone bottom-left, Task 2: canned food | qty 24 | zone middle-left, Deadline: 3 PM today, Substitution: use similar substitute, Notes: Ensure proper storage conditions, Confidence: high.

```

The exact wording can vary. What matters is that image-derived fields stay tied to the shelf photo, and audio-derived fields stay tied to the spoken instruction.

## Verify that both modalities are used

To verify that the model is truly multimodal, perform a simple A/B test:

**Swap the audio**

Keep the image fixed and replace the voice note with a different instruction.

Verify that:

- `Coverage` and `Priority zone` stay similar
- `Task`, `qty`, `Deadline`, and `Substitution` change to match the new audio

**Swap the image**

Keep the audio fixed and replace the shelf image.

Verify that:

- `Coverage` and `Priority zone` change with the new image
- `Task`, `qty`, `Deadline`, and `Substitution` remain aligned with the original audio

## Verify the result

Check that:

- the output stays on one structured line
- the coverage and priority zone are based on the image
- the quantities, deadline, and substitution policy are based on the audio
- missing details are returned as `NOT_SURE` rather than invented

If the model adds extra text before or after the ticket, tighten the prompt and repeat the run.

### Completion checklist

You have completed this Learning Path when you can:

✓ Run text, vision, audio, and combined multimodal examples on Armv9

✓ Generate a final ticket from one image and one voice note

✓ Verify that changing one modality only affects the fields derived from that modality

## What you've learned and what's next

In this section, you:

- Combined image and audio inputs into a single multimodal prompt
- Generated a complete restock ticket from one inference call
- Verified that each modality contributes specific information to the final output

### Your multimodal workflow is complete

You've built a complete multimodal inference workflow on Armv9 using only the CPU:

1. Started with a text-only baseline
2. Added vision reasoning from a shelf image
3. Extracted structured tasks from a voice note
4. Combined both inputs into a single-shot restock ticket



### Next steps

Extend the workflow by:

- Saving tickets to JSON format
- Sending results to a local service or API
- Benchmarking latency and throughput across different Armv9 platforms
