---
title: Run QuantLib benchmark workloads
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Run a baseline benchmark

After building QuantLib, move to the test suite directory and run the benchmark with its default settings. The command uses the `QL_VER` variable that you exported when downloading the source archive:

```bash
cd ~/QuantLib-$QL_VER/test-suite
./quantlib-benchmark
```

Successfully running the benchmark with default settings confirms that the benchmark is working correctly on your system.

To understand how performance scales across the Arm cores in the VM, keep the workload size constant and change only the number of worker processes:

```bash
./quantlib-benchmark --size=80 --nProc=1
./quantlib-benchmark --size=80 --nProc=2
./quantlib-benchmark --size=80 --nProc=4
```

The `Standard_D4ps_v5` virtual machine has a limited number of cores. Start with 1, 2, and 4 workers. Larger values such as 12, 24, or 48 are better suited to larger machines and can oversubscribe this VM, which makes the results harder to interpret.

## Vary workload size

Next, keep the thread count fixed and vary the problem size. By using varied problem sizes, you can see how runtime changes as the benchmark does more work:

```bash
./quantlib-benchmark --size=1 --nProc=1
./quantlib-benchmark --size=5 --nProc=1
./quantlib-benchmark --size=8 --nProc=1
```

## Interpret the output

The `--size=1 --nProc=1` run is the quickest of the three, completing in roughly 2 minutes 25 seconds on this configuration. It's a good first check before committing to longer runs. Adding `--verbose=2` prints a per-test runtime breakdown alongside the summary. Without it, only the summary block is printed. Verbosity levels run from 0 (summary only) to 2 (per-test detail). Level 3 adds internal debug output.

The first run with `--size=1 --nProc=1 --verbose=2` produces output similar to the following:

```output
*** No errors detected

------------------------------------------------------------------------------------
                       Total Runtime spent in each test 
------------------------------------------------------------------------------------
NthToDefaultTests/testGauss                                             : 7.98616s
MarketModelCmsTests/testMultiStepCmSwapsAndSwaptions                    : 8.77406s
ZabrTests/testConsistency                                               : 5.86461s
MarkovFunctionalTests/testVanillaEngines                                : 6.88742s
...
FunctionsTests/testFactorial                                            : 0.004909s
------------------------------------------------------------------------------------

Benchmark Size        = Custom (1)
Number of processes   = 1
System Throughput     = 0.598422 tasks/s
Benchmark Runtime     = 145.382s
Num. Worker Processes = 1
Tail Effect Ratio     = 1
```

The benchmark first confirms that all tests passed, then lists the runtime for each individual test, and finishes with a summary. 

The `System Throughput` and `Benchmark Runtime` values are what you'll compare across runs. The individual test lines show which computations dominate total runtime. Longer-running tests such as `testMultiStepCmSwapsAndSwaptions` and `testGauss` reflect the most numerically intensive parts of the workload.

## Keep benchmark runs controlled

For meaningful comparisons:

- Change one parameter at a time
- Keep the environment consistent
- Repeat runs if results vary

Doing so ensures that differences in runtime reflect real performance changes.

## What you've accomplished and what's next

You've now benchmarked QuantLib with default settings and with varied workloads. You've also reviewed the output of the benchmark.

Next, you'll further analyze and compare benchmark results. 
