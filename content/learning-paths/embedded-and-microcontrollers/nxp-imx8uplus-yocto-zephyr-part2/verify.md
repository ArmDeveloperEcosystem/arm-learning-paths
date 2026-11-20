---
title: "NXP FRDM i.MX 8M Plus: Verify MCU and Linux together"
description: "Observe heartbeat output, RPMsg delivery, and repeatable cleanup."
weight: 6
layout: "learningpathall"
---

## Observe RPMmsg action in Yocto

While the heartbeat runs in Zephyr on the MCU, the MCU DEBUG UART console in Yocto should show:

```output
NXP FRDM i.MX 8M Plus: Zephyr on application MCU
MCU heartbeat 0
MCU heartbeat 1
MCU heartbeat 2
```

On the board over SSH, optionally inspect the heartbeat through Linux's RPMsg TTY:

```bash
python3 - <<'PYTHON'
import os, select, time, tty
fd = os.open("/dev/nxp-temperature", os.O_RDWR | os.O_NOCTTY | os.O_NONBLOCK)
try:
    tty.setraw(fd)
    os.write(fd, b"HELLO\n")
    end = time.monotonic() + 10
    while time.monotonic() < end:
        if select.select([fd], [], [], 0.5)[0]:
            data = os.read(fd, 4096)
            if not data:
                break
            os.write(1, data)
finally:
    os.close(fd)
PYTHON
uname -m
uptime
systemctl status --with-dependencies greengrass-lite.target
```

You should see the MCU counter advancing its heartbeat count.

Lastly, we can shut the heartbeat back down by running on the board:

```bash
nxp-mcore stop
nxp-mcore status
```

Verify the offline state. This indicates the heartbeat has been shut down.

## Additional details: Diagnosing faults

| Symptom | Inspect |
| --- | --- |
| Entire board hangs at M7 start | Corrected FRDM clock override, `prepare_mcore` before Linux, named vring reservations, TCM ELF validation, and both serial logs; see bundle `HANG-FIX.md` |
| No remoteproc match | Correct machine image, loaded DTB, kernel remoteproc option, boot firmware, and `/etc/nxp-lp/board.json` |
| Attached/detached core | A bootloader demo or another owner is already running; correct startup ownership |
| Running core but no heartbeat | MCU console selection, correct local board target, UART ownership, and clocks |
| RPMsg aliases missing | RPMSG_TTY, endpoint source addresses, udev rules, vrings, fixed resource table, and the source patch |
| Stop acknowledgment missing | Separate control endpoint, application health, mailbox/cache configuration, and manager journal |

Use `dmesg` and `journalctl -u nxp-mcore-test.service` for evidence. The heartbeat startup and RPMsg results above are user-reported hardware evidence. Stop/restart acceptance, physical BMP280 readings and AWS deployment remain to be tested; keep their logs separately. Finish with the test service stopped and the MCU offline, then continue with [Part 3](/learning-paths/embedded-and-microcontrollers/nxp-imx8uplus-gglite-zephyr-combined-part3/).

## What you have learned

You can verify that the Zephyr heartbeat is functioning and sending messages via RPMsg as well as and show repeatable MCU control and cleanup.
