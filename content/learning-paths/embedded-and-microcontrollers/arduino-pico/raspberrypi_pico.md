---
# User change
title: "Build a smart device prototype"

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Build your first device

To get started on your first embedded project, you can use a cheap and widely available device: the [Raspberry Pi Pico](https://www.raspberrypi.com/products/raspberry-pi-pico/).

![Photo of a Raspberry Pi Pico development board showing its compact rectangular shape with dual rows of GPIO pins along both edges and a micro-USB port. The board features an RP2040 microcontroller with dual Cortex-M0+ cores, the same chip used in Arduino Nano RP2040, making it compatible with Arduino core packages.#center](_images/raspberry_pi_pico.jpg)

You were probably expecting an Arduino board, rather than a Raspberry Pi board but it turns out that the Arduino core package that supports the Arduino Nano RP2040 will also support the Raspberry Pi Pico, because they use the exact same RP2040 microprocessor. Plus the Pico is less expensive, currently retailing for less than $5 USD (you can also use the Raspberry Pi Pico with other programming environments, such as MicroPython).

## Accessories

For interacting with the physical world you can use two cheap commodity components. 

![Diagram showing PIR motion sensor pinout with three pins labeled from left to right: VCC for power input, OUT for data signal output that goes high when motion is detected, and GND for ground. Understanding this pinout is essential for wiring the sensor correctly to the Pico's 3.3V power, ground, and GPIO pins.#center](_images/pir-sensor-pinout.png)

First a PIR motion sensor. This sensor reacts to infrared photons emitted by a warm moving object, like a person or animal. The interface is simple, it has one pin for input voltage, one pin for ground to complete the circuit, and a third pin that will have the same voltage as the input pin when motion is detected, and the same voltage as the ground pin when it isn't.


![Diagram showing piezo-electric buzzer pinout with two terminals: a positive terminal marked with a plus sign that connects to a GPIO pin for signal input, and a negative terminal that connects to ground. When voltage is applied to the positive terminal, the buzzer emits a high-pitched beep to signal motion detection.#center](_images/buzzer-pin-diagram.png.webp)

Second, a very simple electric buzzer. You could get fancy with one of these and make it play different sounds with something called Pulse Width Modulation (PWM) but, for simplicity, you can give it a constant voltage which will result in a high-pitched beeping noise.

![Diagram showing standard solderless breadboard layout with color-coded connection patterns. Holes in each column are connected vertically, while the center divider isolates left and right sides. Power rails along the edges run horizontally for distributing voltage and ground. This layout allows you to connect multiple components to the same Pico pins by plugging wires into holes on the same connected column.#center](_images/breadboard.jpeg)

Finally, you can use a breadboard to connect the components together without having to do any soldering.

If you're not familiar with a breadboard, the image above shows you how all of the little holes are connected together. When you plug a wire into a hole, it connects it to every other hole on the same connected line. This configuration lets you connect multiple components to the same pin on your development board.

## Assemble your system

### Step 1: Seat your Raspberry Pi

![Photo showing Raspberry Pi Pico seated on a breadboard with its dual rows of GPIO pins straddling the center divider. This placement ensures that each pin has its own column of connected holes on either side, allowing you to wire components to the Pico's GPIOs without creating short circuits across pins.#center](_images/pico_on_breadboard.webp)

Seat your Raspberry Pi Pico on the breadboard so that its rows of pins sit on either side of the center divider. Make sure that it's firmly pressed all the way down but be careful not to bend any of the pins.

### Step 2: PIR ground

![Photo showing a black jumper wire connecting the PIR sensor's ground pin to physical pin 38 on the Raspberry Pi Pico. Pin 38 is one of the Pico's ground pins that completes the circuit for powering the PIR sensor. Using black wire for ground connections is a common convention that makes circuits easier to troubleshoot.#center](_images/pir_sensor_1.webp)

Using a black jumper wire, connect the ground pin of your PIR sensor to pin #38 on your Pico. This pin is a ground voltage pin on the Pico.

### Step 3: PIR input voltage

![Photo showing a red jumper wire connecting the PIR sensor's VCC power pin to physical pin 36 on the Raspberry Pi Pico. Pin 36 provides 3.3V output to power the PIR sensor. Using red wire for voltage connections follows standard wiring conventions and helps distinguish power connections from ground and signal lines.#center](_images/pir_sensor_2.webp)

Using a red wire, connect the input voltage pin of your PIR sensor to pin #36 on your Pico. This pin is a 3.3 volt pin on the Pico and will supply power to your PIR sensor.

### Step 4: PIR data

![Photo showing a jumper wire connecting the PIR sensor's data output pin to physical pin 34 on the Raspberry Pi Pico. This pin corresponds to GPIO 28, which your code will monitor to detect when the PIR sensor signals motion. Note the distinction between physical pin numbering and GPIO numbering, which is important when writing your Arduino sketch.#center](_images/pir_sensor_3.webp)

The last step to connecting the PIR sensor is to connect the middle data pin to pin #34 on your Pico. This is a GPIO pin that you can use to either read or write data. 

Note that this is GPIO #28, even though it's physical pin #34. Physical pin number and GPIO numbers are not the same.

### Step 5: Buzzer ground

![Photo showing a jumper wire connecting the piezo-electric buzzer's negative terminal to physical pin 23 on the Raspberry Pi Pico. Pin 23 is a ground pin that completes the buzzer circuit. With both ground and power connections in place, the buzzer will emit a tone when the GPIO pin provides voltage to signal detected motion.#center](_images/piezo_1.webp)

Next, it's time to connect the buzzer. Start by connecting the buzzer's ground pin to pin #23 on your Pico. This is another ground pin that is build into your board.

### Step 6: Buzzer input

![Photo showing a jumper wire connecting the piezo-electric buzzer's positive terminal to physical pin 25 on the Raspberry Pi Pico. This pin corresponds to GPIO 19, which your Arduino code will control to trigger the buzzer when motion is detected. By setting this GPIO pin high, you provide voltage that causes the piezo element to vibrate and emit a beep.#center](_images/piezo_2.webp)

Then, connect the buzzer's input pin to pin #25 on your Pico. This is another GPIO pin, this time GPIO #19.

### Review

Your physical device is now assembled and ready. 

Here is a review:

The motion sensor is connected to power, ground, and GPIO #28, which is where you will read the motion state from.

The buzzer is connected to ground and GPIO #24, which is what you will use to turn it on and off.

Now it's time to start programming!
