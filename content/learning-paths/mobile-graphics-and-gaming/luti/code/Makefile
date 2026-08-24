#
# SPDX-FileCopyrightText: Copyright 2026 Arm Limited and/or its affiliates <open-source-office@arm.com>
#
# SPDX-License-Identifier: Apache-2.0
#

TARGET := sme2_luti
ANDROID_TARGET := sme2_luti_android
ZREG_EXPERIMENT_TARGET := sme2_luti_zreg_experiment

EXAMPLE_1_SOURCE := example_1_luti_sme2.c
MACOS_EXAMPLE_1_OBJECT := example_1_luti_sme2_macos.o
ANDROID_EXAMPLE_1_OBJECT := example_1_luti_sme2_android.o
COMMON_SOURCES := luti_sme2_programming.c luti_sme2_programming_test.c

CFLAGS ?= -O2 -Wall -Wextra -Werror
# NDK r29's Clang 21 miscompiles the chained LUTI4-to-LUTI2 example when
# optimization is enabled, so keep Android builds unoptimized.
ANDROID_CFLAGS ?= -O0 -Wall -Wextra -Werror
MACOS_LLVM_MIN_VERSION := 22
MACOS_APPLE_CLANG_MIN_VERSION := 21
ANDROID_LLVM_MIN_VERSION := 21

# Native macOS build settings. Prefer Homebrew LLVM and fall back to the
# active Xcode Apple Clang when Homebrew LLVM is not installed.
MACOS_LLVM_CC ?= $(firstword $(wildcard /opt/homebrew/opt/llvm/bin/clang /usr/local/opt/llvm/bin/clang))
MACOS_APPLE_CLANG_CC ?= $(shell xcrun --find clang 2>/dev/null)
MACOS_CC ?= $(if $(MACOS_LLVM_CC),$(MACOS_LLVM_CC),$(MACOS_APPLE_CLANG_CC))
MACOS_SDKROOT ?= $(shell xcrun --show-sdk-path 2>/dev/null)
MACOS_SME_CFLAGS ?= -march=native+sme2+nosve2+nosve -isysroot $(MACOS_SDKROOT)
MACOS_ZREG_SME_CFLAGS ?= -march=native+sme2+lut+nosve2+nosve -isysroot $(MACOS_SDKROOT)

# Android cross-build settings. The NDK provides an LLVM/Clang wrapper for
# the selected API level and the target AArch64 Android sysroot.
ANDROID_API ?= 35
ANDROID_NDK_HOME ?= $(NDK)
HOST_OS := $(shell uname -s)
ifeq ($(HOST_OS),Darwin)
ANDROID_HOST_TAG ?= darwin-x86_64
else ifeq ($(HOST_OS),Linux)
ANDROID_HOST_TAG ?= linux-x86_64
else
ANDROID_HOST_TAG ?= unsupported
endif
ANDROID_TOOLCHAIN := $(ANDROID_NDK_HOME)/toolchains/llvm/prebuilt/$(ANDROID_HOST_TAG)
ANDROID_CC := $(ANDROID_TOOLCHAIN)/bin/aarch64-linux-android$(ANDROID_API)-clang
ANDROID_SME_CFLAGS ?= -march=armv9.2-a+sme2

.PHONY: all macos android clean check-llvm check-macos-llvm \
	check-android-llvm run test zreg-luti-experiment

all: macos

macos: check-macos-llvm $(TARGET)

check-llvm: check-macos-llvm

check-macos-llvm:
	@if [ "$(HOST_OS)" != "Darwin" ]; then \
		echo "error: the native target requires macOS; use 'make android' to cross-compile for Android" >&2; \
		exit 1; \
	fi
	@if [ ! -x "$(MACOS_CC)" ]; then \
		echo "error: a macOS Clang compiler was not found; install Homebrew LLVM or the Xcode Command Line Tools, or set MACOS_CC" >&2; \
		exit 1; \
	fi
	@version="$$($(MACOS_CC) --version 2>/dev/null)"; \
	major="$$($(MACOS_CC) -dumpversion 2>/dev/null | sed 's/\..*//')"; \
	case "$$version" in \
		*"Apple clang"*) compiler="Apple Clang"; minimum=$(MACOS_APPLE_CLANG_MIN_VERSION) ;; \
		*) compiler="LLVM Clang"; minimum=$(MACOS_LLVM_MIN_VERSION) ;; \
	esac; \
	case "$$major" in \
		''|*[!0-9]*) valid=no ;; \
		*) valid=yes ;; \
	esac; \
	if [ "$$valid" != yes ] || [ "$$major" -lt "$$minimum" ]; then \
		echo "error: $$compiler $$minimum or newer is required for macOS; found '$$major' from $(MACOS_CC)" >&2; \
		exit 1; \
	fi

$(TARGET): $(COMMON_SOURCES) $(MACOS_EXAMPLE_1_OBJECT)
	$(MACOS_CC) $(CFLAGS) $(MACOS_SME_CFLAGS) $^ -o $@

$(MACOS_EXAMPLE_1_OBJECT): $(EXAMPLE_1_SOURCE)
	$(MACOS_CC) $(CFLAGS) $(MACOS_SME_CFLAGS) -Dmain=ex1_luti_test -c $< -o $@

run test: macos
	./$(TARGET)

android: check-android-llvm $(ANDROID_TARGET)

check-android-llvm:
	@if [ "$(ANDROID_HOST_TAG)" = "unsupported" ]; then \
		echo "error: Android cross-compilation is supported from macOS and Linux hosts" >&2; \
		exit 1; \
	fi
	@if [ -z "$(ANDROID_NDK_HOME)" ]; then \
		echo "error: set ANDROID_NDK_HOME (or NDK) to your Android NDK directory" >&2; \
		exit 1; \
	fi
	@if [ ! -x "$(ANDROID_CC)" ]; then \
		echo "error: Android LLVM Clang was not found at $(ANDROID_CC)" >&2; \
		exit 1; \
	fi
	@major="$$($(ANDROID_CC) -dumpversion 2>/dev/null | sed 's/\..*//')"; \
	case "$$major" in \
		''|*[!0-9]*) valid=no ;; \
		*) valid=yes ;; \
	esac; \
	if [ "$$valid" != yes ] || [ "$$major" -lt $(ANDROID_LLVM_MIN_VERSION) ]; then \
		echo "error: Android NDK LLVM $(ANDROID_LLVM_MIN_VERSION) or newer is required; found '$$major' from $(ANDROID_CC)" >&2; \
		exit 1; \
	fi

$(ANDROID_TARGET): $(COMMON_SOURCES) $(ANDROID_EXAMPLE_1_OBJECT)
	$(ANDROID_CC) $(ANDROID_CFLAGS) $(ANDROID_SME_CFLAGS) $^ -o $@

$(ANDROID_EXAMPLE_1_OBJECT): $(EXAMPLE_1_SOURCE)
	$(ANDROID_CC) $(ANDROID_CFLAGS) $(ANDROID_SME_CFLAGS) -Dmain=ex1_luti_test -c $< -o $@

zreg-luti-experiment: check-macos-llvm $(COMMON_SOURCES) $(MACOS_EXAMPLE_1_OBJECT)
	$(MACOS_CC) $(CFLAGS) $(MACOS_ZREG_SME_CFLAGS) \
		-DENABLE_ZREG_LUTI_EXPERIMENT $(COMMON_SOURCES) \
		$(MACOS_EXAMPLE_1_OBJECT) -o $(ZREG_EXPERIMENT_TARGET)

clean:
	$(RM) $(TARGET) $(ANDROID_TARGET) $(ZREG_EXPERIMENT_TARGET) \
		$(MACOS_EXAMPLE_1_OBJECT) $(ANDROID_EXAMPLE_1_OBJECT) \
		example_1_luti_sme2_test.o