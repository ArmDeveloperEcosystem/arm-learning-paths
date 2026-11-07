---
title: Interpret wasmCloud HTTP benchmark results
description: Interpret your HTTP timing and load-test measurements and learn how wasmCloud instance pooling and concurrency settings affect throughput.
weight: 6

layout: learningpathall
---

## Connect the numbers to the application

The application that you measured performs little work beyond returning a greeting.
Its results describe the HTTP hosting path on your Graviton-based system. An
application that queries a database, transforms a large payload, or performs
substantial computation will have different behavior.

Use your measurements to answer the following questions:

- Does the ready application return successful responses consistently?
- How does response latency change when you increase concurrent connections?
- Does throughput increase, and are the resulting latencies acceptable?

One small application can handle many requests. The number of connections,
requests, guest instances, and independently hosted applications are different
quantities.

## wasmCloud HTTP handler benchmark

wasmCloud publishes a benchmark for its HTTP handler in [wasmCloud benchmark scripts](https://github.com/wasmCloud/wasmCloud/tree/main/scripts/bench). On an 8-core Neoverse V2 system, hot invocations complete in hundreds of microseconds. HTTP throughput reaches tens of thousands of requests per second. 

Your `wrk` measurements use a different load client and measurement boundary, so the numbers aren't directly comparable. However, the published benchmark describes the same hosting path.

## Warm instance pooling and concurrency

Some applications do expensive setup before they can handle useful work. Keeping
an initialized instance warm avoids repeating that setup on every request.
Applications that spend time waiting can also benefit from overlapping requests when the runtime and component support it.

wasmCloud lets you configure a pool of warm instances (`poolSize`) and allows each
instance to handle multiple calls simultaneously (`maxConcurrency`). Total warm
capacity becomes `poolSize × maxConcurrency` in-flight calls. 

The wasmCloud 2.7 release measured roughly a 13.6-times improvement in concurrent throughput when concurrent
pooling was enabled. This improvement was observed for workloads with
significant initialization cost or I/O waiting.

For results across releases, see the [wasmCloud benchmark site](https://wasmcloud.github.io/arewefastyet/).

You didn't configure these policies in the sample greeting application. The concept
matters when you move to a workload with real initialization cost or concurrency.
Measure your application before choosing a policy.

## What wasmCloud provides

wasmCloud provides a way to package application logic as WebAssembly components
and host those components with shared runtime capabilities. For developers,
this separates handler business logic from the machinery that listens
for requests and provides infrastructure access. For operators, workload and
instance policies offer readiness, concurrency, and resource use choices.

The practical value depends on your workload. You can build and run a component on Graviton and observe its HTTP
performance. It doesn't measure a maximum application count, memory savings
against containers, or a performance advantage over native services.

## What you've learned

You've learned how to interpret warm response time and throughput results. You've also learned how wasmCloud instance pooling and concurrency settings affect throughput.

You can now extend the Learning Path with a more representative application and judge its
behavior using your own requirements.
