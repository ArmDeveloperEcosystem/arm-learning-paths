---
title: Set up FFmpeg and encode a test video
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview
System resource usage provides an approach to understand the performance of an application as a black box. This Learning Path demonstrates how to sample system resource usage using a script.

The example application you will use is FFmpeg, a tool set that performs video encode and decode tasks. You will run the same tests with both the x86_64 binary (using Windows instruction emulation) and the Arm64 native binary on a Windows on Arm computer.

## Download the packages

You don't need to build FFmpeg from scratch—just grab the ready-made binaries and get started.

- First, download the [FFmpeg x86_64 package](https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2025-07-31-14-15/ffmpeg-n7.1.1-56-gc2184b65d2-win64-gpl-7.1.zip).
- Next, download the [FFmpeg Arm64 native package](https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2025-07-31-14-15/ffmpeg-n7.1.1-56-gc2184b65d2-winarm64-gpl-7.1.zip).

## Unzip the downloaded packages

Once you've downloaded both packages, unzip them. You'll find the binaries in the `bin` folder inside each package. The x86_64 version is for emulation, while the Arm64 version runs natively on your Windows on Arm device. Double-check the folder names so you don't mix them up.

{{% notice Note %}}
It's a good idea to create a separate folder for each version. Make a note of where you put both `ffmpeg.exe` and `ffplay.exe` for each version—you'll need these paths soon to run your tests and compare results.
{{% /notice %}}

Now you're set up with both versions of FFmpeg. Next, you'll use these binaries to encode a video and see how each one performs.

## Download the video source

For this test, you'll use a sample video called RaceNight. Download it from [this public dataset](https://ultravideo.fi/video/RaceNight_3840x2160_50fps_420_8bit_YUV_RAW.7z).

Unzip the package and make a note of the path to the `.yuv` file inside.

## Encode the video

The video you just downloaded is in YUV raw format, which means it's uncompressed and doesn't need decoding to play. To really test your system, you'll use FFmpeg to compress the video with the x265 encoder and convert it to an `.mp4` file.

Assuming everything is in your current directory, open a terminal and run this command:

```console
ffmpeg-n7.1.1-56-gc2184b65d2-win64-gpl-7.1\ffmpeg-n7.1.1-56-gc2184b65d2-win64-gpl-7.1\bin\ffmpeg.exe -f rawvideo -pix_fmt yuv420p -s 3840x2160 -r 50 -i RaceNight_3840x2160_50fps_420_8bit_YUV_RAW\RaceNight_3840x2160_50fps_8bit.yuv -vf scale=1920:1080 -c:v libx265 -preset medium -crf 20 RaceNight_1080p.mp4 -benchmark -stats -report
```

{{% notice Note %}}
Make sure to update the paths to `ffmpeg.exe` and the YUV video file to match where you saved them.
{{% /notice %}}

This command resizes the video and compresses it into an MP4 file using H.265 encoding (via the x265 encoder). The `-benchmark` option shows performance stats while the encoding runs. When it's done, you'll have a new file called `RaceNight_1080p.mp4`.

Try running the command with both the x86_64 and Arm64 versions of FFmpeg. Then, compare the results to see which one is faster.

## View the results

Here's what the output looks like for the x86_64 version of `ffmpeg.exe`:

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

And here's the output from the Arm64 native version:

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

Check out the last line in each output—the run time and frames per second show how each build performed. The Arm64 version is much faster, thanks to running natively on your hardware.

## Review your progress and compare performance

You've successfully set up both x86_64 and Arm64 versions of FFmpeg, downloaded a sample video, and encoded it using each binary on your Windows on Arm device. By comparing the output, you've seen firsthand how native Arm64 performance outpaces emulated x86_64. This gives you a solid foundation for deeper resource usage analysis in the next section.
