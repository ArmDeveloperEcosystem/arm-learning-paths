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
The results show that 6.18.1 performs slightly better than 6.19-rc1 in this benchmark, with a 3.39% improvement.

More examples of analyzing results can be found in the [Fastpath Results User Guide](https://fastpath.docs.arm.com/en/latest/user-guide/resultshow.html).

## Clean up resources

When you're done testing, clean up your AWS resources to avoid unnecessary charges.

### Terminate EC2 instances

You can terminate instances from the AWS Console or using the AWS CLI:

```console
aws ec2 terminate-instances --instance-ids <INSTANCE_ID>
```

Replace `<INSTANCE_ID>` with the IDs of your build host, Fastpath host, and SUT instances.

### Delete CloudFormation stacks (if used)

If you used CloudFormation templates, delete the stacks:

```console
aws cloudformation delete-stack --stack-name fastpath-build
aws cloudformation delete-stack --stack-name fastpath-host
aws cloudformation delete-stack --stack-name fastpath-sut
```

### Remove security groups and other resources

After the instances are terminated, remove any custom security groups, key pairs, or other resources you created specifically for this Learning Path.

## What you've accomplished and what's next

In this section, you:
- Analyzed benchmark results using Fastpath's result commands
- Compared kernel performance metrics between multiple versions
- Identified performance differences between v6.18.1 and v6.19-rc1 kernels
- Cleaned up AWS resources to avoid unnecessary charges

You now have a complete workflow for building custom kernels, deploying them to test systems, and comparing their performance using Fastpath. You can use this approach to test kernel patches, configuration changes, or different kernel versions for your specific workloads. To continue exploring, consider testing different benchmarks from the Fastpath library, experimenting with kernel configuration options, or comparing performance across different instance types.
