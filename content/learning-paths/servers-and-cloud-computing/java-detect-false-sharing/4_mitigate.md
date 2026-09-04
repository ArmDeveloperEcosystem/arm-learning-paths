---
title: Add @Contended and verify contention padding
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Add `@Contended` groups

HotSpot's `@Contended` annotation asks the JVM to isolate an annotated class or
field group by inserting padding into the object layout. Fields with different
group names are separated, reducing the chance that independent writes target
the same cache line. The annotation changes memory layout rather than Java
concurrency semantics, and the extra padding increases each object's memory
footprint.

Edit `FalseSharingDemo.java` so it contains the following complete program.
The changes import `@Contended`, add `PaddedCounters`, accept a `padded` mode,
and select the counter implementation from the command line. The baseline mode
remains available for a like-for-like comparison.

```java
import java.util.concurrent.CountDownLatch;
import jdk.internal.vm.annotation.Contended;

/** Baseline and padded controls for cache-line false sharing. */
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

    static final class PaddedCounters implements Counters {
        @Contended("left") volatile long left;
        @Contended("right") volatile long right;

        public void incrementLeft() { left++; }
        public void incrementRight() { right++; }
        public long sum() { return left + right; }
    }

    public static void main(String[] args) throws Exception {
        if (args.length != 1 ||
                !(args[0].equals("baseline") || args[0].equals("padded"))) {
            throw new IllegalArgumentException("use: baseline | padded");
        }

        Counters counters = args[0].equals("baseline")
                ? new BaselineCounters() : new PaddedCounters();
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
        System.out.printf("mode=%s seconds=%.6f sum=%d pid=%d%n",
                args[0], seconds, counters.sum(), ProcessHandle.current().pid());
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

`@Contended` is an internal HotSpot annotation. Compile with the package export,
then run application annotations with the restriction disabled:

```bash
"$javac_bin" \
  --add-exports java.base/jdk.internal.vm.annotation=ALL-UNNAMED \
  FalseSharingDemo.java

taskset -c 0,1 "$java_bin" \
  --add-exports java.base/jdk.internal.vm.annotation=ALL-UNNAMED \
  -XX:-RestrictContended FalseSharingDemo padded
```

Confirm that the output contains `mode=padded` and `sum=1000000000`.

## Inspect the padded layout

```bash
"$java_bin" -XX:-RestrictContended \
  --add-exports java.base/jdk.internal.vm.annotation=ALL-UNNAMED \
  -cp jol-cli-0.17-full.jar:. org.openjdk.jol.Main internals \
  'FalseSharingDemo$PaddedCounters'
```

A representative OpenJDK 21 layout is:

```output
FalseSharingDemo$PaddedCounters object internals:
OFF  SZ   TYPE DESCRIPTION               VALUE
  0   8        (object header: mark)     0x0000000000000001
  8   4        (object header: class)    0x01085290
 12 132        (alignment/padding gap)
144   8   long PaddedCounters.left       0
152 128        (alignment/padding gap)
280   8   long PaddedCounters.right      0
Instance size: 288 bytes
Space losses: 260 bytes internal + 0 bytes external = 260 bytes total
```

With HotSpot's default 128-byte contention-padding width, the first reported
gap combines the original 4-byte alignment gap with 128 bytes of contention
padding. Another 128-byte gap separates the two contention groups. The fields
move from offsets 16 and 24 in the 32-byte baseline object to offsets 144 and
280 in the 288-byte padded object. The 128-byte inter-field gap prevents the
two 8-byte fields from occupying the same 64-byte cache line, at the cost of
256 additional bytes per object. Exact layouts can vary with JVM settings.

## Record and compare the padded mode

Record with the same Perf binary, CPUs, JVM, and workload used for the baseline:

```bash
sudo perf c2c record -o padded.data -- \
  taskset -c 0,1 "$java_bin" \
  --add-exports java.base/jdk.internal.vm.annotation=ALL-UNNAMED \
  -XX:-RestrictContended FalseSharingDemo padded

sudo perf c2c report --stdio -i padded.data | tee padded-c2c.txt
```

Confirm that the recorded payload prints `mode=padded` and
`sum=1000000000`. The previous step creates `baseline-c2c.txt`, and the
preceding command creates `padded-c2c.txt`. Use the same AWK match for both
reports to display their highest-ranked cache lines together:

```bash
top_c2c_line() {
  local label="$1"
  local report="$2"

  awk -v label="$label" -v filename="$report" '
  $1 ~ /^[0-9]+$/ && $2 ~ /^0x[[:xdigit:]]+$/ {
      print label " report file:", filename
      print label " most contended cache line:", $2
      print label " report row:", $0
      found = 1
      exit
  }
  END {
      if (!found) {
          print label ": no shared cache-line row found in " filename > "/dev/stderr"
          exit 1
      }
  }' "$report"
}

top_c2c_line baseline baseline-c2c.txt
top_c2c_line padded padded-c2c.txt
```

The output is similar to the following result:

```output
baseline report file: baseline-c2c.txt
baseline most contended cache line: 0x101019100
baseline report row:       0         0x101019100     0   60983   32.14%       36       36        0   938563   938544       19        0        0       19        0   938508        0        36        0         0        0         0         0

padded report file: padded-c2c.txt
padded most contended cache line: 0xffff005e4e9c5b00
padded report row:       0  0xffff005e4e9c5b00     0      14    9.30%        4        4        0       18       18        0        0        0        0        0       14        0         4        0         0        0         0         0
```

Confirm that both reports say `Cachelines sort on: Peer Snoop` before making
this comparison. In this output:

- The baseline's top line has 36 peer hits, all local, compared with 4 local
  peer hits for the padded report's top line. The baseline count is nine times
  the padded count, equivalent to an approximately 89% reduction.
- The baseline line contains 938,563 sampled records: 938,544 loads and 19
  stores. The padded line contains only 18 sampled records, all loads. The
  baseline also ran longer, so it provided Perf with more sampling time; do not
  interpret the record-count difference as a normalized performance ratio.
- `32.14%` and `9.30%` are each line's share of the peer-snoop events in its own
  report. Because the two percentages have different denominators, compare the
  absolute peer counts of 36 and 4 rather than subtracting the percentages.

This result is consistent with contention padding removing the original hot
counter line. It does not prove that either address belongs to the counter
object. The two addresses do not need to match because they come from separate
JVM processes.

The padded report can still contain shared lines from JVM internals,
`CountDownLatch`, thread coordination, or other runtime activity. Percentages
can also rise when the total number of samples falls, so compare absolute peer
counts rather than relying only on percentages.

{{% notice Note %}}
HotSpot normally restricts `@Contended` in application classes. Keep
`-XX:-RestrictContended` on every padded run; without it, HotSpot ignores the
padding annotation for this class.
{{% /notice %}}
