---
title: Capture a performance profile with Streamline CLI tools
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Capture a performance profile with Streamline CLI tools

The Streamline CLI tools are native command-line tools that are designed to run
directly on an Arm server running Linux.

Profiling with these tools is a three-step process:

* Use `sl-record` to capture the raw sampled data for the profile.
* Use `sl-analyze` to pre-process the raw sampled data to create a set of
  function-attributed counters and metrics.
* Use `sl-format.py` to pretty-print the function-attributed metrics in a more
  human-readable form.

![Streamline CLI tools workflow](images/streamline-cli-workflow.svg)

### 3.1 System compatibility check

Before you begin, you can use the the Arm Sysreport utility to determine
whether your system configuration supports hardware-assisted profiling.

Follow the instructions in this [Learning Path tutorial][1] to discover how to
download and run this utility.

[1]: https://learn.arm.com/learning-paths/servers-and-cloud-computing/sysreport/

The `perf counters` entry in the generated report will indicate how many CPU
counters are available. The `perf sampling` entry will indicate if SPE is
available.

You will achieve the best profiles in systems with at least 6 available CPU
counters and SPE.

The Streamline CLI tools can be used in systems with no CPU counters, but will
only be able to return a basic hot-spot profile based on time-based sampling.
No top-down methodology metrics will be available.

The Streamline CLI tools can give top-down metrics in systems with as few as 3
available CPU counters. The effective sample rate for each metrics will be
lower, because we will need to time-slice the counters to capture all of the
requested metrics, so you will need to run your application for longer to get
the same number of samples for each metric. Metrics that require more input
counters than are available cannot be captured.

The Streamline CLI tools can be used without SPE. Load operation data source
metrics will not be available, and branch mispredict metrics may be less
accurate.

### Installing the tools

The Streamline CLI tools are available as a standalone download to enable
easier integration in to server workflows.

```sh
wget https://artifacts.tools.arm.com/arm-performance-studio/2024.2/Arm_Streamline_CLI_Tools_9.2.0_linux_arm64.tgz 

tar -xzf Arm_Streamline_CLI_Tools_9.2.0_linux_arm64.tgz 
```

The `sl-format.py` Python script requires Python 3.8 or later, and depends on
several third-party modules. We recommend creating a Python virtual environment
containing these modules to run the tools. For example:

```sh
# From Bash
python3 -m venv sl-venv
source ./sl-venv/bin/activate

# From inside the virtual environment
python3 -m pip install -r ./<install>/bin/requirements.txt
```

**Note:** The instructions below assume you have added the `<install>/bin/`
directory to your `PATH` environment variable, and that you run all Python
commands from inside the virtual environment.

### Capturing a profile

Use `sl-record` to capture a raw profile of your application and save the data
to a directory on the filesystem.

```sh
sl-record -C workflow_topdown_basic -o <output.apc> -A <your app command-line>
```

This command uses the following options:

* The `-C` option provides a comma-separated list of counters and metrics to
  capture. The workflow-prefixed options in the counter list select a
  predefined group of counters and metrics, making it easier to select
  everything you need for a standard configuration. Using
  `workflow_topdown_basic` is a good baseline option to start with.

  To list all of the available counters and metrics for the current machine,
  use the command `sl-record --print counters`.
* The `-o` option provides the output directory for the capture data. The
  directory must not already exist because it is created by the tool when
  profiling starts.
* The `-A` option provides the command-line for the user application. This
  option must be the last option provided to `sl-record` because all subsequent
  arguments are passed to the user application.

Optionally, to enable SPE add the `-X workflow_spe` option. Enabling SPE
significantly increases the amount of data captured and the `sl-analyze`
processing time.

Captures are highly customizable, with many different options that allow you to
choose how to profile your application. Use the `--help` option to see the
full list of options for customizing your captures.

#### Minimizing profiling application impact

The `sl-record` application requires some portion of the available processor
time to capture the data and prepare it for storage. When profiling a system
with a high number of CPU cores, Arm recommends that you leave a small number
of cores free so that the profiler can run in parallel without impacting the
application. You can achieve this in two different ways:

* Running an application with fewer threads than the number of cores available.
* Running the application under `taskset` to limit the number of cores that the
  application can use. You must only `taskset` the application, not
  `sl-record`, for example:

```sh
sl-record -C … -o … -A taskset <core_mask> <your app command-line>
```

**Note:** The number of samples made is independent of the number of counters
and metrics that you enable. Enabling more counters reduces the effective
sample rate per counter, and does not significantly increase the performance
impact that capturing has on the running application.

### Analyzing a profile

Use `sl-analyze` to process the raw profile of your application and save the
analysis output as several CSV files on the filesystem.

```sh
sl-analyze -o <output_dir> <input_dir.apc>
```

This command uses the following arguments:

* The `-o` option provides the output directory for the generated CSV files.
* The positional argument is the raw profile directory created by `sl-record`.

Several CSV files are generated by this analysis:

* Files that start `functions-`: A flat list of functions, sorted by cost,
  showing per-function metrics.
* Files that start `callpaths-`: A hierarchical list of function call paths in
  the application, showing per-function metrics for each function per call path
  location.
* Files that end `-bt.csv`: Results from the analysis of the software-sampled
  performance counter data, which can include back-traces for each sample.
* Files that end `-spe.csv`:  Results from the analysis of the hardware-sampled
  Statistical Profiling Extension (SPE) data. SPE data does not include call
  back-trace information.

### Formatting a function profile

The function profile CSV files generated by `sl-analyze` contain all the
enabled events and metrics, for all functions that were sampled in the profile.

Use `sl-format.py` to generate a simpler pretty-printed XLSX spreadsheet that
is suitable for human consumption.

```sh
python3 sl-format.py -o <output.xlsx> <input.csv>
```

This command uses the following arguments:

* The `-o` option provides the output file path to save the XLSX file to.
* The positional argument is the `functions-*.csv` file created by `sl-record`.

This formatter has several basic capabilities:

* Selecting and ordering the desired metrics columns.
* Filtering out low-value function rows by absolute or relative significance.
* Formatting metrics columns using short names for compact presentation.
* Formatting metrics cell colors using threshold rules to spotlight bad values.
* Emitting the data as an XLSX data table, allowing interactive column sorting
  and row filtering when opened in OpenOffice or Microsoft Excel.

[Section 4](#custom-formats) of this guide explains how you create and specify
custom format definitions that are used to change the pretty-printed data
visualization.

### Using a formatted function profile

There is no right way to profile and optimize, but the top-down data
presentation gives you a systematic way to find optimization opportunities.

Here is our optimization checklist:

1. Check the compiler did a good job:
    * Disassemble your most significant functions.
    * Verify that the generated code looks efficient.

1. Check the functions that are the most frontend bound:
    * If you see high instruction cache miss rate, apply profile-guided
  optimization to reduce the code size of less important functions. This frees
  up more instruction cache space for the important hot-functions.
    * If you see high instruction TLB misses, apply code layout optimization, using tools such as [Bolt][2]. This improves locality of code accesses, reducing the number of TLB misses.

    [2]: https://learn.arm.com/learning-paths/servers-and-cloud-computing/bolt/overview/

1. Check the functions have the highest bad speculation rate:

    * If you see high branch mispredict rates, use a more predictable branching pattern, or change the software to avoid branches by using conditional selects.

1. Check the functions that are the most backend bound:

    * If you see high data cache misses, reduce data size, reduce data copies and moves, and improve access locality.
    * If you see high pipeline congestion on a specific issue queue, alter your software to move load a different queue. For example, converting run-time computation to a lookup table if your program is arithmetic limited.

1. Check the most retiring bound functions:

    * Apply SIMD vectorization to process more work per clock.
    * Look for higher-level algorithmic improvements.

## Data caveats

The Streamline CLI tools provide you with function-attributed performance
metrics. To implement this using the Arm PMU, we take an interrupt at the start
of the sample window to zero the counters, and at the end of the sample
window to capture the counters.

This pair of context-switches has an overhead on the running software. The
absolute value of some metrics can differ to the value that would be reported
if our sample was non-invasive. However, functions will rank correctly, and
trends are directionally accurate when showing the impact of an optimization.

Our methodology has three known side-effects that impact the metrics:

* At the start of the sample window, it takes some cycles to refill the
  pipeline when returning from the context switch. This means we retire fewer
  instructions in the sample window than normal steady-state execution.
* At the end of the sample window, issued instructions that are queued in the
  issue queue are cancelled to reduce the context switch latency. This means we
  see a much higher number of instructions that are speculatively issued but
  not retired than normal steady-state execution.
* The kernel code run at the start of the sample window places higher pressure
  on caches and other cache-like structures. However, for most software the
  impact of this is minor.

### Impacted metrics

We are aware of the following impact on the default top-down metrics shown in
the formatted report:

| Top-down metric | Impact                      |
| --------------- | --------------------------- |
| Retiring        | Reports lower than normal   |
| Frontend bound  | Reports higher than normal  |
| Bad speculation | Reports higher than normal  |
| Backend bound   | Reports lower than normal   |

