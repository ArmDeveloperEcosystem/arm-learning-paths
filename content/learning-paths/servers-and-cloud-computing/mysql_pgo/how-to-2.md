---
title: performance test results
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Test Environment
the Environment is setup from Alibaba ECS, as shown below:

| C/S    | OS                   | Kernel                  | GCC    | cores  | RAM   |
| :----- | :------------------  | :---------------------- | :---   | :----- | :-----|
| Server |  Ubuntu 22.04.2 LTS  | 5.15.0-76-generic       | 11.4.0 | 8      | 32G   |
| Client |  Alibaba Cloud Linux | 5.10.134-14.al8.aarch64 | N/A    | 32     | 128G  |


## Test Results
This is how the test was run:

1. reboot server
2. start MySQL server which doesn't enable PGO
3. run write test
4. run read test
5. repeat step 1-4 for another 2 times
6. reboot server
7. start MySQL server which enables PGO
8. run write test
9. run read test
10. repeat step 6-9 for another 2 times

### write test results without PGO
this is 3 rounds of write test without PGO:
```
Throughput:

    events/s (eps):                      7837.0387

    time elapsed:                        300.0977s

    total number of events:              2351876

Throughput:

    events/s (eps):                      7616.9932

    time elapsed:                        300.0844s

    total number of events:              2285740

Throughput:

    events/s (eps):                      7893.9496

    time elapsed:                        300.0817s

    total number of events:              2368829

```

### read test results without PGO
this is 3 rounds of read test without PGO:
```
Throughput:

    events/s (eps):                      3768.8060

    time elapsed:                        300.1503s

    total number of events:              1131208



Throughput:

    events/s (eps):                      3688.1464

    time elapsed:                        300.1504s

    total number of events:              1106998



Throughput:

    events/s (eps):                      3774.9087

    time elapsed:                        300.1509s

    total number of events:              1133042
```

### Write test results (+13.4%, +16.7%, +11.8%) with PGO
this is 3 rounds of write test with PGO, it shows performance improved 13.4%, 16.7%, 11.8% for each round compared to non-PGO test:
```
Throughput:

    events/s (eps):                      8891.5023

    time elapsed:                        300.0943s

    total number of events:              2668288



Throughput:

    events/s (eps):                      8892.7030

    time elapsed:                        300.0876s

    total number of events:              2668589



Throughput:

    events/s (eps):                      8831.1063

    time elapsed:                        300.0857s

    total number of events:              2650088
```

### Read test results (+25.9%, +20.9%, +16.4%) with PGO
this is 3 rounds of test test with PGO, it shows performance improved 25.9%, 20.9%, 16.4% for each round compared to non-PGO test:
```
Throughput:

    events/s (eps):                      4746.7576

    time elapsed:                        300.1492s

    total number of events:              1424735

Throughput:

    events/s (eps):                      4460.4811

    time elapsed:                        300.1489s

    total number of events:              1338808

Throughput:

    events/s (eps):                      4395.7754

    time elapsed:                        300.1699s

    total number of events:              1319479
```
