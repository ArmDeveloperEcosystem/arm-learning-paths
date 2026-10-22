---
title: "Verify Zephyr and Linux running together"
description: Observe the MCU heartbeat, verify Linux and Greengrass health, and diagnose loading failures.
weight: 6
layout: "learningpathall"
---

## Observe the MCU heartbeat

Read the serial terminal connected to MCU_UART0. The output is similar to:

```output
PocketBeagle 2: Zephyr on Cortex-M4F
M4 heartbeat 0
M4 heartbeat 1
M4 heartbeat 2
```

The Zephyr boot banner can precede these lines. Observe the counter increasing approximately once per second. These messages come from the Cortex-M4F UART, not the Linux journal or the Greengrass Hello World component.

## Verify the Linux side

While heartbeat messages continue, run these commands in the SSH terminal:

```bash
uname -m
uptime
pb2-m4 status
```

You should see something like this in the output:

```output
root@pocketbeagle2:~# uname -m
aarch64
root@pocketbeagle2:~# uptime
 22:09:27 up 2 days,  7:12,  2 users,  load average: 0.00, 0.01, 0.00
root@pocketbeagle2:~# pb2-m4 status
device=/sys/class/remoteproc/remoteproc0 name=5000000.m4fss state=running firmware=pb2-zephyr-heartbeat.elf
root@pocketbeagle2:~#
```

We can also verify that the AWS IoT Greengrass service, from our [Part 1](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/deployment/) series, continues to run:

```bash
systemctl status --with-dependencies greengrass-lite.target
```

Linux must still report `aarch64`, the M4 must report `running`, and Greengrass services should remain healthy. Use the [Part 1 component verification](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/deployment/) to confirm that `com.arm.HelloGreengrassLiteWorld` still produces its minute-by-minute message if you kept it deployed.

Successful completion requires both observations at the same time: the MCU counter advances on MCU_UART0, and Linux remains reachable with its services running. Remoteproc's `running` state alone cannot prove the firmware prints correctly or that a peripheral is configured correctly.

## Diagnose a failed run

| Symptom | What to inspect |
| --- | --- |
| `pb2-m4` is missing | Boot the updated Part 1 image; copying an older bundle does not update an installed root filesystem |
| No M4 remote processor | Loaded AM6254 DTB, M4 kernel driver, mailbox, reserved memory, and boot logs |
| Core is `attached` or `detached` | Bootloader ownership; obtain an offline core rather than forcing a live replacement |
| ELF header check fails | Use `zephyr.elf` from the M4 build, not an A53 executable or raw binary |
| Bad program-header address or missing resource table | Correct v4.3.0 board target, unstripped ELF, and matching Linux carveouts |
| Running state but no heartbeat | Adapter RX connected to P2.07, common ground, correct serial device, 115200 8N1, and pin ownership |
| `stop` times out | The pinned kernel waits for a shutdown handshake that the sample does not implement; restart the board for another run |

For loader failures, inspect the relevant kernel log after attempting the load:

```bash
dmesg | tail -n 100
```

Do not change DDR addresses, enable the MCU UART in Linux, or reuse a different board's ELF to bypass an error. Match the firmware board target and the image's device tree first.

## Finish the experiment

The helper does not enable a startup service or change the default firmware filename. Save any other work, then shut down and power-cycle the development board to end the experiment. Check its remoteproc state on the next boot before reusing the M4. Keep the ELF and source on the development host for future builds.

## What you have accomplished

You built a Zephyr application for the AM6254 Cortex-M4F, loaded it through Linux remoteproc, and observed it executing alongside Yocto Linux and Greengrass. You can now extend the heartbeat with a peripheral that Linux explicitly releases to the MCU. Adding RPMsg communication or automatic firmware startup requires further work on shared resources and the firmware lifecycle.
