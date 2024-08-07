---
title: Run Process Watch
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Root user
Although you can run Process Watch as a non-root user, it requires modifications made by root, which makes your system less secure. It is recommended that Process Watch is instead run by root.

To enable non-root users to run Process Watch, you need to run the following as root:
```bash
sudo setcap CAP_PERFMON,CAP_BPF=+ep ./processwatch
sudo sysctl -w kernel.perf_event_paranoid=-1
sudo sysctl kernel.unprivileged_bpf_disabled=0
```

## Run Process Watch
The Process Watch tool accepts a number of command-line arguments. You can view these by running:
```bash
sudo ./processwatch -h
```
The output should look like:
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
  -s <samp>   Profiles instructions with a sampling period of <samp>.
  -f <filter> Can be used multiple times. Defines filters for columns. Defaults to 'FPARMv8', 'NEON', 'SVE' and 'SVE2'.
  -l          Prints all available categories, or mnemonics if -m is specified.
  -d          Prints only debug information.
  ```


By default, Process Watch:
 * Prints results every two seconds.
 * Prints results until the tool is killed (via Ctrl+c).
 * Prints all results in a table format on `stdout`.
 * Profiles all running processes.
 * Displays counts for the default filters, which are 'FPARMv8', 'NEON', 'SVE', and 'SVE2'.
 * Sets the sample period to every 10000 events.

## Default Process Watch output
You can run Process Watch with no arguments:

```bash
sudo ./processwatch
```

The output should look like:
```output
PID      NAME             FPARMv8  NEON     SVE      SVE2     %TOTAL   TOTAL
ALL      ALL              0.00     0.29     0.00     0.00     100.00   346
17400    processwatch     0.00     0.36     0.00     0.00     80.64    279
254      systemd-journal  0.00     0.00     0.00     0.00     13.01    45
542      irqbalance       0.00     0.00     0.00     0.00     2.60     09
544      rs:main Q:Reg    0.00     0.00     0.00     0.00     2.02     07
560      snapd            0.00     0.00     0.00     0.00     1.16     04
296      multipathd       0.00     0.00     0.00     0.00     0.58     02

PID      NAME             FPARMv8  NEON     SVE      SVE2     %TOTAL   TOTAL
ALL      ALL              3.57     12.86    0.00     0.00     100.00   140
17400    processwatch     3.73     13.43    0.00     0.00     95.71    134
4939     sshd             0.00     0.00     0.00     0.00     2.86     04
296      multipathd       0.00     0.00     0.00     0.00     0.71     01
560      snapd            0.00     0.00     0.00     0.00     0.71     01

PID      NAME             FPARMv8  NEON     SVE      SVE2     %TOTAL   TOTAL
ALL      ALL              1.18     5.12     0.00     0.00     100.00   254
17400    processwatch     1.19     5.16     0.00     0.00     99.21    252
6651     packagekitd      0.00     0.00     0.00     0.00     0.39     01
4939     sshd             0.00     0.00     0.00     0.00     0.39     01
```
Every two seconds, the next set of samples are appended to the bottom of the output.

Now use Ctrl+c to terminate the run.

