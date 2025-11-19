---
title: Deploy TensorFlow on Google Cloud C4A (Arm-based Axion VMs)

draft: true
cascade:
    draft: true
    
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers deploying and optimizing TensorFlow workloads on Arm64 Linux environments, specifically using Google Cloud C4A virtual machines powered by Axion processors. 

learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install TensorFlow on a SUSE Arm64 (C4A) instance
  - Verify TensorFlow by running basic computation and model training tests on Arm64  
  - Benchmark TensorFlow using tf.keras to evaluate inference speed and model performance on Arm64 systems.

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled  
  - Basic familiarity with [TensorFlow](https://www.tensorflow.org/)

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers: Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - TensorFlow
  - Python
  - Keras

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Google Cloud documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: TensorFlow documentation
      link: https://www.tensorflow.org/learn
      type: documentation
  
  - resource:
      title: Phoronix Test Suite (PTS) documentation
      link: https://www.phoronix-test-suite.com/
      type: documentation   

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
