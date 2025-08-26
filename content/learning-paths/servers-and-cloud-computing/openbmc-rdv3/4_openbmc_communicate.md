---
title: Extend Simulation Features
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Interact with Host Console via Serial over LAN (SOL)

The OpenBMC platform provides Serial over LAN (SOL) to enable console access to the host system (RD-V3 FVP) through the BMC. This feature is useful for remotely interacting with the host without needing a direct serial cable.

In this section, you’ll create a virtual serial bridge using socat, verify port mappings, and access the host console via the BMC Web UI.


### Step 1: Connect the BMC and Host Consoles

Run the following command on your development Linux machine (where the simulation is running) to bridge the BMC and host UART ports:

```bash
socat -x tcp:localhost:5005 tcp:localhost:5067
```

This command connects the host-side UART port (5005) to the BMC-side port (5067), allowing bidirectional serial communication.

{{% notice Note %}}
If you see a Connection refused error, check the FVP logs to verify the port numbers:
* In fvp_boot.log, look for a line like:
terminal_ns_uart0: Listening for serial connection on port 5005
* In obmc_boot.log, confirm the corresponding line:
terminal_3: Listening for serial connection on port 5067
{{% /notice %}}

Ensure both ports are active and match the socat command arguments.


### Step 2: Manually Set Host Power State

Once the SOL bridge is established, run the following command from the OpenBMC console shell to simulate the host being powered on:

```bash
busctl set-property xyz.openbmc_project.State.Host \
/xyz/openbmc_project/state/host0 xyz.openbmc_project.State.Host \
CurrentHostState s xyz.openbmc_project.State.Host.HostState.Running
```

This updates the BMC’s internal host state, allowing UEFI to begin execution.

### Step 3. Access Host Console from Web UI

1.	Open the BMC Web UI in your browser:
   https://127.0.0.1:4223
2.	Log in using the default credentials:
   * Username: root
	* Password: 0penBmc
3.	From the Overview page, click the SOL Console button.
4.	You’ll see the host console output (UEFI or Linux prompt), and you can interact directly with it via the Web UI terminal.


![img3 alt-text#center](openbmc_webui_login.jpg "WebUI")


![img3 alt-text#center](openbmc_webui_overview.jpg "WebUI")


![img3 alt-text#center](openbmc_webui_sol.jpg "WebUI")


From here, you can monitor the UEFI boot sequence, interact with the host shell, and run diagnostic or validation commands—just as if you were connected to the physical serial port.

This console also allows you to verify host-BMC coordination, observe system logs in real time, test UEFI shell commands, or trigger custom boot workflows for pre-silicon validation.