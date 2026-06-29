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
    - If you do not already have an NGINX setup, review [Learn how to deploy NGINX](/learning-paths/servers-and-cloud-computing/nginx/).

author: Julio Suarez

generate_summary_faq: true
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
