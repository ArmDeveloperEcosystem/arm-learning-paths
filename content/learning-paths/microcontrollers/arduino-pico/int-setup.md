---
title: Add the interrupt code
weight: 9

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Remove state

Previously, you used two variables to keep track of the current value and the previous value of the PIR sensor. 

The variables were used to identify a change in state that needs a response: 

```arduino {linenos=table,linenostart=12}
// This variable will hold the current value of the motion detection pin's charge
// LOW means no motion is detected, HIGH means motion is detected
int motionState = LOW;

// This variable will hold the read value on each iteration of the loop
int val = 0;
```

The new code does not need to keep track of the state, only if the state changes.

You can replace the two variables with just one:

```arduino {linenos=table,linenostart=12}
// This variable tells us if motion triggered the interrupt
bool motionDetected = false;
```

## Interrupt handler

The next thing to do is write the interrupt handling code. 

An interrupt handler is just a function in Arduino. Importantly, this function does not take any arguments and it doesn't return a value.

```arduino
void motion_detected() {
  motionDetected = true;
}
```

Remember that your interrupt handler should be small and fast. All you need to do is change the value of the `motionDetected` variable, it doesn't get much smaller or faster than that!

## Triggering an interrupt

Now that the handler function is in place, you need to tell the device when to call it. To do that, add the line below to the `setup()` function:

```arduino
attachInterrupt(digitalPinToInterrupt(motionPin), motion_detected, RISING);
```

The `attachInterrupt` function takes three arguments: 
- the interrupt number
- the interrupt handler function
- the interrupt condition

The arguments are described in the next three sections.

### Interrupt number

Depending on the CPU, there can be a number of things that can trigger an interrupt. The CPU gives each of these a number and you need to look at the documentation for your specific device to know which number corresponds to which trigger. In this Arduino sketch, you can use the `digitalPinToInterrupt()` function to look up the interrupt number for a given pin, such as the `motionPin` variable.

### Interrupt handler

This is a reference to your function. Be sure to use the function name and don't put parentheses after it or else it will execute the function and pass the return value to `attachInterrupt`, which isn't what you want.

### Interrupt condition

Depending on your hardware there may be different conditions that can be used to trigger an interrupt. Arduino typically supports `CHANGE`, `FALLING` and `RISING` to trigger interrupts based on changes to the pin's input voltage: 
- `FALLING` for a change from `HIGH` to `LOW`
- `RISING` for a change from `LOW` to `HIGH`
- `CHANGE` for a change in either direction

Use the `RISING` condition because you only want to do something when the PIR sensor changes from  `LOW` to `HIGH`. 

Continue to the next section to see the updated application code. 
