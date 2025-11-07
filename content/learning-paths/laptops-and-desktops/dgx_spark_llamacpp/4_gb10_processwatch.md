---
title: Analyze CPU instruction mix using Process Watch
weight: 6
layout: "learningpathall"
---

## How can I analyze the instruction mix on the CPU using Process Watch?

In this section, you'll explore how the Grace CPU executes Armv9 vector instructions during quantized LLM inference.

Process Watch helps you observe Neon SIMD instruction execution on the Grace CPU and understand why SVE and SVE2 remain inactive under the current kernel configuration. This demonstrates how Armv9 vector execution works in AI workloads and shows the evolution from traditional SIMD pipelines to scalable vector computation.

## Install and configure Process Watch

First, install the required packages:

```bash
sudo apt update
sudo apt install -y git cmake build-essential libncurses-dev libtinfo-dev
```

Now clone and build Process Watch:

```bash
cd ~
git clone --recursive https://github.com/intel/processwatch.git
cd processwatch
./build.sh
sudo ln -s ~/processwatch/processwatch /usr/local/bin/processwatch
```

Process Watch requires elevated privileges to access kernel performance counters and eBPF features.

Run the following commands to enable the required permissions:

```bash
sudo setcap CAP_PERFMON,CAP_BPF=+ep ./processwatch
sudo sysctl -w kernel.perf_event_paranoid=-1
sudo sysctl kernel.unprivileged_bpf_disabled=0
```

These commands grant Process Watch access to performance monitoring and eBPF tracing capabilities.

Verify the installation:

```bash
./processwatch --help
```

You should see a usage summary similar to:

```output
usage: processwatch [options]
options:
  -h          Displays this help message.
  -v          Displays the version.
  -i <int>    Prints results every <int> seconds.
  -n <num>    Prints results for <num> intervals.
  -c          Prints all results in CSV format to stdout.
  -p <pid>    Only profiles <pid>.
  -m          Displays instruction mnemonics, instead of categories.
  -s <samp>   Profiles instructions with a sampling period of <samp>. Defaults to 100000 instructions (1 in 100000 instructions).
  -f <filter> Can be used multiple times. Defines filters for columns. Defaults to 'FPARMv8', 'NEON', 'SVE' and 'SVE2'.
  -a          Displays a column for each category, mnemonic, or extension. This is a lot of output!
  -l          Prints a list of all available categories, mnemonics, or extensions.
  -d          Prints only debug information.
```

You can run a quantized TinyLlama model on the Grace CPU to generate the instruction activity.

Use the same CPU-only llama.cpp build created in the previous section:

```bash
cd ~/llama.cpp/build-cpu/bin
./llama-cli \
	-m ~/models/TinyLlama-1.1B/tinyllama-1.1b-chat-v1.0.Q8_0.gguf \
	-ngl 0 \
	-t 20 \
	-p "Explain the benefits of vector processing in modern Arm CPUs."
```

Keep this terminal running while the model generates text output. You can now attach Process Watch to this active process. Once the llama.cpp process is running on the Grace CPU, attach Process Watch to observe its live instruction activity.

If only one `llama-cli` process is running, you can directly launch Process Watch without manually checking its PID:

```bash
sudo processwatch --pid $(pgrep llama-cli)
```

If multiple processes are running, first identify the correct process ID:

```bash
pgrep llama-cli
```

Then attach Process Watch to monitor the instruction mix of this process:

```bash
sudo processwatch --pid <LLAMA-CLI-PID>
```

Replace `<LLAMA-CLI-PID>` with the actual process ID from the previous command.

{{% notice Note %}}
`processwatch --list` does not display all system processes.
It is intended for internal use and may not list user-level tasks like llama-cli.
Use `pgrep` or `ps -ef | grep llama` or `htop` to identify process IDs before attaching.
{{% /notice %}}

Process Watch displays a live instruction breakdown similar to the following:

```output
PID      NAME             FPARMv8  NEON     SVE      SVE2     %TOTAL   TOTAL   
ALL      ALL              5.07     15.23    0.00     0.00     100.00   29272   
72930    llama-cli        5.07     15.23    0.00     0.00     100.00   29272   

PID      NAME             FPARMv8  NEON     SVE      SVE2     %TOTAL   TOTAL   
ALL      ALL              2.57     9.95     0.00     0.00     100.00   69765   
72930    llama-cli        2.57     9.95     0.00     0.00     100.00   69765   

PID      NAME             FPARMv8  NEON     SVE      SVE2     %TOTAL   TOTAL   
ALL      ALL              1.90     6.61     0.00     0.00     100.00   44249   
72930    llama-cli        1.90     6.61     0.00     0.00     100.00   44249   

PID      NAME             FPARMv8  NEON     SVE      SVE2     %TOTAL   TOTAL   
ALL      ALL              2.60     10.16    0.00     0.00     100.00   71049   
72930    llama-cli        2.60     10.16    0.00     0.00     100.00   71049   

PID      NAME             FPARMv8  NEON     SVE      SVE2     %TOTAL   TOTAL   
ALL      ALL              2.12     7.56     0.00     0.00     100.00   68553   
72930    llama-cli        2.12     7.56     0.00     0.00     100.00   68553   

PID      NAME             FPARMv8  NEON     SVE      SVE2     %TOTAL   TOTAL   
ALL      ALL              2.52     9.40     0.00     0.00     100.00   65339   
72930    llama-cli        2.52     9.40     0.00     0.00     100.00   65339   

PID      NAME             FPARMv8  NEON     SVE      SVE2     %TOTAL   TOTAL   
ALL      ALL              2.34     7.76     0.00     0.00     100.00   42015   
72930    llama-cli        2.34     7.76     0.00     0.00     100.00   42015   

PID      NAME             FPARMv8  NEON     SVE      SVE2     %TOTAL   TOTAL   
ALL      ALL              2.66     9.77     0.00     0.00     100.00   74616   
72930    llama-cli        2.66     9.77     0.00     0.00     100.00   74616   

PID      NAME             FPARMv8  NEON     SVE      SVE2     %TOTAL   TOTAL   
ALL      ALL              2.15     7.06     0.00     0.00     100.00   58496   
72930    llama-cli        2.15     7.06     0.00     0.00     100.00   58496   

PID      NAME             FPARMv8  NEON     SVE      SVE2     %TOTAL   TOTAL   
ALL      ALL              2.61     9.34     0.00     0.00     100.00   73365   
72930    llama-cli        2.61     9.34     0.00     0.00     100.00   73365   

PID      NAME             FPARMv8  NEON     SVE      SVE2     %TOTAL   TOTAL   
ALL      ALL              2.52     8.37     0.00     0.00     100.00   26566   
72930    llama-cli        2.52     8.37     0.00     0.00     100.00   26566   
```

Here is an interpretation of the values:
- NEON: 7–15% for SIMD integer and floating-point operations
- FPARMv8: 2-5% for scalar FP operations such as activation and normalization
- SVE/SVE2: 0%, the kernel does not issue SVE instructions

This confirms that the Grace CPU performs quantized inference primarily using NEON.

## Why are SVE and SVE2 inactive?

Although the Grace CPU supports SVE and SVE2, the vector length is 16 bytes (128-bit).

Verify the current setting:

```bash
cat /proc/sys/abi/sve_default_vector_length
```

The output is similar to:

```output
16
```

Even if you try to increase the length it cannot be changed. 

```bash
echo 256 | sudo tee /proc/sys/abi/sve_default_vector_length
```

This behavior is expected because SVE is available but fixed at 128 bits.

{{% notice Note %}}
Future kernel updates might introduce SVE2 instructions.
{{% /notice %}}

## What you've accomplished and what's next

You have completed the Learning Path for analyzing large language model inference on the DGX Spark platform with Arm-based Grace CPUs and Blackwell GPUs.

Throughout this Learning Path, you have learned how to:

- Set up your DGX Spark system with the required Arm software stack and CUDA 13 environment
- Build and validate both GPU-accelerated and CPU-only versions of llama.cpp for quantized LLM inference
- Download and run quantized TinyLlama models for efficient testing and benchmarking
- Monitor GPU utilization and performance using tools like nvtop
- Analyze CPU instruction mix with Process Watch to understand how Armv9 vector instructions are used during inference
- Interpret the impact of NEON, SVE, and SVE2 on AI workloads, and recognize current kernel limitations for vector execution

By completing these steps, you are now equipped to:

- Profile and optimize LLM workloads on Arm-based systems
- Identify performance bottlenecks and opportunities for acceleration on both CPU and GPU
- Prepare for future enhancements in Armv9 vector processing and software support
- Confidently deploy and monitor AI inference on modern Arm server platforms
For additional learning, see the resources in the Further Reading section. You can continue experimenting with different models and monitoring tools as new kernel updates become available.

