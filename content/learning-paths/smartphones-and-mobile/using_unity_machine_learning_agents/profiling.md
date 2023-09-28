---
title: Profiling
weight: 8


### FIXED, DO NOT MODIFY
layout: learningpathall
---

# Profiling
This time do a _Build and Run_, but with the following options ticked:

![Profiling Settings](profiling-settings.png "Figure 1. Profiling Settings")

It may take some time, but after the game starts, switch back to the Unity Editor and you should see the Profiler dialog.

![Profiler Dialog](profiler-dialog.png "Figure 2. Profiler Dialog")

Let's zoom in and get an idea of what is going on.

![Profiling Details 1](profiling-details-1.png "Figure 3. Profiling Details 1")

We're running at 30 frames per second, and a large chunk of the frame is just waiting for the next frame. So if we zoom in on the bit where it's actually doing something useful...

![Profiling Details 2](profiling-details-2.png "Figure 4. Profiling Details 2")

Going from right to left, we see that a big chunk at the end is rendering. Next, there's a big chunk of physics and animation update. The last big chunk is the behavior updates that we're really interested in. 

About half the time in the behaviour update is "Collect SphereCast", which is the Ray Perception casting all the rays we requested and getting them back, so that we have the state of our environment. Then in the neural network execution, you can see it is evidently playing the hard boss battle. Most of it is running the neural network and then there's a very thin sliver dedicated to getting the actions back out again, which will then move the characters and get them to to perform the appropriate actions.

The profiler only records about 300 frames by default. Looking back at Figure 2, we get a view across those 300 frames. The blue bits are scripts and that's mainly our Behavior scripts running. There's also little jagged teeth that appear every five frames. It is every five frames because we've told it to run the neural network every fifth frame, and that the increased load.

The profiler allows you to see the performance. Then you can tell whether something is taking too long and decide to fix that issue.