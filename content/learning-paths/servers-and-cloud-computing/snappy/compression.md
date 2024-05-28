---
# User change
title: "Install lzbench and measure algorithm performance"

weight: 2

layout: "learningpathall"


---

## Detailed Steps

The latest released version of [Snappy](http://google.github.io/snappy/) and [Zstandard](http://facebook.github.io/zstd/) data compression algorithms are supported on the following Linux distributions:

* Amazon Linux 2
* RHEL/CentOS 8
* Ubuntu Versions - 22.04, 20.04, 18.04

The detailed steps below have been tested on `AWS EC2` and `Oracle OCI` Arm-based servers running `Ubuntu 20.04`.

## Install necessary software packages

* GNU gcc and g++ for your Arm Linux distribution using the [GNU compiler install guide](/install-guides/gcc/native/).
* Unzip and make utilities

```bash { pre_cmd="sudo apt install -y gcc g++" }
sudo apt install -y unzip make
```

## Install lzbench

[lzbench](https://github.com/inikep/lzbench) is an in-memory benchmark of open-source compression algorithms.Use this benchmark to measure stand-alone performance of the compression algorithms on Arm servers. 

This benchmark also contains the source files for the `snappy` and `zstd` compression algorithms among others. They are built as part of the `lzbench` build process.

On your running EC2 instance, run the following command

```bash
git clone https://github.com/inikep/lzbench && cd lzbench
make
```

## Download a data set to benchmark the compression algorithms

To benchmark the data compression algorithms, you will need a data set to run the compression and decompression algorithms on. Use the [Silesia corpus](https://sun.aei.polsl.pl//~sdeor/index.php?page=silesia) data set, which is a data set of files that covers the typical data types used nowadays.

Download and unpack the data set:
```bash { cwd="lzbench" }
cd ..
wget https://sun.aei.polsl.pl//~sdeor/corpus/silesia.zip
mkdir silesia && cd silesia
unzip ../silesia.zip
cd ../lzbench
```

## Run lzbench with snappy and zstd

To benchmark the stand-alone performance of `snappy` with `lzbench`, using one of the files(`dickens`) from the Silesia corpus data set you installed run the following command:

```bash { cwd="lzbench" }
./lzbench -esnappy ../silesia/dickens
```

The output will look similar to:

```output
lzbench 1.8 (64-bit Linux)  (null)
Assembled by P.Skibinski

Compressor name         Compress. Decompress. Compr. size  Ratio Filename
memcpy                  16435 MB/s 16275 MB/s    10192446 100.00 ../silesia/dickens
snappy 2020-07-11         234 MB/s   625 MB/s     6340267  62.21 ../silesia/dickens
done... (cIters=1 dIters=1 cTime=1.0 dTime=2.0 chunkSize=1706MB cSpeed=0MB)
```

To benchmark the stand-alone performance of `zstd` with `lzbench`, using one of the files(`dickens`) from the Silesia corpus data set you installed run the following command:

```bash { cwd="lzbench" }
./lzbench -ezstd ../silesia/dickens
```

The output will look similar to:

```output
lzbench 1.8 (64-bit Linux)  (null)
Assembled by P.Skibinski

Compressor name         Compress. Decompress. Compr. size  Ratio Filename
memcpy                  17434 MB/s 16647 MB/s    10192446 100.00 ../silesia/dickens
zstd 1.5.5 -1             194 MB/s   774 MB/s     4261734  41.81 ../silesia/dickens
zstd 1.5.5 -2             138 MB/s   638 MB/s     3864999  37.92 ../silesia/dickens
zstd 1.5.5 -3            97.2 MB/s   584 MB/s     3667667  35.98 ../silesia/dickens
zstd 1.5.5 -4            83.6 MB/s   532 MB/s     3587632  35.20 ../silesia/dickens
zstd 1.5.5 -5            53.6 MB/s   563 MB/s     3529639  34.63 ../silesia/dickens
zstd 1.5.5 -6            37.4 MB/s   603 MB/s     3418515  33.54 ../silesia/dickens
zstd 1.5.5 -7            29.7 MB/s   579 MB/s     3345600  32.82 ../silesia/dickens
zstd 1.5.5 -8            23.0 MB/s   603 MB/s     3308676  32.46 ../silesia/dickens
zstd 1.5.5 -9            20.8 MB/s   560 MB/s     3282524  32.21 ../silesia/dickens
zstd 1.5.5 -10           13.7 MB/s   538 MB/s     3217624  31.57 ../silesia/dickens
zstd 1.5.5 -11           8.40 MB/s   518 MB/s     3175497  31.16 ../silesia/dickens
zstd 1.5.5 -12           8.02 MB/s   495 MB/s     3168791  31.09 ../silesia/dickens
zstd 1.5.5 -13           2.91 MB/s   503 MB/s     3122251  30.63 ../silesia/dickens
zstd 1.5.5 -14           2.21 MB/s   499 MB/s     3084587  30.26 ../silesia/dickens
zstd 1.5.5 -15           1.85 MB/s   481 MB/s     3057963  30.00 ../silesia/dickens
zstd 1.5.5 -16           1.91 MB/s   545 MB/s     2924845  28.70 ../silesia/dickens
zstd 1.5.5 -17           1.54 MB/s   519 MB/s     2895574  28.41 ../silesia/dickens
zstd 1.5.5 -18           1.34 MB/s   496 MB/s     2864587  28.11 ../silesia/dickens
zstd 1.5.5 -19           1.28 MB/s   479 MB/s     2850277  27.96 ../silesia/dickens
zstd 1.5.5 -20           1.26 MB/s   456 MB/s     2849447  27.96 ../silesia/dickens
zstd 1.5.5 -21           1.24 MB/s   454 MB/s     2849413  27.96 ../silesia/dickens
zstd 1.5.5 -22           1.19 MB/s   474 MB/s     2849384  27.96 ../silesia/dickens
done... (cIters=1 dIters=1 cTime=1.0 dTime=2.0 chunkSize=1706MB cSpeed=0MB)
```
The value passed to `-e` in the command above is the compression algorithm.

For full usage and viewing all the arguments you can pass to `lzbench` run the command below:

```bash { cwd="lzbench" }
./lzbench --help
```
You can repeat with another file.

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
