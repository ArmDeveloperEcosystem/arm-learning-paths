---
title: Deploy PaddlePaddle on Arm Cortex-M with Arm Virtual Hardware

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers interested in using PaddlePaddle for Arm Cortex-M processors.

learning_objectives: 
    - Export Paddle inference model
    - Compile Paddle inference model with TVMC
    - Deploy on the AVH Corstone-300 platform with Arm Cortex-M55

prerequisites:
    - Some familiarity with embedded programming 
    - Some familiarity with AI/ML software development 
    - An Amazon Web Services(AWS) [account](https://aws.amazon.com/) to subscribe [Arm Virtual Hardware](https://aws.amazon.com/marketplace/pp/prodview-urbpq7yo5va7g) Amazon Machine Image(AMI). 

author: Liliya Wu

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-M
    - Corstone
operatingsystems:
    - Baremetal
tools_software_languages:
    - Arm Virtual Hardware
<<<<<<< HEAD
=======
    - Coding
>>>>>>> 5f2151168 (Changed model to Tiny Rock–Paper–Scissors CNN)
    - GCC
    - Paddle
    - TVMC

further_reading:
    - resource:
        title: AVH Product Overview
        link: https://arm-software.github.io/AVH/main/overview/html/index.html
        type: documentation
    - resource:
        title: PaddleOCR
        link: https://github.com/PaddlePaddle/PaddleOCR
        type: website
    - resource:
        title: Paddle examples for AVH
        link: https://github.com/ArmDeveloperEcosystem/Paddle-examples-for-AVH/tree/main/Object-Detection-example
        type: website
    - resource:
        title: Arm and Baidu PaddlePaddle blog
        link: https://www.arm.com/blogs/blueprint/baidu-paddlepaddle
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
