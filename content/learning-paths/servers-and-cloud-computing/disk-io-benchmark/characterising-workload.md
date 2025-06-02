---
title: Analyzing I/O behavior with real workloads
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Workload attributes 

The basic attributes of a given workload are the following: 

- IOPS.
- I/O size.
- Throughput.
- Read-to-write ratio.
- Random vs. sequential access.

While latency is also an important factor, this section focuses on these high-level metrics to establish a foundational understanding.

## Run an example workload

Connect to an Arm-based server or cloud instance. 

As an example workload, use the media manipulation tool, FFMPEG on an AWS `t4g.medium` instance. 

This is an Arm-based (AWS Graviton2) virtual machine with two vCPUs and 4 GiB of memory, designed for general-purpose workloads with a balance of compute, memory, and network resources.

First, install the required tools: 

```bash
sudo apt update 
sudo apt install ffmpeg iotop -y
```

Download the sample video `BigBuckBunny.mp4`, available under the [Creative Commons Attribution 3.0 License](https://creativecommons.org/licenses/by/3.0/).

```bash
cd ~
mkdir src && cd src
wget http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4
```

Run the following command to begin transcoding the video and audio using the `H.264` and `aac` transcoders respectively. The `-flush_packets` flag forces FFMPEG to write each chunk of video data from memory to storage immediately, rather than buffering it in memory. 

This reduces the risk of data loss in case of a crash and allows disk write activity to be more observable during monitoring, making it easier to study write behavior in real-time.

```bash
ffmpeg -i BigBuckBunny.mp4 -c:v libx264 -preset fast -crf 23 -c:a aac -b:a 128k -flush_packets 1 output_video.mp4
```

### Observe disk usage 

While the transcoding is running, you can use the `pidstat` command to see the disk statistics of that specific process. 

```bash
pidstat -d -p $(pgrep ffmpeg) 1
```

Since this example video (151 MB) fits within memory, you observe no `kB_rd/s` for the storage device after the initial read. However, because you are flushing to storage, you observe periodic writes of approximately 275 `kB_wr/s`.  

```output
Linux 6.8.0-1024-aws (ip-10-248-213-118)        04/15/25        _aarch64_       (2 CPU)

10:01:24      UID       PID   kB_rd/s   kB_wr/s kB_ccwr/s iodelay  Command
10:01:25     1000     24250      0.00    276.00      0.00       0  ffmpeg
10:01:26     1000     24250      0.00    256.00      0.00       0  ffmpeg
10:01:27     1000     24250      0.00    216.00      0.00       0  ffmpeg
10:01:28     1000     24250      0.00    184.00      0.00       0  ffmpeg
10:01:29     1000     24250      0.00    424.00      0.00       0  ffmpeg
10:01:30     1000     24250      0.00    312.00      0.00       0  ffmpeg
10:01:31     1000     24250      0.00    372.00      0.00       0  ffmpeg
10:01:32     1000     24250      0.00    344.00      0.00       0  ffmpeg
```

{{% notice Note%}}
In this simple example, since you are interacting with a file on the mounted filesystem, you are also observing the behavior of the filesystem. 
{{% /notice %}}

There might be other processes or background services that are writing to this disk. You can use the `iotop` command for inspection. As shown in the output below, the `ffmpeg` process has the highest disk utilization. 

```bash
sudo iotop
```

```output
Total DISK READ:         0.00 B/s | Total DISK WRITE:       332.11 K/s
Current DISK READ:       0.00 B/s | Current DISK WRITE:       0.00 B/s
    TID  PRIO  USER     DISK READ DISK WRITE>    COMMAND                                                       
  24891 be/4 ubuntu      0.00 B/s  332.11 K/s ffmpeg -i BigBuckBunny.mp4 -c:v ~ts 1 output_video.mp4 [mux0:mp4]
      1 be/4 root        0.00 B/s    0.00 B/s systemd --system --deserialize=74
      2 be/4 root        0.00 B/s    0.00 B/s [kthreadd]
```

Using the input/output statistics command (`iostat`), you can observe the system-wide metrics from the `nvme0n1` drive. 

{{% notice Note%}}
Be mindful of the fact that you are using a snapshot of this workload; more accurate characteristics can be obtained by measuring the distribution of a workload. 
{{% /notice %}}



```bash
watch -n 0.1 iostat -z nvme0n1
```
You see output similar to that below. 

```output
Device             tps    kB_read/s    kB_wrtn/s    kB_dscd/s    kB_read    kB_wrtn    kB_dscd
nvme0n1           3.81        31.63       217.08         0.00     831846    5709210          0
```

To observe more detailed metrics, you can run `iostat` with the `-x` option.

```bash
iostat -xz nvme0n1
```

The output is similar to:

```output
Device            r/s     rkB/s   rrqm/s  %rrqm r_await rareq-sz     w/s     wkB/s   wrqm/s  %wrqm w_await wareq-sz     d/s     dkB/s   drqm/s  %drqm d_await dareq-sz     f/s f_await  aqu-sz  %util
nvme0n1          0.66     29.64     0.24  26.27    0.73    44.80    2.92    203.88     3.17  52.01    2.16    69.70    0.00      0.00     0.00   0.00    0.00     0.00    0.00    0.00    0.01   0.15
```

### Basic attributes of the example workload

This is a simple transcoding workload with flushed writes, where most data is processed and stored in memory. Disk I/O is minimal, with an IOPS of just 3.81, low throughput (248.71 kB/s), and an average IO depth of 0.01 — all summarized in very low disk utilization. The 52% write merge rate and low latencies further suggest sequential, infrequent disk access, reinforcing that the workload is primarily memory-bound.

| Metric             | Calculation Explanation                                                                                     | Value         |
|--------------------|-------------------------------------------------------------------------------------------------------------|---------------|
| IOPS               | Taken directly from the `tps` (transfers per second) field                                                  | 3.81          |
| Throughput (Read)  | From monitoring tool output                                                                                 | 31.63 kB/s    |
| Throughput (Write) | From monitoring tool output                                                                                 | 217.08 kB/s   |
| Throughput (Total) | Sum of read and write throughput                                                                            | 248.71 kB/s   |
| Avg I/O Size       | Total throughput divided by IOPS: 248.71 / 3.81                                                             | ≈ 65.3 KB     |
| Read Ratio         | Read throughput ÷ total throughput: 31.63 / 248.71                                                          | ~13%          |
| Write Ratio        | Write throughput ÷ total throughput: 217.08 / 248.71                                                        | ~87%          |
| IO Depth           | Taken directly from `aqu-sz` (average number of in-flight I/Os)                                             | 0.01          |
| Access Pattern     | 52% of writes were merged (`wrqm/s` = 3.17, `w/s` = 2.92), indicating mostly sequential disk access with low wait times and frequent cache hits | Sequential (52.01% merged) |

{{% notice Note %}}
If you have access to the workload's source code, you can more easily observe the expected access patterns. 
{{% /notice %}}
