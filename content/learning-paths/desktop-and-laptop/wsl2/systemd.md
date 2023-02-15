---
title: Enable systemd in WSL

weight: 4
layout: learningpathall
---

## Enable systemd 

For Linux distributions which use systemd, such as Ubuntu, it can be enabled. 

When systemd is enabled services such as SSH and docker will start automatically.

Edit (or create) the file /etc/wsl.conf

Add the following lines to /etc/wsl.conf

```console
[boot]
systemd=true
```

Stop the distribution.

```cmd
wsl --terminate Ubuntu-22.04
```

Restart the distribution.

```cmd
wsl -d Ubuntu-22.04
```

Confirm systemd is running.

```bash
systemctl list-unit-files --type=service
```

Individual servers can also be queried to confirm they are running.

```bash
systemctl status ssh
```