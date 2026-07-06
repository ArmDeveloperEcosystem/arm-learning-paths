---
title: Tune NGINX performance on Arm-based platforms
description: Learn how to tune NGINX, Linux network settings, and supporting libraries to improve web server, reverse proxy, and API gateway performance on Arm-based platforms.

minutes_to_complete: 60

who_is_this_for: This Learning Path is for software developers and system administrators who want to optimize NGINX performance on Arm-based platforms.

learning_objectives:
    - Configure Linux network settings that affect NGINX connection handling.
    - Tune NGINX directives for static file server, reverse proxy, and API gateway workloads.
    - Evaluate compiler, OpenSSL, PCRE, and zlib choices that can affect NGINX performance.
    - Measure NGINX performance before and after tuning.

prerequisites:
    - A cloud or bare-metal installation of an NGINX file server, reverse proxy, or API gateway.
    - A repeatable HTTP workload or load test that you can run before and after tuning.
    - If you don't already have an NGINX setup, see [Learn how to deploy NGINX](/learning-paths/servers-and-cloud-computing/nginx/).

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T15:49:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 39f9323dac9bd7f5480e501ad8fd93d2d9999c420ed1c2eb45eba2ccb3be63ad
  summary_generated_at: '2026-06-30T15:49:37Z'
  summary_source_hash: 39f9323dac9bd7f5480e501ad8fd93d2d9999c420ed1c2eb45eba2ccb3be63ad
  faq_generated_at: '2026-06-30T15:49:37Z'
  faq_source_hash: 39f9323dac9bd7f5480e501ad8fd93d2d9999c420ed1c2eb45eba2ccb3be63ad
  summary: >-
    You'll learn how to tune NGINX on Arm-based platforms using a measurement-first
    workflow. Using a baseline, you'll iteratively adjust Linux network stack parameters and
    evaluate compiler and library choices such as OpenSSL, PCRE, and zlib. You'll review tuned configuration examples and guidance for sizing directives to refine configurations
    for static file serving, reverse proxy, and API gateway scenarios. You'll also learn about `wrk`
    as an option for generating traffic and reporting throughput and latency on NGINX. By the end, you'll use `wrk` to compare before-and-after results and verify the impact of each tuning change.
  faqs:
  - question: How do I know whether a tuning change improved performance?
    answer: >-
      Re-run the same repeatable workload and compare throughput and latency before and after
      the change. Adjust one parameter at a time or use a designed experiment so results are attributable
      to specific settings.
  - question: Where do I change Linux network parameters when tuning?
    answer: >-
      Modify settings in /etc/sysctl.conf or use the sysctl command. Refer to the Linux kernel
      sysctl documentation, and treat these changes as part of the same measurement process used
      for NGINX directives.
  - question: Do I need to use wrk if I already have a load test?
    answer: >-
      No. If you already have a repeatable HTTP workload, use that. wrk is provided as a starting point
      only when you don't already have an established test method.
  - question: When tuning the reverse proxy or API gateway, what should I reuse from the static
      file server configuration?
    answer: >-
      Use the same top-level nginx.conf from the static file server section. Then apply the tuned
      reverse proxy and API gateway configuration and validate the result with repeatable measurements.
  - question: How do compiler, OpenSSL, PCRE, and zlib choices factor into tuning?
    answer: >-
      Evaluate these choices as part of your experiments because they can affect NGINX performance.
      Compare alternatives using the same workload and interpret results alongside your NGINX
      and kernel changes.
# END generated_summary_faq

author: Julio Suarez

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Web
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
tools_software_languages:
    - NGINX
    - Runbook

operatingsystems:
    - Linux

test_images:
    - ubuntu:latest
test_link: null
test_maintenance: true

further_reading:
    - resource:
        title: NGINX documentation
        link: https://nginx.org/en/docs/
        type: documentation
    - resource:
        title: NGINX directive index
        link: https://nginx.org/en/docs/dirindex.html
        type: documentation
    - resource:
        title: NGINX variable index
        link: https://nginx.org/en/docs/varindex.html
        type: documentation
    - resource:
        title: NGINX Admin Guide
        link: https://docs.nginx.com/nginx/admin-guide/
        type: documentation
    - resource:
        title: h2load HOW-TO
        link: https://nghttp2.org/documentation/h2load-howto.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

