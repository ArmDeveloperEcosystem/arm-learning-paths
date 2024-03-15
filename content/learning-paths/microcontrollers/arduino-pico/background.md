---
# User change
title: "About Embedded Programming"

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## What is Embedded Programming?

For a long time application development and embedded programming have lived in different worlds, they had different tools and stacks and patterns, and it was rare for somebody to go from one to the other.

The arrival of smart connected devices, whether it be the Internet of Things (IoT), smart cities, smart cars or even smart watches, has blurred the line between application and embedded spaces. This opens the door for application developers to enter the exciting space of embedded devices but, because of that prior separation, you might feel like you don't have the knowledge or skills needed to make that leap.

That's where this Learning Path comes in. Here you will learn about the key differences between application and embedded development and how to leverage your knowledge of application development in this space. There are also hands-on, practical projects that will provide a solid foundation for your journey into embedded software development.

## Mindset, not skillset

The good news is that, fundamentally, there are no differences between the code you would write for embedded devices and the code you would write for an application. Everything that you know about variables, flow control, functions, call stacks, and data structures will be used the same way in embedded programming. Your embedded program has an entry point, like `main()`, and from there it will run whatever code you tell it to run, just like you're used to.

The biggest change you need to make is to your mindset and thinking more about your physical hardware and environment. 

## Resource constraints

Application developers have had the luxury of abundance and abstraction when it comes to resources. Today, even on mobile you'll have gigabytes of memory and CPUs running at several gigahertz at your disposal. On a microcontroller, however, your code may need to fit in just a few hundred **kilobytes** of RAM and execute at a few hundred **megahertz** on the CPU.

It's not as dire is at sounds though. The tools, software, and libraries that have been built for embedded development will help you. Instead of a heavy operating system intended to support any hardware, you'll be using one that's been tailored for your specific device. The libraries you use, rather than trying to do as much as possible, have been designed to use the minimum amount of resources. You generally won't be sharing your resources with other applications as embedded systems tend to do one thing at a time (although this is changing with the advent of smart devices).

## Environment interface

Another big difference is that your interactions will be with the physical environment more than with a user. Don't expect to have mouse or touch events to drive your interactions. Most embedded programming won't even have a graphical interface to speak of. 

What you will have are sensors that will tell you about your physical environment: the temperature, pressure, level of noise or vibration, distance, speed, etc. You'll also have the ability to change things in your physical environment, with lights, motors, electrical relays, valves, etc. All of this your embedded program will do without any human interaction at all.

## In real-time

Lastly, the timing of your code's execution is going to be subtly different than it is for an application. You always want your code to be responsive and "fast" but that takes on a whole new meaning with embedded devices where milliseconds matter.

You know that when a user clicks on a button in your application, it will trigger some piece of your code to run. Eventually. But before that happens, the click "event" has to make it's way through the operating system's abstractions, wait for your application's process to be scheduled time on the CPU, and then eventually make it's way into the event thread of toolkit or webserver, before finally getting to your code.

This all takes too long when your embedded device is controlling a piece of heavy equipment or critical infrastructure. Instead, your embedded programming environment is going to make use of interrupts, ways of executing code immediately when something happens in the physical environment. Interrupts let your code preempt anything else running on the device and respond immediately to that change. The drawback of this is that, because nothing else can happen while your code is executing (not even the ticking of the system's clock) you have to make sure that it does whatever it needs to do as quickly as possible.
