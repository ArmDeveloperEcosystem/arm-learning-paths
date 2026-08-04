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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T22:09:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5c865102481efdcedc651da28eaae1e2ee3e491eb5e075a260d91065c157f44c
  summary_generated_at: '2026-08-04T22:09:18Z'
  summary_source_hash: 5c865102481efdcedc651da28eaae1e2ee3e491eb5e075a260d91065c157f44c
  faq_generated_at: '2026-08-04T22:09:18Z'
  faq_source_hash: 5c865102481efdcedc651da28eaae1e2ee3e491eb5e075a260d91065c157f44c
  summary: >-
    You enable and use Arm Fixed Rate Compression (AFRC) in Vulkan
    on Android. You start by enabling the required Vulkan extensions, using VK_EXT_image_compression_control
    to verify default compression and request fixed-rate compression, and adding VK_EXT_image_compression_control_swapchain
    for swapchain images. You then use intended VkImageCreateInfo properties to query whether
    a given image configuration supports fixed-rate compression. With support confirmed, you request
    AFRC by chaining VkImageCompressionControlEXT to VkImageCreateInfo and setting the fixed-rate
    default flag before creating the image. You use a Vulkan API Sample as a reference so
    you can experiment and validate that compression settings are applied on a supported device.
  faqs:
  - question: Which Vulkan extensions should I enable for fixed-rate compression?
    answer: >-
      Enable VK_EXT_image_compression_control to verify compression and request fixed-rate compression.
      For swapchain images, also enable VK_EXT_image_compression_control_swapchain.
  - question: How do I check if my device supports the required extensions?
    answer: >-
      Call vkEnumerateDeviceExtensionProperties and look for the needed extension names. If present,
      add them to VkDeviceCreateInfo.ppEnabledExtensionNames before calling vkCreateDevice.
  - question: How do I know if a specific image configuration supports fixed-rate compression?
    answer: >-
      Define the image’s intended VkImageCreateInfo properties and use them to query for fixed-rate
      compression support on your platform. Continue only if the query indicates support for that
      configuration.
  - question: Where do I request AFRC during image creation?
    answer: >-
      Provide a VkImageCompressionControlEXT in the pNext chain of VkImageCreateInfo and set flags
      to VK_IMAGE_COMPRESSION_FIXED_RATE_DEFAULT_EXT. Then create the image with vkCreateImage.
  - question: How can I verify that compression was applied?
    answer: >-
      Use VK_EXT_image_compression_control to check whether compression (including default or
      requested fixed-rate) was applied. Inspect the reported compression information to confirm
      your request was honored.
# END generated_summary_faq

author: Jose-Emilio Munoz-Lopez

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
