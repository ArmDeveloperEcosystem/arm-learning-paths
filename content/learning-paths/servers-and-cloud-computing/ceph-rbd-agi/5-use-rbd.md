---
title: Create and use an RBD volume
description: Create a single-replica learning pool and map its RBD image on Ubuntu 26.04 using a pool-restricted client.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Use Ceph storage from Linux

You'll create a RADOS Block Device (RBD) image, map it as a block device, and mount a filesystem on it to store a test file. Run all commands inside `ceph1`, which acts as both a storage node and an RBD client. A checksum check after remapping will verify that the file persists in Ceph.

### Create the storage pool

A pool groups the objects that store your RBD image and controls how many copies Ceph keeps. Start with one copy because only one object storage daemon (OSD) is available. Cluster administration uses `cephadm shell`. RBD mapping uses the pinned container tools to configure a kernel block device for the VM.

Create the pool:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph osd pool create agi-rbd 8
sudo /usr/local/sbin/cephadm shell -- ceph config get mon mon_allow_pool_size_one
```

By default, Ceph prevents setting a pool size to 1 to protect against data loss. Temporarily enable single-replica pools, set the size to 1, and immediately restore the safety check:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph config set mon mon_allow_pool_size_one true
sudo /usr/local/sbin/cephadm shell -- ceph osd pool set agi-rbd size 1 --yes-i-really-mean-it
sudo /usr/local/sbin/cephadm shell -- ceph config set mon mon_allow_pool_size_one false
```

The `size` of the pool is the desired number of copies, and `min_size` is the minimum required to serve I/O. Set that minimum to `1` for this single-OSD stage, then initialize the pool for RBD:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph osd pool set agi-rbd min_size 1
sudo /usr/local/sbin/cephadm shell -- rbd pool init agi-rbd
sudo /usr/local/sbin/cephadm shell -- ceph osd pool get agi-rbd size
sudo /usr/local/sbin/cephadm shell -- ceph osd pool get agi-rbd min_size
sudo /usr/local/sbin/cephadm shell -- ceph pg ls-by-pool agi-rbd
```

Confirm that `size` and `min_size` are `1` and all placement groups for `agi-rbd` show `active+clean`. This means they can serve I/O and have the copies required by the pool settings.

{{% notice Warning %}}
A single-replica pool can lose all of its data if its OSD or backing disk fails. Use it only for this learning stage. You'll change the pool to three replicas after adding the other nodes.
{{% /notice %}}

Create a new 1 GiB image:

```bash
sudo /usr/local/sbin/cephadm shell -- rbd create --size 1024 agi-rbd/demo-volume
sudo /usr/local/sbin/cephadm shell -- rbd info agi-rbd/demo-volume
```

### Create a pool-restricted client

Generate a minimal configuration and an `aes256k` credential for `client.agirbd`. The credential grants access to the `agi-rbd` pool. Run each block individually in the same SSH session on `ceph1`, checking its result before continuing.

Prepare a private directory for the generated files:

```bash
umask 077
CLIENT_DIRECTORY="$HOME/agi-rbd-client"
mkdir -p "$CLIENT_DIRECTORY"
```

Generate the configuration with a bounded wait:

```bash
sudo timeout --kill-after=5s 30s \
  /usr/local/sbin/cephadm shell -- ceph config generate-minimal-conf \
  </dev/null > "$CLIENT_DIRECTORY/ceph.conf.new"
echo "Configuration exit status: $?"
```

Continue only if the exit status is `0`. Then, create or retrieve the pool-restricted credential:

```bash
sudo timeout --kill-after=5s 30s \
  /usr/local/sbin/cephadm shell -- ceph auth get-or-create \
  --key-type=aes256k client.agirbd \
  mon 'profile rbd' \
  osd 'profile rbd pool=agi-rbd' \
  mgr 'profile rbd pool=agi-rbd' \
  </dev/null > "$CLIENT_DIRECTORY/ceph.client.agirbd.keyring.new"
echo "Credential exit status: $?"
```

After generating the configuration and credential files, verify that both commands completed successfully, then install them to the system directory:

```bash
test -s "$CLIENT_DIRECTORY/ceph.conf.new" &&
test -s "$CLIENT_DIRECTORY/ceph.client.agirbd.keyring.new" &&
sudo install -d -m 700 /etc/ceph/rbd-client &&
sudo install -m 644 "$CLIENT_DIRECTORY/ceph.conf.new" \
  /etc/ceph/rbd-client/ceph.conf &&
sudo install -m 600 "$CLIENT_DIRECTORY/ceph.client.agirbd.keyring.new" \
  /etc/ceph/rbd-client/ceph.client.agirbd.keyring &&
echo "Client files installed successfully"
```

Continue when the success message appears. The `.new` files keep command output separate from the installed files until generation succeeds.

### Define the RBD mapping command

Mapping exposes the RBD image as a device such as `/dev/rbd0` inside `ceph1`. 

Save a script that runs the matching Ceph tools in a container, so that you can reload it after reconnecting by SSH:

```bash
cat > "$HOME/agi-rbd-tools.sh" <<'TOOLS'
CEPH_IMAGE='quay.io/ceph/ceph@sha256:ff836bb28e7d0be0ec4dd22e79407174452a96e11ee62e9cdd1fa47f4bcc3bdc'

rbd_kernel() {
  sudo podman run --rm --privileged --network host \
    --volume /etc/ceph/rbd-client:/etc/ceph:ro \
    --volume /dev:/dev \
    --volume /sys:/sys \
    --volume /lib/modules:/lib/modules:ro \
    --entrypoint /usr/bin/rbd \
    "$CEPH_IMAGE" --id agirbd "$@"
}
TOOLS

source "$HOME/agi-rbd-tools.sh"
sudo modprobe rbd
rbd_kernel info agi-rbd/demo-volume
rbd_kernel device list
```

The privileged container needs access to the devices and sysfs of the VM to configure kernel mappings. The Ceph credential restricts cluster access to the pool but doesn't restrict the privileges of the container within the VM.

Map the RBD image to a kernel block device:

```bash
rbd_kernel device map agi-rbd/demo-volume
```

Set `RBD_DEVICE` to the returned path:

```bash
RBD_DEVICE=/dev/rbd0
rbd_kernel device list
sudo lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS "$RBD_DEVICE"
sudo blockdev --getsize64 "$RBD_DEVICE"
```

Confirm that the device list associates this path with `agi-rbd/demo-volume`. Ensure that the block size is 1 GiB (`1073741824` bytes), and that it has no filesystem or mount point.

#### Allow RBD inspection if AppArmor blocks lsblk

If `lsblk` returns `Permission denied`, verify whether AppArmor blocked access to the RBD sysfs path:

```bash
sudo dmesg --color=never | grep -Ei 'apparmor|denied|rbd|ceph' | tail -n 30
sudo grep -n 'local/' /etc/apparmor.d/lsblk
```

If AppArmor denied `lsblk` access to `/sys/devices/rbd/`, add a read rule to the local profile override and reload AppArmor:

```bash
sudo mkdir -p /etc/apparmor.d/local
sudo tee -a /etc/apparmor.d/local/lsblk >/dev/null <<'EOF_APPARMOR'

# Allow lsblk to inspect kernel-mapped Ceph RBD devices.
/sys/devices/rbd/ r,
/sys/devices/rbd/** r,
EOF_APPARMOR
sudo apparmor_parser -r -T /etc/apparmor.d/lsblk
sudo lsblk -o NAME,SIZE,TYPE,FSTYPE,MOUNTPOINTS "$RBD_DEVICE"
```

When `lsblk` displays the device details without permission errors, you're ready to format the volume.

### Format and verify persistent data

Create a filesystem on the new image so that Linux can store files on it. After confirming the image identity, size, and absence of a filesystem, format it once. Then, mount the filesystem and record the checksum of a test file for later comparisons:

```bash
sudo mkfs.ext4 "$RBD_DEVICE"
sudo mkdir -p /mnt/ceph-rbd
sudo mount "$RBD_DEVICE" /mnt/ceph-rbd
echo "Ceph RBD on $(uname -m)" | sudo tee /mnt/ceph-rbd/hello.txt
sudo sync -f /mnt/ceph-rbd/hello.txt
sudo sha256sum /mnt/ceph-rbd/hello.txt | tee "$HOME/agi-rbd-baseline.sha256"
```

Run checksum reads with `sudo` so that they can access files on the mounted volume. The unprivileged `tee` saves the baseline in your home directory.

Unmount and unmap the image, then map it again:

```bash
cd "$HOME"
sudo umount /mnt/ceph-rbd
rbd_kernel device unmap "$RBD_DEVICE"
rbd_kernel device map agi-rbd/demo-volume
```

Update `RBD_DEVICE` if the new mapping returned a different path. Mount the existing filesystem without formatting it again:

```bash
RBD_DEVICE=/dev/rbd0
sudo mount "$RBD_DEVICE" /mnt/ceph-rbd
sudo sha256sum -c "$HOME/agi-rbd-baseline.sha256"
```

The expected output is:

```output
/mnt/ceph-rbd/hello.txt: OK
```

Keep the volume mounted.

If you disconnect or start a new SSH session on `ceph1`, reload the helper functions and check the device path:

```bash
source "$HOME/agi-rbd-tools.sh"
rbd_kernel device list
```

## What you've accomplished and what's next

You've created an RBD image, mapped it through the Ubuntu 26.04 guest kernel, and verified persistent data. 

Next, you'll add two Ceph hosts and change the pool from one replica to three.
