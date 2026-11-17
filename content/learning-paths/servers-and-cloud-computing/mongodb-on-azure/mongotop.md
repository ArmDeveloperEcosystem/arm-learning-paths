---
title: Monitor MongoDB with mongotop
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Observe per-collection activity

`mongotop` reports the time MongoDB spends reading and writing each collection. Keep the workload from the previous section running in terminal 1. In terminal 2, SSH into the same Cobalt 200 VM and collect three samples at two-second intervals:

```console
mongotop --host 127.0.0.1 --port 27017 --rowcount=3 2
```

The command stops after three samples. To monitor continuously, omit `--rowcount=3` and press **Ctrl+C** to stop.

The output includes the following activity (idle namespaces are omitted):

```output
2026-11-10T18:58:35.085+0000	connected to: mongodb://127.0.0.1:27017/

                        ns    total    read    write    2026-11-10T18:58:37Z
benchmarkDB.testCollection    181ms    40ms    141ms

                        ns    total    read    write    2026-11-10T18:58:39Z
benchmarkDB.testCollection    185ms    40ms    144ms

                        ns    total    read    write    2026-11-10T18:58:41Z
benchmarkDB.testCollection    182ms    40ms    142ms
```

These samples were collected on a **Standard_D4ps_v7** Cobalt 200 VM (4 vCPUs, 16 GiB) running **Ubuntu 24.04 LTS**, **MongoDB 8.0.12**, and **Database Tools 100.13.0** with the provided workload. Your values will vary.

## Interpret the metrics

- **ns** identifies the `database.collection` namespace.
- **total** reports the accumulated read and write time for that collection during the interval.
- **read** reports time spent on read operations.
- **write** reports time spent on write operations.
- The timestamp identifies the sample interval.

Look for activity in `benchmarkDB.testCollection`, the collection used by the load script. Other namespaces can appear because of server housekeeping or earlier tutorial operations.

These are accumulated collection activity times, not per-request latencies. They do not establish production capacity or a performance comparison with other VM types. For details, see the [mongotop documentation](https://www.mongodb.com/docs/database-tools/mongotop/).
