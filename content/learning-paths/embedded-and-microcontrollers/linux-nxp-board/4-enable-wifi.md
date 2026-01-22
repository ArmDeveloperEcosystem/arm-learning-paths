---
# User change
title: "Transfer files to the board"

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Proceed with the remainder of this Learning Path logged in as `root`. 

Once the board is on your network, copying files over SSH is usually the fastest workflow. If you can’t use WiFi, you can still move files with a USB drive. Create a test file to transfer.

```bash
echo "test" > test.txt
```

## Transfer files over WiFi (scp)

You’ll need the board’s IP address. On the board, run:

```bash
ifconfig | grep RUNNING -A 1
```

Look for the WiFi interface (often `mlan0`) and note the `inet` address.

On your development machine, copy a file to the board with `scp` by updating the IP address in the following command:

```bash
scp test.txt root@<ip-address>:/root/test.txt
```

If you haven’t used SSH with this board before, you might be prompted to accept the host key. That’s expected. 

## Transfer files over USB

If WiFi isn’t available, copy your files onto a USB-A thumb drive on your development machine, then insert the drive into the board.

On the board, mount the drive and copy the file:

```bash
mount /dev/sda1 /mnt
cp /mnt/test.txt /root
```

If `/dev/sda1` doesn’t exist, list block devices and use the partition that matches your USB drive:

```bash
lsblk
```

For example:

```bash
cp /mnt/test.txt ./
```

When you’re done, unmount the drive:

```bash
umount /mnt
```

## Confirm file transfer

You should now see the file in the `root` directory:

```output
root@imx93evk:~# ls /root
test.txt
```

Proceed to the final section to automate reconnecting to wifi.