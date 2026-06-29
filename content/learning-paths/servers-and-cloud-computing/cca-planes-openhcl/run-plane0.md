---
# User change
title: "Boot plane 0 Linux"

weight: 4

# Do not modify these elements
layout: "learningpathall"
---

## Run the FVP

Make sure that `FVP_Base_RevC-2xAEMvA` is available in your `PATH`.

Start the CCA stack on the FVP:

```console
shrinkwrap run cca-3world.yaml --overlay cca-planes-lp.yaml --overlay planes.yaml \
    --rtvar ROOTFS=$(realpath "$SHRINKWRAP_PACKAGE/cca-3world/rootfs.ext2")
```

Log in to the CCA host as `root`. No password is required.

## Start a Realm with plane 0 Linux

Change to the directory that contains the CCA demo files:

```console
cd /cca
```

Start the Realm with the plane 0 kernel, 9P sharing, and a 32 MB huge page for the auxiliary plane payload:

```console
./lkvm run --realm --disable-sve --irqchip=gicv3-its \
    -c 1 -m 512 --no-pvtime --force-pci --console virtio \
    --kernel /cca/Image_ohcl --9p /cca/,cca_mount \
    -p "console=hvc0 root=/dev/vda2 hugepagesz=32M hugepages=1" \
    --measurement-algo=sha256 --restricted_mem
```

The plane 0 Linux kernel boots inside the Realm. Log in as `root` when the login prompt appears.

## Prepare shared files and huge pages

Create a mount point for the 9P share:

```console
mkdir -p /root/mount
mount -t 9p -o trans=virtio cca_mount /root/mount
```

Create the hugetlbfs mount used by `tmk_vmm`:

```console
mkdir -p /root/huge
mount -t hugetlbfs -o pagesize=32768kB,size=32768kB none /root/huge
```

Confirm that the test binaries are visible from plane 0:

```console
ls /root/mount/simple_tmk /root/mount/tmk_vmm
```

The output should show both files:

```output
/root/mount/simple_tmk
/root/mount/tmk_vmm
```

## What you've accomplished

You have booted plane 0 Linux inside a CCA Realm and prepared the shared filesystem and huge page needed by the auxiliary plane test.
