---
title: Test degraded operation and recovery
description: Stop one OSD, verify that the RBD data remains readable, and watch Ceph return to a healthy state.
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verify access during an OSD outage

You'll test whether the replicated RBD volume stays readable and writable when one OSD stops. Run all commands on `ceph1`, using the mounted volume and checksum baseline from the RBD exercise. You'll restore the OSD and verify both the original file and a file written during the outage.

## Record the healthy state

On `ceph1`, confirm that the cluster is healthy before introducing a failure:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph -s
sudo /usr/local/sbin/cephadm shell -- ceph osd tree
sudo sha256sum -c "$HOME/agi-rbd-baseline.sha256"
```

The checksum check should report `OK`. 

Make sure to reload the helper with `source "$HOME/agi-rbd-tools.sh"` if this is a new SSH session. 

Use `rbd_kernel device list` to identify the mapping for `agi-rbd/demo-volume` and set `RBD_DEVICE` to that path. The cluster should report three OSDs `up` and `in`, and all placement groups should be `active+clean`.

## Stop one OSD

Stop the OSD on `ceph3` to test loss of one storage daemon while keeping the rest of the cluster running. 

First, identify its daemon name:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph orch ps --hostname ceph3 --daemon-type osd
```

Copy the daemon name from the `NAME` column, such as `osd.2`, and assign it to `OSD_NAME`:

```bash
OSD_NAME=osd.2
sudo /usr/local/sbin/cephadm shell -- ceph orch daemon stop "$OSD_NAME"
```

Inspect the cluster:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph -s
sudo /usr/local/sbin/cephadm shell -- ceph osd tree
```

Wait for the OSD tree to report the selected OSD `down` and the other two `up`. The health status reports degraded redundancy. Keep the outage brief. Because the pool has three copies and `min_size` is two, the mapped RBD volume remains available. 

Verify the file and its checksum:

```bash
sudo cat /mnt/ceph-rbd/hello.txt
sudo sha256sum -c "$HOME/agi-rbd-baseline.sha256"
```

The baseline check should report `OK`. Now write new data and flush it to storage while the OSD is down:

```bash
sudo timeout 30s dd if=/dev/urandom of=/mnt/ceph-rbd/during-outage.bin \
  bs=1M count=8 conv=fsync status=progress
```

Save the new file's checksum outside the RBD volume, then unmount and remount to check persistence:

```bash
sudo sha256sum /mnt/ceph-rbd/during-outage.bin | tee "$HOME/agi-rbd-outage.sha256"
cd "$HOME"
sudo umount /mnt/ceph-rbd
sudo mount "$RBD_DEVICE" /mnt/ceph-rbd
sudo sha256sum -c "$HOME/agi-rbd-baseline.sha256"
sudo sha256sum -c "$HOME/agi-rbd-outage.sha256"
```

Both checks should report `OK`.

## Restore the OSD

Restart the stopped OSD to restore the third copy of the pool's data:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph orch daemon start "$OSD_NAME"
watch sudo /usr/local/sbin/cephadm shell -- ceph -s
```

Ceph detects the returning OSD and repairs any objects that changed while it was unavailable. Stop `watch` with Ctrl+C after the cluster returns to `HEALTH_OK` and all placement groups are `active+clean`.

Verify both files again after recovery:

```bash
sudo sha256sum -c "$HOME/agi-rbd-baseline.sha256"
sudo sha256sum -c "$HOME/agi-rbd-outage.sha256"
```

Both checks should report `OK`.

## Clean up the mapped volume

When you are done, unmount and unmap the RBD image. 

Reload the helper first if this is a new SSH session, then identify the current mapping:

```bash
source "$HOME/agi-rbd-tools.sh"
rbd_kernel device list
```

Set `RBD_DEVICE` to the path shown for `agi-rbd/demo-volume`, then unmount every mount point for that device and unmap it:

```bash
RBD_DEVICE=/dev/rbd0
sudo umount -A "$RBD_DEVICE" 2>/dev/null || true
rbd_kernel device unmap "$RBD_DEVICE"
```

Using `umount -A` with the device path unmounts the device wherever it is mounted, even if the mount point differs from `/mnt/ceph-rbd`.

If the unmap reports `Device or resource busy`, first confirm the device is not mounted and no process holds it open:

```bash
findmnt --source "$RBD_DEVICE"
sudo fuser -vm "$RBD_DEVICE"
```

If both commands report nothing, the kernel can still hold a watch on the image, which keeps the mapping busy even with no filesystem mounted. Confirm the device is unmounted, then force the unmap:

```bash
rbd_kernel device unmap -o force "$RBD_DEVICE"
rbd_kernel device list
```

Confirm the image is no longer mapped:

```bash
rbd_kernel device list
```

The list should no longer show `agi-rbd/demo-volume`. This leaves the Ceph cluster and RBD image in place for further exploration.

## What you've accomplished and learned

You've built a three-node Ceph cluster on Arm virtual machines, used RBD as Linux block storage, and verified data availability and integrity during an OSD outage and recovery. You've learned how replication settings and CRUSH placement work together to protect data, and how to monitor cluster health.

You also learned about OSD recovery. Protecting against physical-host failure requires spreading the cluster across independent hosts. You can apply the same Ceph concepts to independent Arm servers and define failure domains that match the physical infrastructure.
