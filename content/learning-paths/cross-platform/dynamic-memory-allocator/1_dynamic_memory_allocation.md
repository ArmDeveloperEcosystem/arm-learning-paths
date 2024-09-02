---
title: Dynamic memory allocation
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Dynamic vs. static memory allocation

In this Learning Path you will learn how to implement dynamic memory allocation.
One example of dynamic memory allocation is if you have used the C programming language "heap" (`malloc`, `free`, etc.) before.

Dynamic memory allocation allows programs to allocate memory while they are running without knowing
at build time how much memory they will need. In contrast, static
memory allocation is used when the amount of memory is known at build time.

The code sample below shows both dynamic and static memory allocation:

```C
#include <stdlib.h>

void fn() {
    // Static allocation
    int a = 0;
    // Dynamic allocation
    int *b = malloc(sizeof(int));
}
```

In the example above, the size and location of `a` is known
when the program is built. The size of `b` is also known, but its location is not.

Sometimes, memory may never be allocated, as in the pseudocode example below:

```C
int main(...) {
    if (/*user has passed some argument*/) {
        int *b = malloc(sizeof(int));
    }
}
```

The arguments passed to the program determine if memory is allocated or not. 

## The C library malloc function

The C standard library provides a special function
[`malloc`](https://en.cppreference.com/w/c/memory/malloc) (`m` for "memory",
`alloc` for "allocate"). This is used to ask for a suitably sized memory
location while a program is running.

```C
void *malloc(size_t size);
```

The C library looks for a chunk of memory with a size of at least X bytes within the memory that it has reserved, where X is the value of the `size`
parameter passed to `malloc`. For instance, on Ubuntu Linux, this is done by GLIBC.

The example at the top of the page is trivial, of course. As it is we could just
initialize both `a` and `b` at compilation time like this:

```C
void fn() {
    int a = 0;
    int *b = NULL;
}
```

This works fine as `a` and `b` are not needed outside of the function or in other
words, if the lifetime of the data is equal to that of the function.

A more complex example (shown below) demonstrates when this is not the case, and the values
live longer than the creating function:

```C
#include <stdlib.h>

typedef struct Entry {
    int data;
    // NULL if end of list, next entry otherwise.
    struct Entry* next;
} Entry;

void add_entry(Entry *entry, int data) {
    // New entry, which becomes the end of the list.
    Entry *new_entry = malloc(sizeof(Entry));
    new_entry->data = data;
    new_entry->next = NULL;

    // Previous tail now points to the newly allocated entry.
    entry->next = new_entry;
}
```

What you see above is a struct `Entry` that defines a singly-linked-list entry.
Singly meaning that you can go forward via `next`, but you cannot go backwards
in the list. There is some `data` and each entry points to the next entry,
`next`, assuming there is one (it will be `NULL` for the end of the list).

`add_entry` makes a new entry and adds it to the end of the list.

Think about how you would use these functions. You could start with some known
sizes of lists, like a global variable for the head (first entry)
of our list.

```C
Entry head = {.data = 123, .next=NULL};
```

Now you want to add another `Entry` to this list at runtime. You do not know
ahead of time what it will contain or if we will add it or not. Where
would you put that entry?

* If it is another global variable, we would have to declare many empty `Entry`
values and hope we never need more than that amount.

{{% notice Other Allocation Techniques%}}
Although in this specific case global variables aren't a good solution, there are
cases where large sets of pre-allocated objects can be beneficial. For example,
it provides a known upper bound of memory usage and makes the timing of each
allocation predictable. These techniques are not covered in this Learning Path. It will, however, be useful to think about them after you have completed this learning
path.
{{% /notice %}}

* If it is in a function's stack frame, that stack frame will be reclaimed and
  modified by future functions, corrupting the new `Entry`.

So you can see, dynamic memory allocation is required, which is why the `add_entry`
shown above calls `malloc`. The resulting pointer points to somewhere not in
the program's global data section or in any function's stack space, but in the
heap memory. It will stay in the heap until a call to `free` is made. 

## The C library free function

You cannot ask malloc for memory forever. Eventually the space will run out. You should give up your dynamic memory once it is not needed,
using [`free`](https://en.cppreference.com/w/c/memory/free).

```C
void free(void *ptr);
```

You call `free` with a pointer previously returned by `malloc`, and this tells
the heap that the memory is no longer needed. 

{{% notice Undefined Behavior%}}
You may wonder what happens if you don't pass the exact same pointer to `free` as
`malloc` returned. The result varies as this is "undefined behavior", which essentially means a large variety of unexpected things can happen.

In practice, many allocators will tolerate this difference or reject it outright
if it's not possible to do something sensible with the pointer.

Remember, just because one allocator handles this a certain way, it does not
mean all allocators will be the same. Indeed, the same allocator may handle it differently for
different allocations within the same program.
{{% /notice %}}

You can use `free` to remove an item from your linked list:

```C
void remove_entry(Entry* previous, Entry* entry) {
    // NULL checks skipped for brevity.
    previous->next = entry->next;
    free(entry);
}
```

`remove_entry` makes the previous entry point to the entry after the one we want
to remove, so that the list skips over it. With `entry` now isolated we call
`free` to give up the memory it occupies:

```text
----- List ------ | - Heap --
[A] -> [B] -> [C] | [A][B][C]
                  |
[A]    [B]    [C] | [A][B][C]
 |-------------^  |
                  |
[A]---------->[C] | [A]   [C]
```

We've now covered the high level how and why for using `malloc` and `free`. Next you will
see a possible implementation of a dynamic memory allocator.
