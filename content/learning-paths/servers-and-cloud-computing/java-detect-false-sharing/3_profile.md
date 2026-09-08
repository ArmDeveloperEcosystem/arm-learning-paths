---
title: Identify the contended cache line
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Check the recorded events

Start with the report statistics:

```bash
sudo perf c2c report --stats -i baseline.data
```

The following sections show representative output from an Arm Neoverse system:

```output
=================================================
            Trace Event Information
=================================================
  Total records                     :    1336447
  Load Operations                   :    1332642
  Load L1D hit                      :    1331026
  Load L2D hit                      :       1248
  Load LLC hit                      :        300
  Load Local DRAM                   :         68
  Load HIT Local Peer               :        112
  Load HIT Remote Peer              :          0
  Store Operations                  :       3805
  Store No available memory level   :       3805
  Unable to parse data source       :          0

=================================================
    Global Shared Cache Line Event Information
=================================================
  Total Shared Cache Lines          :         42
  Load HITs on shared lines         :     938977
  L1D hits on shared lines          :     938848
  L2D hits on shared lines          :         16
  LLC hits on shared lines          :        113
  Load hits on peer cache or nodes  :        112
  Store HITs on shared lines        :         81
  Store No available memory level   :         81
  Total Merged records              :         81

=================================================
                 c2c details
=================================================
  Events                            : arm_spe_0/ts_enable=1,pa_enable=1,load_filter=1,store_filter=1,min_latency=30/
                                    : dummy:u
                                    : memory
  Cachelines sort on                : Peer Snoop
  Cacheline data grouping           : offset,iaddr
```

The most relevant values are:

- `Total records: 1336447`, including `1332642` loads and `3805` stores,
  confirms that Perf sampled the workload.
- `Load HIT Local Peer: 112` is direct evidence that sampled loads obtained
  data from a peer cache on the local system. The matching
  `Load hits on peer cache or nodes: 112` value summarizes those hits across
  the lines classified as shared.
- `Total Shared Cache Lines: 42` means the recording contains 42 candidate
  shared lines. It does not mean that every line belongs to
  `BaselineCounters` or is equally contended.
- `Store HITs on shared lines: 81` shows that store samples were associated
  with the shared lines. The much larger L1D-hit count describes accesses to
  those lines, but an L1D hit by itself is not a cache-line ownership transfer.

These statistics confirm that the recording contains sharing evidence, but
they do not identify which of the 42 lines is the baseline counter line. Use
the detailed report in the next section to find the line with the largest
absolute peer-snoop count and inspect its accesses.

{{% notice Warning %}}
A zero-event or zero-peer report does not prove that false sharing is absent.
Confirm that the Java payload ran, the workload lasted long enough, the SPE
kernel driver is available, Perf has permission to record, and the installed
Perf version decodes data sources for the processor.
{{% /notice %}}


## Display and rank shared lines

Generate a text report:

```bash
sudo perf c2c report --stdio -i baseline.data | tee baseline-c2c.txt
```

Perf normally ranks cache lines by its sharing metric. If the standard view
hides lines because no peer data was decoded, display all recorded lines:

```bash
sudo perf c2c report --stdio --show-all -i baseline.data
```

Confirm that the `c2c details` section in the normal Arm report says
`Cachelines sort on: Peer Snoop`. The first data row in the shared cache-line
table is then the line with the highest peer-snoop count.

Inspect the extracted line's records, loads, stores, sampled CPUs, offsets, and
access symbols in the full report. A strong baseline candidate has all of these
properties:

- Two or more CPUs access the same cache line.
- Stores and loads repeatedly target offsets within that line.
- The sharing count is large relative to other lines in the same recording.
- The accesses occur while `left-writer` and `right-writer` run.

Do not expect the exact addresses, counts, or percentages to match another
machine. SPE sampling, scheduling, object placement, and workload duration all
affect them. `--show-all` can reveal sampled addresses without creating peer
snoop percentages; absent peer percentages usually mean that Perf did not
decode the required data-source information.

You can extract the highest contended cache line address
and complete summary row without reading the full report:

```bash
sudo perf c2c report --stdio -i baseline.data |
awk '
$1 ~ /^[0-9]+$/ && $2 ~ /^0x[[:xdigit:]]+$/ {
    print "Most contended cache line:", $2
    print "Report row:", $0
    found = 1
    exit
}
END {
    if (!found) {
        print "No shared cache-line row found" > "/dev/stderr"
        exit 1
    }
}'
```

The output is similar to:

```output
Most contended cache line: 0x101019100
Report row:       0         0x101019100     0   60983   32.14%       36       36        0   938563   938544       19        0        0       19        0   938508        0        36        0         0        0         0         0
```

The command prints the cache-line address from the second column and its full
summary row. If the report is not sorted by `Peer Snoop`, the first row does
not necessarily have the highest peer-snoop count.

{{% notice Note %}}
JOL and Perf provide complementary evidence. JOL shows that `left` and `right`
are adjacent within `BaselineCounters`; Perf C2C shows whether accesses to a
runtime cache line caused inter-core sharing. Neither tool alone proves that a
specific sampled address belongs to a particular Java object. To correlate a
Perf C2C cache-line address with a live heap object and its fields, follow
[Attribute contended cache lines to Java heap objects](/learning-paths/servers-and-cloud-computing/java-attribute-cache-lines/).
{{% /notice %}}
