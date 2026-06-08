---
title: Learn how to deploy a Django application
description: Learn how to create a simple Django web application and deploy it on Arm machines using Nginx and PostgreSQL.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for engineers who want to deploy a Django based application on Arm machines.

learning_objectives:
    - Create a simple Django application
    - Deploy the Django application using Nginx and PostgreSQL
    - Verify that the Django application is working correctly

prerequisites:
    - At least either an [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider, on-premises Arm server, or a Linux virtual machine on your Arm device.
    - Sudo access to install dependencies and to modify system configuration files.
    - Be comfortable with SSH/Linux terminal and basic system administration tasks.
    - To install both [Nginx](/learning-paths/servers-and-cloud-computing/nginx/) and [PostgreSQL](/learning-paths/servers-and-cloud-computing/postgresql/)

generate_summary_faq: false
rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:41:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c316c81de911ecd7f8e517f4ae5e5006d66a637199b8952fe195a74f3456a5e0
  summary_generated_at: '2026-06-02T03:33:56Z'
  summary_source_hash: c316c81de911ecd7f8e517f4ae5e5006d66a637199b8952fe195a74f3456a5e0
  faq_generated_at: '2026-06-03T00:41:18Z'
  faq_source_hash: c316c81de911ecd7f8e517f4ae5e5006d66a637199b8952fe195a74f3456a5e0
  summary: >-
    Build and deploy a simple Django web application on Arm-based Linux machines using Nginx and
    PostgreSQL. This introductory path uses Ubuntu 22.04 LTS and walks you through creating a
    Django project, configuring its PostgreSQL database settings, creating the database and user,
    deploying behind Nginx, and verifying the application is working. You can run the steps on
    an Arm instance from AWS, Microsoft Azure, Google Cloud, or Oracle, on an on-premises Arm
    server, or on a Linux VM on your Arm device. Prerequisites include sudo access, comfort with
    SSH and basic Linux administration, and the ability to install Nginx and PostgreSQL.
  faqs:
  - question: What environment do I need to run this?
    answer: >-
      Use an Arm-based instance from a cloud provider, an on-premises Arm server, or a Linux VM
      on your Arm device. The instructions use Ubuntu 22.04 LTS and are the same regardless of
      the Arm machine type.
  - question: Do I need a specific Python version or a virtual environment?
    answer: >-
      Ubuntu 22.04 provides Python 3.10, which you can use, or you may optionally install a newer
      Python via the Deadsnakes PPA. The steps assume you are working in a terminal with a Python
      virtual environment activated.
  - question: Do I need to install Nginx and PostgreSQL before deploying?
    answer: >-
      Yes. Installing both Nginx and PostgreSQL is listed as a prerequisite for this path. Follow
      the referenced Learning Paths for Nginx and PostgreSQL if you need installation guidance.
  - question: How do I know the Django project was created correctly?
    answer: >-
      After running django-admin startproject myproject, you should see a myproject directory
      with manage.py and a myproject package containing asgi.py, __init__.py, settings.py, urls.py,
      and wsgi.py. You can start the development server from the project directory to quickly
      validate it runs.
  - question: Which PostgreSQL settings should I use and how do I create the database?
    answer: >-
      In settings.py set ENGINE to django.db.backends.postgresql with NAME myprojectdb, USER usr,
      PASSWORD mypassword, HOST as localhost or your machine’s IP, and PORT 5432. Open the PostgreSQL
      prompt with sudo -u postgres psql and create the database and user to match those values.
# END generated_summary_faq

author: Diego Russo

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
    - Django
    - Python
    - NGINX
    - PostgreSQL
operatingsystems:
    - Linux


further_reading:
    - resource:
        title: PostgreSQL Documentation
        link: https://www.postgresql.org/docs/
        type: documentation
    - resource:
        title: Nginx Documentation
        link: https://nginx.org/en/docs/
        type: documentation
    - resource:
        title: Django Documentation
        link: https://docs.djangoproject.com/
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

