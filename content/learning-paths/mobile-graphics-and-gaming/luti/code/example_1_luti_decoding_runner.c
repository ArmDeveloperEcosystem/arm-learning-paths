/*
 * SPDX-FileCopyrightText: Copyright 2026 Arm Limited and/or its affiliates <open-source-office@arm.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#include <stdio.h>

#if defined(__APPLE__)
#include <sys/types.h>
#include <sys/sysctl.h>
#elif defined(__linux__)
#include <asm/hwcap.h>
#include <sys/auxv.h>

#ifndef HWCAP2_SME2
#define HWCAP2_SME2 (1UL << 37)
#endif
#endif

int example_1_luti_decoding_test(void);

static int has_sme2(void) {
#if defined(__APPLE__)
    int supported = 0;
    size_t size = sizeof(supported);
    return sysctlbyname("hw.optional.arm.FEAT_SME2", &supported, &size, NULL, 0) == 0 && supported;
#elif defined(__linux__)
    return (getauxval(AT_HWCAP2) & HWCAP2_SME2) != 0;
#else
    return 0;
#endif
}

int main(void) {
    if (!has_sme2()) {
        puts("SKIP: No support for SME2 on this device.");
        return 0;
    }

    return example_1_luti_decoding_test();
}
