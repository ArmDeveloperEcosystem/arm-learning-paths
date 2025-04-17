---
title: Using FIO
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Setup and Install Fio

I will be using the same `t4g.medium` instance from the previous section with 2 different types of SSD-based elastic block storage devices as per the console screenshot below. Both block devices have the same, 8GiB capacity but the `io1` type offers greater IOPS. In this section we want to observe what the real-world performance for our workload is so that it can inform our selection.

![EBS](./EBS.png)

Flexible I/O (fio) is a command-line tool to generate a synthetic workload with specific I/O characteristics.  Fio is available through most Linux distribution packages. Please refer to the [documentation](https://github.com/axboe/fio) for the binary package availability.

```bash
sudo apt update
sudo apt install fio -y
```

Confirm installation with the following commands. 

```bash
fio --version
```

```output
fio-3.36
```

## Locate Device 

`Fio` allows us to microbenchmark either the block device or a mounted filesystem. The disk free, `df` command to confirm our EBS volumes are not mounted.

```bash
df -hTx tmpfs
```

```output
Filesystem      Type      Size  Used Avail Use% Mounted on
Filesystem      Type      Size  Used Avail Use% Mounted on
/dev/root       ext4      6.8G  2.8G  4.0G  41% /
efivarfs        efivarfs  128K  3.7K  125K   3% /sys/firmware/efi/efivars
/dev/nvme0n1p16 ext4      891M   57M  772M   7% /boot
/dev/nvme0n1p15 vfat       98M  6.4M   92M   7% /boot/efi
```

Using the `lsblk` command to view the EBS volumes attached to the server (`nvme1n1` and `nvme2n1`). The immediate number appended to `nvme`, e.g., `nvme0`, shows it is a physically separate device. `nvme1n1` corresponds to the faster `io2` block device and `nvme2n1` corresponds to the slower `gp3` block device. 

```bash
lsblk -e 7
```

```output
NAME         MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
nvme1n1      259:0    0    8G  0 disk 
nvme0n1      259:1    0    8G  0 disk 
├─nvme0n1p1  259:3    0    7G  0 part /
├─nvme0n1p15 259:4    0   99M  0 part /boot/efi
└─nvme0n1p16 259:5    0  923M  0 part /boot
nvme2n1      259:2    0    8G  0 disk 
```

{{% notice Please Note%}}
If you have more than 1 block volumes attached to an instance, the `sudo nvme list` command from the `nvme-cli` package and be used to differentiate between volumes
{{% /notice %}}

We can use the `blkid` command to find the directory for `nvme1n1`. 

## Generating a Synthetic Workload

Let us say we want to simulate a fictional logging application with the following characteristics observed using the tools from the previous section. 

{{% notice Workload%}}
The logging workload has a light sequential read and write workload. The system write throughput per thread is 5 MB/s with 83% writes. There are infrequent bursts of reads for approximately 5 seconds, operating at 16MB/s per thread. The workload can scale the infrequent reads and writes to use up to 16 threads each. The block size for the writes and reads are 64KiB and 256KiB respectively (as opposed to the standard 4KiB Page size). 

Further, the application is sensitive to latency and since it holds critical information, needs to write directly to non-volatile storage (directIO). 
{{% /notice %}}

The fio tool uses simple configuration `jobfiles` to describe the characterisics of your synthetic workload. Parameters under the `[global]` option are shared among jobs. From the example below, we have created 2 jobs to represent the steady write and infrequent reads. Please refer to the official [documentation](https://fio.readthedocs.io/en/latest/fio_doc.html#job-file-format) for more details. 

Copy and paste the configuration file below into 2 files named `nvme<x>.fio`. Replace the `<x>` with the block devices we are comparing and just the `filename` parameter accordingly. 

```ini
 ; -- start job file including.fio --
[global]
ioengine=libaio
direct=1 ; write directly to the drive
time_based
runtime=30
group_reporting=1
log_avg_msec=1000
rate=16m,5m ; limit to 16 MB/s and 5MB/s for read and write per job
numjobs=${NUM_JOBS} ; set at the command line
iodepth=${IO_DEPTH} ; set at the command line
filename=/dev/nvme1n1 ; or nvme2n1

[steady_write]
name=steady_write
rw=write ; sequential write
bs=64k ; Block size of 64KiB (default block size of 4 KiB)

[burst_read]
name=burst_read
rw=read
bs=256k ; adjust the block size to 64KiB writes (default is 4KiB)
startdelay=10 ; simulate infrequent reads (5 seconds out 30)
runtime=5
; -- end job file including.fio --
```

Run the following commands to run each test back to back.  

```bash
sudo NUM_JOBS=16 IO_DEPTH=64 fio nvme1.fio
```

Then

```bash
sudo NUM_JOBS=16 IO_DEPTH=64 fio nvme2.fio 
```

### Interpreting Results

```output

nvme1:

Run status group 0 (all jobs):
   READ: bw=118MiB/s (124MB/s), 118MiB/s-118MiB/s (124MB/s-124MB/s), io=629MiB (660MB), run=5324-5324msec
  WRITE: bw=80.0MiB/s (83.9MB/s), 80.0MiB/s-80.0MiB/s (83.9MB/s-83.9MB/s), io=2400MiB (2517MB), run=30006-30006msec

Disk stats (read/write):
  nvme1n1: ios=2663/38225, sectors=1294480/4892800, merge=0/0, ticks=148524/454840, in_queue=603364, util=62.19%

nvme2:

Run status group 0 (all jobs):
   READ: bw=85.6MiB/s (89.8MB/s), 85.6MiB/s-85.6MiB/s (89.8MB/s-89.8MB/s), io=456MiB (478MB), run=5322-5322msec
  WRITE: bw=60.3MiB/s (63.2MB/s), 60.3MiB/s-60.3MiB/s (63.2MB/s-63.2MB/s), io=1816MiB (1904MB), run=30119-30119msec

Disk stats (read/write):
  nvme2n1: ios=1872/28855, sectors=935472/3693440, merge=0/0, ticks=159753/1025104, in_queue=1184857, util=89.83%
```

Here we can see that the faster `io2` block storage (`nvme1`) is able to meet the throughput requirement of 80MB/s for steady writes when all 16 write threads are running (5MB/s per thread). However `gp2` saturates at 60.3 MiB/s with over 89.8% SSD utilisation. 

We are told the fictional logging application is sensitive to operation latency. The output belows highlights that over ~35% operations have a latency above 1s on nvme2 compared to ~7% on nvme1. 

```output

  nvme2:

  lat (usec)   : 10=0.01%, 500=1.53%, 750=5.13%, 1000=7.55%
  lat (msec)   : 2=29.49%, 4=0.89%, 10=0.09%, 20=0.02%, 50=0.21%
  lat (msec)   : 100=0.56%, 250=1.84%, 500=6.39%, 750=9.76%, 1000=10.17%
  lat (msec)   : 2000=19.59%, >=2000=6.77%

  nvme1:

  lat (usec)   : 750=0.44%, 1000=0.41%
  lat (msec)   : 2=62.63%, 4=1.12%, 10=0.34%, 20=1.61%, 50=3.91%
  lat (msec)   : 100=2.34%, 250=5.91%, 500=8.46%, 750=4.33%, 1000=2.50%
  lat (msec)   : 2000=3.62%, >=2000=2.38%
```

The insights gathered by microbenchmarking with fio above can lead to more informed decisions about which block storage to connect to your Arm-based instance. 
