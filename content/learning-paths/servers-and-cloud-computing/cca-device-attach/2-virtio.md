---
title: "Device attach: virtio"
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

This section introduces VirtIO and Bounce Buffers in the context of CCA Realms, and explains how they enable secure data exchange between a Realm and the untrusted external world.

A Realm must use physical devices at some point to interact with the external
and or physical world. The easiest way to achieve this is by using VirtIO, which
provides a fast, high-level emulation layer. This can be viewed as the first level of
device attach.

More advanced device attach features can be
performed leveraging hardware security features like PCIe-TDISP (**T**EE
**D**evice **I**nterface **S**ecurity **P**rotocol) and PCIe-IDE (**I**ntegrity
and **D**ata **E**ncryption), where the host OS assigns a physical device to
a Realm. The Realm can then make security measurements on the physical device and include those in its attestation base.

## VirtIO

Learn how VirtIO provides an efficient, paravirtualized I/O interface between Realms and host devices.

### What is VirtIO ?

VirtIO is an abstraction layer for virtual devices in virtualized environments.
It provides standardized and efficient interfaces between guest virtual machines
(VMs) and host devices, making it easier to develop paravirtualized drivers.

Paravirtualized means that the guest OS is aware it’s running in a virtualized
environment and can use optimized drivers (VirtIO) to communicate with virtual
hardware. Emulating physical hardware devices (like NICs or disks) for VMs is slow and
inefficient. VirtIO allows VMs to bypass full device emulation and use streamlined drivers.

VirtIO is most commonly used with KVM/QEMU virtualization. Example drivers include:
- `virtio-net`: Paravirtualized networking
- `virtio-blk`: Block device (disk) access
- `virtio-fs`: File sharing (host ↔ guest)
- `virtio-balloon`: Dynamic memory management
- `virtio-rng`: Random number source
- `virtio-console`: Simple console interface
- ...

### How VirtIO works in VMs

Here is an overview of how VirtIO works in Virtual Machines:

1. The Host Hypervisor (for example, QEMU/KVM) exposes VirtIO backend devices.
2. The guest OS loads VirtIO _frontend_ drivers (for example, `virtio_net`,
   `virtio_blk`) that communicate using the VirtIO protocol.
3. Communication happens via shared memory (`virtqueues`) for I/O operations,
   avoiding full device emulation.
4. Devices are exposed over the PCI or MMIO bus to the guest.

For example, instead of emulating an Intel e1000 NIC, the host exposes a `virtio-net` interface, and the guest OS uses the `virtio-net` driver to send and receive packets via shared buffers.

## Bounce buffers

### What are bounce buffers?

Bounce buffers are temporary memory buffers used when Direct Memory Access (DMA) cannot be performed directly on the original data buffer. This might be because:

1. The original buffer is not physically contiguous
2. The buffer is in high memory or not accessible to the device
3. The buffer does not meet alignment or boundary constraints required by the device

## Why use bounce buffers?

Data _bounces_ between:
- The original buffer (in user or kernel space) and
- The DMA-capable bounce buffer (used for I/O with the device)

This ensures that data transfer is possible even when the original memory isn’t suitable for DMA.

## CCA Realms, VirtIO and bounce buffers

The defining feature of a Realm is that its memory (called *Realm memory*) is
cryptographically isolated from both the Normal and Secure Worlds. 

This means that:
- Realm memory is encrypted with unique keys
- Non-Realm entities (host OS, hypervisor) cannot directly read or
  write to Realm memory
- Even Direct Memory Access (DMA) from peripherals or untrusted drivers cannot
  access Realm data

This design ensures confidentiality but introduces a problem: How can Realms
interact with untrusted components, such as:
- Network stacks in the host OS,
- Storage subsystems,
- I/O devices managed by untrusted drivers?

To exchange data securely with untrusted components (for example, network stacks, storage subsystems), Realms use bounce buffers as intermediaries.

### How bounce buffers are used with RME

1. Exporting Data:
   - A Realm application prepares some data (for example, the results of computation)
   - It copies this data from protected Realm memory into a bounce buffer.
   - The Realm notifies the untrusted host or hypervisor that the data is ready.
   - The host retrieves the data from the bounce buffer.

2. Importing Data:
   - The host places data (e.g., input from a file or device) into a bounce buffer.
   - The Realm is notified and validates the source.
   - The Realm copies the data from the bounce buffer into its protected memory.

This pattern preserves confidentiality and integrity of Realm data, since:
- The Realm never allows direct access to its memory.
- It can validate and sanitize any data received via bounce buffers.
- No sensitive data is exposed without explicit copying.

### Confidentiality preserved with bounce buffers, really?

In the previous section, it was mentioned that bounce buffers preserve
confidentiality. Lets dive a little deeper into that. Bounce buffers
are nothing more than an explicitly shared temporary area between the Realm
world and the outside world. This does indeed preserve the confidentiality of
all the rest of the Realm data. On the other hand, for the data being
transferred, it is leaving the Realm world and will only remain confidential if it
is encrypted in some way, e.g. for network traffic, TLS should be used.

## Seeing a Realm's bounce buffers at work

Let's put this to work and check for ourselves that bounce buffers are used. The
steps in this section will build on the Key Broker demo that was used in the [CCA
Essentials learning path](/learning-paths/servers-and-cloud-computing/cca-essentials/example/),
demonstrating an end-to-end attestation.

### Start the Key Broker Server (KBS)

First, pull the docker container image with the pre-built KBS, and then run the container:

```bash
docker pull armswdev/cca-learning-path:cca-key-broker-v2 
docker run --rm -it armswdev/cca-learning-path:cca-key-broker-v2
```

Now within your running docker container, get a list of network interfaces:

```bash
ip -c a
```

The output should look like:

```output
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
20: eth0@if21: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:ac:11:00:02 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 172.17.0.2/16 brd 172.17.255.255 scope global eth0
       valid_lft forever preferred_lft forever
```

Start the KBS on the `eth0` network interface, and replace 172.17.0.2 shown in
the command below with the IP address corresponding to eth0 in the output of `ip
-c a` above.

```bash
./keybroker-server -v --addr 172.17.0.2
```

The output should look like:

```output
INFO starting 16 workers
INFO Actix runtime found; starting in Actix runtime
INFO starting service: "actix-web-service-172.17.0.2:8088", workers: 16, listening on: 172.17.0.2:8088
```

### Get into a Realm

With the Key Broker Server running in one terminal, open up a new terminal in
which you will run the Key Broker Client (KBC). The intent is to
observe that the data transmitted over the network (thru `virtio_net`) are
indeed using bounce buffers.

Pull the docker container image with the pre-built KBC, and then run the container:

```bash
docker pull armswdev/cca-learning-path:cca-simulation-v2
docker run --rm -it armswdev/cca-learning-path:cca-simulation-v2
```

Within the running container, launch the `run-cca-fvp.sh` script to run the Arm
CCA pre-built binaries on the FVP:

```bash
./run-cca-fvp.sh
```
The `run-cca-fvp.sh` script uses the screen command to connect to the different
UARTs in the FVP.

You should see the host Linux kernel boot on your terminal and you will be
prompted to log in to the host. Enter root as the username:

```output
[    4.169458] Run /sbin/init as init process
[    4.273748] EXT4-fs (vda): re-mounted 64d1bcff-5d03-412c-83c6-48ec4253590e r/w. Quota mode: none.
Starting syslogd: OK
Starting klogd: OK
Running sysctl: OK
Starting network: [    5.254843] smc91x 1a000000.ethernet eth0: link up, 10Mbps, half-duplex, lpa 0x0000
udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 172.20.51.1, server 172.20.51.254
udhcpc: lease of 172.20.51.1 obtained from 172.20.51.254, lease time 86400
deleting routers
adding dns 172.20.51.254
OK

Welcome to the CCA host
host login: root
(host) #
```

Change directory to `/cca` and use `lkvm` to launch a guest Linux in a Realm:
```bash
cd /cca
./lkvm run --realm --disable-sve --irqchip=gicv3-its --firmware KVMTOOL_EFI.fd -c 1 -m 512 --no-pvtime --disk guest-disk.img --restricted_mem --virtio-transport pci --pmu --network mode=user
```

You should see the realm boot. Note that `lkvm` is invoked with `--network
mode=user`, which makes the guest see the network through a VirtIO device.

After boot up, which might take some time, you will be prompted to log in at the
guest Linux prompt. Use root again as the username:

```output
Starting syslogd: OK
Starting klogd: OK
Running sysctl: OK
Starting network: udhcpc: started, v1.36.1
udhcpc: broadcasting discover
udhcpc: broadcasting select for 192.168.33.15, server 192.168.33.1
udhcpc: lease of 192.168.33.15 obtained from 192.168.33.1, lease time 14400
deleting routers
adding dns 172.20.51.254
OK

Welcome to the CCA realm
realm login: root
(realm) #
```

### Observe bounce buffer usage in the realm

First, check that the Linux kernel has tracing support:

```bash { output_lines="2-46" }
ls /sys/kernel/debug/tracing/events/
9p                       i2c_slave                qcom_glink
alarmtimer               icmp                     qcom_smp2p
asoc                     initcall                 qdisc
block                    interconnect             ras
bpf_test_run             io_uring                 raw_syscalls
bpf_trace                iomap                    rcu
bridge                   iommu                    regmap
capability               ipi                      regulator
cgroup                   irq                      rpcgss
chipidea                 jbd2                     rpm
clk                      kmem                     rpmh
cma                      ksm                      rseq
compaction               kvm                      rtc
cpuhp                    kyber                    sched
cros_ec                  libata                   scmi
csd                      lock                     scsi
dev                      lockd                    signal
devfreq                  maple_tree               skb
devlink                  mdio                     smbus
dma                      memcg                    sock
dma_fence                migrate                  spi
dpaa2_eth                mmap                     spmi
dpaa_eth                 mmap_lock                sunrpc
dwc3                     mmc                      swiotlb
e1000e_trace             module                   task
enable                   mtu3                     tcp
error_report             musb                     tegra_apb_dma
ext4                     napi                     thermal
fib                      neigh                    thermal_power_allocator
filelock                 net                      thp
filemap                  netfs                    timer
fsl_edma                 netlink                  timer_migration
ftrace                   nfs                      timestamp
gadget                   nfs4                     tlb
gpio                     notifier                 udp
gpu_mem                  oom                      ufs
handshake                optee                    vmalloc
header_event             page_isolation           vmscan
header_page              page_pool                watchdog
hns3                     pagemap                  workqueue
huge_memory              percpu                   writeback
hugetlbfs                power                    xdp
hw_pressure              printk                   xhci-hcd
hwmon                    pwm
i2c                      qcom_aoss
```

As shown above, you should see a list of the available trace
points.

Now, enable the kernel tracing infrastructure together with bounce buffer
tracing, read the trace in the background (filtering on `keybroker-app-`) and
run the Key Broker Client application in the realm, using the endpoint address
that the Key Broker Server is listening on (from the other terminal):

```bash
echo 1 > /sys/kernel/debug/tracing/tracing_on
echo 1 > /sys/kernel/debug/tracing/events/swiotlb/enable
grep keybroker-app- /sys/kernel/debug/tracing/trace_pipe &
keybroker-app -v --endpoint http://172.17.0.2:8088 skywalker
```

In the `keybroker-app`command above, `skywalker` is the key name that is
requested from the KBS.

The output should look like:

```output
INFO Requesting key named 'skywalker' from the keybroker server with URL http://172.17.0.2:8088/keys/v1/key/skywalker
INFO Challenge (64 bytes) = [5c, ec, 1e, f5, 93, 54, 4a, 8a, ee, 2e, 46, a0, 50, 0d, 41, dd, d4, 60, b0, 58, 5b, 51, 71, 76, d1, 66, d3, b7, 38, e8, af, ae, 0a, 07, 4e, c5, 60, dc, 4a, c0, b8, 73, 98, d9, bd, af, 41, 96, 99, 6d, 74, cc, 19, 70, 24, c4, c9, 5c, 21, 61, 1a, cb, 76, 75]
INFO Submitting evidence to URL http://172.17.0.2:8088/keys/v1/evidence/1928844131
INFO Attestation success :-) ! The key returned from the keybroker is 'May the force be with you.'
   keybroker-app-143     [000] b..2.  1772.607321: swiotlb_bounced: dev_name: 0000:00:00.0 dma_mask=ffffffffffffffff dev_addr=80b6717e size=66 FORCE
   keybroker-app-143     [000] b..2.  1772.644478: swiotlb_bounced: dev_name: 0000:00:00.0 dma_mask=ffffffffffffffff dev_addr=80b6717e size=66 FORCE
```

Note that the interleaving of the trace messages and KBC messages might differ
from one run to another. With the `switlb_bounced` messages above you can successfully observe that the bounce buffers are being used in the realm.

