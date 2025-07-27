---
title: Define performance regions in Godot
weight: 6
layout: learningpathall
---

## Define regions of interest for performance analysis

To define regions of interest within the game, use marker pairs prefixed with “Region Start” and “Region End”:

```gdscript
performance_studio.marker("Region Start Times Square")
# Do work
performance_studio.marker("Region End Times Square")
```

These regions are shown in the **frame rate analysis chart** in Performance Advisor.

![Regions in Performance Advisor](pa_frame_rate_regions.png "Figure 5. Regions in Performance Advisor")

Each region gets a dedicated chart in the final report, so you can analyze them independently.

![Dedicated region charts in Performance Advisor](pa_dedicated_region_charts.png "Figure 6. Dedicated region charts in Performance Advisor")
