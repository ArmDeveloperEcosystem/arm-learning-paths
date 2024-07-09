---
title: "How can I migrate my applications to Arm?"
layout: "migration"       # Easier for dynamic content loading, keep the same
---

Software developers are embracing the Arm architecture for its superior price performance and energy efficiency across a wide range of applications, including containerized workloads, cloud managed services, and Linux applications. 

To achieve higher performance and lower cost, you can migrate your self-managed workloads to Arm virtual machines and make sure to select Arm for managed services.

This three step migration guide covers the most common scenarios for adopting Arm. It also provides links to additional resources.

## STEP 1: Learn and explore

Before you start migrating applications, some background on Arm Neoverse is helpful.

### What is Arm Neoverse?

Arm Neoverse is a family of processor cores designed for servers and cloud data centers. There are 2 families of processors currently available, Neoverse V-series and Neoverse N-series.

Neoverse V-series offers the highest overall performance, and Neoverse N-series offers industry-leading performance-per-watt and serves a broad set of server and cloud use cases. Each Neoverse CPU implements a version of the [Arm architecture](https://www.arm.com/architecture/cpu). Arm continually works with partners to advance the architecture and increase computing capability.

Below is a list of Neoverse CPUs, the architecture versions, and examples of systems which use them. 

| CPU         | Architecture version | Example Cloud processors                      |
| ----------- | -------------------- | --------------------------------------------- |
| Neoverse V1 | Armv8.4-A            | AWS Graviton3                                 |
| Neoverse V2 | Armv9.0-A            | NVIDIA Grace, AWS Graviton4, Google Axion     |
| Neoverse N1 | Armv8.2-A            | Ampere Altra, Oracle A1, AWS Graviton2        |
| Neoverse N2 | Armv9.0-A            | Microsoft Cobalt                              |

Neoverse cores generally focus on high per-socket performance and do not rely on multithreading or extreme clock speeds to provide predictable performance. 

Read [Get started with Servers and Cloud Computing](https://learn.arm.com/learning-paths/servers-and-cloud-computing/intro) to learn more where you can find Arm hardware in the cloud.

## STEP 2: Plan your transition

Start your transition by researching your software requirements and identifying possible challenges.

### Survey your software

[Migrating applications to Arm servers](https://learn.arm.com/learning-paths/servers-and-cloud-computing/migration/) is a good place to start your migration journey. It explains how to set up a development machine, some migration challenges, and other tips for different programming languages. 

Make notes about operating system versions, programming languages, development tools, container tools, performance analysis tools, deployment tools, and any other important scripts included in the project.

Newer software is generally easier to migrate because Arm support continues to improve and performance optimizations are typically better in newer versions of software. 

Interpreted languages and Jit compilers, such as Python, Java, PHP, and Node.js are easiest to migrate. 

Compiled languages such as C/C++, Go, and Rust are slightly more difficult because they need to be recompiled. 

The most difficult situations involve a language, runtime, operating system, or something else which is not available on Arm and would be difficult to run on Arm. 

Depending on your situation, you may want to try the migration using a bottom-up approach or a top-down approach. A top-down example is to change the virtual machine instance types in your infrastructure-as-code to Arm instances, run the code, and debug as things fail. A bottom-up example is to to manually create an Arm virtual machine, pick out a part of your application or some of the dependencies, try to build and run on Arm, and slowly work up to running the complete application.

### Research dependencies

Look through your scripts and Makefiles to see if you spot architecture specific files. 

Migration typically falls into 3 categories:
1. The Linux package manager installs software from the main repositories without any changes, totally seamless.
2. Software installed using scripts or binary downloads requires minor changes to strings, such as changing “x86_64” and “amd64” to “arm64” or “aarch64”.
3. A few software projects still don't support Arm Linux, some are well known projects like the Edge browser, and the others are smaller projects that haven't added Arm support, yet. Some could be blockers and others may be easy to compile yourself.

The [Software Ecosystem Dashboard for Arm](https://www.arm.com/developer-hub/ecosystem-dashboard/) is a resource to identify if your software dependencies are available for Arm. 

Use the Ecosystem Dashboard to find software and understand if everything you need runs on Arm. If you don't find software listed, please raise an issue in the [GitHub project](https://github.com/ArmDeveloperEcosystem/ecosystem-dashboard-for-arm/) or submit a pull request. 

### Migration helpers

If you face specific issues with porting software you can try [Porting Advisor for Graviton](https://learn.arm.com/install-guides/porting-advisor/), a source code analysis tool which identifies incompatibilities.

If your code uses intrinsics from another architecture, you can use the libraries covered in [Porting architecture specific intrinsics](https://learn.arm.com/learning-paths/cross-platform/intrinsics/)

There are additional resources which may help you find answers to your migration questions:

- [All Arm Learning Paths for Servers and Cloud](https://learn.arm.com/learning-paths/servers-and-cloud-computing/) 
    - [AWS Learning Paths](https://learn.arm.com/learning-paths/servers-and-cloud-computing/?cloud-service-providers-filter=aws/#)
    - [Google Cloud Learning Paths](https://learn.arm.com/learning-paths/servers-and-cloud-computing/?cloud-service-providers-filter=google-cloud/#)
    - [Microsoft Azure Learning Paths](https://learn.arm.com/learning-paths/servers-and-cloud-computing/?cloud-service-providers-filter=microsoft-azure/#)
    - [Oracle Learning Paths](https://learn.arm.com/learning-paths/servers-and-cloud-computing/?cloud-service-providers-filter=oracle/#)
- [Infrastructure Solutions blog](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/)
- [Arm software install guides](https://learn.arm.com/install-guides)
- [AWS Graviton Technical Guide](https://github.com/aws/aws-graviton-getting-started) contains a wealth of information. 

Additional migration resources:
 - [Programming Languages](/migration/languages/)
 - [Optimized Libraries](/migration/libraries/)
 - [Containers](/migration/containers/)
 - [Databases](/migration/databases/)
 - [Web applications](/migration/web/)
 - [Networking](/migration/networking/)


## Build and run

Based on your initial research, decide how to proceed with trying your software on Arm. 

Use the resources above to build and run your application on Arm. 

Make sure to watch for any test tools or saved test results so you can plan for them on Arm. 

## STEP 3: Test and Optimize

### Measure performance

Once the application is running you can measure performance. This can be as simple as timing an application or may involve using performance analysis tools 

Additional performance analysis and benchmarking resources:
- [Learn the Arm Neoverse N1 performance analysis methodology](https://learn.arm.com/learning-paths/servers-and-cloud-computing/top-down-n1/)
- [Profiling for Neoverse with Streamline CLI Tools](https://learn.arm.com/learning-paths/servers-and-cloud-computing/profiling-for-neoverse/)
- [Learn how to optimize an application with BOLT](https://learn.arm.com/learning-paths/servers-and-cloud-computing/bolt/)
- [How to use the Arm Performance Monitoring Unit and System Counter](https://learn.arm.com/learning-paths/servers-and-cloud-computing/arm_pmu/)
- [NVIDIA Grace CPU Benchmarking Guide](https://nvidia.github.io/grace-cpu-benchmarking-guide/index.html)
- [Learn about Large System Extensions (LSE)](https://learn.arm.com/learning-paths/servers-and-cloud-computing/lse/)


Your goal is to understand if the performance you see will translate into the expected price performance advantages. If you are unsure or need additional help you can submit an issue on GitHub. 

### Deploy

Once the price performance gains are confirmed, you can plan for a larger deployment. 

This may involve a variety of steps:
- Experimenting with different virtual machine sizes or instance types to find the best fit for your application
- Adding some Arm notes to your Kubernetes cluster and running a subset of workloads on Arm
- Directing some of your web traffic to an Arm version of the application 
- Creating a complete version of your application in a dev environment for additional testing

Make sure to research the details needed for these tasks by checking any places you use infrastructure as code or other places you store details about virtual machine types and sizes, as well as parameters for managed services.

You can also check [Works on Arm](https://www.arm.com/markets/computing-infrastructure/works-on-arm) for the latest cloud and CI/CD initiatives for developers.

## Summary

The 3 step process combined with the available resources help you migrate applications to Arm.


