---
title: Test With FVP
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Test with FVP
We can test the firmware build using the fixed virtual platform model of RD-N2 that we can download from [here](https://developer.arm.com/downloads/-/arm-ecosystem-fvps). 

### Setup the FVP
We want the RD-N2 for linux. Checking the [platform readme](https://neoverse-reference-design.docs.arm.com/en/latest/platforms/rdn2/readme.html#release-tags) we determine that we need version `11.24.12` of the FVP model. We unpack the tarball and run the install script.
```bash
ubuntu@ip-10-0-0-164:~$ ls FVP_RD_N2_11.24_12_Linux64.tgz 
FVP_RD_N2_11.24_12_Linux64.tgz
ubuntu@ip-10-0-0-164:~$ ./FVP_RD_N2.sh --i-agree-to-the-contained-eula --no-interactive
=======================================================
Welcome to the Installer for ARM Fast Models FVP RD-N2
=======================================================
Do you want to proceed with the installation? [yes]
'/home/ubuntu/FVP_RD_N2' does not exist, create? [yes]

--- Installing to '/home/ubuntu/FVP_RD_N2' (This may take a while...)

-----------------------------------
Installation completed successfully
-----------------------------------

=======================================================
ubuntu@ip-10-0-0-164:~$ ls FVP_RD_N2/models/Linux64_GCC-9.3/
FVP_RD_N2          arm_singleton_registry.so  cmn700_rd_n2_css1.yml                libSDL2-2.0.so.0.10.0  libsystemc-2.3.4.so
FVP_RD_N2.so       armlm-ipc                  cmn700_rd_n2_css2.yml                libarmctmodel.so       newt.so
FVP_RD_N2_Cfg2     cmn700_rd_n2.yml           cmn700_rd_n2_css3.yml                libarmlm.so            ni700_io_main.yml
FVP_RD_N2_Cfg2.so  cmn700_rd_n2_css0.yml      libMAXCOREInitSimulationEngine.3.so  libscxframework.so
```

Now we should export the path to the `FVP_RD_N2` model binary as the `MODEL` environment variable.
```bash
ubuntu@ip-10-0-0-164:~$ realpath FVP_RD_N2/models/Linux64_GCC-9.3/FVP_RD_N2
/home/ubuntu/FVP_RD_N2/models/Linux64_GCC-9.3/FVP_RD_N2
ubuntu@ip-10-0-0-164:~$ export MODEL=/home/ubuntu/FVP_RD_N2/models/Linux64_GCC-9.3/FVP_RD_N2
ubuntu@ip-10-0-0-164:~$ 
```

We can do a quick test of the model now, giving it no parameters to see what it does.
```bash
ubuntu@ip-10-0-0-164:~$ $MODEL
terminal_uart_scp: Listening for serial connection on port 5000
terminal_uart_mcp: Listening for serial connection on port 5001
INFO: RD_N2.css.cmn700: Using 'CFGM_PERIPHBASE_PARAM' for periphbase address.

INFO: RD_N2.css.cmn700: CMN-700 r1p0 model, periphbase=0x0000000140000000, mesh_config_file='cmn700_rd_n2.yml'

terminal_ns_uart_ap: Listening for serial connection on port 5002
terminal_s_uart_ap: Listening for serial connection on port 5003
INFO: RD_N2.css.io_macro_0.ni_700: NI-700 r0p0 model, periphbase=0x0000000040c00000, mesh_config_file='/home/ubuntu/FVP_RD_N2/models/Linux64_GCC-9.3/ni700_io_main.yml'

INFO: RD_N2.css.io_macro_1.ni_700: NI-700 r0p0 model, periphbase=0x0000000040c00000, mesh_config_file='/home/ubuntu/FVP_RD_N2/models/Linux64_GCC-9.3/ni700_io_main.yml'

INFO: RD_N2.css.io_macro_2.ni_700: NI-700 r0p0 model, periphbase=0x0000000040c00000, mesh_config_file='/home/ubuntu/FVP_RD_N2/models/Linux64_GCC-9.3/ni700_io_main.yml'

INFO: RD_N2.css.io_macro_3.ni_700: NI-700 r0p0 model, periphbase=0x0000000040c00000, mesh_config_file='/home/ubuntu/FVP_RD_N2/models/Linux64_GCC-9.3/ni700_io_main.yml'

INFO: RD_N2.css.io_macro_4.ni_700: NI-700 r0p0 model, periphbase=0x0000000040c00000, mesh_config_file='/home/ubuntu/FVP_RD_N2/models/Linux64_GCC-9.3/ni700_io_main.yml'

iomacro_terminal_0: Listening for serial connection on port 5004
iomacro_terminal_1: Listening for serial connection on port 5005
terminal_s0: Listening for serial connection on port 5006
terminal_s1: Listening for serial connection on port 5007
terminal_mcp: Listening for serial connection on port 5008
terminal_0: Listening for serial connection on port 5009
terminal_1: Listening for serial connection on port 5010

Warning: RD_N2: vis_hdlcd:: Visualisation setup failed - the model will run with the Visualisation window disabled
In file: (unknown):0

Warning: RD_N2: vis_dashboard:: Visualisation setup failed - the model will run with the Visualisation window disabled
In file: (unknown):0

Warning: RD_N2: MCP: Access to reserved memory region: Write 4 bytes 0x0 to 0xe7fefff0. Aborting.
In file: (unknown):0
In process: RD_N2.thread_p_129 @ 0 s
...
...
...
```

The model proceeds with additional failures so we abort it using Ctrl+C. It is interesting to observe that the model will output UARTs to local ports 5000..5010. If we were running the model on a local machine, or we had X11 forwarding setup, the model would open a number of xterm terminals with the UART output piped to them, one per port. 

### Screen configuration for UARTs
If we do not have X11 forwarding and we are executing on a remote server, we can use screen to spawn persistent terminals that will listen on those ports and we get the information out that way. Let's set up the UART. terminals now. We need to make sure we have the `screen` tool installed.
```bash
ubuntu@ip-10-0-0-164:~$ sudo apt-get install screen
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libtinyxml2-9 libz3-4 python3-pygments
Use 'sudo apt autoremove' to remove them.
The following NEW packages will be installed:
  screen
0 upgraded, 1 newly installed, 0 to remove and 30 not upgraded.
Need to get 672 kB of archives.
After this operation, 1029 kB of additional disk space will be used.
Get:1 http://eu-west-1.ec2.archive.ubuntu.com/ubuntu jammy/main amd64 screen amd64 4.9.0-1 [672 kB]
Fetched 672 kB in 0s (43.1 MB/s)
Selecting previously unselected package screen.
(Reading database ... 160179 files and directories currently installed.)
Preparing to unpack .../screen_4.9.0-1_amd64.deb ...
Unpacking screen (4.9.0-1) ...
Setting up screen (4.9.0-1) ...
Processing triggers for install-info (6.8-4build1) ...
Processing triggers for man-db (2.10.2-1) ...
Scanning processes...                                                                                                                                             
Scanning candidates...                                                                                                                                            
Scanning linux images...                                                                                                                                          

Restarting services...
Service restarts being deferred:
 /etc/needrestart/restart.d/dbus.service
 systemctl restart getty@tty1.service
 systemctl restart libvirtd.service
 systemctl restart networkd-dispatcher.service
 systemctl restart systemd-logind.service
 systemctl restart unattended-upgrades.service
 systemctl restart user@1000.service

No containers need to be restarted.

No user sessions are running outdated binaries.

No VM guests are running outdated hypervisor (qemu) binaries on this host.
ubuntu@ip-10-0-0-164:~$ 
```

Then we should open a new terminal where we will start a `screen` session and connect to it. We could do it in our terminal and add another `screen` window for running the model in as well, but for now we will use two logins. Running the help command tells us that we can use `-c rdn2-fvp.cfg` to run a session with pre-configured windows and commands.
```bash
ubuntu@ip-10-0-0-164:~$ screen --help
Use: screen [-opts] [cmd [args]]
 or: screen -r [host.tty]

Options:
-4            Resolve hostnames only to IPv4 addresses.
-6            Resolve hostnames only to IPv6 addresses.
-a            Force all capabilities into each window's termcap.
-A -[r|R]     Adapt all windows to the new display width & height.
-c file       Read configuration file instead of '.screenrc'.
-d (-r)       Detach the elsewhere running screen (and reattach here).
-dmS name     Start as daemon: Screen session in detached mode.
-D (-r)       Detach and logout remote (and reattach here).
-D -RR        Do whatever is needed to get a screen session.
-e xy         Change command characters.
-f            Flow control on, -fn = off, -fa = auto.
-h lines      Set the size of the scrollback history buffer.
-i            Interrupt output sooner when flow control is on.
-l            Login mode on (update /var/run/utmp), -ln = off.
-ls [match]   or
-list         Do nothing, just list our SockDir [on possible matches].
-L            Turn on output logging.
-Logfile file Set logfile name.
-m            ignore $STY variable, do create a new screen session.
-O            Choose optimal output rather than exact vt100 emulation.
-p window     Preselect the named window if it exists.
-q            Quiet startup. Exits with non-zero return code if unsuccessful.
-Q            Commands will send the response to the stdout of the querying process.
-r [session]  Reattach to a detached screen process.
-R            Reattach if possible, otherwise start a new session.
-s shell      Shell to execute rather than $SHELL.
-S sockname   Name this session <pid>.sockname instead of <pid>.<tty>.<host>.
-t title      Set title. (window's name).
-T term       Use term as $TERM for windows, rather than "screen".
-U            Tell screen to use UTF-8 encoding.
-v            Print "Screen version 4.09.00 (GNU) 30-Jan-22".
-wipe [match] Do nothing, just clean up SockDir [on possible matches].
-x            Attach to a not detached screen. (Multi display mode).
-X            Execute <cmd> as a screen command in the specified session.
ubuntu@ip-10-0-0-164:~$ 
```

Let us craft such a config file so that when we start a session with it, we get ten windows and each will periodically try to connect to one of the local ports where a UART is running. We might as well change the titles of the windows so we know which terminal is which. The resulting `screen-uart.cfg` file will look like this:
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

When we start the screen session using `screen -c rd-infra/model-scripts/rdinfra/screen-uart.cfg` we get the following look:
![screen terminals alt-text#center](images/terminal.png "Figure 1. Screen Terminals")

The errors are expected as there is nothing talking to those ports yet. We can quit from within the screen by the getting a prompt using `Ctrl+A :` key combo, followed by the `quit` command. Alternatively `Ctrl+A D` will detach the screen session and send it to background. Unfortunately, reattaching the session wipes our neat window arrangement so that's not very useful. We can check if we have any screen sessions running on the system:
```bash
ubuntu@ip-10-0-0-164:~/rd-infra/model-scripts/rdinfra$ screen -list
There is a screen on:
	2408179.pts-2.ip-10-0-0-164	(01/12/24 17:32:33)	(Attached)
1 Socket in /run/screen/S-ubuntu.
ubuntu@ip-10-0-0-164:~/rd-infra/model-scripts/rdinfra$ 
```
And this allows us to detach, reattach, purge or kill stuff as needed.

### Running the FVP

Running the FVP at this point is a matter of executing the appropriate model script:
```bash
ubuntu@ip-10-0-0-164:~$ cd rd-infra/model-scripts/rdinfra/
ubuntu@ip-10-0-0-164:~/rd-infra/model-scripts/rdinfra$ ./uefi.sh -p rdn2
 Continue with <network_enabled> as false !!! 
 Continue with <BL1_IMAGE> as tf-bl1.bin !!! 
 Continue with <FIP_IMAGE> as fip-uefi.bin !!! 
NOR1 flash image: /home/ubuntu/rd-infra/model-scripts/rdinfra/platforms/rdn2/nor1_flash.img
NOR2 flash image: /home/ubuntu/rd-infra/model-scripts/rdinfra/platforms/rdn2/nor2_flash.img

Fast Models [11.24.12 (Dec  4 2023)]
Copyright 2000-2023 ARM Limited.
All Rights Reserved.


Info: /OSCI/SystemC: Simulation stopped by user.

SCP UART Log = /home/ubuntu/rd-infra/model-scripts/rdinfra/platforms/rdn2/rdn2/refinfra-2410813-uart-0-scp_2024-01-12_17.34.47
MCP UART Log = /home/ubuntu/rd-infra/model-scripts/rdinfra/platforms/rdn2/rdn2/refinfra-2410813-uart-0-mcp_2024-01-12_17.34.47
TF/MM UART Log = /home/ubuntu/rd-infra/model-scripts/rdinfra/platforms/rdn2/rdn2/refinfra-2410813-uart-0-sec_2024-01-12_17.34.47
UEFI/OS UART Log = /home/ubuntu/rd-infra/model-scripts/rdinfra/platforms/rdn2/rdn2/refinfra-2410813-uart-0-nsec_2024-01-12_17.34.47

Launching RD-N2 model

/home/ubuntu/FVP_RD_N2/models/Linux64_GCC-9.3/FVP_RD_N2 --data css.scp.armcortexm7ct=../../../../output/rdn2/rdn2/scp_ramfw.bin@0x0BD80000 --data css.mcp.armcortexm7ct=../../../../output/rdn2/rdn2/mcp_ramfw.bin@0x0BF80000 -C css.mcp.ROMloader.fname=../../../../output/rdn2/rdn2/mcp_romfw.bin -C css.scp.ROMloader.fname=../../../../output/rdn2/rdn2/scp_romfw.bin -C css.trustedBootROMloader.fname=../../../../output/rdn2/rdn2/tf-bl1.bin -C board.flashloader0.fname=../../../../output/rdn2/rdn2/fip-uefi.bin -C board.flashloader1.fname=/home/ubuntu/rd-infra/model-scripts/rdinfra/platforms/rdn2/nor1_flash.img -C board.flashloader1.fnameWrite=/home/ubuntu/rd-infra/model-scripts/rdinfra/platforms/rdn2/nor1_flash.img -C board.flashloader2.fname=/home/ubuntu/rd-infra/model-scripts/rdinfra/platforms/rdn2/nor2_flash.img -C board.flashloader2.fnameWrite=/home/ubuntu/rd-infra/model-scripts/rdinfra/platforms/rdn2/nor2_flash.img -S -R -C css.scp.pl011_uart_scp.out_file=rdn2/refinfra-2410813-uart-0-scp_2024-01-12_17.34.47 -C css.scp.pl011_uart_scp.unbuffered_output=1 -C css.scp.pl011_uart_scp.uart_enable=true -C css.mcp.pl011_uart_mcp.out_file=rdn2/refinfra-2410813-uart-0-mcp_2024-01-12_17.34.47 -C css.mcp.pl011_uart_mcp.unbuffered_output=1 -C css.pl011_ns_uart_ap.out_file=rdn2/refinfra-2410813-uart-0-nsec_2024-01-12_17.34.47 -C css.pl011_ns_uart_ap.unbuffered_output=1 -C css.pl011_ns_uart_ap.flow_ctrl_mask_en=1 -C css.pl011_ns_uart_ap.enable_dc4=1 -C css.pl011_s_uart_ap.out_file=rdn2/refinfra-2410813-uart-0-sec_2024-01-12_17.34.47 -C css.pl011_s_uart_ap.unbuffered_output=1 -C css.pl011_s_uart_ap.flow_ctrl_mask_en=1 -C css.pl011_s_uart_ap.enable_dc4=0 -C soc.pl011_uart0.flow_ctrl_mask_en=1 -C soc.pl011_uart0.enable_dc4=0 -C css.gic_distributor.ITS-device-bits=20 -C pcie_group_0.pciex16.hierarchy_file_name=<default> -C pcie_group_1.pciex16.hierarchy_file_name=example_pcie_hierarchy_2.json -C pcie_group_2.pciex16.hierarchy_file_name=example_pcie_hierarchy_3.json -C pcie_group_3.pciex16.hierarchy_file_name=example_pcie_hierarchy_4.json -C pcie_group_0.pciex16.pcie_rc.ahci0.endpoint.ats_supported=true -C board.dram_size=0x200000000 -C css.tzc0.tzc400.rst_gate_keeper=0x0f -C css.tzc0.tzc400.rst_region_attributes_0=0xc000000f -C css.tzc0.tzc400.rst_region_id_access_0=0xffffffff -C css.tzc1.tzc400.rst_gate_keeper=0x0f -C css.tzc1.tzc400.rst_region_attributes_0=0xc000000f -C css.tzc1.tzc400.rst_region_id_access_0=0xffffffff -C css.tzc2.tzc400.rst_gate_keeper=0x0f -C css.tzc2.tzc400.rst_region_attributes_0=0xc000000f -C css.tzc2.tzc400.rst_region_id_access_0=0xffffffff -C css.tzc3.tzc400.rst_gate_keeper=0x0f -C css.tzc3.tzc400.rst_region_attributes_0=0xc000000f -C css.tzc3.tzc400.rst_region_id_access_0=0xffffffff -C css.tzc4.tzc400.rst_gate_keeper=0x0f -C css.tzc4.tzc400.rst_region_attributes_0=0xc000000f -C css.tzc4.tzc400.rst_region_id_access_0=0xffffffff -C css.tzc5.tzc400.rst_gate_keeper=0x0f -C css.tzc5.tzc400.rst_region_attributes_0=0xc000000f -C css.tzc5.tzc400.rst_region_id_access_0=0xffffffff -C css.tzc6.tzc400.rst_gate_keeper=0x0f -C css.tzc6.tzc400.rst_region_attributes_0=0xc000000f -C css.tzc6.tzc400.rst_region_id_access_0=0xffffffff -C css.tzc7.tzc400.rst_gate_keeper=0x0f -C css.tzc7.tzc400.rst_region_attributes_0=0xc000000f -C css.tzc7.tzc400.rst_region_id_access_0=0xffffffff 

terminal_uart_scp: Listening for serial connection on port 5000
terminal_uart_mcp: Listening for serial connection on port 5001
INFO: RD_N2.css.cmn700: Using 'CFGM_PERIPHBASE_PARAM' for periphbase address.

INFO: RD_N2.css.cmn700: CMN-700 r1p0 model, periphbase=0x0000000140000000, mesh_config_file='cmn700_rd_n2.yml'

terminal_ns_uart_ap: Listening for serial connection on port 5002
terminal_s_uart_ap: Listening for serial connection on port 5003
INFO: RD_N2.css.io_macro_0.ni_700: NI-700 r0p0 model, periphbase=0x0000000040c00000, mesh_config_file='/home/ubuntu/FVP_RD_N2/models/Linux64_GCC-9.3/ni700_io_main.yml'

INFO: RD_N2.css.io_macro_1.ni_700: NI-700 r0p0 model, periphbase=0x0000000040c00000, mesh_config_file='/home/ubuntu/FVP_RD_N2/models/Linux64_GCC-9.3/ni700_io_main.yml'

INFO: RD_N2.css.io_macro_2.ni_700: NI-700 r0p0 model, periphbase=0x0000000040c00000, mesh_config_file='/home/ubuntu/FVP_RD_N2/models/Linux64_GCC-9.3/ni700_io_main.yml'

INFO: RD_N2.css.io_macro_3.ni_700: NI-700 r0p0 model, periphbase=0x0000000040c00000, mesh_config_file='/home/ubuntu/FVP_RD_N2/models/Linux64_GCC-9.3/ni700_io_main.yml'

INFO: RD_N2.css.io_macro_4.ni_700: NI-700 r0p0 model, periphbase=0x0000000040c00000, mesh_config_file='/home/ubuntu/FVP_RD_N2/models/Linux64_GCC-9.3/ni700_io_main.yml'

iomacro_terminal_0: Listening for serial connection on port 5004
iomacro_terminal_1: Listening for serial connection on port 5005
terminal_s0: Listening for serial connection on port 5006
terminal_s1: Listening for serial connection on port 5007
terminal_mcp: Listening for serial connection on port 5008
terminal_0: Listening for serial connection on port 5009
terminal_1: Listening for serial connection on port 5010

Warning: RD_N2: vis_hdlcd:: Visualisation setup failed - the model will run with the Visualisation window disabled
In file: (unknown):0

Warning: RD_N2: vis_dashboard:: Visualisation setup failed - the model will run with the Visualisation window disabled
In file: (unknown):0

Info: RD_N2: RD_N2.css.scp.ROMloader: FlashLoader: Loaded 44 kB from file '../../../../output/rdn2/rdn2/scp_romfw.bin'

Info: RD_N2: RD_N2.css.mcp.ROMloader: FlashLoader: Loaded 42 kB from file '../../../../output/rdn2/rdn2/mcp_romfw.bin'

Info: RD_N2: RD_N2.css.trustedBootROMloader: FlashLoader: Loaded 80 kB from file '../../../../output/rdn2/rdn2/tf-bl1.bin'

Info: RD_N2: RD_N2.board.flashloader0: FlashLoader: Loaded 5 MB from file '../../../../output/rdn2/rdn2/fip-uefi.bin'

Info: RD_N2: RD_N2.board.flashloader1: FlashLoader: Loaded 64 MB from file '/home/ubuntu/rd-infra/model-scripts/rdinfra/platforms/rdn2/nor1_flash.img'

Info: RD_N2: RD_N2.board.flashloader2: FlashLoader: Loaded 64 MB from file '/home/ubuntu/rd-infra/model-scripts/rdinfra/platforms/rdn2/nor2_flash.img'

Info: RD_N2: CADI Debug Server started for ARM Models...

Warning: RD_N2: pcie_macro: write of 0x00000003 to defined APB interface at 0x000ef23000 not implemented in model. The 'warn_once' parameter is set, so subsequent warnings will be suppressed.
In file: (unknown):0
In process: RD_N2.thread_p_130 @ 75431622660 ps
```

And we can observe the platform running on our shiny terminals:
![fvp terminals alt-text#center](images/uefi.png "Figure 2. FVP Terminals")

We can also use the `./boot.sh -p rdn2` command line to boot to busy-box.
![docker terminal alt-text#center](images/docker-run.png "Figure 3. Docker Terminal")
