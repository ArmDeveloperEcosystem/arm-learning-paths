---
title: Create and verify C2PA Content Credentials on Arm

draft: true
cascade:
    draft: true

description: Understand why digital media needs verifiable provenance. Add Content Credentials to an image on an Arm device. Inspect its C2PA manifest. Validate it with an external validator. Observe a content-binding validation failure after a controlled change to the image.

minutes_to_complete: 55

who_is_this_for: This is an introductory topic for developers who want to add and validate C2PA Content Credentials on Arm devices.

learning_objectives:
    - Explain what C2PA is, the content provenance problem it addresses, and why provenance matters.
    - Add Content Credentials to a sample image on an Arm device.
    - Inspect the manifest and interpret the content-binding, signature, and trust results.
    - Validate Content Credentials with an external validator.
    - Demonstrate a content-binding failure after a controlled change to the image.

prerequisites:
    - "The current stable release of [C2PA Tool](/install-guides/c2patool/) installed on your Arm device"
    - "[ExifTool](/install-guides/exiftool/) installed on your Arm device"
    - "[libjpeg-turbo](/install-guides/libjpeg-turbo/) installed on your Arm device"
    - Familiarity with running command-line tools

author:
    - Kostiantyn Perehuda
    - Yogesh Deshpande

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Security
armips:
    - Cortex-A
tools_software_languages:
    - Content Credentials
    - C2PA Tool
    - ExifTool
    - libjpeg-turbo
operatingsystems:
    - Linux
    - macOS
    - Windows

further_reading:
    - resource:
        title: C2PA technical specification
        link: https://c2pa.org/specifications/
        type: documentation
    - resource:
        title: C2PA Tool source repository
        link: https://github.com/contentauth/c2patool
        type: repository

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
