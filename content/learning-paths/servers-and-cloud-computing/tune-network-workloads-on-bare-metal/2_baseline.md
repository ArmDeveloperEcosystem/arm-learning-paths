---
title: Establish baseline performance
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you establish a baseline configuration before applying advanced techniques to tune the performance of Tomcat-based network workloads on an Arm Neoverse bare-metal instance.

{{% notice Note %}}
To avoid running out of file descriptors under load, raise the file‑descriptor limit on **both** the server and the client:
```bash
ulimit -n 65535
```
{{% /notice %}}

## Configure an optimal baseline before tuning

This baseline includes:

- Aligning IOMMU settings with Ubuntu defaults
- Setting a default CPU configuration
- Disabling access logging
- Setting optimal thread counts

## Align IOMMU settings with Ubuntu defaults

{{% notice Note %}}
If you are using a cloud image (for example, AWS) with non-default kernel parameters, align IOMMU settings with the Ubuntu defaults: `iommu.strict=1` and `iommu.passthrough=0`.
{{% /notice %}}

1. Edit GRUB and add (or update) `GRUB_CMDLINE_LINUX`:

    ```bash
    sudo vi /etc/default/grub
    ```

    Add or update the line to include:
    ```bash
    GRUB_CMDLINE_LINUX="iommu.strict=1 iommu.passthrough=0"
    ```

2. Update GRUB and reboot to apply the settings:

    ```bash
    sudo update-grub && sudo reboot
    ```

3. Verify that the default settings have been successfully applied:
```bash
sudo dmesg | grep iommu
```
You should see that under the default configuration, `iommu.strict` is enabled, and `iommu.passthrough` is disabled:
```output
[    0.877401] iommu: Default domain type: Translated (set via kernel command line)
[    0.877404] iommu: DMA domain TLB invalidation policy: strict mode (set via kernel command line)
...
```

## Establish a baseline on Arm Neoverse bare-metal instances

{{% notice Note %}}
To mirror a typical Tomcat deployment and simplify tuning, keep **8 CPU cores online** and set the remaining cores offline. Adjust the CPU range to match your instance. The example below assumes 192 CPUs (as on AWS `c8g.metal-48xl`).
{{% /notice %}}

1. Set CPUs 8–191 offline:

    ```bash
    for no in {8..191}; do sudo bash -c "echo 0 > /sys/devices/system/cpu/cpu${no}/online"; done
    ```

2. Confirm that CPUs `0–7` are online and the rest are offline:

    ```bash
    lscpu
    ```

    Example output:
    ```output
    Architecture:                aarch64
      CPU op-mode(s):            64-bit
      Byte Order:                Little Endian
    CPU(s):                      192
      On-line CPU(s) list:       0-7
      Off-line CPU(s) list:      8-191
    Vendor ID:                   ARM
      Model name:                Neoverse-V2
    ...
    ```

3. Restart Tomcat on the Arm instance:

    ```bash
    ~/apache-tomcat-11.0.10/bin/shutdown.sh 2>/dev/null
    ulimit -n 65535 && ~/apache-tomcat-11.0.10/bin/startup.sh
    ```

4. From your `x86_64` benchmarking client, run `wrk2` (replace `<tomcat_ip>` with the server’s IP):

    ```bash
    ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://<tomcat_ip>:8080/examples/servlets/servlet/HelloWorldExample
    ```

    Example result:
    ```output
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency    16.76s     6.59s   27.56s    56.98%
        Req/Sec     1.97k   165.05     2.33k    89.90%
      14680146 requests in 1.00m, 7.62GB read
      Socket errors: connect 1264, read 0, write 0, timeout 1748
    Requests/sec: 244449.62
    Transfer/sec:    129.90MB
    ```

## Disable access logging

Disabling access logs removes I/O overhead during benchmarking.

1. Edit `server.xml` and comment out (or remove) the **`org.apache.catalina.valves.AccessLogValve`** block:

    ```bash
    vi ~/apache-tomcat-11.0.10/conf/server.xml
    ```

    ```xml
    <!--
        <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
                prefix="localhost_access_log" suffix=".txt"
                pattern="%h %l %u %t &quot;%r&quot; %s %b" />
    -->
    ```

2. Restart Tomcat:

    ```bash
    ~/apache-tomcat-11.0.10/bin/shutdown.sh 2>/dev/null
    ulimit -n 65535 && ~/apache-tomcat-11.0.10/bin/startup.sh
    ```

3. Re-run `wrk2`:

    ```bash
    ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://<tomcat_ip>:8080/examples/servlets/servlet/HelloWorldExample
    ```

    Example result:
    ```output
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency    16.16s     6.45s   28.26s    57.85%
        Req/Sec     2.16k     5.91     2.17k    77.50%
      16291136 requests in 1.00m, 8.45GB read
      Socket errors: connect 0, read 0, write 0, timeout 75
    Requests/sec: 271675.12
    Transfer/sec:    144.36MB
    ```

## Set optimal thread counts

To minimize contention and context switching, align Tomcat’s CPU‑intensive thread count with available CPU cores.

1. While `wrk2` is running, identify CPU‑intensive Tomcat threads:

    ```bash
    top -H -p "$(pgrep -n java)"
    ```

    Example output:
    ```output
    top - 08:57:29 up 20 min,  1 user,  load average: 4.17, 2.35, 1.22
    Threads: 231 total,   8 running, 223 sleeping,   0 stopped,   0 zombie
    %Cpu(s): 31.7 us, 20.2 sy,  0.0 ni, 31.0 id,  0.0 wa,  0.0 hi, 17.2 si,  0.0 st
    MiB Mem : 386127.8 total, 380676.0 free,   4040.7 used,   2801.1 buff/cache
    MiB Swap:      0.0 total,      0.0 free,      0.0 used. 382087.0 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
   4677 ubuntu    20   0   36.0g   1.4g  24452 R  89.0   0.4   1:18.71 http-nio-8080-P
   4685 ubuntu    20   0   36.0g   1.4g  24452 R   4.7   0.4   0:04.42 http-nio-8080-A
   4893 ubuntu    20   0   36.0g   1.4g  24452 S   3.3   0.4   0:00.60 http-nio-8080-e
   4963 ubuntu    20   0   36.0g   1.4g  24452 S   3.3   0.4   0:00.66 http-nio-8080-e
   4924 ubuntu    20   0   36.0g   1.4g  24452 S   3.0   0.4   0:00.59 http-nio-8080-e
   4955 ubuntu    20   0   36.0g   1.4g  24452 S   3.0   0.4   0:00.60 http-nio-8080-e
   5061 ubuntu    20   0   36.0g   1.4g  24452 S   3.0   0.4   0:00.61 http-nio-8080-e
   4895 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.58 http-nio-8080-e
   4907 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.59 http-nio-8080-e
   4940 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.58 http-nio-8080-e
   4946 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.59 http-nio-8080-e
   4956 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.65 http-nio-8080-e
   4959 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.59 http-nio-8080-e
   4960 ubuntu    20   0   36.0g   1.4g  24452 R   2.7   0.4   0:00.60 http-nio-8080-e
   4962 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.57 http-nio-8080-e
   4982 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.63 http-nio-8080-e
   4983 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.58 http-nio-8080-e
   4996 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.60 http-nio-8080-e
   5033 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.59 http-nio-8080-e
   5036 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.66 http-nio-8080-e
   5056 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.61 http-nio-8080-e
   5065 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.56 http-nio-8080-e
   5068 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.61 http-nio-8080-e
   5070 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.60 http-nio-8080-e
   5071 ubuntu    20   0   36.0g   1.4g  24452 S   2.7   0.4   0:00.61 http-nio-8080-e
...
```

    You’ll typically see **`http-nio-8080-e`** and **`http-nio-8080-P`** threads as CPU intensive. Because the **`http-nio-8080-P`** thread count is fixed at 1 (in current Tomcat releases), and you have 8 online CPU cores, set **`http-nio-8080-e`** to **7**.

2. Edit `server.xml` and update the HTTP connector to set the worker thread counts and connection limits:

    ```bash
    vi ~/apache-tomcat-11.0.10/conf/server.xml
    ```

    Replace the existing connector:
    ```xml
    <!-- Before -->
        <Connector port="8080" protocol="HTTP/1.1"
                   connectionTimeout="20000"
                   redirectPort="8443" />
    ```

    With the tuned settings:
    ```xml
    <!-- After -->
        <Connector port="8080" protocol="HTTP/1.1"
                   connectionTimeout="20000"
                   redirectPort="8443"
                   minSpareThreads="7"
                   maxThreads="7"
                   maxKeepAliveRequests="500000"
                   maxConnections="100000"
        />
    ```

3. Restart Tomcat and re-run `wrk2`:

    ```bash
    ~/apache-tomcat-11.0.10/bin/shutdown.sh 2>/dev/null
    ulimit -n 65535 && ~/apache-tomcat-11.0.10/bin/startup.sh

    ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://<tomcat_ip>:8080/examples/servlets/servlet/HelloWorldExample
    ```

    Example result:
    ```output
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency    10.26s     4.55s   19.81s    62.51%
        Req/Sec     2.86k    89.49     3.51k    77.06%
      21458421 requests in 1.00m, 11.13GB read
    Requests/sec: 357835.75
    Transfer/sec:    190.08MB
    ```

With a solid baseline in place, you’re ready to proceed to NIC queue tuning, NUMA locality optimization, and IOMMU exploration in the next sections.
