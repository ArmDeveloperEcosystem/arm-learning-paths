---
title: Deploy NGINX on Azure Cobalt 100 Arm-based virtual machines 

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic for system administrators and developers who want to learn how to deploy and benchmark NGINX on Microsoft Azure Cobalt 100 Arm-based instances.

learning_objectives: 
    - Create an Arm64 virtual machine on Azure Cobalt 100 (Dpsv6) using the Azure console with Ubuntu Pro 24.04 LTS as the base image
    - Install and configure the NGINX web server on the Azure Arm64 virtual machine
    - Configure and test a static website with NGINX on the virtual machine
    - Run baseline NGINX performance tests with ApacheBench (ab) on Ubuntu Pro 24.04 LTS Arm64


prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:18Z'
  generator: template
  source_hash: e6f6f4d843b4974d1c1d67a35009b4428d08bb356d26c08a441f82726e002fb2
  summary: >-
    Deploy NGINX on Azure Cobalt 100 Arm-based virtual machines walks you through an end-to-end
    Arm software workflow. It is designed for system administrators and developers who want to
    learn how to deploy and benchmark NGINX on Microsoft Azure Cobalt 100 Arm-based instances.
    By the end, you will be able to create an Arm64 virtual machine on Azure Cobalt 100 (Dpsv6)
    using the Azure console with Ubuntu Pro 24.04 LTS as the base image, install and configure
    the NGINX web server on the Azure Arm64 virtual machine, and configure and test a static website
    with NGINX on the virtual machine. It focuses on tools and technologies such as NGINX and
    ApacheBench, Linux environments, Arm platforms including Neoverse, and cloud platforms such
    as Microsoft Azure. The main steps cover Overview of Azure Cobalt 100 and NGINX, Create an
    Arm-based Azure VM with Cobalt 100, Install NGINX, NGINX Baseline Testing, and NGINX Benchmarking.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will create an Arm64 virtual machine on Azure Cobalt 100 (Dpsv6) using the Azure console
      with Ubuntu Pro 24.04 LTS as the base image, install and configure the NGINX web server
      on the Azure Arm64 virtual machine, and configure and test a static website with NGINX on
      the virtual machine.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for system administrators and developers who want to learn
      how to deploy and benchmark NGINX on Microsoft Azure Cobalt 100 Arm-based instances.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Microsoft Azure](https://azure.microsoft.com/)
      account with access to Cobalt 100 based instances (Dpsv6).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including NGINX and ApacheBench, Linux environments, Arm platforms
      such as Neoverse, and cloud platforms such as Microsoft Azure.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Overview of Azure Cobalt 100 and NGINX, Create an
      Arm-based Azure VM with Cobalt 100, Install NGINX, NGINX Baseline Testing, and NGINX Benchmarking.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - NGINX
    - ApacheBench

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: NGINX official documentation
      link: https://nginx.org/en/docs/
      type: documentation
  - resource:
      title: ApacheBench official documentation
      link: https://httpd.apache.org/docs/2.4/programs/ab.html
      type: documentation
  - resource:
      title: NGINX on Azure virtual machines
      link: https://docs.nginx.com/nginx/deployment-guides/microsoft-azure/virtual-machines-for-nginx/
      type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

