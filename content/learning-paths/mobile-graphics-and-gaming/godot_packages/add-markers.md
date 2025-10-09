---
title: Annotate Game Events for Profiling in Godot
weight: 5
layout: learningpathall
---

## Use the Performance Studio extension in your project

All annotation features are provided through the `PerformanceStudio` class. To begin, create an instance in your script:

```gdscript
var performance_studio = PerformanceStudio.new()
```

## Add single markers to highlight key game events

The simplest annotations are single markers. These appear in the Streamline timeline and help you correlate game behavior with performance data.

To emit a basic marker, use the `marker()` method with a descriptive label:

```gdscript
performance_studio.marker("Game Started")
```

This creates a timestamped marker labeled **Game Started**. When you capture a profile in Streamline, you’ll see this marker at the point the game starts.

![Marker annotation in Streamline#center](sl_marker.png "Marker annotation in Streamline")


## Assign a custom color

You can assign a color to the marker using the `marker_color()` method:

```gdscript
performance_studio.marker_color("Game Started", Color8(0, 255, 0))
```

This example displays the Game Started marker in green. Use different colors to visually distinguish important game events.





