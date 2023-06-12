---
title: "sysinit.c"
weight: 6

# FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Create `sysinit.c`

The `sysinit.c` contains hardware initialisation code - specifically,
a function called `SysInit()`. When MCU boots, the startup code from a
startup file calls `SysInit()` first, then it calls user-defined `main()`.
The `SysInit()` function sets up system clock - in our case, we set it to the
maximum for the board.

Create a new file `sysinit.c` and copy/paste the following contents inside:

```c
// Copyright (c) 2022-2023 Cesanta Software Limited
#include "hal.h"

uint32_t SystemCoreClock = CPU_FREQUENCY;

static inline unsigned int div2prescval(unsigned int div) {
  // 0 --> /1; 8 --> /2 ... 11 --> /16;  12 --> /64 ... 15 --> /512
  if (div == 1) return 0;
  if (div > 16) div /= 2;
  unsigned int val = 7;
  while (div >>= 1) ++val;
  return val;
}

static inline unsigned int pllrge(unsigned int f) {
  unsigned int val = 0;
  while (f >>= 1) ++val;
  return val - 1;
}

void SystemInit(void) {  // Called automatically by startup code
  SCB->CPACR |= ((3UL << 10 * 2) | (3UL << 11 * 2));  // Enable FPU
  asm("DSB");
  asm("ISB");
  PWR->CR3 |= BIT(1);                           // select LDO (reset value)
  while ((PWR->CSR1 && BIT(13)) == 0) spin(1);  // ACTVOSRDY
  PWR->D3CR |= BIT(15) | BIT(14);               // Select VOS1
  uint32_t f = PWR->D3CR;  // fake read to wait for bus clocking
  while ((PWR->CSR1 && BIT(13)) == 0) spin(1);  // ACTVOSRDY
  SYSCFG->PWRCR |= BIT(0);                      // ODEN
  f = SYSCFG->PWRCR;
  while ((PWR->CSR1 && BIT(13)) == 0) spin(1);  // ACTVOSRDY
  (void) f;
  SETBITS(
      RCC->D1CFGR, (0x0F << 8) | (7 << 4) | (0x0F << 0),
      (div2prescval(D1CPRE) << 8) | (D1PPRE << 4) | (div2prescval(HPRE) << 0));
  RCC->D2CFGR = (D2PPRE2 << 8) | (D2PPRE1 << 4);
  RCC->D3CFGR = (D3PPRE << 4);
  SETBITS(RCC->PLLCFGR, 3 << 2,
          pllrge(PLL1_HSI / PLL1_M)
              << 2);  // keep reset config (DIVP1EN, !PLL1VCOSEL), PLL1RGE
  SETBITS(RCC->PLL1DIVR, (0x7F << 9) | (0x1FF << 0),
          ((PLL1_P - 1) << 9) | ((PLL1_N - 1) << 0));  // Set PLL1_P PLL1_N
  SETBITS(RCC->PLLCKSELR, 0x3F << 4,
          PLL1_M << 4);  // Set PLL1_M (source defaults to HSI)
  RCC->CR |= BIT(24);    // Enable PLL1
  while ((RCC->CR & BIT(25)) == 0) spin(1);  // Wait until done
  RCC->CFGR |= (3 << 0);                     // Set clock source to PLL1
  while ((RCC->CFGR & (7 << 3)) != (3 << 3)) spin(1);  // Wait until done
  FLASH->ACR |= FLASH_LATENCY;                         // default is larger
#if 0
  // Enable SRAM block if you want to use it for ETH buffer (needs proper attributes in driver code)
  // RCC->AHB2ENR |= BIT(29) | BIT(30) | BIT(31);
#endif

  RCC->APB4ENR |= RCC_APB4ENR_SYSCFGEN;  // Enable SYSCFG
  rng_init();                            // Initialise random number generator
  SysTick_Config(CPU_FREQUENCY / 1000);  // Sys tick every 1ms
}
```

Note: the for F7 Nucleo board, use this `sysinit.c`:

```c
// Copyright (c) 2022-2023 Cesanta Software Limited
#include "hal.h"

uint32_t SystemCoreClock = SYS_FREQUENCY;

void SystemInit(void) {  // Called automatically by startup code
  SCB->CPACR |= ((3UL << 10 * 2) | (3UL << 11 * 2));  // Enable FPU
  asm("DSB");
  asm("ISB");
  FLASH->ACR |= FLASH_LATENCY | BIT(8) | BIT(9);    // Flash latency, prefetch
  RCC->PLLCFGR &= ~((BIT(17) - 1));                 // Clear PLL multipliers
  RCC->PLLCFGR |= (((PLL_P - 2) / 2) & 3) << 16;    // Set PLL_P
  RCC->PLLCFGR |= PLL_M | (PLL_N << 6);             // Set PLL_M and PLL_N
  RCC->CR |= BIT(24);                               // Enable PLL
  while ((RCC->CR & BIT(25)) == 0) spin(1);         // Wait until done
  RCC->CFGR = (APB1_PRE << 10) | (APB2_PRE << 13);  // Set prescalers
  RCC->CFGR |= 2;                                   // Set clock source to PLL
  while ((RCC->CFGR & 12) == 0) spin(1);            // Wait until done

  RCC->APB2ENR |= RCC_APB2ENR_SYSCFGEN;    // Enable SYSCFG
  rng_init();                              // Initialise random number generator
  SysTick_Config(SystemCoreClock / 1000);  // Sys tick every 1ms
}
```

Note: for the F4 Nucleo board, use the following `sysinit.c`:

```c
// Copyright (c) 2022-2023 Cesanta Software Limited
#include "hal.h"

uint32_t SystemCoreClock = SYS_FREQUENCY;

void SystemInit(void) {  // Called automatically by startup code
  SCB->CPACR |= ((3UL << 10 * 2) | (3UL << 11 * 2));  // Enable FPU
  asm("DSB");
  asm("ISB");
  FLASH->ACR |= FLASH_LATENCY | BIT(8) | BIT(9);    // Flash latency, prefetch
  RCC->PLLCFGR &= ~((BIT(17) - 1));                 // Clear PLL multipliers
  RCC->PLLCFGR |= (((PLL_P - 2) / 2) & 3) << 16;    // Set PLL_P
  RCC->PLLCFGR |= PLL_M | (PLL_N << 6);             // Set PLL_M and PLL_N
  RCC->CR |= BIT(24);                               // Enable PLL
  while ((RCC->CR & BIT(25)) == 0) spin(1);         // Wait until done
  RCC->CFGR = (APB1_PRE << 10) | (APB2_PRE << 13);  // Set prescalers
  RCC->CFGR |= 2;                                   // Set clock source to PLL
  while ((RCC->CFGR & 12) == 0) spin(1);            // Wait until done

  RCC->APB2ENR |= RCC_APB2ENR_SYSCFGEN;    // Enable SYSCFG
  rng_init();                              // Initialise random number generator
  SysTick_Config(SystemCoreClock / 1000);  // Sys tick every 1ms
}
```
