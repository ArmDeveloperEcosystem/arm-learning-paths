---
title: Validate the execution boundaries
description: Verify that job files do not persist, execution time is bounded, and network cleanup completes after each microVM exits.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verify filesystem disposability

Verify that a file created by one job is absent from the next job's filesystem. This confirms that each execution starts from a fresh copy of the base image without retaining files from the previous run.

Run the marker program twice:

```bash
cd ~/firecracker-ai-sandbox
sudo ./sandbox/run-job.sh ./sandbox/examples/write-marker.sh
sudo ./sandbox/run-job.sh ./sandbox/examples/write-marker.sh
```

Each execution checks for `/tmp/ai-sandbox-marker` before creating it. Both jobs print:

```output
Created /tmp/ai-sandbox-marker inside this microVM.
Run this example again: the marker will be absent because the disk is disposable.
```

The second job starts from another copy of the clean base image, so it cannot see the marker created by the first job.

You can also run the combined demonstration:

```bash
cd ~/firecracker-ai-sandbox
sudo ./sandbox/demo.sh
```

The demonstration runs the architecture inspection program followed by two marker jobs.

## Verify the execution timeout

The timeout example sleeps longer than the configured job limit. Run it with a three-second limit and capture the expected nonzero status:

```bash
cd ~/firecracker-ai-sandbox
set +e
sudo FC_JOB_TIMEOUT=3 ./sandbox/run-job.sh ./sandbox/examples/timeout.sh
STATUS=$?
set -e
echo "runner exit code=$STATUS"
```

The result includes:

```output
outcome=timed_out
exit_code=124
runner exit code=124
```

The timeout runs on the host and terminates the SSH client if execution stops responding. After recording and printing the result, the cleanup trap terminates Firecracker and removes the job disk. Boot and file transfer happen before this timeout starts.

For this sleep example, exit code `124` demonstrates the timeout. The runner also labels exit code `137` as `timed_out`. A guest program can return either code itself, so this result label alone doesn't prove that an arbitrary job exceeded its deadline.

## Confirm cleanup

Check that no sandbox TAP device remains:

```bash
if ip link show fc-ai0 >/dev/null 2>&1; then
  echo "TAP cleanup failed"
else
  echo "TAP cleanup succeeded"
fi
```

The expected output is:

```output
TAP cleanup succeeded
```

Check that the runtime directory contains no job directories:

```bash
sudo find /opt/firecracker-ai/runtime -mindepth 1 -maxdepth 1 -type d -print
```

The command produces no output after cleanup. The `runner.lock` file remains and is reused to prevent concurrent jobs. These checks verify TAP and runtime-directory removal. 

## Understand the next security steps

This example demonstrates disposable microVM execution. Running untrusted code in production also requires host hardening, resource controls, and network policies suited to your workload. Implementing and validating those controls is outside the scope of this Learning Path. Before extending the example into a service, review the [Firecracker production host setup recommendations](https://github.com/firecracker-microvm/firecracker/blob/main/docs/prod-host-setup.md) and assess your deployment's security requirements.

## What you've accomplished

You've built an Arm-native execution sandbox where each shell program receives a dedicated Firecracker microVM, bounded resources, restricted networking, and a disposable filesystem. You also validated that filesystem state doesn't cross job boundaries and that the host stops programs that exceed their time limit.
