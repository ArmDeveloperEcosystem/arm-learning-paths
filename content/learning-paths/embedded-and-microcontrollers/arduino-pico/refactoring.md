---
title: Refactor the application
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Responding to state change

Previously the `loop()` code had to perform multiple checks. 

First, it had to read the current state of the PIR sensor into `val`, then it had to compare the current state to the previous state stored in `motionState`, and finally it had to do something different depending on the four possible combinations of values for the two variables.

Now, there is just one variable to consider. The updated `loop()` function is below: 

```arduino
void loop() {
  // put your main code here, to run repeatedly:

  // Every iteration of the loop has a half-second delay, this reduces the processing load on the device
  delay(500);
  
  if (motionDetected) {
    Serial.println("Motion Detected!");
  
    // First we write to the USB console that motion was detected
    Serial.println("Motion detected");
    // Next we turn the LED off, indicating that we're not longer in the waiting state
    ledOff();
    // Then we trigger the beep
    doBeep();
    // And increment our counter
    counter++;
    Serial.print("Counter is now at ");
    Serial.println(counter);
    
    // Turn the LED back on, indicating that we're re-entering a waiting state
    ledOn();
    // Finally we save the fact that we've handled this motion event
    motionDetected = false;

  }

}
```

As you can see, the nested if/else blocks have been replaced by a single check, `if (motionDetected)`. If it's true, call the helper functions `ledOff()`, `doBeep()`, and `ledOn()`, increment the counter, and write the new value to the serial console. 

You'll notice that you don't need the "cooling off" code anymore. That's because the `RISING` interrupt won't happen again until the PIR sensor has cooled off, returning `motionPin` to a `LOW` state.

Finally, you do have to set `motionDetected = false` because the event has been handled.

## Conclusion

That's it! You have learned how to use interrupts. You can see how much smaller and simpler the use of interrupts makes things, even for an example that was small and simple to begin with.

Not only that but using interrupts makes other improvements possible. For example, you could stop the `loop()` and put the device into a very low-power state while no motion is detected, and let the interrupt power it back up to respond.

You can download the complete [pir_sensor.ino](/learning-paths/embedded-and-microcontrollers/arduino-pico/pir_sensor_2.ino) and try it out yourself.
