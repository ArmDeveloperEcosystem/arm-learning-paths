---
title: MQTT shell
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Set up the MQTT shell example

In this section, you will build a minimal Zephyr application that enables the **Zephyr Shell MQTT backend**, run an Eclipse Mosquitto broker in Docker, and send shell commands to the board using the Mosquitto command-line tools.

This example uses the **NXP FRDM-MCXN947** as the development board. Any other Zephyr-supported board with Ethernet works as well, because the MQTT shell backend is selected entirely through Kconfig and the application contains no board-specific code. To run the example on a different board, follow the same steps and substitute your board's Zephyr identifier in the wizard. The "Switch to a different board" section near the end of this page shows how to change boards on an existing project without recreating it.

The application does not need networking code in `main.c`. Zephyr starts the shell, network stack, DHCP client, and MQTT shell backend from configuration options in `prj.conf`.

## How the MQTT shell backend works

When `CONFIG_SHELL_BACKEND_MQTT=y` is enabled, Zephyr’s MQTT shell backend connects to a broker and uses MQTT topics to carry shell traffic (commands and responses).

The default topic pattern is:

| Direction | Topic |
|-----------|-------|
| Commands sent to the board | `<device_id>/sh/rx` |
| Responses sent from the board | `<device_id>/sh/tx` |

The backend derives `<device_id>` from the hardware device ID, so each board uses a unique topic prefix. You will read this ID from the broker after the board connects for the first time.


## Create the project

In the **Workbench for Zephyr** panel, select **New Application** to open the **Create a new Zephyr Application Project** wizard. Fill in the following fields:

1. **Select West Workspace**: select your initialized West workspace for Zephyr v4.4.0 (for example, `zephyr`).
2. **Select Toolchain**: select `zephyr-sdk-1.0.1`.
3. **Select Board**: select **NXP FRDM-MCXN947 (CPU0)** (Zephyr identifier `frdm_mcxn947/mcxn947/cpu0`).
4. **Application type**: select **Create new application**.
5. **Select Sample project**: select `hello_world`.
6. **Project Name**: enter `mqtt_shell_backend`.
7. **Project Location**: select the directory where you want to create the project (for example, `zephyr/apps`).
8. **Debug preset**: leave checked.
9. **Advanced options**: leave at the defaults.

Select **Create** to generate the project.

<p style="text-align:center;">
  <img src="/learning-paths/embedded-and-microcontrollers/zephyr_shell/images/WZ-new_project.png"
       alt="Workbench for Zephyr Create a new Zephyr Application Project wizard with West Workspace zephyr, Toolchain zephyr-sdk-1.0.1, Board NXP FRDM-MCXN947 CPU0, Application type Create new application, Sample project hello_world, Project Name mqtt_shell_backend, Project Location zephyr/apps, and Debug preset checked."
       width="640"
       style="max-width:100%;height:auto;" />
  <br/>
  <em>Create a new Zephyr Application Project wizard</em>
</p>

## Configure the application

The `hello_world` sample provides a working `CMakeLists.txt`, `prj.conf`, and `src/main.c`. Leave `CMakeLists.txt` unchanged, and replace `prj.conf` and `src/main.c` with the contents below.

### prj.conf

```bash
# Shell and MQTT backend
CONFIG_SHELL=y
CONFIG_SHELL_BACKEND_MQTT=y

# Networking
CONFIG_NETWORKING=y
CONFIG_NET_IPV4=y
CONFIG_NET_TCP=y
CONFIG_NET_DHCPV4=y
CONFIG_NET_CONFIG_SETTINGS=y

# MQTT broker address
CONFIG_SHELL_MQTT_SERVER_ADDR="192.168.1.233"

# Optional shell modules and logging
CONFIG_NET_SHELL=y
CONFIG_LOG=y

# Resource tuning
CONFIG_HEAP_MEM_POOL_SIZE=8192
CONFIG_MAIN_STACK_SIZE=2048
CONFIG_NET_PKT_RX_COUNT=16
CONFIG_NET_BUF_RX_COUNT=32
```

Replace `192.168.1.233` with the IP address of the host running Mosquitto, as seen from the board's Ethernet network.

The values in the Resource tuning section are the main knobs you will adjust to keep the shell footprint small on Cortex-M while still allowing the network stack and MQTT client to operate reliably.

### Use a static IPv4 address

DHCP is convenient, but it is not required. To use a static address, remove:

```bash
CONFIG_NET_DHCPV4=y
```

Then add values that match your network:

```bash
CONFIG_NET_CONFIG_MY_IPV4_ADDR="192.168.1.50"
CONFIG_NET_CONFIG_MY_IPV4_NETMASK="255.255.255.0"
CONFIG_NET_CONFIG_MY_IPV4_GW="192.168.1.1"
```

Keep `CONFIG_NET_CONFIG_SETTINGS=y` enabled so Zephyr applies the network configuration at boot.

### src/main.c

The shell and MQTT backend start from Zephyr initialization hooks, so `main.c` can stay minimal:

```c
int main(void)
{
    return 0;
}
```

## Build and flash

In the **Workbench for Zephyr** panel, select your project and build configuration. Select **Build**, then select **Flash**.

The FRDM-MCXN947 uses NXP LinkServer as the debug runner. If LinkServer is not installed, follow the Workbench for Zephyr prompt to install or configure it.

## Create the Mosquitto Docker Compose project

Create a directory named `mosquitto_shell` on your host computer with the following structure:

```output
mosquitto_shell/
|-- docker-compose.yml
`-- mosquitto/
    `-- config/
        `-- mosquitto.conf
```

### docker-compose.yml

```yaml
services:
  mosquitto:
    image: eclipse-mosquitto:latest
    container_name: mosquitto-mqtt
    ports:
      - "1883:1883"
    volumes:
      - ./mosquitto/config:/mosquitto/config:ro
      - ./mosquitto/data:/mosquitto/data
      - ./mosquitto/log:/mosquitto/log
    restart: unless-stopped
```

### mosquitto/config/mosquitto.conf

```bash
listener 1883 0.0.0.0
allow_anonymous true

persistence true
persistence_location /mosquitto/data/

log_dest file /mosquitto/log/mosquitto.log
log_dest stdout
log_type all
```

From the `mosquitto_shell` directory, start the broker:

```bash
docker compose up -d
```

Check that the container is running:

```bash
docker compose ps
```

You should see output similar to:

```output
NAME                  IMAGE                        STATUS
mosquitto-mqtt        eclipse-mosquitto:latest     Up
```

The `eclipse-mosquitto` image includes `mosquitto_pub` and `mosquitto_sub`, so you can run both tools from inside the container with `docker exec`.

### Install Mosquitto directly

If you prefer not to use Docker, you can install Mosquitto directly on your host computer. This gives you the `mosquitto` broker, `mosquitto_pub`, and `mosquitto_sub` commands locally.

Install Mosquitto with your operating system package manager:

```bash
sudo apt install mosquitto mosquitto-clients
```

On macOS, use Homebrew:

```bash
brew install mosquitto
```

After installing Mosquitto directly, start the broker using your operating system service manager or run it manually with a local configuration file. In the commands below, replace:

```bash
docker exec -it mosquitto-mqtt mosquitto_sub -h localhost
```

with:

```bash
mosquitto_sub -h localhost
```

Similarly, replace:

```bash
docker exec -i mosquitto-mqtt mosquitto_pub -h localhost
```

with:

```bash
mosquitto_pub -h localhost
```

## Find the device ID

The MQTT shell backend derives its client ID from the board's hardware UID, so each board connects with topics under `<device_id>/sh/rx` and `<device_id>/sh/tx`. There are two ways to read this ID.

### Option 1: from the board's serial console

If you have a serial terminal open on the board's UART (or J-Link RTT Viewer attached), the MQTT backend logs the topics it subscribes to and publishes from at boot. A typical FRDM-MCXN947 boot log looks like this:

```output
*** Booting Zephyr OS build v4.4.0 ***
[00:00:01.654,000] <inf> phy_mii: PHY (0) Link speed 100 Mb, full duplex
[00:00:01.654,000] <inf> eth_nxp_enet_qos_mac: Link is up
[00:00:01.656,000] <wrn> shell_mqtt: Network connected
[00:00:01.656,000] <inf> app_main: MQTT shell backend demo on frdm_mcxn947
[00:00:02.656,000] <inf> shell_mqtt: DNS resolved for 192.168.1.31:1883
[00:00:02.656,000] <err> shell_mqtt: mqtt_connect error: -22
[00:00:03.656,000] <inf> shell_mqtt: DNS resolved for 192.168.1.31:1883
[00:00:03.656,000] <err> shell_mqtt: mqtt_connect error: -22
[00:00:04.656,000] <inf> shell_mqtt: DNS resolved for 192.168.1.31:1883
[00:00:04.656,000] <err> shell_mqtt: mqtt_connect error: -22
[00:00:05.656,000] <inf> shell_mqtt: DNS resolved for 192.168.1.31:1883
[00:00:05.656,000] <err> shell_mqtt: mqtt_connect error: -22
[00:00:06.656,000] <inf> shell_mqtt: DNS resolved for 192.168.1.31:1883
[00:00:06.818,000] <wrn> shell_mqtt: MQTT client connected!
[00:00:07.823,000] <wrn> shell_mqtt: MQTT subscribe: ok
[00:00:07.823,000] <inf> shell_mqtt: Logs will be published to: 1a2b3c/sh/tx
[00:00:07.823,000] <inf> shell_mqtt: Subscribing shell cmds from: 1a2b3c/sh/rx
```

The two `<inf> shell_mqtt:` lines at the bottom give you the device ID directly. In this example it is `1a2b3c`.

{{% notice Note %}}
The `mqtt_connect error: -22` lines you see during the first few seconds are expected. The Zephyr MQTT client retries the connect handshake until the broker accepts it, usually within a few attempts. The connection completes when you see `MQTT client connected!`, followed by `MQTT subscribe: ok`.
{{% /notice %}}

### Option 2: from the broker side

If you do not have a serial terminal open, watch every shell-output topic with a wildcard:

```bash
docker exec -it mosquitto-mqtt mosquitto_sub -h localhost -t "+/sh/tx" -v
```

When the board connects, it publishes its shell prompt to `<device_id>/sh/tx`. The topic prefix on the first message is the device ID:

```output
1a2b3c/sh/tx rtt:~$
```

You can also confirm the same value from the broker's connection log:

```bash
docker logs mosquitto-mqtt | grep "as 1a2b3c"
```

```output
New client connected from 192.168.65.1:65496 as 1a2b3c (p4, c0, k60).
```

## Subscribe to shell output

Narrow the subscription to your board's response topic only (replace `1a2b3c` with your device ID):

```bash
docker exec -it mosquitto-mqtt mosquitto_sub -h localhost -t "1a2b3c/sh/tx" -v
```

Keep this terminal open. Every shell response from the board will print here.

## Send shell commands

Open a second terminal to publish commands to the board:

```bash
printf 'kernel version\n' | docker exec -i mosquitto-mqtt mosquitto_pub -h localhost -t "1a2b3c/sh/rx" -s
```

The command is published to Mosquitto, the board executes it, and the response appears in the first terminal:

```output
1a2b3c/sh/tx Zephyr version 4.4.0
```

Try the following commands:

| Command | Description |
|---------|-------------|
| `kernel version` | Print the Zephyr version string. |
| `kernel uptime` | Print the time since boot. |
| `kernel thread list` | Print the thread list and stack usage. |
| `net iface` | Print network interface configuration, including the assigned IPv4 address. |
| `net ping <ip>` | Send ICMP echo requests to a reachable host (for example, your gateway). |
| `device list` | Print registered Zephyr devices. |
| `help` | Print available shell modules and commands. |

The `net` commands are available because `CONFIG_NET_SHELL=y` was set in `prj.conf`. Without that option, only the `kernel`, `device`, and `shell` modules are exposed.

Example output for `kernel uptime`:

```output
1a2b3c/sh/tx Uptime: 55310 ms
```

Example output for `kernel thread list` on the FRDM-MCXN947 (truncated; the full list shows the network and Ethernet driver threads):

```output
1a2b3c/sh/tx Scheduler: 1046 since last call
Threads:
*0x300015d0 shell_mqtt
	options: 0x0, priority: 14 timeout: 0
	state: queued, entry: 0x100069e5
	stack size 2048, unused 1096, usage 952 / 2048 (46 %)

 0x30001c30 sh_mqtt_workq
	options: 0x0, priority: -9 timeout: 800
	state: pending, entry: 0x100223cd
	stack size 2048, unused 1160, usage 888 / 2048 (43 %)

 0x30002688 conn_mgr_monitor
	options: 0x0, priority: -1 timeout: 0
	state: pending, entry: 0x1001ea0d
	stack size 512, unused 264, usage 248 / 512 (48 %)

 0x300027c0 ENETQOS_RX
	options: 0x0, priority: -13 timeout: 0
	state: pending, entry: 0x100223cd
	stack size 1024, unused 752, usage 272 / 1024 (26 %)

 0x300028b0 idle
	options: 0x1, priority: 15 timeout: 0
	state: , entry: 0x1003a335
	stack size 320, unused 256, usage 64 / 320 (20 %)
```

The `*` next to `shell_mqtt` marks the running thread, which is the shell that just executed the command. Note that responses larger than the MQTT buffer are split across multiple publishes; `mosquitto_sub -v` reassembles them sequentially under the `1a2b3c/sh/tx` topic prefix.

Example output for `net iface` on the FRDM-MCXN947 (truncated to the IPv4 section):

```output
1a2b3c/sh/tx Default interface: 1

Interface eth0 (0x30000c70) (Ethernet) [1]
===================================
Link addr : XX:XX:XX:XX:XX:XX
MTU       : 1500
Flags     : AUTO_START,IPv4,IPv6
Status    : oper=UP, admin=UP, carrier=ON
Ethernet link speed: 100 Mbits full-duplex
IPv4 unicast addresses (max 1):
	192.168.1.41/255.255.255.0 DHCP preferred
IPv4 gateway : 192.168.1.1
DHCPv4 state      : bound
DHCPv4 server     : 192.168.1.1
```

Example output for `net ping 192.168.1.1` (board pinging its gateway):

```output
1a2b3c/sh/tx PING 192.168.1.1
28 bytes from 192.168.1.1 to 192.168.1.41: icmp_seq=1 ttl=64 time=0 ms
28 bytes from 192.168.1.1 to 192.168.1.41: icmp_seq=2 ttl=64 time=0 ms
28 bytes from 192.168.1.1 to 192.168.1.41: icmp_seq=3 ttl=64 time=0 ms
```

Replace `192.168.1.1` with the gateway address shown by `net iface`. The board sends three ICMP echo requests by default.

{{% notice Note %}}
The MQTT shell backend executes a command after it receives a newline character. The `printf 'kernel version\n' | ... mosquitto_pub -s` form sends the command with the required newline.
{{% /notice %}}

## Switch to a different board

The application is portable across any Zephyr-supported board with Ethernet, because the MQTT backend is selected through Kconfig and there is no board-specific code in `main.c`. You do not need to recreate the project to test it on another board.

To change the target board on an existing project:

1. Open the **Workbench for Zephyr** panel in the VS Code Activity Bar.
2. Expand the **Applications** section. The project you created appears with its current board name underneath.
3. Right-click the board name and select **Change board**. Pick a new board from the list (for example, an STM32 Nucleo, Nordic nRF52, or another Cortex-M board with Ethernet).
4. Right-click the application and select **Clean** to remove the previous build artifacts.
5. Right-click the application and select **Build (pristine)** to rebuild the project from scratch with the new board configuration.

After the pristine build completes, flash the board as before. The same `prj.conf` and `main.c` work without changes, and the MQTT backend connects as soon as the new board acquires an IPv4 address.

{{% notice Note %}}
A pristine build is required when you change the board because Workbench for Zephyr caches board-specific generated files (device tree, Kconfig, linker script) in the build directory. Without a clean rebuild, the previous board's configuration leaks into the new build and produces incorrect binaries.
{{% /notice %}}

## What's next?

You now have a working Zephyr shell over MQTT on the FRDM-MCXN947. In the next section, you will enable the RTT shell backend on the Silicon Labs xG27 Dev Kit and interact with the shell through J-Link RTT Viewer.
