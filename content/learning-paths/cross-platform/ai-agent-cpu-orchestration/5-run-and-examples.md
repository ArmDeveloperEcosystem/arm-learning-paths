---
title: Run the agent and read the timeline
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run the agent

Make sure both pieces are in place before you start:

- Ollama is running and serving `gemma3:4b` (from the previous section).
- Your virtual environment is active and `SERPER_API_KEY` is set in the current terminal.

From your project directory, start the agent:

```bash
python3 concierge_agent.py
```

The agent greets you and waits for a question:

```output
Hello! I am your local concierge agent.
Ask me anything - I research topics by browsing multiple websites in real time.
Make sure Ollama is running in the background.
Type "quit" or "exit" to end the session.

What would you like to find?
>
```

## Ask a research question

Type a question that benefits from searching and reading several pages. For example:

```text
Find three highly rated ramen restaurants in San Francisco that are open late
```

As the agent works, watch the log lines. Cyan `[CPU]` lines show orchestration and web I/O; yellow `[GPU]` lines show each model call:

```output
[GPU] Thinking with local Gemma model...
[CPU] Expanding base query 'late night ramen San Francisco' into multiple variants...
[CPU] Generated 3 search variants: [...]
[CPU] Dispatching 3 parallel search threads...
[CPU] Merging search results and deduplicating URLs...
[GPU] Thinking with local Gemma model...
[CPU] Dispatching 8 parallel browse threads...
[CPU] Running TF-IDF ranking on scraped content...
[CPU] Deduplicating sentences across all scraped sources...
[CPU] Extracting named entities from aggregated content...
[GPU] Thinking with local Gemma model...
```

The agent then prints a fact-checked summary that answers your question.

<!-- TODO: replace with a real screenshot of the CPU/GPU log lines for a query -->
![Terminal showing interleaved CPU and GPU log lines as the agent answers a query alt-text#center](agent_run_logs.png "The agent logs every CPU orchestration step in cyan and every GPU model call in yellow.")

## Read the timing breakdown

After each answer, the agent prints how the time was spent:

```output
--- Processing Timeline ---
CPU operations:             4.812s
GPU input token processing: 1.934s
GPU token generation:       3.057s
GPU total:                  4.991s
```

These numbers separate the three kinds of work:

- **CPU operations** – every orchestration and text-processing stage combined.
- **GPU input token processing** – the time the model spends reading each prompt before producing output (prefill).
- **GPU token generation** – the time spent writing the answers.

{{% notice Note %}}
Your exact numbers depend on your hardware, the model size, and how many pages the agent reads. The point isn't the absolute values, but the fact that CPU work is a substantial share of every query.
{{% /notice %}}

## Read the timeline

Below the breakdown, the agent prints a text-based timeline. Each character is a slice of wall-clock time, color-coded by what was active:

```output
CCCCCCCPGGGGCCCCCCCCCCCCCCPGGGGGGGGCCCCCCCCCCCCCCCCCCCPGGGGGGGGGGGG
C=CPU (orchestration + web I/O) P=GPU input token processing G=GPU token generation .=idle
Total: 9.803s
```

Reading left to right, you can see the pattern of an agentic query: long stretches of CPU work (`C`) for searching, browsing, and processing, punctuated by short GPU bursts where the model reads a prompt (`P`) and generates text (`G`).

<!-- TODO: replace with a real screenshot of the colored timeline output -->
![Color-coded timeline showing long CPU stretches between short GPU bursts alt-text#center](agent_timeline.png "The timeline shows the CPU active for most of the query, with the GPU running in short bursts.")

## Try more queries

The agent keeps conversation history, so you can ask follow-up questions in the same session. Try a few different kinds of research tasks and compare their timelines:

```text
Compare the battery life of the three most recommended noise-cancelling headphones
```

```text
Summarize the key differences between the latest Raspberry Pi models
```

Type `quit` or `exit` to end the session.

In the next section, you'll look more closely at why the CPU does so much of the work in an agentic workflow.
