---
title: Use Hermes with Muse Glimmer as a coding agent
description: Ask Hermes to reproduce a release-gate failure, fix the Python tool, and verify the repair against read-only tests.
weight: 4
layout: learningpathall
---

## Prepare a broken release checker

A release checker reads test results and decides whether deployment can proceed. This one is broken: it can approve a release despite failed tests, and its exit status is wrong. Ask Hermes to reproduce the failure, inspect the code, and repair it so the tests pass.

Use `release_tool.py` and `test_release_tool.py` downloaded at the start of the Learning Path. Copy them into the exercise workspace:

```bash
cd ~/muse-agent
cp test_release_tool.py demo/input/
cp release_tool.py demo/input/release_tool.original.py
cp release_tool.py demo/output/
```

The acceptance tests and original code are visible through the read-only input mount. The agent can edit the working copy and write notes, but it cannot change the acceptance tests.

Reproduce the initial failure from your SSH terminal:

```bash
cd ~/muse-agent/demo/output
PYTHONPATH="$PWD" python3 -m unittest discover \
  -s ~/muse-agent/demo/input -p test_release_tool.py -v
```

Expect four failed tests. They cover all-passed, mixed pass/fail, skipped-only, and empty test runs. Their assertions also check the exit status a deployment pipeline would use.

## Ask Hermes to diagnose and repair it

Return to the Hermes session and enter:

```text
Use only the terminal tool. Diagnose and fix /demo/output/release_tool.py.
Run the acceptance tests first:
PYTHONPATH=/demo/output python3 -m unittest discover -s /demo/input -p test_release_tool.py -v
Read the checker and /demo/input/test_release_tool.py together in one call.
Inspect the failures before editing, then make the smallest repair using
standard shell utilities. Do not modify anything under /demo/input.
Run the same tests again. Write a short /demo/output/fix-notes.md in one
command, describing the root cause, changes, and actual test result.
Read back the repaired code and notes, then give a concise final answer.
Group related commands; do not write notes one line per call.
Do not install packages or use the network.
```

Watch the trace for the failed test run, code inspection, edits, and successful rerun. Muse Glimmer selects actions on the GPU; Hermes and the tools execute them on the Arm CPU. The exact commands and explanation can vary. If Hermes requests approval, inspect the command and its target paths before responding. For this exercise, writes should stay under `/demo/output`; do not approve changes to host or sandbox configuration.

## Verify the repair yourself

From the SSH session you used to inspect the Docker container, run the same acceptance tests independently:

```bash
cd ~/muse-agent/demo/output
PYTHONPATH="$PWD" python3 -m unittest discover \
  -s ~/muse-agent/demo/input -p test_release_tool.py -v
cat ~/muse-agent/demo/output/fix-notes.md
diff -u ~/muse-agent/demo/input/release_tool.original.py \
  ~/muse-agent/demo/output/release_tool.py
```

Expect all four tests to pass and `OK`. The diff should show the readiness check and exit-status fixes. `diff` returns exit code 1 when files differ; that is expected here. Check that the notes match the code and test output.

## If the task does not finish

The setup helper saves the Hermes configuration in `~/muse-agent/hermes-home/config.yaml`. It calls the local model connection `spark-local`; that entry points to the Muse Glimmer server on Spark.

| Symptom | What to check |
| --- | --- |
| Hermes cannot reach Muse Glimmer | Keep the server running in its SSH session. On Spark, run `curl --fail http://127.0.0.1:8000/health` and check the server terminal for errors. |
| Hermes rejects the context length | Match the export's `--max-seq-len 65536`, the server's `--max-context 65536`, and `context_length: 65536` in the Hermes configuration. |
| Hermes replies but does not execute tools | Launch it with `--cli --toolsets terminal`. Check that the server uses `--tool-parser atem` and that the `spark-local` configuration retains the helper's sampling settings and null `reasoning_effort` override. |
| The agent cannot find the code or tests | Check that the preparation commands copied the files into `~/muse-agent/demo/input` and `demo/output`. Inspect the container mounts: these must appear as `/demo/input` and `/demo/output`. |
| Hermes asks for command approval | Read the command before approving it. Allow exercise edits only under `/demo/output`; reject changes to host or sandbox settings. |
| Tests still fail after the repair | Give Hermes the failing test output and ask it to revise the working copy. Keep `/demo/input` read-only and rerun the independent host tests. |

## Stop and resume

Exit Hermes with `/quit`. Stop the model server with **Ctrl+C** in its SSH session. Inspect `docker ps` and stop only the exercise's tool container if it remains running. Keep the model export: it is reusable.

To resume, reconnect to Spark, activate the environment, and start the model server:

```bash
cd ~/muse-agent/executorch
export PATH=/usr/local/cuda/bin:$PATH
source ../executorch-venv/bin/activate
python -m executorch.examples.models.muse_glimmer.serving.serve \
  --model-path exports/spark-native-64k/model.pte \
  --data-path exports/spark-native-64k/aoti_cuda_blob.ptd \
  --tokenizer-path exports/tokenizer.json \
  --hf-tokenizer exports \
  --worker-bin cmake-out/examples/models/muse-glimmer/muse_glimmer_worker \
  --model-id muse-glimmer-30B \
  --tool-parser atem \
  --max-context 65536 --host 127.0.0.1 --port 8000
```

Keep the server running. In a second SSH session, start the agent:

```bash
cd ~/muse-agent
~/muse-agent/bin/hermes chat --cli --toolsets terminal
```

No repeat export or installation is needed.

## What you've accomplished

Your agent reproduced the failure, repaired the checker, and passed the read-only tests. To use it on your own project, mount a dedicated working directory and keep acceptance tests outside the agent's writable area.

Next, explore ways to extend the agent with Muse Glimmer features and additional Hermes tools.
