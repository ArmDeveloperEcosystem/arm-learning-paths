---
title: Create and track custom counters in Godot
weight: 8
layout: learningpathall
---
## What are counters?

Counters are floating-point values plotted as line charts in Streamline. Each value appears with two decimal places of precision.

There are two types of counters:

- Absolute counters: every value is treated as an independent measurement

- Delta counters: each value represents the change since the last measurement (for example, the number of enemy spawns since the last update)

## Define your counter chart

When charts are first defined, you can specify:

- A title: this names the chart in Streamline

- A series name: this labels the specific data stream within the chart

You can group multiple counter series under the same title to plot them on the same chart.

## Create and update a counter

Use the `create_counter()` method to define a counter in your script. For example:

```console
var counter = performance_studio.create_counter("Title", "Series", false)
```

The third parameter sets whether the counter is a delta counter `(true)` or absolute counter `(false)`.

To update the counter value, use:

```console
counter.setValue(42.2)
```

This value will appear in the timeline alongside other profiling data during a Streamline capture.

