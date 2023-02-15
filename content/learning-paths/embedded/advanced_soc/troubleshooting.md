---
# User change
title: "Troubleshooting - Makefile errors in Vitis" 

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

Double check if the 3 Makefiles in the project wrapper files which you can access from the explorer tab in Vitis:

•	If you did not create a custom AXI4 peripheral, then the paths are as follows:
1.	hw/drivers/axi_gpio_asoc_v1_0/src/Makefile
2.	ps7_cortexa9_0/standalone_ ps7_cortexa9_0/bsp/ ps7_cortexa9_0/libsrc/ axi_gpio_asoc_v1_0/src/Makefile
3.	zynq_fsbl/zynq_fsbl_bsp/ps7_cortexa9_0/libsrc/axi_gpio_asoc_v1_0/src/Makefile

•	If you created a custom AXI4 peripheral, then the paths are (assuming your IP name is AUP_advanced_SoC_v1_0):
1.	hw/drivers/<AUP_advanced_SoC_v1_0>/src/Makefile
2.	ps7_cortexa9_0/standalone_ ps7_cortexa9_0/bsp/ ps7_cortexa9_0/libsrc/ < AUP_advanced_SoC_v1_0>/src/Makefile
3.	zynq_fsbl/zynq_fsbl_bsp/ps7_cortexa9_0/libsrc/<AUP_advanced_SoC_v1_0>/src/Makefile
Make the following changes (underlined in red below) so that the Makefiles are as shown below:

***Note: If you are copying and pasting the whole code snippet below into your Makefiles, please ensure that the tab indentations are correct as this may give a Makefile error.***

    
    COMPILER=
    ARCHIVER=
    CP=cp
    COMPILER_FLAGS=
    EXTRA_COMPILER_FLAGS=
    LIB=libxil.a
    RELEASEDIR=../../../lib
    INCLUDEDIR=../../../include
    INCLUDES=-I./. -I${INCLUDEDIR}
    INCLUDEFILES=*.h
    LIBSOURCES= $(wildcard *.c)
    OUTS = *.o
    OBJECTS = $(addsuffix .o, $(basename $(wildcard *.c)))
    ASSEMBLY_OBJECTS = $(addsuffix .o, $(basename $(wildcard *.S)))
    libs:
        echo "Compiling axi_gpio_asoc..."
        $(COMPILER) $(COMPILER_FLAGS) $(EXTRA_COMPILER_FLAGS) $(INCLUDES) $(LIBSOURCES)
        $(ARCHIVER) -r ${RELEASEDIR}/${LIB} ${OBJECTS} ${ASSEMBLY_OBJECTS}
        make clean
    include:
        ${CP} $(INCLUDEFILES) $(INCLUDEDIR)
    clean:
        rm -rf ${OBJECTS} ${ASSEMBLY_OBJECTS}
    
Save all the modified changes in the Makefile.