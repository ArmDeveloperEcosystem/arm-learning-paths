---
title: Understanding Process Watch
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understanding Process Watch
At a high level the Process Watch tool works like so
* It uses the Linux perf_events interface to sample retired instructions
* It uses a BPF program to retrieve certain things, for example the Program Counter, the PID of the currently executing process and the process name
* The instruction at the PC is decoded and internally Process Watch maintains counts for each instruction sampled

The output of Process Watch looks like

```console
sudo ./processwatch

PID      NAME             FPARMv8  NEON     SVE      SVE2     %TOTAL   TOTAL
ALL      ALL              0.00     0.29     0.00     0.00     100.00   346
17400    processwatch     0.00     0.36     0.00     0.00     80.64    279
254      systemd-journal  0.00     0.00     0.00     0.00     13.01    45
542      irqbalance       0.00     0.00     0.00     0.00     2.60     09
544      rs:main Q:Reg    0.00     0.00     0.00     0.00     2.02     07
560      snapd            0.00     0.00     0.00     0.00     1.16     04
296      multipathd       0.00     0.00     0.00     0.00     0.58     02
```

The two columns on the far left show the process ID and name of all running processes that were sampled during that sampling period.

The two columns on the far right show the total number of retired instructions for each process - and what % of the overall system-wide retired instruction count this processes count relates to. For example, in the 2 second sample period above, there were 346 retired instructions. Of those, 279 instructions were when the processwatch (PID 17400) was running, and 279 is 80.64% of the total 346.

As can be seen, the totals per process/row add up to the overall total.

## Mnemoics / Group columns
By default, Process Watch will output counts of retired instructions for the groups
```console
FPARMv8, NEON, SVE, SVE2
```

These can be override on the CLI and it's also possible to specify mnemoics instead. The allowed group names and allowed mnemonics are derived from LLVM, with the Capstone decoder providing an API to retrieve them.

An example can be see by
```console
 sudo ./processwatch -l
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

Adding -m to the above, like so will list the available mnemonics

```console
 sudo ./processwatch -l -m
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

There is ~110 groups (processwatch -l) and ~1700 mnemonics (processwatch -l -m)

To override the default groups, you can use the -f argument and specify the group or mnemonic name. You can specify multiple -f arguments. However you can't have mnemonics and groups together.

```console
 sudo ./processwatch -f HasSVE2BitPerm -f HasNEONorSME

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

and 

```console
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