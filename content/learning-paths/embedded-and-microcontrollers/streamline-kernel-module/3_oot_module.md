---
title: Build the out-of-tree kernel module
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Develop a cache-unfriendly Linux kernel module to analyze with Arm Streamline

You'll create a simple Linux kernel module that acts as a character device and intentionally causes cache misses. It does this by traversing a two-dimensional array in column-major order, which is inefficient for the CPU cache because it jumps between non-adjacent memory locations. This pattern helps you see how cache-unfriendly code can slow down performance, making it easier to analyze with Arm Streamline.

To build the Linux kernel module, start by creating a new directory, for example `example_module`. Inside this directory, add two files: `Makefile` and `mychardrv.c`. 

## Makefile  

To build your Linux kernel module for Arm, you need a Makefile that instructs the build system how to compile and link your code against the kernel source. The Makefile below is designed for use with Buildroot and cross-compiles your module for the aarch64 architecture. Update the `BUILDROOT_OUT` variable to match your Buildroot output directory before running the build:

```makefile
obj-m += mychardrv.o
BUILDROOT_OUT := $(BUILDROOT_HOME)/output # Change this to your buildroot output directory
KDIR := $(BUILDROOT_OUT)/build/linux-custom
CROSS_COMPILE := $(BUILDROOT_OUT)/host/bin/aarch64-buildroot-linux-gnu-
ARCH := arm64

all:
    $(MAKE) -C $(KDIR) M=$(PWD) ARCH=$(ARCH) CROSS_COMPILE=$(CROSS_COMPILE) modules

clean:
    $(MAKE) -C $(KDIR) M=$(PWD) clean
```


## mychardrv.c  

The `mychardrv.c` file contains the source code for your custom Linux kernel module. This module implements a simple character device that demonstrates cache-unfriendly behavior by traversing a two-dimensional array in column-major order. The code below allocates and initializes the array, performs the cache-unfriendly traversal, and exposes a write interface for user input. You’ll use this module to generate measurable performance bottlenecks for analysis with Arm Streamline.

```c
// SPDX-License-Identifier: GPL-2.0
#include "linux/printk.h"
#include <linux/cdev.h>
#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/module.h>
 
// Using fixed major and minor numbers just for demonstration purposes.
// Major number 42 is for demo/sample uses according to
// https://www.kernel.org/doc/Documentation/admin-guide/devices.txt
#define MAJOR_VERSION_NUM 42
#define MINOR_VERSION_NUM 0
#define MODULE_NAME "mychardrv"
#define MAX_INPUT_LEN 64
 
static struct cdev my_char_dev;
 
/**
 * @brief Traverse a 2D matrix and calculate the sum of its elements.
 *
 * @size: The size of the matrix (number of rows and columns).
 *
 * This function allocates a 2D matrix of integers, initializes it with the sum
 * of its indices, and then calculates the sum of its elements by accessing them
 * in a cache-unfriendly column-major order.
 *
 * Return: 0 on success, or -ENOMEM if memory allocation fails.
 */
int char_dev_cache_traverse(long size) {
  int i, j;
  long sum = 0;
 
  int **matrix;
 
  // Allocate rows
  matrix = kmalloc_array(size, sizeof(int *), GFP_KERNEL);
  if (!matrix)
    return -ENOMEM;
 
  // Allocate columns and initialize matrix
  for (i = 0; i < size; i++) {
    matrix[i] = kmalloc_array(size, sizeof(int), GFP_KERNEL);
    if (!matrix[i]) {
      for (int n = 0; n < i; n++) {
        kfree(matrix[n]);
      }
      kfree(matrix);
      return -ENOMEM;
    }
 
    for (j = 0; j < size; j++)
      matrix[i][j] = i + j;
  }
 
  // Access in cache-UNFRIENDLY column-major order
  for (j = 0; j < size; j++) {
    for (i = 0; i < size; i++) {
      sum += matrix[i][j];
    }
  }
 
  pr_info("Sum: %ld\n", sum);
 
  // Free memory
  for (i = 0; i < size; i++)
    kfree(matrix[i]);
  kfree(matrix);
 
  return 0;
}
 
/**
 * @brief Gets the size of the list to be created from user space.
 *
 */
static ssize_t char_dev_write(struct file *file, const char *buff,
                              size_t length, loff_t *offset) {
  (void)file;
  (void)offset;
 
  ssize_t ret = 0;
  char *kbuf;
  long size_value;
 
  // Allocate kernel buffer
  kbuf = kmalloc(MAX_INPUT_LEN, GFP_KERNEL);
  if (!kbuf)
    return -ENOMEM;
 
  // copy data from user space to kernel space
  if (copy_from_user(kbuf, buff, length)) {
    ret = -EFAULT;
    goto out;
  }
  kbuf[length] = '\0';
 
  // Convert string to long (Base 10)
  ret = kstrtol(kbuf, 10, &size_value);
  if (ret)
    goto out;
 
  // Call cache traversal function
  ret = char_dev_cache_traverse(size_value);
  if (ret)
    goto out;
 
  ret = length;
 
out:
  kfree(kbuf);
  return ret;
}
 
static int char_dev_open(struct inode *node, struct file *file) {
  (void)file;
  pr_info("%s is open - Major(%d) Minor(%d)\n", MODULE_NAME,
          MAJOR(node->i_rdev), MINOR(node->i_rdev));
  return 0;
}
 
static int char_dev_release(struct inode *node, struct file *file) {
  (void)file;
  pr_info("%s is released - Major(%d) Minor(%d)\n", MODULE_NAME,
          MAJOR(node->i_rdev), MINOR(node->i_rdev));
  return 0;
}
 
// File operations structure
static const struct file_operations dev_fops = {.owner = THIS_MODULE,
                                                .open = char_dev_open,
                                                .release = char_dev_release,
                                                .write = char_dev_write};
 
static int __init char_dev_init(void) {
  int ret;
  // Allocate Major number
  ret = register_chrdev_region(MKDEV(MAJOR_VERSION_NUM, MINOR_VERSION_NUM), 1,
                               MODULE_NAME);
  if (ret < 0)
    return ret;
 
  //  Initialize cdev structure and add it to kernel
  cdev_init(&my_char_dev, &dev_fops);
  ret = cdev_add(&my_char_dev, MKDEV(MAJOR_VERSION_NUM, MINOR_VERSION_NUM), 1);
 
  if (ret < 0) {
    unregister_chrdev_region(MKDEV(MAJOR_VERSION_NUM, MINOR_VERSION_NUM), 1);
    return ret;
  }
 
  return ret;
}
 
static void __exit char_dev_exit(void) {
  cdev_del(&my_char_dev);
  unregister_chrdev_region(MKDEV(MAJOR_VERSION_NUM, MINOR_VERSION_NUM), 1);
}
 
module_init(char_dev_init);
module_exit(char_dev_exit);
 
MODULE_LICENSE("GPL");
MODULE_AUTHOR("Yahya Abouelseoud");
MODULE_DESCRIPTION("A simple char driver with cache misses issue");
```

The module above receives the size of a 2D array as a string through the `char_dev_write()` function, converts it to an integer, and passes it to the `char_dev_cache_traverse()` function. This function then creates the 2D array, initializes it with simple data, traverses it in a column-major (cache-unfriendly) order, computes the sum of its elements, and prints the result to the kernel log. The cache-unfriendly aspects allows you to inspect a bottleneck using Streamline in the next section.

## Build and run the kernel module

To compile the kernel module, run `make` inside the `example_module` directory. This generates the output file `mychardrv.ko`.

Transfer the kernel module (`mychardrv.ko`) to your target device using the `scp` command. Then, insert the module with `insmod` and create the character device node with `mknod`. To test the module, write a size value (such as 10000) to the device file and use the `time` command to measure how long the operation takes. This lets you see the performance impact of the cache-unfriendly access pattern in a clear, hands-on way:

```bash
    scp mychardrv.ko root@<target-ip>:/root/
```

{{% notice Note %}} Replace `<target-ip>` with your target's IP address
{{% /notice %}}

SSH onto your target device:

```bash
    ssh root@<your-target-ip>
```    

Execute the following commads on the target to run the module:
```bash
    insmod /root/mychardrv.ko
    mknod /dev/mychardrv c 42 0
```

{{% notice Note %}}
    42 and 0 are the major and minor number specified in the module code above.
  {{% /notice %}}

To confirm that your kernel module is loaded and running, use the `dmesg` command. You should see a message like this in the output:


 ```bash
    dmesg
 ```

  ```output
      [12381.654983] mychardrv is open - Major(42) Minor(0)
  ```

To make sure it's working as expected you can use the following command:

```bash { output_lines = "2-4" }
    time echo '10000' > /dev/mychardrv
    #   real    0m 38.04s
    #   user    0m 0.00s
    #   sys     0m 38.03s
```
The command above sends the value 10000 to your kernel module, which sets the size of the 2D array it creates and traverses. Because the module accesses the array in a cache-unfriendly way, the `echo` command takes a noticeable amount of time to finish - it's about 38 seconds in this example. This delay is expected and highlights the performance impact of inefficient memory access patterns, making it easy to analyze with Arm Streamline.

You have successfully built and run your kernel module. In the next section, you'll profile it using Arm Streamline to capture runtime behavior, identify performance bottlenecks, and observe the effects of cache-unfriendly access patterns. This analysis will help you understand and optimize your code.
