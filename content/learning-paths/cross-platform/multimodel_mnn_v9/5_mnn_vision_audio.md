---
title: Convert spoken restock notes into structured tickets with MNN Omni
weight: 6
layout: learningpathall
---

## Introduction

In this module, you use an audio prompt and an MNN Omni model to convert a spoken restock note into a structured one-line ticket on an Armv9 system.

This mirrors a simple retail workflow. A store associate records a short voice note during a shelf walk, and the system converts it into a task that can be reviewed by staff or passed to another tool.

To keep the output predictable, this module uses a single-line format with semicolon-separated fields. This also helps when terminal output does not preserve line breaks consistently.

## Prepare the audio asset

This example assumes that `restock_note.wav` contains a short spoken instruction describing what to restock.

A suitable recording might say:

- please restock the bottom-left large pet food bags, add ten bags
- also restock the middle-left canned pet food, add twenty-four cans
- finish before 3 PM today
- if something is out of stock, use a similar substitute

From that audio, the model should extract:

- items
- quantities
- shelf zones
- deadline
- substitution policy

The goal is not full speech analytics. The goal is to turn a short spoken instruction into a compact operational ticket.

## Verify the audio format

Check that the input file is a WAV file:

```bash
file ~/mnn/assets/restock_note.wav
```

You should see output indicating that the file is a RIFF/WAV audio file.

If you only have an MP3 recording, convert it to a speech-friendly WAV format:

```bash
ffmpeg -y -i input.mp3 -ac 1 -ar 16000 -c:a pcm_s16le ~/mnn/assets/restock_note.wav
```

This creates a mono, 16 kHz, 16-bit PCM WAV file, which is a practical format for speech input.

The spoken content can be similar to:

```text
This is the pet food aisle, left shelf. Please restock the bottom left large pet food bags, add 10 bags. Also restock the middle left canned food, add 24 cans. Finish before 3 PM today. If something is out of stock, use a similar substitute.
```

## Create the audio prompt

Create a prompt file that attaches the WAV file and asks the model to return a single structured line.

{{% notice Note %}}
`llm_demo` commonly treats each line in the file as a separate prompt. Keep the full prompt on one line.
{{% /notice %}}

Create the prompt file:

```bash
cat > ~/mnn/prompt_audio_ticket.txt <<'EOF'
<audio>/home/radxa/mnn/assets/restock_note.wav</audio> You are a retail store replenishment assistant. Convert the spoken note into a restocking ticket. Output EXACTLY ONE line using bullet-style segments separated by semicolons: Restock ticket; - Location: pet food aisle left shelf; - Task 1: <generic item> | qty <number or NOT_SURE> | zone <top|middle|bottom>-<left|center|right or NOT_SURE>; - Task 2: <generic item> | qty <number or NOT_SURE> | zone <top|middle|bottom>-<left|center|right or NOT_SURE>; - Deadline: <time or NOT_SURE>; - Substitution: <use similar substitute|no substitute|NOT_SURE>; - Notes: <short note>; - Confidence: <high|medium|low>. Rules: do not invent quantities if not in audio.
EOF
```

If your username or home directory is different, replace `/home/radxa` with the correct local path.

This prompt asks the model to:

- use generic item names instead of brands
- return `NOT_SURE` for missing details
- preserve a one-line structure that is easy to read and parse

## Run the audio demo

Run `llm_demo` with the model configuration and the audio prompt:

```bash
cd ~/mnn/MNN/build
./llm_demo ~/mnn/Qwen2.5-Omni-7B-MNN/config.json ~/mnn/prompt_audio_ticket.txt
```

You should see output similar to:

```text
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
The exact wording can vary. What matters is that the response stays close to the requested structure and reflects the spoken content rather than invented details.
![image2 Prompt Audio Ticket](prompt_audio_ticket.gif)

## Verify the result

Check that:

- the quantities and deadline match the spoken note
- any missing field is returned as `NOT_SURE`
- the output remains on a single structured line
- the ticket is readable enough for a simple downstream workflow

If the model adds extra commentary after the ticket, tighten the prompt and rerun the command. If quantities or zones are wrong, verify the audio clarity and confirm that the WAV file was converted correctly.

## Next steps

In the next module, you will combine multimodal inference patterns into a practical restock workflow on Armv9.
