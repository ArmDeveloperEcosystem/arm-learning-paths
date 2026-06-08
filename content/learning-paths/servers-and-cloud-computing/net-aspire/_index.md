---
title: Run a .NET Aspire application on Arm-based VMs on AWS and GCP

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers interested in learning how to deploy .NET Aspire applications on Arm-based virtual machines (VMs) on Amazon Web Services (AWS) and Google Cloud Platform (GCP).

learning_objectives: 
    - Demonstrate knowledge and understanding of .NET Aspire developer tools.
    - Create a .NET Aspire application.
    - Modify code on a Windows on Arm development machine.
    - Deploy a .NET Aspire application to Arm-powered virtual machines in the Cloud.
prerequisites:
    - A Windows on Arm machine, for example the Lenovo Thinkpad X13s running Windows 11 to build the .NET Aspire project.    
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from AWS or GCP.
    - Any code editor. [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user) is an example of a suitable editor.    

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:38:53Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5a5fd9b66a09de71009ccb098c7ef08a848463a8a7956643020ab1fb1db22fbb
  summary_generated_at: '2026-06-02T04:36:04Z'
  summary_source_hash: 5a5fd9b66a09de71009ccb098c7ef08a848463a8a7956643020ab1fb1db22fbb
  faq_generated_at: '2026-06-03T01:38:53Z'
  faq_source_hash: 5a5fd9b66a09de71009ccb098c7ef08a848463a8a7956643020ab1fb1db22fbb
  summary: >-
    This introductory Learning Path guides you through creating, running, modifying, and deploying
    a .NET Aspire application using a Windows on Arm development machine and Arm-based virtual
    machines on AWS and Google Cloud. You will verify .NET 8.0 or later, install the Aspire workload,
    generate and run the project (including trusting the HTTPS development certificate and using
    the Aspire dashboard), and add a computation service to simulate intensive work. The path
    then shows how to deploy to an Arm-powered EC2 instance, such as AWS Graviton; Google Cloud
    Arm-based VMs are also targeted. Prerequisites include a Windows on Arm device, an Arm-based
    instance from AWS or GCP, and a code editor (for example, Visual Studio Code for Arm64).
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Windows on Arm machine (for example, a Lenovo ThinkPad X13s running Windows 11),
      access to an Arm-based instance on AWS or GCP, and a code editor. Visual Studio Code for
      Arm64 is an example of a suitable editor.
  - question: How do I check my .NET version and install the Aspire workload?
    answer: >-
      Open a PowerShell terminal and run dotnet --version to confirm .NET 8.0 or later is installed.
      Then install the Aspire workload with dotnet workload install aspire and wait for the download
      and installation to complete without errors.
  - question: How do I run the application locally and confirm it started correctly?
    answer: >-
      First trust the HTTPS development certificate by running dotnet dev-certs https --trust.
      Then change into the project directory and run dotnet run --project NetAspire.Arm.AppHost;
      you should see build output, an Aspire version line, and messages such as “Distributed application
      starting.”
  - question: Where do I add the computational code, and what does it do?
    answer: >-
      Add a new file named ComputationService.cs in the NetAspire.Arm.ApiService project. The
      provided code performs matrix multiplication to mimic computationally intensive work.
  - question: Which cloud targets are supported, and how do I begin with AWS?
    answer: >-
      The path targets Arm-based VMs on AWS and Google Cloud. For AWS, sign in to the AWS Management
      Console, navigate to the EC2 service, and choose an Arm-powered instance type such as those
      based on AWS Graviton.
# END generated_summary_faq

author: Dawid Borycki

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - AWS
  - Google Cloud

armips:
    - Neoverse
    
tools_software_languages:
    - .NET
    - C# 
    - Visual Studio Code

operatingsystems:
    - Windows
    - Linux


further_reading:
    - resource:
        title: .NET Aspire Overview
        link: https://learn.microsoft.com/en-us/dotnet/aspire/get-started/aspire-overview
        type: Documentation
    - resource:
        title: Compute Service - Amazon EC2
        link: https://aws.amazon.com/pm/ec2
        type: Documentation
    - resource:
        title: Compute Service - Google GCP
        link: https://cloud.google.com/products/compute/
        type: Documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

