---
title: Learn about interrupts
weight: 8

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Disadvantages of looping

So far, you have used the Arduino `loop()` function to check the state of the PIR sensor multiple times per second. You have also had to store the state between checks so that the program knows when the state changes. While this approach is conceptually very simple and familiar to application developers, it does have some significant disadvantages in the resource constrained world of microcontrollers.

For starters, the program must keep running, constantly checking for a change in the PIR sensor. It never has the opportunity to enter a low-power state. In application development this isn't usually a concern, as a little excess CPU usage doesn't cost anything. But if your application is running on a device with a small battery, sometimes even a non-rechargeable one, excess CPU usage reduces the life expectancy of your device.

The other disadvantage is complexity. This example is simple from an application developer's perspective but from a microcontroller perspective, it could be even simpler. All the work the software does to maintain state information between checks of the PIR sensor can be handled by the hardware itself. Instead of checking the state on every iteration of the loop, you just need to know when the state has changed.

## Introducing interrupts

As the name implies, an interrupt is something that can "interrupt" the running program. It's a way to make your CPU pause execution of one piece of code, begin executing another, and finally return to the original piece of code and continue executing where it left off. This can be done without threading, concurrency or adding mutexes to your code because the CPU makes sure that nothing else will change while the interrupt code is running. It may sound like advanced programming but in reality, it makes things much simpler.

To use an interrupt, you first have to define an interrupt handler. If you've used event handlers and callbacks in application development, you'll find these to be very familiar. An interrupt handler is just a function that contains the code you want to run when the interrupt condition happens. Again, nothing else will be running when your interrupt function is running, so you don't need to have event threads or concurrency checking. 

## Things to consider

You do need to make sure that your interrupt code is small and fast because nothing else can run while your interrupt handler is running. Therefore, you want to make sure that it finishes quickly so your main application can resume. You should only use the interrupt handler to change the state of your application, not to respond to that changed state. Leave the response to your main code. In the example this would be the `loop()` function of the Arduino sketch.

Another thing to be aware of is what you can't do in your interrupt code. Since nothing else runs, not even in the background, you can't make calls to `delay()` because this relies on updates to the system clock but the system clock isn't being updated while your interrupt code is running. If you do call `delay(1000)` in your interrupt code, it will **never** return because it won't ever see that the system clock advanced by one second, and your interrupt code will freeze your whole device.

Likewise you can't read or write to your `Serial` console in interrupt code because those functions rely on background execution, and that background execution won't be running while your interrupt code is running. More complex interfaces, like I2C or SPI, are also unable to function from within your interrupt handler.

With this introduction to interrupts, you can revisit the example code for the motion detector and see how to get the same functionality with less code using interrupts.
