---
title:  Profile your Godot game with Arm Performance Studio
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

This Learning Path shows you how to annotate and analyze performance in your Godot game using the Arm Performance Studio extension. You’ll use markers, counters, and timelines to highlight game events, then visualize them in Streamline and Performance Advisor to identify CPU and GPU bottlenecks.

{{% notice Note %}}
 This extension is compatible with **Godot 4.3 and later**.
{{% /notice %}}

## What is Arm Performance Studio?

[Arm Performance Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio) is a free suite of analysis tools to help you profile game performance on mobile devices with Arm CPUs and GPUs. Arm provides a Godot extension to make data from [Godot games](https://godotengine.org/) visible in the Arm Performance Studio tools, [Streamline](https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer) and [Performance Advisor](https://developer.arm.com/Tools%20and%20Software/Performance%20Advisor).

## Add annotations to your Godot project

This package provides a simple way to incorporate annotations into your Godot project. These annotations enable you to mark the timeline with events or custom counters which provides valuable context alongside the performance data in Streamline, so you can see what was happening in the game when bottlenecks occur. For example, here you can see markers that highlight where a wave of enemies is spawning:

![Marker annotations in Streamline#center](sl_annotation.png "Marker annotations in Streamline")
