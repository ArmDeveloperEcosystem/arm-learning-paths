#!/bin/bash
set -e

dir_name="balena_pi_package"
output_filename="balenaos_rpi4b.zip"
firmware_name=$1
image_name=$(basename ${firmware_name} .zip)

[ -d ${dir_name} ] || mkdir ${dir_name}
cd ${dir_name}
cp ../${firmware_name} .
unzip ${firmware_name}
mv ${image_name} nand

# Mount the firmware image and extract the kernel and device tree
LO="$(losetup -f)"
losetup -P "${LO}" nand
mkdir {boot,rootfs}
mount "${LO}p1" boot
cp boot/bcm2711-rpi-4-b.dtb devicetree
umount boot/
rm -r boot/

mount "${LO}p2" rootfs
cp rootfs/hostapps/*/boot/Image.gz .
gunzip Image.gz
mv Image kernel 
umount rootfs/
rm -r rootfs/
losetup -d "${LO}"

# create the Info plist that describes the model image
cat << EOF > Info.plist
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Type</key>
    <string>iot</string>
    <key>UniqueIdentifier</key>
    <string>BalenaOS</string>
    <key>DeviceIdentifier</key>
    <string>rpi4b</string>
    <key>Version</key>
    <string>2.113.18</string>
    <key>Build</key>
    <string>production</string>
</dict>
</plist>
EOF

zip -m ../${output_filename} nand kernel devicetree Info.plist
cd ../
rm -r ${dir_name}
