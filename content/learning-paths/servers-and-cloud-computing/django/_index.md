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
    - One of either an [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider, an on-premises Arm server, or a Linux virtual machine on your Arm device
    - Sudo access to install dependencies and to modify system configuration files
    - Familiarity with SSH and Linux terminal, and basic system administration tasks
    - Both [NGINX](/learning-paths/servers-and-cloud-computing/nginx/) and [PostgreSQL](/learning-paths/servers-and-cloud-computing/postgresql/) installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:51:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c316c81de911ecd7f8e517f4ae5e5006d66a637199b8952fe195a74f3456a5e0
  summary_generated_at: '2026-07-27T18:51:37Z'
  summary_source_hash: c316c81de911ecd7f8e517f4ae5e5006d66a637199b8952fe195a74f3456a5e0
  faq_generated_at: '2026-07-27T18:51:37Z'
  faq_source_hash: c316c81de911ecd7f8e517f4ae5e5006d66a637199b8952fe195a74f3456a5e0
  summary: >-
    You'll create a minimal Django project on an Arm-based Linux machine and prepare it for deployment
    with PostgreSQL and NGINX. You'll initialize the project, verify the development server, and configure
    the PostgreSQL backend and matching database user. Then, you'll connect the application to NGINX. By the
    end, you'll have a working Django application backed by PostgreSQL and deployed on Ubuntu 22.04 LTS.
  faqs:
  - question: Which Linux distribution do the steps assume?
    answer: >-
      The steps use Ubuntu 22.04 LTS. Follow the same instructions whether you connect to a remote
      Arm server over SSH or use a local Arm VM or machine.
  - question: What files should I see after running `django-admin startproject myproject`?
    answer: >-
      Expect a `myproject` directory containing `manage.py` and a `myproject` package with
      `__init__.py`, `asgi.py`, `settings.py`, `urls.py`, and `wsgi.py`. The structure matches the tree shown in the
      steps.
  - question: Which DATABASES settings do I need to change for PostgreSQL?
    answer: >-
      Set `ENGINE` to `django.db.backends.postgresql` and provide `NAME`, `USER`, `PASSWORD`, `HOST`, and
      `PORT`. Use `localhost` or your machine’s IP address for `HOST` and keep `PORT` as `5432` unless configured
      otherwise.
  - question: How do I create the PostgreSQL database and user to match my Django settings?
    answer: >-
      Open the PostgreSQL prompt with `sudo -u postgres psql`, then create the database and user
      using the same values you set in `settings.py`. Ensure the user has the required password
      and access to the specified database.
  - question: When should I configure NGINX in this workflow?
    answer: >-
      Configure NGINX after confirming the Django project runs and the PostgreSQL connection works.
      Proceed to the deployment steps to integrate NGINX with the application.
# END generated_summary_faq

author: Diego Russo

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
