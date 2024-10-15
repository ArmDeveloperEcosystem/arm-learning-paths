---
layout: learningpathall
title: Build and Run the AV1 codec
weight: 2
---

## What is the AV1 codec?

AV1 is an open video compression format from the [Alliance for Open Media (AOM)](https://aomedia.org/). 

The reference software implementation for AV1 encoding and decoding can be found in the `libxaom` library. Significant efforts have been made to optimize the `libxaom` implementation on Arm platforms. This includes making use of the Neon and SVE2 vector extensions available on Arm Neoverse platforms.  The optimized code is available on [Google Git](https://aomedia.googlesource.com/aom/).

## Install the necessary software packages

You will need various development tools to build `libxaom` including CMake and the GNU compiler.

The instructions assume you are running Ubuntu. 

Install the required tools by running: 

```bash
sudo apt install gcc g++ wget cmake p7zip-full -y
```

## Download and build libaom from source

Download the `libxaom` source code:

```bash
git clone https://aomedia.googlesource.com/aom
```

Change directory to the repository, configure the build, and build the library:

```bash
mkdir -p aom/build_aom
cd aom/build_aom
cmake ..
make -j$(nproc)
```

For additional details refer to the [README](https://aomedia.googlesource.com/aom/?pli=1#basic-build).

## Run libaom unit tests

The `libxaom` library has a comprehensive suite of unit tests, written using the GTest framework.

The build above includes the `test_libaom` executable. 

You can run all unit tests by starting `test_libaom` with no arguments. However, the number of tests is huge, and it takes a long to run. Instead, you can constrain the number of tests by specifying a filter.

You can try this help argument:

```bash
./test_libaom --help
```
 
There is also an argument to list the tests:

```bash
./test_libaom --gtest_list_tests | less
```

To run a subset of tests, you can use a filter to run only the Neon Sum of Absolute Difference (SAD) tests.

Here is an example with the filter:

```bash
./test_libaom --gtest_filter="*NEON*SAD*"
```

The output is:

```output
Note: Google Test filter = *NEON*SAD*-:NEON_I8MM.*:NEON_I8MM/*:NEON_I8MM_*:SVE.*:SVE/*:SVE_*:SVE2.*:SVE2/*:SVE2_*
[==========] Running 3650 tests from 17 test suites.
[----------] Global test environment set-up.
[----------] 22 tests from NEON/MaskedSADTest
[ RUN      ] NEON/MaskedSADTest.OperationCheck/0
[       OK ] NEON/MaskedSADTest.OperationCheck/0 (152 ms)
[ RUN      ] NEON/MaskedSADTest.OperationCheck/1
[       OK ] NEON/MaskedSADTest.OperationCheck/1 (152 ms)
[ RUN      ] NEON/MaskedSADTest.OperationCheck/2
[       OK ] NEON/MaskedSADTest.OperationCheck/2 (152 ms)
[ RUN      ] NEON/MaskedSADTest.OperationCheck/3
[       OK ] NEON/MaskedSADTest.OperationCheck/3 (152 ms)
[ RUN      ] NEON/MaskedSADTest.OperationCheck/4
[       OK ] NEON/MaskedSADTest.OperationCheck/4 (153 ms)
[ RUN      ] NEON/MaskedSADTest.OperationCheck/5
[       OK ] NEON/MaskedSADTest.OperationCheck/5 (152 ms)
[ RUN      ] NEON/MaskedSADTest.OperationCheck/6
[       OK ] NEON/MaskedSADTest.OperationCheck/6 (152 ms)

< output omitted>

[----------] 90 tests from NEON_DOTPROD/SADSkipx4Test (1433 ms total)

[----------] Global test environment tear-down
[==========] 3650 tests from 17 test suites ran. (56720 ms total)
[  PASSED  ] 3650 tests.

  YOU HAVE 581 DISABLED TESTS
```

## Performance benchmarking

You can benchmark either the encoding or decoding processes. In this section, you will focus on encoding. 

For Performance benchmarking, you can select video encoding either on-demand or live stream.

To start, download some example `8-bit FHD`, `8-bit 4K` and `10-bit 4K` video files:

```bash
wget https://ultravideo.fi/video/Bosphorus_1920x1080_120fps_420_8bit_YUV_Y4M.7z 
wget https://ultravideo.fi/video/Bosphorus_3840x2160_120fps_420_8bit_YUV_Y4M.7z 
wget https://ultravideo.fi/video/Bosphorus_3840x2160_120fps_420_10bit_YUV_Y4M.7z 
```

Next, extract the contents of the 7z files: 

```bash
7za e Bosphorus_1920x1080_120fps_420_8bit_YUV_Y4M.7z
7za e Bosphorus_3840x2160_120fps_420_8bit_YUV_Y4M.7z
7za e Bosphorus_3840x2160_120fps_420_10bit_YUV_Y4M.7z 
```

### On-demand video encoding

For on-demand encoding you can experiment different number of processors and monitor performance.

For example, run with `--good` and use the `--cpu-used` argument to vary video quality/compression options from 2 to 6.

{{% notice Note %}}
The `--cpu-used` flag is used to trade-off encoding speed for resulting video quality/compression, not to determine how many CPUs to use for parallel encoding. Lower numbers indicate better quality and longer encoding time.
{{% /notice %}}

Run standard bit depth and change the CPU count and see the results using:

```bash
./aomenc --good --cpu-used=4 --bit-depth=8 -o output.mkv Bosphorus_1920x1080_120fps_420_8bit_YUV.y4m 
```

Try the above command with different `--cpu-used` values.
```bash
./aomenc --good --cpu-used=6 --bit-depth=8 -o output_cpu_used_2.mkv Bosphorus_1920x1080_120fps_420_8bit_YUV.y4m 
```

You can do the same for high bit depth:

```bash
./aomenc --good --cpu-used=4 --bit-depth=10 -o output.mkv Bosphorus_3840x2160_120fps_420_10bit.y4m 
```

### Live stream video encoding

For live stream encoding you can experiment with different number of processors and monitor performance using the `--cpus-used` flag, varying the range from 5 to 9. 

For standard bit depth with 8 CPUs run:

```bash
./aomenc --rt --cpu-used=8 --bit-depth=8 -o output.mkv Bosphorus_1920x1080_120fps_420_8bit_YUV.y4m
```

For high bit depth run:

```bash
./aomenc --rt --cpu-used=8 --bit-depth=10 -o output.mkv Bosphorus_3840x2160_120fps_420_10bit.y4m
```

## View Results

The encoding frame rate (which is frames per second) for the video files is output at the end of each run.

Shown below is example output from running the `libxaom` codec on the 8-bit FHD sample video file with different `--cpu-used` settings to compare the encoding time.

First, run the codec with `--cpu-used=2`:
```bash
./aomenc --good --cpu-used=2 --bit-depth=8 -o output_cpu_used_2.mkv Bosphorus_1920x1080_120fps_420_8bit_YUV.y4m
```
 The output is similar to:
```output
Pass 1/2 frame  600/601   139432B    1859b/f   55770b/s   62641 ms (9.58 fps)
Pass 2/2 frame  600/600   638429B    8512b/f  255360b/s 1103538 ms (0.54 fps)
```

Now, run the codec with `--cpu-used=6`:
```bash
./aomenc --good --cpu-used=6 --bit-depth=8 -o output_cpu_used_6.mkv Bosphorus_1920x1080_120fps_420_8bit_YUV.y4m
```
The output is similar to:
```output
Pass 1/2 frame  600/601   139432B    1859b/f   55770b/s   17500 ms (34.28 fps)
Pass 2/2 frame  600/600   637902B    8505b/f  255150b/s  103754 ms (5.78 fps)
```
As demonstrated in these examples, `--cpu-used=6` is significantly faster than `--cpu-used=2`, by a factor of 2 to 10.
