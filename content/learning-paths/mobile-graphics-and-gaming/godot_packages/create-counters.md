---
title: Create and track custom counters in Godot
weight: 8
layout: learningpathall
---
### Creating counters

Counters are numerical data points that can be plotted as a chart in the Streamline timeline view. Counters can be created as either absolute counters, where every value is an absolute value, or as a delta counter, where values are the number of instances of an event since the last value was emitted. All values are floats and will be presented to 2 decimal places.

When charts are first defined, you can specify a title and series name. The title names the chart, the series names the data series.

Multiple counter series can use the same title, which means that they will be plotted on the same chart in the Streamline timeline.

To create a counter:

```console
var counter = performance_studio.create_counter("Title", "Series", false)
```

Counter values are set easily as shown below:

```console
counter.setValue(42.2)
```

