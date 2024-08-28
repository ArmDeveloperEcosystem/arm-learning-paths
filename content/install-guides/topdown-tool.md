---
### Title the install tools article with the name of the tool to be installed
### Include vendor name where appropriate
title: Telemetry Solution (Topdown Methodology)

### Optional additional search terms (one per line) to assist in finding the article
additional_search_terms:
- perf
- profiling
- profiler
- Linux
- WSL

### Estimated completion time in minutes (please use integer multiple of 5)
minutes_to_complete: 10

author_primary: Jason Andrews

### Link to official documentation
official_docs: https://gitlab.arm.com/telemetry-solution/telemetry-solution

### PAGE SETUP
weight: 1                       # Defines page ordering. Must be 1 for first (or only) page.
tool_install: true              # Set to true to be listed in main selection page, else false
multi_install: false            # Set to true if first page of multi-page article, else false
multitool_install_part: false   # Set to true if a sub-page of a multi-page article, else false
layout: installtoolsall         # DO NOT MODIFY. Always true for tool install articles
---

The Arm Telemetry Solution provides tools and data for performance analysis.

The Arm Topdown Methodology specifies a set of metrics and steps to measure them using the Telemetry Solution.

The Telemetry Solution requires Linux Perf to collect metrics.

The Telemetry Solution also includes data for defining PMU events, a test suite to stress CPU resources, and a tool to parse Statistical Profiling Extension (SPE) data for analysis.

## Before you begin

Follow the instructions below to install the Telemetry Solution on an Arm Linux system.

1. Confirm you are using an Arm machine by running:

```console
uname -m
```

The output should be:

```output
aarch64
```

If you see a different result, you are not using an Arm computer running 64-bit Linux.

2. Install Perf

Install Perf using the [Perf for Linux on Arm install guide](/install-guides/perf).

3. Install Python 3 and pip

Python 3.7 or later and pip are required.

Install these on your Linux distribution.

For Debian based distributions (including Ubuntu) run:

```bash { target="ubuntu:latest" }
sudo apt update
sudo apt install python3-pip python-is-python3 -y
```

## Install the Telemetry Solution

1. Clone the repository:

```bash { target="ubuntu:latest" }
git clone https://git.gitlab.arm.com/telemetry-solution/telemetry-solution.git
cd telemetry-solution/tools/topdown_tool
```

2. Install the `topdown-tool` executable:

Install `topdown-tool` in `/usr/local/bin` using:

```console
pip3 install -e .
```

{{% notice Note %}}
If you are getting errors on the environment being externally managed, try creating a virtual environment.
```
sudo apt install python3-venv
python3 -m venv topdown-venv
source topdown-venv/bin/activate
pip3 install -e .
```
{{% /notice %}}

3. Confirm you can run `top-down` using the `version` command:

```bash { target="ubuntu:latest" }
topdown-tool --help
```

The output will be similar to:

```output
usage: topdown-tool [-h] [--all-cpus] [--pid PIDS] [--perf-path PERF_PATH] [--perf-args PERF_ARGS] [--cpu CPU]
                    [--list-cpus] [--list-groups] [--list-metrics] [-c {none,metric,group}]
                    [--max-events MAX_EVENTS] [-m METRIC_GROUPS] [-n NODE] [-s STAGES] [-i INTERVAL]
                    [--use-event-names] [-d] [--show-sample-events] [--perf-output PERF_OUTPUT] [--csv CSV] [-v]
                    [--debug]
                    ...

positional arguments:
  command               command to analyse. Subsequent arguments are passed as program arguments. e.g. "sleep
                        10"

options:
  -h, --help            show this help message and exit
  --all-cpus, -a        System-wide collection for all CPUs.
  --pid PIDS, -p PIDS   comma separated list of process IDs to monitor.
  --perf-path PERF_PATH
                        path to perf executable
  --perf-args PERF_ARGS
                        additional command line arguments to pass to Perf
  --cpu CPU             CPU name to use to look up event data (auto-detect by default)
  -i INTERVAL, -I INTERVAL, --interval INTERVAL
                        Collect/output data every <interval> milliseconds

query options:
  --list-cpus           list available CPUs and exit
  --list-groups         list available metric groups and exit
  --list-metrics        list available metrics and exit

collection options:
  -c {none,metric,group}, --collect-by {none,metric,group}
                        when multiplexing, collect events grouped by "none", "metric" (default), or "group".
                        This can avoid comparing data collected during different time periods.
  --max-events MAX_EVENTS
                        Maximum simultaneous events. If more events are required, <command> will be run multiple
                        times.
  -m METRIC_GROUPS, --metric-group METRIC_GROUPS
                        comma separated list of metric groups to collect. See --list-groups for available groups
  -n NODE, --node NODE  name of topdown node as well as its descendants (e.g. "frontend_bound"). See --list-
                        metrics for available nodes
  -s STAGES, --stages STAGES
                        control which stages to display, separated by a comma. e.g. "topdown,uarch". "all" may
                        also be specified, or "combined" to display all, but without separated the output in to
                        stages.
  --use-event-names     use event names rather than event codes (e.g. "r01") when collecting data from perf.
                        This can be useful for debugging.

output options:
  -d, --descriptions    show group/metric descriptions
  --show-sample-events  show sample events for metrics
  --perf-output PERF_OUTPUT
                        output file for perf event data
  --csv CSV             output file for metric CSV data
  -v, --verbose         enable verbose output
  --debug               enable debug output
```

4. Test `topdown-tool`

{{% notice Note %}}
You may need to enable access to the counters. More information about the options is in the [Linux Perf install guide](/install-guides/perf/).

```console
sudo sh -c "echo -1 > /proc/sys/kernel/perf_event_paranoid"
sudo sh -c "echo 0 > /proc/sys/kernel/kptr_restrict"
```
{{% /notice %}}

Confirm `topdown-tool` is able to collect events:

```console
topdown-tool -m Cycle_Accounting -a sleep 5
```

The output is similar to:

```output
Stage 1 (Topdown metrics)
=========================
[Cycle Accounting]
Frontend Stalled Cycles 57.67% cycles
Backend Stalled Cycles. 21.06% cycles
```

{{% notice Note %}}
If you encounter the error `Could not detect CPU. Specify via --cpu`, you can check what CPUs are available, and pass it to the command.

```console
topdown-tool --list-cpus
topdown-tool --cpu <cpu-name> -m Cycle_Accounting -a sleep 5

```
{{% /notice %}}

Your output may be different, but if values are printed you are ready to apply the Arm Top Down methodology.
