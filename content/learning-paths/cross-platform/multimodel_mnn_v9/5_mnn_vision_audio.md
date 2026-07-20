---
title: Convert spoken restock notes into structured tickets with MNN Omni
weight: 6
layout: learningpathall
---

## Convert audio restock notes to structured output

In this section, you use an audio prompt and an MNN Omni model to convert a spoken restock note into a structured one-line ticket on an Armv9 system.

This mirrors a simple retail workflow where a store associate records a short voice note during a shelf walk, and the system converts it into a task that can be reviewed by staff or passed to another tool.

To keep the output predictable, this section uses a single-line format with semicolon-separated fields. This also helps when terminal output does not preserve line breaks consistently.

## Prepare the audio asset

To simplify the demonstration and improve clarity for this Learning Path, directly download the prepared audio file:

```bash
mkdir -p ~/mnn/assets
wget https://github.com/odincodeshen/multimodel_mnn_armv9/raw/main/assets/restock_note.wav -P ~/mnn/assets
```

The audio file contains a spoken restocking instruction similar to:

```text
This is the pet food aisle, left shelf. Please restock the bottom left large pet food bags, add 10 bags. Also restock the middle left canned food, add 24 cans. Finish before 3 PM today. If something is out of stock, use a similar substitute.
```

From this spoken note, the model extracts item names, quantities, shelf zones, a deadline, and a substitution policy. The goal isn't comprehensive speech analytics — it's converting a short spoken instruction into a compact operational ticket.

## Verify the audio format

Check that the input file is a WAV file:

```bash
file ~/mnn/assets/restock_note.wav
```

The output should indicate that the file is a RIFF/WAV audio file.

If you have your own MP3 recording, convert it to a speech-friendly WAV format:

```bash
ffmpeg -y -i input.mp3 -ac 1 -ar 16000 -c:a pcm_s16le ~/mnn/assets/restock_note.wav
```

This creates a mono, 16 kHz, 16-bit PCM WAV file, which is a practical format for speech input.

In store inspection scenarios with unreliable connectivity or environments where teams prefer not to upload audio in real time, local speech understanding on Armv9 has clear deployment value.

In this section, the audio input isn't just an audio prompt — it acts as on-device spoken task capture for store operations, turning a short spoken restocking note into structured operational input.

## Create the audio prompt

Create a prompt file that attaches the WAV file and asks the model to return a single structured line.

{{% notice Note %}}
`llm_demo` commonly treats each line in the file as a separate prompt. Keep the full prompt on one line.
{{% /notice %}}

Create the prompt file:

```bash
cat > ~/mnn/prompt_audio_ticket.txt <<EOF
<audio>$HOME/mnn/assets/restock_note.wav</audio> You are a retail store replenishment assistant. Convert the spoken note into a restocking ticket. Output EXACTLY ONE line using bullet-style segments separated by semicolons: Restock ticket; - Location: pet food aisle left shelf; - Task 1: <generic item> | qty <number or NOT_SURE> | zone <top|middle|bottom>-<left|center|right or NOT_SURE>; - Task 2: <generic item> | qty <number or NOT_SURE> | zone <top|middle|bottom>-<left|center|right or NOT_SURE>; - Deadline: <time or NOT_SURE>; - Substitution: <use similar substitute|no substitute|NOT_SURE>; - Notes: <short note>; - Confidence: <high|medium|low>. Rules: do not invent quantities if not in audio.
EOF
```

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

The output is similar to:

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
![Animated terminal output showing llm_demo processing an audio prompt and returning a structured restock ticket on Armv9#center](prompt_audio_ticket.gif "llm_demo audio prompt output on Armv9")

## Verify the result

A successful run should show that:

- the model can process the local audio file on Armv9
- the response keeps the requested ticket structure
- explicit spoken values such as quantity or deadline appear in the output
- missing or unclear fields are marked as `NOT_SURE` rather than invented

At this stage, the goal is not to evaluate full speech recognition quality. The goal is to validate that local audio understanding can extract operational task information that you can combine with other inputs later.

## What you've learned and what's next

In this section, you:

- Converted a spoken restock note into a structured ticket using audio inference
- Validated that MNN Omni can process local audio files on Armv9 CPU
- Confirmed that the model extracts operational details like quantities, zones, and deadlines from voice input

You've now validated text, vision, and audio inference independently.

In the next section, you'll combine these multimodal patterns into a single inference call that processes both image and audio inputs together.
