---
title: Build a single-shot multimodal restock ticket on Armv9
weight: 7
layout: "learningpathall"
---

## Goal

In this final project you will combine:

- A **shelf image** for coverage and priority zone
- A **voice note** for tasks, quantities, deadlines, and substitution policy

into **one multimodal prompt** that produces an **operational restock ticket** in a single inference.


## Inputs

You will reuse the same assets:

- Shelf image: `~/mnn_lp/assets/pet_food_aisle.jpg`
- Voice note: `~/mnn_lp/assets/restock_note.wav`


## Output format

The output is a **single-line, bullet-style ticket** that must include:

- **Coverage (image-derived):** `top=<high|medium|low>, middle=..., bottom=...`
- **Priority zone (image-derived):** `<top|middle|bottom>-<left|center|right>`
- **Tasks (audio-derived):** Task 1 and Task 2 with item, quantity, and zone
- **Deadline (audio-derived)**
- **Substitution policy (audio-derived)**
- **Notes and confidence**


## Prompt and run

Create the multimodal prompt file:

```bash
cat > ~/mnn_lp/prompt_final_multimodal.txt <<'EOF'
<img>/home/radxa/mnn_lp/assets/pet_food_aisle.jpg</img> <audio>/home/radxa/mnn_lp/assets/restock_note.wav</audio> You are an on-device retail replenishment assistant. Use the IMAGE to estimate facing coverage for the main LEFT shelf by level as high|medium|low and pick a priority zone. Use the AUDIO to extract item requests including quantities, zones, deadline, and substitution policy. Output EXACTLY ONE line using bullet-style segments separated by semicolons: Restock ticket; - Location: pet food aisle left shelf; - Coverage: top=<high|medium|low>, middle=<high|medium|low>, bottom=<high|medium|low>; - Priority zone: <top|middle|bottom>-<left|center|right>; - Task 1: <generic item> | qty <number or NOT_SURE> | zone <top|middle|bottom>-<left|center|right or NOT_SURE>; - Task 2: <generic item> | qty <number or NOT_SURE> | zone <top|middle|bottom>-<left|center|right or NOT_SURE>; - Deadline: <time or NOT_SURE>; - Substitution: <use similar substitute|no substitute|NOT_SURE>; - Notes: <short operational note>; - Confidence: <high|medium|low>. Rules: Qty/Deadline/Substitution must come from audio; if audio contains explicit numbers you must output them.
EOF
```

Run the final multimodal demo:

```bash
cd ~/mnn_lp/MNN/build

./llm_demo ~/mnn_lp/Qwen2.5-Omni-7B-MNN/config.json ~/mnn_lp/prompt_picture_coverage.txt
./llm_demo ~/mnn_lp/Qwen2.5-Omni-7B-MNN/config.json ~/mnn_lp/prompt_audio_ticket.txt
./llm_demo ~/mnn_lp/Qwen2.5-Omni-7B-MNN/config.json ~/mnn_lp/prompt_final_multimodal.txt
```

This sequence lets you compare:

1. Vision-only output  
2. Audio-only output  
3. Combined multimodal output  


## Verification

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
