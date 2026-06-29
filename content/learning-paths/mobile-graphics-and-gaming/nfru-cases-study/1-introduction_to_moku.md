--- 
title: Introduction to the Moku project
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Project Moku?

Project Moku is an Unreal Engine sample project developed by Arm that demonstrates neural rendering technologies for mobile platforms. Built on Unreal 5.6, it provides a controlled environment for testing Neural Frame Rate Upsampling (NFRU), along with complementary neural rendering techniques such as Neural Super Sampling (NSS), Neural Super Sampling and Denoising (NSSD), and Opacity Micromap (OMM). It is designed to exercise dedicated neural accelerators on GPUs with built-in neural processing support.

![Project Moku corridor scene#center](./images/moku_intro.jpg "Project Moku corridor scene")

## Why use Project Moku for NFRU?

The Project Moku corridor level is designed to showcase NFRU in a clear, controlled scene. Its long corridor makes it easy to observe the visual improvements from higher frame rates, while the fast-moving robot highlights NFRU's ability to generate intermediate frames from consecutive frame pairs. The project also includes various lighting environments and particle VFX scenarios, which help exercise frame generation under different motion or illumination conditions.

For repeatable testing, Project Moku provides reference cuts that replay the same camera paths and gameplay actions across runs. These cuts create a consistent development and test environment, making it easier to compare NFRU disabled and enabled captures, inspect visual artifacts, and measure performance changes. The following screenshots show examples of these reference cuts.

| ![Reference cut 02 showing a Moku lighting and corridor test view#center](./images/reference-cut-02.jpg "Reference cut 02") | ![Reference cut 03 showing a Moku scene variation for NFRU testing#center](./images/reference-cut-03.jpg "Reference cut 03") | ![Reference cut 04 showing a Moku particle VFX test view#center](./images/reference-cut-04.jpg "Reference cut 04") |
| --- | --- | --- |

The scene is optimized to run at over 60 FPS and can present at 120 FPS using generated intermediate frames for a smooth visual experience.

## The result of Moku with and without NFRU
The animated comparison below shows the same Moku scene with NFRU disabled and enabled. Use it to observe how NFRU inserts generated intermediate frames to increase the perceived frame rate, making motion appear smoother while preserving visual detail.

![Comparison of Moku without NFRU at 60 FPS and with NFRU at 120 FPS#center](./images/compare_no_nfru_60fps_vs_nfru_120fps_half_speed_first_half.gif "Comparison of Moku without NFRU at 60 FPS and with NFRU at 120 FPS")

## Next step

Now that you have seen why Project Moku is useful for NFRU evaluation, continue by enabling the Arm Neural Graphics Plugin in the Unreal Engine project.
