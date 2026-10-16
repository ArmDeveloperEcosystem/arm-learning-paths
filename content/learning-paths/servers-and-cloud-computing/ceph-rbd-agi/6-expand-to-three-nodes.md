---
title: Expand Ceph to three nodes
description: Add ceph2 and ceph3, deploy their OSDs and monitors, and increase the RBD pool to three replicas.
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Replicate data across three nodes

You'll add the prepared `ceph2` and `ceph3` virtual machines (VMs) to the existing cluster. Then, you'll increase the RADOS Block Device (RBD) pool from one copy of its data to three. Start on the AGI host to authorize SSH access, then administer the cluster from `ceph1`. Keep the RBD volume mounted so that you can check the same file after replication completes.

### Authorize cephadm on the new nodes

Cephadm uses SSH to deploy and manage services on the additional nodes. 

Start in a terminal on the AGI host with the SSH key at `~/.ssh/agi_ceph`.

Retrieve the public SSH key of the cluster from `ceph1`:

```bash
ssh -o ConnectTimeout=10 -i "${HOME}/.ssh/agi_ceph" \
  ubuntu@192.168.100.11 'sudo -n cat /etc/ceph/ceph.pub' \
  > /tmp/agi-ceph-cluster.pub
ssh-keygen -lf /tmp/agi-ceph-cluster.pub
```

Install that public key using the existing `ubuntu` access on each new node:

```bash
for VM_NUMBER in 2 3; do
  VM_IP="192.168.100.$((10 + VM_NUMBER))"
  ssh -o ConnectTimeout=10 -o BatchMode=yes \
    -i "${HOME}/.ssh/agi_ceph" "ubuntu@${VM_IP}" \
    'sudo -n install -d -m 700 /root/.ssh &&
     sudo -n touch /root/.ssh/authorized_keys &&
     sudo -n chmod 600 /root/.ssh/authorized_keys &&
     sudo -n tee -a /root/.ssh/authorized_keys >/dev/null' \
    < /tmp/agi-ceph-cluster.pub
done
```

This authorizes the cephadm root SSH key without enabling password login or copying the private key of the AGI host. 

Return to the SSH session on `ceph1` for all remaining commands. 

Add both hosts with their stable addresses: 

```bash
sudo /usr/local/sbin/cephadm shell -- ceph orch host add ceph2 192.168.100.12
sudo /usr/local/sbin/cephadm shell -- ceph orch host add ceph3 192.168.100.13
sudo /usr/local/sbin/cephadm shell -- ceph orch host ls
```

The hostnames passed to `ceph orch host add` match the output of `hostname` on each VM.

### Add the other OSDs

Each additional object storage daemon (OSD) provides a storage location for another copy of the pool's data. Confirm that each new data disk is available:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph orch device ls --hostname ceph2 --wide --refresh
sudo /usr/local/sbin/cephadm shell -- ceph orch device ls --hostname ceph3 --wide --refresh
```

After you confirm `/dev/vdb` is the intended empty disk on both nodes, create the OSDs:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph orch daemon add osd ceph2:/dev/vdb
sudo /usr/local/sbin/cephadm shell -- ceph orch daemon add osd ceph3:/dev/vdb
```

Wait until all three OSDs are `up` and `in`:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph osd tree
```

The tree should show one OSD beneath each of `ceph1`, `ceph2`, and `ceph3`. A container reporting `running` doesn't prove the OSD is `up`. Wait for the OSD tree and cluster status to agree before increasing replication.

### Place monitors on all three nodes

Monitors maintain the cluster maps and use a majority to agree on cluster state. Deploy a monitor on each node:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph orch apply mon --placement="ceph1,ceph2,ceph3"
sudo /usr/local/sbin/cephadm shell -- ceph orch ps --daemon-type mon
```

Run `sudo /usr/local/sbin/cephadm shell -- ceph -s` and wait until quorum includes all three hosts. An odd number of monitors allows a majority to form if one monitor becomes unavailable.

### Increase the pool replication

Confirm that the pool uses a replicated CRUSH rule with `host` as its failure domain:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph osd pool get agi-rbd crush_rule
sudo /usr/local/sbin/cephadm shell -- ceph osd crush rule dump replicated_rule
```

In the rule output, find the step containing `chooseleaf` and confirm that its type is `host`. If your pool uses a differently named rule, substitute that rule name in the second command.

Set `size` to `3` to keep a copy on each virtual host, and `min_size` to `2`:

```bash
sudo /usr/local/sbin/cephadm shell -- ceph osd pool set agi-rbd size 3
sudo /usr/local/sbin/cephadm shell -- ceph osd pool set agi-rbd min_size 2
watch sudo /usr/local/sbin/cephadm shell -- ceph -s
```

These values ensure that I/O can continue during a single-OSD outage.

Ceph copies existing pool data to the new OSDs through backfill. 

Stop `watch` with **Ctrl+C** after all placement groups return to `active+clean`. The new replica count is then satisfied.

Confirm that the file remains available:

```bash
sudo cat /mnt/ceph-rbd/hello.txt
```

The expected output is:

```output
Ceph RBD on aarch64
```

## What you've accomplished and what's next

You've expanded the cluster to three virtual hosts and changed the RBD pool to three host-level replicas. 

Next, you'll stop one OSD and observe degraded operation and recovery.
