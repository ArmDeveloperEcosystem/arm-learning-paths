---
title: Learn how to deploy a Django application

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
