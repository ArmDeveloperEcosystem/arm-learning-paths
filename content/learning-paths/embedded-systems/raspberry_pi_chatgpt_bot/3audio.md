---
title: Setting Up Audio
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Setting Up Audio - Speakers and Microphone
First, with your speakers and microphone plugged in, we'll verify if they're working automatically. If they are you'll be able to skip ahead to the next session. If not we'll have to manually configure the audio.

Right click on the speaker icon and select your speakers

![Raspberry Pi audio output](audio.png)

Open up the terminal, run the following command, and speak into the microphone for five seconds.
```
arecord -d 5 test.wav
```

This will try to record a five second clip using the default microphone and then output the test.wav file to the current directory. 

Use the following command to attempt to play back test.wav using your default speakers
```
aplay test.wav
```

**If everything worked correctly and you are hearing what your recorded, congrats, you can skip ahead to the next section. If not, we'll do some manual setup.**

## Manual audio setup

### Find the audio devices for speakers and microphone
Use the following commands to find the card and device for your microphone and your speakers
```
arecord -l
aplay -l
```

The output should look like the following:

![arecord aplay output](arecord-aplay-output.png)

In the example above, you can see my USB microphone is card 3, device 0. So 3,0
And the USB speakers are card 2, device 0. So 2,0.

Let's find out if the devices are running correctly by once again running arecord and aplay, but this time specifying the card and device using the above information.

Change your card and device numbers in plughw to match your output, and try recording a five second clip by speaking into your microphone again
```
arecord -D plughw:3,0 -d 5 test.wav
```

And to play back that recording
```
aplay -D plughw:2,0 test.wav
```

If you can now hear what you recorded we'll go ahead and create a config file.

#### Troubleshooting the above
If the above doesn't work you'll have to dive deeper. Some steps you can take
1. Verify that the speakers and microphone are properly connect. Maybe something is loose
2. Use 'alsamixer' or 'amixer' to check that your devices aren't muted and that the volume levels are high enough
3. Make sure you are completely up to date with 
	1. 'sudo apt update'
	2. 'sudo apt upgrade'
4. Check online and see if your microphone and / or speakers are linux compatible
5. Try other speakers / microphones

### Create an asound.conf file using the above information to set the defaults

Using your text editor of choice, create an /etc/asound.conf file and fill it with the appropriate information found in using aplay -l and arecord -l

Create an asound.conf file inside /etc/
```
sudo vim /etc/asound.conf
```

Paste in the following, changing the pcm.!default playback and ctl.!default to match the aplay -l results. And change the pcm.!default capture section to the arecord -l results.
```
pcm.!default {
    type asym
    playback.pcm {
        type plug
        slave.pcm "hw:2,0"
    }
    capture.pcm {
        type plug
        slave.pcm "hw:3,0"
    }
}

ctl.!default {
    type hw
    card 2
}

```

Save, exit, then reboot
```
reboot
```

After rebooting, try the following commands again to verify everything is now working:
```
arecord -d 5 test.wav
aplay test.wav
```
