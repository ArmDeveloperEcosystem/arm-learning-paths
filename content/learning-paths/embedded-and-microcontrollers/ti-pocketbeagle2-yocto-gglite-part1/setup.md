---
title: "Boot the image and connect the board"
description: Write the PocketBeagle 2 Yocto image to a microSD card, then verify SSH access and outbound Internet connectivity before Greengrass nucleus lite provisioning.
weight: 4
layout: "learningpathall"
---

## Write the microSD card

After building the Yocto image for the PocketBeagle 2, write the image to the microSD card.

With the microSD card in a card reader attached to the host computer, install `bmap-tools` and identify the card:

```bash
sudo apt-get install bmap-tools
lsblk -o NAME,SIZE,MODEL,MOUNTPOINTS
```

The card is the removable disk with the size that you expect. 

In the following example, the 64 GB card is `sda`, and the computer disk is `nvme0n1`:

```output
NAME          SIZE MODEL                  MOUNTPOINTS
sda          59.5G Mass-Storage
├─sda1        512M                        /run/media/user/system-boot
└─sda2         59G
nvme0n1     476.9G KBG5AZNT512G LA KIOXIA
├─nvme0n1p1   260M                        /boot/efi
└─nvme0n1p6  89.9G                        /
```

{{% notice Warning %}}
Writing the image erases the selected device. Replace `/dev/sdX` with the entire microSD device rather than a partition. A card in a built-in slot usually appears as `/dev/mmcblk0` instead. Check its size and model before proceeding.
{{% /notice %}}

Ubuntu often mounts a card automatically. Unmount each partition that shows a mount point, for example:

```bash
sudo umount /dev/sdX1
```

Change to the folder that holds the image and block map from earlier, then write the image:

```bash
cd "$HOME/yocto-pocketbeagle2/build/deploy-ti/images/pocketbeagle2"
sudo bmaptool copy --bmap pocketbeagle2-dev-image-pocketbeagle2.rootfs.wic.bmap \
  pocketbeagle2-dev-image-pocketbeagle2.rootfs.wic.xz /dev/sdX
sync
```

The uncompressed image is 21 GiB, so writing takes several minutes. On a 64 GB card in a USB reader, it took about 14 minutes. 

A successful write ends with a line that reports the copying time and speed:

```output
bmaptool: info: block map format version 2.0
bmaptool: info: 5491928 blocks of size 4096 (21.0 GiB), mapped 2792928 blocks (10.7 GiB or 50.9%)
bmaptool: info: copying image 'pocketbeagle2-dev-image-pocketbeagle2.rootfs.wic.xz' to block device '/dev/sda' using bmap file 'pocketbeagle2-dev-image-pocketbeagle2.rootfs.wic.bmap'
bmaptool: info: synchronizing '/dev/sda'
bmaptool: info: copying time: 13m 59.0s, copying speed 13.0 MiB/sec
```

Check that the card now has the two partitions of the image:

```bash
sudo partprobe /dev/sdX
lsblk -o NAME,SIZE,FSTYPE,LABEL /dev/sdX
```

```output
NAME    SIZE FSTYPE LABEL
sda    59.5G
├─sda1  128M vfat   boot
└─sda2 20.8G ext4   root
```

## Boot the board and connect over USB Ethernet

Insert the card in the PocketBeagle 2. Connect the USB-C port of the PocketBeagle 2 to the host computer with a data cable. When the board boots, a new USB Ethernet interface appears on the host computer. 

Check for the interface:

```bash
ip -br link
```

A serial console is useful if boot or networking fails. The debug UART (serial port) of the board uses 115200 baud, 8N1. For debug hardware and power requirements, see the [PocketBeagle 2 Quick Start Guide](https://docs.beagleboard.org/boards/pocketbeagle-2/02-quick-start.html).

The image creates interface `pb2usb0` with address `192.168.7.2/24`. Its Dynamic Host Configuration Protocol (DHCP) server, which assigns addresses automatically, offers `192.168.7.1/24` to the host computer.

From the host computer, connect to the board:

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

Confirm that `uname -m` prints `aarch64` and that both `command -v` commands print a path. This image includes `debug-tweaks`, a Yocto debug feature that allows passwordless root login. Use this image only on a controlled development network. A production image needs configured accounts and removal of that feature.

## Provide outbound internet access

USB SSH access alone doesn't give the board Internet access. You can use a USB Ethernet adapter on a USB port provided by a cape, an expansion board for the PocketBeagle 2. Alternatively, you can use internet sharing from the host computer. For an adapter, the image uses DHCP on conventional ethernet interfaces. Check `ip -br address`, `ip route`, and `resolvectl status` on the board.

### Share the host computer connection

Internet sharing lets the board reach AWS through the connection of the host computer. Use a serial console for this change so that you can recover if SSH disconnects. The image includes a USB serial console. A separate debug UART stays available even if you restart the USB gadget service. The service provides the USB network and serial ports of the board. 

First, confirm that the host computer can reach the board over USB.

On the host computer, identify the USB Ethernet interface and check its carrier. The carrier shows whether the USB link is up. Replace `YOUR_USB_INTERFACE` with its actual name, such as `enx060cae3c4bd8`:

```bash
export PB2_USB_IF=YOUR_USB_INTERFACE
ip -br link show dev "$PB2_USB_IF"
cat "/sys/class/net/$PB2_USB_IF/carrier"
```

Expect `LOWER_UP` in the link flags, and a carrier value of `1`. An interface can be administratively `UP`, while its route still shows `linkdown`. In that state, restore the USB link before configuring IP routing or DNS lookups. For more information, see [Recover USB connectivity](/learning-paths/embedded-and-microcontrollers/ti-pocketbeagle2-yocto-gglite-part1/setup/#recover-usb-connectivity).

On the board as root, keep the bundled static address `192.168.7.2/24` and disable its DHCP server. Set the `192.168.7.1` address of the host computer as the gateway and DNS forwarder:

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

Confirm that `192.168.7.2/24` remains assigned. The static address comes from the bundled `20-pb2-usb.network`. Don't replace that main file or enable a DHCP client for this setup.

On the host computer, create the shared profile only if it doesn't already exist:

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

Ensure that the USB route doesn't show `linkdown`. The host computer keeps its existing upstream default route. The NetworkManager [shared IPv4 mode](https://www.networkmanager.dev/docs/api/1.46.2/nm-settings-nmcli.html) provides sharing to the board. If a previous automatic profile takes over the same interface, reactivate `pb2-usb-share` rather than creating another profile.

### Update `/etc/resolv.conf`

To make sure that the board can resolve names such as `amazontrust.com`, add a public DNS server. In an SSH session or on the UART console, edit `/etc/resolv.conf` on the board and add the following line:

```text
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

Each command should show the following:

| Command | Expected result |
| --- | --- |
| `ip route` | A default route. With Internet sharing, it points to `192.168.7.1`. |
| `resolvectl status` | At least one DNS server |
| `timedatectl status` | The correct date and time, in UTC |
| `ping -c 3 google.com` | Three replies and no packet loss |
| `curl -I …` | An HTTP response with status 200 |

The board needs outbound HTTPS and MQTT connectivity to AWS IoT. MQTT is the messaging protocol that AWS IoT uses. No inbound Internet port forwarding is required.

### Check the clock

Certificate validation fails when the board clock is wrong, so correct the clock before provisioning. In either the SSH session or the UART console session on the board, enable time synchronization:

```bash
timedatectl set-ntp true
```

Confirm that the time is correct:

```bash
date
```

The image usually defaults to the UTC time zone.

### (Optional) Recover USB connectivity

Use the following steps if the host computer can't reach the board at `192.168.7.2`. The steps are also applicable if the USB interface shows `linkdown`, during or after setting up Internet sharing.

A host route ending in `linkdown` indicates that the link isn't operational, even if the host computer has `192.168.7.1` assigned. Changing DNS settings won't restore the USB carrier. Keep the working upstream connection of the host computer unchanged.

From the serial console of the board, inspect the interface and services:

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

On the host computer, activate the existing shared profile on the USB interface, and check carrier again:

```bash
sudo nmcli connection up pb2-usb-share ifname "$PB2_USB_IF"
cat "/sys/class/net/$PB2_USB_IF/carrier"
ping -c 3 192.168.7.2
```

If carrier remains `0`, inspect the gadget service and USB enumeration before continuing. Reconnect the data cable and identify the interface again if it re-enumerates. Restart `pb2-usb-gadget.service` only from a separate debug UART. That restart disconnects both USB Ethernet and the USB serial console.

If carrier is `1` but ping still fails, confirm that the board still has `192.168.7.2/24`. Inspect `ip neigh show dev "$PB2_USB_IF"` on the host computer, and check the networkd logs of the board. After the host computer can reach the board over USB, return to the step that failed.

## What you've accomplished and what's next

You've written the Yocto image to the microSD card and booted the PocketBeagle 2. The board boots 64-bit Arm Linux, accepts SSH connections, and reaches the Internet. 

Next, you'll create a unique AWS identity for the PocketBeagle 2 and initialize Greengrass nucleus lite.
