---
title: Profile Arm Neural Technology workloads with the Arm Streamline GUI

description: Profile your Android ML for Vulkan workload with the Arm Streamline GUI, then inspect NX activity, GPU timeline events, and graph-operation costs.

minutes_to_complete: 45

who_is_this_for: This Learning Path is for Android and graphics developers who want to profile their ML for Vulkan applications on the Mali Neural Accelerator using the Arm Streamline GUI.

learning_objectives:
    - Identify how neural accelerator (NX), Vulkan ML workloads, and GPU shader execution relate to a Streamline capture.
    - Prepare your debuggable Android workload for Streamline capture.
    - Collect and open a 30-second workload capture using the Streamline GUI.
    - Inspect NX activity and graph operations using Mali Timeline and Dispatch Graph Workloads.

prerequisites:
    - Your own debuggable Android app, already installed on the device, with a supported ML for Vulkan workload
    - An Android 11 or later device with NX-capable Mali G2 or later hardware, Mali DDK r56p0 or later, and USB debugging access
    - Basic familiarity with Android applications, Vulkan, and terminal commands
    - A Windows, macOS, or supported Linux host for Arm Performance Studio and Android SDK Platform Tools
    - A USB data cable to connect the Android device to your host or wireless debugging enabled

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-23T17:52:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 560b2a63a796a5c370b3c916b2e3192dd01be07b72252bd540af3da98f74109f
  summary_generated_at: '2026-10-23T17:52:54Z'
  summary_source_hash: 560b2a63a796a5c370b3c916b2e3192dd01be07b72252bd540af3da98f74109f
  faq_generated_at: '2026-10-23T17:52:54Z'
  faq_source_hash: 560b2a63a796a5c370b3c916b2e3192dd01be07b72252bd540af3da98f74109f
  summary: >-
    You'll use Arm Streamline to profile an Android ML for Vulkan workload and inspect NX activity, GPU timeline events, and graph-operation costs. First, you'll review how Vulkan graph dispatches can use NX and shader cores. Then, you'll prepare a debuggable app and Android device and capture about 30 seconds in the Streamline GUI. Finally, you'll analyze the capture using the Mali Timeline and Dispatch Graph Workloads views.
  # faqs:
  # - question: How can I check whether Streamline supports NX profiling?
  #   answer: >-
  #     In **Streamline**, select **About Streamline** and check the version. Use Streamline 9.9 or newer for the NX workflow.
  # - question: How do I check that an Android device is ready for capture in Streamline?
  #   answer: >-
  #     In the **Start** view, select **Android (adb)** and check **Select device**. Confirm that `adb devices -l` lists the device with status `device`; if the status is `unauthorized`, accept the debugging authorization prompt.
  # - question: Which application and counters should I select before recording?
  #   answer: >-
  #     Choose the template that matches the GPU. For the example GPU, select **Mali G2-Ultra - 5th Generation** and confirm **Mali Timeline events: Perfetto** appears in **Events to collect**.
  # - question: What result should I expect after recording a 30-second capture?
  #   answer: >-
  #     After capture, check the device, app, and duration. Confirm NX activity during the intended workload and GPU workload events in **Mali Timeline**. Select **Dispatch Graph Workloads: Mali Timeline** separately to inspect graph-operation data; the data depends on the workload, template, Timeline layer, and statistics.
  # - question: How do I interpret mixed NX and shader-core activity in the capture?
  #   answer: >-
  #     Check **Type** in **Dispatch Graph Workloads** to distinguish **NX** execution from shader-core execution. The mapping depends on the operation, tensor data types and shapes, and the capabilities of the target GPU and driver.
# END generated_summary_faq

author:
    - Kieran Hejmadi
    - Amarbold Batzorig

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: false

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Graphics
armips:
    - Mali
tools_software_languages:
    - Arm Performance Studio
    - Streamline
    - Vulkan
    - NX
operatingsystems:
    - Android

further_reading:
    - resource:
        title: Arm Streamline 9.9 User Guide
        link: https://support.arm.com/documentation/101816/9-9
        type: documentation
    - resource:
        title: Install Arm Streamline
        link: /install-guides/streamline/
        type: documentation
    - resource:
        title: Install Arm Performance Studio
        link: /install-guides/ams/
        type: documentation
    - resource:
        title: Arm Neural Technology Playbook - Evaluate
        link: /learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/
        type: learningpath
    - resource:
        title: Analyze Neural Frame Rate Upscaling using Project Moku
        link: /learning-paths/mobile-graphics-and-gaming/nfru-cases-study/
        type: learningpath
    - resource:
        title: Vulkan physical device driver properties
        link: https://docs.vulkan.org/refpages/latest/refpages/source/VkPhysicalDeviceDriverProperties.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
