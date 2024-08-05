---
layout: learningpathall
title: Build and Run AV1 codec on Arm Servers and Apple Silicon 
weight: 2
---

## Install necessary software packages
`libaom` is a free software video codec library from the Alliance for Open Media ([AOM](https://aomedia.org/)). It serves as the reference software implementation for the AV1 video coding format. It will also be the foundation for AV2 development. There have been significant efforts to optimize the open-source libxaom implementation of the AV2 encoder on Arm Neoverse platforms which supports Neon instructions. The optimized code is available on [googlesource](https://aomedia.googlesource.com/aom/)
There have been significant efforts to optimize the open-source implementation of the AV1 encoder on Arm Neoverse platforms which supports Neon and SVE2 instructions.
Install GCC for your Arm Linux distribution. Refer to the [install guide](/install-guides/gcc/native/) for additional information. 

Install `Cmake`, `gcc`, `g++`and other dependencies:
```bash
sudo apt install gcc g++ git wget cmake
```

## Download and build AV1 source

```bash
git clone https://aomedia.googlesource.com/aom

mkdir build_aom
cd build_aom
cmake <path-to-libaom-source>
make -j 12
```

For detailed instructions refer to this [README](https://aomedia.googlesource.com/aom/?pli=1#basic-build).


## Run AV1 on unit test

`libaom` has a comprehensive suite of unit tests, written using the GTest framework.
Building the code as per the sections above will produce a number of binaries. Among them will be `test_libaom` and running the project unit tests is as simple as doing:

```console
./test_libaom
```

However, the number of tests is huge, and it takes far too long to run them all. Thankfully you can constrain the number of tests by specifying a regex filter:
```console
# Show all of the options that GTest affords us.
./test_libaom --help
 
# List all of the tests - you probably want to pipe this into 'less'.
./test_libaom --gtest_list_tests
```

Or, you can filter runs only the Neon Sum of Absolute Difference (SAD) tests.
```bash
./test_libaom --gtest_filter="*NEON*SAD*"
```

Then, the outout will looks like:
```output
[ RUN      ] NEON_DOTPROD/SADSkipx4Test.SrcAlignedByWidth/14
[       OK ] NEON_DOTPROD/SADSkipx4Test.SrcAlignedByWidth/14 (0 ms)
[ DISABLED ] NEON_DOTPROD/SADSkipx4Test.DISABLED_Speed/0
[ DISABLED ] NEON_DOTPROD/SADSkipx4Test.DISABLED_Speed/1
[ DISABLED ] NEON_DOTPROD/SADSkipx4Test.DISABLED_Speed/2
[ DISABLED ] NEON_DOTPROD/SADSkipx4Test.DISABLED_Speed/3
[ DISABLED ] NEON_DOTPROD/SADSkipx4Test.DISABLED_Speed/4
[ DISABLED ] NEON_DOTPROD/SADSkipx4Test.DISABLED_Speed/5
[ DISABLED ] NEON_DOTPROD/SADSkipx4Test.DISABLED_Speed/6
[ DISABLED ] NEON_DOTPROD/SADSkipx4Test.DISABLED_Speed/7
[ DISABLED ] NEON_DOTPROD/SADSkipx4Test.DISABLED_Speed/8
[ DISABLED ] NEON_DOTPROD/SADSkipx4Test.DISABLED_Speed/9
[ DISABLED ] NEON_DOTPROD/SADSkipx4Test.DISABLED_Speed/10
[ DISABLED ] NEON_DOTPROD/SADSkipx4Test.DISABLED_Speed/11
[ DISABLED ] NEON_DOTPROD/SADSkipx4Test.DISABLED_Speed/12
[ DISABLED ] NEON_DOTPROD/SADSkipx4Test.DISABLED_Speed/13
[ DISABLED ] NEON_DOTPROD/SADSkipx4Test.DISABLED_Speed/14
[----------] 90 tests from NEON_DOTPROD/SADSkipx4Test (767 ms total)

[----------] Global test environment tear-down
[==========] 3650 tests from 17 test suites ran. (31046 ms total)
[  PASSED  ] 3650 tests.

  YOU HAVE 581 DISABLED TESTS
```

## Performance Benchmarking

There are some useful speed unit tests that can act as a good smoke test for an optimization idea. You can run these speed tests (disabled by default) like so:

```bash
# Example: This filter runs only the Neon Sum of Absolute Difference (SAD) speed tests.
./test_libaom --gtest_filter="*NEON*SAD*Speed*" --gtest_also_run_disabled_tests
```

Now, you can benchmark video encoding either On-Demand or Live-Stream.

First of all, you need Download the `8-bit FHD`, `8-bit 4K` and `10-bit 4K` video files:
```bash
wget https://ultravideo.fi/video/Bosphorus_1920x1080_120fps_420_8bit_YUV_Y4M.7z // 8-bit FHD
wget https://ultravideo.fi/video/Bosphorus_3840x2160_120fps_420_8bit_YUV_Y4M.7z // 8-bit 4K
wget https://ultravideo.fi/video/Bosphorus_3840x2160_120fps_420_10bit_YUV_Y4M.7z // 10-bit 4K 
```

Next, extract the contents of the 7z file into your preferred benchmark directory. While I used 7za for this, feel free to use any decompression tool you prefer.

```bash
7za e Bosphorus_1920x1080_120fps_420_8bit_YUV_Y4M.7z
7za e Bosphorus_3840x2160_120fps_420_8bit_YUV_Y4M.7z
7za e Bosphorus_3840x2160_120fps_420_10bit_YUV_Y4M.7z 
```

### On-Demand Video Encoding Benchmarking
For VoD encoding with --good, you should care about --cpu-used in the range [2-6] - so you have to run the following commands five times to cover all cases.

Standard Bitdepth
```bash
./aomenc --good --cpu-used=4 --bit-depth=8 -o output.mkv Bosphorus_1920x1080_120fps_420_8bit_YUV.y4m # --limit=<x> (only encode x frames to reduce waiting time)
```

High Bitdepth
```bash
./aomenc --good --cpu-used=4 --bit-depth=10 -o output.mkv Bosphorus_3840x2160_120fps_420_10bit.y4m # --limit=<x> (only encode x frames to reduce waiting time)
```

### Live-Stream Video Encoding Benchmarking
For the live-stream case with --rt, you should care about --cpu-used in the range [5-9] - so 5 different runs to cover all cases.

```bash
./aomenc --rt --cpu-used=8 --bit-depth=8 -o output.mkv Bosphorus_1920x1080_120fps_420_8bit_YUV.y4m
```

High Bitdepth
```bash
./aomenc --rt --cpu-used=8 --bit-depth=10 -o output.mkv Bosphorus_3840x2160_120fps_420_10bit.y4m
```


## View Results

The encoding Frame Rate (Frames per second) for the video files is output at the end of each run.

Shown below is example output from running the codec on the 8-bit FHD sample video file:

```output
Pass 1/2 frame  600/601   139432B    1859b/f   55770b/s   62641 ms (9.58 fps)
Pass 2/2 frame  600/600   638429B    8512b/f  255360b/s 1103538 ms (0.54 fps)
```
