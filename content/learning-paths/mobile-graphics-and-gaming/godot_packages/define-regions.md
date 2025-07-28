---
title: Define performance regions in Godot
weight: 6
layout: learningpathall
---

## Defining regions in a Godot project

To define regions of interest within the game, you can specify a pair of markers prefixed with “Region Start” and “Region End”, for example:

```console
performance_studio.marker("Region Start Times Square")
# Do work
performance_studio.marker("Region End Times Square")
```

These regions are shown on the frame rate analysis chart in the Performance Advisor report.

![Regions in Performance Advisor](pa_frame_rate_regions.png "Figure 5. Regions in Performance Advisor")

Also, dedicated charts for each region are appended to the end of the report, so you can analyze each region independently.

![Dedicated region charts in Performance Advisor](pa_dedicated_region_charts.png "Figure 6. Dedicated region charts in Performance Advisor")





