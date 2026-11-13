---
title: Understand the example
description: Trace how the console example uses the Cairn Python SDK to discover a camera, deploy an inference workflow, and receive detection results.
weight: 4
layout: learningpathall
---

## Identify the components in the running demo

The object-detection example uses Docker Compose to run an instance of each Cairn service. Its `compose.yaml` file gives those instances the following Compose service names:

| Compose service name in this example | Component it runs |
| --- | --- |
| `camera-service` | A Cairn Media Service instance |
| `perception-service` | A Cairn Perception Service instance |
| `messaging-service` | A Cairn Messaging Service instance |

The project adds its own application container alongside those Cairn instances. Its Compose service, `perception-example`, runs the console application that calls the Cairn SDK.

`OPK_HF_DETECTION_MODEL` is a parameter declared by this project's Topo metadata. Its download script uses the value to package a model for the Cairn Perception Service.

## Trace the workflow lifecycle

Open `main.py` in your local `~/cairn-lab/object-detection` directory.

The [Cairn Python SDK](https://github.com/arm/composable-ai-runtimes/blob/main/lib/README.md) provides the `CameraService` client to query the Media Service. `CameraService().list_cameras()` discovers cameras, and the example asks each camera for stream configurations matching its chosen resolution, pixel format, and frame rate. The example selects one supported configuration or raises an error if none matches.

After selecting the camera configuration, the client describes and deploys an inference workflow:

```python
workflow = PerceptionWorkflow(
    "detection-workflow",
    camera_configuration,
)
workflow.infer("objects", "detection_model")

service = await PerceptionService.connect()
session = await service.deploy(workflow)
```

`PerceptionWorkflow`, `infer()`, and `PerceptionService.deploy()` are Cairn SDK APIs. The strings supplied to them are names chosen by the example:

| Name in this example | What it identifies |
| --- | --- |
| `detection-workflow` | The workflow described by this `PerceptionWorkflow` instance |
| `objects` | The inference stage added by this call to `infer()` |
| `detection_model` | The model registered with the Perception Service from the example's packaged model directory |

`deploy()` returns a Cairn `PerceptionSession` identifying the running workflow. Its `topics.results` property supplies the topic generated for that session. The example checks that the topic exists, then subscribes its own `print_result` callback:

```python
subscription = await notifications.subscribe(
    session.topics.results, print_result
)
```

The Cairn SDK's `NotificationService` client subscribes through the Messaging Service. `PerceptionResult.decode()` decodes each event payload, and the SDK result type `BoxDetections` identifies entries containing detected boxes. `print_result` is an application callback defined in `main.py`; its name and console formatting belong to the example.

Inspect the `finally` blocks too. The application unsubscribes and stops the perception session when it receives a shutdown signal.

## Stop the deployment

Stop the console deployment to release its service ports and camera before starting the next application:

```bash
topo stop --target "$CAIRN_TARGET"
```

## What you've accomplished and what's next

You've understood how the simple object detection example used Cairn's API. Next, inspect how Acorn Attack turns the same type of detections into browser events.
