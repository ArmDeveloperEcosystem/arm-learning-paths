---
title: Verify that compression is applied
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Verify that compression is applied

To query which compression was applied, if any, once a `VkImage` has been created, use a [VkImageCompressionPropertiesEXT](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VkImageCompressionPropertiesEXT.html) structure.
Add `VkImageCompressionPropertiesEXT` to the `pNext` chain of [VkImageSubresource2EXT](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VkImageSubresource2EXT.html), and then call [vkGetImageSubresourceLayout2EXT](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/vkGetImageSubresourceLayout2EXT.html):

```C
VkImageCompressionPropertiesEXT applied_compression_properties{VK_STRUCTURE_TYPE_IMAGE_COMPRESSION_PROPERTIES_EXT};

VkSubresourceLayout2EXT subresource_layout{VK_STRUCTURE_TYPE_SUBRESOURCE_LAYOUT_2_KHR};
subresource_layout.pNext = &applied_compression_properties;

VkImageSubresource2EXT image_subresource{VK_STRUCTURE_TYPE_IMAGE_SUBRESOURCE_2_KHR};
image_subresource.imageSubresource.aspectMask = VK_IMAGE_ASPECT_COLOR_BIT;
image_subresource.imageSubresource.mipLevel   = 0;
image_subresource.imageSubresource.arrayLayer = 0;

vkGetImageSubresourceLayout2EXT(get_device().get_handle(), image_handle, &image_subresource, &subresource_layout);
```

Inspect the values written to the `imageCompressionFlags` and  `imageCompressionFixedRateFlags` components of `VkImageCompressionPropertiesEXT`:

```C
LOGI("Created image reports {}", compression_to_string(applied_compression_properties.imageCompressionFlags));
LOGI("Created image reports {}", fixed_rate_flags_to_string(applied_compression_properties.imageCompressionFixedRateFlags));
```

The output may then look like this:

```output
I/VulkanSamples: [info] Created image reports VK_IMAGE_COMPRESSION_FIXED_RATE_EXPLICIT_EXT
I/VulkanSamples: [info] Created image reports VK_IMAGE_COMPRESSION_FIXED_RATE_5BPC_BIT_EXT
```

You have now successfully added fixed-rate compression to your image, saving both memory and bandwidth.
