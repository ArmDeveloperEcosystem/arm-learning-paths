---
title: Adding Interrupt Code
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Removing state
Previously we used two variables to keep track of what the current value of the PIR sensor was, and what the previous value was, so that we could compare them to identify a change in state that we wanted our code to respond to:

```arduino {linenos=table,linenostart=12}
// This variable will hold the current value of the motion detection pin's charge
// LOW means no motion is detected, HIGH means motion is detected
int motionState = LOW;

// This variable will hold the read value on each iteration of the loop
int val = 0;
```

In our new code we don't have to keep track of state, only if it has changed. So we can replace those two variables with just one:
```arduino {linenos=table,linenostart=12}
// This variable tells us if motion triggered the interrupt
bool motionDetected = false;
```

## Interrupt handler
The next thing we need to do is write our interrupt handling code. An interrupt handler is just a function in Arduino. Importantly, this function does not take any arguments, and it doesn't return in value.

```arduino
void motion_detected() {
  motionDetected = true;
}
```

Remember that your interrupt handler should be as small and fast as possible. All we need it to do is change the value of the `motionDetected` variable, it doesn't get much smaller or faster than that!

## Triggering an interrupt
Now that we have our handler function in place, we need to tell our device when to call it. To do that, in our `setup()` function, we need to add this line:

```arduino
attachInterrupt(digitalPinToInterrupt(motionPin), motion_detected, RISING);
```

The `attachInterrupt` function takes three arguments: the interrupt number, the interrupt handler function, and the interrupt condition. Let's take a look at each of them.

### Interrupt number
Depending on our CPU there can be any number of things that can trigger an interrupt. The CPU gives each of these a number, and you'd need to look at the documentation for your specific device to know which number corresponds to which trigger. But in our Arduino sketch we can use the `digitalPinToInterrupt()` function to lookup the interrupt number for a given pin, such as our `motionPin` variable.

### Interrupt handler
This is just a reference to your function. Be sure to use just the name as your function here, don't put `()` after it, that would execution the funcitona and pass its return value to `attachInterrupt`, which isn't what we want.

### Interrupt condition
Depending on your hardware there may be different conditions that can be used to trigger an interrupt. Arduino typically supports `CHANGE`, `FALLING` and `RISING` to trigger based on changes to the pin's input voltage: `FALLING` for a change from `HIGH` to `LOW`, `RISING` for a change from `LOW` to `HIGH`, and `CHANGE` for a change in either direction. 

Since we only want to do something when the PIR sensor changes from  `LOW` to `HIGH`, we use the `RISING` condition.