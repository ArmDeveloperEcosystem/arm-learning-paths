---
layout: learningpathall
title: Build and Run the VP9 codec
weight: 3
---

## What is the VP9 codec?

VP9 is a next-generation video compression format developed by the [WebM Project](https://www.webmproject.org/).

The reference software implementation for VP9 encoding and decoding can be found in the `libvpx` library. Similar to our efforts around AV1, Arm has invested significant effort to optimize the `libvpx` implementation on Arm platforms. This includes making use of the Neon and SVE2 vector extensions available on Arm Neoverse platforms. You can learn more on [Google for Developers](https://developers.google.com/media/vp9).

## Download and build libvpx from source

Download the `libvpx` source code:

```bash
git clone https://chromium.googlesource.com/webm/libvpx
cd libvpx
```

The configuration allows for different options to be enabled and disabled. 

To see the options run:

```bash
./configure --help
```

Configure and build with VP8 disabled, VP9 enabled, and unit tests enabled:

```bash
./configure --disable-vp8 --enable-vp9 --enable-vp9-highbitdepth --enable-unit-tests
make -j$(nproc)
```

For more information refer to the [README](https://github.com/webmproject/libvpx/blob/main/README).

## Run libvpx unit tests

You can run `libvpx` unit tests using `make`. For example, to run the decoder test run:

```bash
make testdata
make test TEST_NAME=vp9_decoder_test
```

The output is:

```output
Note: Google Test filter = *-:NEON_I8MM.*:NEON_I8MM/*:SVE.*:SVE/*:SVE2.*:SVE2/*
Note: This is test shard 1 of 10.
[==========] Running 1592 tests from 132 test suites.
[----------] Global test environment set-up.
[----------] 1 test from ByteAlignmentTest
[ RUN      ] ByteAlignmentTest.SwitchByteAlignment
[       OK ] ByteAlignmentTest.SwitchByteAlignment (5248 ms)
[----------] 1 test from ByteAlignmentTest (5248 ms total)

[----------] 4 tests from EncodeAPI
[ RUN      ] EncodeAPI.SetRoi
[       OK ] EncodeAPI.SetRoi (4 ms)
[ RUN      ] EncodeAPI.DynamicDeadlineChange
[       OK ] EncodeAPI.DynamicDeadlineChange (4 ms)
[ RUN      ] EncodeAPI.Buganizer311294795
[       OK ] EncodeAPI.Buganizer311294795 (212 ms)
[ RUN      ] EncodeAPI.Buganizer329179808RowMT1BitDepth10
[       OK ] EncodeAPI.Buganizer329179808RowMT1BitDepth10 (26 ms)
[----------] 4 tests from EncodeAPI (248 ms total)

< output omitted >
```

## Performance Benchmarking

Since the majority of developers on Arm servers come from the encoding field, let's focus on explaining this aspect in the following sections.

For Performance benchmarking, you can select video encoding either on-demand or live-stream.

{{% notice Note %}}
The video files are large so adjust the paths to the y4m files in the commands below. You can also copy them to the current directory.
{{% /notice %}}

### On-demand video encoding 

For on-demand encoding you can experiment different number of processors and monitor performance. 

For example, run with `--good` and use the `--cpu-used` argument to vary the number from 2 to 6.

{{% notice Note %}}
The naming of `--cpu-used` flag is to trade off encoding speed for resulting video quality/compression, not to determine how many CPUs to use for parallel encoding. Lower numbers indicate better quality but longer encoding time. For VoD a reasonable range of quality settings is 0-4 inclusive.
{{% /notice %}}

Run standard bit depth and change the CPU count and see the results using:

```bash
./vpxenc --good --cpu-used=2 --profile=0 --bit-depth=8 -o output.mkv Bosphorus_1920x1080_120fps_420_8bit_YUV.y4m 
```

Try the above command with different `--cpu-used` values.
```bash
./vpxenc --good --cpu-used=6 --profile=0 --bit-depth=8 -o output.mkv Bosphorus_1920x1080_120fps_420_8bit_YUV.y4m 
```

You can do the same for high bit depth:

```bash
./vpxenc --good --cpu-used=2 --profile=2 --bit-depth=10 -o output.mkv Bosphorus_3840x2160_120fps_420_10bit_YUV.y4m
```

### Live-stream video encoding

For live-stream encoding you can experiment different number of processors and monitor performance using the `--cpus-used` in the range from 5 to 9. 

{{% notice Note %}}
The naming of `--cpu-used` flag is to trade off encoding speed for resulting video quality/compression, not to determine how many CPUs to use for parallel encoding. Lower numbers indicate better quality but longer encoding time. For live-stream a reasonable range of quality settings is 5-9.
{{% /notice %}}


For standard bit depth with 8 CPUs run:

```bash
./vpxenc --rt --cpu-used=8 --profile=0 --bit-depth=8 -o output.mkv Bosphorus_1920x1080_120fps_420_8bit_YUV.y4m
```

For high bit depth run:

```bash
./vpxenc --rt --cpu-used=8 --profile=2 --bit-depth=10 -o output.mkv Bosphorus_3840x2160_120fps_420_10bit_YUV.y4m
```


## View Results

The encoding frame rate (frames per second) for the video files is output at the end of each run.

Shown below is example output from running the `libvpx` codec on the 8-bit FHD sample video file with different --cpu-used settings to compare the encoding time.

As demonstrated in these examples, --cpu-used=6 is 30% faster than --cpu-used=2.

--cpu-used=2
```output
Pass 1/2 frame  175/174    37584B 7956010 us 22.00 fps [ETA  0:00:00] Error reading Y4M frame data.
Pass 1/2 frame  175/176    38016B    1737b/f   52136b/s 8002966 us (21.87 fps)
Pass 2/2 frame  175/150   177340B   35578 ms 4.92 fps [ETA  0:00:05]     213FError reading Y4M frame data.
Pass 2/2 frame  175/151   177553B   35715 ms 4.90 fps [ETA  0:00:05]     272F    213F    212F    224F    205F    183F    164F    160F    146F     52F   4604F    27Pass 2/2 frame  175/175   186760B    8537b/f  256128b/s   29706 ms (5.89 fps)
```

--cpu-used=6
```output
Pass 1/2 frame  175/174    37584B 7975777 us 21.94 fps [ETA  0:00:00] Error reading Y4M frame data.
Pass 1/2 frame  175/176    38016B    1737b/f   52136b/s 8022443 us (21.81 fps)
Pass 2/2 frame  175/150   189400B   27014 ms 6.48 fps [ETA  0:00:04]     227FError reading Y4M frame data.
Pass 2/2 frame  175/151   189627B   27048 ms 6.47 fps [ETA  0:00:04]     252F    209F    226F    215F    210F    197F    180F    171F    158F     49F   5257F    16Pass 2/2 frame  175/175   199034B    9098b/f  272960b/s   20373 ms (8.59 fps)
```