---
title: "NXP FRDM i.MX 93: Load and stop the MCU heartbeat" 
description: "Manually load and stop the Zephyr based heartbeat app on the MCU."
weight: 5
layout: "learningpathall"
---

## Transfer the unstripped ELF

From the Ubuntu build host, transfer the ELF to the board (BOARD_IP is attained via `ip addr` on the board):

```bash
cd "$HOME/nxp-imx93-mcu"
scp build/heartbeat/zephyr/zephyr.elf root@OUR_BOARD_IP_ADDRESS:/root/nxp-imx93-heartbeat.elf
scp components/firmware_manager.py root@OUR_BOARD_IP_ADDRESS:/root/nxp-firmware-manager.py
scp check-linux.py root@OUR_BOARD_IP_ADDRESS:/root/nxp-check-linux.py
ssh root@OUR_BOARD_IP_ADDRESS
```

Copy `check-linux.py` from the extracted source bundle to `/root/check-linux.py` on the board. Complete the FRDM boot preparation from the previous page before loading. On the board as root:

```bash
nxp-mcore status
install -m 0644 /root/nxp-firmware-manager.py /usr/libexec/nxp-lp/firmware_manager.py
install -m 0644 /root/nxp-check-linux.py /usr/libexec/nxp-lp/check-linux.py
nxp-mcore load /root/nxp-imx93-heartbeat.elf
journalctl -u nxp-mcore-test.service -b -f
```

The helper creates a transient `nxp-mcore-test.service` running the same foreground manager that Part 3 packages. It requires an offline application Cortex-M33, validates the ELF header and remoteproc vector section, records ownership, installs a unique firmware filename, starts remoteproc, and checks the RPMsg control endpoint. Expect `MCore started firmware=...` and a numbered heartbeat on the MCU serial terminal.

Press Ctrl+C to stop following the journal. This does not stop the service. Check status independently:

```bash
nxp-mcore status
ls -l /dev/nxp-temperature /dev/nxp-mcore-control
```

## Stopping the heartbeat application

Lets now stop the heartbeat application:

```bash
nxp-mcore stop
nxp-mcore status
journalctl -u nxp-mcore-test.service -b --no-pager -n 80
```

Part 3 will require the application MCU be offline. 

## Recovering ownership and MCU after an interrupted run

An unexpected power cycle can leave the persistent manager work files while
the application MCU is offline. The updated manager archives verified ownership
from another Linux boot automatically. Legacy records without a boot ID, or
records from the current boot, require explicit recovery:

```bash
python3 /usr/libexec/nxp-lp/firmware_manager.py recover --work /var/lib/nxp-mcore-test
```

Run this only after installing the updated manager from the source bundle.
See `MCU-RECOVERY.md` in the bundle for the no-reflash update commands. Recovery
holds the existing lock, requires an offline core and archives only recorded,
digest-matched files. Then load the desired ELF again. A manually loaded test
is not automatically restarted by a reboot.

If an older ELF starts without RPMsg devices and cannot acknowledge `STOP`,
shut down Linux and power-cycle the board before retrying the rebuilt ELF.
[REMOTEPROC-VECTORS.md](../bundle/REMOTEPROC-VECTORS.md) covers updating an existing image.

## What you have learned

You can transfer and load the actual NXP FRDM i.MX 93 MCU ELF, observe its foreground execution, and stop it through the control handshake.
