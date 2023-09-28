---
title: Scene Walkthrough
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
--- 

# Scene Walkthrough

Let's look at the various components of the example scene.

## UI
A group of canvases for menus and onscreen controls:

![UI](ui-canvases.png "UI Canvases")

## Environment
Includes the arena mesh and light:

![Environment](environment-mesh-light.png "Environment")

## ML-Core
A group of various managers:

![ML-Core](ml-core.png "ML-Core")

## Agents Settings
This component of the scene will be our focus. Agent Settings contains:

- A Battle Environment Controller script
- A Camera
- 2 characters ( Player and NPC, who will be fighting each other)
    * Both are setup with ML
    * Both have models and abilities (like fireball and to lock on target)

![Agents Settings](agents-settings.png "Agents Settings")