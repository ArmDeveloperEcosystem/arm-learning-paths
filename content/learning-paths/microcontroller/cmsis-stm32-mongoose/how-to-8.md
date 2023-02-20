---
title: "Web Server"
weight: 8

# FIXED, DO NOT MODIFY
layout: "learningpathall"
---

## Web server firmware

On this step, we upgrade our Blinky firmware to run a web server. In order
to create a network-enabled firmware, the following components are required:

- a network driver, which sends/receives Ethernet frames to/from MAC controller
- a network stack, that parses frames and understands TCP/IP
- a network library that understands HTTP

We will use Mongoose Network Library which implements all of that in a single
file. It is a dual-licensed library (GPLv2/commercial) that was designed to
make network embedded development fast and easy.

Copy
[mongoose.c](https://raw.githubusercontent.com/cesanta/mongoose/7.9/mongoose.c)
and
[mongoose.h](https://raw.githubusercontent.com/cesanta/mongoose/7.9/mongoose.h)
to our project. Now we have a driver, a network stack, and a library at hand.

Modify `main.c` file to look like this:

```c
// Copyright (c) 2023 Cesanta Software Limited
// All rights reserved

#include "hal.h"
#include "mongoose.h"

#define LED2 PIN('E', 1)   // On-board LED pin (yellow)
#define LED LED2              // Use blue LED for blinking
#define BLINK_PERIOD_MS 1000  // LED blinking period in millis

static volatile uint64_t s_ticks;  // Milliseconds since boot
void SysTick_Handler(void) {       // SyStick IRQ handler, triggered every 1ms
  s_ticks++;
}

uint64_t mg_millis(void) {  // Let Mongoose use our uptime function
  return s_ticks;           // Return number of milliseconds since boot
}

void mg_random(void *buf, size_t len) {  // Use on-board RNG
  for (size_t n = 0; n < len; n += sizeof(uint32_t)) {
    uint32_t r = rng_read();
    memcpy((char *) buf + n, &r, n + sizeof(r) > len ? len - n : sizeof(r));
  }
}

static void timer_fn(void *arg) {
  gpio_toggle(LED);                               // Blink LED
  struct mg_tcpip_if *ifp = arg;                  // And show
  const char *names[] = {"down", "up", "ready"};  // network stats
  MG_INFO(("Ethernet: %s, IP: %M, rx:%u, tx:%u, dr:%u, er:%u",
           names[ifp->state], mg_print_ip4, &ifp->ip, ifp->nrecv, ifp->nsent,
           ifp->ndrop, ifp->nerr));
}

static void fn(struct mg_connection *c, int ev, void *ev_data, void *fn_data) {
  if (ev == MG_EV_HTTP_MSG) {
    mg_http_reply(c, 200, "", "hi\n");
  }
}

static void ethernet_init(void) {
  // Initialise Ethernet. Enable MAC GPIO pins, see
  // https://www.st.com/resource/en/user_manual/um2407-stm32h7-nucleo144-boards-mb1364-stmicroelectronics.pdf
  uint16_t pins[] = {PIN('A', 1),  PIN('A', 2),  PIN('A', 7),
                     PIN('B', 13), PIN('C', 1),  PIN('C', 4),
                     PIN('C', 5),  PIN('G', 11), PIN('G', 13)};
  for (size_t i = 0; i < sizeof(pins) / sizeof(pins[0]); i++) {
    gpio_init(pins[i], GPIO_MODE_AF, GPIO_OTYPE_PUSH_PULL, GPIO_SPEED_INSANE,
              GPIO_PULL_NONE, 11);  // 11 is the Ethernet function
  }
  NVIC_EnableIRQ(ETH_IRQn);                     // Setup Ethernet IRQ handler
  SETBITS(SYSCFG->PMCR, 7 << 21, 4 << 21);      // Use RMII (12.3.1)
  RCC->AHB1ENR |= BIT(15) | BIT(16) | BIT(17);  // Enable Ethernet clocks
}

int main(void) {
  gpio_output(LED);               // Setup green LED
  uart_init(UART_DEBUG, 115200);  // Initialise debug printf
  ethernet_init();                // Initialise ethernet pins

  MG_INFO(("Chip revision: %c, max cpu clock: %u MHz", chiprev(),
           (chiprev() == 'V') ? 480 : 400));
  MG_INFO(("Starting, CPU freq %g MHz", (double) SystemCoreClock / 1000000));

  struct mg_mgr mgr;        // Initialise
  mg_mgr_init(&mgr);        // Mongoose event manager
  mg_log_set(MG_LL_DEBUG);  // Set log level

  // Initialise Mongoose network stack
  // Specify MAC address, and IP/mask/GW in network byte order for static
  // IP configuration. If IP/mask/GW are unset, DHCP is going to be used
  struct mg_tcpip_driver_stm32h_data driver_data = {.mdc_cr = 4};
  struct mg_tcpip_if mif = {.mac = GENERATE_LOCALLY_ADMINISTERED_MAC(),
                            .driver = &mg_tcpip_driver_stm32h,
                            .driver_data = &driver_data};
  mg_tcpip_init(&mgr, &mif);
  mg_timer_add(&mgr, BLINK_PERIOD_MS, MG_TIMER_REPEAT, timer_fn, &mif);

  MG_INFO(("MAC: %M. Waiting for IP...", mg_print_mac, mif.mac));
  while (mif.state != MIP_STATE_READY) {
    mg_mgr_poll(&mgr, 0);
  }

  MG_INFO(("Initialising application..."));
  mg_http_listen(&mgr, "http://0.0.0.0", fn, NULL);

  MG_INFO(("Starting event loop"));
  for (;;) {
    mg_mgr_poll(&mgr, 0);
  }

  return 0;
}
```

The main pieces in this code are:

- `ethernet_init()` - an ethernet initialisation function
- `fn` - a web server event handler function. It responds with "hi" on any request
- `mg_http_listen()` - sets up HTTP listener on port 80

## Build and flash

Plug in your board to the Ethernet switch. Rebuild and reflash our firmware:

```
make flash
```

On the serial monitor, we could observe how our board acquires an IP address
from DHCP:

```
7ec    2 main.c:34:timer_fn             Ethernet: up, IP: 0.0.0.0, rx:0, tx:1, dr:0, er:0
805    3 mongoose.c:7815:rx_ip          UDP 192.168.0.1:67 -> 192.168.0.171:68 len 548
80c    2 mongoose.c:7348:onstatechange  READY, IP: 192.168.0.171
812    2 mongoose.c:7349:onstatechange         GW: 192.168.0.1
```

There, we can see an IP address acquired by our board. Fire a browser
and type that IP address in the address line: http://IP

You should see "hi" printed on a browser window. Congratulations!
