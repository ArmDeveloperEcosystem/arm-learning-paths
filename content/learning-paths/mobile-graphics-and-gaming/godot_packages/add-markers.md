---
title: Annotate Game Events for Profiling in Godot
weight: 5
layout: learningpathall
---

## Using the extension

All functionality in the extension is provided by the PerformanceStudio class, so first create an instance of it:

```console
var performance_studio = PerformanceStudio.new()
```
## Add single markers to highlight key game events

All functionality in the extension is provided by the `PerformanceStudio` class. First, create an instance:

```gdscript
var performance_studio = PerformanceStudio.new()
```

The simplest annotations are single markers, which can have a name and a color. For example:

```gdscript
performance_studio.marker("Game Started")
```

This will emit a timestamped marker labeled "Game Started." When you capture a profile in Streamline, you’ll see this marker at the point the game starts.

![Marker annotation in Streamline](sl_marker.png "Figure 4. Marker annotation in Streamline")

To assign a color:

```gdscript
performance_studio.marker_color("Game Started", Color8(0, 255, 0))
