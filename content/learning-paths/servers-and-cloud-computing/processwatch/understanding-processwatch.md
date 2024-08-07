---
title: Learn how Process Watch works
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understanding Process Watch

Process Watch uses the Linux `perf_events` interface to sample retired instructions. It uses a Berkeley Packet Filter (BPF) program to retrieve the Program Counter (PC) and the Process ID (PID) of the process being executed. It then decodes the instruction at the PC and internally maintains counts for each instruction that is sampled.

In the previous section, you saw what the output of Process Watch looks like. Let's look at what each field in the output means:

```output
PID      NAME             FPARMv8  NEON     SVE      SVE2     %TOTAL   TOTAL
ALL      ALL              0.00     0.29     0.00     0.00     100.00   346
17400    processwatch     0.00     0.36     0.00     0.00     80.64    279
254      systemd-journal  0.00     0.00     0.00     0.00     13.01    45
542      irqbalance       0.00     0.00     0.00     0.00     2.60     09
544      rs:main Q:Reg    0.00     0.00     0.00     0.00     2.02     07
560      snapd            0.00     0.00     0.00     0.00     1.16     04
296      multipathd       0.00     0.00     0.00     0.00     0.58     02
```

The two columns on the far left show the Process ID and name of all running processes that were sampled during that sampling period.

The two columns on the far right show the total number of retired instructions for each process, and what percentage of the overall system-wide retired instruction count this processes count relates to. For example, in the two second sample period above, there were 346 retired instructions. Of those, 279 instructions were when the processwatch (PID 17400) was running, and 279 is 80.64% of the total 346.

As can be seen, the totals per process and row add up to the overall total.

## Mnemonics / Group columns
By default, Process Watch output counts of retired instructions for the following groups:

```output
FPARMv8, NEON, SVE, SVE2
```

You can change this by using the command-line options. It is also possible to specify mnemonics instead. The allowed group names and allowed mnemonics are derived from LLVM, with the Capstone decoder providing an API to retrieve them.

Let's look at an example:
```bash
 sudo ./processwatch -l
```
The output from this command should look like:
```output
Listing all available categories:
jump
call
return
int
privilege
branch_relative
HasV8_0a
...
HasV8_8a
HasV8_9a
HasV9_0a
...
HasSVE
HasSVE2
HasSVE2p1
HasSVE2AES
HasSVE2SM4
HasSVE2SHA3
...
HasSME2p1
HasSVEorSME
HasSVE2orSME
HasSVE2p1_or_HasSME
HasSVE2p1_or_HasSME2
HasSVE2p1_or_HasSME2p1
HasNEONorSME
...
```

Adding `-m` to the command line arguments lists the available mnemonics:

```bash
 sudo ./processwatch -l -m
```
```output
Listing all available mnemonics:
invalid
abs
adclb
adclt
adcs
...
sbfiz
ubfiz
bfc
bfi
bfxil
```

There are approximately 110 groups (processwatch -l) and around 1700 mnemonics (processwatch -l -m)

To override the default groups, you can use the `-f` argument and specify the group or mnemonic name. You can specify multiple `-f` arguments. However you cannot have mnemonics and groups together.

Here is an example:

```bash
 sudo ./processwatch -f HasSVE2BitPerm -f HasNEONorSME
```
The output will look similar to:
```output
PID      NAME             SVE2BitP NEONorSM %TOTAL   TOTAL
ALL      ALL              0.00     0.00     100.00   94
316709   processwatch     0.00     0.00     98.94    93
254      systemd-journal  0.00     0.00     1.06     01

PID      NAME             SVE2BitP NEONorSM %TOTAL   TOTAL
ALL      ALL              0.00     0.00     100.00   70
316709   processwatch     0.00     0.00     97.14    68
316669   sshd             0.00     0.00     1.43     01
316707   sudo             0.00     0.00     1.43     01
```

Here is another example:

```bash
 sudo ./processwatch -m -f adcs -f bfxil
```
The output will look similar to:

```output
 sudo ./processwatch -m -f adcs -f bfxil

PID      NAME             adcs     bfxil    %TOTAL   TOTAL
ALL      ALL              0.00     0.00     100.00   182
316713   processwatch     0.00     0.00     100.00   182

PID      NAME             adcs     bfxil    %TOTAL   TOTAL
ALL      ALL              0.00     0.00     100.00   17
316713   processwatch     0.00     0.00     88.24    15
316669   sshd             0.00     0.00     5.88     01
316711   sudo             0.00     0.00     5.88     01
```
