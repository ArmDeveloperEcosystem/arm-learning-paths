---
title: Run code in a disposable microVM
description: Execute a shell program in a fresh Arm Firecracker microVM and inspect the retained job results.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Download the sandbox runner

From `~/firecracker-ai-sandbox`, create the runner directories:

```bash
cd ~/firecracker-ai-sandbox
mkdir -p sandbox/examples
```

Download the runner and example programs:

```bash
cd ~/firecracker-ai-sandbox
BASE_URL=https://raw.githubusercontent.com/ArmDeveloperEcosystem/arm-learning-paths/main/content/learning-paths/servers-and-cloud-computing/firecracker-ai-sandbox

for FILE in 00-common.sh run-job.sh demo.sh; do
  wget -q "$BASE_URL/files/sandbox/$FILE" -O "sandbox/$FILE"
done

for FILE in hello-arm.sh write-marker.sh timeout.sh; do
  wget -q "$BASE_URL/files/sandbox/examples/$FILE" -O "sandbox/examples/$FILE"
done

chmod +x sandbox/*.sh sandbox/examples/*.sh
```

Verify that the downloads completed successfully before running the scripts as root. This lists the files in the `sandbox/` directory, including the `sandbox/examples/` subdirectory. 

```bash
find "$PWD/sandbox" -maxdepth 2 -type f -name "*.sh" -printf "%P\n" | sort
```

The expected output is:

```output
00-common.sh
demo.sh
examples/hello-arm.sh
examples/timeout.sh
examples/write-marker.sh
run-job.sh
```

## Run the first job

Use the supplied `hello-arm.sh` program to demonstrate how a sandbox could execute code submitted by an AI coding agent. This simple Bash program reports the guest architecture, kernel, CPU count, and memory. The runner copies it into a fresh microVM and executes it with `/bin/bash`.

The program uses tools already installed in the base image; jobs cannot rely on outbound IPv4 access to install dependencies.

Start a microVM and execute the architecture inspection program:

```bash
cd ~/firecracker-ai-sandbox
sudo ./sandbox/run-job.sh ./sandbox/examples/hello-arm.sh
```

The output is similar to:

```output
Job:       20260928T140000Z-12345
Resources: 1 vCPU, 512 MiB, 15s timeout
Cloning a disposable root filesystem...
Booting the microVM...
Executing inside the microVM...

--- stdout ---
Hello from an ephemeral AI code-execution sandbox
architecture=aarch64
kernel=6.1.186
cpus=1
...
--- result ---
job_id=20260928T140000Z-12345
outcome=succeeded
exit_code=0
...
```

The kernel version and job identifier can differ. The important values are `architecture=aarch64`, `cpus=1`, `outcome=succeeded`, and `exit_code=0`.

After the result is printed, the cleanup trap stops Firecracker and removes the job's TAP device and writable root filesystem.

## Inspect retained results

List the result directories on the host:

```bash
sudo find /opt/firecracker-ai/results -mindepth 1 -maxdepth 1 -type d -printf "%f\n"
```

Identify the most recent result and inspect its metadata:

```bash
RESULT_DIR=$(sudo find /opt/firecracker-ai/results -mindepth 1 -maxdepth 1 -type d -printf '%T@ %p\n' | sort -nr | head -n1 | cut -d' ' -f2-)
sudo cat "$RESULT_DIR/result.env"
```

After the runner reaches the execution phase and writes its result, the result directory contains:

- `stdout`: output written by the guest program
- `stderr`: errors written by the guest program or SSH
- `serial.log`: Firecracker guest serial output
- `result.env`: outcome, exit code, duration, source hash, and resource settings

Keep the source file unchanged until the runner exits. The runner computes its SHA-256 hash after execution, so editing the host file during a job can make the recorded hash differ from the program copied into the guest.

The `duration_ms` field measures the host-side SSH execution phase, excluding disk preparation, guest boot, file transfer, and cleanup. If startup fails, `result.env` might not exist. Inspect the retained `serial.log` for boot errors and check for conflicting routes or host firewall rules if SSH cannot connect.

## Change the resource limits

Set environment variables before `run-job.sh` to change the Firecracker resources and timeout:

```bash
cd ~/firecracker-ai-sandbox
sudo FC_VCPUS=2 FC_MEM_MIB=1024 FC_JOB_TIMEOUT=30 \
  ./sandbox/run-job.sh ./sandbox/examples/hello-arm.sh
```

The job receives two virtual CPUs, 1,024 MiB of memory, and a 30-second timeout. These settings apply only to this execution.

The memory allocation includes the guest operating system, so the program has less memory available. The virtual CPU count controls guest CPUs; it doesn't set a host CPU quota. The execution timeout starts after boot and file transfer, so total elapsed time is longer.

## What you've accomplished and what's next

You've executed a program on native Arm inside a job-specific microVM and inspected the host-side audit artifacts. Next, you'll prove that filesystem changes don't persist and that the host enforces the execution timeout.
