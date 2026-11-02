---
title: "Package the Linux telemetry bridge"
description: Prepare offline AArch64 SDK dependencies and understand UART validation, Greengrass IPC, and bridge cleanup.
weight: 5
layout: "learningpathall"
---

## Follow the bridge data flow

`components/bridge.py` opens the dedicated Linux MAIN_UART0 port at 115200 8N1, reads newline-delimited frames, and accepts only the `pb2.external.temperature` schema. It checks integer types, counter signs, and the sensor's temperature range, bounds UART buffering, and ignores boot banners and error messages.

For each valid frame it calls Greengrass IPC `PublishToIoTCore`, with QoS 1 and this exact topic:

```text
ti/pocketbeagle2/temperature/external
```

An illustrative published message is:

```json
{
  "schemaVersion": 1,
  "thingName": "MyPocketBeagle2",
  "sensor": "BMP280",
  "location": "external",
  "temperatureC": 25.08,
  "sequence": 12,
  "mcuUptimeMs": 60320,
  "linuxBootId": "698a3054-59a4-4b6f-a4e3-bcf329b9d75a",
  "timestamp": "2026-10-29T18:00:00.123+00:00"
}
```

`timestamp` is Linux's UTC receipt time, not an MCU wall clock. Keep the board's clock synchronized as in Part 1. `sequence` and `mcuUptimeMs` restart when the M4 restarts; `linuxBootId` identifies the Linux boot. QoS 1 can deliver duplicates. The bridge logs publish failures and drops the affected samples, then attempts later samples again. This exercise provides live monitoring without a persistent offline queue or a lossless-delivery promise.

The bridge uses the [AWS IoT Device SDK for Python v2](https://github.com/aws/aws-iot-device-sdk-python-v2/tree/v1.26.0), pinned here as `awsiotsdk==1.26.0`, with its required `awscrt==0.28.1`. Greengrass provides the IPC socket and component authentication environment. The [MQTT IPC authorization guide](https://docs.aws.amazon.com/greengrass/v2/developerguide/ipc-iot-core-mqtt.html) defines the recipe's topic-limited `aws.greengrass.ipc.mqttproxy` permission.

## Stage both components

On the Ubuntu host, use the source workspace and the new ELF:

```bash
cd "$HOME/pb2-temperature-part3"
sh tools/stage.sh \
  "$HOME/pb2-zephyr-workspace/build/pb2-external-temperature/zephyr/zephyr.elf" 312
find staging -type f -print
```

The script downloads wheels for **Linux AArch64 and Python 3.12**, even when the build host is x86_64. It must produce an AArch64 `awscrt` wheel and a universal `awsiotsdk` wheel. Do not ship an x86_64 native wheel to the board or allow the component to compile a dependency during installation.

The directory structure is:

```text
staging/
  com.arm.PocketBeagle2.ZephyrExternalTemperature/1.0.0/
    firmware_manager.py
    zephyr.elf
  com.arm.PocketBeagle2.ExternalTemperatureBridge/1.0.0/
    bridge.py
    bridge_lifecycle.sh
    awsiotsdk-1.26.0-....whl
    awscrt-0.28.1-...aarch64.whl
```

If Python differs on your image, rebuild the wheel selection for that interpreter and verify it on the target before deployment. The example assumes the unchanged Part 1 Scarthgap image's Python 3.12 and glibc environment.

## Understand offline installation and cleanup

Greengrass downloads each declared artifact from S3 **before** `install`. The bridge install script runs pip with `--no-index`, `--no-cache-dir`, `--find-links {artifacts:path}`, and a private `--target {work:path}/installed-<digest>`. Its digest covers the bridge, lifecycle script, and wheels so different versions can be staged independently. The board requires S3 access, but no PyPI access during deployment. Python, pip, and standard library modules come from the existing Yocto image.

The foreground `run` supervisor starts the bridge in its own component control group. On normal SIGTERM it waits for Python to close the UART and IPC client, then removes the installed Python directory. The next start can rebuild that directory from the cached artifacts. It installs no separately enabled service, credential copy, or global Python package.

Both bridge phases request root in this development example for direct serial-device access. For a production image, set up an appropriate device group and use an unprivileged bridge user; retain privilege only for the remoteproc operations that require it.

The two custom components have no dependency on one another. They can be removed separately: removing the bridge leaves sensing on the M4; removing the firmware leaves a bridge that reports missing samples. Deploy and remove them together for the full exercise. Their startup order is immaterial because the MCU sends repeatedly and the bridge tolerates a quiet UART.

## What you have learned

You have learned how the Linux bridge validates MCU UART frames, converts them into JSON, and publishes them through Greengrass IPC to the required IoT Core topic. You can package the bridge with compatible AArch64 wheels for offline installation and explain its timestamp, delivery, and cleanup behavior.
