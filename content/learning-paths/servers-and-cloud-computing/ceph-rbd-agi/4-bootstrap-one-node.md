---
title: Bootstrap Ceph on one node
description: Install cephadm, bootstrap the cluster on ceph1, and provision the first OSD.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Start the storage cluster

In this section, you will bootstrap a new Ceph cluster on `ceph1` and provision its data disk as the first OSD. Run all commands inside `ceph1`; the other two VMs will join later. The result is a working single-node cluster, ready to store an RBD image.

## Install cephadm

Use the [standalone cephadm installation method](https://docs.ceph.com/en/squid/cephadm/install/#curl-based-installation) with release 19.2.6. This example uses Ceph Squid 19.2.6, but the Ubuntu 26.04 repositories provide Ceph 20.2.0. To keep the deployment tools and cluster on the same release, download cephadm 19.2.6 directly rather than installing it through the Ubuntu package manager (APT), and use the pinned Ceph 19.2.6 container image.

Download the executable and check its version before installing it:

```bash
(
set -e
mkdir -p "$HOME/ceph-tools"
cd "$HOME/ceph-tools"
curl --fail --show-error --location \
  --output cephadm-19.2.6 \
  https://download.ceph.com/rpm-19.2.6/el9/noarch/cephadm
python3 ./cephadm-19.2.6 version
)
```

Continue only if the command identifies 19.2.6. Stop on a download error or Python traceback. Install the executable and check the host:

```bash
sudo install -m 755 "$HOME/ceph-tools/cephadm-19.2.6" /usr/local/sbin/cephadm
sudo /usr/local/sbin/cephadm version
sudo /usr/local/sbin/cephadm check-host
```

The expected output is:
```output
cephadm version 19.2.6 (f9fd95b4335bad6a26d7a74468f55d269e8dbef4) squid (stable)
podman (/usr/bin/podman) version 5.7.0 is present
systemctl is present
lvcreate is present
Unit chrony.service is enabled and running
Host looks OK
```

## Bootstrap the cluster

Set `CEPH1_IP` to the stable address you recorded for `ceph1`:

```bash
CEPH1_IP=192.168.100.11
CEPH_IMAGE='quay.io/ceph/ceph@sha256:ff836bb28e7d0be0ec4dd22e79407174452a96e11ee62e9cdd1fa47f4bcc3bdc'
sudo podman pull "$CEPH_IMAGE"
sudo podman run --rm --entrypoint /usr/bin/ceph "$CEPH_IMAGE" --version
sudo /usr/local/sbin/cephadm --image "$CEPH_IMAGE" bootstrap --mon-ip "$CEPH1_IP"
```

If you changed the `agi-net` subnet or supplied your own VMs, replace `192.168.100.11` with the address you recorded for `ceph1`. Bootstrap can take several minutes while Ceph downloads container images and starts the first monitor and manager.

You should see the message "Bootstrap complete". At completion, cephadm writes the cluster configuration and administrator keyring under `/etc/ceph/`. Run the administrative commands through `cephadm shell` to use the Ceph client from the cluster's container image:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph --version
sudo /usr/local/sbin/cephadm shell -- ceph -s
sudo /usr/local/sbin/cephadm shell -- ceph versions
sudo /usr/local/sbin/cephadm shell -- ceph orch ps
```

The shell prints the inferred cluster ID, configuration path, and container image before the command output. Compare the container client version with the monitor and manager versions reported by `ceph versions`.

{{% notice Note %}}
Use the pinned container client for administration throughout this path. Squid 19.2.6 introduced the `aes256k` CephX key type; an older userspace client can fail to parse these credentials even when the guest kernel supports them. Upstream kernel support began with Linux 7.0. See the [Ceph key-format compatibility guidance](https://www.ceph.io/en/news/blog/2026/v20-2-4-v19-2-6-combo-released/).
{{% /notice %}}

The status initially reports no OSDs. A warning about the default pool replication count is expected until you add storage.

## Add the first OSD

Ask the orchestrator whether `/dev/vdb` is available:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph orch device ls --hostname ceph1 --wide
```

The expected output is similar to the following. The seed ISO size and refresh times can vary:

```output
HOST   PATH      TYPE  TRANSPORT  RPM  DEVICE ID                      SIZE   HEALTH  IDENT  FAULT  AVAILABLE  REFRESHED  REJECT REASONS
ceph1  /dev/sr0  hdd                  QEMU_CD-ROM_drive-scsi0-0-0-0   368k           N/A    N/A    No         11m ago    Has a FileSystem, Insufficient space (<5GB), read-only
ceph1  /dev/vdb  hdd                                                 10.0G          N/A    N/A    Yes        11m ago
```

For the VMs created in this Learning Path, the device listing should include:

| Device | Purpose | Expected availability |
| --- | --- | --- |
| `/dev/sr0` | Cloud-init seed CD-ROM | `No`: it contains a file system, is read-only, and is smaller than 5 GB. |
| `/dev/vdb` | Empty 10 GB Ceph data disk | `Yes`, with no reject reasons. |

The rejection of `/dev/sr0` is expected. Keep the seed ISO attached and leave it out of OSD provisioning.

Confirm that `/dev/vdb` reports `AVAILABLE: Yes` and is the unused data disk you checked in the previous section. Then give the complete disk to Ceph:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph orch daemon add osd ceph1:/dev/vdb
```

This operation erases and provisions `/dev/vdb`. Wait for the OSD to start, then inspect the result:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph orch ps --hostname ceph1 --daemon-type osd
sudo /usr/local/sbin/cephadm shell -- ceph osd tree
```

The `ceph orch ps` command should report a running OSD, similar to:

```output
NAME   HOST   PORTS  STATUS         REFRESHED  AGE  MEM USE  MEM LIM  VERSION  IMAGE ID      CONTAINER ID
osd.0  ceph1         running (37s)    35s ago  37s    10.4M    4096M  19.2.6   9e014221cd72  a97627c1ce67
```

Times, memory usage, version, image ID, and container ID can vary. The `ceph osd tree` command should show:

```output
ID  CLASS  WEIGHT   TYPE NAME       STATUS  REWEIGHT  PRI-AFF
-1         0.00980  root default
-3         0.00980      host ceph1
 0    hdd  0.00980          osd.0       up   1.00000  1.00000
```

The tree IDs and weight can vary with the cluster and disk capacity.

The output includes one OSD beneath host `ceph1`, with status `up`.

The next section tests the complete client path: the pinned userspace tools, the Ubuntu 26.04 guest kernel, authentication, and persistent filesystem access.

## What you've accomplished and what's next

You've bootstrapped a Ceph monitor and manager and added one OSD on `ceph1`. Next, you'll create an RBD image and use it as a Linux block device.
