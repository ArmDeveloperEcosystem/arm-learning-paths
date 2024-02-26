---
title: Refactoring Your Application
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Responding to state change
Previously our `loop()` code had to perform multiple checks. First it had to read the current state of the PIR sensor into `val`, then it had to compare that to the previous state stored in `motionState`, and then finally it had to do something different depending the four possible combinations of values for those two variables.

Now, however, we just need to worry about one:

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

As you can see, our nested if/else blocks have all been replaced by a single check: `if (motionDetected)`. If it's true then we call our helper functions `ledOff()`, `doBeep()`, and `ledOn()`, increment our counter, and write the new value out to the serial console, just as we need before. 

You'll notice that we don't need our "cooling off" code anymore. That's because the `RISING` interrupt won't happen again until the PIR sensor has cooled off, returing `motionPin` to a `LOW` state.

Finally, we do have to set `motionDetected = false` here, since we've handled that event.

## Conclusion
That's it! That's all there is to using interrupts in our code. You can see how much smaller and simpler the use of interrupts makes things, even for an example that was small and simple to begin with.

Not only that, but using interrupts makes other improvements possible. For example, we could stop the `loop()` and put our device into a very low-power state while no motion is detected, and let the interrupt power it back up to respond. But that's a subject for another learning path.

You can download the complete [pir_sensor.ino](./pir_sensor_2.ino) and try it out yourself.