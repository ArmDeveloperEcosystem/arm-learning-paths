
// This is the pin that the motion sensor is connected to
int motionPin = 28;

// This is the pin that the buzzer is connected to
int buzzerPin = 19;

// This is the pin that connects to the build-in LED
int ledPin = 25;


// This variable tells us if motion triggered the interrupt
bool motionDetected = false;

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

void motion_detected() {
  motionDetected = true;
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

  attachInterrupt(digitalPinToInterrupt(motionPin), motion_detected, RISING);
  Serial.println("Beginning motion detection");
}


void loop() {
  // put your main code here, to run repeatedly:
  
  if (motionDetected) {
    // First we write to the USB console that motion was detected
    Serial.println("Motion Detected!");
  
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