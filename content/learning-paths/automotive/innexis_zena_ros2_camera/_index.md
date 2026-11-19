---
title: Develop a ROS 2 Camera Application on Arm Zena CSS

draft: true
cascade:
    draft: true

description: Publish virtual camera frames as ROS 2 images, develop a small application, and validate a software change on Arm Zena CSS with Siemens Innexis ANA.

minutes_to_complete: 60

who_is_this_for: Robotics and automotive application developers with access to a running Arm Zena CSS virtual platform in Siemens Innexis ANA.

learning_objectives:
    - Publish frames from the Zena CSS guest camera as a standard ROS 2 image topic.
    - Check ROS 2 topic discovery, message content, and received image rate.
    - Develop an image-processing node that publishes a motion event.
    - Change the application threshold and verify the updated behavior in the virtual platform.

prerequisites:
    - A running Zena CSS virtual platform in Siemens Innexis ANA with terminal or authorized SSH access to its EWAOL Linux guest.
    - Complete the virtual camera setup and moving-traffic video steps in Build a Camera-to-VLM Pipeline on Arm Zena CSS; confirm that the guest camera can receive frames.
    - Basic Linux, containers, Python, and ROS 2 topic knowledge.
    - Internet access from the guest to obtain the ROS 2 container base image and packages, with enough guest storage for the build.

author: Odin Shen

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
armips:
    - Cortex-A
tools_software_languages:
    - Arm Zena CSS
    - Siemens Innexis ANA
    - ROS 2
    - Podman
    - Python
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Siemens Innexis Architecture Native Acceleration
        link: https://www.siemens.com/en-us/products/ic/hav/innexis/architecture-native-acceleration/
        type: documentation
    - resource:
        title: ROS 2 Jazzy documentation
        link: https://docs.ros.org/en/jazzy/
        type: documentation

### FIXED, DO NOT MODIFY
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---
