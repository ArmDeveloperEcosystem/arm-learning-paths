---
title: Running Process Watch
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Root or not root
Process Watch can be ran by a non-root user, however to do so requires root to modify your system to be non-standard and less secure. It is recommended that Process Watch is instead ran by root.

To enable non-root users to run Process Watch. You'll need to run the following as root
* setcap CAP_PERFMON,CAP_BPF=+ep ./processwatch
* sysctl -w kernel.perf_event_paranoid=-1
* sysctl kernel.unprivileged_bpf_disabled=0 (this is only needed on later Ubuntu versions from 21.10 onwards)

## Running Process Watch
The Process Watch tool accepts a number of CLI arguments; These can be seen by running
```output
sudo ./processwatch -h
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


By default, Process Watch will:
 * Print results every 2 seconds
 * Print results until the tool is killed (via ctrl+c)
 * Print all results in a table format on stdout
 * Profile all running processes
 * Display counts for the default filters, which are 'FPARMv8', 'NEON', 'SVE' and 'SVE2'
 * Set the sample period to every 10000 events


## Default Process Watch output
Running Process Watch with no arguments results in the following output:

```output
sudo ./processwatch

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

Every 2 seconds, the next set of samples will be appended to the bottom of the output.