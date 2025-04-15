---
title: Problem solving – inefficient transfer workloads
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Focusing on transfer workloads

Your application may contain inefficient transfer workloads.

{{% notice "What are transfer workloads?" %}}
Transfer workloads use the GPU to move data between resources.

Transfer operations require power and bandwidth. For this reason, they should be made as small and efficient as possible – or preferably, avoided entirely.

Transfer workloads are initiated by specific API calls. These include:

- `vkCmdCopyBuffer()`, which copies regions of a buffer
- `vkCmdClearColorImage()`, which clears an image.
{{% /notice %}}

To find which API calls your application uses to start transfer workloads:

- Open the render graph for your captured frames
- Click a transfer node
- Now move to the API Calls view (labeled “API Calls”)
- Observe the API calls in use.

## Problem: inefficient clear routines

`vkCmdClearColorImage()` is an inefficient way to clear an image.

A more efficient way to clear an image attachment is to clear the attachment at the start of a render pass. To do this:

- Set the `loadOp` parameter in a `VkAttachmentDescription` structure to `VK_ATTACHMENT_LOAD_OP_CLEAR`
- Attach the `VkAttachmentDescription` to a `VkRenderPassCreateInfo`
- Supply this to API `vkCreateRenderPass()`

## Problem: inefficient image resolutions

In the previous section, you saw an issue where unnecessarily large textures were inputs to a render pass. Similar problems can be seen in the context of transfer operations, which should operate over the smallest practicable area. To achieve this, change the values in the `VkBufferCopy` structure passed to `vkCmdCopyBuffer()`.
