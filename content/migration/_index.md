---
title: "How can I migrate applications to Arm Neoverse?"
layout: "migration"       # Easier for dynamic content loading, keep the same
description: Software developers are embracing the Arm architecture for its superior price performance and energy efficiency across a wide range of applications, including containerized workloads, cloud managed services, and Linux applications. To achieve higher performance and lower cost, you can migrate your self-managed workloads to Arm virtual machines and make sure to select Arm for managed services. A three step migration process covers the most common scenarios, and provides links to additional resources.
---

## PREFACE: Learn and explore

Arm Neoverse is a family of processor cores designed for servers and cloud data centers. There are 2 families currently available, Neoverse V-series and Neoverse N-series.

### What is Arm Neoverse?

Neoverse V-series offers the highest overall performance, and Neoverse N-series offers industry-leading performance-per-watt and serves a broad set of server and cloud use cases. Each Neoverse CPU implements a version of the [Arm architecture](https://www.arm.com/architecture/cpu). Arm continually works with partners to advance the architecture and increase computing capability. Neoverse cores focus on predictable per-socket performance and do not rely on multithreading or extreme clock speeds.

Below is a list of Neoverse CPUs, the architecture versions, and the key additions for each.

| CPU         | Architecture version | Key additions |
| ----------- | -------------------- | --------------------------------------------------------- |
| Neoverse-N1 | Armv8.2-A            | LSE - Large System Extensions improves multi-threaded performance. |
| Neoverse-V1 | Armv8.4-A            | SVE - Scalable Vector Extension adds high performance vector processing for HPC and AI workloads. |
| Neoverse-N2 | Armv9.0-A            | SVE2 - Extends SVE for improved data parallelism and wider vectors. |
| Neoverse-V2 | Armv9.0-A            | SVE2 - Targets high single threaded performance for HPC and AI workloads. |

### What cloud hardware is available today?

Review each cloud service provider below to learn about Arm-based servers.

{{< tabpane-normal >}}
  {{< tab header="AWS">}}

AWS offers more than [150 instance types with Graviton processors](https://aws.amazon.com/ec2/graviton/). The largest instance has 192 vCPUs and 1.5 TB of memory. A wide variety of instance sizes are available, including bare-metal (look for '.metal'). To find instances with Graviton processors look for 'g' in the name (C7g, M7g, and R7g). 

| Generation    | Arm CPU      | Instance types | Comments                                                                    |
|---------------|--------------|----------------|-----------------------------------------------------------------------------|
| Graviton  | Cortex-A72   | A1             | First Arm-based instance.
| Graviton2 | Neoverse-N1  | C6g, M6g, R6g  | 600% performance and efficiency increases.                                  |
| Graviton3 | Neoverse-V1  | C7g, M7g, R7g  | 25% performance increase, DDR5 memory added, 50% more memory bandwidth.     |
| Graviton4 | Neoverse-V2  | R8g            | 75% more memory bandwidth, up to 40% faster for databases and 30% faster for web applications.   |

  {{< /tab >}}
  {{< tab header="Google GCP">}} 
Google GCP offers a variety of [virtual machine instances with Arm processors](https://cloud.google.com/compute/docs/instances/arm-on-compute). The latest generation of Arm-based VMs are based on Google Axion processor. The largest instance has 72 vCPUs and 576 Gb of RAM. It does not offer bare-metal instances. It offers `highcpu` and `highmem` VM instances for compute and memory intensive workloads respectively.

| Generation    | Arm CPU      | Instance types     | Comments  |  
| --------------|--------------|--------------------|-----------|
| T2A       | Neoverse-N1  | T2A-standard | Optimized for general-purpose workloads - web servers, and microservices. |
| Axion (C4A) | Neoverse-V2 | c4a-standard, c4a-highmem, c4a-highcpu  | General-purpose, AI/ML workloads and high performance computing. |

  {{< /tab >}}
  {{< tab header="Microsoft Azure">}}
Microsoft Azure offers a variety of [virtual machine instances with Arm Neoverse processors](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dpsv6-series). The latest generation of Arm-based VMs are based on Cobalt 100 CPU. The largest instance has 96 vCPUs and 384 Gb of RAM in the 'D96ps_v6' format. It does not offer bare-metal instances. It offers compute for general-purpose workloads (Dps and Dpls) and memory-optimized workloads (Eps).

| Generation    | Arm CPU      | Instance types     | Comments  |  
| --------------|--------------|--------------------|-----------|
| Dpsv5      | Neoverse-N1  | Dpsv5, Epsv5       | General purpose and memory optimized instances. |
| Dpsv6      | Neoverse-N2  | Dpsv6, Dpls6, Epsv6 | Cobalt 100 processor improves performance, Dpsv6 (general purpose 4:1 mem:cpu ratio), Dplsv6 (general purpose, 2:1 mem:cpu ratio), Epsv6 (memory-optimized, 8:1 mem:cpu ratio). |

  {{< /tab >}}
  {{< tab header="Oracle OCI">}} 
Oracle Cloud Infrastructure (OCI) Ampere [Arm-based compute](https://www.oracle.com/cloud/compute/arm/) provides market-leading price-performance for AI, containers, big data, web services, and related workloads. The largest intsance has 160 vCPUs and 1024 Gb of RAM in the 'BM.Standard.A1' format. It offers bare-metal instances (look for 'BM' as opposed to 'VM'). 

| Generation    | Arm CPU      | Instance types         | Comments  |  
| --------------|--------------|--------------------|-----------|
| A1            | Neoverse-N1  | VM.Standard.A1  | Offers predefined (.#CPUs) or dynamic OCPU and memory allocation (.Flex) |
| A2            | AmpereOne    | VM.Standard.A2, VM.Optimized3.A2 | Tailored for high-performance and memory-intensive workloads. |

  {{< /tab >}}

{{< /tabpane-normal >}}

Read [Get started with Servers and Cloud Computing](https://learn.arm.com/learning-paths/servers-and-cloud-computing/intro) to learn more and find additional cloud service providers.

## STEP 1: Plan your transition

Newer software is generally easier to migrate because Arm support continues to improve and performance optimizations are typically better in newer versions. Interpreted languages and Jit compilers, such as Python, Java, PHP, and Node.js are easiest to migrate. Compiled languages such as C/C++, Go, and Rust are slightly more difficult because they need to be recompiled. The most difficult situations involve a language, runtime, operating  system, or something else which is not available on Arm or would be difficult to run on Arm.


### 1.1 Survey your software stack

Step one in a typical migration journey is understanding the software stack. Make notes about operating  system versions, programming languages, development tools, container  tools, performance analysis tools, and any other important scripts included in the project. You can reference **Migrating applications to Arm servers** below for tips on how to get started - setting up a development machine, common challenges, and tips to proceed at pace.

[Migrating applications to Arm servers](https://learn.arm.com/learning-paths/servers-and-cloud-computing/migration/)

### 1.2 Discover Arm compatibility

Step two is to look through your scripts and build files and see if you spot architecture specific files. Software migration typically falls into 3 categories:
1. **Automatic:** The Linux package manager installs software from the main repositories without any changes, totally seamless.
2. **Small modifications:** Software installed using scripts or binary downloads requires minor changes to strings, such as changing “x86_64” and “amd64” to “arm64” or “aarch64”.
3. **Challenging:** A few software projects still don't support Arm Linux, some are well known projects like the Edge browser, and the others are smaller projects that haven't added Arm support, yet. Some could be blockers and others may be easy to compile yourself.

You can quickly find out if software dependencies are available for Arm using the **Software Ecosystem Dashboard for Arm** link below - search for your package and find out which versions work on Arm and review the getting started tips. The dashboard is actively growing, and is a good place to understand if your software stack will run on Arm servers.

[Software Ecosystem Dashboard for Arm.](https://www.arm.com/developer-hub/ecosystem-dashboard/) 

### 1.3 Find resources to help

The below resources are curated to address migration challenges on specific cloud providers. Look through them for additional context.
- [Porting architecture specific intrinsics](https://learn.arm.com/learning-paths/cross-platform/intrinsics/) - perfect for porting intrinsics from another architecture.
- [Arm software install guides](https://learn.arm.com/install-guides) - good for quickly installing common tools and software.
- [simd.info](https://simd.info/) - a searchable reference tool for C intrinsics for SIMD engines.
- [Arm Infrastructure Solutions blog](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/) - an Arm-specific technical blog.
- [Arm Learning Paths for Servers and Cloud](https://learn.arm.com/learning-paths/servers-and-cloud-computing/) - general tutorials for Arm servers. You can search for specific cloud service providers, including [AWS](https://learn.arm.com/learning-paths/servers-and-cloud-computing/?cloud-service-providers-filter=aws/#), [Google Cloud](https://learn.arm.com/learning-paths/servers-and-cloud-computing/?cloud-service-providers-filter=google-cloud/#), [Microsoft Azure](https://learn.arm.com/learning-paths/servers-and-cloud-computing/?cloud-service-providers-filter=microsoft-azure/#), and [Oracle](https://learn.arm.com/learning-paths/servers-and-cloud-computing/?cloud-service-providers-filter=oracle/#).
     

- AWS has additional resources such as the [Porting Advisor for Graviton](https://learn.arm.com/install-guides/porting-advisor/) and [AWS Graviton Technical Guide](https://github.com/aws/aws-graviton-getting-started).

Lastly, below are some specific migration helpers for various types of software:

{{< tabpane-normal >}}

  {{< tab header="Containers">}} 

Which tools are available for building and running containers on Arm servers? 

| Tool | Learning Paths | Other Content (Blogs/Videos) |
|-----------|----------------|----------------------------------------|
| Docker | [Learn how to use Docker](https://learn.arm.com/learning-paths/cross-platform/docker/) | [How to build cloud-native applications for multi-architecture infrastructure](https://stackoverflow.blog/2024/02/05/how-to-build-cloud-native-applications-for-multi-architecture-infrastructure/)
| AWS CodeBuild  | [Build and share Docker images using AWS CodeBuild](https://learn.arm.com/learning-paths/servers-and-cloud-computing/codebuild/) | |
| Docker Build Cloud | [Build multi-architecture container images with Docker Build Cloud](https://learn.arm.com/learning-paths/cross-platform/docker-build-cloud/) | [Supercharge your Arm builds with Docker Build Cloud: Efficiency meets performance](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/supercharge-arm-builds-with-docker-build-cloud) |
| GitHub Actions (GitHub runners) | [Build multi-architecture container images with GitHub Arm-hosted runners](https://learn.arm.com/learning-paths/cross-platform/github-arm-runners/) | [Arm64 on GitHub Actions: Powering faster, more efficient build systems](https://github.blog/news-insights/product-news/arm64-on-github-actions-powering-faster-more-efficient-build-systems/) |
| GitHub Actions (AWS Graviton runners) | [Managed, self-hosted Arm runners for GitHub Actions](https://learn.arm.com/learning-paths/servers-and-cloud-computing/github-actions-runner/) |
| GitLab (GitLab runners) | [Build a CI/CD pipeline with GitLab on Google Axion](https://learn.arm.com/learning-paths/cross-platform/gitlab/) |  |

  {{< /tab >}}

  {{< tab header="Programming Languages">}}

Which programming languages work on Arm servers? - Nearly all of them.

| Languages | Learning Paths | Other Content (Blogs/Videos) |
|-----------|----------------|----------------------------------------|
| C/C++ | [Migrating C/C++ applications](https://learn.arm.com/learning-paths/servers-and-cloud-computing/migration/c-c++/) | [What is new in LLVM 18?](https://community.arm.com/arm-community-blogs/b/tools-software-ides-blog/posts/p1-whats-new-in-llvm-18) |
| Rust | [Rust Install Guide](https://learn.arm.com/install-guides/rust/) | [Neon Intrinsics in Rust](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/rust-neon-intrinsics) |
| Java | [Java Install Guide](https://learn.arm.com/install-guides/java/) | [Improving Java performance on Neoverse N1 systems](https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/java-performance-on-neoverse-n1) |
|      | [Migrating Java applications](https://learn.arm.com/learning-paths/servers-and-cloud-computing/migration/java/) | [Java Vector API on AArch64](https://community.arm.com/arm-community-blogs/b/high-performance-computing-blog/posts/java-vector-api-on-aarch64) |
|      | [Run Java applications on Google Axion](https://learn.arm.com/learning-paths/servers-and-cloud-computing/java-on-axion/)| [Java on Graviton](https://github.com/aws/aws-graviton-getting-started/blob/main/java.md) |
|      | | [Optimizing Java Workloads on Azure General Purpose D-series v5 VMs with Microsoft’s Build of OpenJDK](https://techcommunity.microsoft.com/t5/azure-compute-blog/optimizing-java-workloads-on-azure-general-purpose-d-series-v5/ba-p/3827610) |
|      | | [Improving Java performance on OCI Ampere A1 compute instances](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/performance-of-specjbb2015-on-oci-ampere-a1-compute-instances) |
| Go | [Go Install Guide](https://learn.arm.com/install-guides/go/) | [Making your Go workloads up to 20% faster with Go 1.18 and AWS Graviton](https://aws.amazon.com/blogs/compute/making-your-go-workloads-up-to-20-faster-with-go-1-18-and-aws-graviton/)|
| .NET | [.NET Install Guide](https://learn.arm.com/install-guides/dotnet/) | [Arm64 Performance Improvements in .NET 7](https://devblogs.microsoft.com/dotnet/arm64-performance-improvements-in-dotnet-7/) |
|      | [Deploy .NET application on Azure Cobalt 100 VMs](https://learn.arm.com/learning-paths/servers-and-cloud-computing/azure-cobalt-cicd-aks/) | [Arm64 Performance Improvements in .NET 8](https://devblogs.microsoft.com/dotnet/this-arm64-performance-in-dotnet-8/) |
| Python | | [Python on Arm](https://community.arm.com/arm-community-blogs/b/tools-software-ides-blog/posts/python-on-arm)|
| PHP | | [Improving performance of PHP for Arm64 and impact on AWS Graviton2 based EC2 instances](https://aws.amazon.com/blogs/compute/improving-performance-of-php-for-arm64-and-impact-on-amazon-ec2-m6g-instances/) |

  {{< /tab >}}
  {{< tab header="Optimized Libraries">}}

Which key libraries are optimized for Arm servers?

| Library/Framework | Learn More | Blogs |
|-------------------|------------|-------|
| x264/x265 | [Run x265 (H.265 codec) on Arm servers](https://learn.arm.com/learning-paths/servers-and-cloud-computing/codec/) |  [Improve video encoding price/performance by up to 36% with Arm Neoverse based Amazon EC2 C6g instances](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/thirty-six-percent-better-video-encoding-with-aws-graviton2_2d00_based-c6g) |  
|  |  | [Reduce H.265 High-Res Encoding Costs by over 80% with AWS Graviton2](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/reduce-h-265-high-res-encoding-costs-by-over-80-with-aws-graviton2-1207706725) |
|  |  | [Ampere Altra Max Delivers Sustainable High-Resolution H.265 Encoding](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/ampere-altra-max-delivers-sustainable-high-resolution-h-265-video-encoding-without-compromise) |
|  |  | [OCI Ampere A1 Compute instances can significantly reduce video encoding costs versus modern CPUs](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/oracle-cloud-infrastructure-arm-based-a1) |
| ArmPL | [Arm Performance Libraries install guide](https://learn.arm.com/install-guides/armpl/) | [Arm Compiler for Linux and Arm Performance Libraries 24.04](https://community.arm.com/arm-community-blogs/b/high-performance-computing-blog/posts/arm-compiler-for-linux-and-arm-performance-libraries-24-04) |
| ArmRAL | [Get started with the Arm 5G RAN Acceleration Library (ArmRAL)](https://learn.arm.com/learning-paths/servers-and-cloud-computing/ran/) | [The next chapter for Arm RAN Acceleration Library: Open-sourcing the code base & accelerating adoption](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/arm-ral-is-now-open-source) |
| OpenSSL | | |
| VP9 | [Run the AV1 and VP9 codecs on Arm Linux](https://learn.arm.com/learning-paths/servers-and-cloud-computing/codec1/) | [Arm-based cloud instances outperform x86 instances by up to 64% on VP9 encoding](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/arm-outperforms-x86-by-up-to-64-percent-on-vp9) |
| ISA-L | | |
| IPSEC-MB | | |
| AV1 | [Run the AV1 and VP9 codecs on Arm Linux](https://learn.arm.com/learning-paths/servers-and-cloud-computing/codec1/) | |
| SLEEF | | [A New Pulse for SLEEF](https://sleef.org/2024/10/02/new-pulse.html) |
| AES | | [AWS Graviton3 delivers leading AES-GCM encryption performance](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/aes-gcm-optimizations-for-armv8-4-on-neoverse-v1-graviton3)  |
| Snappy | [Measure performance of compression libraries on Arm servers](https://learn.arm.com/learning-paths/servers-and-cloud-computing/snappy/) | [Comparing data compression algorithm performance on AWS Graviton2](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/comparing-data-compression-algorithm-performance-on-aws-graviton2-342166113) |
| Cloudflare zlib | [Learn how to build and use Cloudflare zlib on Arm servers](https://learn.arm.com/learning-paths/servers-and-cloud-computing/zlib/) | |

  {{< /tab >}}

  {{< tab header="Databases">}} 

Which databases are available on Arm servers?

| Database | Learning Paths | Other Content (Blogs/Videos) |
|-----------|----------------|----------------------------------------|
| MySQL | [Deploy WordPress with MySQL on Elastic Kubernetes Service (EKS)](https://learn.arm.com/learning-paths/servers-and-cloud-computing/eks/) | |
| MySQL | [Learn how to deploy MySQL](https://learn.arm.com/learning-paths/servers-and-cloud-computing/mysql/) | |
| MySQL | [Benchmarking MySQL with Sysbench](https://learn.arm.com/learning-paths/servers-and-cloud-computing/mysql_benchmark/) | | 
| MySQL | [Learn how to Tune MySQL](https://learn.arm.com/learning-paths/servers-and-cloud-computing/mysql_tune/)  | |
| PostgreSQL | [Learn how to deploy PostgreSQL](https://learn.arm.com/learning-paths/servers-and-cloud-computing/postgresql/) | |
| Flink | [Benchmark the performance of Flink on Arm servers](https://learn.arm.com/learning-paths/servers-and-cloud-computing/flink/) |
| Clickhouse | [Measure performance of ClickHouse on Arm servers](https://learn.arm.com/learning-paths/servers-and-cloud-computing/clickhouse/) | [Improve ClickHouse Performance up to 26% by using AWS Graviton3](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/improve-clickhouse-performance-up-to-26-by-using-aws-graviton3) |
| MongoDB | [Test the performance of MongoDB on Arm servers](https://learn.arm.com/learning-paths/servers-and-cloud-computing/mongodb/) | [MongoDB performance on Arm Neoverse based AWS Graviton2 processors](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/mongodb-performance-on-aws-with-the-arm-graviton2) |
| Redis | [Deploy Redis on Arm](https://learn.arm.com/learning-paths/servers-and-cloud-computing/redis/) | [Improve Redis performance up to 36% by deploying on Alibaba Cloud Yitian 710 instances](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/improve-redis-performance-by-deploying-on-alibaba-cloud-yitian-710-instances) |
| Spark | [Learn how to deploy Spark on AWS Graviton2](https://learn.arm.com/learning-paths/servers-and-cloud-computing/spark/) | [Spark on AWS Graviton2 best practices: K-Means clustering case study](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/optimize-spark-on-aws-graviton2-best-practices-k-means-clustering) |
| MariaDB | [Deploy MariaDB on Arm servers](https://learn.arm.com/learning-paths/servers-and-cloud-computing/mariadb/) |
| Elasticsearch/Opensearch |  |
| Spark+Gluten+Velox |  |
| Pinecone |  |

  {{< /tab >}}

  {{< tab header="Web applications">}} 
Which software helps me build web applications on Arm servers?
| Software | Learning Paths | Other Content (Blogs/Videos) |
|-----------|----------------|----------------------------------------|
| Nginx | [Learn how to deploy Nginx](https://learn.arm.com/learning-paths/servers-and-cloud-computing/nginx/) | [Nginx Performance on AWS Graviton3](https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/nginx-performance-on-graviton-3) |
| | [Learn how to tune Nginx](https://learn.arm.com/learning-paths/servers-and-cloud-computing/nginx_tune/) |  |
| Django | [Learn how to deploy a Django application](https://learn.arm.com/learning-paths/servers-and-cloud-computing/django/) |  |


  {{< /tab >}}

  {{< tab header="Networking">}} 
Which networking software works on Arm servers?

| Software | Learning Paths | Other Content (Blogs/Videos) |
|-----------|----------------|----------------------------------------|
| Vectorscan | [Install Vectorscan (Hyperscan on Arm) and use it with Snort 3](https://learn.arm.com/learning-paths/servers-and-cloud-computing/vectorscan/) | |
| DPDK | | [DPDK Tuning Guide](https://developer.arm.com/documentation/109701/1-0/?lang=en) |
  {{< /tab >}}

{{< /tabpane-normal >}}

## STEP 2: Test, build, and run

Based on your initial research, decide how to proceed with trying your software on Arm. In general, you can use a top-down or bottom-up strategy to migrate to Arm. Select a methodology and use the resources above to build and run your application. 

### 2.1 Top-down methodology

Top-down porting involves moving the complete software stack to an Arm machine and trying to build and run it straightaway. You will almost certainly face errors, which you can address one at a time until the full application runs on Arm. 

![Top-down porting methodology](/migration/Top-down.png) 

This methodology is great for simpler stacks, when breaking down the problem would take more time than fixing errors iteratively. 

### 2.2 Bottom-up methodology

Bottom-up porting is more systematic. Here, you break apart your software stack, starting with the foundations of your app to get those running on an Arm server first. Then add back one or two software packages at a time, and recompile and run to ensure it works on Arm. If errors arise, fix them or replace the incompatible package with an Arm compatible version. Continue building back your stack until it is fully formed on an Arm server. 

![Bottom-up porting methodology](/migration/Bottom-up.png) 

This methodology is sensible for large stacks, where running the whole app on Arm immediately would cause too many errors to effectively work through.

## STEP 3: Optimize your application

If you've reached this step, congratulations! Your application is running on Arm. The next action is to ensure it is running optimally. 

### 3.1 Measure performance

Once the application is running you can measure performance. This can be as simple as timing an application or may involve using performance analysis tools.

You may have some performance analysis methodologies you already follow, continue to use those. 

Below are some additional performance analysis tips and methodologies specific to Arm-based servers:
- [Learn the Arm Neoverse N1 performance analysis methodology](https://learn.arm.com/learning-paths/servers-and-cloud-computing/top-down-n1/)
- [Profiling for Neoverse with Streamline CLI Tools](https://learn.arm.com/learning-paths/servers-and-cloud-computing/profiling-for-neoverse/)
- [Learn how to optimize an application with BOLT](https://learn.arm.com/learning-paths/servers-and-cloud-computing/bolt/)
- [How to use the Arm Performance Monitoring Unit and System Counter](https://learn.arm.com/learning-paths/servers-and-cloud-computing/arm_pmu/)
- [NVIDIA Grace CPU Benchmarking Guide](https://nvidia.github.io/grace-cpu-benchmarking-guide/index.html)
- [Learn about Large System Extensions (LSE)](https://learn.arm.com/learning-paths/servers-and-cloud-computing/lse/)

### 3.2 Ask for help

Your goal is to understand if the performance you see will translate into the expected price performance advantages. If you are unsure or need additional help you can ask the Arm developer community for help. Join the [Arm Developer Program](https://www.arm.com/resources/developer-program) and talk directly to other developers and Arm Experts on Discord.

### DELIVER: Deploy your application to users

Once the price performance gains are confirmed, you can plan for a larger deployment. 

Deployment is outside the scope of this guide, but here are some concepts to keep in mind:
- Experiment with different virtual machine sizes and instance types to find the best fit for your application.
- Add some Arm nodes to your Kubernetes cluster and run a subset of workloads on Arm.
- Direct some of your web traffic to an Arm version of the application.
- Create a complete version of your application in a dev environment for additional testing.

Make sure to research the details needed for these tasks by checking any places you use infrastructure as code or other places you store details about virtual machine types and sizes, as well as parameters for managed services.

You can also check [Works on Arm](https://www.arm.com/markets/computing-infrastructure/works-on-arm) for the latest cloud and CI/CD initiatives for developers.

## Summary

With this 3 step process and the provided resources, you are well positioned to migrate your applications to Arm. Happy porting!
