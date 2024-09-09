---
title: "Introduction: What is ray tracing?"
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Introduction: What is ray tracing?

Ray tracing is a technique to render images using ray casting methods to simulate light transport. Traditionally, this is not suitable for real time or games, and is mostly used by CGI or movies.

Vulkan includes a new set of extensions for ray intersection tests, designed to facilitate ray tracing.

The API allows applications to define a ray, setting an origin and a direction and then test this ray against the scene geometry. By default, the API will return the closest hit that the ray will intercept in our scene.

Vulkan's ray tracing API is very flexible and allows creative uses like collision detection in physics simulations. However, the main use case for ray tracing is rendering. This is because ray tracing allows applications to simulate the behavior of light, in a way resembling physical reality.

In the real world a light source emits light rays in all directions, these rays interact with multiple objects. When a ray intersects an object, the light will interact with it, causing the object to absorb and reflect certain amounts of light.

Traditionally, developers render games using rasterization. Rasterization works by transforming the geometry into triangle primitives and projecting them onto the screen. GPUs then use a depth buffer to resolve the visibility and decide which pixels are covered by each triangle.

With ray tracing, we can instead use path tracing. A path tracer does not need to use rasterization, instead it can launch rays from the camera. These rays will bounce around the scene until they produce a final image, resolving visibility using the closest hit. In the real world, rays travel from a light until they reach the camera, but this is extremely inefficient since most rays will not reach our eyes, this is why in rendering we launch rays in the reverse order, starting from the camera.

Path tracing is extremely costly since we will need to launch thousands of rays per pixel to produce a non-noisy image. Rendering a frame in real time using path tracing is not feasible even on desktop high end GPUs. The common approach is to have a hybrid renderer, with a traditional rasterization pass to resolve visibility and compute the G-buffer, and then implement each ray tracing effect as a separate post-process.

{{< tabpane >}}
  {{< tab header="Example 1: RT ON" title="Example 1: ray tracing ON" img_src="/learning-paths/smartphones-and-mobile/ray_tracing/images/city_rt_on.png">}}{{< /tab >}}
  {{< tab header="Example 1: RT OFF" title="Example 1: ray tracing OFF" img_src="/learning-paths/smartphones-and-mobile/ray_tracing/images/city_rt_off.png">}}{{< /tab >}}
  {{< tab header="Example 2: RT ON" title="Example 2: ray tracing ON" img_src="/learning-paths/smartphones-and-mobile/ray_tracing/images/bonza_rt_on.png">}}{{< /tab >}}
  {{< tab header="Example 2: RT OFF" title="Example 2: ray tracing OFF" img_src="/learning-paths/smartphones-and-mobile/ray_tracing/images/bonza_rt_off.png">}}{{< /tab >}}
  {{< tab header="Example 3: RT ON" title="Example 3: ray tracing ON" img_src="/learning-paths/smartphones-and-mobile/ray_tracing/images/immortalis_rt_on.png">}}{{< /tab >}}
  {{< tab header="Example 3: RT OFF" title="Example 3: ray tracing OFF" img_src="/learning-paths/smartphones-and-mobile/ray_tracing/images/immortalis_rt_off.png">}}{{< /tab >}}
{{< /tabpane >}}