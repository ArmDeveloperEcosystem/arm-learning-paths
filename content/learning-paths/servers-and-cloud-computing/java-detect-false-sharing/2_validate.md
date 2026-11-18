---
title: Create and inspect the baseline
description: Build a Java false-sharing workload, inspect its object layout with JOL, and record a baseline with Perf C2C on an Arm server.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Before you begin

Run the instructions in this Learning Path on an Arm-based Linux server with
Arm Statistical Profiling Extension (SPE) enabled. For instructions to confirm that SPE is
enabled on your server, see [Enable and verify Arm SPE support](/learning-paths/servers-and-cloud-computing/spe-on-performix/how-to-3/).

Install the OpenJDK 21 Java Development Kit (JDK) on your Arm-based Ubuntu
server:

```bash
sudo apt update
sudo apt install -y openjdk-21-jdk
```

## Prepare the baseline example

Before you run the examples, resolve the absolute path to the Java executable.
Derive `javac_bin` from the same JDK so the compiler and runtime versions match.

Use the same terminal throughout this Learning Path. If you open a new terminal,
you'll need to rerun the following commands:

```bash
java_bin=$(readlink -f "$(command -v java)")
javac_bin="$(dirname "$java_bin")/javac"

"$java_bin" -version
"$javac_bin" -version
```

{{% notice Note %}}
Using the absolute path is important when Perf starts the payload with `sudo`,
because the restricted `sudo` `PATH` might not contain your Java installation.
{{% /notice %}}

### Set up the false-sharing demo

In your workspace, create a file named `FalseSharingDemo.java` with the following code:

```java
import java.util.concurrent.CountDownLatch;

/** A small workload that is likely to exhibit cache-line false sharing. */
public final class FalseSharingDemo {
    private static final long ITERATIONS = 500_000_000L;

    interface Counters {
        void incrementLeft();
        void incrementRight();
        long sum();
    }

    static final class BaselineCounters implements Counters {
        volatile long left;
        volatile long right;

        public void incrementLeft() { left++; }
        public void incrementRight() { right++; }
        public long sum() { return left + right; }
    }

    public static void main(String[] args) throws Exception {
        if (args.length != 1 || !args[0].equals("baseline")) {
            throw new IllegalArgumentException("use: baseline");
        }

        Counters counters = new BaselineCounters();
        CountDownLatch ready = new CountDownLatch(2);
        CountDownLatch start = new CountDownLatch(1);
        Thread left = new Thread(
                () -> runWorker(ready, start, counters::incrementLeft),
                "left-writer");
        Thread right = new Thread(
                () -> runWorker(ready, start, counters::incrementRight),
                "right-writer");
        left.start();
        right.start();
        ready.await();
        long begin = System.nanoTime();
        start.countDown();
        left.join();
        right.join();
        double seconds = (System.nanoTime() - begin) / 1_000_000_000.0;
        System.out.printf("mode=baseline seconds=%.6f sum=%d pid=%d%n",
                seconds, counters.sum(), ProcessHandle.current().pid());
    }

    private static void runWorker(
            CountDownLatch ready, CountDownLatch start, Runnable update) {
        try {
            ready.countDown();
            start.await();
            for (long i = 0; i < ITERATIONS; i++) {
                update.run();
            }
        } catch (InterruptedException exception) {
            Thread.currentThread().interrupt();
            throw new RuntimeException(exception);
        }
    }
}
```

The example has two worker threads that update adjacent `volatile long` fields. Each worker performs 500 million increments, making the sharing behavior easier to sample.

Compile the baseline:

```bash
"$javac_bin" FalseSharingDemo.java
```

The following commands use logical CPUs 0 and 1. Confirm that both CPUs are in
the current shell's permitted affinity list:

```bash
taskset -pc $$
```

If needed, replace `0,1` with two online CPUs from the reported list.

Run the baseline:

```bash
taskset -c 0,1 "$java_bin" FalseSharingDemo baseline
```

The output is similar to:

```output
mode=baseline seconds=45.123456 sum=1000000000 pid=12345
```

Your elapsed time and process ID will differ. Confirm that the output contains
`mode=baseline` and `sum=1000000000`.

`taskset` restricts the Java Virtual Machine (JVM) and its threads to the selected logical CPUs. It
doesn't assign one writer thread to each CPU, so either thread can migrate
within the permitted set.

## Inspect the baseline layout with JOL

[Java Object Layout (JOL)](https://github.com/openjdk/jol) is an OpenJDK tool that's
used to inspect JVM object-layout details, including field offsets, alignment
gaps, and total object size.

Download the [JOL CLI 0.17 full JAR](https://repo.maven.apache.org/maven2/org/openjdk/jol/jol-cli/0.17/jol-cli-0.17-full.jar)
from Maven Central
into the directory containing the compiled `FalseSharingDemo` classes:

```bash
curl -LO https://repo.maven.apache.org/maven2/org/openjdk/jol/jol-cli/0.17/jol-cli-0.17-full.jar
```

The `full` JAR includes the dependencies required by the command-line tool.
Inspect `BaselineCounters` with the same JDK used for the workload:

```bash
"$java_bin" -cp jol-cli-0.17-full.jar:. \
  org.openjdk.jol.Main internals 'FalseSharingDemo$BaselineCounters'
```

A representative OpenJDK 21 layout is similar to:

```output
FalseSharingDemo$BaselineCounters object internals:
OFF  SZ   TYPE DESCRIPTION               VALUE
  0   8        (object header: mark)     0x0000000000000001
  8   4        (object header: class)    0x01085290
 12   4        (alignment/padding gap)
 16   8   long BaselineCounters.left     0
 24   8   long BaselineCounters.right    0
Instance size: 32 bytes
Space losses: 4 bytes internal + 0 bytes external = 4 bytes total
```

In this configuration, the header is 12 bytes: an 8-byte mark word and a
4-byte compressed class pointer. A `long` is aligned to an 8-byte boundary so
that it can be accessed efficiently as one aligned value rather than straddling
two 8-byte words. JOL therefore shows a 4-byte gap before `left`. The header
itself hasn't been padded to 16 bytes.

The two fields are adjacent at offsets 16 and 24. They can occupy one 64-byte
cache line, although their offsets within the object don't reveal where the
object was placed relative to a physical cache-line boundary. Your layout can
differ with the JDK and virtual machine configuration.

## Record the baseline with Perf C2C

The Arm Statistical Profiling Extension (SPE) is a hardware profiling feature
that samples operations and records information about how the operations executed with
low overhead. For sampled memory operations, SPE can record the data address,
access type, latency, and memory-source information. For more information, see the
[Arm SPE performance analysis white paper](https://developer.arm.com/documentation/109429/latest/).

On supported Arm systems, `perf c2c` uses SPE to sample loads and stores, then
groups their addresses into cache lines. Peer-cache and peer-node data-source
values indicate that another CPU's cache supplied data. Perf C2C uses this
evidence to rank cache lines that are likely to be shared between CPUs.

{{% notice Note %}}
On Neoverse V2-based systems, use Perf 6.13 or later. Earlier versions can record SPE
packets but don't decode Neoverse V2 data-source values into peer-cache hits.
For other Neoverse processors, confirm that your Perf version supports the
processor's SPE data-source encoding.
{{% /notice %}}

Check the Perf version:

```bash
perf version
```

Before recording, confirm that Linux exposes an Arm SPE performance monitoring
unit (PMU):

```bash
find /sys/bus/event_source/devices -maxdepth 1 \
  -name 'arm_spe_*' -printf '%f\n'
```

The output should list at least one SPE PMU, usually `arm_spe_0`:

```output
arm_spe_0
```

If the command produces no output, don't continue to `perf c2c record`. Follow
the [SPE enablement and verification instructions](/learning-paths/servers-and-cloud-computing/spe-on-performix/how-to-3/), then repeat the check. Without an exposed SPE PMU, Perf reports
`failed: no PMU supports the memory events`.

After the SPE PMU appears, record the workload:

```bash
sudo perf c2c record -o baseline.data -- \
  taskset -c 0,1 "$java_bin" FalseSharingDemo baseline
```

Confirm again that the payload prints `mode=baseline` and
`sum=1000000000`. The absolute `"$java_bin"` path is expanded by the shell
before `sudo` runs Perf, avoiding the restricted `sudo` `PATH`.

## What you've accomplished and what's next

You've created a baseline example, inspected its layout with JOL, and recorded the baseline with Perf C2C.

Next, you'll analyze the recorded `baseline.data` file.
