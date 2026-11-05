---
title: Understand the results
description: Interpret your curl and wrk measurements and learn how wasmCloud instance pooling and concurrency settings affect throughput.
weight: 6
layout: learningpathall
---

## Connect the numbers to the application

The application you measured performs little work beyond returning a greeting.
Its results describe the HTTP hosting path on your Graviton system. An
application that queries a database, transforms a large payload, or performs
substantial computation will have different behavior.

Use your measurements to answer these questions:

- Does the ready application return successful responses consistently?
- How does response latency change when you increase concurrent connections?
- Does throughput increase, and are the resulting latencies acceptable?

One small application can handle many requests. The number of connections,
requests, guest instances, and independently hosted applications are different
quantities.

## A reference point from the Graviton benchmark

wasmCloud publishes a benchmark for its HTTP handler in the [wasmCloud benchmark scripts](https://github.com/wasmCloud/wasmCloud/tree/main/scripts/bench). On an 8-core Neoverse V2 system, hot invocations complete in hundreds of microseconds and HTTP throughput reaches tens of thousands of requests per second. Your `wrk` measurements use a different load client and measurement boundary, so the numbers aren't directly comparable, but they describe the same hosting path.

## Warm instance pooling and concurrency

Some applications do expensive setup before they can handle useful work. Keeping
an initialized instance warm avoids repeating that setup on every request.
Applications that spend time waiting, for example on an external service, can
also benefit from overlapping requests when the runtime and component support it.

wasmCloud lets you configure a pool of warm instances (`poolSize`) and allow each
instance to handle multiple calls simultaneously (`maxConcurrency`). Total warm
capacity becomes `poolSize × maxConcurrency` in-flight calls. For workloads with
significant initialization cost or I/O waiting, the wasmCloud 2.7 release
measured roughly a 13.6× improvement in concurrent throughput when concurrent
pooling was enabled. The [wasmCloud benchmark site](https://wasmcloud.github.io/arewefastyet/)
tracks these results across releases.

You didn't configure those policies in the greeting application. The concept
matters once you move to a workload with real initialization cost or concurrency.
Measure your application before choosing a policy.

## What wasmCloud provides

wasmCloud provides a way to package application logic as WebAssembly components
and host those components with shared runtime capabilities. For developers,
this separates the handler's business logic from the machinery that listens
for requests and provides infrastructure access. For operators, workload and
instance policies offer choices about readiness, concurrency, and resource use.

The practical value depends on your workload. You can build and run a component on Graviton and observe its HTTP
performance. It does not measure a maximum application count, memory savings
against containers, or a performance advantage over native services.

## Clean up

Stop `wash dev` with Ctrl+C in its terminal. Stop any SSH tunnel you opened.
Keep the application source and results if you want to repeat the tests.
When finished with your AWS instance, stop or terminate it according to your
normal AWS workflow to avoid continued charges.

## What you've accomplished

You have built and changed a WebAssembly HTTP component, hosted it on an Arm
server with wasmCloud, and measured warm response time and throughput. You can
now use the same sequence with a more representative application and judge its
behavior using your own latency and throughput requirements.
