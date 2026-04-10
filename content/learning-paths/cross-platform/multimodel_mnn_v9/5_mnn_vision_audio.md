---
title: Convert audio restock instructions into tickets with MNN Omni
weight: 6
layout: learningpathall
---

In this module you will convert a **spoken restock note** into a **readable, single-line restock ticket** using MNN Omni.

This mirrors a common retail workflow: an associate records a short voice note during a shelf walk, and the system converts it into an operational ticket that can be handed to staff or logged in a task system.

Because `llm_demo` output may normalize newlines on some terminals, this module uses a **single-line** format with `;`-separated fields.

## Step 1 - Prepare the audio asset

Before you run the demo, make sure you know what your `restock_note.wav` contains. This learning path assumes the WAV is a short “store associate voice note” describing what to restock.

### Suggested Audio Content Scenario

Record (or provide) a short voice note similar to the following:

* Please restock the bottom-left large pet food bags, add ten bags.  
* Also restock the middle-left canned pet food, add twenty-four cans.  
* Finish before 3 PM today. If something is out of stock, use a similar substitute.

Your goal in this module is to extract these fields from the audio:

- **Items**
- **Quantities**
- **Zones**
- **Deadline**
- **Substitution policy**

…and encode them as a **single-line ticket** with labeled fields.


### Verify the WAV file format

This demo expects a WAV (RIFF) file: For example `restock_note.wav` 

```bash
file ~/mnn/assets/restock_note.wav
```

If you only have an MP3 file, convert it to a suitable WAV format:

```bash
ffmpeg -y -i input.mp3 -ac 1 -ar 16000 -c:a pcm_s16le ~/mnn_lp/assets/restock_note.wav
```

This produces a **mono, 16 kHz, 16-bit PCM** WAV file, which is commonly used for speech models.

```
This is the pet food aisle, left shelf. Please restock the bottom left large pet food bags, add 10 bags. Also restock the middle left canned food, add 24 cans. Finish before 3 PM today. If something is out of stock, use a similar substitute.
```

## Step 2 - Create the audio prompt

llm_demo commonly treats ***each line*** as a separate prompt. Keep this prompt file as ***one line***.

This prompt instructs the model to:
- Use ***generic*** item labels (avoid brands unless clearly spoken)
- Output ***NOT_SURE*** for fields not stated in the audio
- Produce a single-line ticket that is easy to read and parse


```bash
cat > ~/mnn/prompt_audio_ticket.txt <<'EOF'
<audio>/home/radxa/mnn/assets/restock_note.wav</audio> You are a retail store replenishment assistant. Convert the spoken note into a restocking ticket. Output EXACTLY ONE line using bullet-style segments separated by semicolons: Restock ticket; - Location: pet food aisle left shelf; - Task 1: <generic item> | qty <number or NOT_SURE> | zone <top|middle|bottom>-<left|center|right or NOT_SURE>; - Task 2: <generic item> | qty <number or NOT_SURE> | zone <top|middle|bottom>-<left|center|right or NOT_SURE>; - Deadline: <time or NOT_SURE>; - Substitution: <use similar substitute|no substitute|NOT_SURE>; - Notes: <short note>; - Confidence: <high|medium|low>. Rules: do not invent quantities if not in audio.
EOF
```

## Step 3 - Run the audio demo

Run the audio demo:

```bash
cd ~/mnn/MNN/build
./llm_demo ~/mnn/Qwen2.5-Omni-7B-MNN/config.json ~/mnn/prompt_audio_ticket.txt
```

The expected result will be: 
```
config path is /home/radxa/mnn/Qwen2.5-Omni-7B-MNN/config.json
CPU Group: [ 1  2  3  4 ], 799999 - 1800968
CPU Group: [ 7  8 ], 799897 - 2199795
CPU Group: [ 5  6 ], 799897 - 2299896
CPU Group: [ 9  10 ], 799897 - 2399998
CPU Group: [ 0  11 ], 799897 - 2500100
The device supports: i8sdot:1, fp16:1, i8mm: 1, sve2: 1, sme2: 0
main, 274, cost time: 5745.955078 ms
Prepare for tuning opt Begin
Prepare for tuning opt End
main, 282, cost time: 767.578979 ms
prompt file is /home/radxa/mnn/prompt_audio_ticket.txt
Restock ticket;
- Location: pet food aisle left shelf;
- Task 1: large pet food bag | qty NOT_SURE | zone bottom-left;
- Task 2: canned food | qty 24 | zone middle-left;
- Deadline: before 3 p.m. today;
- Substitution: use similar substitute;
- Notes: restock before deadline;
- Confidence: medium. Restock the large pet food bag and canned food as per the given quantities. If any item is out of stock, replace it with a similar substitute. Make sure it's done by 3 p.m. today. Let me know if you need further clarification or if there's anything else on your mind.

```

![image2 Prompt Audio Ticket](prompt_audio_ticket.gif)

## Checkpoint

You have completed this module when:

- The ticket’s **quantities and deadline** match what is actually spoken
- Fields that are **not mentioned** in the audio are filled with `NOT_SURE` rather than invented values
- The resulting line is easy to parse and understand

