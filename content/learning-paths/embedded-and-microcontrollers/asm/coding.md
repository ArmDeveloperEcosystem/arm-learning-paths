---
# User change
title: Writing assembly functions

weight: 6 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---
You will create a C application, but add assembly language subroutines to perform string copy and capitalization operations.

## Create main.c

If using μVision, Right-click `Source Group 1` and select `Add New Item`. Select `C file (.c)` and name it `main.c`.

If using Keil Studio, open `main.c` within the `Source Files` group.

## The main Function

Create the `main` C function. This function creates two character arrays, `a` and `b`, and calls two functions, `my_strcpy` and `my_capitalize`, that shall be implemented later.

```C
void my_strcpy(const char *src, char *dst);
void my_capitalize(char *str);

int main(void)
{
    const char a[] = "Hello world!";
    char b[20];

    my_strcpy(a, b);
    my_capitalize(b);

    return 0;
}
```
## Register usage and the Arm Procedure Call Standard

There are certain register use conventions which must be followed for the assembly code to coexist with the C code.

### Calling functions and passing arguments

When a function calls a subroutine, it places the return address in the link register `lr`. The arguments (if any) are passed in registers `r0-r3`, starting with `r0`.

If there are more than four arguments, or they are too large to fit in the 32-bit registers, they are passed on the stack.

### Temporary storage

Registers `r0-r3` and `r12` can be used for temporary storage if they were not used for arguments, or if the argument value is no longer needed. These registers are corruptible by the subroutine.

### Preserved registers

Registers `r4-r11` must be preserved by a subroutine. If any must be used, they must be saved before use, and restored before returning. This is typically done by pushing them to, and popping from, the stack.

### Returning from subroutines

Because the return address has been stored in the link register, the `BX lr` instruction will reload the `pc` with the return address value from the `lr`. If the function returns a value, it will be passed through register `r0`.

## Embedded Assembly in C

The keyword [__asm](https://developer.arm.com/documentation/101754/latest/armclang-Reference/Compiler-specific-Keywords-and-Operators/--asm) is used to implement assembly code within a wider section of C code.

This attribute tells the compiler that the function is an embedded assembly function. See the Arm Compiler for Embedded [Reference Guide](https://developer.arm.com/documentation/101754/latest/armclang-Reference/Compiler-specific-Function--Variable--and-Type-Attributes/--attribute----naked---function-attribute) for more information.


## Implement string-copy function

The function `my_strcpy` has two arguments (`src`, `dst`). Each is a 32-bit long pointer to a character array. In this case, a pointer fits into a register, so argument `src` is passed through register `r0` and `dst` is passed through `r1`.

Our function will load a character from memory, save it into the destination pointer and increment both pointers until the end of the string.

```C
__attribute__((naked)) void my_strcpy(const char *src, char *dst)
{
    __asm(
        "loop:              \n\t\
            LDRB  r2, [r0]  \n\t\
            ADDS  r0, #1    \n\t\
            STRB  r2, [r1]  \n\t\
            ADDS  r1, #1    \n\t\
            CMP   r2, #0    \n\t\
            BNE   loop      \n\t\
            BX    lr        \n\t\
    "    
    );
}
```
Observe that `r0-r2` are corrupted by this function, and will contain different values when the function returns.

## Implement string-capitalization function

You can implement a function to capitalize all the lower-case letters in the string. The function will load each character, check to see if it is a lower-case `ASCII` letter, and if so, capitalize it. 

Each character in the string is represented with its ASCII code. For example, `A` is represented with a 65 (0x41), `B` with 66 (0x42), and so on up to `Z` which uses 90 (0x5a). The lower case letters start at `a` (97, or 0x61) and end with `z` (122, or 0x7a). Convert a lower case letter to upper case by subtracting 32 (0x20).

```C
__attribute__((naked)) void my_capitalize(char *str)
{
    __asm(
        "cap_loop:             \n\t\
            LDRB  r1, [r0]     \n\t\
            CMP   r1, #'a'-1   \n\t\
            BLS   cap_skip     \n\t\
            CMP   r1, #'z'     \n\t\
            BHI   cap_skip     \n\t\
            SUBS  r1,#32       \n\t\
            STRB  r1, [r0]     \n\t\
        cap_skip:              \n\t\
            ADDS  r0, r0, #1   \n\t\
            CMP   r1, #0       \n\t\
            BNE   cap_loop     \n\t\
            BX    lr           \n\t\
        "    
    );
}
```
The code loads the first byte into `r1`. If the value is less than `a` the code immediately proceeds to the next loop iteration. 

Note the first `CMP` instruction compares `r1` against the character immediately before `a` in the table. There is no `lower than` condition, just `lower or same` (LS).

To use the conditional `BLS` branch instruction, reduce by one the value `r1` is compared against.

## Build the example

Save all files, and click the `Build` icon.

## Debug the example

Click the `Debug` icon to load the example to the FVP. The code will stop at `main()`.

Observe the values of `a` and `b` in the μVision `Call Stack + Locals` tab, or the Keil Studio `Watch` pane (click `+` to add to this view).

Initially they will have no meaningful data.

`Step` through the code and notice how the values of `a` and `b` change. Observe the string `Hello world!` copy to `b` and then capitalize.
