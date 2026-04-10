---
title: Build a single-shot multimodal restock ticket on Armv9
weight: 7
layout: learningpathall
---

## Create the single-shot multimodal prompt (image + audio)

In this final project you will generate an **operational restock ticket** from **one single-shot multimodal prompt**.

You will combine:
- A **shelf image** to estimate shelf coverage and select a priority zone
- A **voice note** to extract tasks, quantities, zones, deadlines, and substitution policy

into **one multimodal inference** using MNN Omni.

This mirrors a real retail workflow: a staff member captures a shelf photo and records a quick voice note, and the device produces a ticket that can be executed immediately.


## Inputs

You will reuse the same local assets from previous modules:

- Shelf image: `~/mnn/assets/Pet_Food_Aisle.jpg.jpg`
- Voice note: `~/mnn/assets/restock_note.wav`

{{% notice Note %}}
Using local files avoids redirect and downloader issues.
{{% /notice %}}


## Output format

The output is a **single-line, bullet-style ticket** (segments separated by `;`), designed to remain readable even when terminals normalize newlines.

The ticket must include:

- **Coverage (image-derived):** `top=<high|medium|low>, middle=..., bottom=...`
- **Priority zone (image-derived):** `<top|middle|bottom>-<left|center|right>`
- **Tasks (audio-derived):** Task 1 and Task 2 with item, quantity, and zone
- **Deadline (audio-derived)**
- **Substitution policy (audio-derived)**
- **Notes and confidence**


## Step 1 Create the multimodal prompt (single line)

Create the multimodal prompt file. Keep the file as **one line**.

```bash
cat > ~/mnn/prompt_final_multimodal.txt <<'EOF'
<img>/home/radxa/mnn/assets/Pet_Food_Aisle.jpg.jpg</img> <audio>/home/radxa/mnn/assets/restock_note.wav</audio> You are an on-device retail replenishment assistant. Use the IMAGE to estimate facing coverage for the main LEFT shelf by level as high|medium|low and pick a priority zone. Use the AUDIO to extract item requests including quantities, zones, deadline, and substitution policy. Output EXACTLY ONE line using bullet-style segments separated by semicolons: Restock ticket; - Location: pet food aisle left shelf; - Coverage: top=<high|medium|low>, middle=<high|medium|low>, bottom=<high|medium|low>; - Priority zone: <top|middle|bottom>-<left|center|right>; - Task 1: <generic item> | qty <number or NOT_SURE> | zone <top|middle|bottom>-<left|center|right or NOT_SURE>; - Task 2: <generic item> | qty <number or NOT_SURE> | zone <top|middle|bottom>-<left|center|right or NOT_SURE>; - Deadline: <time or NOT_SURE>; - Substitution: <use similar substitute|no substitute|NOT_SURE>; - Notes: <short operational note>; - Confidence: <high|medium|low>. Rules: Qty/Deadline/Substitution must come from audio; if audio contains explicit numbers you must output them.
EOF
```

## Step 2 - Run the single-shot multimodal demo

Run `llm_demo` with the multimodal prompt:

```bash
cd ~/mnn/MNN/build
./llm_demo ~/mnn/Qwen2.5-Omni-7B-MNN/config.json ~/mnn/prompt_final_multimodal.txt
```

Your output should be a single line similar to:
```
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

Exact wording may differ, but the coverage/priority should be image-driven and the quantities/deadline/substitution should be audio-driven.


## Step 3 - Verify image and audio are both used (optional)

To verify true multimodal behavior, perform a simple A/B test.

- Swap the **audio** file: quantities/deadline/substitution should change.
- Swap the **image** file: coverage/priority zone should change.

To verify that the model is truly multimodal, perform a simple A/B test:

**Swap the audio**

- Keep the image fixed
- Replace the voice note with a different restock instruction
- **Expect:** `Coverage` and `Priority zone` remain the same; `Tasks`, `qty`, `Deadline`, and `Substitution` change according to the new audio

**Swap the image**

- Keep the audio fixed
- Change to a different shelf image
- **Expect:** `Coverage` and `Priority zone` change; `Tasks`, `qty`, and `Deadline` remain aligned with the original audio


## Checkpoint

You have completed this module when you can show:

- At least one **baseline multimodal ticket**
- One run where changing the **audio** changes only audio-derived fields
- One run where changing the **image** changes only image-derived fields

This demonstrates that your pipeline is performing **true multimodal reasoning** on-device.
