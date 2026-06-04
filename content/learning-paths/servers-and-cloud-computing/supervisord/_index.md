---
title: Access running containers using Supervisor, SSH, and Remote.It

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers who want to learn how to run multiple services in a container and access running containers using Supervisor, SSH, and Remote.It during the debug and test phases of a project.

learning_objectives:
    - Use Supervisor to run multiple services in a container
    - Access a container running in AWS Fargate without changing the security group for debug and test

prerequisites:
    - An Arm Linux computer running Docker
    - An AWS account
    - A Remote.It account

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:08:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d3fa3b409ed7cf2ecb521fa4d19af8411718909881861ef3885214824031b541
  summary_generated_at: '2026-06-02T05:13:51Z'
  summary_source_hash: d3fa3b409ed7cf2ecb521fa4d19af8411718909881861ef3885214824031b541
  faq_generated_at: '2026-06-03T02:08:16Z'
  faq_source_hash: d3fa3b409ed7cf2ecb521fa4d19af8411718909881861ef3885214824031b541
  summary: >-
    Learn how to run multiple services in a single container with Supervisor and access that container
    for debugging and testing without opening SSH ports or changing AWS security groups. You will
    update a Dockerfile to add Supervisor, enable SSH, and install and configure Remote.It, then
    build and run the container on an Arm Linux system using Docker. The path then demonstrates
    launching the container on AWS ECS with a Fargate launch type using the AWS Copilot CLI and
    connecting to it through Remote.It. Prerequisites are an Arm Linux computer running Docker,
    an AWS account, and a Remote.It account. After completing the steps, you can reach running
    containers for debug and test using Supervisor and Remote.It.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm Linux computer running Docker, an AWS account, and a Remote.It account.
      No additional prerequisites are explicitly listed.
  - question: Which changes should I make in the Dockerfile to run multiple services and enable
      access?
    answer: >-
      Install and configure Supervisor, OpenSSH (with password login), and Remote.It, and add
      a Supervisor configuration file. The example uses Ubuntu 24.04 and also installs common
      debug/test utilities.
  - question: How do I access a container running in AWS Fargate without changing security groups?
    answer: >-
      Use the AWS Copilot CLI to launch the container on AWS ECS with Fargate, then connect to
      it using Remote.It. This avoids opening any port for SSH access.
  - question: How do I know the container is ready to accept SSH via Remote.It?
    answer: >-
      After building and running the image with the provided Supervisor configuration, both the
      SSH daemon and Remote.It should start in the container. You should be able to initiate a
      Remote.It session and open an SSH shell.
  - question: Can I adapt this approach to other container runtimes besides AWS Fargate?
    answer: >-
      Yes. The example demonstrates AWS ECS with Fargate, but you can adapt the technique to any
      container runtime environment.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
armips:
    - Neoverse 
    - Cortex-A
operatingsystems:
    - Linux 
tools_software_languages:
    - Docker
    - Remote.It
    - Supervisor
    
further_reading:
    - resource:
        title: Run multiple processes in a container
        link: https://docs.docker.com/config/containers/multi-service_container/
        type: documentation
    - resource:
        title: Supervisor with Docker Lessons learned
        link: https://advancedweb.hu/supervisor-with-docker-lessons-learned/
        type: blog
    - resource:
        title: Multiple services in a Docker container with supervisord
        link: https://dev.to/pratapkute/multiple-services-in-a-docker-container-with-supervisord-2g13
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

