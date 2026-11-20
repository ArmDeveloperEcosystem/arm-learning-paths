---
title: "NXP FRDM i.MX 8M Plus: Package the RPMsg-to-IoT-Core bridge"
description: "Prepare offline dependencies and a foreground Linux telemetry bridge."
weight: 5
layout: "learningpathall"
---

## Introduction to the RPMsg-to-IoTCore relay/bridge

Within the bridge code, `components/bridge.py` waits for `/dev/nxp-temperature`, opens the RPMsg TTY in raw mode, and sends a host greeting to establish its endpoint address. It accepts only newline-delimited `nxp.external.temperature` schema-1 frames with valid integer fields and BMP280-range values. It publishes each accepted sample through Greengrass IPC `PublishToIoTCore`, with QoS 1, to **`nxp/imx8mplus/temperature/external`**. The boards existing Greengrass environment, by default, supplies and manages the MQTT/TLS authentication for the bridge into AWS IoTCore.

JSON messages published to AWS IoTCore will resemble this:
```json
{"schemaVersion":1,"thingName":"MyNXPIMX8MPlus","sensor":"BMP280","location":"external","temperatureC":25.08,"sequence":12,"mcuUptimeMs":60320,"linuxBootId":"example-boot-id","timestamp":"2026-10-29T18:00:00.123+00:00"}
```

The timestamp is Linux's UTC receipt time. Sequence and MCU uptime restart with the firmware; QoS 1 can duplicate deliveries. Publish failures are logged and the affected sample is dropped.

## Build and stage our artifacts for the bridge

On the Ubuntu host, type:

```bash
source "$HOME/nxp-imx8uplus-zephyr-venv/bin/activate"
cd "$HOME/nxp-imx8uplus-temperature-part3"
sh tools/stage.sh build/temperature/zephyr/zephyr.elf 313
find staging -type f -print
```

Replace `313` with the board's actual python interpreter version if different (should not need to be changed though). The script downloads `awsiotsdk==1.26.0` and its pinned `awscrt==0.28.1` wheel for Linux AArch64, independent of the build host's architecture.

Before staging, the script runs the ELF inspector using the Zephyr virtual
environment's `pyelftools`. An old failing ELF is rejected before artifacts are
copied. The firmware component has three artifacts: ELF, manager and Linux
preflight helper. The bridge has four: source, lifecycle script, universal SDK wheel, and AArch64 CRT wheel.

The component version comes from `release.json` (currently `1.0.1`). Staging,
recipe generation and the deployment page use that same value. Keep earlier
staged versions for rollback; the uploader selects only the current plan.

## Understand the AWS Greengrass component install, run, and removal

Greengrass downloads S3 artifacts before the install phase. The bridge install script uses `pip --no-index --no-cache-dir --find-links` and a private digest-named target directory under component work storage. Python and pip come from the Part 1 image.

The foreground run supervisor starts Python, keeps it in the component control group, and handles termination. Python closes its RPMsg TTY and IPC client; the supervisor removes the private installed directory. It can reinstall from immutable artifacts on the next run. The firmware manager uses a different endpoint for stop control.

The recipes run with root privileges in this development image to access serial and remoteproc resources. A production image should grant the bridge a suitable device group and reserve root only for operations that require it.

## What you have learned

You can explain the bridge's RPMsg greeting and schema design as well as build/stage our bridge for inclusion into an AWS IoT Greengrass custom component.