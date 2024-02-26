---
title: Why Interrupts
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Disadvantages of looping
In the previous learning path, [Embedded programming with the Raspberry Pi Pico](), we created a simple motion detector using a PIR sensor and a Raspberry Pi Pico. 

In that example we used the Arduino `loop()` function to check on the state of the PIR sensor multiple times per second. We also had to store state between checks so that our program would know when it had changed. And while this approach is conceptually very simple and familiar to application developers, it does have some significant disadvantages in the resource constrained world of microcontrollers and embedded systems.

For starters our program had to keep running, constantly checking for a change in the PIR sensor. It never had the opportunity to enter a low-power state. In application development this isn't usually a concern, you have plenty of electricity available to run your program and a little excess CPU use doesn't cost you anything. But if your application is running on a device with a small battery, sometimes even a non-rechargeable one, excess CPU use reduces the life expectancy of your device.

The other disadvantage is complexity. Sure this example was simple from an application developer's perspective, but from a microcontroller perspective it could be even simpler. All of the work our software is doing to maintain state information between checks of the PIR sensor, just to know when the state of the sensor has changed, can be handled by the hardware itself instead. Instead of checking what the state is on every iteration of the loop, all we need to know is when that state has changed.

## Introducing Interrupts
As the name implies, an interrupt is something that can "interrupt" the running program. It's a way to make your CPU pause execution of once piece of code, begin executing another, and finally returning to the original piece of code and continuing exection where it left off. This can be done without threading, or concurrency, or adding mutexes to your code, because the CPU makes sure that nothing else will change while the interrupt code is running. It may sound like more advanced programming, but in reality it makes things much simpler.

To use an interrupt, you first have to define an interrupt handler. If you've used event handlers and callbacks in application development you'll find these to be very familiar. An interrupt handler is just a function that contains the code you want to run when the interrupt condition happens. Again, nothing else will be running when your interrupt function is running, so you don't need to have event threads or concurrency checking. 

## Things do consider
What you do need to do, however, is make sure that your interrupt code is as small and as fast as possible. Because, again, nothing else can run while your interrupt handler is running, you want to make sure that it finishes quickly so your main application can resume. To that end you should only use interrupt code to change the state of your application, not to respond to that changed state. Leave the response to your main code, in our example that would be the `loop()` function of our Arduino sketch.

Another thing to be aware of is what you can't do in your interrupt code. Since nothing else runs, not even in the background, you can't make calls to something like `delay()`, that function relies on updates to the system clock, but the system clock isn't being updated while your interrupt code is running. If you do call `delay(1000)` in your interrupt code, it will **never** return, because it won't ever see that the system clock advanced by one second, and your interrupt code will freeze your whole device.

Likewise you can't read or write to your `Serial` console in interrupt code, because those functions rely on background execution handling that communication, and that background execution won't be running while your interrupt code is running. More complex interfaces, like I2C or SPI, are also unable to function from within your interrupt handler.

## Refactoring
Now, with all that out of the way, let's go back to the example code running our motion detector and see how to get the same functionality with less code using interrupts.
