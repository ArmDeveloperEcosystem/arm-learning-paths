---
# User change
title: "(Optional) Enable Persistent WiFi"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

ConnMan usually persists your WiFi network configuration across reboots. On this Linux image, the missing piece is often that the WiFi driver module isn’t loaded automatically at boot.

In this section, you’ll run one command at boot to load the WiFi driver. After that, ConnMan should reconnect to the saved network automatically.

## Confirm ConnMan can reconnect after loading the driver

First, connect to WiFi once using `connmanctl` (from the previous section). Then reboot the board.

After the reboot, log in and load the driver:

```bash
sudo /usr/sbin/modprobe moal mod_para=nxp/wifi_mod_para.conf
```

Give it a few seconds, then confirm you have an IP address and Internet connectivity:

```bash
ifconfig | grep RUNNING -A 1
curl -I http://www.example.com
```

If this reconnects reliably, you’re ready to automate it.

## Load the WiFi driver automatically on boot

Create a small `systemd` unit that runs `modprobe` at startup.

```bash
sudo nano /etc/systemd/system/nxp-wifi-driver.service
```

Add the following:

```bash
[Unit]
Description=Load WiFi driver (moal) for NXP i.MX93
After=multi-user.target

[Service]
Type=oneshot
ExecStart=/usr/sbin/modprobe moal mod_para=nxp/wifi_mod_para.conf
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

Enable the service:

```bash
sudo systemctl daemon-reload
sudo systemctl enable nxp-wifi-driver.service
```

Reboot and confirm the board reconnects on its own:

```bash
sudo reboot
```

After it comes back up, check WiFi and Internet:

```bash
ifconfig | grep RUNNING -A 1
curl -I http://www.example.com
```

## What you’ve accomplished and what’s next:

You’ve set up an NXP FRDM i.MX 93 board as a practical Linux-based development target for ML workflows on Arm.

In this Learning Path, you:

- Booted the board and logged in over a serial console.
- Created a non-root user for day-to-day development.
- Connected the board to WiFi and transferred files using SSH or USB.
- Automated WiFi bring-up by loading the driver module on boot.

To go deeper, review the **Further reading** resources at the end of this Learning Path.

