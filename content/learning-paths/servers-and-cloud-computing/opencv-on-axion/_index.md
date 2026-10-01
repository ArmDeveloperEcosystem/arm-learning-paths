---
title: Build computer vision pipelines with OpenCV on a Google Cloud C4A Axion VM
description: Deploy and run OpenCV-based computer vision pipelines on Google Cloud Axion C4A Arm-based VMs, covering image processing, video pipelines, browser-based visualization, and integration with machine learning models.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for DevOps engineers, software developers, and AI practitioners who want to build and run computer vision pipelines on SUSE Linux Enterprise Server (SLES) Arm64 using OpenCV, process images and videos, visualize outputs in real time, and integrate ML models.

learning_objectives:
    - Install and configure OpenCV on Google Cloud C4A Axion Arm64 instances
    - Build image processing pipelines using OpenCV
    - Develop video processing pipelines with real-time frame updates
    - Visualize OpenCV outputs in the browser using an HTTP server
    - Integrate OpenCV pipelines with machine learning models 

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Python and Linux command line
  - Understanding of basic image/video processing concepts

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:42:48Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6382d70b3cd7040b984083cffee014bd2377ba150508b818e393263542a56333
  summary_generated_at: '2026-10-01T19:42:48Z'
  summary_source_hash: 6382d70b3cd7040b984083cffee014bd2377ba150508b818e393263542a56333
  faq_generated_at: '2026-10-01T19:42:48Z'
  faq_source_hash: 6382d70b3cd7040b984083cffee014bd2377ba150508b818e393263542a56333
  summary: >-
    Build browser-based computer-vision pipelines with OpenCV on a Google Cloud C4A Axion virtual
    machine. You provision a SUSE Linux VM, open port 8000, and prepare a Python 3.11 virtual
    environment. You then create image and video pipelines that process frames and serve updated
    output through an HTTP server. Finally, you add a machine learning model, stream its visual
    predictions, and validate the output from the VM's external IP address.
  faqs:
  - question: Which C4A machine type should I create for the VM?
    answer: >-
      Use the `c4a-standard-4` machine type with four vCPUs and 16 GB of memory. This instance runs
      the OpenCV application used throughout the workflow.
  - question: Which port do I open for the browser view, and how do I check that it works?
    answer: >-
      Open TCP port 8000 with a VPC firewall rule. After you start the project's HTTP server,
      visit `http://EXTERNAL_IP:8000`; a page that loads confirms the rule and service are configured.
  - question: What Python version do I need during setup?
    answer: >-
      Install Python 3.11. You also install development tools with zypper to support building
      OpenCV’s pip package.
  - question: Where are the project files and virtual environment created?
    answer: >-
      Use the `~/opencv-project` directory and a virtual environment named `cv-env`. Run subsequent
      scripts from that directory with the environment activated.
  - question: What should be ready before I integrate the machine learning model?
    answer: >-
      Have a running Google Axion Arm-based VM with SUSE Linux, Python 3.11, the `~/opencv-project`
      directory with the `cv-env` environment and OpenCV, and port 8000 open in the firewall.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: ML
platforms:
  - Google Axion

armips:
  - Neoverse

tools_software_languages:
  - OpenCV
  - Python
  - NumPy
  - Flask

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================

further_reading:
  - resource:
      title: OpenCV official documentation
      link: https://docs.opencv.org/
      type: documentation

  - resource:
      title: OpenCV GitHub repository
      link: https://github.com/opencv/opencv
      type: documentation

  - resource:
      title: NumPy documentation
      link: https://numpy.org/doc/
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: yes
---
