---
title: Run devices and an orchestrating agent on a Device Connect server
weight: 3

# FIXED, DO NOT MODIFY
layout: learningpathall
---

## Setup of Device Connect portal

The Device Connect portal is operated by Arm as a hosted developer service for the open-source [Device Connect](https://github.com/arm/device-connect) framework. Signing in creates a private **tenant** for your account. A tenant is an isolated namespace on the shared Device Connect service: devices and agents commissioned to your tenant can discover and invoke each other, but other tenants cannot see or use them.

Only your account email and the cryptographic identities (device IDs, JWTs, public keys) you create on the portal are stored. The contents of messages your devices exchange are not stored, seen, or proxied. Treat each `.creds.json` file like a private key, and do not put secrets, API keys, or personal data into device names or descriptions. For questions or issues, open one at [`arm/device-connect`](https://github.com/arm/device-connect/issues).

The portal page header shows your tenant slug in `Manage device credentials for tenant <slug>`. For a new account, the slug is your username. If your account has a different slug, use the value shown in the portal. The portal prefixes every device identity with this slug, so this Learning Path uses names such as `${TENANT}-device-001`.

New tenants include three device identities by default:

- `${TENANT}-device-001`
- `${TENANT}-device-002`
- `${TENANT}-device-003`

This Learning Path uses `device-001` and `device-002` for the simulated robot arms, and `device-003` for the Python client or AI agent. You can create your own device identities in the portal if you prefer, but using the default names lets you run the commands below without editing the device names.

1. Open [`https://portal.deviceconnect.dev/`](https://portal.deviceconnect.dev/) and sign in.
2. Open **My Devices** and copy the tenant slug from the page header.
3. Download the credentials for the three default identities.

Export the tenant settings so the rest of the walkthrough can reuse them. Replace `<tenant-slug>` with the slug from the portal.

```bash
export TENANT=<tenant-slug>
export NATS_URL=nats://portal.deviceconnect.dev:4222
export MESSAGING_BACKEND=nats
```

Now save the downloaded credentials to a stable directory:

```bash
mkdir -p ~/.device-connect/credentials
mv ~/Downloads/${TENANT}-device-001.creds.json ~/.device-connect/credentials/
mv ~/Downloads/${TENANT}-device-002.creds.json ~/.device-connect/credentials/
mv ~/Downloads/${TENANT}-device-003.creds.json ~/.device-connect/credentials/
chmod 600 ~/.device-connect/credentials/*.creds.json
```

Verify that all three credential files are in place:

```bash
ls ~/.device-connect/credentials/
```

The portal also exposes a **Coding Agents** tab that can download credentials on your behalf. The manual flow above is useful to walk through once so you understand what the agent automates.

## Install the Device Connect packages

Create a virtual environment and install the edge runtime and the agent tools:

```bash
mkdir -p ~/device-connect-fabric && cd ~/device-connect-fabric
python3 -m venv .venv
source .venv/bin/activate
pip install device-connect-edge device-connect-agent-tools
```

{{% notice Note %}}
Fabric is the hosted Device Connect service used by the portal. In this Learning Path, Fabric runs the NATS router and registry for you, so you do not install or run `device-connect-server` locally.

If you would rather self-host, install `device-connect-server` with `pip install device-connect-server` and run the router and registry yourself. See the [device-connect-server README](https://github.com/arm/device-connect/tree/main/packages/device-connect-server) for the Docker Compose deployment options.
{{% /notice %}}

## Create a simulated robot arm 

Create a file called `robot_arm.py`. The driver pretends to be a 6-DOF robot arm: it exposes RPCs for moving to a target pose and homing, tracks its current position, and emits a `motion_completed` event after every move.

```python
import argparse
import asyncio
import random

from device_connect_edge import DeviceRuntime
from device_connect_edge.drivers import DeviceDriver, emit, rpc
from device_connect_edge.types import DeviceIdentity, DeviceStatus


class RobotArmDriver(DeviceDriver):
    device_type = "robot_arm"

    def __init__(self):
        super().__init__()
        self._position = {"x": 0.0, "y": 0.0, "z": 0.0}

    @property
    def identity(self) -> DeviceIdentity:
        return DeviceIdentity(
            device_type="robot_arm",
            manufacturer="Device Connect",
            model="SIM-ARM-6DOF",
            description="Simulated 6-DOF robot arm",
        )

    @property
    def status(self) -> DeviceStatus:
        return DeviceStatus(availability="available", location="simulator")

    @rpc()
    async def move_to(self, x: float, y: float, z: float) -> dict:
        # pretend to physically traverse to the target
        await asyncio.sleep(random.uniform(0.2, 0.6))
        self._position = {"x": x, "y": y, "z": z}
        await self.motion_completed(target=self._position)
        return {"position": self._position}

    @rpc()
    async def home(self) -> dict:
        return await self.move_to(0.0, 0.0, 0.0)

    @rpc()
    async def get_position(self) -> dict:
        return self._position

    @emit()
    async def motion_completed(self, target: dict):
        return None


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--device-id", required=True)
    args = parser.parse_args()

    runtime = DeviceRuntime(driver=RobotArmDriver(), device_id=args.device_id)
    await runtime.run()


if __name__ == "__main__":
    asyncio.run(main())
```

Note that there is no `allow_insecure=True` on the runtime. The runtime will only join the mesh if it has valid credentials, which is what makes commissioning meaningful.

## Connect the device to the server

You will use three terminals: two for simulated devices and one for the Python client. Each terminal must have the virtual environment active and the shared tenant enviroment variables exported.

| Terminal | Purpose | Credential |
|----------|---------|------------|
| 1 | First simulated robot arm | `${TENANT}-device-001.creds.json` |
| 2 | Second simulated robot arm | `${TENANT}-device-002.creds.json` |
| 3 | Python client or AI agent | `${TENANT}-device-003.creds.json` |

In every new terminal, run:

```bash
cd ~/device-connect-fabric
source .venv/bin/activate
export TENANT=<tenant-slug>
export NATS_URL=nats://portal.deviceconnect.dev:4222
export MESSAGING_BACKEND=nats
```

Replace `<tenant-slug>` with the slug from the portal.

For each process, `NATS_URL` points at the hosted NATS server and `NATS_CREDENTIALS_FILE` selects the identity that process will use. The `--device-id` value must match the identity inside the credentials file.

In terminal 1, start the first simulated robot arm:

```bash
NATS_CREDENTIALS_FILE=~/.device-connect/credentials/${TENANT}-device-001.creds.json \
  python robot_arm.py --device-id ${TENANT}-device-001
```

On startup, the runtime presents its JWT to NATS. NATS verifies it against your tenant's signing key, and the device is allowed to publish, subscribe, and register itself. From this moment it shows up in the portal under your tenant, with its identity, capabilities, and live status.

The output should look like:

```output
2026-05-12 14:26:01,582 - device_connect_edge.device.<tenant-slug>-device-001 - INFO - Registering device
2026-05-12 14:26:01,761 - device_connect_edge.device.<tenant-slug>-device-001 - INFO - Device registered: registration_id=16d550ee-b287-41af-ac69-d3faabfc8178
2026-05-12 14:26:01,762 - device_connect_edge.device.<tenant-slug>-device-001 - INFO - Subscribed to commands on device-connect.<tenant-slug>.<tenant-slug>-device-001.cmd
```

In terminal 2, start the second simulated robot arm:

```bash
NATS_CREDENTIALS_FILE=~/.device-connect/credentials/${TENANT}-device-002.creds.json \
  python robot_arm.py --device-id ${TENANT}-device-002
```

The output should be similar to that in the first terminal. You now have two commissioned devices on your tenant.

## Discover and invoke from Python

In terminal 3, run a short client with the third credential. This is the same `device-connect-agent-tools` API you would use from a Strands or LangChain agent.

The agent-tools `connect()` function reads `TENANT` only when its `zone` argument is left unset, so call it as `connect(zone=os.environ["TENANT"])` in the Python snippets below.

```bash
NATS_CREDENTIALS_FILE=~/.device-connect/credentials/${TENANT}-device-003.creds.json \
  python - <<'PY'
import os
from device_connect_agent_tools import connect, discover_devices, invoke_device

tenant = os.environ["TENANT"]
connect(zone=tenant)

devices = discover_devices()
print(f"Found {len(devices)} device(s) on tenant")
for d in devices:
    print(f"  {d['device_id']:24} {d['device_type']:20} {d.get('status', {}).get('availability', '?')}")

# Drive both arms through the server. The server routes each call to the right device.
for d in devices:
    print(f"\nhome on {d['device_id']}:")
    print(invoke_device(d['device_id'], 'home'))

print(f"\nmove {tenant}-device-001 to (0.2, 0.1, 0.3):")
print(invoke_device(f'{tenant}-device-001', 'move_to', {'x': 0.2, 'y': 0.1, 'z': 0.3}))

print(f"\nposition of {tenant}-device-002:")
print(invoke_device(f'{tenant}-device-002', 'get_position'))
PY
```

You should see `${TENANT}-device-001` and `${TENANT}-device-002` listed, then each one home, then the first arm move, then the second arm's position read. The client never needs to know which network the arms are on; it only needs the tenant's NATS URL and its own credentials. Your output should end with confirmation that one of the device positions has been updated:

```output
move <tenant-slug>-device-001 to (0.2, 0.1, 0.3):
{'success': True, 'result': {'position': {'x': 0.2, 'y': 0.1, 'z': 0.3}}}

position of <tenant-slug>-device-002:
{'success': True, 'result': {'x': 0.0, 'y': 0.0, 'z': 0.0}}
```

## (Optional) Attach a Strands AI agent

`device-connect-agent-tools` ships an adapter that turns the same Device Connect mesh into a Strands tool surface:

```bash
pip install "device-connect-agent-tools[strands]"
```

```python
import asyncio
from device_connect_agent_tools.adapters.strands_agent import StrandsDeviceConnectAgent

async def main():
    agent = StrandsDeviceConnectAgent(
        goal="Coordinate the two robot arms: home them, then plan and execute moves on user request",
        model_id="claude-sonnet-4-20250514",
    )
    async with agent:
        await agent.run()

asyncio.run(main())
```

Run it with the agent's credentials and an Anthropic API key:

```bash
NATS_CREDENTIALS_FILE=~/.device-connect/credentials/${TENANT}-device-003.creds.json \
  ANTHROPIC_API_KEY="sk-ant-..." \
  python my_agent.py
```

The agent subscribes to events on your tenant, batches them over a short window, and prompts Claude to react. Claude can call back into devices using `invoke_device()` and `get_device_status()`.

## Tear down

Stop the running terminals with `Ctrl-C`. Your tenant and credentials remain valid until you revoke them from the portal, so there is nothing on your machine to clean up beyond the virtual environment:

```bash
deactivate
rm -rf ~/device-connect-fabric/.venv
```

To rotate credentials, regenerate them from the portal and replace the `.creds.json` files. Old credentials are revoked the moment new ones are issued.

## What you've built

You now have a working Device Connect deployment with a hosted server in the loop:

- a hosted NATS router and persistent registry on your tenant
- two commissioned simulated robot arms, each authenticated by its own JWT credential
- a third credential used by a Python client with `device-connect-agent-tools` to discover the arms and drive them through the server
- (optionally) a Strands agent coordinating both arms over the same mesh

This is the same shape of deployment you would use to put real robot arms, conveyors, cameras, or actuators on the mesh; only the driver code and the credential names change.
