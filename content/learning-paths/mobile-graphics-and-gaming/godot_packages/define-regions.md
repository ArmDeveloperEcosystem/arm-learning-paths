---
title: Define performance regions in Godot
weight: 6
layout: learningpathall
---

## Defining regions in your Godot project

To define regions of interest within the game, you can specify a pair of markers prefixed with **Region Start** and **Region End**, for example:

```console
performance_studio.marker("Region Start Times Square")
# Do work
performance_studio.marker("Region End Times Square")
```

These regions are shown on the frame rate analysis chart in the Performance Advisor report.

![Regions in Performance Advisor#center](pa_frame_rate_regions.png "Regions in Performance Advisor")

Performance Advisor also includes dedicated charts for each region at the end of the report, allowing you to analyze them independently.

![Dedicated region charts in Performance Advisor#center](pa_dedicated_region_charts.png "Dedicated region charts in Performance Advisor")





