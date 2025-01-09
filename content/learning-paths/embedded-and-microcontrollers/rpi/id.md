---
# User change
title: "Identifying the hardware"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Hardware identification	
				
The first place to start is identifying the hardware. 

Both the Raspberry Pi 4 and the Arm cloud server are running a 64-bit Linux OS. 

The first command to try is `uname`. 

The output is similar on both machines. Your output may be slightly different depending on the version of the Linux kernel.

On each machine run the `uname` command.

```console
uname -a
```

For the Raspberry Pi 4, the output is:

```output
Linux raspberrypi 5.15.30-v8+ #1536 SMP PREEMPT Mon Mar 28 13:53:14 BST 2022 aarch64 GNU/Linux
```

For an Oracle Cloud Ampere A1 instance, the output is:

```output
Linux instance-20220413-2250 5.15.0-1027-oracle #33~20.04.1-Ubuntu SMP Tue Jan 10 11:17:00 UTC 2023 aarch64 aarch64 aarch64 GNU/Linux
```
					
For an AWS Graviton2 instance, the output is:

```output
Linux ip-10-0-0-162 5.15.0-1028-aws #32-Ubuntu SMP Mon Jan 9 12:29:05 UTC 2023 aarch64 aarch64 aarch64 GNU/Linux
```

On each machine run the `lscpu` command to list more information about the processors.

```console
lscpu
```

The Raspberry Pi 4 output is below. The processor name is Cortex-A72 and there are only few flags. Also inspect the cache sizes. 

```output
Architecture:                    aarch64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
CPU(s):                          4
On-line CPU(s) list:             0-3
Thread(s) per core:              1
Core(s) per socket:              4
Socket(s):                       1
Vendor ID:                       ARM
Model:                           3
Model name:                      Cortex-A72
Stepping:                        r0p3
CPU max MHz:                     1800.0000
CPU min MHz:                     600.0000
BogoMIPS:                        108.00
L1d cache:                       128 KiB
L1i cache:                       192 KiB
L2 cache:                        1 MiB
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Mmio stale data:   Not affected
Vulnerability Retbleed:          Not affected
Vulnerability Spec store bypass: Vulnerable
Vulnerability Spectre v1:        Mitigation; __user pointer sanitization
Vulnerability Spectre v2:        Vulnerable
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected
Flags:                           fp asimd evtstrm crc32 cpuid
```						 				
					
For the AWS Graviton2 instance the processor name is Neoverse-N1. There are numerous additional flags printed which are not present on the Raspberry Pi 4, and the cache sizes are different.

```output
Architecture:           aarch64
  CPU op-mode(s):       32-bit, 64-bit
  Byte Order:           Little Endian
CPU(s):                 1
  On-line CPU(s) list:  0
Vendor ID:              ARM
  Model name:           Neoverse-N1
    Model:              1
    Thread(s) per core: 1
    Core(s) per socket: 1
    Socket(s):          1
    Stepping:           r3p1
    BogoMIPS:           243.75
    Flags:              fp asimd evtstrm aes pmull sha1 sha2 crc32 atomics fphp asimdhp cpui
                        d asimdrdm lrcpc dcpop asimddp ssbs
Caches (sum of all):
  L1d:                  64 KiB (1 instance)
  L1i:                  64 KiB (1 instance)
  L2:                   1 MiB (1 instance)
  L3:                   32 MiB (1 instance)
NUMA:
  NUMA node(s):         1
  NUMA node0 CPU(s):    0
Vulnerabilities:
  Itlb multihit:        Not affected
  L1tf:                 Not affected
  Mds:                  Not affected
  Meltdown:             Not affected
  Mmio stale data:      Not affected
  Retbleed:             Not affected
  Spec store bypass:    Mitigation; Speculative Store Bypass disabled via prctl
  Spectre v1:           Mitigation; __user pointer sanitization
  Spectre v2:           Mitigation; CSV2, BHB
  Srbds:                Not affected
  Tsx async abort:      Not affected
```

Use the `lshw` command to check other hardware. 

If `lshw` is not available on either machine install it using apt. 

```console
sudo apt-get install lshw
```				
					
Run the `lshw` command with sudo to get the most output. 

```console
sudo lshw
```				
					
The output is long and not shown here. 

The key differences are the additional hardware on the Raspberry Pi 4 for wireless and USB which are not present on Arm servers, but there are many interesting details available to study.

The next sections present some software examples to use on the Raspberry Pi 4 and the Arm cloud server. 
