---
# User change
title: "Linux Perf"

weight: 8 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Linux Perf					

Linux software developers use `perf` to analyze performance. 

Install and enable `perf` using the commands below. Make sure to become root where indicated. 

For Ubuntu running on the Arm server run this command to install `perf`:

```console
sudo apt install linux-tools-common linux-tools-generic linux-tools-`uname -r` -y
```

For the Raspberry Pi 4 run this command:

```bash		
sudo apt-get install linux-perf	-y
```

Become root to enable access to the perf data:

```bash
sudo su -
```

As root run the commands shown:

```bash
echo -1 > /proc/sys/kernel/perf_event_paranoid
echo 0 > /proc/sys/kernel/kptr_restrict
```

Exit root:

```bash
exit
```
					

If you don't have the Linux source tree used in the [Linux Kernel Compile section](/learning-paths/embedded-and-microcontrollers/rpi/kernel/), retrieve it again using git:

```console
git clone --depth=1 https://github.com/raspberrypi/linux
```

In some cases, `perf` may not work on the Raspberry Pi 4 due to a mismatch between your running kernel and the `linux-perf` Debian package. To overcome this, build `perf` from source code. 

Install the required tools for kernel building:

```console
sudo apt install git bc bison flex libssl-dev make
```

Build `perf` using `make`:

```console
cd linux
make -C tools/perf/
```

The `perf` command should now be available in the directory `$HOME/linux/tools/perf`

To list the available `perf` events:

```console			
perf list
```
					
If you built `perf` from source in `$HOME/linux` list the events using:

```console
$HOME/linux/tools/perf/perf list
```

Linux `perf` works on both the Arm server and the Raspberry Pi 4. Arm servers have additional perf events because of the different processor type.

An example event which is included on the Arm server is `stalled-cycles-backend`. This event is not available on the Raspberry Pi 4.

Run a `tar` command to compress the Linux kernel source tree and count the `stalled-cycles-backend` event. 

On the Arm server, run `perf` on a `tar` command to see the events. 

```console
perf stat -e stalled-cycles-backend tar cfz test.tgz ./linux/
```

The expected output should be similar to:

```output
 Performance counter stats for 'tar cfz test.tgz ./linux/':

    27,701,570,350      stalled-cycles-backend    #    0.00% backend cycles idle

      44.461783841 seconds time elapsed

      43.283230000 seconds user
       2.121127000 seconds sys

```
					
The Raspberry Pi doesn’t have the `stalled-cycles-backend` event.

```console
perf stat -e stalled-cycles-backend tar cfz test.tgz ./linux/
```

The expected output shows the `stalled-cycles-backend` is not available.

```output
 Performance counter stats for 'tar cfz test.tgz ./linux/':

   <not supported>      stalled-cycles-backend

     143.177396310 seconds time elapsed

     129.623757000 seconds user
       8.292624000 seconds sys

```			
					
Linux `perf` is available on the Arm server and the Raspberry Pi 4. The events are slightly different due to the processor, but `perf` generally works the same on both. 
