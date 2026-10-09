---
title: Analyze the performance of MongoDB on Arm servers

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to learn how to deploy and measure MongoDB performance on Arm servers.

description: Install MongoDB on Arm servers and benchmark database performance using Yahoo Cloud Serving Benchmark (YCSB) to compare against other architectures.

learning_objectives:
- Install and run MongoDB on an Arm server.
- Test MongoDB performance using open-source tooling.
- Measure and compare the performance of MongoDB on Arm versus other architectures with YCSB.

prerequisites:
- An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider, or access to the Arm AGI CPU

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:53:07Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d9de7909403eaf16499db936d900459d84f3834db4f0100883d2e561bd3f0913
  summary_generated_at: '2026-09-28T19:53:07Z'
  summary_source_hash: d9de7909403eaf16499db936d900459d84f3834db4f0100883d2e561bd3f0913
  faq_generated_at: '2026-09-28T19:53:07Z'
  faq_source_hash: d9de7909403eaf16499db936d900459d84f3834db4f0100883d2e561bd3f0913
  summary: >-
    You'll install and benchmark MongoDB Community Edition 8.0 on Arm-based Linux servers. First, you'll configure
    a three-node replica set and a separate YCSB client. Then, you'll load
    data, run common read and update mixes, warm up the database, and adjust threads and dataset
    parameters to increase CPU use. You can also run a Java-based performance tool for targeted
    operation mixes and compare results across systems.
  faqs:
  - question: Which Linux distributions can I use to install MongoDB Community Edition 8.0 on
      Arm?
    answer: >-
      You can use Ubuntu 20.04, 22.04, or 24.04; RHEL or CentOS 8 and 9; or Amazon Linux 2023.
      For more information, see the MongoDB [Platform Support Matrix](https://www.mongodb.com/docs/manual/administration/production-notes/#platform-support-matrix).
  - question: How should I set up the environment to run YCSB against MongoDB?
    answer: >-
      Use one instance for the YCSB client and one or more instances for MongoDB. For the recommended
      topology, create three equal-size replica-set nodes and send test traffic to the designated
      primary.
  - question: Which YCSB workloads should I run first, and how long should I warm up?
    answer: >-
      Start with a 95% read and 5% update mix, which is recommended for real-world testing.
      You can also run 100% read or a 90% read and 10% update mix. Warm up the database for about
      five minutes before you collect performance data.
  - question: What should I change if CPU utilization is low during the benchmark?
    answer: >-
      Increase the thread count and adjust `operationcount` and `recordcount`. Aim for about 90%
      or higher CPU utilization before you record measurements.
  - question: What software do I need to run the benchmarking tools?
    answer: >-
      Install Java and `curl`, then use the bundled `bin/ycsb.sh` launcher for YCSB. Install an
      OpenJDK runtime if you also use the alternative MongoDB performance test tool.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

armips:
- Neoverse

operatingsystems:
- Linux

layout: learningpathall
learning_path_main_page: 'yes'
skilllevels: Introductory
subjects: Databases
platforms:
  - Arm AGI CPU  
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
test_maintenance: false
tools_software_languages:
- MongoDB
- GCC
- Runbook

further_reading:
    - resource:
        title: MongoDB Manual
        link: https://www.mongodb.com/docs/manual/
        type: documentation
    - resource:
        title: MongoDB Performance Tool
        link: https://github.com/idealo/mongodb-performance-test#readme
        type: documentation
    - resource:
        title: YCSB
        link: https://github.com/brianfrankcooper/YCSB/wiki/
        type: documentation
    - resource:
        title: Compare performance of MongoDB on Arm vs Intel
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/mongodb-performance-on-aws-with-the-arm-graviton2
        type: blog

weight: 1
---
