---
# User change
title: "Measure performance of snappy and zstd compression libraries on Arm servers"

weight: 2

layout: "learningpathall"


---

## Prerequisites

* An Arm-based instance from your preferred cloud service [provider](/learning-paths/server-and-cloud/csp/). See the supported operating systems below.
* GCC for your Arm Linux distribution. Install using the steps [here](/install-tools/gcc/#native).
* Unzip and make utilities
```bash { pre_cmd="sudo apt install -y gcc g++" }
sudo apt install -y unzip make
```

## Detailed Steps

The latest released version of [Snappy](http://google.github.io/snappy/) and [Zstandard](http://facebook.github.io/zstd/) data compression algorithms are supported on the following Linux distributions:

* Amazon Linux 2
* RHEL/CentOS 8
* Ubuntu Versions - 20.04, 18.04

The detailed steps below have been tested on `AWS EC2` and `Oracle OCI` Arm-based servers running `Ubuntu 20.04`.

## Install lzbench

[lzbench](https://github.com/inikep/lzbench) is an in-memory benchmark of open-source compression algorithms. We will use this benchmark to measure stand-alone performance of the compression algorithms on Arm servers. 

This benchmark also contains the source files for the snappy and zstd compression algorithms among others. They are built as part of the lzbench build process.

On your running EC2 instance, run the following command

```bash
git clone https://github.com/inikep/lzbench && cd lzbench
make
```

## Download a data set to benchmark the compression algorithms

To benchmark the data compression algorithms, you will need a data set to run the compression and decompression algorithms on. In this how-to guide we will use the [Silesia corpus](https://sun.aei.polsl.pl//~sdeor/index.php?page=silesia) data set, which is a data set of files that covers the typical data types used nowadays.

Download and unpack the data set:
```bash { cwd="lzbench" }
cd ..
wget https://sun.aei.polsl.pl//~sdeor/corpus/silesia.zip
mkdir silesia && cd silesia
unzip ../silesia.zip
cd ../lzbench
```

## Run lzbench with snappy and zstd

To benchmark the standalone performance of `snappy` with `lzbench`, using one of the files(`dickens`) from the Silesia corpus data set we installed run the following command:

```bash { cwd="lzbench" }
./lzbench -esnappy ../silesia/dickens
```

To benchmark the standalone performance of `zstd` with `lzbench`, using one of the files(`dickens`) from the Silesia corpus data set we installed run the following command:

```bash { cwd="lzbench" }
./lzbench -ezstd ../silesia/dickens
```

The value passed to `-e` in the command above is the compression algorithm.

For full usage and viewing all the arguments you can pass to lzbench run the command below

```bash { cwd="lzbench" }
./lzbench --help
```
You can repeat with other file

## View Results

The Compression, Decompression Bandwidth, Latency and Compression ratio for the files is printed at the end of each of these commands

Below is a table with the results on `AWS EC2 Arm 64-bit C6g` instance, with `Ubuntu 20.04` and `gcc 9.3` running with `snappy`.

| File name | Compression Bandwidth (MB/s) | Decompression Bandwidth(MB/s) | Compression Latency (us) | Decompression Latency(us) | Compr Size | Ratio  (%) |
| ---       | ---                          | ---                           | ---                      | ---                       | ---        | ---        |
| ../silesia/nci	           | 755 | 1900	| 44271 | 17684 |	6146795 |	18.32 |
| ../silesia/xml               | 555 | 1462 | 9609  | 3659  |	1308581 |	24.48 |
| ../silesia/samba             | 471 | 1146 | 45841 | 18907 |	8057361 |	37.29 |
| ../silesia/webster           | 296 | 729  | 139904 | 56786 |	20211213 |	48.75 |
| ../silesia/reymont |	290 |	640 |	22833 |	10352 |	3234968 |	48.81 |
| ../silesia/mozilla |	388 |	973 |	131761 |	52582 |	26690826 |	52.11 |
| ../silesia/osdb |	457 |	1211 |	22004 |	8340 |	5412825 | 	53.67 |
| ../silesia/mr |	373 |	787 |	26649 |	12658 |	5440451 |	54.57 |
| ../silesia/dickens |	244 |	548 |	41656 |	18563 |	6340267 |	62.21 |
| ../silesia/ooffice |	292 |	820 |	21028 |	7509 |	4311901 | 	70.09 |
| ./silesia/sao |	313 |	829 |	23175 |	8715 |	6469352 |	89.21 |
| ../silesia/x-ray |	6626 |	11654 |	1270 |	698 |	8459794 |	99.83 |
