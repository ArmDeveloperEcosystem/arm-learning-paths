---
title: Use channels for threaded performance annotations
weight: 7
layout: learningpathall
---
### Using channels in a Godot project

Channels are custom event timelines associated with a software thread. You can create channels and place annotations within them. A channel annotation has a text label and a color but, unlike markers, they span a range of time.

To create a channel called "Spawner" and insert an annotation called "Spawning Wave", with the color red:

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

To see channels in Streamline, select the **Core Map** view, and expand the **VkThread** thread:

![Channel annotations in Streamline](sl_channel.png "Figure 7. Channel annotations in Streamline")