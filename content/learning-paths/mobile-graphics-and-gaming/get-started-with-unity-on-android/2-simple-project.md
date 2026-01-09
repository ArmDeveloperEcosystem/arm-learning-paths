---
title: Sample project
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Open the sample project

With Unity installed with Android build support and a spinning cube running too slowly, you can now start to investigate what's wrong.

1. Open the project in Unity (if you haven't already).

1. Open the _SampleScene_ scene by double-clicking the scene file from the _Project_ tab:

![Open the sample scene#center](images/open-sample-scene.png "Figure 1. Double-click the scene file to open the scene")

You will see a really simple scene with just a few objects:

- Main Camera
- Directional Light
- Cube

The camera and directional light haven't been modified, but if you click on the Cube object, you will see a custom script called `Spin.cs` has been added.

![Spin component on the Cube object#center](images/inspector-cube-object.png "Figure 2. Custom Spin component on the Cube object")

As you can see, the _Spin_ component looks very basic; it simply applies a rotation to the _Cube_ every frame. The speed of which can be changed using the _Rotation_ parameter.

In the next section, you will build the project and deploy it to your Android device. In a real-life case it is good practice to confirm which devices are being affected by which issues.

