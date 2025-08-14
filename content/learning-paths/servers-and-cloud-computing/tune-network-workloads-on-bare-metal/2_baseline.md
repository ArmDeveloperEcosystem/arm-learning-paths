---
title: Optimal baseline before tuning
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

{{% notice Note %}}
To achieve maximum performance, ulimit -n 65535 must be executed on both server and client!
{{% /notice %}}

## Optimal baseline before tuning
- Baseline on Grace bare-metal (default configuration)
- Baseline on Grace bare-metal (access logging disabled)
- Baseline on Grace bare-metal (optimal thread count)

### Baseline on Grace bare-metal (default configuration)
{{% notice Note %}}
To align with the typical deployment scenario of Tomcat, reserve 8 cores online and set all other cores offline
{{% /notice %}}

1. You can offline the CPU cores using the below command.
```bash
for no in {8..143}; do sudo bash -c "echo 0 > /sys/devices/system/cpu/cpu${no}/online"; done
```
2. Use the following commands to verify that cores 0-7 are online and the remaining cores are offline.
```bash
lscpu
```
You can check the following information:
```bash
Architecture:             aarch64
  CPU op-mode(s):         64-bit
  Byte Order:             Little Endian
CPU(s):                   144
  On-line CPU(s) list:    0-7
  Off-line CPU(s) list:   8-143
Vendor ID:                ARM
  Model name:             Neoverse-V2
...
```

3. Use the following command on the Grace bare-metal where `Tomcat` is on
```bash
~/apache-tomcat-11.0.9/bin/shutdown.sh 2>/dev/null
ulimit -n 65535 && ~/apache-tomcat-11.0.9/bin/startup.sh
```

4. And use the following command on the `x86_64` bare-metal where `wrk2` is on
```bash
tomcat_ip=10.169.226.181
```
```bash
ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://${tomcat_ip}:8080/examples/servlets/servlet/HelloWorldExample
```

The result of default configuration is:
```bash
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    13.29s     3.25s   19.07s    57.79%
    Req/Sec   347.59    430.94     0.97k    66.67%
  3035300 requests in 1.00m, 1.58GB read
  Socket errors: connect 1280, read 0, write 0, timeout 21760
Requests/sec:  50517.09
Transfer/sec:     26.84MB
```

### Baseline on Grace bare-metal (access logging disabled)
To disable the access logging, use a text editor to modify the `server.xml` file by commenting out or removing the **`org.apache.catalina.valves.AccessLogValve`** configuration.

The file is at:
```bash
vi ~/apache-tomcat-11.0.9/conf/server.xml
```

The configuratin is at the end of the file, and common out or remove it.
```xml
<!-- 
    <Valve className="org.apache.catalina.valves.AccessLogValve" directory="logs"
        prefix="localhost_access_log" suffix=".txt"
        pattern="%h %l %u %t &quot;%r&quot; %s %b" />
-->
```

1. Use the following command on the Grace bare-metal where `Tomcat` is on
```bash
~/apache-tomcat-11.0.9/bin/shutdown.sh 2>/dev/null
ulimit -n 65535 && ~/apache-tomcat-11.0.9/bin/startup.sh
```

2. And use the following command on the `x86_64` bare-metal where `wrk2` is on
```bash
ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://${tomcat_ip}:8080/examples/servlets/servlet/HelloWorldExample
```

The result of access logging disabled is:
```bash
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    12.66s     3.05s   17.87s    57.47%
    Req/Sec   433.69    524.91     1.18k    66.67%
  3572200 requests in 1.00m, 1.85GB read
  Socket errors: connect 1280, read 0, write 0, timeout 21760
Requests/sec:  59451.85
Transfer/sec:     31.59MB
```

### Baseline on Grace bare-metal (optimal thread count)
To minimize resource contention between threads and overhead from thread context switching, the number of CPU-intensive threads in Tomcat should be aligned with the number of CPU cores.

1. When using `wrk` to perform pressure testing on `Tomcat`:
```bash
top -H -p$(pgrep java)
```

You can see the below information
```bash
top - 12:12:45 up 1 day,  7:04,  5 users,  load average: 7.22, 3.46, 1.75
Threads:  79 total,   8 running,  71 sleeping,   0 stopped,   0 zombie
%Cpu(s):  3.4 us,  1.9 sy,  0.0 ni, 94.1 id,  0.0 wa,  0.0 hi,  0.5 si,  0.0 st
MiB Mem : 964975.5 total, 602205.6 free,  12189.5 used, 356708.3 buff/cache
MiB Swap:      0.0 total,      0.0 free,      0.0 used. 952786.0 avail Mem

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND
  53254 yinyu01   20   0   38.0g   1.4g  28288 R  96.7   0.1   2:30.70 http-nio-8080-e
  53255 yinyu01   20   0   38.0g   1.4g  28288 R  96.7   0.1   2:30.62 http-nio-8080-e
  53256 yinyu01   20   0   38.0g   1.4g  28288 R  96.7   0.1   2:30.64 http-nio-8080-e
  53258 yinyu01   20   0   38.0g   1.4g  28288 R  96.7   0.1   2:30.62 http-nio-8080-e
  53260 yinyu01   20   0   38.0g   1.4g  28288 R  96.7   0.1   2:30.69 http-nio-8080-e
  53257 yinyu01   20   0   38.0g   1.4g  28288 R  96.3   0.1   2:30.59 http-nio-8080-e
  53259 yinyu01   20   0   38.0g   1.4g  28288 R  96.3   0.1   2:30.63 http-nio-8080-e
  53309 yinyu01   20   0   38.0g   1.4g  28288 R  95.3   0.1   2:29.69 http-nio-8080-P
  53231 yinyu01   20   0   38.0g   1.4g  28288 S   0.3   0.1   0:00.10 VM Thread
  53262 yinyu01   20   0   38.0g   1.4g  28288 S   0.3   0.1   0:00.12 GC Thread#2
```

It can be observed that **`http-nio-8080-e`** and **`http-nio-8080-P`** threads are CPU-intensive.
Since the __`http-nio-8080-P`__ thread is fixed at 1 in current version of Tomcat, and the current number of CPU cores is 8, the http-nio-8080-e thread count should be configured to 7.

To configure the `http-nio-8080-e` thread count, use a text editor to modify the `context.xml` file by updating the `<Connector port="8080" protocol="HTTP/1.1"` configuration.

The file is at:
```bash
vi ~/apache-tomcat-11.0.9/conf/server.xml
```


```xml
<!-- Before -->
    <Connector port="8080" protocol="HTTP/1.1"
               connectionTimeout="20000"
               redirectPort="8443" />
```

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

2. Use the following command on the Grace bare-metal where `Tomcat` is on
```bash
~/apache-tomcat-11.0.9/bin/shutdown.sh 2>/dev/null
ulimit -n 65535 && ~/apache-tomcat-11.0.9/bin/startup.sh
```

3. And use the following command on the `x86_64` bare-metal where `wrk2` is on
```bash
ulimit -n 65535 && wrk -c1280 -t128 -R500000 -d60 http://${tomcat_ip}:8080/examples/servlets/servlet/HelloWorldExample
```

The result of optimal thread count is:
```bash
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    24.34s     9.91s   41.81s    57.77%
    Req/Sec     1.22k     4.29     1.23k    71.09%
  9255672 requests in 1.00m, 4.80GB read
Requests/sec: 154479.07
Transfer/sec:     82.06MB
```
