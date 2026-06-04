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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:39:34Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e6f6f4d843b4974d1c1d67a35009b4428d08bb356d26c08a441f82726e002fb2
  summary_generated_at: '2026-06-02T04:37:18Z'
  summary_source_hash: e6f6f4d843b4974d1c1d67a35009b4428d08bb356d26c08a441f82726e002fb2
  faq_generated_at: '2026-06-03T01:39:34Z'
  faq_source_hash: e6f6f4d843b4974d1c1d67a35009b4428d08bb356d26c08a441f82726e002fb2
  summary: >-
    This Learning Path shows how to deploy and validate NGINX on an Arm-based Microsoft Azure
    Cobalt 100 virtual machine. Using the Azure portal, you create a general-purpose Dpsv6 Arm64
    VM with Ubuntu Pro 24.04 LTS, install and enable NGINX, and replace the default page with
    a simple static site to confirm the server is working. You then install ApacheBench (ab) to
    run baseline NGINX performance tests and review the output, with a sample result from a D4ps_v6
    configuration. The path is introductory and Linux-focused, takes about 30 minutes, and is
    intended for system administrators and developers. Prerequisite: an Azure account with access
    to Cobalt 100 (Dpsv6) instances.
  faqs:
  - question: What do I need before I start creating the VM on Azure?
    answer: >-
      You need a Microsoft Azure account with access to Cobalt 100 based instances (Dpsv6). This
      access is required to select the Arm64 Cobalt 100 VM used in the steps.
  - question: Which Azure VM series and OS image should I select?
    answer: >-
      Use a general-purpose D-series VM in the Dpsv6 size series and choose Ubuntu Pro 24.04 LTS
      as the base image for Arm64.
  - question: Can I use Azure CLI or IaC instead of the portal to create the VM?
    answer: >-
      There are multiple ways to create a Cobalt 100 VM, but this Learning Path uses the Azure
      portal. CLI and IaC workflows are not covered here.
  - question: How do I know NGINX is installed and serving content?
    answer: >-
      After installation and enabling, NGINX should serve its default welcome page. Then create
      /var/www/my-static-site with a simple HTML file to replace the default page and confirm
      it is delivered by the server.
  - question: How do I install and verify ApacheBench (ab) on Ubuntu Pro 24.04 LTS?
    answer: >-
      Install the apache2-utils package and verify the tool with ab -V. You can then run a basic
      benchmark and review the key metrics, with a sample result provided for an Azure D4ps_v6
      instance.
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

