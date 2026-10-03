---
title: Booting a nested L2 guest VM in the Hypervisor VM
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Prepare and boot a nested L2 guest VM inside the hypervisor VM 

This process will essentially be identical to the process we followed to create the L1 guest VM on the host. We install all the virtualziation tools we will need in our Hypervisor VM, copy the base image from the host to the fedora-l1-hyper VM, resize its disk, create a new seed ISO, and re-run virt-install for fedora-l2-guest. 

1. Copy the Fedora cloud image and private SSH key from the host into the hypervisor using scp.

   ```
    # In the host: 
    scp –i /path/to/private/key $IMG /path/to/private/key fedora@{fedora-l1-hyper IP address}:~/ 
   ```

2. Log in to the `fedora-l1-hyper` VM, and install the same virtualization software stack as we installed on the host: 
   ```
    sudo dnf -y install libvirt libvirt-daemon-qemu libvirt-client qemu-kvm virt-install dnsmasq genisoimage 
   ```

3. After the installation has completed, restart the hypervisor VM from the host to start virtualization services. You will need to wait a minute to be able to connect again with SSH: 
   ```
    # In the host:
    sudo virsh reboot fedora-l1-hyper 
    # After boot is complete
    ssh -i /path/to/private/key fedora@{fedora-l1-hyper IP address}
   ```

4. After the VM restarts, connect to it again and create the L2 guest VM image:
   ```
    export VMDIR="/var/lib/libvirt/images" 
    export IMG="/home/fedora/Fedora-Cloud-Base-Generic-44-1.7.aarch64.qcow2" 
    export DISK_L2_GUEST="/var/lib/libvirt/images/fedora-l2-guest.qcow2" 

    # Prepare the L2 guest image 
    sudo cp "$IMG" "$DISK_L2_GUEST" 
    sudo qemu-img resize "$DISK_L2_GUEST" 40G 
   ```

5. Create a seed ISO image for `cloud-config` similar to the other VMs. 

   ```
    cat > /tmp/user-data <<EOF 
    # cloud-config 
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

6. Now start the L2 guest VM and verify that you can connect: 
   ```
    sudo virt-install \
      --name fedora-l2-guest \
      --memory 8192 \
      --vcpus 8 \
      --arch aarch64 \
      --machine virt \
      --disk path=${DISK_L2_GUEST},format=qcow2,bus=virtio \
      --disk path=/path/to/seed_guest.iso,device=cdrom,readonly=on \
      --network network=default,model=virtio \
      --os-variant fedora43 \
      --import \
      --noautoconsole
   ``` 

7. After the VM is started, find its IP address and connect to it with SSH.
   ``` 
    sudo virsh net-dhcp-leases default
    ssh –i /path/to/private_key fedora@{fedora-l2-guest ip address}
   ```

Congratulations! You are now connected to an L2 guest VM  running inside an L1 hypervisor VM over SSH.  

In the next step, we will use a common synthetic benchmark, sysbench, to measure the overhead of running an application inside a nested VM. To minimize any resource conflicts or CPU scheduling issues, we will pin all VMs to a fixed set of cores.

