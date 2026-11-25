---
title: Understand the Cairn perception stack
description: Trace camera frames through Cairn inference and messaging services to understand how applications receive detection events.
weight: 3
layout: learningpathall
---

## Composable AI Runtimes (Cairn)

[Composable AI Runtimes (Cairn)](https://github.com/arm/composable-ai-runtimes) provides containerized services and Rust and Python client libraries for edge and physical AI applications on Arm Linux. You can use the Python SDK to discover cameras, describe an inference workflow, and subscribe to its results.

You now have live detections arriving from the camera. Before examining the console application, identify the Cairn components that made those results possible. You'll then inspect the application's Python client.

## Learn the Cairn service names

Cairn provides three runtime services used by the object-detection example. Each has a Python client through which your application interacts with it:

| Cairn component | Responsibility | Cairn Python client |
| --- | --- | --- |
| Media Service | Discovers cameras and makes their streams available | `CameraService` |
| Perception Service | Deploys and runs inference workflows on camera streams | `PerceptionService` |
| Messaging Service | Lets services and applications publish and subscribe to events | `NotificationService` |

## Understand how Cairn uses OPK

[Open Perception Kit (OPK)](https://github.com/arm/open-perception-kit) provides reusable components for vision inference on Arm Linux. It uses GStreamer, a media-processing framework, to connect stages that prepare camera frames, run a model, and interpret its outputs. OPK also defines structured inference results and provides a browser viewer for inspecting video, detections, and debug information.

Cairn's [Perception Service](https://github.com/arm/composable-ai-runtimes/blob/main/services/perception/README.md) runs OPK pipelines on camera streams made available by the Media Service. Your application describes the processing through Cairn's SDK; the Perception Service manages the underlying GStreamer pipeline.

The Perception Service forwards OPK inference results through Cairn's Messaging Service. Your application uses the SDK to receive and decode those results, then decides what to do with them. In the object-detection example, OPK performs the frame processing and inference, Cairn provides service access and workflow management, and the console application prints the detections.

## Describe a workflow and receive its results

A Cairn *workflow* describes the processing you want to run on a camera stream. You build that description with `PerceptionWorkflow` and add an inference stage with `infer()`.

Deploying a workflow through the Perception Service returns a *session*, represented by `PerceptionSession`. The session identifies the running workflow and provides its result *topic*. A topic is the messaging channel your application subscribes to with `NotificationService` to receive events. The Perception Service supplies the session's result topic; your application reads it from `session.topics.results`.

For SDK usage and API details, see the [Cairn SDK documentation](https://github.com/arm/composable-ai-runtimes/blob/main/lib/README.md).

## Separate deployment from runtime behaviour

Topo builds and deploys the Compose project to your Arm target over SSH, starting the service and application containers. After those containers start, the Python application calls `PerceptionService.deploy()` to start a Cairn workflow. These are two different deployment steps: Topo deploys containers; the Cairn SDK deploys a workflow inside the running Perception Service.

## What you've learned and what's next

You understand what Cairn is, and how it integrates with OPK and Topo. Next, you will examine the console-based object detection example to see how this is implemented using Cairn.
