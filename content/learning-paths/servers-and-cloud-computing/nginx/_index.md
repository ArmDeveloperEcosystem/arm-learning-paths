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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:39:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c5e077458808373c8ce9660235716b5bb55e4e7eb8b6300c162c041ef1c96cb0
  summary_generated_at: '2026-06-02T04:36:50Z'
  summary_source_hash: c5e077458808373c8ce9660235716b5bb55e4e7eb8b6300c162c041ef1c96cb0
  faq_generated_at: '2026-06-03T01:39:16Z'
  faq_source_hash: c5e077458808373c8ce9660235716b5bb55e4e7eb8b6300c162c041ef1c96cb0
  summary: >-
    Deploy the open source Nginx on Arm-based Linux servers and configure it as a minimal HTTPS
    static file server and as a reverse proxy and API gateway. You will first install Nginx using
    a package manager and review its build configuration, then optionally build Nginx from source
    with the features you need. Next, you will create a key and certificate, add a basic Nginx
    configuration, and start the server. Finally, you will set up a third node to act as a reverse
    proxy and API gateway that load balances across two upstream file servers. Prerequisites include
    Arm-based instances (AWS, Microsoft Azure, Google Cloud, or Oracle) or on-prem Arm servers,
    and network access on ports 22 and 443. No other explicit prerequisites are listed.
  faqs:
  - question: Which Nginx edition does this path use?
    answer: >-
      The path uses the open source version of Nginx. Nginx Plus is mentioned for context but
      is not used here.
  - question: How many Arm-based instances do I need to complete the exercises?
    answer: >-
      You need at least one instance to create a static file server. For the reverse proxy and
      API gateway, you need at least three instances: two file servers and one reverse proxy/API
      gateway node.
  - question: Should I install Nginx from a package manager or build from source?
    answer: >-
      The path covers both approaches. It recommends inspecting the build configuration of a prebuilt
      package first to inform which features you enable when compiling from source.
  - question: What network settings should I configure before starting?
    answer: >-
      Ensure your firewalls and security groups allow communication on port 22 (SSH) and port
      443 (HTTPS). These are required for access and for serving HTTPS.
  - question: What should be ready before configuring the reverse proxy and API gateway?
    answer: >-
      Set up two static file servers using the earlier section. The third node will run the reverse
      proxy/API gateway and load balance across the two upstream file servers.
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

