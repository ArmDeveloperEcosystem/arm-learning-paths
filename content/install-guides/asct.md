---
title: Arm System Characterization Tool

draft: true

additional_search_terms:
- ASCT
- Neoverse
- benchmarking
- performance analysis
- memory latency
- memory bandwidth
- storage performance

minutes_to_complete: 15

test_maintenance: false

# No official documentation 
official_docs: https://learn.arm.com/install-guides/

author: Jason Andrews

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

The Arm System Characterization Tool (ASCT) is a command-line utility for running low-level benchmarks, diagnostic scripts, and system tests to analyze and debug performance on Arm-based platforms. ASCT provides a standardized environment for evaluating key hardware characteristics and is especially suited for platform bring-up, system tuning, and architectural comparison tasks.

ASCT provides capabilities for:
- Memory latency and bandwidth benchmarking across NUMA nodes
- Storage I/O performance testing
- System hardware and software configuration reporting
- Core-to-core latency measurements
- Cache hierarchy mapping through sweep operations

ASCT is available for Linux on Arm (AArch64) systems and requires Python 3.10 or later.

## What should I do before installing ASCT?

ASCT requires a Linux system running on Arm hardware. Confirm you are using an Arm computer with 64-bit Linux by running:

```bash
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

### Install prerequisites

Before installing ASCT, ensure you have the required system packages:

```bash
sudo apt update
sudo apt install python3 python3-pip python-is-python3 gcc make numactl fio linux-tools-generic linux-tools-$(uname -r) -y
```

These packages are required for:
- `python3` - Python 3.10 or later for running ASCT
- `gcc` and `make` - For compiling benchmark components
- `numactl` - For NUMA-aware memory benchmarks
- `fio` - Version 3.36 or later for storage benchmarks
- `linux-tools-generic` and `linux-tools-$(uname -r)` - Linux Perf for performance analysis

For more information about installing Perf on different Linux distributions, see the [Perf install guide](/install-guides/perf/).

## How do I download and install ASCT?

ASCT is distributed as a Python package and requires Python 3.10 or later.

### Download ASCT

Download the latest ASCT release from the [artifacts.tools.arm.com](https://artifacts.tools.arm.com/asct/dist/) page.

For example, to download version 0.4.1:

```bash
wget https://artifacts.tools.arm.com/asct/dist/0.4.1/asct-0.4.1+a304bc8.tar.gz
```

### How do I install ASCT using uv?

The recommended installation method uses [uv](https://github.com/astral-sh/uv), a fast Python package installer. First, install `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install ASCT system-wide using:

```bash
UV_TOOL_BIN_DIR=/usr/local/bin sudo -E $(which uv) tool install asct-0.4.1+a304bc8.tar.gz
```

This installs ASCT to `/usr/local/bin` making it available system-wide. Installing to `/usr/local/bin` instead of the default `~/.local/bin` allows you to run ASCT with `sudo`, which is required for some benchmarks to access system resources and configure huge pages.

### How do I verify that ASCT is installed?

After installing ASCT, verify the installation by checking the version:

```bash
asct version
```

The output is similar to:

```output
ASCT 0.4.1+a304bc8
```

You can also display the help information:

```bash
asct --help
```

The output displays available commands and benchmarks.

## How do I use ASCT?

ASCT provides several commands for benchmarking and system analysis, including `run`, `system-info`, `list`, `diff`, and `sysreg`. 

Some benchmarks require `sudo` or root privileges to configure huge pages and access certain system information. You can run ASCT without `sudo`, but some benchmarks might be unavailable or limited in functionality.

### Get system information

To generate a system information report:

```bash
sudo asct system-info
```

To save the system information in JSON format:

```bash
sudo asct system-info --format json --output-dir my_output
```

### List available benchmarks

To see all available benchmarks and their associated keywords:

```bash
asct list
```

### Run benchmarks

To run the default set of benchmarks:

```bash
sudo asct run
```

To run all available benchmarks (including optional ones):

```bash
sudo asct run all
```

To run specific benchmarks by name:

```bash
sudo asct run latency-sweep idle-latency
```

Each benchmark has associated keywords that describe its characteristics. You can use these keywords to run groups of related benchmarks without specifying each one individually.

To run all benchmarks tagged with the `memory` keyword:

```bash
sudo asct run memory
```

To run all benchmarks tagged with both `latency` and `bandwidth` keywords:

```bash
sudo asct run latency bandwidth
```

Common keywords include `memory`, `storage`, `latency`, `bandwidth`, `sweep`, and `long-runtime`. Use `asct list` to see which keywords are associated with each benchmark.

To exclude benchmarks by keyword, prepend the keyword with the `^` character:

```bash
sudo asct run all ^bandwidth
```

This runs all benchmarks except those tagged with the `bandwidth` keyword.

To save benchmark results in CSV format:

```bash
sudo asct run --format csv --output-dir results
```

By default, ASCT saves output in a directory named `data.<YYYYMMDD_HHMMSS_microseconds>` in the current working directory. Use `--output-dir` to specify a custom location.

### Compare results

To compare results from multiple ASCT runs:

```bash
asct diff --output-dir results1 --output-dir results2
```

## What are the available benchmarks?

ASCT includes several categories of benchmarks:

Memory benchmarks:
- `latency-sweep` (`ls`) - Measures memory latency across data sizes from 128 bytes to 1 GiB, revealing cache hierarchy transitions. Uses 1 GiB huge pages to reduce TLB impact. Calculates optimal data sizes for L1, L2, LLC, and DRAM.
- `idle-latency` (`il`) - Reports a matrix of idle memory latency across NUMA nodes
- `peak-bandwidth` (`pb`) - Measures peak memory bandwidth
- `cross-numa-bandwidth` (`cnb`) - Measures cross-NUMA node memory bandwidth
- `bandwidth-sweep` (`bs`) - Sweeps bandwidth by data size to map cache hierarchy
- `loaded-latency` (`ll`) - Measures memory latency under load conditions (not run by default)
- `c2c-latency` (`ccl`) - Measures core-to-core communication latency

Storage benchmarks:
- `storage-request-size-sweep` (`srss`) - Sweeps I/O request sizes to measure performance
- `storage-io-depth-sweep` (`sids`) - Sweeps I/O queue depths to find optimal settings
- `storage-process-count-sweep` (`spcs`) - Sweeps process counts to measure scaling
- `storage-access-pattern-sweep` (`saps`) - Evaluates different workload profiles including sequential and random access (not run by default)

You can filter benchmarks using keywords like `latency`, `bandwidth`, `memory`, `storage`, `sweep`, or `long-runtime`.

## What output formats are supported?

ASCT supports three output formats:
- `stdout` - Human-readable console output (default)
- `csv` - Individual CSV files for each benchmark (for example, `benchmark-name.csv`)
- `json` - Single combined JSON file (`report.json`) containing all results

Specify the format using the `--format` or `-f` option:

```bash
sudo asct run --format json
```

## What other options are available?

ASCT provides several additional options:

- `--log-level` or `-L` - Set logging verbosity (debug, info, warning, error, critical)
- `--log-file` - Save logs to a specific file
- `--force` - Overwrite existing output directory
- `--quiet` or `-q` - Disable all output to stdout and stderr
- `--no-progress-bar` - Use single-line updates instead of animated progress bar
- `--dry-run` - Show which benchmarks would run without executing them
- `--no-cache` - Disable cached benchmark data
- `--clear-cache` - Clear cached benchmark data

## How do I uninstall ASCT?

If you installed ASCT using `uv`, remove it with:

```bash
sudo -E $(which uv) tool uninstall asct
```

## Where can I find more information?

Use the built-in help command to get detailed information about any ASCT command:

```bash
asct help <command>
```

For example:

```bash
asct help run
```
