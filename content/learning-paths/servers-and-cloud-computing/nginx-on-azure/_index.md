---
title: Deploy NGINX on Azure Cobalt 100 Arm-based virtual machines 

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic for system administrators and developers who want to learn how to deploy and benchmark NGINX on Microsoft Azure Cobalt 100 Arm-based instances.

learning_objectives: 
    - Create an Arm64 virtual machine (VM) on Azure Cobalt 100 (Dpsv6) using the Azure console with Ubuntu Pro 24.04 LTS as the base image.
    - Install and configure the NGINX web server on the Azure Arm64 VM.
    - Configure and test a static website with NGINX on the VM.
    - Run baseline NGINX performance tests with ApacheBench (ab).

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100-based instances (Dpsv6)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:39:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f556dee0540494860c18e38f186e7a602db0635cded4fd4c6cbb649e115ef294
  summary_generated_at: '2026-10-01T19:39:38Z'
  summary_source_hash: f556dee0540494860c18e38f186e7a602db0635cded4fd4c6cbb649e115ef294
  faq_generated_at: '2026-10-01T19:39:38Z'
  faq_source_hash: f556dee0540494860c18e38f186e7a602db0635cded4fd4c6cbb649e115ef294
  summary: >-
    You'll deploy NGINX on an Arm-based Microsoft Azure VM powered by Cobalt 100, and capture a baseline
    benchmark. First, you'll create an Ubuntu Pro 24.04 LTS Dpsv6 VM in the Azure portal, install NGINX,
    and verify its default page. You'll then configure a static site and confirm that NGINX serves
    your content. Finally, you'll install ApacheBench and record initial throughput and timing results.
  faqs:
  - question: Which Azure VM size and image should I choose?
    answer: >-
      Use an Arm-based VM in the Dpsv6 series with the Ubuntu Pro 24.04 LTS Arm64 image.
  - question: How do I know that NGINX installed correctly before I change any configuration?
    answer: >-
      Run `sudo systemctl status nginx` and check for `Active: active (running)`.
      Use `curl -I http://localhost/` to check for `HTTP/1.1 200 OK`. Then, open
      your VM's public IP address in a browser to confirm that you see the default welcome page.
  - question: Where should I put my static site files, and what should I expect when it works?
    answer: >-
      Create `/var/www/my-static-site/index.html` and configure `/etc/nginx/conf.d/static-site.conf`
      to use that directory and `index.html`. Disable the packaged default site with
      `sudo unlink /etc/nginx/sites-enabled/default`. Run `sudo nginx -t` before
      `sudo nginx -s reload`, then open your VM's public IP address to check your custom page.
  - question: Should I run ApacheBench on the VM or from another machine?
    answer: >-
      Run ApacheBench on your NGINX VM to match the demonstrated baseline test.
      Use `ab -n 1000 -c 50 http://localhost/` to send 1,000 requests with 50 concurrent connections.
  - question: Which package installs ApacheBench on Ubuntu Pro 24.04 LTS, and how do I verify it?
    answer: >-
      Install the `apache2-utils` package. Run `ab -V` to confirm that ApacheBench is available and
      prints a version string.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Web
platforms:
  - Microsoft Azure Cobalt

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
