---
title: Deploy and verify live object detection
description: Prepare a Raspberry Pi 5 target, deploy the pinned Cairn object-detection example with Topo, and verify camera-driven results.
weight: 2
layout: learningpathall
---

## Run object detection on your Pi with Cairn

You will start by deploying the [Cairn object-detection example](https://github.com/Arm-Examples/composable-ai-perception-object-detection). After it runs, you'll learn what Cairn provides and how the example uses it, before moving onto a more complex example.

## Prepare your development machine and target

Use Docker on both your development machine and the Pi. Start Docker on both machines and confirm that your user account can run Docker commands. If Docker isn't installed yet, see the [Docker installation guide](/install-guides/docker/).

{{% notice Note %}}
The commands use Bash. On Windows, run them inside a WSL 2 Linux distribution with Git and the Linux version of Topo installed there. Enable [Docker Desktop's WSL 2 integration](https://docs.docker.com/desktop/features/wsl/) for that distribution.
{{% /notice %}}

You will use Topo to deploy the object-detection example. To learn more about Topo, and how and why to use it, check out [Deploy containerized workloads to Arm-based Linux targets with Topo](https://learn.arm.com/learning-paths/cross-platform/deploy-containerized-workloads-with-topo/).

Install Topo [14.4.1](https://github.com/arm/topo/releases/tag/v14.4.1) on your development machine using its versioned installer. Skip the installation commands if you already have this version:

```bash
curl -fsSL https://raw.githubusercontent.com/arm/topo/v14.4.1/scripts/install.sh -o /tmp/topo-install.sh
sh /tmp/topo-install.sh --version v14.4.1 --path "$HOME/.local/bin"
export PATH="$HOME/.local/bin:$PATH"
```

Check the versions on your development machine:

```bash
topo --version
docker version
docker compose version
```

Confirm Topo reports `14.4.1`.

Connect your USB camera or Pi Camera module to the Raspberry Pi.

Set `CAIRN_TARGET` to your Pi's SSH destination by replacing `pi@raspberrypi.local`

```bash
export CAIRN_TARGET=pi@raspberrypi.local
```
Run a `topo health` check to confirm deployment prerequisites.
```bash
topo health --target "$CAIRN_TARGET"
```

Resolve failed health checks before deploying. 

{{% notice Note %}}
If the health check reports that key-based authentication isn't configured, run `topo setup-keys --target "$CAIRN_TARGET"`. Enter your Pi account's password when prompted to authorize the setup, then repeat the health check.
{{% /notice %}}

## Clone the object detection example

On your development machine, create a workspace and clone the example:

```bash
mkdir -p ~/cairn-lab
cd ~/cairn-lab
git clone https://github.com/Arm-Examples/composable-ai-perception-object-detection.git object-detection
cd object-detection
git checkout 6a995eaee273968864a5d59dcd3a4aa0800349dd
```

Select the supplied object-detection model through the example project's `OPK_HF_DETECTION_MODEL` parameter:

```bash
topo configure OPK_HF_DETECTION_MODEL=Arm/yolo26n-320-int8-onnx-raspberrypi5
```

## Deploy the example containers

Build and deploy from the `object-detection` directory:

```bash
topo deploy --target "$CAIRN_TARGET"
```

The first build downloads container images, Python dependencies, and the model package. Wait for Topo deployment to finish, then follow the console application's logs. Its Compose service is named `perception-example`:

```bash
topo logs --target "$CAIRN_TARGET" --follow perception-example
```

The application prints a result topic identifying its output channel, followed by a list of detections or `detections=none`. Each detection includes a label or class identifier and a confidence percentage.

## Verify that results follow the scene

Present an object the model recognizes, such as a person, glass, cup, phone, or chair. Observe its label in the logs, for example:

```output
perception-example-1  | result topic=cairn.perception.sessions.6fe56b9e-6a48-4a8b-9927-382e2215da8a.results detections=wine glass 95%
```

Press **Ctrl+C** to stop following logs.

## What you've accomplished and what's next

You've deployed the Cairn service stack together with a console example application that uses it, and verified that the application prints detection results from your camera. Next, learn what Cairn provides and how its services support the example.
