---
title: Deploy NGINX on Arm

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for engineers who want to use NGINX on Arm.

learning_objectives:
    - Install and run NGINX on Arm servers.
    - Set up NGINX as a web server, reverse proxy, or an API Gateway.
    - Verify NGINX is working correctly.

prerequisites:
    - At least one [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider, or one on-premises Arm server, to create a file server
    - At least three Arm based instances from a cloud service provider, or at least three on-premises Arm servers, to create a reverse proxy or API gateway
    - Network settings (firewalls and security groups) which allow communication on port 22 (SSH) and port 443 (HTTPS)

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
    You'll deploy NGINX on Arm-based Linux servers and progress from a package installation to a working
    web-service configuration. First, you'll install NGINX from a package and inspect the packaged build options that you can use to compile
    NGINX from source when you need a custom build. You'll then configure an HTTPS static file server,
    create its key and certificate, and verify file delivery. Finally, you'll configure a third node
    as a reverse proxy and API gateway for two upstream servers.
  faqs:
  - question: How do I know which NGINX features are enabled in the packaged install?
    answer: >-
      Run `nginx -V` to inspect your packaged build. You can see the NGINX and OpenSSL
      versions, compiler flags, module options, and configured paths in the output.
  - question: Do I need to build NGINX from source?
    answer: >-
      You can install NGINX with a package manager. If you choose a source build,
      use the packaged build options as a starting point and enable the features you need.
  - question: What do I need before setting up the reverse proxy and API gateway?
    answer: >-
      Set up two file servers and prepare a third node for the reverse
      proxy and API gateway. Ensure network settings allow communication on ports 22 (SSH) and 443
      (HTTPS).
  - question: How do I verify that the static HTTPS file server is working?
    answer: >-
      Run `wget --no-check-certificate https://localhost/file.txt` on your server, then
      `wget --no-check-certificate https://<ip_or_dns>/file.txt` from another node.
      You can also check the index page with `curl -k https://<ip_or_dns>/index.html`.
      Use these certificate-check bypasses only for the self-signed certificate demo;
      for production, use a certificate issued by a certificate authority.
  - question: What result should I expect after configuring the reverse proxy and API gateway?
    answer: >-
      You should retrieve `file.txt` through the reverse proxy and `apigw_file.txt` through
      `/api_old/apigw_file.txt`. Your API gateway rewrites `/api_old/` to `/api_new/`
      before forwarding the request upstream. Verify retrieval with the demonstrated `wget`
      commands on the proxy node and another node.
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
