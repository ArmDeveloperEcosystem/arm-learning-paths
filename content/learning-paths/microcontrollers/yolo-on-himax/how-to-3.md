---
title: Flash Firmware
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Update The Firmware

Update firmware in Windows environment by python code.

### Step 4.1. Open ‘cmd’ over Seeed_Grove_Vision_AI_Module_V2-main.

### Step 4.2. Install xmodem.

Run the following command 

```python
pip install -r xmodem/requirements.txt
```

### Step 4.3. Connect the module to PC by USB cable.

### Step 4.4. Flash the firmware by the following commands:

```python
python xmodem\xmodem_send.py --port=[your COM number] --baudrate=921600 --protocol=xmodem --file=we2_image_gen_local\output_case1_sec_wlcsp\output.img 
```

    Note: For each project, the command might be slightly different. See the instructions on project pages for this command.

After the firmware image burning is completed, the message "Do you want to end file transmission and reboot system? (y)" is displayed. Press the reset button on module to restart.
