---
# User change
title: "(Optional) Enable Persistent WiFi"

weight: 8 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

On this page you will configure the NXP board to connect to a specific WiFi network on boot.

1. [Log in to Linux]( {{< relref "2-boot-nxp.md" >}} ) on the board, as `root`

2. Create a `wpa_supplicant.conf`:
   ```bash
   touch /etc/wpa_supplicant.conf
   nano /etc/wpa_supplicant.conf
   ```
   Enter your WiFi credentials into the `wpa_supplicant.conf` file:
   ```bash
   ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
   update_config=1

   network={
       ssid="YOUR_SSID"
       psk="YOUR_PASSWORD"
       key_mgmt=WPA-PSK
   }
   ```

3. Test the `wpa_supplicant.conf` file:
   ```bash
   modprobe moal mod_para=nxp/wifi_mod_para.conf
   ifconfig mlan0 up
   wpa_supplicant -B -i mlan0 -c /etc/wpa_supplicant.conf
   udhcpc -i mlan0
   ```
   * mlan0 is the WiFi interface on i.MX93
	* If this connects to WiFi, we’re ready for automation

4. Configure DNS server IP addresses, so that the NXP board can resolve Internet addresses:
   ```bash
   touch /usr/share/udhcpc/default.script
   nano /usr/share/udhcpc/default.script
   ```
   and add in the following `udhcpc` script:
   ```bash
   #!/bin/sh
   # udhcpc script
   case "$1" in
       deconfig)
           ip addr flush dev $interface
           ;;
       bound|renew)
           ip addr add $ip/$subnet dev $interface
           ip route add default via $router
           echo "nameserver 8.8.8.8" > /etc/resolv.conf
           echo "nameserver 1.1.1.1" >> /etc/resolv.conf
           ;;
   esac
   ```
   Make the `default.script` executable:
   ```bash
   chmod +x /usr/share/udhcpc/default.script
   ```

5. Create a `nxp-wifi-setup.sh` script:
   ```bash
   touch /usr/bin/nxp-wifi-setup.sh
   nano /usr/bin/nxp-wifi-setup.sh
   ```
   and add in the following lines:
   ```bash
   #!/bin/sh
   # Load WiFi driver
   /usr/sbin/modprobe moal mod_para=nxp/wifi_mod_para.conf

   # Bring interface up
   /usr/bin/ifconfig mlan0 up

   # Connect to WiFi
   /usr/sbin/wpa_supplicant -B -i mlan0 -c /etc/wpa_supplicant.conf

   # Obtain DHCP IP + DNS
   /usr/sbin/udhcpc -i mlan0 -s /usr/share/udhcpc/default.script
   ```
   Make the `nxp-wifi-setup.sh` executable:
   ```bash
   chmod +x /usr/bin/nxp-wifi-setup.sh
   ```

6. Create a `nxp-wifi-setup.service`:
   ```bash
   touch /etc/systemd/system/nxp-wifi-setup.service
   nano /etc/systemd/system/nxp-wifi-setup.service
   ```
   Enter the following systemd commands into the `nxp-wifi-setup.service` file:
   ```bash
   [Unit]
   Description=WiFi Setup for NXP FRDM i.MX93
   After=network.target

   [Service]
   Type=oneshot
   ExecStart=/usr/bin/nxp-wifi-setup.sh
   RemainAfterExit=yes

   [Install]
   WantedBy=multi-user.target
   ```

7. Create a `wpa_supplicant.service`:
   ```bash
   touch /etc/systemd/system/wpa_supplicant.service
   nano /etc/systemd/system/wpa_supplicant.service
   ```
   Enter the following systemd commands into the `wpa_supplicant.service` file:
   ```bash
   [Unit]
   Description=WPA Supplicant daemon
   After=network.target

   [Service]
   Type=simple
   ExecStart=/usr/sbin/wpa_supplicant -i mlan0 -c /etc/wpa_supplicant.conf
   Restart=always

   [Install]
   WantedBy=multi-user.target
   ```
   
8. Enable and Start the `nxp-wifi-setup.service`:
   ```bash
   systemctl daemon-reload
   systemctl enable nxp-wifi-setup.service wpa_supplicant.service
   systemctl start nxp-wifi-setup.service wpa_supplicant.service
   ```

10. Check status:
   ```bash
   systemctl status nxp-wifi-setup.service
   systemctl status wpa_supplicant.service
   ```
   and confirm Internet connectivity:
   ```bash
   curl -I http://www.example.com
   ```