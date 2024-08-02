---
layout: learningpathall
title: Build and Run VP9 codec on Arm servers
weight: 2
---

## Install necessary software packages

`libvpx` is a free software video codec library from Google. It serves as the reference software implementation for the VP9 video coding formats.
There have been significant efforts to optimize the open-source libvpx implementation of the VP9 encoder on Arm Neoverse platforms which supports Neon and SVE2 instructions.
Install GCC for your Arm Linux distribution. Refer to the [install guide](/install-guides/gcc/native/) for additional information. 

Install `Cmake`, `gcc`, `g++`and other dependencies:
```bash
sudo apt install gcc g++ git wget cmake
```

## Download and build AV1 source

```bash
git clone https://chromium.googlesource.com/webm/libvpx

mkdir build_libvpx
cd build_libvpx
# ./<path-to-libvpx-source>/configure --help is interesting...
./<path-to-libvpx-source>/configure --disable-vp8 --enable-vp9 --enable-vp9-highbitdepth
make -j 12
```

For detailed instructions refer to this [README](https://aomedia.googlesource.com/aom/?pli=1#basic-build).


## Run AV1 on unit test

`libvpx` has a comprehensive suite of unit tests, written using the GTest framework.
Building the code as per the sections above will produce a number of binaries. Among them will be `test_libvpx` and running the project unit tests is as simple as doing:

```console
./test_libvpx
```

However, the number of tests is huge, and it takes far too long to run them all. Thankfully you can constrain the number of tests by specifying a regex filter:
```console
# Show all of the options that GTest affords us.
./test_libvpx --help
 
# List all of the tests - you probably want to pipe this into 'less'.
./test_libvpx --gtest_list_tests
```

Or, you can filter runs only the Neon Sum of Absolute Difference (SAD) tests.
```
./test_libvpx --gtest_filter="*NEON*SAD*"


[ DISABLED ] NEON/SADSkipx4Test.DISABLED_Speed/42
[ DISABLED ] NEON/SADSkipx4Test.DISABLED_Speed/43
[ DISABLED ] NEON/SADSkipx4Test.DISABLED_Speed/44
[ DISABLED ] NEON/SADSkipx4Test.DISABLED_Speed/45
[ DISABLED ] NEON/SADSkipx4Test.DISABLED_Speed/46
[ DISABLED ] NEON/SADSkipx4Test.DISABLED_Speed/47
[ DISABLED ] NEON/SADSkipx4Test.DISABLED_Speed/48
[----------] 294 tests from NEON/SADSkipx4Test (6 ms total)
[----------] Global test environment tear-down
[==========] 1511 tests from 9 test suites ran. (29 ms total)
[  PASSED  ] 1511 tests.

  YOU HAVE 281 DISABLED TESTS
```

## Performance Benchmarking

There are some useful speed unit tests that can act as a good smoke test for an optimization idea. You can run these speed tests (disabled by default) like so:

```
# Example: This filter runs only the Neon Sum of Absolute Difference (SAD) speed tests.
./test_libvpx --gtest_filter="*NEON*SAD*Speed*" --gtest_also_run_disabled_tests
```

Now, you can benchmark video encoding either On-Demand or Live-Stream.

First of all, you need Download the `8-bit FHD`, `8-bit 4K` and `10-bit 4K` video files:
```bash
wget https://ultravideo.fi/video/Bosphorus_1920x1080_120fps_420_8bit_YUV_Y4M.7z // 8-bit FHD
wget https://ultravideo.fi/video/Bosphorus_3840x2160_120fps_420_8bit_YUV_Y4M.7z // 8-bit 4K
wget https://ultravideo.fi/video/Bosphorus_3840x2160_120fps_420_10bit_YUV_Y4M.7z // 10-bit 4K 
```


### On-Demand Video Encoding Benchmarking

For VoD encoding with --good, you should care about --cpu-used in the range [2-6] - so you have to run the following commands five times to cover all cases.

Standard Bitdepth
```
./vpxenc --good --cpu-used=[0-2] --profile=0 --bit-depth=8 -o output.mkv <8-bit-input-video>.y4m # --limit=<x> (only encode x frames to reduce waiting time)
```

High Bitdepth
```
./vpxenc --good --cpu-used=[0-2] --profile=2 --bit-depth=10 -o output.mkv <10-bit-input-video>.y4m # --limit=<x> (only encode x frames to reduce waiting time)
```

### Live-Stream Video Encoding Benchmarking
For the live-stream case with --rt, you should care about --cpu-used in the range [5-9] - so 5 different runs to cover all cases.

```
./vpxenc --rt --cpu-used=[5-9] --profile=0 --bit-depth=8 -o output.mkv <8-bit-input-video>.y4m
```

High Bitdepth
```
./vpxenc --rt --cpu-used=[5-9] --profile=2 --bit-depth=10 -o output.mkv <10-bit-input-video>.y4m
```





## View Results

The encoding Frame Rate (Frames per second) for the video files is output at the end of each run.

Shown below is example output from running the codec on the 8-bit FHD sample video file:

```output
Pass 1/2 frame  175/174    37584B 7956010 us 22.00 fps [ETA  0:00:00] Error reading Y4M frame data.
Pass 1/2 frame  175/176    38016B    1737b/f   52136b/s 8002966 us (21.87 fps)
Pass 2/2 frame  175/150   177340B   35578 ms 4.92 fps [ETA  0:00:05]     213FError reading Y4M frame data.
Pass 2/2 frame  175/151   177553B   35715 ms 4.90 fps [ETA  0:00:05]     272F    213F    212F    224F    205F    183F    164F    160F    146F     52F   4604F    27Pass 2/2 frame  175/175   186760B    8537b/f  256128b/s   29706 ms (5.89 fps)
```
