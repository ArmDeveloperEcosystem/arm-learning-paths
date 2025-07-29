---
title:  Profile your Godot game with Arm Performance Studio
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this Learning Path, you'll learn how to annotate and analyze performance in your Godot game using the Arm Performance Studio extension. You’ll add markers, counters, and timelines to capture game events and visualize them in Streamline and Performance Advisor. These tools help you identify CPU and GPU bottlenecks and optimize performance on Arm-based Android devices.

{{% notice Note %}}
 This extension is compatible with **Godot 4.3 and later**.
{{% /notice %}}

## What is Arm Performance Studio?

[Arm Performance Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Performance%20Studio) is a free suite of analysis tools to profile game performance on mobile devices with Arm CPUs and GPUs. It includes:

- [Streamline](https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer): a performance analyzer that collects CPU and GPU metrics.

- [Performance Advisor](https://developer.arm.com/Tools%20and%20Software/Performance%20Advisor): a report generator that offers optimization suggestions.

Arm provides a Godot extension from [Godot games](https://godotengine.org/) that integrates with these tools, making it easier to capture performance data directly from your game.

## Add annotations to your Godot project

The Arm Performance Studio extension lets you add custom annotations to your Godot project. These annotations include timeline markers and counters that describe what's happening during gameplay,such as loading a level or spawning enemies.

When you record a capture in Streamline, these annotations appear in the timeline alongside CPU and GPU metrics. This context makes it easier to correlate performance issues with in-game events.

For example, here’s a capture showing a marker for when a wave of enemies spawns:

![Marker annotations in Streamline#center](sl_annotation.png "Marker annotations in Streamline")
