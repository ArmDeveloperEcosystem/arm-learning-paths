# SPDX-License-Identifier: Apache-2.0
cmake_minimum_required(VERSION 3.20.0)
find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(pb2_m4_heartbeat)
target_sources(app PRIVATE src/main.c src/resource_table.c)
