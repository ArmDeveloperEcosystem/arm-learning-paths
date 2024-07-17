---
title: Deploy firmware container using containerd
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Hello World example

Now that the container image has been pulled, we can create and start the container.

- Create and start the container

```console
ctr run --runtime io.containerd.hybrid ghcr.io/smarter-project/hybrid-runtime/hello_world_imx8mp:latest test
```

- Check the container was created
```console
ctr c ls
CONTAINER    IMAGE                                                               RUNTIME
test         ghcr.io/smarter-project/hybrid-runtime/hello_world_imx8mp:latest    io.containerd.hybrid
```

- Check the container is running
```console
ctr t ls
TASK    PID    STATUS    
test    808    RUNNING
```
The output from the hello-world application running on the Cortex-M can be seen in the AVH GUI by selecting “Cortex-M Console”

![Cortex-M output alt-text#center](containerd1.png "Figure 1. Cortex-M output")

- Check container info

```console
ctr c info test
```
The output should be:

```output
{
    "ID": "test",
    "Labels": {
        "Board": "NXP i.MX8MPlus EVK board",
        "Firmware name": "/hello_world.elf",
        "Firmware path": "/var/lib/containerd/io.containerd.snapshotter.v1.overlayfs/snapshots/2/fs",
        "MCU name": "imx-rproc",
        "MCU path": "/sys/class/remoteproc/remoteproc0"
    },
    "Image": "ghcr.io/smarter-project/hybrid-runtime/hello_world_imx8mp:latest",
    "Runtime": {
        "Name": "io.containerd.hybrid",
        "Options": null
    },
    "SnapshotKey": "test",
    "Snapshotter": "overlayfs",
    "CreatedAt": "2024-06-27T09:48:34.470393903Z",
    "UpdatedAt": "2024-06-27T09:48:40.188131946Z",
    "Extensions": {},
    "SandboxID": "",
    "Spec": {
        "ociVersion": "1.1.0-rc.1",
        "process": {
            "user": {
                "uid": 0,
                "gid": 0,
                "additionalGids": [
                    0
                ]
            },
            "args": [
                "/hello_world.elf"
            ],
            "env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
            ],
            "cwd": "/",
            "capabilities": {
                "bounding": [
                    "CAP_CHOWN",
                    "CAP_DAC_OVERRIDE",
                    "CAP_FSETID",
                    "CAP_FOWNER",
                    "CAP_MKNOD",
                    "CAP_NET_RAW",
                    "CAP_SETGID",
                    "CAP_SETUID",
                    "CAP_SETFCAP",
                    "CAP_SETPCAP",
                    "CAP_NET_BIND_SERVICE",
                    "CAP_SYS_CHROOT",
                    "CAP_KILL",
                    "CAP_AUDIT_WRITE"
                ],
                "effective": [
                    "CAP_CHOWN",
                    "CAP_DAC_OVERRIDE",
                    "CAP_FSETID",
                    "CAP_FOWNER",
                    "CAP_MKNOD",
                    "CAP_NET_RAW",
                    "CAP_SETGID",
                    "CAP_SETUID",
                    "CAP_SETFCAP",
                    "CAP_SETPCAP",
                    "CAP_NET_BIND_SERVICE",
                    "CAP_SYS_CHROOT",
                    "CAP_KILL",
                    "CAP_AUDIT_WRITE"
                ],
                "permitted": [
                    "CAP_CHOWN",
                    "CAP_DAC_OVERRIDE",
                    "CAP_FSETID",
                    "CAP_FOWNER",
                    "CAP_MKNOD",
                    "CAP_NET_RAW",
                    "CAP_SETGID",
                    "CAP_SETUID",
                    "CAP_SETFCAP",
                    "CAP_SETPCAP",
                    "CAP_NET_BIND_SERVICE",
                    "CAP_SYS_CHROOT",
                    "CAP_KILL",
                    "CAP_AUDIT_WRITE"
                ]
            },
            "rlimits": [
                {
                    "type": "RLIMIT_NOFILE",
                    "hard": 1024,
                    "soft": 1024
                }
            ],
            "noNewPrivileges": true
        },
        "root": {
            "path": "rootfs"
        },
        "mounts": [
            {
                "destination": "/proc",
                "type": "proc",
                "source": "proc",
                "options": [
                    "nosuid",
                    "noexec",
                    "nodev"
                ]
            },
            {
                "destination": "/dev",
                "type": "tmpfs",
                "source": "tmpfs",
                "options": [
                    "nosuid",
                    "strictatime",
                    "mode=755",
                    "size=65536k"
                ]
            },
            {
                "destination": "/dev/pts",
                "type": "devpts",
                "source": "devpts",
                "options": [
                    "nosuid",
                    "noexec",
                    "newinstance",
                    "ptmxmode=0666",
                    "mode=0620",
                    "gid=5"
                ]
            },
            {
                "destination": "/dev/shm",
                "type": "tmpfs",
                "source": "shm",
                "options": [
                    "nosuid",
                    "noexec",
                    "nodev",
                    "mode=1777",
                    "size=65536k"
                ]
            },
            {
                "destination": "/dev/mqueue",
                "type": "mqueue",
                "source": "mqueue",
                "options": [
                    "nosuid",
                    "noexec",
                    "nodev"
                ]
            },
            {
                "destination": "/sys",
                "type": "sysfs",
                "source": "sysfs",
                "options": [
                    "nosuid",
                    "noexec",
                    "nodev",
                    "ro"
                ]
            },
            {
                "destination": "/run",
                "type": "tmpfs",
                "source": "tmpfs",
                "options": [
                    "nosuid",
                    "strictatime",
                    "mode=755",
                    "size=65536k"
                ]
            }
        ],
        "linux": {
            "resources": {
                "devices": [
                    {
                        "allow": false,
                        "access": "rwm"
                    },
                    {
                        "allow": true,
                        "type": "c",
                        "major": 1,
                        "minor": 3,
                        "access": "rwm"
                    },
                    {
                        "allow": true,
                        "type": "c",
                        "major": 1,
                        "minor": 8,
                        "access": "rwm"
                    },
                    {
                        "allow": true,
                        "type": "c",
                        "major": 1,
                        "minor": 7,
                        "access": "rwm"
                    },
                    {
                        "allow": true,
                        "type": "c",
                        "major": 5,
                        "minor": 0,
                        "access": "rwm"
                    },
                    {
                        "allow": true,
                        "type": "c",
                        "major": 1,
                        "minor": 5,
                        "access": "rwm"
                    },
                    {
                        "allow": true,
                        "type": "c",
                        "major": 1,
                        "minor": 9,
                        "access": "rwm"
                    },
                    {
                        "allow": true,
                        "type": "c",
                        "major": 5,
                        "minor": 1,
                        "access": "rwm"
                    },
                    {
                        "allow": true,
                        "type": "c",
                        "major": 136,
                        "access": "rwm"
                    },
                    {
                        "allow": true,
                        "type": "c",
                        "major": 5,
                        "minor": 2,
                        "access": "rwm"
                    }
                ],
                "cpu": {
                    "shares": 1024
                }
            },
            "cgroupsPath": "/default/test",
            "namespaces": [
                {
                    "type": "pid"
                },
                {
                    "type": "ipc"
                },
                {
                    "type": "uts"
                },
                {
                    "type": "mount"
                },
                {
                    "type": "network"
                }
            ],
            "maskedPaths": [
                "/proc/acpi",
                "/proc/asound",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/sys/firmware",
                "/proc/scsi"
            ],
            "readonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        }
    }
}
```

- Stop container
```console
ctr t kill test
```
- Check container was stopped
```console
ctr t ls
TASK    PID    STATUS    
test    808    STOPPED
```
- Delete container
```console
ctr c rm test
```

## SMARTER Demo firmware 

We are also able to use a pre-built container image from the SMARTER project, available on GitHub for the i.MX8M-PLUS-EVK AVH model. The container image contains a FreeRTOS application built using the NXP SDK that outputs a timestamp to the serial console output of the board. The application also sends the output to the cortexm_console helper application running under Linux on the board.

You can pull the pre-built image onto the AVH model using:

```console
ctr image pull ghcr.io/smarter-project/smart-camera-hybrid-application/hybrid_app_imx8mp:latest
```
Creating and running the container:
```console
ctr run --runtime io.containerd.hybrid ghcr.io/smarter-project/smart-camera-hybrid-application/hybrid_app_imx8mp:latest test2
```
The Cortex-M Console output will now show:

![Cortex-M output alt-text#center](containerd2.png "Figure 2. Cortex-M output")

The output from the Cortex-M is also available under `/var/lib/hybrid-runtime/<container_name>/<container_name>.log`
```output
cat  /var/lib/hybrid-runtime/test2/test2.log
Timestamp: 0
Timestamp: 1
Timestamp: 2
Timestamp: 3
Timestamp: 4
Timestamp: 5
Timestamp: 6
Timestamp: 7
Timestamp: 8
Timestamp: 9
Timestamp: 10
```
When the container is deleted, the log file will also be removed:
```console
ctr t kill test2
ctr c rm test 2
cat  /var/lib/hybrid-runtime/test2/test2.log
  cat: /var/lib/hybrid-runtime/test2/test2.log: No such file or directory
```