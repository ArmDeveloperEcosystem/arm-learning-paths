---
title: Initial Setup
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install Raspberry Pi OS

Install Raspberry Pi Imager from [RaspberryPi.com](https://www.raspberrypi.com/software/) and start it up

1. Select your Raspberry Pi device, in my case Raspberry Pi 5
2. Under Operating System, choose Raspberry Pi OS (64-bit)
3. Under Storage, select your microSD card
4. Click Next
5. When it asks you "Would you like to apply OS customization settings?" select Edit Settings
6. Check Set username and password, Configure wireless LAN, and Set locale settings, and enter the appropriate settings
7. After clicking Save, click Yes
8. Click yes to tell it to erase the card

## Insert the microSD card into the Raspberry Pi and power it on

*Even though I set the Wireless LAN when writing to the SD card it typically needs to be manually connected in the desktop settings when first logged on. This may not happen to you, but it's just something to be aware of.*

**Open the terminal and update the device.**

*Note: I've had an issue with this Raspberry Pi OS release, where sometimes when I first run 'sudo apt update' I get a few errors and it doesn't work. I just rerun the command until it works properly and without errors:*
```
sudo apt update
sudo apt upgrade
```

Install the dependencies we'll require
```
sudo apt install portaudio19-dev python3-pyaudio mpg321 flac vim -y
```

Reboot
```
reboot
```

## Get the necessary access keys

### Porcupine
Create a Forever-Free account on picovoice.ai for use with personal projects
1. Go to [Picovoice's Porcupine](https://picovoice.ai/platform/porcupine/)
2. Click "Start Free"
3. Click "Sign Up" at the bottom left in order to sign up for a Forever-Free account
4. ![Picovoice account creation](./picovoice-account-creation.png)
5. On the right, under Get Start, sign up using a GitHub, Google, or LinkedIn account
6. Get your access key for Porcupine wake word, save it somewhere safe, and don't share it with anyone

### OpenAI's API
1. OpenAI's API isn't free, and their pricing model is based on usage. You can find out more here: [OpenAI pricing](https://openai.com/pricing)
2. Create an OpenAI account at [OpenAI account signup](https://platform.openai.com/signup), or if you already have one log in at [OpenAI account login](https://platform.openai.com/login). 
3. Navigate to the [API key page](https://platform.openai.com/account/api-keys) and "Create new secret key"
4. Save it somewhere safe, and don't share it with anyone
