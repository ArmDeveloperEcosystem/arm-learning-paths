---
title: Create and track custom counters in Godot
weight: 8
layout: learningpathall
---

## Track numerical performance data using counters

Counters are float values plotted as charts in the Streamline timeline. You can use **absolute counters** (e.g., frame rate) or **delta counters** (e.g., events per frame).

### Create a counter:

```gdscript
var counter = performance_studio.create_counter("Title", "Series", false)
```

- `Title` = name of the chart
- `Series` = label for the data series
- `false` = absolute (set `true` for delta counters)

### Update counter values:

```gdscript
counter.setValue(42.2)
```

Multiple series can share the same chart title to group related values together.
