---
title: Use channels for threaded performance annotations
weight: 7
layout: learningpathall
---
## Use channels for threaded annotations in Godot

Channels are custom event timelines associated with a specific software thread. Unlike single-point markers, channel annotations span a duration and include a label and optional color. You can use them to trace task execution or track long-running operations, such as asset loading or enemy spawning.

## Create and annotate a channel

To define a new channel named **Spawner** and insert an annotation labeled **Spawning Wave**, use the following approach:

```console
var channel : PerformanceStudio_Channel

func _ready() -> void:
    channel = performance_studio.create_channel("Spawner")

# Annotations can then be inserted into a channel:
func _on_new_wave_started() -> void:
    channel.annotate_color("Spawning Wave", Color8(255, 0, 0))

func _on_wave_completed() -> void:
    channel.end()
```
In this example:

- The `annotate_color()` method begins a red-colored annotation labeled Spawning Wave

- The end() method marks when the annotation finishes

## View channels in Streamline

To see channels in Streamline, select the **Core Map** view, and expand the **VkThread** thread:

![Channel annotations in Streamline#center](sl_channel.png "Channel annotations in Streamline")