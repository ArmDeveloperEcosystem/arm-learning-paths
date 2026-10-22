/* SPDX-License-Identifier: Apache-2.0 */
#include <zephyr/kernel.h>
#include <zephyr/sys/printk.h>

int main(void)
{
    unsigned int count = 0;

    printk("PocketBeagle 2: Zephyr on Cortex-M4F\n");
    while (1) {
        printk("M4 heartbeat %u\n", count++);
        k_sleep(K_SECONDS(1));
    }
    return 0;
}
