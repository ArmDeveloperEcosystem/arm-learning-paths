--- 
title: Introduction to the Moku project
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is Project Moku?

Project Moku is an Unreal Engine sample project developed by Arm that demonstrates neural rendering technologies for mobile platforms. Built on Unreal 5.6, it provides a controlled environment for testing Neural Frame Rate Upscaling (NFRU), along with complementary neural rendering techniques such as Neural Super Resolution (NSS), Neural Super Resolution with denoising (NSSD), and Opacity Micro Map (OMM). It is designed to exercise dedicated neural accelerators on GPUs with built-in neural processing support.

![Moku Introduction](images/moku_intro.jpg)

## Why use Project Moku for NFRU?

The Project Moku corridor level is designed to showcase NFRU in a clear, controlled scene. Its long corridor makes it easy to observe the visual improvements from higher frame rates, while the fast-moving robot highlights NFRU's ability to generate intermediate frames from consecutive frame pairs. The scene is optimized to run at over 60 FPS and can be efficiently upscaled to 120 FPS for a smooth visual experience.

## The result of Moku with and without NFRU
The animated comparison below shows the same Moku scene with NFRU disabled and enabled. Use it to observe how NFRU inserts generated intermediate frames to increase the perceived frame rate, making motion appear smoother while preserving visual detail.

![Comparison of Moku without NFRU at 60 FPS and with NFRU at 120 FPS](images/compare_no_nfru_60fps_vs_nfru_120fps_half_speed_first_half.gif)

## What you'll accomplish

In this Learning Path, you will learn how to analyze the visual quality of generated frames, debug visual artifacts, and use Streamline analysis to optimize performance.
