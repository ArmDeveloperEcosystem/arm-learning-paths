---
title: Learn how to deploy Nginx

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for engineers who want to use Nginx on Arm.

learning_objectives:
    - Install and run Nginx on Arm servers
    - Set up Nginx as a web server, reverse proxy, or an API Gateway
    - Verify Nginx is working correctly

prerequisites:
    - To create a file server you will need at least one [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or one on-premises Arm server.
    - To create a reverse proxy or API gateway you will need at least three Arm based instances from a cloud service provider or at least three on-premises Arm servers.
    - Network settings (firewalls and security groups) which allow communication on port 22 (SSH) and port 443 (HTTPS).

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:18Z'
  generator: template
  source_hash: c5e077458808373c8ce9660235716b5bb55e4e7eb8b6300c162c041ef1c96cb0
  summary: >-
    Learn how to deploy Nginx walks you through an end-to-end Arm software workflow. It is designed
    for engineers who want to use Nginx on Arm. By the end, you will be able to install and run
    Nginx on Arm servers, set up Nginx as a web server, reverse proxy, or an API Gateway, and
    verify Nginx is working correctly. It focuses on tools and technologies such as NGINX, Linux
    environments, Arm platforms including Neoverse, and cloud platforms such as AWS, Microsoft
    Azure, Google Cloud, and Oracle. The main steps cover Install Nginx using a package manager
    and check the build configuration, Build Nginx from source, Setup a static file server, and
    Setup a reverse proxy and API gateway.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will install and run Nginx on Arm servers, set up Nginx as a web server, reverse proxy,
      or an API Gateway, and verify Nginx is working correctly.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for engineers who want to use Nginx on Arm.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: To create a file server you will need
      at least one [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from
      a cloud service provider or one on-premises Arm server.; To create a reverse proxy or API
      gateway you will need at least three Arm based instances from a cloud service provider or
      at least three on-premises Arm servers.; Network settings (firewalls and security groups)
      which allow communication on port 22 (SSH) and port 443 (HTTPS).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including NGINX, Linux environments, Arm platforms such as
      Neoverse, and cloud platforms such as AWS, Microsoft Azure, Google Cloud, and Oracle.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Install Nginx using a package manager and check the
      build configuration, Build Nginx from source, Setup a static file server, and Setup a reverse
      proxy and API gateway.
# END generated_summary_faq

author: Julio Suarez

### Tags
skilllevels: Introductory
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
operatingsystems:
    - Linux

test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true

further_reading:
    - resource:
        title: Guidelines for Deploying Nginx Plus on Amazon Web Services
        link: https://armkeil.blob.core.windows.net/developer/Files/pdf/white-paper/guidelines-for-deploying-nginx-plus-on-aws.pdf
        type: documentation
    - resource:
        title: Optimize Your Nginx Plus Deployment with Arm-Based Amazon EC2 M6g Instances
        link: https://www.nginx.com/blog/optimize-nginx-plus-deployment-arm-based-amazon-ec2-m6g-instances/
        type: blog
    - resource:
        title: Deploying NGINX as an API Gateway
        link: https://www.nginx.com/blog/deploying-nginx-plus-as-an-api-gateway-part-1/
        type: blog


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

