#
# SPDX-FileCopyrightText: Copyright 2026 Arm Limited and/or its affiliates <open-source-office@arm.com>
#
# SPDX-License-Identifier: Apache-2.0
#

EXAMPLE_1 := example_1_luti_decoding
EXAMPLE_1_ANDROID := example_1_luti_decoding_android
EXAMPLE_2 := example_2_luti_programming
EXAMPLE_2_ANDROID := example_2_luti_programming_android

EXAMPLE_1_SOURCES := example_1_luti_decoding.c example_1_luti_decoding_runner.c
EXAMPLE_2_SOURCES := example_2_luti_programming.c example_2_luti_programming_test.c

HOST_OS := $(shell uname -s)
HOST_ARCH := $(shell uname -m)
WARNINGS := -Wall -Wextra -Werror
CFLAGS ?= -O2 $(WARNINGS)
ANDROID_CFLAGS ?= -O2 $(WARNINGS)
# Do not emit ordinary SVE or SVE2 instructions outside SME streaming mode.
SME_FLAGS := -march=armv8-a+sme2+nosve2+nosve

# Native macOS build.
MACOS_LLVM ?= /opt/homebrew/opt/llvm
MACOS_CC ?= $(MACOS_LLVM)/bin/clang
MACOS_OBJDUMP ?= $(MACOS_LLVM)/bin/llvm-objdump
MACOS_SDKROOT ?= $(shell xcrun --show-sdk-path 2>/dev/null)
MACOS_FLAGS := -march=native+sme2+nosve2+nosve -isysroot "$(MACOS_SDKROOT)"

# Android AArch64 build.
ANDROID_API ?= 35
ANDROID_NDK_HOME ?= $(NDK_PATH)
ANDROID_HOST_TAG := $(if $(filter Darwin,$(HOST_OS)),darwin-x86_64,linux-x86_64)
ANDROID_TOOLCHAIN := $(ANDROID_NDK_HOME)/toolchains/llvm/prebuilt/$(ANDROID_HOST_TAG)

ifeq ($(HOST_OS),Darwin)
ANDROID_CC ?= $(MACOS_LLVM)/bin/clang
ANDROID_OBJDUMP ?= $(MACOS_LLVM)/bin/llvm-objdump
ANDROID_LD ?= $(ANDROID_TOOLCHAIN)/bin/ld.lld
else
ANDROID_CC ?= clang-22
ANDROID_OBJDUMP ?= llvm-objdump-22
# Use native LLD on both Linux architectures; the NDK tools are x86-64 only.
ANDROID_LD ?= $(shell command -v ld.lld-22 2>/dev/null)
endif

# Use LLVM 22 intrinsic headers with NDK r29 compiler-rt libraries.
ANDROID_NDK_RESOURCE := $(ANDROID_TOOLCHAIN)/lib/clang/21
ANDROID_CLANG_INCLUDE = $(shell "$(ANDROID_CC)" --no-default-config -print-resource-dir 2>/dev/null)/include
ANDROID_FLAGS = --no-default-config --target=aarch64-linux-android$(ANDROID_API) \
	--sysroot="$(ANDROID_TOOLCHAIN)/sysroot" \
	-resource-dir "$(ANDROID_NDK_RESOURCE)" \
	-nobuiltininc -isystem "$(ANDROID_CLANG_INCLUDE)"
ANDROID_LDFLAGS = --ld-path="$(ANDROID_LD)" --rtlib=compiler-rt

.PHONY: all clean check-macos check-android
.PHONY: disassemble-example-1 disassemble-example-1-android

all: $(EXAMPLE_1)

check-macos:
	@test "$(HOST_OS)-$(HOST_ARCH)" = Darwin-arm64 || \
		{ echo "error: native builds require an Apple Silicon Mac" >&2; exit 1; }

check-android:
	@test -n "$(ANDROID_NDK_HOME)" && test -d "$(ANDROID_TOOLCHAIN)/sysroot" || \
		{ echo "error: set ANDROID_NDK_HOME to the NDK r29 directory" >&2; exit 1; }

$(EXAMPLE_1): $(EXAMPLE_1_SOURCES) | check-macos
	"$(MACOS_CC)" $(CFLAGS) $(MACOS_FLAGS) $^ -o $@

$(EXAMPLE_1_ANDROID): $(EXAMPLE_1_SOURCES) | check-android
	"$(ANDROID_CC)" $(ANDROID_CFLAGS) $(SME_FLAGS) $(ANDROID_FLAGS) \
		$(ANDROID_LDFLAGS) $^ -o $@

$(EXAMPLE_2): $(EXAMPLE_2_SOURCES) | check-macos
	"$(MACOS_CC)" $(CFLAGS) $(MACOS_FLAGS) $^ -o $@

$(EXAMPLE_2_ANDROID): $(EXAMPLE_2_SOURCES) | check-android
	"$(ANDROID_CC)" $(ANDROID_CFLAGS) $(SME_FLAGS) $(ANDROID_FLAGS) \
		$(ANDROID_LDFLAGS) $^ -o $@

disassemble-example-1: $(EXAMPLE_1)
	"$(MACOS_OBJDUMP)" -d $< | \
		grep -E '[[:space:]](luti2|smopa)[[:space:]]'

disassemble-example-1-android: $(EXAMPLE_1_ANDROID)
	"$(ANDROID_OBJDUMP)" -d $< | \
		grep -E '[[:space:]](luti2|smopa)[[:space:]]'

clean:
	$(RM) $(EXAMPLE_1) $(EXAMPLE_1_ANDROID) $(EXAMPLE_2) $(EXAMPLE_2_ANDROID)
