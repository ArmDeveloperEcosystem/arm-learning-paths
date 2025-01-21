---
title: "Setup: enabling ray tracing"
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Setup: Enabling ray tracing

Vulkan uses the same API for ray tracing on PC and mobile devices. This makes it extremely easy to implement and test ray tracing effects on PC and deploy them on mobile. Porting existing ray tracing effects from PC to mobile should also be simple.

Arm® Mali™-G7-series GPUs after the [Arm® Mali™-G715](https://developer.arm.com/Processors/Mali-G715) might or might not support ray tracing, depending on the phone model. Immortalis GPUs such as [Arm® Immortalis-G715](https://developer.arm.com/Processors/Immortalis-G715), [Arm® Immortalis-G720](https://developer.arm.com/Processors/Immortalis-G720), or [Arm® Immortalis-G925](https://developer.arm.com/Processors/Immortalis-G925) support ray tracing. These GPUs are available in multiple devices already in the market. Moreover, ray tracing is a promising modern technology, so multiple GPU vendors support the API. Most recent high-end Android smartphones support ray tracing, making it a feature game developers can rely on.

Vulkan offers ray tracing as a series of extensions, making it easy to query for support and to enable it. The most relevant extensions are: `VK_KHR_acceleration_structure`, `VK_KHR_ray_query`, and `VK_KHR_ray_tracing_pipeline`.

You can query the physical device to check if it supports the extensions. Here is a helper function:

``` cpp
uint32_t device_extension_count;
std::vector<VkExtensionProperties> supported_extensions;
vkEnumerateDeviceExtensionProperties(physical_device, nullptr,
                                     &device_extension_count, nullptr);
supported_extensions.resize(device_extension_count);
vkEnumerateDeviceExtensionProperties(physical_device, nullptr,
                                     &device_extension_count,
                                     supported_extensions.data());

auto is_extension_supported =
    [&supported_extensions](const std::string_view requested_extension) {
      for (const auto &device_extension : supported_extensions) {
        if (device_extension.extensionName == requested_extension) {
          return true;
        }
      }
      return false;
    };
```

You can use it to query the ray tracing extensions' features:

``` cpp
VkPhysicalDeviceFeatures2 features2{VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FEATURES_2};

VkPhysicalDeviceAccelerationStructureFeaturesKHR acceleration_structure_features{VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_ACCELERATION_STRUCTURE_FEATURES_KHR};
if (is_extension_supported(VK_KHR_ACCELERATION_STRUCTURE_EXTENSION_NAME))
{
    acceleration_structure_features.pNext = features2.pNext;
    features2.pNext = &acceleration_structure_features;
}
VkPhysicalDeviceRayQueryFeaturesKHR ray_query_features{VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_QUERY_FEATURES_KHR};
if (is_extension_supported(VK_KHR_RAY_QUERY_EXTENSION_NAME))
{
    ray_query_features.pNext = features2.pNext;
    features2.pNext = &ray_query_features;
}
VkPhysicalDeviceRayTracingPipelineFeaturesKHR ray_tracing_pipeline_features{VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_RAY_TRACING_PIPELINE_FEATURES_KHR};
if (is_extension_supported(VK_KHR_RAY_TRACING_PIPELINE_EXTENSION_NAME))
{
    ray_tracing_pipeline_features.pNext = features2.pNext;
    features2.pNext = &ray_tracing_pipeline_features;
}

vkGetPhysicalDeviceFeatures2(physical_device, &features2);
```

Finally, you can enable the extensions when creating the logical device:

``` cpp
std::vector<const char *> enabled_extensions{};

VkPhysicalDeviceFeatures2 requested_features2{VK_STRUCTURE_TYPE_PHYSICAL_DEVICE_FEATURES_2};
requested_features2.features = other_requested_gpu_features;

if (acceleration_structure_features.accelerationStructure)
{
    enabled_extensions.push_back(VK_KHR_ACCELERATION_STRUCTURE_EXTENSION_NAME);
    acceleration_structure_features.pNext = requested_features2.pNext;
    requested_features2.pNext = &acceleration_structure_features;
}

if (ray_query_features.rayQuery)
{
    enabled_extensions.push_back(VK_KHR_RAY_QUERY_EXTENSION_NAME);
    ray_query_features.pNext = requested_features2.pNext;
    requested_features2.pNext = &ray_query_features;
}

if (ray_tracing_pipeline_features.rayTracingPipeline)
{
    enabled_extensions.push_back(VK_KHR_RAY_TRACING_PIPELINE_EXTENSION_NAME);
    ray_tracing_pipeline_features.pNext = requested_features2.pNext;
    requested_features2.pNext = &ray_tracing_pipeline_features;
}

VkDeviceCreateInfo create_info{VK_STRUCTURE_TYPE_DEVICE_CREATE_INFO};
create_info.pQueueCreateInfos = queue_create_infos.data();
create_info.queueCreateInfoCount = to_u32(queue_create_infos.size());
create_info.enabledExtensionCount = to_u32(enabled_extensions.size());
create_info.ppEnabledExtensionNames = enabled_extensions.data();
create_info.pNext = &requested_features2;
create_info.pEnabledFeatures = nullptr;

vkCreateDevice(physical_device, &create_info, nullptr, &device);
```