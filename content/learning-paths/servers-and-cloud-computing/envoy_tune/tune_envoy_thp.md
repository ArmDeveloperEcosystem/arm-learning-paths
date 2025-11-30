---
title: "Tune Envoy by THP"
weight: 2
layout: "learningpathall"
---

###  Envoy Deployment Tuning by THP

Transparent Huge Pages (THP) in Linux is a feature that automatically utilizes larger memory pages (typically 2 MB) to improve memory management efficiency for large-scale applications. It reduces the overhead associated with managing numerous small pages, enhancing TLB efficiency. Applying THP to Envoy can result in an 18% enhancement in performance.

Use the information below as general guidance to tune Envoy by THP.

##  Kernel configuration
To check your kernel configuration on your Ubuntu machine, run:

```console
cat /boot/config-$(uname -r)
```

Make sure the following configurations are enabled in your kernel config:
```console
CONFIG_HUGETLBFS = y
CONFIG_HUGETLB_PAGE = y
```

### Dependencies on libraries and tools

On Ubuntu, run the following:

```console
sudo apt-get update
sudo apt-get install libhugetlbfs-dev libhugetlbfs-bin
```

### Enable HugeTLB filesystem and THP

Use the commands shown below to enable `hugetlbfs` and THP:

```console
mkdir -p  /mnt/hugetlbfs
mount -t hugetlbfs none /mnt/hugetlbfs
hugeadm --list-all-mounts
hugeadm --pool-pages-max 2MB:500
hugeadm --pool-pages-min 2MB:300
echo always >/sys/kernel/mm/transparent_hugepage/enabled
echo always >/sys/kernel/mm/transparent_hugepage/defrag
```

### Run Envoy as a server

```console
LD_PRELOAD=/usr/lib/aarch64-linux-gnu/libhugetlbfs.so HUGETLB_MORECORE=thp  nohup bin/envoy-static.stripped  -c configs/config-http.yaml --concurrency 16 > /dev/null &
```

### Enable THP on Alibaba Cloud Linux

For Alibaba Cloud Linux, the above scripts are unnecessary. Instead, execute the following command:

```console
echo 3 > /sys/kernel/mm/transparent_hugepage/hugetext_enabled
```
