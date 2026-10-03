---
title: Preparing and Starting an L1 Guest Virtual Machine
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Preparing and Starting an L1 Guest VM

Before we create a nested VM, we will create an L1 Guest VM which will be running on our host, so that we have an unnested VM to compare the performance overhead of virtualization with the additional overnead of nested virtualization, and to compare the additional work required to create an L1 hypervisor VM at the next step.

To create a VM, we will first download a cloud image, make some configuration changes to the base image using cloud-config, and install and start the VM using `virt-install`. Once we have started the VM, we will connect to it to confirm that it has started correctly.

1. Download an Arm64 cloud image to use for the VMs. To be consistent with the host, we use Fedora 44, but any recent Linux distribution will do:
   ```
      curl -LO https://dl.fedoraproject.org/pub/fedora/linux/releases/42/Cloud/aarch64/images/Fedora-Cloud-Base-Generic-42-1.1.aarch64.qcow2 
   ```

2. We will make copies of our base disk image and resize it to give the VM more disk space. For convenience, we also set some environment variables: 
   ``` 
    export VMDIR="/var/lib/libvirt/images” 
    export IMG="${HOME}/Fedora-Cloud-Base-Generic-42-1.1.aarch64.qcow2" 
    export DISK_L1_GUEST="${VMDIR}/fedora-l1-guest.qcow2" 

    # Prepare the L1 guest image 
    sudo cp "$IMG" "$DISK_L1_GUEST" 
    sudo qemu-img resize "$DISK_L1_GUEST" 40G 
   ```

3. Create a seed ISO image for `cloud-init`. `cloud-init` will run automatically the first time that we instantiate the virtual machine, and can perform some initialization actions for us. `cloud-init` looks for special files called `meta-data` and `user-data` for configuration information. In this case, we want to create a default unprivileged user (fedora), ensure that the user has permission to run commands as root using `sudo` without a password, and that our public SSH key is included in the `authorized_keys` of that user so that we can SSH into the virtual machine from the host. If you do not have a public/private key-pair, this is a good time to generate the pair, and use the public key file here.

   After creating these files, we will generate a special CD disk image (format ISO) which will be attached to the VM when we instantiate it. Once we have the ISO image, we copy it to the same directory as the qcow2 VM image we created in the previous step.

   ```
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
    instance-id: my-guest 
    local-hostname: my-guest 
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

4. Start the L1 guest VM using `virt-install`. The `virt-install` command includes parameters for our VM image, the ISO CD image we created for `cloud-config`, a "name" parameter to identify the image with `virsh` and `virt-manager`, and parameters for the number of virtual CPUs and amount of memory that will be allocated to the VM. The `os-variant` argument passes hints about what operating system will be running - at the time of writing, `fedora44` is not an accepted option, but any recent `fedoraXX` value should work.

   ```
    sudo virt-install \
      --name fedora-l1-guest \
      --memory 8192 \
      --vcpus 8 \
      --arch aarch64 \
      --machine virt \
      --disk path=${DISK_L1_GUEST},format=qcow2,bus=virtio \
      --disk path=${VMDIR}/seed_guest.iso,device=cdrom,readonly=on \
      --network network=default,model=virtio \
      --os-variant fedora42 \
      --import \
      --noautoconsole 
   ```

5. After the VM is started, which takes a few seconds, we will get its IP address and connect to it using SSH.
   ```  
    sudo virsh net-dhcp-leases default 
    # The IP address of the VM will be in the output of this command once it has finished booting
    ssh –i /path/to/private_key fedora@{ip address}
   ```

At this point, you should be connected to the L1 guest VM over SSH.

In the next step, we will instantiate a hypervisor VM, which will require some additional configuration steps. Once you have verified that we can connect to the L1 Guest VM, you can exit the shell to return to the host environment.

