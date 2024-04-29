---
title: Build
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build
Now that we have the environment and the source, let us perform a build of the firmware stack. We will follow the [instructions](https://neoverse-reference-design.docs.arm.com/en/latest/platform-boot/busybox-boot.html) to build a busy-box root. This will build a lightweight kernel with shell, giving fast performance on the FVP.
This will test that the firmware implementation builds and boots. It requires `TF-A`, `UEFI`, `SCP` and a lightweight OS loader, to make sure we exercise the UEFI `ExitBootServices` transition. The `busy-box` boot is perfect for this.

Launch the container:
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra" }
./container-scrits/container.sh -v /home/ubuntu/rd-infra/ run
```

Perform a build inside the container:
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra | 2-13" }
./build-scripts/rdinfra/build-test-busybox.sh -p rdn2 build
Running docker image: rdinfra-builder ...
~/rd-infra ~/rd-infra
~/rd-infra
Parsing variant
Sorting the build scripts for correctness.
build-kvmtool.sh build-scp.sh build-tf-a.sh build-uefi.sh build-linux.sh build-busybox.sh build-buildroot.sh build-grub.sh build-target-bins.sh
build-kvmtool.sh build-scp.sh build-tf-a.sh build-uefi.sh build-linux.sh build-busybox.sh build-buildroot.sh build-grub.sh build-target-bins.sh
Done.
***********************************
Execute build for build-kvmtool.sh on rdn2[rdn2][busybox]
...
...
```

This results in a X MB (!!) of plaintext (available to download) with the build log. During the build we can see that TF-A, UEFI and SCP firmware are built using their own build systems. The log finishes with the following:
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra | 1-14" }
...
...
output/bin/grub-mkimage: info: kernel_img=0x7f366cf65010, kernel_size=0x1a000.
output/bin/grub-mkimage: info: the core size is 0xa2a98.
output/bin/grub-mkimage: info: writing 0xa5000 bytes.
Execute build for build-grub.sh on rdn2[rdn2][busybox] done.
-----------------------------------
***********************************
Execute build for build-target-bins.sh on rdn2[rdn2][busybox]
~/rd-infra ~/rd-infra
~/rd-infra
Build
Execute build for build-target-bins.sh on rdn2[rdn2][busybox] done.
-----------------------------------
```

Because our rd-infra workspace is mounted into the container from outside, we should be able to find the output of the build normally in our host filesystem, we don't have to extract it from the container.
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra | 4-21" }
ls tf-a/build/rdn2/debug/
ls scp/output/rdn2/0/*/bin
ls uefi/edk2/Build/RdN2/DEBUG_GCC5/FV/
tf-a/build/rdn2/debug:
bl1  bl1.bin  bl2  bl2.bin  bl31  bl31.bin  fdts  lib  libc  libfdt  libmbedtls  libwrapper  romlib

scp/output/rdn2/0/mcp_ramfw/bin:
mcp_ramfw.bin  rdn2-mcp-bl2.elf  rdn2-mcp-bl2.map

scp/output/rdn2/0/mcp_romfw/bin:
mcp_romfw.bin  rdn2-mcp-bl1.elf  rdn2-mcp-bl1.map

scp/output/rdn2/0/scp_ramfw/bin:
rdn2-bl2.elf  rdn2-bl2.map  scp_ramfw.bin

scp/output/rdn2/0/scp_romfw/bin:
rdn2-bl1.elf  rdn2-bl1.map  scp_romfw.bin

uefi/edk2/Build/RdN2/DEBUG_GCC5/FV:
BL33_AP_UEFI.fd  FVMAIN.Fv.map  FVMAIN.ext  FVMAIN_COMPACT.Fv      FVMAIN_COMPACT.Fv.txt  Ffs        GuidedSectionTools.txt
FVMAIN.Fv        FVMAIN.Fv.txt  FVMAIN.inf  FVMAIN_COMPACT.Fv.map  FVMAIN_COMPACT.inf     Guid.xref
```

## Package the built images

The build system provides scripts to package the build products into image files that can be consumed by the FVP.
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra | 3-222" }
./container-scripts/container.sh -v /home/ubuntu/rd-infra/ run
./build-scripts/rdinfra/build-test-busybox.sh -p rdn2 package
Running docker image: rdinfra-builder ...
~/rd-infra ~/rd-infra
~/rd-infra
Parsing variant
Sorting the build scripts for correctness.
build-kvmtool.sh build-scp.sh build-tf-a.sh build-uefi.sh build-linux.sh build-busybox.sh build-buildroot.sh build-grub.sh build-target-bins.sh
build-kvmtool.sh build-scp.sh build-tf-a.sh build-uefi.sh build-linux.sh build-busybox.sh build-buildroot.sh build-grub.sh build-target-bins.sh
Done.
***********************************
Execute package for build-kvmtool.sh on rdn2[rdn2][busybox]
~/rd-infra ~/rd-infra
~/rd-infra
Ignoring filesystem none for rdn2[rdn2]

kvmtool Packaged..


kvm-unit-test Packaged..

Execute package for build-kvmtool.sh on rdn2[rdn2][busybox] done.
-----------------------------------
***********************************
Execute package for build-scp.sh on rdn2[rdn2][busybox]
~/rd-infra ~/rd-infra
~/rd-infra
~/rd-infra ~/rd-infra
~/rd-infra
Execute package for build-scp.sh on rdn2[rdn2][busybox] done.
-----------------------------------
***********************************
Execute package for build-tf-a.sh on rdn2[rdn2][busybox]
~/rd-infra ~/rd-infra
~/rd-infra
Packaging tf-a... 
~/rd-infra ~/rd-infra
~/rd-infra
Execute package for build-tf-a.sh on rdn2[rdn2][busybox] done.
-----------------------------------
***********************************
Execute package for build-uefi.sh on rdn2[rdn2][busybox]
~/rd-infra ~/rd-infra
~/rd-infra
Packaging uefi... 
~/rd-infra ~/rd-infra
~/rd-infra
Execute package for build-uefi.sh on rdn2[rdn2][busybox] done.
-----------------------------------
***********************************
Execute package for build-linux.sh on rdn2[rdn2][busybox]
~/rd-infra ~/rd-infra
~/rd-infra
Packaging Linux... 
~/rd-infra ~/rd-infra
/home/ubuntu/rd-infra/build-scripts/build-linux.sh: line 176: [: ==: unary operator expected
Execute package for build-linux.sh on rdn2[rdn2][busybox] done.
-----------------------------------
***********************************
Execute package for build-busybox.sh on rdn2[rdn2][busybox]
~/rd-infra ~/rd-infra
~/rd-infra
Packaging BUSYBOX... 
~/rd-infra/build-scripts/ramdisk ~/rd-infra
~/rd-infra
~/rd-infra ~/rd-infra
~/rd-infra
Execute package for build-busybox.sh on rdn2[rdn2][busybox] done.
-----------------------------------
***********************************
Execute package for build-buildroot.sh on rdn2[rdn2][busybox]
~/rd-infra ~/rd-infra
~/rd-infra
Execute package for build-buildroot.sh on rdn2[rdn2][busybox] done.
-----------------------------------
***********************************
Execute package for build-grub.sh on rdn2[rdn2][busybox]
~/rd-infra ~/rd-infra
~/rd-infra
Execute package for build-grub.sh on rdn2[rdn2][busybox] done.
-----------------------------------
***********************************
Execute package for build-target-bins.sh on rdn2[rdn2][busybox]
~/rd-infra ~/rd-infra
~/rd-infra
Packaging target binaries 
~/rd-infra/output/rdn2/components ~/rd-infra
Using TBBR spec terminology for image name identifiers
fip_param is --tb-fw /home/ubuntu/rd-infra/output/rdn2/components/rdn2/tf-bl2.bin --scp-fw /home/ubuntu/rd-infra/output/rdn2/components/rdn2/scp_ramfw.bin --tos-fw /home/ubuntu/rd-infra/output/rdn2/components/css-common/mm_standalone.bin   --fw-config /home/ubuntu/rd-infra/output/rdn2/components/rdn2/rdn2_fw_config.dtb --tb-fw-config /home/ubuntu/rd-infra/output/rdn2/components/rdn2/rdn2_tb_fw_config.dtb --nt-fw-config /home/ubuntu/rd-infra/output/rdn2/components/rdn2/rdn2_nt_fw_config.dtb  --tos-fw-config /home/ubuntu/rd-infra/output/rdn2/components/rdn2/rdn2_stmm_sel0_manifest.dtb --soc-fw /home/ubuntu/rd-infra/output/rdn2/components/rdn2/tf-bl31.bin
NOTICE:  CoT Generation Tool: Built : 14:53:02, Jan 12 2024
NOTICE:  Target platform: TBBR Generic
NOTICE:  Creating new key for 'Trusted World key'
NOTICE:  Creating new key for 'Non Trusted World key'
NOTICE:  Creating new key for 'SCP Firmware Content Certificate key'
NOTICE:  Creating new key for 'SoC Firmware Content Certificate key'
NOTICE:  Creating new key for 'Trusted OS Firmware Content Certificate key'
NOTICE:  Creating new key for 'Non Trusted Firmware Content Certificate key'
Trusted Boot Firmware BL2: offset=0x330, size=0x15E31, cmdline="--tb-fw"
SCP Firmware SCP_BL2: offset=0x16161, size=0x21DD4, cmdline="--scp-fw"
EL3 Runtime Firmware BL31: offset=0x37F35, size=0x186A1, cmdline="--soc-fw"
Secure Payload BL32 (Trusted OS): offset=0x505D6, size=0x280000, cmdline="--tos-fw"
Non-Trusted Firmware BL33: offset=0x2D05D6, size=0x200000, cmdline="--nt-fw"
FW_CONFIG: offset=0x4D05D6, size=0x190, cmdline="--fw-config"
TB_FW_CONFIG: offset=0x4D0766, size=0xE8, cmdline="--tb-fw-config"
TOS_FW_CONFIG: offset=0x4D084E, size=0x5EF, cmdline="--tos-fw-config"
NT_FW_CONFIG: offset=0x4D0E3D, size=0x791, cmdline="--nt-fw-config"
Trusted key certificate: offset=0x4D15CE, size=0x616, cmdline="--trusted-key-cert"
SCP Firmware key certificate: offset=0x4D1BE4, size=0x4DA, cmdline="--scp-fw-key-cert"
SoC Firmware key certificate: offset=0x4D20BE, size=0x4DA, cmdline="--soc-fw-key-cert"
Trusted OS Firmware key certificate: offset=0x4D2598, size=0x4E8, cmdline="--tos-fw-key-cert"
Non-Trusted Firmware key certificate: offset=0x4D2A80, size=0x4EB, cmdline="--nt-fw-key-cert"
Trusted Boot Firmware BL2 certificate: offset=0x4D2F6B, size=0x4BE, cmdline="--tb-fw-cert"
SCP Firmware content certificate: offset=0x4D3429, size=0x3E9, cmdline="--scp-fw-cert"
SoC Firmware content certificate: offset=0x4D3812, size=0x430, cmdline="--soc-fw-cert"
Trusted OS Firmware content certificate: offset=0x4D3C42, size=0x4CE, cmdline="--tos-fw-cert"
Non-Trusted Firmware content certificate: offset=0x4D4110, size=0x441, cmdline="--nt-fw-cert"
Execute package for build-target-bins.sh on rdn2[rdn2][busybox] done.
-----------------------------------


-------------------------------------
Preparing disk image for busybox boot
-------------------------------------
~/rd-infra/grub/output ~/rd-infra
grep: /home/ubuntu/.mtoolsrc: No such file or directory
2048+0 records in
2048+0 records out
1048576 bytes (1.0 MB, 1.0 MiB) copied, 0.00230828 s, 454 MB/s
40960+0 records in
40960+0 records out
20971520 bytes (21 MB, 20 MiB) copied, 0.0450279 s, 466 MB/s
mkfs.fat 4.2 (2021-01-31)
FAT partition image created
409600+0 records in
409600+0 records out
209715200 bytes (210 MB, 200 MiB) copied, 0.450419 s, 466 MB/s
mke2fs 1.46.5 (30-Dec-2021)
Discarding device blocks: done                            
Creating filesystem with 51200 4k blocks and 51200 inodes
Filesystem UUID: 535add81-5875-4b4a-b44a-464aee5f5cbd
Superblock backups stored on blocks: 
	32768

Allocating group tables: done                            
Writing inode tables: done                            
Creating journal (4096 blocks): done
Copying files into the device: done
Writing superblocks and filesystem accounting information: done

EXT3 partition image created
GPT fdisk (gdisk) version 1.0.8

Partition table scan:
  MBR: not present
  BSD: not present
  APM: not present
  GPT: not present

Creating new GPT entries in memory.

Command (? for help): Partition number (1-128, default 1): First sector (34-454622, default = 2048) or {+-}size{KMGTP}: Last sector (2048-454622, default = 454622) or {+-}size{KMGTP}: Current type is 8300 (Linux filesystem)
Hex code or GUID (L to show codes, Enter = 8300): Changed type of partition to 'Microsoft basic data'

Command (? for help): 
Final checks complete. About to write GPT data. THIS WILL OVERWRITE EXISTING
PARTITIONS!!

Do you want to proceed? (Y/N): OK; writing new GUID partition table (GPT) to grub-busybox.img.
Warning: The kernel is still using the old partition table.
The new table will be used at the next reboot or after you
run partprobe(8) or kpartx(8)
The operation has completed successfully.
GPT fdisk (gdisk) version 1.0.8

Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present

Found valid GPT with protective MBR; using GPT.

Command (? for help): Partition number (2-128, default 2): First sector (34-454622, default = 43008) or {+-}size{KMGTP}: Last sector (43008-454622, default = 454622) or {+-}size{KMGTP}: Current type is 8300 (Linux filesystem)
Hex code or GUID (L to show codes, Enter = 8300): Changed type of partition to 'Linux filesystem'

Command (? for help): 
Final checks complete. About to write GPT data. THIS WILL OVERWRITE EXISTING
PARTITIONS!!

Do you want to proceed? (Y/N): OK; writing new GUID partition table (GPT) to grub-busybox.img.
Warning: The kernel is still using the old partition table.
The new table will be used at the next reboot or after you
run partprobe(8) or kpartx(8)
The operation has completed successfully.
GPT fdisk (gdisk) version 1.0.8

Partition table scan:
  MBR: protective
  BSD: not present
  APM: not present
  GPT: present

Found valid GPT with protective MBR; using GPT.

Command (? for help): 
Expert command (? for help): Partition number (1-2): Enter the partition's new unique GUID ('R' to randomize): New GUID is 535ADD81-5875-4B4A-B44A-464AEE5F5CBD

Expert command (? for help): 
Final checks complete. About to write GPT data. THIS WILL OVERWRITE EXISTING
PARTITIONS!!

Do you want to proceed? (Y/N): OK; writing new GUID partition table (GPT) to grub-busybox.img.
Warning: The kernel is still using the old partition table.
The new table will be used at the next reboot or after you
run partprobe(8) or kpartx(8)
The operation has completed successfully.
Completed preparation of disk image for busybox boot
----------------------------------------------------
```

The script first confirmed that the firmware was already built, firmware was marshalled, signing keys generated and firmware signed, firmware image files created and finally a busy-box ramdisk created.

Verify the package was created successfully:
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra | 2" }
ls output/rdn2/
components  grub-busybox.img  ramdisk-busybox.img  rdn2
```

Examining the full build directory with:
```bash { command_line="ubuntu@ip-10-0-0-164:~/rd-infra | 2-14" }
ls output/rdn2/rdn2/ -l
total 4948
-rw-r--r-- 1 ubuntu ubuntu 5064017 Jan 12 15:35 fip-uefi.bin
lrwxrwxrwx 1 ubuntu ubuntu      25 Jan 12 15:35 Image -> ../components/linux/Image
lrwxrwxrwx 1 ubuntu ubuntu      35 Jan 12 15:35 Image.defconfig -> ../components/linux/Image.defconfig
lrwxrwxrwx 1 ubuntu ubuntu      26 Jan 12 15:35 lkvm -> ../components/kvmtool/lkvm
lrwxrwxrwx 1 ubuntu ubuntu      32 Jan 12 15:35 mcp_ramfw.bin -> ../components/rdn2/mcp_ramfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      32 Jan 12 15:35 mcp_romfw.bin -> ../components/rdn2/mcp_romfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      32 Jan 12 15:35 scp_ramfw.bin -> ../components/rdn2/scp_ramfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      32 Jan 12 15:35 scp_romfw.bin -> ../components/rdn2/scp_romfw.bin
lrwxrwxrwx 1 ubuntu ubuntu      29 Jan 12 15:35 tf-bl1.bin -> ../components/rdn2/tf-bl1.bin
lrwxrwxrwx 1 ubuntu ubuntu      29 Jan 12 15:35 tf-bl2.bin -> ../components/rdn2/tf-bl2.bin
lrwxrwxrwx 1 ubuntu ubuntu      30 Jan 12 15:35 tf-bl31.bin -> ../components/rdn2/tf-bl31.bin
lrwxrwxrwx 1 ubuntu ubuntu      33 Jan 12 15:35 uefi.bin -> ../components/css-common/uefi.bin
```

The `fip-uefi.bin` firmware image will contain the `TF-A BL2` boot loader image which is responsible for unpacking all the rest of the firmware as well as the rest of the firmware that TF-A BL2 unpacks.

This includes the `SCP BL2` (`scp_ramfw.bin`) image that is unpacked by the AP firmware and transferred over to the SCP TCMs using the SCP shared data store module.

Along with the FIP image, the FVP will also need the `TF-A BL1` image and the `SCP BL1` (`scp_romfw.bin`) image files.

