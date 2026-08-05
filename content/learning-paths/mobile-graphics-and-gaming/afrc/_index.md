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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-05T14:49:39Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5c865102481efdcedc651da28eaae1e2ee3e491eb5e075a260d91065c157f44c
  summary_generated_at: '2026-08-05T14:49:39Z'
  summary_source_hash: 5c865102481efdcedc651da28eaae1e2ee3e491eb5e075a260d91065c157f44c
  faq_generated_at: '2026-08-05T14:49:39Z'
  faq_source_hash: 5c865102481efdcedc651da28eaae1e2ee3e491eb5e075a260d91065c157f44c
  summary: >-
    You'll enable and verify Arm Fixed Rate Compression for Vulkan images on Android. You'll confirm the
    required Vulkan extensions, define image settings, query fixed-rate support, and request
    compression with the appropriate `pNext` structure. Then, you'll inspect the compression state to
    validate the setting for your images, including swapchain-specific extension requirements.
  faqs:
  - question: How do I check whether my device supports the required Vulkan extensions?
    answer: >-
      Call `vkEnumerateDeviceExtensionProperties` and look for `VK_EXT_image_compression_control`.
      If present, add it to `VkDeviceCreateInfo.ppEnabledExtensionNames` before `vkCreateDevice`.
  - question: What should I do differently for swapchain images?
    answer: >-
      Swapchain images also require `VK_EXT_image_compression_control_swapchain`. Enable this extension
      in addition to `VK_EXT_image_compression_control` if you want fixed-rate compression on swapchain
      images.
  - question: Can I follow this path without creating a new Vulkan sample?
    answer: >-
      Yes. You can use your own Vulkan application and refer to the Khronos Vulkan Samples code
      as a reference for the steps shown.
  - question: How do I know if a specific image configuration supports fixed-rate compression?
    answer: >-
      Populate `VkImageCreateInfo` with your format, image type, tiling, and usage, then use these
      properties to query support before creating the image. If supported, proceed to request
      fixed-rate compression.
  - question: How do I request and verify that fixed-rate compression is applied?
    answer: >-
      Provide a `VkImageCompressionControlEXT` with `VK_IMAGE_COMPRESSION_FIXED_RATE_DEFAULT_EXT`
      in the `pNext` chain of `VkImageCreateInfo` when creating the image. Use `VK_EXT_image_compression_control`
      to inspect the compression state and confirm that fixed-rate compression is active.
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
