---
title: Test With FVP
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

The firmware build can be executed on the Neoverse N2 Reference Design FVP that you can download from [Arm Ecosystem FVPs](https://developer.arm.com/downloads/-/arm-ecosystem-fvps). 


### Setup the FVP

Download from the above page, or directly with:
```bash
wget https://developer.arm.com/-/media/Arm%20Developer%20Community/Downloads/OSS/FVP/Neoverse-N2/Neoverse-N2-11-24-12/FVP_RD_N2_11.24_12_Linux64.tgz
```
Unpack the tarball and run the install script.
```bash
tar -xf FVP_RD_N2_11.24_12_Linux64.tgz 
./FVP_RD_N2.sh --i-agree-to-the-contained-eula --no-interactive
```

Export the path to the `FVP_RD_N2` model binary as the `MODEL` environment variable.
```bash
export MODEL=/home/ubuntu/FVP_RD_N2/models/Linux64_GCC-9.3/FVP_RD_N2
```
### Screen configuration for UARTs

The model will output UARTs to local ports 5000..5010. If we were running the model on a local machine, or we had X11 forwarding setup, the model would open a number of xterm terminals with the UART output piped to them, one per port. 

If we do not have X11 forwarding and we are executing on a remote server, we can use `screen` to spawn persistent terminals that will listen on those ports and we get the information out that way.

Open a new terminal where we will start a `screen` session and connect to it.

To install `screen` use:
```bash
sudo apt-get install screen
```

Use a text editor to create the below configuration file, which will set up `screen` windows for each UART.

#### screen-uart.cfg

```bash
# Split horizontally into two
split -v

# Start the SCP UART telnet
screen -t  "SCP UART" run-one-constantly telnet localhost 5000

# Split screen and start MCP UART
split
focus
screen -t "MCP term" run-one-constantly telnet localhost 5001

# Split screen and start AP-NS UART
split
focus
screen -t "AP-NS term" run-one-constantly telnet localhost 5002

# Split screen and start AP-S UART
split
focus
screen -t "AP-S term" run-one-constantly telnet localhost 5003

# Focus on the second vertical pane
focus

# Start a second set of terminals
screen -t "IO-1" run-one-constantly telnet localhost 5004

# Split 
split
focus
screen -t "IO-2" run-one-constantly telnet localhost 5005

# Split 
split
focus
screen -t "S-0" run-one-constantly telnet localhost 5006

# Split 
split
focus
screen -t "S-1" run-one-constantly telnet localhost 5007

# Split 
split
focus
screen -t "MCP-extern" run-one-constantly telnet localhost 5008

# Split 
split
focus
screen -t "term-0" run-one-constantly telnet localhost 5009

# Split 
split
focus
screen -t "term-1" run-one-constantly telnet localhost 5010

# Focus back on the AP-NS UART
focus
focus
focus
```
Start the screen session with this configuration file:
```bash
screen -c screen-uart.cfg
```
The result should be similar to:

![screen terminals alt-text#center](images/terminal.png)

### Running the FVP

In your original terminal, launch the FVP using the supplied script:
```bash
cd rd-infra/model-scripts/rdinfra/
./uefi.sh -p rdn2
```
Observe the platform is running successfully.
![fvp terminals alt-text#center](images/uefi.png)

To boot to `busy-box`, use:
```bash
./boot.sh -p rdn2
```
![busy-box terminal alt-text#center](images/docker-run.png)
