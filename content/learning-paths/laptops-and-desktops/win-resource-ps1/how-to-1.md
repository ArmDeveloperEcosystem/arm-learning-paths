---
title: Set up FFmpeg and encode a test video
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
System resource usage provides an approach to understand the performance of an application as a black box. This Learning Path demonstrates how to sample system resource usage using a script.

The example application you will use is FFmpeg, a tool set that performs video encode and decode tasks. You will run the same tests with both the x86_64 binary (using Windows instruction emulation) and the Arm64 native binary on a Windows on Arm computer.

## Application
Binary builds of FFmpeg are available, so you don't need to build them from source. 

To get started: 

1. Download the [FFmpeg x86_64 package](https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2025-07-31-14-15/ffmpeg-n7.1.1-56-gc2184b65d2-win64-gpl-7.1.zip).

2. Download the [FFmpeg Arm64 native package](https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2025-07-31-14-15/ffmpeg-n7.1.1-56-gc2184b65d2-winarm64-gpl-7.1.zip).

3. Unzip the downloaded packages. 

You can find the binaries in the `bin` folder. 

{{% notice Note %}}
Make note of the paths to both versions of `ffmpeg.exe` and `ffplay.exe`, so you can run each one and compare the results. 
{{% /notice %}}

## Video source
Download the test video [RaceNight](https://ultravideo.fi/video/RaceNight_3840x2160_50fps_420_8bit_YUV_RAW.7z) from a public dataset. 

Unzip the package and note the path to the uncompressed `.yuv` file.

## Video encoding
The downloaded video file is in YUV raw format, which means playback of the video file involves no decoding effort. You need to encode the raw video with compression algorithms to add computation pressure during playback.

Use `ffmpeg.exe` to compress the YUV raw video with the x265 encoder and convert the file format to `.mp4`. 

Assuming you downloaded the files and extracted them in the current directory, open a terminal and run the following command:

```console
ffmpeg-n7.1.1-56-gc2184b65d2-win64-gpl-7.1\ffmpeg-n7.1.1-56-gc2184b65d2-win64-gpl-7.1\bin\ffmpeg.exe -f rawvideo -pix_fmt yuv420p -s 3840x2160 -r 50 -i  RaceNight_3840x2160_50fps_420_8bit_YUV_RAW\RaceNight_3840x2160_50fps_8bit.yuv -vf scale=1920:1080 -c:v libx265 -preset medium -crf 20 RaceNight_1080p.mp4 -benchmark -stats -report
```

{{% notice Note %}}
Modify the paths to `ffmpeg.exe` and the YUV raw video file to match your locations.
{{% /notice %}}

The command transforms the video size and compresses the video into an MP4 file using H.265 encoding (via the x265 encoder). 

The `benchmark` option is turned on to show performance data at the same time. 

The generated file will be at RaceNight_1080p.mp4.

Run the command with both the x86_64 and the Arm64 versions of FFmpeg and compare the output.

### View results

The output below is from the x86_64 version of `ffmpeg.exe`:

```output
x265 [info]: tools: rd=3 psy-rd=2.00 early-skip rskip mode=1 signhide tmvp
x265 [info]: tools: b-intra strong-intra-smoothing lslices=6 deblock sao
Output #0, mp4, to 'RaceNight_1080p.mp4':
  Metadata:
    encoder         : Lavf61.7.100
  Stream #0:0: Video: hevc (hev1 / 0x31766568), yuv420p(tv, progressive), 1920x1080, q=2-31, 50 fps, 12800 tbn
      Metadata:
        encoder         : Lavc61.19.101 libx265
      Side data:
        cpb: bitrate max/min/avg: 0/0/0 buffer size: 0 vbv_delay: N/A
[out#0/mp4 @ 0000020e0d6f3880] video:13297KiB audio:0KiB subtitle:0KiB other streams:0KiB global headers:2KiB muxing overhead: 0.079970%
frame=  600 fps=8.4 q=29.4 Lsize=   13308KiB time=00:00:11.96 bitrate=9115.2kbits/s speed=0.167x
bench: utime=480.344s stime=10.203s rtime=71.548s
bench: maxrss=910112KiB
x265 [info]: frame I:      3, Avg QP:22.41  kb/s: 50202.13
x265 [info]: frame P:    146, Avg QP:23.73  kb/s: 18265.18
x265 [info]: frame B:    451, Avg QP:28.45  kb/s: 5827.62
x265 [info]: Weighted P-Frames: Y:0.0% UV:0.0%

encoded 600 frames in 71.51s (8.39 fps), 9075.96 kb/s, Avg QP:27.27
```

The output below is from the Arm64 native compiled `ffmpeg.exe`:

```output
x265 [info]: tools: rd=3 psy-rd=2.00 early-skip rskip mode=1 signhide tmvp
x265 [info]: tools: b-intra strong-intra-smoothing lslices=6 deblock sao
Output #0, mp4, to 'RaceNight_1080p.mp4':
  Metadata:
    encoder         : Lavf61.7.100
  Stream #0:0: Video: hevc (hev1 / 0x31766568), yuv420p(tv, progressive), 1920x1080, q=2-31, 50 fps, 12800 tbn
      Metadata:
        encoder         : Lavc61.19.101 libx265
      Side data:
        cpb: bitrate max/min/avg: 0/0/0 buffer size: 0 vbv_delay: N/A
[out#0/mp4 @ 000001b3c215f8e0] video:13348KiB audio:0KiB subtitle:0KiB other streams:0KiB global headers:2KiB muxing overhead: 0.080169%
frame=  600 fps= 23 q=29.3 Lsize=   13359KiB time=00:00:11.96 bitrate=9150.2kbits/s speed=0.456x
bench: utime=169.891s stime=7.281s rtime=26.224s
bench: maxrss=1040836KiB
x265 [info]: frame I:      3, Avg QP:22.40  kb/s: 50457.20
x265 [info]: frame P:    146, Avg QP:23.71  kb/s: 18246.21
x265 [info]: frame B:    451, Avg QP:28.40  kb/s: 5878.38
x265 [info]: Weighted P-Frames: Y:0.0% UV:0.0%

encoded 600 frames in 26.20s (22.90 fps), 9110.78 kb/s, Avg QP:27.23
```

The last line of each output shows the run time and the frames per second for each build of FFmpeg. 

Continue to learn how to track resource usage and compare each version.