---
# User change
title: "Compare the results with LSE and NoLSE"
weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Now you can run the mongodb benchmark using Glibc with LSE and NoLSE and compare the results.

## Result with No-LSE
Launch MongoDB with Glibc without LSE and obtain benchmark result.  
The overall TPS is __6662.1275371047195__ with No-LSE Glibc.
```console
[OVERALL], RunTime(ms), 750511
[OVERALL], Throughput(ops/sec), 6662.1275371047195
[TOTAL_GCS_G1_Young_Generation], Count, 3527
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 27871
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 3.713603131732913
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 3527
[TOTAL_GC_TIME], Time(ms), 27871
[TOTAL_GC_TIME_%], Time(%), 3.713603131732913
[READ], Operations, 1998800
[READ], AverageLatency(us), 3047.5279422653593
[READ], MinLatency(us), 225
[READ], MaxLatency(us), 219775
[READ], 95thPercentileLatency(us), 10495
[READ], 99thPercentileLatency(us), 23791
[READ], Return=OK, 1998800
[READ-MODIFY-WRITE], Operations, 999359
[READ-MODIFY-WRITE], AverageLatency(us), 5748.511211686691
[READ-MODIFY-WRITE], MinLatency(us), 482
[READ-MODIFY-WRITE], MaxLatency(us), 379135
[READ-MODIFY-WRITE], 95thPercentileLatency(us), 17455
[READ-MODIFY-WRITE], 99thPercentileLatency(us), 32271
[CLEANUP], Operations, 64
[CLEANUP], AverageLatency(us), 57.46875
[CLEANUP], MinLatency(us), 0
[CLEANUP], MaxLatency(us), 3519
[CLEANUP], 95thPercentileLatency(us), 3
[CLEANUP], 99thPercentileLatency(us), 38
[UPDATE], Operations, 2500755
[UPDATE], AverageLatency(us), 2888.259603599713
[UPDATE], MinLatency(us), 211
[UPDATE], MaxLatency(us), 378367
[UPDATE], 95thPercentileLatency(us), 9743
[UPDATE], 99thPercentileLatency(us), 22895
[UPDATE], Return=OK, 2500755
[SCAN], Operations, 1499804
[SCAN], AverageLatency(us), 22936.992162975963
[SCAN], MinLatency(us), 317
[SCAN], MaxLatency(us), 335615
[SCAN], 95thPercentileLatency(us), 51551
[SCAN], 99thPercentileLatency(us), 70143
[SCAN], Return=OK, 1499804
```

## Result with LSE
Launch MongoDB with Glibc with LSE and obtain benchmark result.  
The overall TPS is __6871.605426919102__ with LSE Glibc.  
___So you can get around 3.14% extra benefit through Glibc with LSE!___
```console
[OVERALL], RunTime(ms), 727632
[OVERALL], Throughput(ops/sec), 6871.605426919102
[TOTAL_GCS_G1_Young_Generation], Count, 3397
[TOTAL_GC_TIME_G1_Young_Generation], Time(ms), 27090
[TOTAL_GC_TIME_%_G1_Young_Generation], Time(%), 3.7230358203047693
[TOTAL_GCS_G1_Old_Generation], Count, 0
[TOTAL_GC_TIME_G1_Old_Generation], Time(ms), 0
[TOTAL_GC_TIME_%_G1_Old_Generation], Time(%), 0.0
[TOTAL_GCs], Count, 3397
[TOTAL_GC_TIME], Time(ms), 27090
[TOTAL_GC_TIME_%], Time(%), 3.7230358203047693
[READ], Operations, 1998456
[READ], AverageLatency(us), 3045.181359009155
[READ], MinLatency(us), 230
[READ], MaxLatency(us), 346111
[READ], 95thPercentileLatency(us), 10535
[READ], 99thPercentileLatency(us), 23631
[READ], Return=OK, 1998456
[READ-MODIFY-WRITE], Operations, 999026
[READ-MODIFY-WRITE], AverageLatency(us), 5786.018821331977
[READ-MODIFY-WRITE], MinLatency(us), 467
[READ-MODIFY-WRITE], MaxLatency(us), 359167
[READ-MODIFY-WRITE], 95thPercentileLatency(us), 17599
[READ-MODIFY-WRITE], 99thPercentileLatency(us), 32463
[CLEANUP], Operations, 64
[CLEANUP], AverageLatency(us), 52.25
[CLEANUP], MinLatency(us), 1
[CLEANUP], MaxLatency(us), 3217
[CLEANUP], 95thPercentileLatency(us), 2
[CLEANUP], 99thPercentileLatency(us), 8
[UPDATE], Operations, 2500888
[UPDATE], AverageLatency(us), 2905.821863674023
[UPDATE], MinLatency(us), 207
[UPDATE], MaxLatency(us), 320767
[UPDATE], 95thPercentileLatency(us), 9903
[UPDATE], 99thPercentileLatency(us), 23007
[UPDATE], Return=OK, 2500888
[SCAN], Operations, 1499682
[SCAN], AverageLatency(us), 21999.80309425598
[SCAN], MinLatency(us), 298
[SCAN], MaxLatency(us), 525311
[SCAN], 95thPercentileLatency(us), 49727
[SCAN], 99thPercentileLatency(us), 67455
[SCAN], Return=OK, 1499682
```

