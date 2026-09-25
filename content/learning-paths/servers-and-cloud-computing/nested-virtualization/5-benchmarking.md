---
title: Testing Nested Virtualization overhead
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Testing Nested Virtualization Overhead


In this step, we are going to install and run a reference benchmark across our three layers – L0 (bare metal), our L1 guest VM, and our L2 guest VM. To make the test comparable, and to minimize the interaction with other workloads running on the server, we are going to do the following: 
* In the host OS: We will use taskset to limit the benchmark to only 8 physical cores, CPU cores 8-15 
* For the L1 guest. we will use ‘virsh vcpupin’ to pin the virtual CPUs 0-7 of the VM to the physical cores 16-23 of the host 
* For the L1 hypervisor VM, we will pin the 16 cores of the VM to cores 24-39 of the host 
* Inside the L1 hypervisor, we will pin the 8 cores of the L2 guest to cores 8-15 of the L1 hypervisor, coresponding to host cores 32-39 

Once we have completed this, and installed sysbench on all of the systems under test, we will run our test, verify that we are seeing the correct cores running at 100% CPU for the period of the test, and finally verify the results to see how much virtualization passthrough affects performance. We can do this core pinning while the VMs are running by using the –live flag for virsh. 

1. Pinning the cores for the L1 guest and L1 hypervisor: 
   ```
    # Pin L1 guest to cores 16-23
    for i in $(seq 0 7); do
      sudo virsh vcpupin fedora-l1-guest $i $((i+16)) --config –live
    done
    sudo virsh emulatorpin fedora-l1-guest 16-23 --config –live

    # Pin L1 hypervisor to cores 24-39
    for i in $(seq 0 15); do
      sudo virsh vcpupin fedora-l1-hyper $i $((i+24)) --config –live
    done
    sudo virsh emulatorpin fedora-l1-hyper 24-31 --config –live
   ```
2. Log in to `fedora-l1-hyper` and pin the cores of `fedora-l2-guest` to cores 8-15: 
   ```
    # On host:
    ssh -i /path/to/private/key fedora@${fedora-l1-hyper IP address}

    # Inside L1 hypervisor: pin L2 guest to vCPUs 8-15 
    for i in $(seq 0 7); do 
      sudo virsh vcpupin fedora-l2-guest $i $((i+8)) --config –live 
    done 
    sudo virsh emulatorpin fedora-l2-guest 8-15 --config –live 
   ```
3. Verify that the pinning has been done correctly, replacing `<domain>` with the domain name for each of the VMs (`fedora-l1-guest`, etc): 
   ```
    sudo virsh vcpuinfo <domain>
    sudo virsh emulatorpin <domain>
   ```
4. Install the sysbench benchmarking tool in all sustems under test (the host, the L1 guest, and the L2 guest): 
   ```
    sudo dnf install -y sysbench 
   ```
5. On each of the systems under test, run the same benchmark test. You can run these in 3 different terminals, at the same time, and since they are using different cores, they should not significantly interfere with each other: 
   ```
    # On the host: 
    taskset -c 8-15 sysbench cpu --cpu-max-prime=20000 --threads=8 --time=60 run 

    # On the L1 and L2 guests 
    sysbench cpu --cpu-max-prime=20000 --threads=8 --time=60 run 
   ```

In our tests, the results were as follows: 

| Metric | Bare Metal | L1 KVM Guest | L2 Nested Guest |
| ------ | ---------- | ------------ | --------------- |
| Events/sec | 2533.02 | 2525.84 | 2306.22 |
| Overhead vs bare metal | — | -0.3% | -8.9% | 
| Min latency | 3.14ms | 3.15ms | 3.38ms |
| Avg latency | 3.16ms | 3.17ms | 3.47ms |
| Max latency | 9.16ms | 13.02ms | 19.72ms |
| 95th percentile | 3.13ms | 3.19ms | 3.55ms | 
| Thread stddev | 52.18 | 41.46 | 73.47 | 

We see some performance drop-off for the nested VM in events/sec (about 10% between bare metal and nested virtual machine), and there is a significant difference in max latency across the three levels, but the average and P95 latencies are very consistent across all three systems under test.

What this shows is that while latency-sensitive workloads may not be a good match for nested VMs in performance critical situations, the performance of applications is good enough for the test & development environments where nested virt is the best fit.

