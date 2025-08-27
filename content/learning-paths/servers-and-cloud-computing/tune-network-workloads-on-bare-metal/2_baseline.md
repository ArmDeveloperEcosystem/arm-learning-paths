---
title: Establish baseline performance
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

{{% notice Note %}}
To achieve maximum performance, ulimit -n 65535 must be executed on both server and client!
{{% /notice %}}

## Optimal baseline before tuning
- Align the IOMMU settings with default Ubuntu settings
- Baseline on Arm Neoverse bare-metal (default configuration)
- Baseline on Arm Neoverse bare-metal (access logging disabled)
- Baseline on Arm Neoverse bare-metal (optimal thread count)

### Align the IOMMU settings with default Ubuntu settings

{{% notice Note %}}
As you are using a custom Ubuntu distribution on AWS, you will first need to align the IOMMU settings with default Ubuntu settings for IOMMU: iommu.strict=1 and iommu.passthrough=0.
{{% /notice %}}

1. To change the IOMMU settings, use a text editor to modify the `grub` file by adding or updating the `GRUB_CMDLINE_LINUX` configuration:

```bash
sudo vi /etc/default/grub
```
Depending on what's in your `grub` file you will need to add or update `GRUB_CMDLINE_LINUX`:
```bash
GRUB_CMDLINE_LINUX="iommu.strict=1 iommu.passthrough=0"
```

2. Update GRUB and reboot your system to apply the default settings.
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

### Establish a baseline configuration on Arm Neoverse bare-metal instances

{{% notice Note %}}
To align with typical deployment scenario of Tomcat, you will need to reserve 8 cores on your instance to be online and set all other cores to be offline
{{% /notice %}}

1. To set the remaining CPU cores on your instance to be offline, run:
```bash
for no in {8..191}; do sudo bash -c "echo 0 > /sys/devices/system/cpu/cpu${no}/online"; done
```
2. Use the following commands to verify that cores 0-7 are online and the remaining cores are offline.
```bash
lscpu
```
The output should look like:
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

3. Now shutdown and restart `Tomcat` on your Arm Neoverse bare-metal instance as shown:
```bash
~/apache-tomcat-11.0.10/bin/shutdown.sh 2>/dev/null
ulimit -n 65535 && ~/apache-tomcat-11.0.10/bin/startup.sh
```

4. On your `x86_64` bare-metal instance, run `wrk2` as shown:

```bash
ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://${tomcat_ip}:8080/examples/servlets/servlet/HelloWorldExample
```
Replace `{tomcat_ip}` in the command above with the IP address of your Arm-based instance where the Tomcat server is running.

The result with this baseline configuration should look like:
```output
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    16.76s     6.59s   27.56s    56.98%
    Req/Sec     1.97k   165.05     2.33k    89.90%
  14680146 requests in 1.00m, 7.62GB read
  Socket errors: connect 1264, read 0, write 0, timeout 1748
Requests/sec: 244449.62
Transfer/sec:    129.90MB
```

### Disable Access logging
To disable access logging, use a text editor to modify the `server.xml` file by commenting out or removing the **`org.apache.catalina.valves.AccessLogValve`** configuration.

The file is at:
```bash
vi ~/apache-tomcat-11.0.10/conf/server.xml
```

Either comment out or delete the configuration shown at the end of the file:
```xml
<!-- 
    <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
        prefix="localhost_access_log" suffix=".txt"
        pattern="%h %l %u %t &quot;%r&quot; %s %b" />
-->
```

1. Shutdown and restart `Tomcat` on your Arm Neoverse bare-metal instance as shown:
```bash
~/apache-tomcat-11.0.10/bin/shutdown.sh 2>/dev/null
ulimit -n 65535 && ~/apache-tomcat-11.0.10/bin/startup.sh
```

2. Run `wrk2` on the `x86_64` bare-metal instance:
```bash
ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://${tomcat_ip}:8080/examples/servlets/servlet/HelloWorldExample
```

The result with access logging disabled should look like:
```bash
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    16.16s     6.45s   28.26s    57.85%
    Req/Sec     2.16k     5.91     2.17k    77.50%
  16291136 requests in 1.00m, 8.45GB read
  Socket errors: connect 0, read 0, write 0, timeout 75
Requests/sec: 271675.12
Transfer/sec:    144.36MB
```

### Set up optimal thread counts
To minimize resource contention between threads and overhead from thread context switching, the number of CPU-intensive threads in Tomcat should be aligned with the number of CPU cores.

1. When using `wrk` to perform pressure testing on `Tomcat`, use `top` to identify the CPU-intensive threads :
```bash
top -H -p$(pgrep java)
```

The output from `top` will look like:
```bash
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

You can observe from the output that **`http-nio-8080-e`** and **`http-nio-8080-P`** threads are CPU-intensive.
As the __`http-nio-8080-P`__ thread is fixed at 1 in current version of Tomcat, and the current number of CPU cores is 8, the `http-nio-8080-e` thread count should be configured to 7.

To configure the `http-nio-8080-e` thread count, use a text editor to modify the `server.xml` file and update the `<Connector port="8080" protocol="HTTP/1.1"` configuration.

The file is at:
```bash
vi ~/apache-tomcat-11.0.10/conf/server.xml
```

Replace the existing Connector setting as shown:
```xml
<!-- Before -->
    <Connector port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443" />
```

With the updated setting:

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

Save the changes to `server.xml`.

2. Now shutdown and restart `Tomcat` on your Arm Neoverse bare-metal instance as shown:
```bash
~/apache-tomcat-11.0.10/bin/shutdown.sh 2>/dev/null
ulimit -n 65535 && ~/apache-tomcat-11.0.10/bin/startup.sh
```

3. Run `wrk2` on the`x86_64` bare-metal instance:
```bash
ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://${tomcat_ip}:8080/examples/servlets/servlet/HelloWorldExample
```

The result with the optimal thread count settings should look like:
```output
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    10.26s     4.55s   19.81s    62.51%
    Req/Sec     2.86k    89.49     3.51k    77.06%
  21458421 requests in 1.00m, 11.13GB read
Requests/sec: 357835.75
Transfer/sec:    190.08MB
```

Now that you have established some baseline settings you can proceed to further tuning your setup.
