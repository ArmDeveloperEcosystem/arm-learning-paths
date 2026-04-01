---
title: Convert audio restock instructions into tickets with MNN Omni
weight: 6
layout: "learningpathall"
---

## Scenario

In this module you will convert a **spoken restock note** into a structured **restock ticket**.

For example, a store associate might say:

> We need to restock large dog food bags on the bottom-left, four units, before tomorrow afternoon. If large bags are out of stock, use medium bags as a substitute.

Your goal is to:

- Extract **items, quantities, zones, deadlines, and substitution policy**
- Encode them as a **single-line ticket** with clearly labeled fields

## Assets

Prepare a WAV file under `assets`:

```bash
file ~/mnn_lp/assets/restock_note.wav
```

If you only have an MP3 file, convert it to a suitable WAV format:

```bash
ffmpeg -y -i input.mp3 -ac 1 -ar 16000 -c:a pcm_s16le ~/mnn_lp/assets/restock_note.wav
```

This produces a **mono, 16 kHz, 16-bit PCM** WAV file, which is commonly used for speech models.


## Prompt design

You will ask the model to produce a **readable, single-line ticket** with:

- Item
- Quantity (or `NOT_SURE` if not spoken)
- Shelf zone
- Deadline
- Substitution policy
- Notes and confidence

Create the prompt file:

```bash
cat > ~/mnn_lp/prompt_audio_ticket.txt <<'EOF'
<audio>/home/radxa/mnn_lp/assets/restock_note.wav</audio> You are a retail store replenishment assistant. Convert the spoken note into a restocking ticket. Output EXACTLY ONE line using bullet-style segments separated by semicolons: Restock ticket; - Location: pet food aisle left shelf; - Task 1: <generic item> | qty <number or NOT_SURE> | zone <top|middle|bottom>-<left|center|right or NOT_SURE>; - Task 2: <generic item> | qty <number or NOT_SURE> | zone <top|middle|bottom>-<left|center|right or NOT_SURE>; - Deadline: <time or NOT_SURE>; - Substitution: <use similar substitute|no substitute|NOT_SURE>; - Notes: <short note>; - Confidence: <high|medium|low>. Rules: do not invent quantities if not in audio.
EOF
```

Run the audio demo:

```bash
cd ~/mnn_lp/MNN/build
./llm_demo ~/mnn_lp/Qwen2.5-Omni-7B-MNN/config.json ~/mnn_lp/prompt_audio_ticket.txt
```


## Checkpoint

You have completed this module when:

- The ticket’s **quantities and deadline** match what is actually spoken
- Fields that are **not mentioned** in the audio are filled with `NOT_SURE` rather than invented values
- The resulting line is easy to parse and understand

