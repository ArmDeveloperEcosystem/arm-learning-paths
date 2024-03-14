---
title: Query for compression support
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Query for compression support

To create a VkImage, you need a [VkImageCreateInfo](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VkImageCreateInfo.html) structure defining the image's properties.
Before creating the image, you can use these properties to query if the image supports fixed-rate compression on your platform.
For instance, the structure may look like this:

```C
VkImageCreateInfo image_create_info{VK_STRUCTURE_TYPE_IMAGE_CREATE_INFO};

image_create_info.format      = VK_FORMAT_R8G8B8_UNORM;
image_create_info.imageType   = VK_IMAGE_TYPE_2D;
image_create_info.tiling      = VK_IMAGE_TILING_OPTIMAL;
image_create_info.usage       = VK_IMAGE_USAGE_COLOR_ATTACHMENT_BIT | VK_IMAGE_USAGE_SAMPLED_BIT;
image_create_info.extent      = {8, 8, 1};
image_create_info.mipLevels   = 1;
image_create_info.arrayLayers = 1;
image_create_info.samples     = VK_SAMPLE_COUNT_1_BIT;
```

To query for fixed-rate compression support, use this information to fill in a [VkImageFormatProperties2](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VkImageFormatProperties2KHR.html) structure:

```C
VkPhysicalDeviceImageFormatInfo2 image_format_info{VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_IMAGE_FORMAT_INFO_2};

image_format_info.format = image_create_info.format;
image_format_info.type   = image_create_info.imageType;
image_format_info.tiling = image_create_info.tiling;
image_format_info.usage  = image_create_info.usage;
```

Additionally, add a [VkImageCompressionControlEXT](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VkImageCompressionControlEXT.html) to its `pNext` chain:

```C
VkImageCompressionControlEXT compression_control{VK_STRUCTURE_TYPE_IMAGE_COMPRESSION_CONTROL_EXT};
compression_control.flags = VK_IMAGE_COMPRESSION_FIXED_RATE_DEFAULT_EXT;

image_format_info.pNext  = &compression_control;
```

You may then prepare a `VkImageFormatProperties2` structure, with a [VkImageCompressionPropertiesEXT](https://registry.khronos.org/vulkan/specs/1.3-extensions/man/html/VkImageCompressionPropertiesEXT.html) in its `pNext` chain:

```C
VkImageCompressionPropertiesEXT supported_compression_properties{VK_STRUCTURE_TYPE_IMAGE_COMPRESSION_PROPERTIES_EXT};

VkImageFormatProperties2 image_format_properties{VK_STRUCTURE_TYPE_IMAGE_FORMAT_PROPERTIES_2};
image_format_properties.pNext = &supported_compression_properties;
```

Finally, put these two together in a call to `vkGetPhysicalDeviceImageFormatProperties2KHR`:

```C
vkGetPhysicalDeviceImageFormatProperties2KHR(get_device().get_gpu().get_handle(), &image_format_info, &image_format_properties);
```

You can then inspect the values written to `VkImageCompressionPropertiesEXT` to determine if the image supports fixed-rate compression.
For instance, you may use the print function helper provided below to inspect the logs when running your sample:

```C
LOGI("Image supports {}", compression_to_string(supported_compression_properties.imageCompressionFlags));

LOGI("Image supports {}", fixed_rate_flags_to_string(supported_compression_properties.imageCompressionFixedRateFlags));
```

The logcat output may look like this:

```output
I/VulkanSamples: [info] Image supports VK_IMAGE_COMPRESSION_FIXED_RATE_EXPLICIT_EXT
I/VulkanSamples: [info] Image supports VK_IMAGE_COMPRESSION_FIXED_RATE_2BPC_BIT_EXT | VK_IMAGE_COMPRESSION_FIXED_RATE_4BPC_BIT_EXT | VK_IMAGE_COMPRESSION_FIXED_RATE_5BPC_BIT_EXT
```

Print helper functions for reference:

```C
const std::string compression_to_string(VkImageCompressionFlagsEXT flag)
{
	switch (flag)
	{
		case VK_IMAGE_COMPRESSION_DEFAULT_EXT:
			return "VK_IMAGE_COMPRESSION_DEFAULT_EXT";
		case VK_IMAGE_COMPRESSION_FIXED_RATE_DEFAULT_EXT:
			return "VK_IMAGE_COMPRESSION_FIXED_RATE_DEFAULT_EXT";
		case VK_IMAGE_COMPRESSION_FIXED_RATE_EXPLICIT_EXT:
			return "VK_IMAGE_COMPRESSION_FIXED_RATE_EXPLICIT_EXT";
		case VK_IMAGE_COMPRESSION_DISABLED_EXT:
			return "VK_IMAGE_COMPRESSION_DISABLED_EXT";
		default:
		{
			return "";
		}
	}
}

const std::string fixed_rate_flags_to_string(uint32_t flags)
{
	if (0 == flags)
	{
		return "VK_IMAGE_COMPRESSION_FIXED_RATE_NONE_EXT";
	}

	const std::map<VkImageCompressionFixedRateFlagsEXT, const char *> string_map =
	    {{VK_IMAGE_COMPRESSION_FIXED_RATE_1BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_1BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_2BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_2BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_3BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_3BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_4BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_4BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_5BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_5BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_6BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_6BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_7BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_7BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_8BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_8BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_9BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_9BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_10BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_10BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_11BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_11BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_12BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_12BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_13BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_13BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_14BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_14BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_15BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_15BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_16BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_16BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_17BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_17BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_18BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_18BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_19BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_19BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_20BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_20BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_21BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_21BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_22BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_22BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_23BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_23BPC_BIT_EXT"},
	     {VK_IMAGE_COMPRESSION_FIXED_RATE_24BPC_BIT_EXT, "VK_IMAGE_COMPRESSION_FIXED_RATE_24BPC_BIT_EXT"}};

	std::stringstream result;
	bool              append = false;
	for (const auto &s : string_map)
	{
		if (flags & s.first)
		{
			if (append)
			{
				result << " | ";
			}
			result << s.second;
			append = true;
		}
	}

	return result.str();
}
```

### Why does this image not support fixed-rate compression?

You may find that the output of the code looks like:

```output
I/VulkanSamples: [info] Image supports VK_IMAGE_COMPRESSION_DISABLED_EXT
I/VulkanSamples: [info] Image supports VK_IMAGE_COMPRESSION_FIXED_RATE_NONE_EXT
```

This means that the image does not support any sort of compression.
Possible reasons are discussed in [Arm GPU Best Practices Developer Guide](https://developer.arm.com/documentation/101897/latest/Buffers-and-textures/AFRC?lang=en).
Depending on the device, image properties like `image_create_info.format` and `image_create_info.usage` (e.g., storage images) may be incompatible with fixed-rate compression.

Try using different values for these in case you find a suitable combination for your application that supports fixed-rate compression.
Otherwise, for better performance, try to find one that at least supports AFBC if possible, following the guidance found in [the AFBC guide](https://developer.arm.com/documentation/101897/latest/Buffers-and-textures/AFBC-textures-for-Vulkan?lang=en), so that the output ideally looks like this:

```output
I/VulkanSamples: [info] IMAGE SUPPORTS VK_IMAGE_COMPRESSION_DEFAULT_EXT
I/VulkanSamples: [info] IMAGE SUPPORTS VK_IMAGE_COMPRESSION_FIXED_RATE_NONE_EXT
```
