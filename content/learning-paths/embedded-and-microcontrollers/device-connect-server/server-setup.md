---
title: Run devices and an orchestrating agent on a Device Connect server
weight: 3

# FIXED, DO NOT MODIFY
layout: learningpathall
---

In this section you will use the hosted Device Connect service to provision a tenant, commission a simulated device with NATS JWT credentials, and verify it from a Python client. The hosted service runs the messaging router (NATS) and the registry for you, so the only thing you operate is the device itself and the agent that talks to it.

## Mint device and agent credentials from the Device Connect portal

The Device Connect portal is operated by Arm as a hosted developer service for the open-source [Device Connect](https://github.com/arm/device-connect) framework. Sign-in provisions a private **tenant** for your account, an isolated namespace on a hosted NATS messaging server, and lets you mint per-device and per-agent JWT credentials so your devices and AI agents can discover and invoke one another across networks. Only your account email and the cryptographic identities (device IDs, JWTs, public keys) you create on the portal are stored; the contents of messages your devices exchange are not stored, seen, or proxied. Treat each `.creds.json` you download like a private key, and do not put secrets, API keys, or personal data into device names or descriptions. For questions or issues, open one at [`arm/device-connect`](https://github.com/arm/device-connect/issues).

1. Open [`https://portal.deviceconnect.dev/`](https://portal.deviceconnect.dev/) and sign in. Signing in gives you a **tenant** — an isolated namespace on the shared Device Connect server that only the devices and agents you commission against it can join. Nothing from another tenant can see, publish to, or invoke anything in yours.
2. Open the **My Devices** section. The page header reads `Manage device credentials for tenant <slug>` — the value of `<slug>` is your **tenant slug** (for example, `beta`). The portal uses it to namespace every identity you create, so `sf-robot` on the `beta` tenant becomes `beta-sf-robot`. The NATS server URL is the same for every tenant: `nats://portal.deviceconnect.dev:4222`.
3. From the same **My Devices** page, add three identities. Type the short names below and the portal prefixes each one with your tenant slug automatically:
   - `sf-robot`: the San Francisco robot arm
   - `tokyo-robot`: the Tokyo robot arm
   - `bangalore-agent`: the orchestrating agent

For each identity, the portal exposes a **Download** button that gives you a NATS JWT credentials file named `<identity>.creds.json`. Treat each `.creds.json` file like a private key: anyone who has it can act as that identity on your tenant.

Export the tenant settings so the rest of the walkthrough can reuse them.

```bash
export TENANT=<tenant-slug>
export NATS_URL=nats://portal.deviceconnect.dev:4222
export MESSAGING_BACKEND=nats
```

Now save the downloaded credentials to a stable directory:

```bash
mkdir -p ~/.device-connect/credentials
mv ~/Downloads/${TENANT}-sf-robot.creds.json        ~/.device-connect/credentials/
mv ~/Downloads/${TENANT}-tokyo-robot.creds.json     ~/.device-connect/credentials/
mv ~/Downloads/${TENANT}-bangalore-agent.creds.json ~/.device-connect/credentials/
chmod 600 ~/.device-connect/credentials/*.creds.json
```

The agent-tools `connect()` function reads `TENANT` only when its `zone` argument is left unset, so always call it as `connect(zone=os.environ["TENANT"])` in the Python snippets below.

The portal also exposes a **Coding Agents** tab that can drive this whole step for you — pointing a coding agent (such as Claude Code or Codex) at it will provision identities and download the credentials on your behalf. The manual flow above is what the agent automates, and is useful to walk through once so you understand what the agent is doing.

## Install the SDKs

Create a virtual environment and install the edge runtime and the agent tools:

```bash
mkdir -p ~/device-connect-fabric && cd ~/device-connect-fabric
python3 -m venv .venv
source .venv/bin/activate
pip install device-connect-edge device-connect-agent-tools
```

You do not need `device-connect-server` locally; Fabric runs that for you in this case. If you would rather self-host, you can install it with `pip install device-connect-server` and run the router and registry yourself; see the [device-connect-server README](https://github.com/arm/device-connect/tree/main/packages/device-connect-server) for the Docker Compose deployment options.

## Write a simulated robot-arm driver

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

Point the runtime at the Fabric NATS server and at the device's `.creds.json` file. The combination of `NATS_URL` and `NATS_CREDENTIALS_FILE` is what turns the device from "an unauthenticated process" into "a commissioned member of your tenant":

```bash
NATS_URL=$NATS_URL \
  NATS_CREDENTIALS_FILE=~/.device-connect/credentials/${TENANT}-sf-robot.creds.json \
  python robot_arm.py --device-id ${TENANT}-sf-robot
```

On startup, the runtime presents its JWT to NATS, NATS verifies it against your tenant's signing key, and the device is allowed to publish, subscribe, and register itself. From this moment it shows up in the portal under your tenant, with its identity, capabilities, and live status.

The `--device-id` you pass on the command line must match the identity inside the credentials file (so `${TENANT}-sf-robot.creds.json` requires `--device-id ${TENANT}-sf-robot`).

In a second terminal, do the same for the Tokyo arm:

```bash
source ~/device-connect-fabric/.venv/bin/activate
NATS_URL=$NATS_URL \
  NATS_CREDENTIALS_FILE=~/.device-connect/credentials/${TENANT}-tokyo-robot.creds.json \
  python robot_arm.py --device-id ${TENANT}-tokyo-robot
```

You now have two commissioned devices on your tenant.

## Discover and invoke from Python

Open a third terminal and run a short client using the agent's credentials. This is the same `device-connect-agent-tools` API you would use from a Strands or LangChain agent. Agents authenticate to the same tenant in the same way devices do, just with a different `.creds.json` file:

```bash
source ~/device-connect-fabric/.venv/bin/activate
NATS_URL=$NATS_URL \
  MESSAGING_BACKEND=nats \
  TENANT=$TENANT \
  NATS_CREDENTIALS_FILE=~/.device-connect/credentials/${TENANT}-bangalore-agent.creds.json \
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

print(f"\nmove {tenant}-sf-robot to (0.2, 0.1, 0.3):")
print(invoke_device(f'{tenant}-sf-robot', 'move_to', x=0.2, y=0.1, z=0.3))

print(f"\nposition of {tenant}-tokyo-robot:")
print(invoke_device(f'{tenant}-tokyo-robot', 'get_position'))
PY
```

You should see both `sf-robot` and `tokyo-robot` listed, then each one home, then the SF arm move, then Tokyo's position read. The agent never needs to know which network the arms are on; it only needs the tenant's NATS URL and its own credentials.

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
NATS_URL=$NATS_URL \
  NATS_CREDENTIALS_FILE=~/.device-connect/credentials/${TENANT}-bangalore-agent.creds.json \
  TENANT=$TENANT \
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
- a Python client using `device-connect-agent-tools` to discover the arms and drive them through the server
- (optionally) a Strands agent coordinating both arms over the same mesh

This is the same shape of deployment you would use to put real robot arms, conveyors, cameras, or actuators on the mesh; only the driver code and the credential names change.
