---
# User change
title: "Set up a Linux user and connect to WiFi"

weight: 3

# Do not modify these elements
layout: "learningpathall"
---

You’re logged in as `root`, which is convenient for bring-up but not a great default for day-to-day development. In this section you’ll create a non-root user with admin privileges, then connect the board to WiFi so you can install packages and move files over the network.

## Create a non-root user with sudo access

Start by allowing members of the `wheel` group to use `sudo`.

```bash
sudo visudo
```

In the editor that opens, find the line below and uncomment it:

```bash { output_lines = "1" }
%wheel ALL=(ALL:ALL) ALL # uncomment this line
```

Now create a user and add it to `wheel`:

```bash
sudo adduser testuser
sudo usermod -aG wheel testuser
```

Switch to the new user and confirm `sudo` works:

```bash
su - testuser
sudo whoami
```

The expected output is `root`.

Log out, then log back in as your new user.

## Connect the board to WiFi

The WiFi driver isn’t brought up automatically on this Linux image. You load the module, then use `connmanctl` to connect.

{{% notice Note %}}

In this Linux image, ConnMan typically remembers the WiFi network you connected to.

After a reboot, you might still need to load the WiFi driver module again. Once the module is loaded, ConnMan usually reconnects automatically.

{{% /notice %}}

Load the WiFi driver and open `connmanctl`:

```bash
sudo /usr/sbin/modprobe moal mod_para=nxp/wifi_mod_para.conf
sudo connmanctl
```

At the `connmanctl>` prompt, enable and scan WiFi, then list services:

```bash
enable wifi
scan wifi
services
```

You’ll see services in a form similar to:

```bash { output_lines = "1-3" }
<SSID>                wifi_0123456789ab_cdef0123456789_managed_psk
<SSID>                wifi_abcdef012345_6789abcdef0123_managed_psk
<SSID>                wifi_fedcba987654_3210fedcba9876_managed_psk
```

{{% notice Note %}}

Duplicate SSIDs can appear, so you might need to try more than one `wifi_..._managed_psk` entry.

{{% /notice %}}

Connect to the right `wifi_..._managed_psk` entry and enter your passphrase when prompted.

In `connmanctl`, the passphrase is your WiFi network password (the WPA2/WPA-PSK key). Don’t add quotes around it.

```bash
agent on
connect wifi_0123456789ab_cdef0123456789_managed_psk
```


After you connect, exit `connmanctl`:

```bash
quit
```

Verify that your WiFi network has internet access:

```bash
curl -I http://www.example.com
```

The output is similar to:

```bash { output_lines = "1-2" }
HTTP/1.1 200 OK
...
```

If you don’t have internet access on that network, you can still confirm the board has an IP address:

```bash
ifconfig | grep RUNNING -A 1
```