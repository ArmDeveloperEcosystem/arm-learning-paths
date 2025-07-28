---
title: Use Custom Activity Maps in Godot profiling
weight: 9
layout: learningpathall
---

### Custom Activity Maps

[Custom Activity Map (CAM)](https://developer.arm.com/documentation/101816/latest/Annotate-your-code/User-space-annotations/Custom-Activity-Map-annotations) views allow execution information to be plotted on a hierarchical set of timelines. Like channel annotations, CAM views plot jobs on tracks, but unlike channel annotations, CAM views are not associated with a specific thread. Each CAM view contains one or more tracks and each track contains one or more jobs.

![Custom activity maps in Streamline](sl_cam.png "Figure 8. Custom activity maps in Streamline")

To create a custom activity map and add tracks to it:

```console
var game_cam : PerformanceStudio_CAM
var wave_track : PerformanceStudio_CAMTrack
var ui_track : PerformanceStudio_CAMTrack

func _ready() -> void:
    # Create the CAM
    game_cam = performance_studio.create_cam("Game Activity")

    # Add tracks to the CAM
    wave_track = game_cam.create_track("Wave Activity")
    ui_track = game_cam.create_track("UI Activity")
```

To create a job within a track:

```console
var wave_job : PerformanceStudio_CAMJob

func _on_new_wave_started() -> void:
    wave_job = wave_track.create_job("Spawning Wave", Color8(255, 0, 0))

func _on_wave_completed() -> void:
    wave_job.stop()
```

You can now annotate your Godot game and analyze the performance with markers that give context to a profile in Arm Performance Studio tools.