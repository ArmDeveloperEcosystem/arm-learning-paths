---
title: Test Snort 3 multithreading
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## System Configuration

Before testing the Snort 3 multithreading, configure your system by following these steps:

* Configure Grub settings.
* Set up the Snort 3 rule set.
* Download the PCAP files.
* Adjust Lua configurations. 

#### Configure Grub settings

To enable Transparent HugePages (THP) and configure CPU isolation and affinity, append the following line to the `/etc/default/grub file`, modifying the CPU numbers as required:

{{% notice Note %}}
For the total available online CPUs ranging from 0 to 95, with CPUs 0 to 9 pinned to Snort, the grubfile configuration is shown below. 
{{% /notice %}}


```bash
CMDLINE="cma=128"
HUGEPAGES="default_hugepagesz=1G hugepagesz=1G hugepages=300"
MAXCPUS=""
ISOLCPUS="isolcpus=nohz,domain,0-9"
IRQAFFINITY="irqaffinity=10-95"
NOHZ="nohz_full=0-9"
RCU="rcu_nocbs=0-9"
IOMMU="iommu.passthrough=1"
THP="transparent_hugepage=madvise"
GRUB_CMDLINE_LINUX="${CMDLINE} ${HUGEPAGES} ${ISOLCPUS} ${IRQAFFINITY} ${NOHZ} ${RCU} ${MAXCPUS} ${IOMMU} ${THP}"
```

After making this change, execute `update-grub` to apply the configuration:

```bash
sudo update-grub
```

Reboot the system to activate the settings:

```bash
sudo reboot
```

Confirm the new command line was used for the last boot:

```bash
cat /proc/cmdline
```

The output shows the additions to the kernel command line, and will look something like this:

```output
BOOT_IMAGE=/boot/vmlinuz-6.5.0-1020-aws root=PARTUUID=2ca5cb77-b92b-4112-a3e0-eb8bd3cee2a2 ro cma=128 default_hugepagesz=1G hugepagesz=1G hugepages=300 isolcpus=nohz,domain,0-9 irqaffinity=10-95 nohz_full=0-9 rcu_nocbs=0-9 iommu.passthrough=1 transparent_hugepage=madvise console=tty1 console=ttyS0 nvme_core.io_timeout=4294967295 panic=-1
```

You can also confirm the isolated processors:

```bash
cat /sys/devices/system/cpu/isolated
```

The output shows the isolated processors:

```output
0-9
```

#### Set up the Snort 3 rule set

Download the rule set from https://www.snort.org/ and extract it into your working directory. 

Start in the `build` directory you used to build Snort:

```bash
cd $HOME/build
```

For testing, you can use the file https://www.snort.org/downloads/registered/snortrules-snapshot-3110.tar.gz.

Download and unzip the rule set:

```bash
wget https://www.snort.org/downloads/community/snort3-community-rules.tar.gz
mkdir -p Test/snortrules
tar -xzvf snort3-community-rules.tar.gz -C Test/snortrules
```

Copy the `lua` folder from the `snort3` source directory into the rules directory:

```bash
cp -r snort3/lua/ Test/snortrules/
```

#### Download the Packet Capture (PCAP) files

You can use any packet capture (PCAP) files that are relevant to your test scenario. 

You can obtain PCAP files at: https://www.netresec.com/?page=MACCDC.

Visit https://share.netresec.com/s/wC4mqF2HNso4Ten and download a PCAP file.

Copy the file to your working directory, and extract it. If you downloaded a different PCAP file, you can change the file name. 

```bash
gunzip maccdc2010_00000_20100310205651.pcap.gz
mkdir Test/Pcap
cp maccdc2010_00000_20100310205651.pcap Test/Pcap/
```

#### Adjust Lua configurations

Now make two modifications to the Lau configurations:

* Pin each Snort thread to a unique core, ensuring that the cores match those isolated in the GRUB configuration.
* Enable the desired ruleset and enabling profiling.

#### Pin Snort Threads to Unique CPU Core

Navigate to the `Test/snortrules/lua` directory:

```bash
cd Test/snortrules/lua
````

Use an editor to create a file named `common.lua`, and copy-and-paste in the contents below:

```bash
-------------------------------------------------------------------------------
---- common: shared configuration included at the end of other configs
-------------------------------------------------------------------------------
---- change these mappings so that the first N tests use unique cores
threads =
{
    { thread = 0, cpuset = '0' },
    { thread = 1, cpuset = '1' },
    { thread = 2, cpuset = '2' },
    { thread = 3, cpuset = '3' },
    { thread = 4, cpuset = '4' },
    { thread = 5, cpuset = '5' },
    { thread = 6, cpuset = '6' },
    { thread = 7, cpuset = '7' },
    { thread = 8, cpuset = '8' },
    { thread = 9, cpuset = '9' }
}
process = { threads = threads }
search_engine = { }
snort_whitelist_append("threads")
```
Edit `snort.lua` to include the contents above, and then add in the line below to the end of the file: 

 ``` bash
 include('common.lua')
 ```

#### Modify the snort.lua file to enable rules and profiling 

Use an editor to modify the `snort.lua` file. 

Enable all the rules by uncommenting the `enable_builtin_rules` line and adding the rule search directory as shown below:

```bash
enable_builtin_rules = true,
rules = [[
    include ../snort3-community-rules/snort3-community.rules
]],
```

Continue to edit `snort.lua` and comment out the `profiler` and `latency` lines to enable profiling and packet statistics.

#### Review the Snort parameters: modify the IPS policy

Snort 3 allows you to fine-tune setups with the `--tweaks` parameter. This feature allows you to use one of Snort's policy files to enhance the detection engine for improved performance or increased security.
    
Snort 3 includes four preset policy files: 

* Max_detect.
* Security.
* Balanced.
* Connectivity. 

The max_detect policy focuses on maximum security, and the connectivity policy focuses on performance and uptime, which might come at the expense of security.

#### Specify the data acquisition module

Snort supports data acquisition (DAQ) modules which serve as an abstraction layer for interfacing with a data source such as a network interface. 

To see list of DAQ modules supported by Snort use the `--daq-list` command.

Return to the `build` directory:

```bash
cd $HOME/build
```

Run Snort with the command:

``` bash
snort  --daq-dir ./snort3/dependencies/libdaq/install/lib/daq --daq-list
```

The output should look like this:

```output
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

For testing, you can use `--daq dump` to analyze the CAP files.

#### Spawn Snort 3 process with multithreading

To run Snort 3 with multithreading, start from the `Test` directory.

```bash
cd $HOME/build/Test
```
The following example shows you how to use multiple Snort threads to analyze PCAP files.

``` bash
MPSE=hyperscan POLICY=./snortrules/lua/snort.lua TCMALLOC_MEMFS_MALLOC_PATH=/dev/hugepages/test snort -c ./snortrules/lua/snort.lua --lua detection.allow_missing_so_rules=true --pcap-filter maccdc2010_00000_20100310205651.pcap --pcap-loop 10 --snaplen 0 --max-packet-threads 10 --daq dump --daq-dir /usr/local/lib/daq --daq-var output=none -H --pcap-dir Pcap -Q --warn-conf-strict --tweaks security
```

Use `--pcap-loop` to loop PCAP files a number of times, 10 in this example.

Use `--max-packet-threads` to specify the number of threads, 10 in this example.

To confirm that the Snort process spans many threads, use the `mpstat` command to evaluate the CPU utilization.

```bash
mpstat -P 0-9 1
```

The output is similar to:

```output
22:52:26     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
22:52:28       0   98.50    0.00    1.50    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28       1   98.00    0.00    2.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28       2   98.50    0.00    1.50    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28       3   98.00    0.00    2.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28       4   98.00    0.00    2.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28       5   99.00    0.00    1.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28       6   99.00    0.00    1.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28       7   99.00    0.00    1.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28       8   98.00    0.00    2.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00
22:52:28       9   97.50    0.00    2.50    0.00    0.00    0.00    0.00    0.00    0.00    0.00
```
#### Test Snort 3 multithreading to process a single PCAP file 

The example demonstrates how multithreading increases the number of packets processed per second. 

PCAP File Description

| Name                   | Total Packets |
|------------------------|---------------|
| maccdc2012_0000.pcap   |    86359430   | 

Performance results

| Threads | Packets Per Second | Runtime in Sec |
|---------|--------------------|----------------|
|    1    |        940960      |    91.777964   |
|    10   |        9406134     |    9.181182    |

The results demonstrate how increasing the thread count by ten times results in a ten times increase in packets processed per second, while reducing the execution time by ten times.
