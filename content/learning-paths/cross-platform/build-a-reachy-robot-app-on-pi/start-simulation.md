---
title: Start the Reachy simulation on MuJoCo
description: Set up a Python 3.12 simulation environment, start the Reachy Mini MuJoCo daemon, and find the host IP address for Raspberry Pi connections.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## What is MuJoCo?

MuJoCo is an open-source physics engine from Google DeepMind, used for simulating articulated bodies such as robots. It can model joints, contacts, gravity, and rigid-body dynamics, which makes it useful for robotics prototyping, control development, reinforcement learning, and safety testing before hardware is available.

In this project, you'll use MuJoCo to see Reachy Mini move without owning a physical
Reachy. It's not a perfect replacement for hardware: real cameras, lighting,
network latency, calibration, mechanical tolerances, and safety constraints
still matter. MuJoCo is best treated as a fast development and validation tool
before moving to physical testing.

## Create or activate a simulation environment

The simulation host doesn't need the full `reachy_gladiator_lp` project. It needs only the Reachy Mini SDK with MuJoCo support and the `start_sim.sh`
launcher script.

### Set up Python environment

Python 3.12 is required for the simulation environment. Python 3.13 can cause dependency resolution failures because pre-built wheels for some SDK dependencies are not yet available for that version. 

Check your Python version:

```bash
python3 --version
```

If Python 3.12 isn't installed, install it by using one of the following commands. On macOS, install Python 3.12 with [Homebrew](https://brew.sh). On Ubuntu or WSL2, use `apt`:

{{< tabpane code=true >}}
  {{< tab header="macOS" language="bash">}}
brew install python@3.12
  {{< /tab >}}
  {{< tab header="Ubuntu or WSL2" language="bash">}}
sudo apt install python3.12 python3.12-venv
  {{< /tab >}}
{{< /tabpane >}}

After ensuring you have Python 3.12 installed, on the machine that will run the simulation, create a small workspace and a Python virtual environment:

```bash
mkdir -p ~/reachy_projects/reachy_sim/scripts
cd ~/reachy_projects/reachy_sim
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install the Reachy Mini SDK with the MuJoCo simulation dependencies:

```bash
python -m pip install --upgrade "reachy-mini[mujoco]"
```

The `mujoco` extra is required for `--sim`. If you install only `reachy-mini`, the daemon can start but simulation fails with `MuJoCo is not installed`.

If you already have a working Reachy Mini simulation environment, you can activate that environment instead.

Download the simulation launcher script from the [reachy_gladiator_lp repository](https://github.com/matt-cossins/reachy_gladiator_lp):

```bash
curl -L https://raw.githubusercontent.com/matt-cossins/reachy_gladiator_lp/main/scripts/start_sim.sh -o scripts/start_sim.sh
chmod +x scripts/start_sim.sh
```

`curl` is available by default on macOS and is commonly available on Linux and
WSL distributions. If your Linux environment doesn't include it, install it
with your package manager.

## Start the Reachy Mini simulation

Start the daemon and MuJoCo simulation from the simulation workspace:

```bash
cd ~/reachy_projects/reachy_sim
source .venv/bin/activate
REACHY_SIM_PORT=18000 ./scripts/start_sim.sh
```

The simulation can take several minutes to start up. When the simulation is ready, the output is similar to:

```output
reachy_mini.daemon.daemon - INFO - Daemon started successfully.
uvicorn.error - INFO - Application startup complete.
uvicorn.error - INFO - Uvicorn running on http://0.0.0.0:18000 (Press CTRL+C to quit)
reachy_mini.utils.discovery - INFO - mDNS service registered: reachy_mini on port 18000
reachy_mini.media.media_server - INFO - Pipeline latency (live=True, min_latency=30000000, max_latency=1200000000)
```

Leave this terminal running after it completes and boots the simulation view.

![MuJoCo physics simulation window showing the Reachy Mini robot in a standing position, confirming the simulation started successfully#center](mujoco.png "MuJoCo simulation window with Reachy Mini")

The script starts the Reachy Mini daemon with simulation enabled, binds FastAPI to `0.0.0.0`, and disables localhost-only mode so the Raspberry Pi can connect. In this Learning Path, you'll use port `18000`.

The daemon is the network boundary between the Pi app and the simulated robot.
The Pi doesn't run MuJoCo. It connects to this daemon and sends the same SDK
motion commands that it would send to a physical Reachy daemon.

The script runs a command equivalent to:

```bash
mjpython -m reachy_mini.daemon.app.main \
  --sim \
  --fastapi-host 0.0.0.0 \
  --fastapi-port 18000 \
  --no-localhost-only
```

On macOS, `mjpython` is often needed because MuJoCo opens a native graphics
window. On Linux, regular `python` is usually enough. The provided script picks
an appropriate runtime when it can.

### Troubleshoot the simulation

If the script reports that address `0.0.0.0:18000` is already in use, another daemon or server is already using port `18000`. 

Find the process:

```bash
lsof -nP -iTCP:18000 -sTCP:LISTEN
```

If the process is an old Reachy daemon, stop it with `Ctrl+C` in its terminal. If you need to terminate it from the command line, replace `<pid>` with the process ID from `lsof`:

```bash
kill <pid>
```

You can also run the simulation on a different port:

```bash
REACHY_SIM_PORT=18001 ./scripts/start_sim.sh
```

If you change the simulation port, use the same port when configuring the Pi app later:

```bash
REACHY_GLADIATOR_DAEMON_PORT=18001 ./scripts/run_pi_app.sh <simulation-host-ip>
```

## Find the simulation host IP address

Use the tab for your simulation host operating system.

{{% notice Note %}}
On macOS, `en0` is usually Wi-Fi. If you use Ethernet or another network interface, the device name might be different.
{{% /notice %}}

{{< tabpane code=true >}}
  {{< tab header="macOS" language="bash">}}
ipconfig getifaddr en0
  {{< /tab >}}
  {{< tab header="Linux" language="bash">}}
hostname -I
  {{< /tab >}}
  {{< tab header="Windows with WSL2" language="bash">}}
hostname -I
  {{< /tab >}}
{{< /tabpane >}}

{{% notice Note %}}
If the Pi can't connect later, check that the simulation machine and Raspberry Pi are on the same network and that the local firewall allows inbound connections to port `18000`.
{{% /notice %}}

## What you've accomplished and what's next

You've now created a simulation environment, started the Reachy Mini MuJoCo daemon on a network-accessible port, and found the host IP address the Raspberry Pi needs when it connects to the simulated robot. You should now see a simulated Reachy robot in MuJoCo.

Next, you'll prepare the Raspberry Pi.
