---
title: Guest and host setup
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## A few tips about Void Linux

For a detailed guide on Void Linux, refer to the [documentation][1].

Commands in this section are executed on the guest system.

It is recommended to use Bash as your default shell on the guest system. To change
the default shell for a user, run this command:

```bash
chsh -s /bin/bash root
```

If you need to install some package, use the following commands:

```bash
# Update repository cache (you need to run this once)
xbps-install -y -S

# Install vim package (for example):
xbps-install -y vim
```

We can add a bit of automation to speed up configuring your system from scratch:

```bash
# Install packages: required and optional
required=(nfs-utils sv-netmount rpcbind)
optional=(vim binutils make strace python3)
for p in "${required[@]}" "${optional[@]}"; do
  xbps-query -l | grep -w ${p} > /dev/null || {
    xbps-install -y ${p}
  }
done
```

Installing the required packages is important for the following steps. Choose
optional packages according to your use case. You can always install or remove
packages later.

The rootfs image that we are using is limited in size, and it might be useful
to free up some space. Since we use our own kernel and firmware, we can safely
delete the following packages:

```bash
# Remove unused packages:
unused=(rpi-firmware rpi-kernel)
for p in "${unused[@]}"; do
  test -f "/etc/xbps.d/disable-${p}.conf" || {
    echo "ignorepkg=${p}" > "/etc/xbps.d/disable-${p}.conf"
    xbps-remove -y ${p}
  }
done
```

Here, we also mask these packages to prevent them from being installed automatically
during system updates, saving time in the process.

The last two code snippets are written so that you can re-run them multiple times.
If a change has already been applied, it will be skipped.

Optionally, to update your guest OS, run:

```bash
xbps-install -y -Su
```

## Lightweight SSH server

Commands in this section are executed on the guest system.

Our main interaction with the guest system will be via SSH. Running software on an
FVP is slower than on real hardware, so we want to reduce the overhead. One way to
do this is by replacing the preinstalled OpenSSH server with a more lightweight
alternative, such as [Dropbear][2].

First, install Dropbear and enable corresponding service:

```bash
# Install Dropbear server
xbps-query -l | grep -w dropbear > /dev/null || {
  xbps-install -y dropbear
}

# Enable Dropbear SSH server service
test -h /var/service/dropbear || {
  ln -s /etc/sv/dropbear /var/service/
}
```

Now, disable the OpenSSH server:

```bash
# Disable OpenSSH server service
test -h /var/service/sshd && {
  sv stop sshd
  rm -vf /var/service/sshd
}
```

Finally, create a simple service that prints a message to the system log when the guest
system is ready for incoming SSH connections:

```bash
# Create service to indicate SSH readiness
test -h /var/service/hello || {
  mkdir -p /etc/sv/hello
  cat <<EOF > /etc/sv/hello/run
#!/bin/bash
sv status dropbear || exit 1
. /etc/runit/functions
msg "SSH service is ready"
sv stop hello
EOF
  chmod a+x /etc/sv/hello/run
  ln -s /etc/sv/hello /var/service/
}
```

During the next boot, you should see this message in the system log. You might also
experience an improvement in SSH connection speed:

```
=> Initialization complete, running stage 2...
...
=> SSH service is ready

```

## Configure SSH on host

Commands in this section should be run on the host system.

Using a password for SSH can be inconvenient when automating tasks. The solution is
to set up authentication via SSH keys. Since we are using the Dropbear server, we need
to use the Dropbear client and configure SSH keys for it.

First, install the Dropbear client:

```bash
sudo apt install dropbear-bin
```

To avoid typing the guest system's IP address every time, add it to `/etc/hosts`:

```
172.17.0.2 fvp
```

Now, create an SSH key and upload its public part to the guest system:

```bash
test -f ~/.ssh/id_dropbear || dropbearkey -t rsa -f ~/.ssh/id_dropbear
dbclient -l root -p 8022 fvp mkdir -p .ssh
dropbearkey -y -f ~/.ssh/id_dropbear | grep "^ssh-rsa " | \
dbclient -l root -p 8022 -T fvp "cat >> .ssh/authorized_keys"
```

Check that you can SSH into the guest system using the Dropbear SSH client without
entering a password:

```bash
dbclient -l root -p 8022 fvp
```

## Non-root user

Commands in this section are executed on the guest system.

Creating a non-root user in the guest system can be practical. Additionally, we will
copy the same SSH key used for the root user to avoid setting up different key pair
and having to alternate between them. For a non-root user in the guest system we
will use the same username `user` as on your host system.

```bash
# Create user
id -u user 2> /dev/null || {
  useradd -m -s /bin/bash user
  test -d /home/user/.ssh || {
    mkdir -p /home/user/.ssh
    chown user:user /home/user/.ssh
    chmod 0700 /home/user/.ssh
  }
  test -f /root/.ssh/authorized_keys && {
    cp /root/.ssh/authorized_keys /home/user/.ssh/authorized_keys
    chown user:user /home/user/.ssh/authorized_keys
    chmod 0600 /home/user/.ssh/authorized_keys
  }
}
```

Now, you should be able to SSH into the guest system running on the FVP as a non-root user
without having to enter a password:

```bash
dbclient -p 8022 fvp
```

## Shared workspace

Commands in this section are executed first on the host system and then on the guest.

It is useful to share a folder between the host and guest systems to facilitate file exchange.
This is especially useful for running Glibc tests, as we will see in the following steps.

To enable file sharing, we leverage the local network set up by Docker and configure an NFS
share. The FVP offers a Plan 9 filesystem protocol server as an alternative to using NFS,
but it does not currently support some file system operations such as `flock` which is used,
for example, by the Glibc tests, so it is not suitable for our use case.

On your host, install the NFS server (this example is for Debian or Ubuntu):

```bash
sudo apt install nfs-kernel-server
sudo systemctl disable nfs-kernel-server
```

Add this line to the `/etc/exports` file (we presume that host user ID is `1000` and group ID
is `1000`, amend according to your actual setup):

```
/home/user/workspace 172.17.0.0/24(rw,sync,no_subtree_check,all_squash,anonuid=1000,anongid=1000,insecure)
```

We allow access only from clients within the Docker network (`172.17.0.0/24`) and use the `insecure`
option to avoid complexities of requiring privileged ports on the guest system. To ensure that
the file permissions are aligned between the guest and the host systems, we also specify `anonuid`
and `anongid` options.

Restart the NFS server for the changes to take effect:

```bash
sudo systemctl restart nfs-kernel-server
```

Now, SSH into the guest system as root and continue the setup on the guest side:

```bash
mkdir -p /home/user/workspace
chown user:user /home/user/workspace
```

Edit the guest system's `/etc/fstab` to mount the NFS share automatically when the system running
on the FVP boots:

```bash
grep "FVP NFS shared folder" /etc/fstab > /dev/null || {
  echo "# FVP NFS shared folder" >> /etc/fstab
  echo "172.17.0.1:/home/user/workspace /home/user/workspace nfs4 defaults,_netdev 0 0" >> /etc/fstab
}
```

Finally, enable the necessary services for the NFS mounting:

```bash
services=(netmount rpcbind statd)
for s in "${services[@]}"; do
  test -h /var/service/${s} || {
    ln -s /etc/sv/${s} /var/service/
  }
done
```

At the next boot, you should be able to SSH into the guest system as a non-root user and
access files in the workspace directory, which should be synchronized between the guest
and the host systems.

## More configuration

The following changes to the guest system configuration help reduce host memory usage by the
FVP:

```bash
# Disable ASLR (helps reduce host memory usage by the FVP process):
mkdir -p /etc/sysctl.d
test -f /etc/sysctl.d/01-disable-aslr.conf || {
  echo "kernel.randomize_va_space = 0" > /etc/sysctl.d/01-disable-aslr.conf
}
```

These changes also help prevent the OOM (Out of Memory) killer from unnecessarily terminating
processes on the guest system when they consume too much memory:

```bash
mkdir -p /etc/sysctl.d
test -f /etc/sysctl.d/02-disable-vm-overcommit.conf || {
  echo "vm.overcommit_memory = 2" > /etc/sysctl.d/02-disable-vm-overcommit.conf
}
```

We are now ready to do something substantial with our Linux system running on the FVP. Let's
build the Glibc from source and run its tests on the FVP.


[1]: https://docs.voidlinux.org/
[2]: https://matt.ucc.asn.au/dropbear/dropbear.html
