---
title: Performance analysis concepts
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Performance analysis concepts

Arm Neoverse™ CPUs provide cloud and server workloads with an energy efficient computing platform. These systems give high application performance and an excellent operational price-performance ratio. To maximize performance, you can tune your software for the underlying hardware. To do this effectively, you need high quality performance data from the hardware, and performance analysis tooling to capture and interpret it.

The Streamline CLI tools are native command-line tools that are designed to run directly on an Arm server running Linux. The tools provide a software profiling methodology that gives you clear and actionable performance data. You can use this data to guide the optimization of the heavily used functions in your software.

Profiling with the Streamline CLI tools is a three-step process:

1. Capture the raw sampled data for the profile.
2. Analyze the raw sampled data to create a set of pre-processed function-attributed performance counters and metrics.
3. Format the pre-processed metrics into a pretty-printed human-readable form.

## Understanding performance

A simple formula for understanding the performance of a software application is:

Delivered performance = Utilization × Efficiency × Effectiveness

_Utilization_ measures the proportion of the total processor execution capacity that is spent processing instructions. This is a measure of the hardware
performance.

_Efficiency_ measures the proportion of the used processor execution capacity that is spent processing useful instructions, and not instructions that are speculatively executed and then discarded. This is a measure of the hardware performance.

_Effectiveness_ measures the implementation efficiency of the software algorithm, compared to a hypothetical optimal implementation. This is a measure of the software performance.

To get the best performance you must implement an effective software algorithm, and then achieve high processor utilization and execution efficiency when running it.

## Abstract CPU model

The processing core of a modern Arm CPU is represented in this methodology as
an abstract model consisting of 3 major phases, Frontend, Backend and Retire.

![An abstract CPU block diagram](images/abstract-cpu-pipeline.svg)

We define the available performance of the core using the maximum number of
micro-operations (micro-ops) that can be issued to the backend each clock
cycle. This execution width is known as the issue slot count of the processor.

This simple model does not include a lot of detail. For the purposes of
optimizing software, most of the low-level microarchitecture is not that
important because software has little control over code execution at that
level.

### Frontend

The frontend phase represents instruction fetch, decode, and dispatch. This
phase handles fetching instructions from the instruction cache, decoding those
instructions, and adding the resulting micro-ops to the backend execution
queues.

Each CPU frontend microarchitecture exposes a fixed number of decode slots that
can decode instructions into micro-ops each cycle. The main goal of the
frontend is to keep these decode slots busy decoding instructions, unless
there is back-pressure from the backend queues because the backend is unable
to accept new micro-ops.

The frontend also implements support for branch prediction and speculative
execution. Predicting where program control flow goes next allows the frontend
to keep the backend queues filled with work when execution is uncertain.
However, incorrect predictions cause the cancellation of issued micro-ops on
the wrong path, and the pipeline might take time to refill with new micro-ops.

### Backend

The backend phase represents the execution of micro-ops by the processing
pipelines inside the core. There are multiple pipeline types, each of which can
process a subset of the instruction set, and be fed by their own issue queues.

An application will have uneven loading on the backend queues. Queue load
depends on the instruction mix in the part of the code that is currently
running. When optimizing your application, try to prioritize changes that will
relieve pressure on the most heavily loaded queue.

### Retire

The retire phase represents the resolution of micro-ops that are
architecturally complete. Measuring the number of retired instructions gives a
metric showing the amount of useful work completed by the processor.

Not all issued instructions will retire. Speculatively issued micro-ops will be
cancelled if they are shown to be on the wrong code path and are therefore not
required.

## Next steps

Using the abstract CPU model, we can define some optimization goals, and associate these with behaviors in the three pipeline stages.
