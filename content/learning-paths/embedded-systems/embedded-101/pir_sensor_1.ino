
// This is the pin that the motion sensor is connected to
int motionPin = 28;

// This is the pin that the buzzer is connected to
int buzzerPin = 19;

// This is the pin that connects to the build-in LED
int ledPin = 25;


// This variable will hold the current value of the motion detection pin's charge
// LOW means no motion is detected, HIGH means motion is detected
int motionState = LOW;

// This variable will hold the read value on each iteration of the loop
int val = 0;

// This variable will keep track of how many times motion has been detected
int counter = 0;


// Beep the buzzer twice in quick succession
void doBeep() {
      digitalWrite(buzzerPin, HIGH); // On for 0.1 seconds
      delay(100);
      digitalWrite(buzzerPin, LOW); // Off
      delay(100);
      digitalWrite(buzzerPin, HIGH); // On for 0.2 seconds
      delay(200);
      digitalWrite(buzzerPin, LOW); // Off
}

// Turn on the built-in LED
void ledOn() {
  digitalWrite(ledPin, HIGH);
}

// Turn off the built-in LED
void ledOff() {
  digitalWrite(ledPin, LOW);
}


void setup() {
  // Here we tell the board whether a pin will be used for reading (INPUT) or writing (OUTPUT)
  
  // This lets us write text over the USB connection to the Arduino IDE
  Serial.begin(9600);

  // We will read values from the motion sensor
  pinMode(motionPin, INPUT);
  
  // We will write values to the buzzer
  pinMode(buzzerPin, OUTPUT);

  // We will write values to the built-in LED
  pinMode(ledPin, OUTPUT);
  // We default to having the LED on, indicating a ready state
  ledOn();

  Serial.println("Beginning motion detection");
}


void loop() {
  // put your main code here, to run repeatedly:

  // Every iteration of the loop has a half-second delay, this reduces the processing load on the device
  delay(500);

  // In every iteration of the loop we start by checking the current value from the PIR sensor
  val = digitalRead(motionPin);

  // A HIGH value means the sensor is detecting motion, so we do our motion-handling
  if (val == HIGH) {

    // If we had previously been in a LOW state (no motion) then this is a new detection!
    if (motionState == LOW) { 
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
      // Finally we save the fact that we're in a motion detecting state
      motionState = HIGH;

    // If we had previously been in a HIGH state (motion detected) then we're seeing the same motion event we've already handled
    } else {
      // PIR sensors can retain a HIGH state for several seconds after motion has stopped
      // So we're adding in a 10 second cooling off period to let it return to a LOW state
      Serial.println("Waiting for sensor to cool-off");
      delay(5000);
    }

  // A LOW value means the sensor isn't detecting motion, so we enter a waiting state
  } else {

    // If we had previously been in a HIGH state, that means the PIR sensor has stopped registing motion
    if (motionState == HIGH) {

      // We save the fact that we're not in a non-motion detecting state
      motionState = LOW;
      // Next we turn on the LED to indicate that we've entered the motion detecting state
      ledOn();
      // Finally we write to the USB console that we're ready to detect motion
      Serial.println("Ready for detection");
      Serial.println();
    }
  }

}
