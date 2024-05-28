---
title: Vulkan Extensions
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Vulkan Extensions

The Vulkan extension [VK_EXT_image_compression_control](https://docs.vulkan.org/spec/latest/appendices/extensions.html#VK_EXT_image_compression_control) may be used to verify if default compression (such as AFBC) was applied, and to request fixed-rate compression.

Swapchain images are a special case, and additionally require the [VK_EXT_image_compression_control_swapchain](https://docs.vulkan.org/spec/latest/appendices/extensions.html#VK_EXT_image_compression_control_swapchain) extension.

### Enable VK_EXT_image_compression_control

In your application, you may use [vkEnumerateDeviceExtensionProperties](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/vkEnumerateDeviceExtensionProperties.html) to check if the device supports the extension, and, if so, include it in [VkDeviceCreateInfo](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VkDeviceCreateInfo.html)'s `ppEnabledExtensionNames` before calling [vkCreateDevice](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/vkCreateDevice.html).
In the Vulkan Samples framework, this can be handled in the sample's constructor with this helper function:

```C
afrc::afrc()
{
	add_device_extension(VK_EXT_IMAGE_COMPRESSION_CONTROL_EXTENSION_NAME);
}
```

If a device supports the extension, it does not mean that it also supports fixed-rate compression of images.
The extension may still be used to verify if the images use default (lossless) compression.

Before compressing a `VkImage`, you need to use the extension to query if any given image, with its particular format and usage properties, supports fixed-rate compression, as shown in the next step.
