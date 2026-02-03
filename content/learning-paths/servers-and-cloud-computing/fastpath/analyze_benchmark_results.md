---
title: "Analyze the benchmark results"
weight: 14

layout: "learningpathall"
---

## Review benchmark results

To inspect the outputs stored in the `results/` directory, use the sample commands output when `generate_plan.sh` completed. Some examples are below:

### List swprofiles from tests

To see the swprofiles (kernels) tested and stored in the results directory, run:

```console
source ~/venv/bin/activate
~/fastpath/fastpath/fastpath result list results-fastpath_test_010826-1837 --object swprofile
```

The output is similar to:

```output
+------------------+----------------------+
| ID               | fp_6.18.1-ubuntu     |
+------------------+----------------------+
| Kernel Name      | 6.18.1-ubuntu+       |
+------------------+----------------------+
| Kernel Git SHA   | <none>               |
+------------------+----------------------+
| Userspace        | Ubuntu 24.04.3 LTS   |
+------------------+----------------------+
| cmdline          | <none>               |
+------------------+----------------------+
| sysctl           | <none>               |
+------------------+----------------------+
| bootscript       | <none>               |
+------------------+----------------------+

+------------------+----------------------+
| ID               | fp_6.19.0-rc1-ubuntu |
+------------------+----------------------+
| Kernel Name      | 6.19.0-rc1-ubuntu+   |
+------------------+----------------------+
| Kernel Git SHA   | <none>               |
+------------------+----------------------+
| Userspace        | Ubuntu 24.04.3 LTS   |
+------------------+----------------------+
| cmdline          | <none>               |
+------------------+----------------------+
| sysctl           | <none>               |
+------------------+----------------------+
| bootscript       | <none>               |
+------------------+----------------------+
```

### View relative results per kernel

To see the relative results for each kernel, run the following command:

```console
~/fastpath/fastpath/fastpath result show results-fastpath_test_010826-1837 --swprofile fp_6.19.0-rc1-ubuntu --relative
```

Relative in this case means that the statistics displayed are relative to the mean. In addition to the min/mean/max, you're also given the confidence interval bounds, the coefficient of variation, and the number of samples.

The output is similar to:

```output
+------------------+--------------------+--------+----------+--------+----------+--------+--------+-------+
| Benchmark        | Result Class       |    min | ci95min  |   mean | ci95max  |    max |     cv | count |
+------------------+--------------------+--------+----------+--------+----------+--------+--------+-------+
| speedometer/v2.1 | score (runs/min)   | -1.81% |  -2.42%  | 221.00 |   2.42%  |  1.81% |  1.52% |     4 |
+------------------+--------------------+--------+----------+--------+----------+--------+--------+-------+
```

You can run it again for the other kernel:

```console
~/fastpath/fastpath/fastpath result show results-fastpath_test_010826-1837 --swprofile fp_6.18.1-ubuntu --relative
```

The output is similar to:

```output
+------------------+--------------------+--------+----------+--------+----------+--------+--------+-------+
| Benchmark        | Result Class       |    min | ci95min  |   mean | ci95max  |    max |     cv | count |
+------------------+--------------------+--------+----------+--------+----------+--------+--------+-------+
| speedometer/v2.1 | score (runs/min)   | -0.86% |  -1.25%  | 233.00 |   1.25%  |  0.86% |  0.78% |     4 |
+------------------+--------------------+--------+----------+--------+----------+--------+--------+-------+
```

### Compare results between kernels

To compare the relative results between both kernels, run:

```console
~/fastpath/fastpath/fastpath result show results-fastpath_test_010826-1837 --swprofile fp_6.19.0-rc1-ubuntu --swprofile fp_6.18.1-ubuntu --relative
```

The output is similar to:

```output
+------------------+--------------------+-----------------------+---------------------+
| Benchmark        | Result Class       | fp_6.19.0-rc1-ubuntu  | fp_6.18.1-ubuntu    |
+------------------+--------------------+-----------------------+---------------------+
| speedometer/v2.1 | score (runs/min)   |                221.00 |               3.39% |
+------------------+--------------------+-----------------------+---------------------+
```
We see 6.18.1 is performing slightly better than 6.19-rc1 in this benchmark.

More examples of analyzing results can be found in the [Fastpath Results User Guide](https://fastpath.docs.arm.com/en/latest/user-guide/resultshow.html).

When you're done testing, remember to terminate your EC2 instances and clean up any other AWS resources you created to avoid unnecessary charges.
