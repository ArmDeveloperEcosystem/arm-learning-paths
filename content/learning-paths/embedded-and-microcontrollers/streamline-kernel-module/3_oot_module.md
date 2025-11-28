---
title: Build the out-of-tree kernel module
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create an out-of-tree Linux kernel module

You'll now create an example Linux kernel module (character device) that demonstrates a cache miss issue caused by traversing a 2D array in column-major order. This access pattern is not cache-friendly, as it skips over most of the neighboring elements in memory during each iteration.

To build the Linux kernel module, start by creating a new directory, for example `example_module`. Inside this directory, add two files: `mychardrv.c` and `Makefile`. 

## Makefile  

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

{{% notice Note %}}
Change `BUILDROOT_OUT` to the correct buildroot output directory on your host machine.
{{% /notice %}}

## mychardrv.c  

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

## Building and Running the Kernel Module

1. To compile the kernel module, run make inside the example_module directory. This will generate the output file `mychardrv.ko`.

2. Transfer the .ko file to the target using scp command and then insert it using insmod command. After inserting the module, you create a character device node using mknod command. Finally, you can test the module by writing a size value (e.g., 10000) to the device file and measuring the time taken for the operation using the `time` command.

    ```bash
    scp mychardrv.ko root@<target-ip>:/root/
    ```

    {{% notice Note %}}
    Replace \<target-ip> with your target's IP address
    {{% /notice %}}

3. SSH onto your target device:

    ```bash
    ssh root@<your-target-ip>
    ```    

4. Execute the following commads on the target to run the module:
    ```bash
    insmod /root/mychardrv.ko
    mknod /dev/mychardrv c 42 0
    ```

    {{% notice Note %}}
    42 and 0 are the major and minor number specified in the module code above
    {{% /notice %}}

4. To verify that the module is active, run `dmesg` and the output should match the below:

    ```bash
    dmesg
    ```

    ```output
      [12381.654983] mychardrv is open - Major(42) Minor(0)
    ```

5. To make sure it's working as expected you can use the following command:

    ```bash { output_lines = "2-4" }
    time echo '10000' > /dev/mychardrv
    #   real    0m 38.04s
    #   user    0m 0.00s
    #   sys     0m 38.03s
    ```

    The command above passes 10000 to the module, which specifies the size of the 2D array to be created and traversed. The **echo** command takes a long time to complete (around 38 seconds) due to the cache-unfriendly traversal implemented in the `char_dev_cache_traverse()` function.

Great job building and running your kernel module! Now that you have a working example, you're ready to take the next step: profiling it with Arm Streamline. In the following section, you'll use Streamline to capture runtime behavior, identify performance bottlenecks, and see firsthand how cache-unfriendly access patterns impact your module. Get ready to gain valuable insights and optimize your code!
