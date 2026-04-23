---
title: Set up D2D communication between a sensor and a monitor
weight: 4

# FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section you'll build two simulated devices on the same mesh:

- a **sensor** that publishes temperature and humidity readings on a schedule
- a **threshold monitor** that subscribes to those readings and raises an alert when the temperature crosses a configurable threshold

This mirrors a real edge scenario, a room supervisor watching environmental sensors for out-of-bounds conditions, and exercises every Device Connect primitive across two cooperating devices.

## Install uv

This walkthrough uses [uv](https://docs.astral.sh/uv/) to manage the project and its Python dependencies. uv will resolve a compatible Python interpreter, create a virtual environment, and install packages for you, so no manual `venv` or `pip` steps are needed.

If you do not already have uv installed, run the official installer for your platform:

```bash
# macOS or Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```powershell
# Windows PowerShell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Alternative install methods (Homebrew, pipx, and others) are listed in the [uv installation docs](https://docs.astral.sh/uv/getting-started/installation/). Verify the install with:

```bash
uv --version
```

## Create the project

Create a new project and add the Device Connect packages:

```bash
mkdir ~/device-connect-d2d
cd ~/device-connect-d2d
uv init --python 3.11
uv add device-connect-edge device-connect-agent-tools
```

The [`device-connect-edge`](https://pypi.org/project/device-connect-edge/) package is the device runtime SDK. It is what turns a Python class into a live peer on the messaging mesh. The [`device-connect-agent-tools`](https://pypi.org/project/device-connect-agent-tools/) package is the client side: it lets an agent or script discover devices and invoke their RPCs. In production you might consume devices from a different client, but for this walkthrough it is the fastest way to confirm that discovery and RPC are working.

## Write a simulated sensor device

Create a file called `sensor.py`:

```python
import argparse
import asyncio
import random

from device_connect_edge import DeviceRuntime
from device_connect_edge.drivers import DeviceDriver, emit, periodic, rpc
from device_connect_edge.types import DeviceIdentity, DeviceStatus


class SimulatedSensor(DeviceDriver):
    device_type = "simulated_sensor"

    def __init__(self):
        super().__init__()
        self._last = {"temperature": 24.0, "humidity": 45.0}

    @property
    def identity(self) -> DeviceIdentity:
        return DeviceIdentity(
            device_type="simulated_sensor",
            manufacturer="Device Connect",
            model="SIM-TH-100",
            description="Simulated temperature and humidity sensor",
        )

    @property
    def status(self) -> DeviceStatus:
        return DeviceStatus(availability="available", location="simulator")

    @rpc()
    async def get_reading(self) -> dict:
        return self._last

    @emit()
    async def reading_ready(self, temperature: float, humidity: float):
        return None

    @periodic(interval=5.0)
    async def publish_reading(self):
        self._last = {
            "temperature": round(random.uniform(22.0, 30.0), 1),
            "humidity": round(random.uniform(35.0, 55.0), 1),
        }
        print(f"publishing {self._last}")
        await self.reading_ready(**self._last)


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device-id", required=True)
    args = parser.parse_args()

    runtime = DeviceRuntime(
        driver=SimulatedSensor(),
        device_id=args.device_id,
        allow_insecure=True,
    )
    await runtime.run()


if __name__ == "__main__":
    asyncio.run(main())
```

This driver uses three of the decorators introduced in the overview:

- `@rpc` exposes `get_reading` as a function that other peers or agents can call
- `@emit` declares `reading_ready` as an event the device publishes to the mesh
- `@periodic` runs `publish_reading` every five seconds so the sensor produces fresh data on its own

The `identity` and `status` properties are what other peers see during discovery. They are how this device advertises itself as a `simulated_sensor` with a known manufacturer, model, and availability.

## Write a threshold monitor device

Now create a second device that consumes the sensor's data. Create a file called `monitor.py`:

```python
import argparse
import asyncio
from collections import deque

from device_connect_edge import DeviceRuntime
from device_connect_edge.drivers import DeviceDriver, emit, on, rpc
from device_connect_edge.types import DeviceIdentity, DeviceStatus


class ThresholdMonitor(DeviceDriver):
    device_type = "threshold_monitor"

    def __init__(self, threshold: float):
        super().__init__()
        self._threshold = threshold
        self._recent_alerts: deque = deque(maxlen=10)

    @property
    def identity(self) -> DeviceIdentity:
        return DeviceIdentity(
            device_type="threshold_monitor",
            manufacturer="Device Connect",
            model="MON-T-100",
            description="Temperature threshold monitor",
        )

    @property
    def status(self) -> DeviceStatus:
        return DeviceStatus(availability="available", location="simulator")

    @on(event_name="reading_ready")
    async def on_reading(self, device_id: str, event_name: str, payload: dict):
        temperature = payload["temperature"]
        print(f"received {temperature} C from {device_id}")
        if temperature > self._threshold:
            alert = {"device_id": device_id, "temperature": temperature}
            self._recent_alerts.append(alert)
            print(f"ALERT: {device_id} at {temperature} C (threshold {self._threshold})")
            await self.alert_raised(**alert)

    @emit()
    async def alert_raised(self, device_id: str, temperature: float):
        return None

    @rpc()
    async def get_recent_alerts(self) -> list:
        return list(self._recent_alerts)


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device-id", required=True)
    parser.add_argument("--threshold", type=float, default=27.0)
    args = parser.parse_args()

    runtime = DeviceRuntime(
        driver=ThresholdMonitor(threshold=args.threshold),
        device_id=args.device_id,
        allow_insecure=True,
    )
    await runtime.run()


if __name__ == "__main__":
    asyncio.run(main())
```

The monitor adds one primitive you haven't seen yet:

- `@on(event_name="reading_ready")` subscribes to `reading_ready` events from any device on the mesh. Whenever the sensor emits, the runtime delivers the event to `on_reading` as a method call with three arguments: the source device id, the event name, and a payload dict carrying the emitted fields. This is device-to-device communication without either side knowing the other's address. You can also narrow the subscription by `device_id=` or `device_type=`; the `device_type` filter matches when the source device id starts with `{device_type}-`.
- `@emit alert_raised` lets the monitor publish its own events when a threshold is crossed, so another peer or agent could subscribe to alerts in turn.
- `@rpc get_recent_alerts` exposes the monitor's recent history so an external caller can query what it has seen.

## Run the sensor and the monitor

Open two terminals in the project directory (`~/device-connect-d2d`). In terminal 1, start the sensor:

```bash
uv run python sensor.py --device-id sensor-001
```

In terminal 2, start the monitor with a threshold below the sensor's typical temperature range so you see alerts quickly:

```bash
uv run python monitor.py --device-id monitor-001 --threshold 27.0
```

`uv run` executes the command inside the project's managed environment, so you do not need to activate a virtual environment manually.

Within a few seconds, the monitor terminal should start printing `received ... from sensor-001` lines, and an `ALERT:` line each time the simulated temperature rises above 27.0 °C. This is the sensor invoking the monitor across the mesh through its emitted event, and you did not configure any address or pairing between them.

## Query the monitor from agent tools

Open a third terminal in the project directory and run:

```bash
uv run python - <<'PY'
from device_connect_agent_tools import connect, discover_devices, invoke_device

connect()

devices = discover_devices()
print(f"Found {len(devices)} device(s)")
for device in devices:
    print(f"  {device['device_id']} ({device['device_type']})")

sensor_id = next(d["device_id"] for d in devices if d["device_type"] == "simulated_sensor")
monitor_id = next(d["device_id"] for d in devices if d["device_type"] == "threshold_monitor")

print("latest reading:", invoke_device(sensor_id, "get_reading"))
print("recent alerts:", invoke_device(monitor_id, "get_recent_alerts"))
PY
```

The script discovers both devices, invokes `get_reading` on the sensor, and invokes `get_recent_alerts` on the monitor. The alert list should contain every breach the monitor has observed since it started.

## What happened

You have exercised every Device Connect primitive across two cooperating devices:

- **Discovery**: the monitor found the sensor by `device_type` automatically, and `discover_devices` from agent tools found both peers
- **RPC**: agent tools called `get_reading` on the sensor and `get_recent_alerts` on the monitor
- **Events**: the sensor emitted `reading_ready`; the monitor reacted through `@on` and emitted its own `alert_raised`
- **Status**: both runtimes advertised themselves as `available` through the `status` property

The sensor and monitor did not know about each other before they started. They found each other on the local network and communicated purely through typed events and RPCs, with no broker, no registry, and no cloud service.

## Outcome

You now have a working D2D deployment where two simulated devices cooperate on the same mesh: a sensor that publishes data and a monitor that reacts to it and exposes its own state. This same driver pattern (a class, a handful of decorators, and a runtime) is how you would describe a real sensor, actuator, or monitor on the network.
