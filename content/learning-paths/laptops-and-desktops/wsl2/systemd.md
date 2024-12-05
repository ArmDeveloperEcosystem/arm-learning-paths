---
title: Enable systemd in WSL

weight: 4
layout: learningpathall
---

## Enable systemd 

You can enable `systemd` in Linux distributions such as Ubuntu. 

When you enable `systemd`, services such as SSH and docker will start automatically.

Use a text editor (as root or using `sudo`) to create (or modify if it exists) the file `/etc/wsl.conf`

Add the following lines to `/etc/wsl.conf`: 

```console
[boot]
systemd=true
```

Open a Windows Command Prompt or PowerShell. Run the following commands to terminate and restart the distribution:

```cmd
wsl --terminate Ubuntu-22.04
wsl -d Ubuntu-22.04
```

Confirm `systemd` is running:

```bash
systemctl list-unit-files --type=service
```

Individual services can also be queried to confirm they are running:

```bash
systemctl status cron
```
