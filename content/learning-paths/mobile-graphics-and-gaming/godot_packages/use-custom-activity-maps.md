---
title: Use Custom Activity Maps in Godot profiling
weight: 9
layout: learningpathall
---

## Visualize jobs and activity with Custom Activity Maps (CAM)

Custom Activity Maps (CAMs) help track complex jobs across multiple non-threaded timelines. Great for modeling gameplay layers like UI, audio, and AI.

### Create a CAM with multiple tracks:

```gdscript
var game_cam : PerformanceStudio_CAM
var wave_track : PerformanceStudio_CAMTrack
var ui_track : PerformanceStudio_CAMTrack

func _ready():
    game_cam = performance_studio.create_cam("Game Activity")
    wave_track = game_cam.create_track("Wave Activity")
    ui_track = game_cam.create_track("UI Activity")
```

### Add jobs to tracks:

```gdscript
var wave_job : PerformanceStudio_CAMJob

func _on_new_wave_started():
    wave_job = wave_track.create_job("Spawning Wave", Color8(255, 0, 0))

func _on_wave_completed():
    wave_job.stop()
```

![Custom activity maps in Streamline](sl_cam.png "Figure 8. Custom activity maps in Streamline")
