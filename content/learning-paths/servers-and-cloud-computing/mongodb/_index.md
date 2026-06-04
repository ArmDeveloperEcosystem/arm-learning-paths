---
title: Analyze the performance of MongoDB on Arm servers

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:32:28Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b52a1b60a74e19f2a3b60b8a77199ad5369c1ccd3b4d5ce0252a169d9f6123fd
  summary_generated_at: '2026-06-02T04:27:23Z'
  summary_source_hash: b52a1b60a74e19f2a3b60b8a77199ad5369c1ccd3b4d5ce0252a169d9f6123fd
  faq_generated_at: '2026-06-03T01:32:28Z'
  faq_source_hash: b52a1b60a74e19f2a3b60b8a77199ad5369c1ccd3b4d5ce0252a169d9f6123fd
  summary: >-
    Learn how to install MongoDB Community Edition 8.0 on Arm-based Linux servers and evaluate
    database performance using Yahoo Cloud Serving Benchmark (YCSB). You will provision an Arm
    instance from a cloud provider (such as AWS, Microsoft Azure, Google Cloud, or Oracle) and
    deploy MongoDB on supported distributions including Ubuntu 20.04/22.04/24.04, RHEL/CentOS
    8/9, and Amazon Linux 2023. The path covers configuring a three-node MongoDB replica set,
    installing supporting packages (Maven, Make, GCC), and running common YCSB workloads (95/5,
    100/0, 90/10) with warm-up and load-tuning guidance. An alternative Java-based MongoDB performance
    test tool using OpenJDK is also included. By the end, you can measure and compare MongoDB
    performance on Arm in about 30 minutes.
  faqs:
  - question: Which Linux distributions are supported for installing MongoDB Community Edition
      8.0 in this path?
    answer: >-
      Ubuntu 20.04, 22.04, and 24.04; RHEL/CentOS 8 and 9; and Amazon Linux 2023 are listed as
      supported. Refer to the Platform Support Matrix for additional details.
  - question: How should I structure the MongoDB environment for testing with YCSB?
    answer: >-
      Use two parts: one instance running YCSB and one or more instances running MongoDB. The
      recommended setup is a three-node replica set of equal-sized nodes, with one primary (the
      target for test traffic) and two secondary nodes.
  - question: What additional packages are required to run YCSB, and how do I install them on
      Ubuntu?
    answer: >-
      Additional software packages are required for YCSB. On Ubuntu, install maven, make, and
      gcc using: sudo apt install -y maven make gcc.
  - question: Which YCSB workloads should I run, for how long, and how do I know the system is
      exercised enough?
    answer: >-
      Common workloads are 95/5, 100/0, and 90/10, with 95/5 recommended for real-world testing.
      After loading the dataset, run the test for about five minutes to warm up, then target high
      CPU utilization (90%+) by adjusting threads, operationscount, and recordscount.
  - question: Is there an alternative to YCSB for testing MongoDB performance in this path?
    answer: >-
      Yes. The MongoDB performance test tool is an open source Java application that measures
      latency and throughput across operations like Inserts, Updates, Deletes, Counts, and Finds.
      To use it, install the appropriate OpenJDK run-time environment.
# END generated_summary_faq

author: Pareena Verma

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to learn how to deploy and measure MongoDB performance on Arm servers.

description: Install MongoDB on Arm servers and benchmark database performance using Yahoo Cloud Serving Benchmark (YCSB) to compare against other architectures.

learning_objectives:
- Install and run MongoDB on an Arm server
- Test MongoDB performance using open-source tooling
- Measure and compare the performance of MongoDB on Arm versus other architectures with Yahoo Cloud Serving Benchmark (YCSB)

prerequisites:
- An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider.

armips:
- Neoverse

operatingsystems:
- Linux

layout: learningpathall
learning_path_main_page: 'yes'
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
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

