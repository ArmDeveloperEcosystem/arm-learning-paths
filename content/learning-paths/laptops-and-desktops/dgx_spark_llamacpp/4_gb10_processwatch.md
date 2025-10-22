---
title: Analyzing Instruction Mix on Grace CPU using Process Watch
weight: 5
layout: "learningpathall"
---

## Analyzing Instruction Mix on the Grace CPU Using Process Watch

In this session, you will explore how the **Grace CPU** executes Armv9 vector and matrix instructions during quantized LLM inference.
By using **Process Watch**, you will observe how Neon SIMD instructions dominate execution on the Grace CPU and learn why SVE and SVE2 remain inactive under the current kernel configuration.
This exercise demonstrates how Armv9 vector execution behaves in real AI workloads and how hardware capabilities evolve—from traditional SIMD pipelines to scalable vector and matrix computation.

### Step 1: Observe SIMD Execution with Process Watch

Start by running a quantized model on the Grace CPU:

In this step, you will install and configure **Process Watch**, an instruction-level profiling tool that shows live CPU instruction usage across threads. It supports real-time visualization of **NEON**, **SVE**, **FP**, and other vector and scalar instructions executed on Armv9 processors.

```bash
sudo apt update
sudo apt install -y git cmake build-essential libncurses-dev libtinfo-dev
```

Use the following commands to download the source code, compile it, and install the binary into the processwatch directory.

```bash
# Clone and build Process Watch
cd ~
git clone --recursive https://github.com/intel/processwatch.git
cd processwatch
./build.sh
sudo ln -s ~/processwatch/processwatch /usr/local/bin/processwatch
```

To collect instruction-level metrics, ***Process Watch*** requires access to kernel performance counters and eBPF features.
Although it can run as a non-root user, full functionality requires elevated privileges. For simplicity and completeness, run it with administrative rights.
For safety and simplicity, it is recommended to run it with administrative rights.

Run the following commands to enable the required permissions:
```bash
sudo setcap CAP_PERFMON,CAP_BPF=+ep ./processwatch
sudo sysctl -w kernel.perf_event_paranoid=-1
sudo sysctl kernel.unprivileged_bpf_disabled=0
```

These commands:
- Grant Process Watch the ability to use performance monitoring (perf) and eBPF tracing.
- Lower kernel restrictions on accessing performance counters.
- Allow unprivileged users to attach performance monitors.

Verify the installation:

```bash
./processwatch --help
```

You should see a usage summary similar to:
```
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

In this step, you will run a quantized TinyLlama model on the Grace CPU to generate live instruction activity.

Use the same CPU-only llama.cpp build created in the previous session:

```bash
cd ~/llama.cpp/build-cpu/bin
./llama-cli \
	-m ~/models/TinyLlama-1.1B/tinyllama-1.1b-chat-v1.0.Q8_0.gguf \
	-ngl 0 \
	-t 20 \
	-p "Explain the benefits of vector processing in modern Arm CPUs."
```

Keep this terminal running while the model generates text output.
You will now attach Process Watch to this active process.

Once the llama.cpp process is running on the Grace CPU, attach Process Watch to observe its live instruction activity.
If only one ***llama-cli process*** is running, you can directly launch Process Watch without manually checking its PID:

```bash
sudo processwatch --pid $(pgrep llama-cli)
```

This automatically attaches to the most active user-space process (typically llama-cli if it is the only inference task running).

If multiple instances of llama-cli or other workloads are active, first list all running processes:

```bash
pgrep llama-cli
```

Then attach Process Watch to monitor the instruction mix of this process:

```bash
sudo processwatch --pid <<LLAMA-CLI ID>>
```
{{% notice Note %}}
processwatch --list does not display all system processes.
It is intended for internal use and may not list user-level tasks like llama-cli.
Use pgrep, ps -ef | grep llama, or htop to identify process IDs before attaching.
{{% /notice %}}

The tool will display a live instruction breakdown similar to the following:
```
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

Interpretation:
- NEON (≈ 7–15 %) : Active SIMD integer and floating-point operations.
- FPARMv8         : Scalar FP operations (e.g., activation, normalization).
- SVE/SVE2 = 0    : The kernel is restricted to 128-bit vectors and does not issue SVE instructions.

This confirms that the Grace CPU performs quantized inference primarily using Neon SIMD pipelines.


### Step 2: Why SVE and SVE2 Remain Inactive

Although the Grace CPU supports SVE and SVE2, the current NVIDIA Grace kernel limits the default vector length to 16 bytes (128-bit).
This restriction ensures binary compatibility with existing Neon-optimized workloads.

You can confirm this setting by:
```bash
cat /proc/sys/abi/sve_default_vector_length
```

Output:
```
16
```

Even if you try to increase the length:

```bash
echo 256 | sudo tee /proc/sys/abi/sve_default_vector_length
cat /proc/sys/abi/sve_default_vector_length
```

It will revert to 16.
This behavior is expected — SVE is enabled but fixed at 128 bits, so Neon remains the active execution path.

{{% notice Note %}}
The current kernel image restricts the SVE vector length to 128 bits to maintain compatibility with existing software stacks.
Future kernel updates are expected to introduce configurable SVE vector lengths (for example, 256-bit or 512-bit).
This Learning Path will be revised accordingly once those capabilities become available on the Grace platform.
{{% /notice %}}

In this session, you used ***Process Watch*** to observe instruction activity on the Grace CPU and interpret how Armv9 vector instructions are utilized during quantized LLM inference.
You confirmed that Neon SIMD remains the primary execution path under the current kernel configuration, while SVE and SVE2 are enabled but restricted to 128-bit vector length for compatibility reasons.

This experiment highlights how architectural features evolve over time — the Grace CPU already implements advanced Armv9 capabilities, and future kernel releases will unlock their full potential.

By mastering these observation tools and understanding the instruction mix, you are now better equipped to:
- Profile Arm-based systems at the architectural level,
- Interpret real-time performance data meaningfully, and
- Prepare your applications for future Armv9 enhancements.

