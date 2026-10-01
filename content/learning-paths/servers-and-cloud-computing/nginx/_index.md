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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:40:11Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 877a608fc16135d4bcfc1ce710fb257fcea3ec3af75052841a3182bd024f8384
  summary_generated_at: '2026-10-01T19:40:11Z'
  summary_source_hash: 877a608fc16135d4bcfc1ce710fb257fcea3ec3af75052841a3182bd024f8384
  faq_generated_at: '2026-10-01T19:40:11Z'
  faq_source_hash: 877a608fc16135d4bcfc1ce710fb257fcea3ec3af75052841a3182bd024f8384
  summary: >-
    Deploy nginx on Arm-based Linux servers and progress from a package installation to a working
    web-service configuration. You inspect the packaged build options and use them to compile
    nginx from source when you need a custom build. You then configure an HTTPS static file server,
    create its key and certificate, and verify file delivery. Finally, you configure a third node
    as a reverse proxy and API gateway for two upstream servers.
  faqs:
  - question: How do I know which nginx features are enabled in the packaged install?
    answer: >-
      Review the packaged build configuration to see which modules and paths are compiled in.
      Use this information to decide which options to enable if you later build from source.
  - question: Do I need to build nginx from source?
    answer: >-
      No. You start with a package install and only build from source if you need a different
      configuration. Looking at the prebuilt configuration first helps you choose the right source
      build options.
  - question: What do I need in place before setting up the reverse proxy and API gateway?
    answer: >-
      Set up two file servers using the previous section, and prepare a third node for the reverse
      proxy/API gateway. Ensure network settings allow communication on ports 22 (SSH) and 443
      (HTTPS).
  - question: How do I verify the static HTTPS file server is working?
    answer: >-
      After configuring nginx, creating a key and certificate, and starting the service, access
      a test file over HTTPS from a client. Successful retrieval confirms the setup; if it fails,
      review your configuration and the nginx documentation on serving static content.
  - question: What result should I expect after configuring the reverse proxy/API gateway?
    answer: >-
      The reverse proxy/API gateway forwards requests to the two upstream file servers and load
      balances across them. During testing, you should observe responses originating from both
      backends; see the nginx reverse proxy documentation for configuration details.
# END generated_summary_faq

author: Julio Suarez

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Web
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
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
