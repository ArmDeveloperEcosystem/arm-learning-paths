---
title: Learn more Linux Container commands
weight: 5
layout: "learningpathall"
---

## Container management

Now that you know the basics, here are some useful commands for managing your container from the Termina shell.

Start a stopped container:

```bash
lxc start u1
```

Stop a running container:

```bash
lxc stop u1
```

Enter the container shell:

```bash
lxc exec u1 -- bash
```

List all available containers and their status:

```bash
lxc list
```

Delete a container (permanent action):

```bash
lxc delete u1
```

Print additional container information:

```bash
lxc info u1
```

Example output:

```output
Name: u1
Status: RUNNING
Type: container
Architecture: aarch64
PID: 24141
Created: 2025/08/07 04:46 EDT
Last Used: 2025/08/07 04:46 EDT

Resources:
  Processes: 120
  CPU usage:
    CPU usage (in seconds): 384
  Memory usage:
    Memory (current): 1.58GiB
    Memory (peak): 4.86GiB
  Network usage:
    eth0:
      Type: broadcast
      State: UP
      Host interface: veth7df9a2e6
      MAC address: 00:16:3e:18:59:08
      MTU: 1500
      Bytes received: 1.28GB
      Bytes sent: 6.11MB
      Packets received: 308930
      Packets sent: 83115
      IP addresses:
        inet:  100.115.92.202/28 (global)
        inet6: fe80::216:3eff:fe18:5908/64 (link)
```

Add the Google Debian container to your list of containers you can install:

```bash
lxc remote add google https://storage.googleapis.com/cros-containers --protocol=simplestreams
```

List the remote containers:

```bash
lxc remote list
```

Example output:

```output
+-----------------+------------------------------------------------+---------------+-------------+--------+--------+--------+
|      NAME       |                      URL                       |   PROTOCOL    |  AUTH TYPE  | PUBLIC | STATIC | GLOBAL |
+-----------------+------------------------------------------------+---------------+-------------+--------+--------+--------+
| google          | https://storage.googleapis.com/cros-containers | simplestreams | none        | YES    | NO     | NO     |
+-----------------+------------------------------------------------+---------------+-------------+--------+--------+--------+
| images          | https://images.linuxcontainers.org             | simplestreams | none        | YES    | NO     | NO     |
+-----------------+------------------------------------------------+---------------+-------------+--------+--------+--------+
| local (current) | unix://                                        | lxd           | file access | NO     | YES    | NO     |
+-----------------+------------------------------------------------+---------------+-------------+--------+--------+--------+
| ubuntu          | https://cloud-images.ubuntu.com/releases       | simplestreams | none        | YES    | YES    | NO     |
+-----------------+------------------------------------------------+---------------+-------------+--------+--------+--------+
| ubuntu-daily    | https://cloud-images.ubuntu.com/daily          | simplestreams | none        | YES    | YES    | NO     |
+-----------------+------------------------------------------------+---------------+-------------+--------+--------+--------+
```

Using the `images` remote you can create a container with images from [Linux Containers](https://images.linuxcontainers.org/).

For example, to start Alpine Linux 3.22:

```bash
lxc launch images:alpine/3.22 a1
```

## Configure container auto-start

From the Termina shell, configure the container to start automatically when you start the Linux development environment:

```bash
# Set the container to start automatically 
lxc config set u1 boot.autostart true

# Set the startup priority (lower number means higher priority)
lxc config set u1 boot.autostart.priority 1
```

## Save and restore

Once you have a container configured with your preferences, you can save it and use the backup to create new containers.

### Create a backup

First, stop the running container to ensure a consistent state:

```bash
lxc stop u1
```

Save the container to a compressed tar file using the `export` command:

```bash
lxc export u1 my-ubuntu.tar.gz
```

Save the backup file to your Google Drive or another easy-to-access location.

### Create a new container from the backup

Import the backup file to create a new container:

```bash
lxc import my-ubuntu.tar.gz u2 
```

Now you have a fresh container named `u2` at the same state you saved the backup.

## Performance tips

For a smoother experience, especially on devices with limited resources, you can monitor and manage your container performance.

### Limit container resources

Configure resource limits for your container from the Termina shell. This can prevent the container from consuming too many system resources.

Limit the container to 4 CPU cores:

```bash
lxc config set u1 limits.cpu 4
```

You can confirm using the Linux `lscpu` command. On an 8-core system you will see 4 cores moved to offline.

Limit the container to 2 GB of RAM:

```bash
lxc config set u1 limits.memory 2GB
```
