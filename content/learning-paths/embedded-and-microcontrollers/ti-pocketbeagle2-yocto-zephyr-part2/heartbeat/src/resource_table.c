/* SPDX-License-Identifier: Apache-2.0 */
#include <stdint.h>

/* Linux remoteproc table version 1, with no RPMsg devices or trace entries. */
static const struct {
    uint32_t version;
    uint32_t num;
    uint32_t reserved[2];
} resource_table __attribute__((section(".resource_table"), used, aligned(4))) = {
    .version = 1,
    .num = 0,
    .reserved = { 0, 0 },
};
