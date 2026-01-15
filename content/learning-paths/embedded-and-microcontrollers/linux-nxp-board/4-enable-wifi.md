---
# User change
title: "Enable WiFi"

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

{{% notice Note %}}

* WiFi network connectivity **does not persist** on NXP board reboot
* It **does persist** on logging out and then logging back in as the same Linux user

{{% /notice %}}

1. [Log in to Linux]( {{< relref "2-boot-nxp.md" >}} ) on the board, as a [super user]( {{< relref "3-create-super-user" >}} )

2. Run the below terminal commands:
   ```bash
   sudo /usr/sbin/modprobe moal mod_para=nxp/wifi_mod_para.conf
   sudo connmanctl
   ```

3. The prompt will change to `connmanctl>`, where you will enter the following commands:

   ```bash
   enable wifi
   scan wifi
   services
   ```

4. Your available WiFi networks will be listed in the following form:

   ```bash { output_lines = "1-3" }
   <SSID>                wifi_0123456789ab_cdef0123456789_managed_psk
   <SSID>                wifi_abcdef012345_6789abcdef0123_managed_psk
   <SSID>                wifi_fedcba987654_3210fedcba9876_managed_psk
   ```

   {{% notice Note %}}
   
   Duplicate SSIDs may appear, so you will have to experiment with the different `wifi_..._managed_psk` names, when you try to connect in the next step

   {{% /notice %}}

5. Still within the `connmanctl>` prompt, enter the following commands:

   ```bash
   agent on
   connect wifi_0123456789ab_cdef0123456789_managed_psk # Your wifi_..._managed_ps name will be different
   Agent RequestInput wifi_0123456789ab_cdef0123456789_managed_psk
   Passphrase = [ Type=psk, Requirement=mandatory ]
   Passphrase? # Enter your WiFi password
   connmanctl> quit
   ```

6. Assuming your WiFi network is connected to the Internet, test connectivity:

   ```bash
   curl -I http://www.example.com
   ```

   If WiFi is configured correctly, you will see the example.com web page load:

   ```bash { output_lines = "1-2" }
   HTTP/1.1 200 OK
   ...
   ```

7. [optional] If your WiFi network is not connected to the internet, test connectivity this way:

   ```bash
   ifconfig | grep RUNNING -A 1
   ```

   If WiFi is configured correctly, you will see a list of `RUNNING` network adapters:
   * one for `127.0.0.1` (`localhost`) and
   * a second for the NXP board's assigned IP address on the WiFi network
   * Example output, where `192.168.1.89` is the NXP board's successfully assigned IP address:
     ```bash { output_lines = "1-5" }
     lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
          inet 127.0.0.1  netmask 255.0.0.0
     --
     mlan0: flags=-28605<UP,BROADCAST,RUNNING,MULTICAST,DYNAMIC>  mtu 1500
          inet 192.168.1.89  netmask 255.255.255.0  broadcast 192.168.1.255
     ```