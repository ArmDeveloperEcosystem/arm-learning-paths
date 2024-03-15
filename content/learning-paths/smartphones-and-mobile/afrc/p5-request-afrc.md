---
title: Request fixed-rate compression
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Request fixed-rate compression

Compression is specified at image creation time. To request fixed-rate compression, provide a `VkImageCompressionControlEXT` structure to the `pNext` chain of `VkImageCreateInfo`:

```C
VkImageCompressionControlEXT compression_control{VK_STRUCTURE_TYPE_IMAGE_COMPRESSION_CONTROL_EXT};
compression_control.flags = VK_IMAGE_COMPRESSION_FIXED_RATE_DEFAULT_EXT;

image_create_info.pNext = &compression_control;
```

Note that these are the same `VkImageCompressionControlEXT` and `VkImageCreateInfo` structures used in the previous step.

The image may then be created:

```C
VkImage image_handle;

vkCreateImage(get_device().get_handle(), &image_create_info, nullptr, &image_handle);
```

This requests default fixed-rate compression (which depends on the device).
On Arm GPUs, it is the highest supported bitrate that is the highest possible quality.

To request a specific bitrate (after confirming that it is supported, as shown in the previous step), you may instead use `VK_IMAGE_COMPRESSION_FIXED_RATE_EXPLICIT_EXT` like this:

```C
VkImageCompressionFixedRateFlagsEXT fixed_rate_flags_array[1] = {VK_IMAGE_COMPRESSION_FIXED_RATE_2BPC_BIT_EXT};

VkImageCompressionControlEXT compression_control{VK_STRUCTURE_TYPE_IMAGE_COMPRESSION_CONTROL_EXT};
compression_control.flags                        = VK_IMAGE_COMPRESSION_FIXED_RATE_EXPLICIT_EXT;
compression_control.compressionControlPlaneCount = 1;
compression_control.pFixedRateFlags              = &fixed_rate_flags_array[0];

image_format_info.pNext = &compression_control;
```

This example requests a fixed rate of 2 bits per component.
