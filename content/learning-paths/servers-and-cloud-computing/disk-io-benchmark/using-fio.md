---
title: Using FIO
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Fio

Flexible I/O (fio) is a command-line tool to generate a synthetic workload with specific I/O characteristics. 

Fio is available through most Linux distribution packages. Please refer to the [documentation](https://github.com/axboe/fio) for the binary package availability.

```bash
sudo apt update
sudo apt install fio gnuplot -y
```

Confirm installation with the following commands. 

```bash
fio --version
gnuplot --version
```

```output
fio-3.36
gnuplot 6.0 patchlevel 0
```

## Locate Device 

We have the option to directly microbenchmark the block device or microbenchmark a mounted filesystem. Use the disk free, `df` command to see if the mounted storage devices connected to your server. We are excluding the temporary file system, `tmpfs` for clarity. 

```bash
df -hTx tmpfs
```
The output below shows a 30GB  

```output
Filesystem      Type      Size  Used Avail Use% Mounted on
Filesystem      Type      Size  Used Avail Use% Mounted on
/dev/root       ext4      6.8G  2.8G  4.0G  41% /
efivarfs        efivarfs  128K  3.7K  125K   3% /sys/firmware/efi/efivars
/dev/nvme0n1p16 ext4      891M   57M  772M   7% /boot
/dev/nvme0n1p15 vfat       98M  6.4M   92M   7% /boot/efi
```

Using the `lsblk` command to view the EBS volumes attached to the server (`nvme1n1` and `nvme2n1`). The immediate number appended to `nvme`, e.g., `nvme0`, shows it is a physically separate device. 

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
We can use the `blkid` command to find the directory for `nvme1n1`. 

## Generating a Synthetic Workload

Let us say we want to simulate an loggin system with the following characteristics observed using the tools from the previous section. 

*The logging workload has a light sequential write averaging 100 IOPS. The system write throughput is 5 MB/s with 83% writes. There are infrequent bursts of reads, operating at 1000 IOPS and 256MB/s. The workload can scale the infrequent reads and writes to use up to 16 threads each.* 

The fio tool uses simple configuration `jobfiles` to describe the characterisics of your synthetic workload. A template `jobfile` is shown below. Parameters under the `[global]` option are shared among jobs. From the example above, we have created 2 jobs to represent the steady write and infrequent reads. 

Please refer to the [documentation](https://fio.readthedocs.io/en/latest/fio_doc.html#job-file-format) for full details on the configuration file structure. 

Copy and paste the configuration file below into 2 files named `nvme<x>.fio`. Replace the `<x>` with the block devices we are comparing and just the `filename` parameter accordingly. 

**Please note**: Do not write to a drive that contains critical information such as drives used for booting. We recommend writing to an unformatted block device or a mounted filesystem that you are OK to lose data from.  

```ini
 ; -- start job file including.fio --
[global]
ioengine=libaio
direct=1 ; write directly to the drive
time_based
runtime=30
group_reporting=1
log_avg_msec=1000
filename=/dev/nvme1n1 ; or nvme1n1


[steady_write]
name=steady_write
rw=write
bs=64k ; Block size of 64KiB (default block size of 4 KiB)
rate=5m ; limit to 5 MiB/s
numjobs=${NUM_JOBS} ; set at the command line
iodepth=${IO_DEPTH}


[burst_read]
name=burst_read
rw=read
bs=256k ; adjust the block size to 64KiB writes (default is 4KiB)
rate=256m ; limit to 256 MiB/s
numjobs=${NUM_JOBS}
iodepth=${IO_DEPTH}
startdelay=10 ; simulate infrequent reads (5 seconds out 30)
runtime=5s
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
The output from NVMe1 shows: 

```output
Run status group 0 (all jobs):
   READ: bw=127MiB/s (133MB/s), 127MiB/s-127MiB/s (133MB/s-133MB/s), io=677MiB (710MB), run=5333-5333msec
  WRITE: bw=80.0MiB/s (83.9MB/s), 80.0MiB/s-80.0MiB/s (83.9MB/s-83.9MB/s), io=2400MiB (2517MB), run=30003-30003msec

Disk stats (read/write):
  nvme1n1: ios=2805/38226, sectors=1391184/4892928, merge=0/0, ticks=188746/514998, in_queue=703745, util=88.53%
```

```output
Run status group 0 (all jobs):
   READ: bw=87.9MiB/s (92.1MB/s), 87.9MiB/s-87.9MiB/s (92.1MB/s-92.1MB/s), io=462MiB (484MB), run=5256-5256msec
  WRITE: bw=59.5MiB/s (62.4MB/s), 59.5MiB/s-59.5MiB/s (62.4MB/s-62.4MB/s), io=1794MiB (1881MB), run=30128-30128msec

Disk stats (read/write):
  nvme2n1: ios=1896/28700, sectors=947760/3673600, merge=0/0, ticks=169728/1054671, in_queue=1224400, util=80.22%
```

More interestingly, the latency for each request is different.

```output
  lat (msec)   : 2=57.80%, 4=0.15%, 10=0.34%, 20=1.46%, 50=3.50%
  lat (msec)   : 100=1.85%, 250=6.17%, 500=11.80%, 750=5.73%, 1000=2.79%
  lat (msec)   : 2000=4.41%, >=2000=4.01%
```

With the `nvme2` device showing 20% of writes taking 2+ seconds to confirm a write, compared to the 4% with `nvme1`. These insights suggest that if this contrived logging system is latency sensitive, the `nvme2` can offer better performance. 

```output
  lat (msec)   : 2=30.37%, 4=0.07%, 10=0.37%, 20=0.14%, 50=0.07%
  lat (msec)   : 100=0.46%, 250=1.89%, 500=6.17%, 750=9.99%, 1000=9.27%
  lat (msec)   : 2000=20.61%, >=2000=9.02%
```
