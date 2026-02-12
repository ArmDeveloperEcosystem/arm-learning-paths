---
title: "Generate and execute the benchmark plan"
weight: 11

layout: "learningpathall"
---

With all required components in place, it's time to generate a Fastpath benchmark plan, execute it, and analyze the results.

## Generate the Fastpath plan

Fastpath uses a YAML-formatted [plan file](https://fastpath.docs.arm.com/en/latest/user-guide/planexec.html#introduction) to define the system under test (SUT), the kernels to deploy, and the benchmark workloads to run.

This YAML file can be manually authored, but to simplify the process for this Learning Path, a helper script is provided that gathers the required information and produces a valid `plan.yaml` file.


Run the following on the Fastpath host to activate the Fastpath virtual environment and run the plan generator script. Have your SUT's private IP address handy, as you'll be prompted to enter it:

```command
source ~/venv/bin/activate
cd ~/arm_kernel_install_guide
./scripts/generate_plan.sh
```

When complete, the script creates the plan with an auto-generated name and provides a list of frequently performed tasks relative to the plan:

```output
Enter SUT private IP: 172.31.100.19
Plan name:
  fastpath_test_010826-1837

Plan written to:
  /home/ubuntu/arm_kernel_install_guide/plans/fastpath_test_010826-1837.yaml

Run Fastpath with:
  ~/fastpath/fastpath/fastpath plan exec --output results/ /home/ubuntu/arm_kernel_install_guide/plans/fastpath_test_010826-1837.yaml

After Fastpath run completes, gather results with:
  ~/fastpath/fastpath/fastpath result list results/ --object swprofile

Relative results per kernel:
  ~/fastpath/fastpath/fastpath result show results/ --swprofile fp_6.19.0-rc1-ubuntu --relative
  ~/fastpath/fastpath/fastpath result show results/ --swprofile fp_6.18.1-ubuntu --relative

Comparison between kernels:
  ~/fastpath/fastpath/fastpath result show results/ --swprofile fp_6.19.0-rc1-ubuntu --swprofile fp_6.18.1-ubuntu --relative
```

## Understand the Fastpath benchmark plan

With the plan generated, you can now run Fastpath to execute the benchmark workloads defined in the plan.

Before you do, take a quick look at the generated plan file to see what kernels and workloads are defined.

Replace the filename with your plan filename.

```console
cat plans/fastpath_test_010826-1837.yaml 
```

The plan will be printed:

```output
sut:
  name: fastpath_test_010826-1837
  connection:
    method: SSH
    params:
      user: fpuser
      host: 172.31.100.19
swprofiles:
- name: fp_6.19.0-rc1-ubuntu
  kernel: /home/ubuntu/kernels/6.19.0-rc1-ubuntu+/Image.gz
  modules: /home/ubuntu/kernels/6.19.0-rc1-ubuntu+/modules.tar.xz
- name: fp_6.18.1-ubuntu
  kernel: /home/ubuntu/kernels/6.18.1-ubuntu+/Image.gz
  modules: /home/ubuntu/kernels/6.18.1-ubuntu+/modules.tar.xz
benchmarks:
- include: speedometer/v2.1.yaml
defaults:
  benchmark:
    warmups: 1
    repeats: 2
    sessions: 2
    timeout: 1h
```

Within the YAML file, you can see the plan name and connection info for the SUT.

Under swprofiles, the two kernel variants built earlier are defined, along with their paths on the Fastpath host (which will be pushed to the SUT during test runtime).

Under benchmarks, the Speedometer v2.1 benchmark workload is specified to run against each kernel.

For more information on the plan file format and options, see the [Fastpath PlanExec User Guide](https://fastpath.docs.arm.com/en/latest/user-guide/planexec.html).

For a list of current benchmarks supported by Fastpath, see the [Fastpath Benchmark User Guide](https://fastpath.docs.arm.com/en/latest/user-guide/planschema.html#benchmark-library).

## Execute the Fastpath benchmark plan

An example plan execution command line is given under the "Run Fastpath with:" section of the plan generator's output, similar to:

```console
source ~/venv/bin/activate
~/fastpath/fastpath/fastpath plan exec --output results-fastpath_test_010826-1837 /home/ubuntu/arm_kernel_install_guide/plans/fastpath_test_010826-1837.yaml
```

Copy and paste that line to begin the testing:

```output
Executing fastpath_test_010826-1837.yaml...
  0%|          | 0/12 [00:00<?, ?it/s]
100%|██████████| 12/12 [10:36<00:00, 53.05s/it]
```

{{% notice Note %}}
In the above command, the `--output` parameter specifies the directory where Fastpath stores benchmark results. If the directory doesn't exist, Fastpath creates it and continues. However, if it does exist already, Fastpath will exit with an error because it doesn't want to add more results to that existing folder (unless explicitly told to do so).

The solution is to use the `--append` parameter at the end of the `fastpath plan exec` command with the existing folder name, or specify a new output directory without the `--append` parameter.
{{% /notice %}}

When the execution completes 100%, Fastpath will have run the Speedometer benchmark against both kernels on the SUT and stored the results in the specified output directory.

In the next section, you'll learn how to analyze and compare the results.
