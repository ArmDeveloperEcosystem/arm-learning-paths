---
title: Run devices and an orchestrating agent on a Device Connect server
weight: 3

# FIXED, DO NOT MODIFY
layout: learningpathall
---

## Provision your tenant and download NATS credentials

### Set up your Device Connect portal account

The Device Connect portal is operated by Arm as a hosted developer service for the open-source [Device Connect](https://github.com/arm/device-connect) framework. Signing in creates a private **tenant** for your account. A tenant is an isolated namespace on the shared Device Connect service: devices and agents commissioned to your tenant can discover and invoke each other, but other tenants can't see or use them.

{{% notice Note %}}
Only your account email and the cryptographic identities (device IDs, JWTs, public keys) you create on the portal are stored. The contents of messages your devices exchange aren't stored, seen, or proxied. Treat each `.creds.json` file like a private key, and don't put secrets, API keys, or personal data into device names or descriptions. For questions or issues, open one at [`arm/device-connect`](https://github.com/arm/device-connect/issues).
{{% /notice %}}

The portal page header shows your tenant slug in `Manage device credentials for tenant <slug>`. For a new account, the slug is your username. If your account has a different slug, use the value shown in the portal. The portal prefixes every device identity with this slug, so this Learning Path uses names such as `${TENANT}-device-001`.

New tenants include three device identities by default:

- `${TENANT}-device-001`
- `${TENANT}-device-002`
- `${TENANT}-device-003`

This Learning Path uses `device-001` for the Raspberry Pi 5 primary device, `device-002` for a secondary device on your development machine, and `device-003` for the Python client or AI agent. You can create your own device identities in the portal if you prefer, but using the default names lets you run the commands without editing.

{{% notice Note %}}
This Learning Path uses a Raspberry Pi 5 as the example primary device. You can use any device that can run the Device Connect Python packages, and you can also use your development machine as a simulated device by running the primary device, secondary device, and client in separate terminals.
{{% /notice %}}

### Download credentials from the portal

- Open [`https://portal.deviceconnect.dev/`](https://portal.deviceconnect.dev/) and sign in.
- Select **My Devices** and copy the tenant slug from the page header.
- Download the credentials for the three default identities: `device-001`, `device-002`, and `device-003`.

### Configure your environment

Export the tenant settings. Replace `<tenant-slug>` with your actual tenant slug from the portal.

```bash
export TENANT=<tenant-slug>
export NATS_URL=nats://portal.deviceconnect.dev:4222
export MESSAGING_BACKEND=nats
```

Now save the downloaded credentials to a stable directory. Store `${TENANT}-device-001.creds.json` on the Raspberry Pi 5 or whichever device you use as the primary device, and store `${TENANT}-device-002.creds.json` and `${TENANT}-device-003.creds.json` on your development machine. If you download all three files on your development machine, copy the `device-001` credential to the primary device before running the commands below. If you are simulating everything on your development machine, keep all three credentials there.

On the Raspberry Pi 5 or your chosen primary device:

```bash
mkdir -p ~/.device-connect/credentials
mv ~/Downloads/${TENANT}-device-001.creds.json ~/.device-connect/credentials/
chmod 600 ~/.device-connect/credentials/*.creds.json
```

On your development machine:

```bash
mkdir -p ~/.device-connect/credentials
mv ~/Downloads/${TENANT}-device-002.creds.json ~/.device-connect/credentials/
mv ~/Downloads/${TENANT}-device-003.creds.json ~/.device-connect/credentials/
chmod 600 ~/.device-connect/credentials/*.creds.json
```

Verify that the credential files are in place on each machine:

```bash
ls ~/.device-connect/credentials/
```

Across the two machines, you should have three `.creds.json` files, one for each device identity.

{{% notice Tip %}}The portal also exposes a **Coding Agents** tab that can download credentials on your behalf. The manual flow is useful to walk through once so you understand what the agent automates.{{% /notice %}}

## Install the Device Connect packages

Create a virtual environment and install the edge runtime and the agent tools on your primary device and your development machine:

```bash
mkdir -p ~/device-connect-fabric && cd ~/device-connect-fabric
python3 -m venv .venv
source .venv/bin/activate
pip install device-connect-edge device-connect-agent-tools
```

{{% notice Note %}}
Fabric is the hosted Device Connect service used by the portal. In this Learning Path, Fabric runs the NATS router and registry for you, so you don't install or run `device-connect-server` locally.

If you'd rather self-host, install `device-connect-server` with `pip install device-connect-server` and run the router and registry yourself. See the [device-connect-server README](https://github.com/arm/device-connect/tree/main/packages/device-connect-server) for the Docker Compose deployment options.
{{% /notice %}}

## Create the device driver

Create a file called `robot_arm.py` on both devices. This driver simulates a 6-DOF robot arm with three capabilities, and uses the same `DeviceDriver` shape you would use for a physical device attached to a Raspberry Pi 5 or another edge device:
- **RPCs**: `move_to()`, `home()`, and `get_position()` for controlling the arm
- **State tracking**: maintains current position
- **Events**: emits `motion_completed` after each move

```python
import argparse
import asyncio
import random

from device_connect_edge import DeviceRuntime
from device_connect_edge.drivers import DeviceDriver, emit, rpc
from device_connect_edge.types import DeviceIdentity, DeviceStatus


class RobotArmDriver(DeviceDriver):
    device_type = "robot_arm"

    def __init__(self, location: str):
        super().__init__()
        self._location = location
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
        return DeviceStatus(availability="available", location=self._location)

    @rpc()
    async def move_to(self, x: float, y: float, z: float) -> dict:
        # Simulate physical movement with a short delay
        await asyncio.sleep(random.uniform(0.2, 0.6))
        self._position = {"x": x, "y": y, "z": z}
        await self.motion_completed(target=self._position)
        return {"position": self._position}

    @rpc()
    async def home(self) -> dict:
        # Return to origin position
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
    parser.add_argument("--location", default="edge-device")
    args = parser.parse_args()

    # No allow_insecure=True - the runtime requires valid credentials
    runtime = DeviceRuntime(driver=RobotArmDriver(location=args.location), device_id=args.device_id)
    await runtime.run()


if __name__ == "__main__":
    asyncio.run(main())
```

The key detail: there's no `allow_insecure=True` parameter. The runtime will only join the mesh if it has valid credentials, which is what makes commissioning secure and meaningful.

The `--location` argument is only a label shown in discovery and status output. Use `raspberry-pi-5` for the example Raspberry Pi 5 flow, or choose another value such as `development-machine` when you run the primary device locally.

## Connect devices to the server

You'll run three processes: the example primary device, a secondary device on your development machine, and one Python client. Each needs its own terminal. If you do not have a separate device, run all three processes in separate terminals on your development machine.

### Terminal setup overview

| Machine | Terminal | Purpose | Credential |
|---------|----------|---------|------------|
| Raspberry Pi 5, another device, or development machine | 1 | Primary device | `${TENANT}-device-001.creds.json` |
| Development machine | 2 | Secondary device | `${TENANT}-device-002.creds.json` |
| Development machine | 3 | Python client | `${TENANT}-device-003.creds.json` |

### Configure each terminal

Open one terminal on the primary device and two terminals on your development machine. If you are simulating everything locally, open three terminals on your development machine. In each one, activate the virtual environment and set the tenant variables. Replace `<tenant-slug>` with your actual tenant slug.

```bash
cd ~/device-connect-fabric
source .venv/bin/activate
export TENANT=<tenant-slug>
export NATS_URL=nats://portal.deviceconnect.dev:4222
export MESSAGING_BACKEND=nats
```

Replace `<tenant-slug>` with the slug from the portal.

For each process, `NATS_URL` points at the hosted NATS server and `NATS_CREDENTIALS_FILE` selects the identity that process will use. The `--device-id` value must match the identity inside the credentials file.

### Start the primary device (Terminal 1)

On the Raspberry Pi 5, another device, or your development machine, run the primary device with its credential file:

```bash
NATS_CREDENTIALS_FILE=~/.device-connect/credentials/${TENANT}-device-001.creds.json \
  python robot_arm.py --device-id ${TENANT}-device-001 --location raspberry-pi-5
```

The runtime presents its JWT credential to NATS for authentication. NATS verifies the signature and allows the device to register. The device now appears in your portal with its identity, capabilities, and live status.

The output is similar to:

```output
2026-05-12 14:26:01,582 - device_connect_edge.device.<tenant-slug>-device-001 - INFO - Registering device
2026-05-12 14:26:01,761 - device_connect_edge.device.<tenant-slug>-device-001 - INFO - Device registered: registration_id=16d550ee-b287-41af-ac69-d3faabfc8178
2026-05-12 14:26:01,762 - device_connect_edge.device.<tenant-slug>-device-001 - INFO - Subscribed to commands on device-connect.<tenant-slug>.<tenant-slug>-device-001.cmd
```

If you see `Device registered`, the primary device is live on your tenant.

### Start the secondary device (Terminal 2)

On your development machine, run the same command with the second credential:

```bash
NATS_CREDENTIALS_FILE=~/.device-connect/credentials/${TENANT}-device-002.creds.json \
  python robot_arm.py --device-id ${TENANT}-device-002 --location development-machine
```

You should see similar registration output. Both devices are now commissioned and registered on your tenant.

## Discover and control devices (Terminal 3)

Now use the third credential on your development machine to run a Python client that discovers both devices and controls them remotely.

### Run the discovery and control script

This client uses the same `device-connect-agent-tools` API that Strands and LangChain agents use.

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

# Drive both devices through the server. The server routes each call to the right device.
for d in devices:
    print(f"\nhome on {d['device_id']}:")
    print(invoke_device(d['device_id'], 'home'))

print(f"\nmove {tenant}-device-001 to (0.2, 0.1, 0.3):")
print(invoke_device(f'{tenant}-device-001', 'move_to', {'x': 0.2, 'y': 0.1, 'z': 0.3}))

print(f"\nposition of {tenant}-device-002:")
print(invoke_device(f'{tenant}-device-002', 'get_position'))
PY
```

### Expected results

The script will:
- Discover both devices on your tenant
- Home both devices (move to origin)
- Move the primary device to a new position
- Read the secondary device's position

The client doesn't need to know which network the devices are on - it only needs the tenant's NATS URL and its credential.

Your output should end with:

```output
move <tenant-slug>-device-001 to (0.2, 0.1, 0.3):
{'success': True, 'result': {'position': {'x': 0.2, 'y': 0.1, 'z': 0.3}}}

position of <tenant-slug>-device-002:
{'success': True, 'result': {'x': 0.0, 'y': 0.0, 'z': 0.0}}
```

You've successfully orchestrated two devices across your tenant using the Device Connect server.

## (Optional) Attach a Strands AI agent

You can connect an AI agent to coordinate the devices through natural language.

### Install the Strands adapter

```bash
pip install "device-connect-agent-tools[strands]"
```

### Create the agent script

Create a file called `my_agent.py`:

```python
import asyncio
from device_connect_agent_tools.adapters.strands_agent import StrandsDeviceConnectAgent

async def main():
    agent = StrandsDeviceConnectAgent(
        goal="Coordinate the primary device and the secondary device: home them, then plan and execute moves on user request",
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

Stop the running terminals with `Ctrl-C`. Your tenant and credentials remain valid until you revoke them from the portal, so there's nothing on your machine to clean up beyond the virtual environment:

```bash
deactivate
rm -rf ~/device-connect-fabric/.venv
```

To rotate credentials, regenerate them from the portal and replace the `.creds.json` files. Old credentials are revoked the moment new ones are issued.

## What you've built

You now have a working Device Connect deployment with a hosted server in the loop:

- a hosted NATS router and persistent registry on your tenant
- a commissioned primary device and a commissioned secondary device, each authenticated by its own JWT credential
- a third credential used by a Python client with `device-connect-agent-tools` to discover the devices and drive them through the server
- (optionally) a Strands agent coordinating both devices over the same mesh

This is the same shape of deployment you would use to put real robot arms, conveyors, cameras, or actuators on the mesh; only the driver code and the credential names change.
