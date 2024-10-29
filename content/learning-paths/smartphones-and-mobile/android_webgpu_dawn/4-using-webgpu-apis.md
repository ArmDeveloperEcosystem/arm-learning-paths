---
title: Using Dawn WebGPU APIs in the application
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Setup project

Now that we have `webgpudawn` library built, we can start by removing the extra files included as part of the stock Game Activity project. Delete all the files from the top `cpp` directory,except `main.cpp`. We will create `webgpuRenderer.cpp` and `webgpuRenderer.h` files for our creating our application with WebGPU.

## Using Dawn WebGPU APIs

There are several layers of abstraction between a device GPU and an application running the WebGPU API.

![WebGPU Application Interface](./images/webgpu_app_interface.png "WebGPU Application Interface")

It is useful to understand these as we begin to use WebGPU APIs in our application

* Physical devices have GPUs. Most devices only have one GPU, but some have more than one.
* A native GPU API, which is part of the OS (e.g. Vulkan, Metal etc.), is a programming interface allowing native applications to use the capabilities of the GPU. API instructions are sent to the GPU (and responses received) via a driver. It is possible for a system to have multiple native OS APIs and drivers available to communicate with the GPU, although the above diagram assumes a device with only one native API/driver.
* A WebGPU implementation like Dawn handles communicating with the GPU via a native GPU API driver. A WebGPU adapter effectively represents a physical GPU and driver available on the underlying system, in your code.
* A logical device is an abstraction via which an application can access GPU capabilities in a compartmentalized way. Logical devices are required to provide multiplexing capabilities. A physical device's GPU is used by many applications and processes concurrently. Each app needs to be able to access WebGPU in isolation for security and logic reasons.

### The Adapter

Before getting our hand on a **device**, we need to select an **adapter**. The same host system may expose multiple adapters if it has access to multiple physical GPUs. It may also have an adapter that represents an emulated/virtual device. Each adapter advertises a list of optional **features** and **supported limits** that it can handle. These are used to determine the overall capabilities of the system before **requesting the device**.The **adapter** is used to **access the capabilities** of the user’s hardware, which are used to select the behavior of your application among very different code paths. Once a code path is chosen, a device is created with the capabilities we choose. Only the capabilities selected for this device are then allowed in the rest of the application. This way, it is **not** possible to inadvertently rely on capabilities specific to your device.

![Supported Limits](./images/adapter_supported_limits.png "Adapter Supported Limits")

{{% notice Tip %}}
In an advanced use of the adapter/device duality, we can set up multiple limit presets and select one depending on the adapter. In our case, we have a single preset and abort early if it is not supported.
{{% /notice %}}

### Requesting Adapter

An adapter is not something we create, but rather something that we *request* using the function `requestAdapter()`.
But before doing that we need to create an instance by using

```C++
wgpu::Instance instance = createInstance(InstanceDescriptor{});
```

In order to display something on screen, the operating system needs to provide some place to *draw*, this is commonly known as **a window**. The Game Activity provides us with *pApp* member which exposes an Android Window. WebGPU has capability to use an Android Window for rendering. WebGPU cannot use the *window* directly, but uses something called **a surface**, which can be easily created using the window

```C++
wgpu::SurfaceDescriptorFromAndroidNativeWindow platformSurfaceDescriptor = {};
platformSurfaceDescriptor.chain.next = nullptr;
platformSurfaceDescriptor.chain.sType = SType::SurfaceDescriptorFromAndroidNativeWindow;
platformSurfaceDescriptor.window = app_->window; //app_ comes from the game activity
wgpu::SurfaceDescriptor surfaceDescriptor = {};
surfaceDescriptor.label = "surfaceDescriptor";
surfaceDescriptor.nextInChain = reinterpret_cast<const ChainedStruct*>(&platformSurfaceDescriptor);
wgpu::Surface surface = instance.createSurface(surfaceDescriptor);
```

Once a Surface is available, we can request the adapter

```C++
wgpu::RequestAdapterOptions adapterOpts{};
adapterOpts.compatibleSurface = surface;
wgpu::Adapter adapter = instance.requestAdapter(adapterOpts);
```

Now after successful creating adapter, we can query basic information such as the GPU vendor, underlying graphics API, etc.

```C++
wgpu::AdapterInfo adapterInfo;
adapter.getInfo(&adapterInfo);
__android_log_print(ANDROID_LOG_INFO, "NATIVE", "%s", "vendor..");
__android_log_print(ANDROID_LOG_INFO, "NATIVE", "%s", adapterInfo.vendor);
__android_log_print(ANDROID_LOG_INFO, "NATIVE", "%s", "architecture..");
__android_log_print(ANDROID_LOG_INFO, "NATIVE", "%s", adapterInfo.architecture);
__android_log_print(ANDROID_LOG_INFO, "NATIVE", "%s", "device..");
__android_log_print(ANDROID_LOG_INFO, "NATIVE", "%s", adapterInfo.device);
__android_log_print(ANDROID_LOG_INFO, "NATIVE", "%s", "description..");
__android_log_print(ANDROID_LOG_INFO, "NATIVE", "%s", adapterInfo.description);
std::string backend = std::to_string((int)adapterInfo.backendType);
__android_log_print(ANDROID_LOG_INFO, "NATIVE", "%s", "backendType..");
__android_log_print(ANDROID_LOG_INFO, "NATIVE", "%s", backend.c_str());
```

### Creating Device

As described above, in order to create a device that meets the requirements for our application, we need to specify *required limits*. There are few options to set theses limits:

* Choose default limits

```C++
wgpu::RequiredLimits requiredLimits = Default;
```

* Query the Adapter's *supported limits* and use them as *required limits*

```C++
wgpu::SupportedLimits supportedLimits;
adapter.getLimits(&supportedLimits);
wgpu::RequiredLimits requiredLimits = Default;
requireLimits.limits = supportedLimits.limits;
```

* Query the Adapter's *supported limits* and define specific *better* limits in the *required limits*

```C++
wgpu::SupportedLimits supportedLimits;
adapter.getLimits(&supportedLimits);
wgpu::RequiredLimits requiredLimits = Default;
requiredLimits.limits.maxVertexAttributes = 3;
requiredLimits.limits.maxVertexBuffers = 1;
requiredLimits.limits.minStorageBufferOffsetAlignment = supportedLimits.limits.minStorageBufferOffsetAlignment;
requiredLimits.limits.minUniformBufferOffsetAlignment = supportedLimits.limits.minUniformBufferOffsetAlignment;
//Define other limits as required

```

{{% notice Tip %}}
Setting *better* limits may not necessarily be desirable, as doing so may have a performance impact. Because of this, and to improve portability across devices and implementations, applications should generally only request better limits if they may actually require them. It is recommended to read mre about ["Supported Limits"](https://developer.mozilla.org/en-US/docs/Web/API/GPUSupportedLimits) and ["limits"](https://gpuweb.github.io/gpuweb/#limits)
{{% /notice %}}

We then use the `requestDevice()` API to request device:

```C++
wgpu::DeviceDescriptor deviceDesc;
deviceDesc.label = "My Device";
deviceDesc.requiredFeatureCount = 0;
deviceDesc.requiredLimits = &requiredLimits;
deviceDesc.defaultQueue.label = "The default queue";
wgpu::Device device = adapter.requestDevice(deviceDesc);
__android_log_print(ANDROID_LOG_INFO, "NATIVE", "%s", "Got device");
static auto errorCallback = device.setUncapturedErrorCallback([](ErrorType type, char const* message) {
    __android_log_print(ANDROID_LOG_ERROR, "NATIVE", "%s", "Got device error");
    __android_log_print(ANDROID_LOG_ERROR, "NATIVE", "%s", "error type:");
    std::string t = std::to_string((int)type);
    __android_log_print(ANDROID_LOG_ERROR, "NATIVE", "%s", t.c_str());
    __android_log_print(ANDROID_LOG_ERROR, "NATIVE", "%s", "error message:");
    __android_log_print(ANDROID_LOG_ERROR, "NATIVE", "%s", message);
});
```

{{% notice Tip %}}
While creating device, we are using a callback function `setUncapturedErrorCallback`, this helps in capturing validation and other errors with the WebGPU device. It is highly recommended to set the callback.
{{% /notice %}}
