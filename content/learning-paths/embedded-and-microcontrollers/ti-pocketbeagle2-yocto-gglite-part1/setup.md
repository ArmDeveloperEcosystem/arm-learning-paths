---
title: "Boot the image and connect the board"
description: Flash the PocketBeagle 2 Yocto image and verify SSH access and outbound Internet connectivity before Greengrass Lite provisioning.
weight: 4
layout: "learningpathall"
---

## Write the microSD card

On a Linux computer with the card reader attached, install `bmap-tools` and identify the card:

```bash
sudo apt-get install bmap-tools
lsblk -o NAME,SIZE,MODEL,MOUNTPOINTS
```

{{% notice warning %}}
Writing the image erases the selected device. Replace `/dev/sdX` with the entire microSD device, not a partition. Check its size and model, and unmount its mounted partitions before proceeding.
{{% /notice %}}

Use the actual image and block-map paths from the previous page:

```bash
sudo bmaptool copy --bmap /path/to/image.wic.bmap \
  /path/to/image.wic.xz /dev/sdX
sync
```

Insert the card in PocketBeagle 2 and connect its USB-C port with a data cable. A serial console is useful if boot or networking fails; the target debug UART uses 115200 baud, 8N1. Follow the [PocketBeagle 2 connection guide](https://docs.beagleboard.org/boards/pocketbeagle-2/02-quick-start.html) for debug hardware and power requirements.

## Connect over USB Ethernet

The supplied image creates interface `pb2usb0` with address `192.168.7.2/24`. Its DHCP server offers `192.168.7.1/24` to the attached computer. Linux and macOS use the default CDC-ECM gadget. Windows users should follow the bundled README's NCM/RNDIS instructions using the serial console first.

From the attached computer, connect to the board:

```bash
ssh root@192.168.7.2
```

The development image initially permits passwordless root access. On the board, set a password and verify its architecture and included tools:

```bash
passwd
uname -m
command -v pb2-provision-greengrass
command -v python3
pb2-network-status
```

The architecture must be `aarch64`. The provisioning helper and Python must be present. This image includes `debug-tweaks`; use it on a controlled development network. A production image needs configured accounts and removal of that feature.

## Provide outbound Internet access

USB SSH access alone does not give the board Internet access. Choose either a USB Ethernet adapter on a supported USB host port/cape, or Internet sharing from the attached computer. For an adapter, the image uses DHCP on conventional Ethernet interfaces. Check `ip -br address`, `ip route`, and `resolvectl status` on the board.

### Share an Ubuntu host connection

Use a serial console for this change so you can recover if SSH disconnects. The image includes a USB serial console; a separate debug UART remains available even if you restart the USB gadget. First, confirm that Ubuntu can reach the board over USB before changing Internet sharing.

On Ubuntu, identify the USB Ethernet interface and check its carrier. Replace `YOUR_USB_INTERFACE` with its actual name, such as `enx060cae3c4bd8`:

```bash
export PB2_USB_IF=YOUR_USB_INTERFACE
ip -br link show dev "$PB2_USB_IF"
cat "/sys/class/net/$PB2_USB_IF/carrier"
```

Expect `LOWER_UP` in the link flags and a carrier value of `1`. An interface can be administratively `UP` while its route still shows `linkdown`; in that state, restore the USB link before configuring IP routing or DNS. See [Recover USB connectivity](#recover-usb-connectivity).

On the board as root, keep the bundled static address `192.168.7.2/24` and disable its DHCP server. Set Ubuntu's `192.168.7.1` address as the gateway and DNS forwarder. This replaces the earlier DHCP-client drop-in if you already created it:

```bash
mkdir -p /etc/systemd/network/20-pb2-usb.network.d
cat > /etc/systemd/network/20-pb2-usb.network.d/50-host-internet.conf <<'EOF'
[Network]
DHCP=no
DHCPServer=no
DNS=192.168.7.1

[Route]
Destination=0.0.0.0/0
Gateway=192.168.7.1
Metric=200
EOF
networkctl reload
networkctl reconfigure pb2usb0
ip link set dev pb2usb0 up
ip -4 address show dev pb2usb0
```

Confirm that `192.168.7.2/24` remains assigned. The static address comes from the bundled `20-pb2-usb.network`; do not replace that main file or enable a DHCP client for this Ubuntu setup.

On Ubuntu, create the shared profile only if it does not already exist:

```bash
nmcli connection show pb2-usb-share
```

If NetworkManager reports an unknown connection, create it:

```bash
sudo nmcli connection add type ethernet ifname "$PB2_USB_IF" con-name pb2-usb-share
```

Configure and activate the profile on the USB interface:

```bash
sudo nmcli connection modify pb2-usb-share \
  connection.interface-name "$PB2_USB_IF" \
  ipv4.method shared ipv4.addresses 192.168.7.1/24 \
  ipv4.never-default yes ipv6.method disabled
sudo nmcli connection up pb2-usb-share ifname "$PB2_USB_IF"
ip -br link show dev "$PB2_USB_IF"
ping -c 3 192.168.7.2
ssh root@192.168.7.2
```

The USB route must no longer show `linkdown`. Ubuntu keeps its existing upstream default route; NetworkManager's [shared IPv4 mode](https://www.networkmanager.dev/docs/api/1.46.2/nm-settings-nmcli.html) provides sharing to the board. If a previous automatic profile takes over the same interface, reactivate `pb2-usb-share` rather than creating another profile.

For macOS or Windows Internet sharing, use the platform instructions in the bundle's README. Their gateway and DHCP subnet can differ, so the Ubuntu-specific static gateway settings do not apply unchanged.

{{% notice Recover USB connectivity %}}

A host route ending in `linkdown` indicates that the link is not operational, even if the host has `192.168.7.1` assigned. Changing DNS or NAT rules will not restore the USB carrier. Keep the host's working upstream connection unchanged.

From the board's serial console, inspect the interface and services:

```bash
ip -br link show dev pb2usb0
ip -4 address show dev pb2usb0
systemctl status pb2-usb-gadget.service systemd-networkd.service sshd.service
journalctl -b -u pb2-usb-gadget.service -u systemd-networkd.service --no-pager -n 80
```

If `pb2usb0` exists but is administratively down, bring it up:

```bash
ip link set dev pb2usb0 up
```

On Ubuntu, activate the existing shared profile on the USB interface and check carrier again:

```bash
sudo nmcli connection up pb2-usb-share ifname "$PB2_USB_IF"
cat "/sys/class/net/$PB2_USB_IF/carrier"
ping -c 3 192.168.7.2
```

If carrier remains `0`, inspect the gadget service and USB enumeration before continuing. Reconnect the data cable and identify the interface again if it re-enumerates. Restart `pb2-usb-gadget.service` only from a separate debug UART: that restart disconnects both USB Ethernet and the USB serial console.

If carrier is `1` but ping still fails, confirm the board still has `192.168.7.2/24`, inspect `ip neigh show dev "$PB2_USB_IF"` on Ubuntu, and check the board's networkd logs. Do not proceed to Internet tests until local USB access works.
{{% /notice %}}

### Update /etc/resolv.conf

On the pocketbeagle board either in a SSH shell or via the UART console, edit /etc/resolv.conf and add the following line:

```bash
nameserver 8.8.8.8
```

Save the file.

### Verify outbound access

On the board, verify routing, DNS, time, and HTTPS:

```bash
ip route
resolvectl status
timedatectl status
ping -c 3 google.com
curl -I https://www.amazontrust.com/repository/AmazonRootCA1.pem
```

Expect a default route, usable DNS servers, a correct UTC time, proper pinging of google.com, and a successful HTTPS response. 

{{% notice Check clock time %}}
Correct the clock before provisioning: certificate validation fails when the time is wrong. The board needs outbound HTTPS and MQTT connectivity to AWS IoT; this exercise requires no inbound Internet port forwarding.

In either the SSH session to the pocketbeagle or the UART console session, type:

```bash
timedatectl set-ntp true
```

Then confirm that the time is correct:

```bash
date
```

It is often the case that the yocto image is initially setup in UTC timezones as the default (and this should be OK).
{{% /notice %}}

## What you have accomplished

The board boots 64-bit Arm Linux, accepts SSH connections, and reaches the Internet. Next, create its unique AWS identity and initialize Nucleus Lite.
