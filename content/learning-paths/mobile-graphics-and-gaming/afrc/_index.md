---
title: Learn about Arm Fixed Rate Compression (AFRC)

minutes_to_complete: 25

description: Learn how to enable and verify Arm Fixed Rate Compression in Vulkan applications on Android devices to reduce memory footprint and bandwidth.

who_is_this_for: Software developers of Android applications and mobile games who are interested in learning how to enable Arm Fixed Rate Compression (AFRC) to improve performance.

learning_objectives:
    - Query for fixed-rate compression support.
    - Specify what compression to use.
    - Verify that compression is applied.

prerequisites:
    - An appropriate Android device (e.g., Google Pixel 8) supporting the required Vulkan extensions.
    - Knowledge of the Vulkan API.
    - A Vulkan application that creates and uses images. This Learning Path shows how to use an API Sample in the [Khronos Vulkan Samples repository](https://github.com/KhronosGroup/Vulkan-Samples/blob/main/scripts/README.adoc#generate-api-sample) as an example.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:39:11Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e4512ad20b372f616409199c51a38d95cb116ec6cf49d9004348d6bb8ee4014d
  summary_generated_at: '2026-06-02T02:39:32Z'
  summary_source_hash: e4512ad20b372f616409199c51a38d95cb116ec6cf49d9004348d6bb8ee4014d
  faq_generated_at: '2026-06-02T23:39:11Z'
  faq_source_hash: e4512ad20b372f616409199c51a38d95cb116ec6cf49d9004348d6bb8ee4014d
  summary: >-
    This Learning Path shows how to enable and verify Arm Fixed Rate Compression (AFRC) in Vulkan
    applications on Android. You will check for VK_EXT_image_compression_control support (and
    VK_EXT_image_compression_control_swapchain for swapchain images), query whether specific VkImage
    configurations support fixed-rate compression, and request AFRC by chaining VkImageCompressionControlEXT
    at image creation. The steps reference a Vulkan API Sample from the Khronos Vulkan Samples
    repository as a test application. Prerequisites include an Android device (for example, Google
    Pixel 8) that supports the required Vulkan extensions, familiarity with the Vulkan API, and
    a Vulkan app that creates and uses images. By the end, you can confirm that compression is
    applied to reduce memory footprint and bandwidth.
  faqs:
  - question: How do I know if my Android device supports the required Vulkan extensions for AFRC?
    answer: >-
      Use vkEnumerateDeviceExtensionProperties to look for VK_EXT_image_compression_control, and
      include VK_EXT_image_compression_control_swapchain if you need swapchain images. If these
      are not listed, the device does not meet the prerequisites for this path.
  - question: Where do I enable the Vulkan extensions in my application?
    answer: >-
      Add the required extension names to VkDeviceCreateInfo::ppEnabledExtensionNames before calling
      vkCreateDevice. This enables VK_EXT_image_compression_control (and the swapchain variant
      when needed) for use in your Vulkan device.
  - question: How do I query whether a specific image setup supports fixed-rate compression?
    answer: >-
      Define your intended VkImageCreateInfo properties (such as format, type, tiling, and usage)
      and use them to query support on your platform before creating the image. The path shows
      using those properties to drive the support check.
  - question: How do I request fixed-rate compression at image creation time?
    answer: >-
      Provide a VkImageCompressionControlEXT structure in the pNext chain of VkImageCreateInfo
      and set flags = VK_IMAGE_COMPRESSION_FIXED_RATE_DEFAULT_EXT. Then create the VkImage with
      these settings applied.
  - question: What result should I expect when verifying that compression was applied?
    answer: >-
      VK_EXT_image_compression_control can be used to verify whether default compression was applied
      and to confirm your fixed-rate request. The verification indicates the compression chosen
      for the image based on device support and your request.
# END generated_summary_faq

author: Jose-Emilio Munoz-Lopez

### Tags
skilllevels: Advanced
subjects: Graphics
armips:
    - Mali
    - Immortalis
operatingsystems:
    - Android
tools_software_languages:
    - Vulkan


further_reading:
    - resource:
        title: AFRC sample and tutorial
        link: https://github.com/KhronosGroup/Vulkan-Samples/blob/main/samples/performance/image_compression_control/README.adoc
        type: website
    - resource:
        title: AFRC best practices
        link: https://developer.arm.com/documentation/101897/latest/Buffers-and-textures/AFRC?lang=en
        type: documentation
    - resource:
        title: AFRC in Arm Immortalis-G715
        link: https://developer.arm.com/community/arm-community-blogs/b/mobile-graphics-and-gaming-blog/posts/arm-immortalis-g715-developer-overview
        type: blog




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

