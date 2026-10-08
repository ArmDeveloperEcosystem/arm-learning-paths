---
title: Prepare and boot a nested L2 guest VM in the hypervisor VM
description: Create an L2 guest VM inside your L1 hypervisor VM and connect to the nested guest over SSH.
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Repeat VM setup in the hypervisor VM

You'll copy the base image and private SSH key from the host to the `fedora-l1-hyper` VM, then install the virtualization tools there. Next, you'll resize the L2 guest disk, create a new seed ISO, and re-run `virt-install` for `fedora-l2-guest`.

## Copy the image and SSH key to the hypervisor

Copy the Fedora cloud image and private SSH key from the host into the hypervisor using `scp`:

```bash
 # In the host: 
 scp -i ~/.ssh/guest_key $IMG ~/.ssh/guest_key fedora@{fedora-l1-hyper IP address}:~/ 
```

## Install the virtualization stack in the hypervisor

Log in to the `fedora-l1-hyper` VM, and install the same virtualization software stack that you installed on the host:

```bash
sudo dnf -y install libvirt libvirt-daemon-qemu libvirt-client qemu-kvm virt-install dnsmasq genisoimage 
```

## Restart the hypervisor VM

After the installation completes, restart the hypervisor VM from the host to start virtualization services:

```bash
 # In the host:
 sudo virsh reboot fedora-l1-hyper 
 # After boot is complete
 ssh -i ~/.ssh/guest_key fedora@{fedora-l1-hyper IP address}
```
Wait for about a minute to be able to connect again with SSH.

## Create the L2 guest image

After the VM restarts, connect to it again and create the L2 guest VM image:

```bash
 export VMDIR="/var/lib/libvirt/images" 
 export IMG="/home/fedora/Fedora-Cloud-Base-Generic-44-1.7.aarch64.qcow2" 
 export DISK_L2_GUEST="/var/lib/libvirt/images/fedora-l2-guest.qcow2" 

 # Prepare the L2 guest image 
 sudo cp "$IMG" "$DISK_L2_GUEST" 
 sudo qemu-img resize "$DISK_L2_GUEST" 40G 
```

## Create a cloud-init seed ISO

Create a seed ISO image for `cloud-config` similar to the other VMs. 

You copied the private key (`~/guest_key`) into the hypervisor earlier. Derive the matching public key from it to use in `ssh_authorized_keys`:

```bash
ssh-keygen -y -f ~/guest_key
```

Use the output of that command in place of `<your-public-key>`:

```bash
 cat > /tmp/user-data <<EOF 
 #cloud-config 
 users:
  - name: fedora
    sudo: ALL=(ALL) NOPASSWD:ALL
    shell: /bin/bash
    ssh_authorized_keys:
      - <your-public-key>
 chpasswd:
   expire: False
 ssh_pwauth: False
 EOF

 cat > /tmp/meta-data <<EOF
 instance-id: my-l2-guest
 local-hostname: my-l2-guest
 EOF
 
 SEEDTMP=$(mktemp -d)
 cp /tmp/user-data "$SEEDTMP/user-data"
 cp /tmp/meta-data "$SEEDTMP/meta-data"
 genisoimage -output ${HOME}/seed_guest.iso \
      -volid cidata -joliet -rock -input-charset utf-8 \
      "$SEEDTMP/user-data" "$SEEDTMP/meta-data"
 sudo cp ${HOME}/seed_guest.iso ${VMDIR}

 rm -rf "$SEEDTMP"
```

## Start the L2 guest VM

Start the L2 guest VM and verify that you can connect:

```bash
 sudo virt-install \
   --name fedora-l2-guest \
   --memory 8192 \
   --vcpus 8 \
   --arch aarch64 \
   --machine virt \
   --disk path=${DISK_L2_GUEST},format=qcow2,bus=virtio \
   --disk path=${VMDIR}/seed_guest.iso,device=cdrom,readonly=on \
   --network network=default,model=virtio \
   --os-variant fedora43 \
   --import \
   --noautoconsole
``` 

## Connect to the L2 guest over SSH

After the VM starts, find its IP address and connect to it with SSH:

```bash
 sudo virsh net-dhcp-leases default
 ssh -i ~/guest_key fedora@{fedora-l2-guest ip address}
```

## What you've accomplished and what's next

You're now connected to an L2 guest VM running inside an L1 hypervisor VM over SSH.

Next, you'll use a synthetic benchmark, `sysbench`, to measure the overhead of running an application inside a nested VM.
