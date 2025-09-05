---
title: Monitor and Control the Host CPU via OpenBMC SOL and Web UI
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Access the Host Console via OpenBMC SOL

The OpenBMC platform provides `Serial over LAN` (SOL), allowing you to access the host console (RD-V3 FVP) remotely through the BMC—without needing a physical serial cable.
In this module, you’ll use `socat` to create a virtual UART bridge, verify port mappings, and access the host console via the BMC Web UI.

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

### Step 3: Access Host Console from Web UI

- From your simulation host, launch a browser and open the BMC Web UI at:
  https://127.0.0.1:4223
   ![img3 alt-text#center](openbmc_webui_login.jpg "WebUI login") 

- Login using the default credentials:
   - Username: root
	- Password: 0penBmc
   {{% notice Note %}}
   As a reminder, the first character of the password is the number ***0***, not a capital ***O***.
   {{% /notice %}}
   After login, you'll see the Web UI dashboard:

- From the Overview page, click the `SOL Console` button.
   ![img4 alt-text#center](openbmc_webui_overview.jpg "WebUI Overview")

- The SOL terminal in the Web UI will display the host console output (UEFI shell or Linux login). You can type commands directly as if you were connected over a physical serial line.
   ![img5 alt-text#center](openbmc_webui_sol.jpg "WebUI SOL")

Once connected to the SOL terminal, you can monitor the UEFI boot sequence, interact with the host shell, and run diagnostic or recovery workflows—just as if you were connected to a physical serial port.

This confirms that OpenBMC is fully managing host power and console access in your simulated environment.

In the next module, you'll expand this control further by sending IPMI commands to the BMC—allowing you to test low-level system interactions and even implement your own OEM command handlers.
