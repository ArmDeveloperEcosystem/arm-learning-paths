---
title: Test Snort3 Multithreading
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
Before we begin testing, follow the steps below to ensure Snort3 is properly configured

1. Configure Grub settings
2. Set up the Snort3 Rule Set
3. Download the PCAP files
4. Adjust Lua configurations 

## 1. Configure Grub settings
To enable Transparent HugePages (THP) and configure CPU isolation and affinity, append the following line to the /etc/default/grub file:
```bash
CMDLINE="cma=128"
HUGEPAGES="default_hugepagesz=1G hugepagesz=1G hugepages=300"
MAXCPUS=""
ISOLCPUS="isolcpus=nohz,domain,<CPU-PINNED-TO-SNORT>"
IRQAFFINITY="irqaffinity=<CPU-LIST>"
NOHZ="nohz_full=<CPU-PINNED-TO-SNORT>"
RCU="rcu_nocbs=<CPU-PINNED-TO-SNORT>"
IOMMU="iommu.passthrough=1"
THP="transparent_hugepage=madvise"
GRUB_CMDLINE_LINUX="${CMDLINE} ${HUGEPAGES} ${ISOLCPUS} ${IRQAFFINITY} ${NOHZ} ${RCU} ${MAXCPUS} ${IOMMU} ${THP}"
```
After making this change, execute update-grub to apply the configuration, and then reboot the system to activate the settings.

## 2.   Set up the Snort3 Rule Set
Download the rule set from https://www.snort.org/ and extract it into your working directory. It should be noted that access to the rule set requires a subscription. 
For testing, I used the file https://www.snort.org/downloads/registered/snortrules-snapshot-3110.tar.gz.
### 2.1.    Download and unzip the rule set 
```bash
mkdir -p Test/snortrules-3110
tar -xzvf snortrules-snapshot-3110.tar.gz -C Test/snortrules-3110
```
### 2.2.   Copy the "lua" folder from "snort3" source directory into the rules directory
```bash
 cp -r snort3/lua/ Test/snortrules-3110/
```
## 3.   Download the PCAP files
Feel free to use any pcap files that are relevant to your test scenario. For reference, I’m using this one for my testing: 
https://www.netresec.com/?page=MACCDC
```bash
gunzip maccdc2012_00000.pcap.gz
mv maccdc2012_00000.pcap Test/Pcap/
```

## 4.  Adjust Lua configurations
First, assign each Snort thread to a unique core, ensuring that the cores match those isolated in the GRUB configuration. Next, modify the Lua configuration files to enable the desired ruleset and profiling settings.
### 4.1.    Pin snort threads to unique cpu core
Create a file named 'common.lua' 
```bash
-------------------------------------------------------------------------------
---- common: shared configuration included at the end of other configs
-------------------------------------------------------------------------------
---- change these mappings so that the first N tests use unique cores
threads =
{
    { thread = 0, cpuset = '2' },
    { thread = 1, cpuset = '3' },
    { thread = 2, cpuset = '4' },
    { thread = 3, cpuset = '5' },
    { thread = 4, cpuset = '6' },
    { thread = 5, cpuset = '7' },
    { thread = 6, cpuset = '8' },
    { thread = 7, cpuset = '9' },
    { thread = 8, cpuset = '10' },
    { thread = 9, cpuset = '11' },
    { thread = 10, cpuset = '12' }
}
process = { threads = threads }
search_engine = { }
snort_whitelist_append("threads")

```
 
Include the above file in snort.lua, to do so edit the snort.lua file add below line at the end of the file
 ``` bash
 include('common.lua')
 ```
### 4.2.  Tweak Snort.lua file to enable "rules" and profiling 
 Enable all the rules by adding below line in "ips" block
 ``` bash
enable_builtin_rules = true,
rules = [[
    include ../rules/includes.rules
]],
```
Uncomment "profiler" and "latency" to enable profiling and packet statistics
 

## Snort Parameters
### 1.  - -tweaks to select IPS policy

Snort additionally allows you to fine-tune setups with the --tweaks parameter. This feature allows you to use one of Snort's policy files to enhance the detection engine for improved performance or increased security.
    
Snort 3 includes four preset policy files: max_detect, security, balanced, and connectivity. The max_detect policy favors maximum security, whereas the connectivity policy focuses on performance and uptime, which may come at the expense of security.

### 2.  - -daq to specify Data Acquisition Module
Snort supports DAQ modules which serves as an abstraction layer for interfacing with data source such as network interface. 

To see list of DAQ modules supported by snort use "--daq-list" command.

``` bash
./snort3_src/snort3/build/src/snort  --daq-dir ./snort3_src/snort3/dependencies/libdaq/install/lib/daq --daq-list
Available DAQ modules:
afpacket(v7): live inline multi unpriv
 Variables:
  buffer_size_mb <arg> - Packet buffer space to allocate in megabytes
  debug - Enable debugging output to stdout
  fanout_type <arg> - Fanout loadbalancing method
  fanout_flag <arg> - Fanout loadbalancing option
  use_tx_ring - Use memory-mapped TX ring

bpf(v1): inline unpriv wrapper

dump(v5): inline unpriv wrapper
 Variables:
  file <arg> - PCAP filename to output transmitted packets to (default: inline-out.pcap)
  output <arg> - Set to none to prevent output from being written to file (deprecated)
  dump-rx [arg] - Also dump received packets to their own PCAP file (default: inline-in.pcap)

fst(v1): unpriv wrapper
 Variables:
  no_binding_verdicts - Disables enforcement of binding verdicts
  enable_meta_ack - Enables support for filtering bare TCP acks
  ignore_checksums - Ignore bad checksums while decoding

gwlb(v1): inline unpriv wrapper

nfq(v8): live inline multi
 Variables:
  debug - Enable debugging output to stdout
  fail_open - Allow the kernel to bypass the netfilter queue when it is full
  queue_maxlen <arg> - Maximum queue length (default: 1024)

pcap(v4): readback live multi unpriv
 Variables:
  buffer_size <arg> - Packet buffer space to allocate in bytes
  no_promiscuous - Disables opening the interface in promiscuous mode
  no_immediate - Disables immediate mode for traffic capture (may cause unbounded blocking)
  readback_timeout - Return timeout receive status in file readback mode

savefile(v1): readback multi unpriv

trace(v1): inline unpriv wrapper
 Variables:
  file <arg> - Filename to write text traces to (default: inline-out.txt)
```

For testing, we will use "dump" to analyse pcap files.

## Spawn Snort3 process with multithreading
The following example shows how to use multiple Snort threads to analyze Pcap file.

``` bash
MPSE=hyperscan POLICY=./snortrules-3110/lua/snort.lua TCMALLOC_MEMFS_MALLOC_PATH=/dev/hugepages/test ../snort3_src/snort3/build/src/snort -c ./snortrules-3110/lua/snort.lua --lua detection.allow_missing_so_rules=true --pcap-filter maccdc2012_00000.pcap --pcap-loop 10 --snaplen 0 --max-packet-threads 10 --daq dump --daq-dir  ../snort3_src/snort3/dependencies/libdaq/install/lib/daq --daq-var output=none -H --pcap-dir /root/snort3_learning_path/Test/Pcap -Q --warn-conf-strict --tweaks security
```
--pcap-loop: to loop pcap files for number specified 
--max-packet-threads: to specify threads, which are 10 in this example.

To confirm that the Snort process spans many threads, use the "mpstat" command to evaluate the CPU utilization.

``` bash
mpstat -P 2-14 1

22:52:26     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
22:52:28       2   98.50    0.00    1.50    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28       3   98.00    0.00    2.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28       4   98.50    0.00    1.50    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28       5   98.00    0.00    2.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28       6   98.00    0.00    2.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28       7   99.00    0.00    1.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28       8   99.00    0.00    1.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28       9   99.00    0.00    1.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28      10   98.00    0.00    2.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28      11   97.50    0.00    2.50    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28      12    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00
22:52:28      13    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00
22:52:28      14    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00  100.00
```
## Usecase : Snort3 multi-threading to process single pcap file 
This use case demonstrates how multithreading increases the number of packets processed per second. 

Pcap File Description

| Name                   | Total Packets |
|------------------------|---------------|
| maccdc2012_0000.pcap   |    86359430   | 

Result
| Threads | Packets Per Second | Runtime in Sec |
|---------|--------------------|----------------|
|    1    |        940960      |    91.777964   |
|    10   |        9406134     |    9.181182    |

The results above illustrates that increasing the thread count by ten times results in a ten times increase in packets processed per second, while reducing the execution time by ten times.