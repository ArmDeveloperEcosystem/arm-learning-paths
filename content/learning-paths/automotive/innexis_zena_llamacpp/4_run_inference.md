---
title: Run CPU inference and inspect the result
description: Run llama.cpp with a verified model and confirm that the Zena CSS guest generates text on its CPU.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run CPU inference and inspect the result

Run a short text prompt with the binary and model you prepared. Use one fixed command so its output can be traced back to the source revision, model file, and Zena guest.

## Check the command options

The tested Zena build exposes `--single-turn` and `--simple-io`. Confirm that your build exposes both options:

```bash
LP2_LLAMA_CLI="$LP2_WORK_DIR/llama.cpp/build/bin/llama-cli"
test -x "$LP2_LLAMA_CLI"
"$LP2_LLAMA_CLI" --help > "$LP2_WORK_DIR/llama-cli-help.txt" 2>&1
grep -F -- '--single-turn' "$LP2_WORK_DIR/llama-cli-help.txt"
grep -F -- '--simple-io' "$LP2_WORK_DIR/llama-cli-help.txt"
```

In the tested Zena guest, both searches returned matching help text:

```output
-st,   --single-turn                    run conversation for a single turn only, then exit when done
--simple-io                             use basic IO for better compatibility in subprocesses and limited
```

If either option is missing from your build, revise the command below before running it.

## Run a text-generation smoke test

Create a results directory and save the prompt beside the application output:

```bash
LP2_RESULTS_DIR="$LP2_WORK_DIR/results"
mkdir -p "$LP2_RESULTS_DIR"
printf '%s\n' 'Write one short sentence about a virtual platform.' \
    > "$LP2_RESULTS_DIR/first-prompt.txt"
```

Run the following command on the **Zena Linux guest**. It requests zero GPU layers with `-ngl 0` and saves both the log and exit code:

```bash
if "$LP2_LLAMA_CLI" \
    -m "$LP2_MODEL_FILE" \
    -t 4 -tb 4 -ngl 0 -c 512 -n 128 --temp 0 --seed 42 \
    --single-turn --simple-io \
    -p 'Write one short sentence about a virtual platform.' \
    > "$LP2_RESULTS_DIR/first-run.log" 2>&1; then
    printf '0\n' > "$LP2_RESULTS_DIR/first-run.exit"
else
    printf '%s\n' "$?" > "$LP2_RESULTS_DIR/first-run.exit"
fi
cat "$LP2_RESULTS_DIR/first-run.exit"
tail -n 60 "$LP2_RESULTS_DIR/first-run.log"
```

In the tested Zena guest, the saved exit code was `0`. The log identified build `b11482-b86d2f075`, loaded the verified Q4_0 file, and contained a non-empty generated response:

```output
build      : b11482-b86d2f075
model      : /root/zena-llamacpp/models/qwen2.5-0.5b-instruct-q4_0.gguf
ftype      : Q4_0

> Write one short sentence about a virtual platform.
A virtual platform is a platform that allows users to create and share digital content, such as images, videos, and documents, in a virtual environment.

Exiting...
```

The CPU-only build also reported that no usable GPU was found. This warning did not prevent inference. This request is a functional smoke test: inspect your own log to confirm that text appears between the prompt and `Exiting...`. The recorded answer used the general meaning of "virtual platform", so it is not a definition of an automotive Virtual SoC or a test of answer quality.

If model loading fails, check the hash and available memory before changing model or runtime settings. Save the failing log and exit code; a changed model or command is a new test condition.

## What you have learned

You have a recorded CPU text-inference result on the selected virtual platform. The next page changes only the prompt and collects the evidence from both runs.
