---
title: Using FIO
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Simulating Workload with FIO

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


## Best Practices for Microbenchmarking

Software which you did not write or has been less extensively tested will have bugs. Be aware of some of the known [bug tracker](https://github.com/axboe/fio/issues?q=is%3Aissue%20state%3Aopen%20label%3Abug). 

List any assumptions you have, for example, there are no chron jobs running at the time, that the storage media has an on-disk cache, the storage device has the latest stable firmware, temperatures are nominal. 

## Locate Device 

Use the disk free, `df` command to see the mounted storage devices connected to your server. We are excluding the temporary file system, `tmpfs` for clarity. 

```bash
df -hTx tmpfs
```
As we can see the storage we configured through the AWS console is at `/dev/root` with 30GB available. **Please Note** using the incorrect filesystem name can cause issues. 

```output
Filesystem      Type      Size  Used Avail Use% Mounted on
/dev/root       ext4       30G  2.2G   28G   8% /
efivarfs        efivarfs  128K  3.1K  125K   3% /sys/firmware/efi/efivars
/dev/nvme0n1p16 ext4      891M   57M  772M   7% /boot
/dev/nvme0n1p15 vfat       98M  6.4M   92M   7% /boot/efi
```

Using the `lsblk` command to view the 2 elastic block storage (EBS) devices attached to the server (`nvme1n1` and `nvme2n1`). This may be useful if you want to target a specific partition of the disk. Here we can see how the `NVMe` storage device has been partitioned. Fio allows us to test a device through a filesystem or to directly write to block device without a file system. 

```output
nvme2n1      259:0    0   16G  0 disk 
nvme0n1      259:1    0   16G  0 disk 
├─nvme0n1p1  259:3    0   15G  0 part /
├─nvme0n1p15 259:4    0   99M  0 part /boot/efi
└─nvme0n1p16 259:5    0  923M  0 part /boot
nvme1n1      259:2    0   16G  0 disk 
```

## Generating a Synthetic Workload

The fio tool uses simple configuration `jobfiles` to describe the characterisics of your synthetic workload. A template `jobfile` is shown below. Parameters under the `[global]` option are shared among jobs. These can be overwritten if a new value is specified under the job. 

```output
; -- start job file --
[global]
; Common param
[job1]
; job1's parameters
[job2]
; job2's parameters
```

Please refer to the [documentation](https://fio.readthedocs.io/en/latest/fio_doc.html#job-file-format) for full details on the configuration file structure. 


Let us say we want to simulate an I/O workload with the following characteristed observed using various tools. 

*The system's disks have a light sequential write workload averaging 100 IOPS. The system throughput is 5 MB/s with 80% writes. There are infrequent bursts of reads, operating at 1000 IOPS and 256MB/s. The workload can scale the infrequent read to use all the available cores. However, the writes are limited to a single job*

Copy and paste the configuration file below into a file named `example.fio`. Replace the `filename` with the location of where you'd like to read / write to. Please note: Do not write to a drive that contains critical information such as drives used for booting. We recommend writing to an unformatted block device or a mounted filesystem that you are OK to lose data from.  

```ini
 ; -- start job file including.fio --
[global]
ioengine=libaio
direct=1
time_based
runtime=30
group_reporting
log_avg_msec=1000
filename=/dev/nvme1n1


[steady_write]
name=steady_write
rw=write
bs=64k
rate=5m
numjobs=1
iodepth=1
write_bw_log=steady_write
write_iops_log=steady_write
write_lat_log=steady_write

[burst_read]
name=burst_read
rw=read
bs=256k
rate=256m
numjobs=${NUM_JOBS}
iodepth=64
startdelay=10
runtime=5
write_bw_log=burst_read
write_iops_log=burst_read
write_lat_log=burst_read

; -- end job file including.fio --
```

Run the following command to run the workload. 

```bash
sudo NUM_JOBS=$(nproc) fio example.fio
```

