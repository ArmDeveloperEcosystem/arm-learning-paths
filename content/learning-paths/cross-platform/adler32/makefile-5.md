---
title: Create a Makefile 
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## How Can I Create a Makefile to Build and Run the Test Program?

Paste the following prompt into GitHub Copilot. It tells Copilot to generate a Makefile that uses `gcc` and targets the Neoverse N1 processor for optimized performance.

```console
Read the .c files in my project and 
create a Makefile to build and run the adler32-test program using gcc. 
Select the best compiler flags for Neoverse N1 to optimize for performance.
```

The output is:

```output

GitHub Copilot: I'll create a Makefile for your Adler-32 project that's optimized for the Neoverse N1 architecture. First, let's look at the project structure and understand the code files better.I see that the file search didn't return results. Let's try again with a different approach.I can see the project contains three files: adler32-simple.c, adler32-simple.h, and adler32-test.c. Let's examine the code in adler32-simple.c to understand the implementation before creating the Makefile.I've examined the code files in your project:

1. adler32-simple.c - Contains the implementation of the Adler-32 checksum algorithm with functions for initialization, update, and finalization
2. adler32-simple.h - Presumably contains the function declarations
3. adler32-test.c - Contains test code for verifying and benchmarking the Adler-32 implementation

Now I'll create a Makefile optimized for performance on the Neoverse N1 architecture. The Neoverse N1 is an ARM architecture that benefits from specific compiler optimizations.

# Makefile for Adler-32 checksum implementation
# Optimized for Neoverse N1 architecture

# Compiler and flags
CC = gcc
# Neoverse N1 specific optimization flags:
# -march=armv8.2-a+crypto: Target ARMv8.2-A architecture with crypto extensions (Neoverse N1)
# -mcpu=neoverse-n1: Specifically optimize for Neoverse N1
# -O3: Highest standard optimization level
# -flto: Link-time optimization
# -fomit-frame-pointer: Don't keep the frame pointer in a register for functions that don't need one
# -ftree-vectorize: Vectorize loops when possible
# -ffast-math: Enable fast math optimizations
# Additional useful flags:
# -Wall -Wextra: Enable warnings
# -g: Include debugging symbols
CFLAGS = -march=armv8.2-a+crypto -mcpu=neoverse-n1 -O3 -flto -fomit-frame-pointer -ftree-vectorize -ffast-math -Wall -Wextra -g

# Source files
SRCS = adler32-simple.c adler32-test.c
OBJS = $(SRCS:.c=.o)
TARGET = adler32-test

# Default target
all: $(TARGET)

# Link the executable
$(TARGET): $(OBJS)
	$(CC) $(CFLAGS) -o $@ $^

# Compile source files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Run the tests
run: $(TARGET)
	./$(TARGET)

# Clean generated files
clean:
	rm -f $(OBJS) $(TARGET)

# Rebuild the project
rebuild: clean all

.PHONY: all run clean rebuild


Made changes.

I've created a Makefile for your Adler-32 project, optimized specifically for the Neoverse N1 architecture. Let me highlight some key features of this Makefile:

### Optimization Flags for Neoverse N1

The Makefile includes several compiler flags tailored for maximum performance on the Neoverse N1:

- `-march=armv8.2-a+crypto`: Targets ARMv8.2-A architecture with crypto extensions
- `-mcpu=neoverse-n1`: Specifically optimizes for the Neoverse N1 processor
- `-O3`: Enables the highest standard optimization level
- `-flto`: Enables link-time optimization for whole-program optimization
- `-fomit-frame-pointer`: Frees up a register by not keeping frame pointers when not needed
- `-ftree-vectorize`: Automatically vectorizes loops to leverage SIMD instructions
- `-ffast-math`: Enables optimizations that might affect floating-point precision but improve performance

### Building and Testing

To use the Makefile, you can run the following commands:

1. To build the project:
   make
   
2. To run the tests after building:
   make run

3. To clean the build files:
   make clean

4. To rebuild everything from scratch:
   make rebuild

The Makefile is designed to be simple but effective, automatically handling dependencies and providing different targets for common development tasks.
```

You are now ready to use the Makefile to build and run the test application.