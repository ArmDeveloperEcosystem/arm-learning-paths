---
title: Learn how to tune Nginx

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers who want to use Nginx on Arm.

learning_objectives:
    - Describe how kernel parameters can impact Nginx performance.
    - Describe how compilers and libraries can impact Nginx performance.
    - Tune a Nginx file server configuration file.
    - Tune a Nginx Reverse Proxy and API Gateway configuration file.
    - Describe how to test Nginx performance.

prerequisites:
    - A cloud or bare-metal installation of a Nginx file server or load balancer.
    - If you do not already have a Nginx setup, a review of [Learn how to deploy Nginx](/learning-paths/servers-and-cloud-computing/nginx/).

generate_summary_faq: false
rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:40:13Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 10f13dee3459577fcadf5966cf80d990f3396321189f638432a3308699e773a8
  summary_generated_at: '2026-06-02T04:38:02Z'
  summary_source_hash: 10f13dee3459577fcadf5966cf80d990f3396321189f638432a3308699e773a8
  faq_generated_at: '2026-06-03T01:40:13Z'
  faq_source_hash: 10f13dee3459577fcadf5966cf80d990f3396321189f638432a3308699e773a8
  summary: >-
    This advanced Learning Path shows how to tune Nginx on Arm-based Linux servers in about 60
    minutes. You will review how Linux kernel parameters, compiler and library choices, and Nginx
    configuration affect performance. The steps walk through tuned examples for a static file
    server (/etc/nginx/nginx.conf) and a Reverse Proxy/API Gateway (/etc/nginx/conf.d/loadbalancer.conf),
    and present a practical method to test changes using wrk2. A cloud or bare-metal Nginx file
    server or load balancer is required to follow along; if you do not already have one, first
    review Learn how to deploy Nginx. By the end, you will be able to apply workload-aware tuning
    and validate the impact with targeted load testing.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a cloud or bare-metal installation of an Nginx file server or load balancer on
      Linux. If you do not already have a setup, review the “Learn how to deploy Nginx” Learning
      Path first.
  - question: How do I list and change the Linux kernel networking parameters mentioned in the
      tuning guidance?
    answer: >-
      Run sudo sysctl -a to list kernel parameters. You can change values in /etc/sysctl.conf
      or apply them using the sysctl command; see the Linux source admin-guide and networking
      documentation for parameter details.
  - question: Which Nginx configuration files will I tune?
    answer: >-
      You will work with the top-level /etc/nginx/nginx.conf and, for Reverse Proxy and API Gateway
      use cases, /etc/nginx/conf.d/loadbalancer.conf. The Learning Path focuses on performance-relevant
      directives in these files.
  - question: Do I have to use wrk2 for performance testing?
    answer: >-
      No. If you already have a performance test methodology for your deployment, you can skip
      the wrk2 section; otherwise, the path shows how wrk2 is typically used for testing Nginx
      at Arm.
  - question: What result should I expect after tuning, and how do I validate it?
    answer: >-
      There is no single recommended setting set; outcomes depend on your workload and use case.
      Validate by measuring before and after with your test methodology (or wrk2) and compare
      results for your specific scenario.
# END generated_summary_faq

author: Julio Suarez

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

further_reading:
    - resource:
        title: Nginx Documentation
        link: https://nginx.org/en/docs/
        type: documentation
    - resource:
        title: Nginx Admin Guide
        link: https://docs.nginx.com/nginx/admin-guide/
        type: documentation
    


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

