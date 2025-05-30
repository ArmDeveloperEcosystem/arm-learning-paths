---
title: False sharing example
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Example code

{{% notice Learning Goal%}}
The example code in this section demonstrates how false sharing affects performance by comparing two multithreaded programs; one with cache-aligned data structures, and one without. You’ll compile and run both versions, observe the runtime difference, and learn how memory layout affects cache behavior. This sets the stage for analyzing performance with `perf c2c` in the next section.
{{% /notice %}}

Use a text editor to copy and paste the C example code below into a file named `false_sharing_example.c`

The code is adapted from [Joe Mario](https://github.com/joemario/perf-c2c-usage-files) and is discussed thoroughly in the Arm Statistical Profiling Extension Whitepaper.

```cpp
/*
 * This is an example program to show false sharing between
 * numa nodes.  
 *
 * It can be compiled two ways:
 *    gcc -g false_sharing_example.c -pthread -lnuma -o false_sharing.exe
 *    gcc -g false_sharing_example.c -pthread -lnuma -DNO_FALSE_SHARING -o no_false_sharing.exe
 *
 * The -DNO_FALSE_SHARING macro reduces the false sharing by expanding the shared data
 * structure into two different cachelines, (and it runs faster).
 *
 * The usage is: 
 *     ./false_sharing.exe <number of threads per node>
 *     ./no_false_sharing.exe <number of threads per node>
 *
 * The program will make half the threads writer threads and half reader
 * threads.  It will pin those threads in round-robin format to the 
 * different numa nodes in the system.
 *
 * For example, on a system with 4 numa nodes:
 * ./false_sharing.exe 2
 * 12165 mticks, reader_thd (thread 6), on node 2 (cpu 144).
 * 12403 mticks, reader_thd (thread 5), on node 1 (cpu 31).
 * 12514 mticks, reader_thd (thread 4), on node 0 (cpu 96).
 * 12703 mticks, reader_thd (thread 7), on node 3 (cpu 170).
 * 12982 mticks, lock_th (thread 0), on node 0 (cpu 1).
 * 13018 mticks, lock_th (thread 1), on node 1 (cpu 24).
 * 13049 mticks, lock_th (thread 3), on node 3 (cpu 169).
 * 13050 mticks, lock_th (thread 2), on node 2 (cpu 49).
 * 
 * # ./no_false_sharing.exe 2
 * 1918 mticks, reader_thd (thread 4), on node 0 (cpu 96).
 * 2432 mticks, reader_thd (thread 7), on node 3 (cpu 170).
 * 2468 mticks, reader_thd (thread 6), on node 2 (cpu 146).
 * 3903 mticks, reader_thd (thread 5), on node 1 (cpu 40).
 * 7560 mticks, lock_th (thread 0), on node 0 (cpu 1).
 * 7574 mticks, lock_th (thread 2), on node 2 (cpu 145).
 * 7602 mticks, lock_th (thread 3), on node 3 (cpu 169).
 * 7625 mticks, lock_th (thread 1), on node 1 (cpu 24).
 *
 */

#define _MULTI_THREADED
#define _GNU_SOURCE
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>
#include <sched.h>
#include <pthread.h>
#include <numa.h>
#include <sys/types.h>

/*
 * A thread on each numa node seems to provoke cache misses
 */
#define 	LOOP_CNT     	(5 * 1024 * 1024 * 100) 

#if defined(__x86_64__) || defined(__i386__) 
static __inline__ uint64_t rdtsc() {
    unsigned hi, lo;
    __asm__ __volatile__ ( "rdtsc" : "=a"(lo), "=d"(hi));
    return ( (uint64_t)lo) | ( ((uint64_t)hi) << 32);
}

#elif defined(__aarch64__)
static __inline__ uint64_t rdtsc(void)
{
    uint64_t val;

    /*
     * According to ARM DDI 0487F.c, from Armv8.0 to Armv8.5 inclusive, the
     * system counter is at least 56 bits wide; from Armv8.6, the counter
     * must be 64 bits wide.  So the system counter could be less than 64
     * bits wide and it is attributed with the flag 'cap_user_time_short'
     * is true.
     */
    asm volatile("mrs %0, cntvct_el0" : "=r" (val));

    return val;
}
#endif


/* 
 * Create a struct where reader fields share a cacheline with the hot lock field.
 * Compiling with -DNO_FALSE_SHARING inserts padding to avoid that sharing.
 */
typedef struct _buf {
  long lock0; 
  long lock1;
  long reserved1;
#if defined(NO_FALSE_SHARING)
  long pad[5];   // to keep the 'lock*' fields on their own cacheline.
#else
  long pad[1];  // to provoke false sharing.
#endif
  long reader1; 
  long reader2; 
  long reader3; 
  long reader4; 
} buf __attribute__((aligned (64)));

buf buf1;
buf buf2;

volatile int wait_to_begin = 1;
struct thread_data *thread;
int max_node_num;
int num_threads; 
char * lock_thd_name = "lock_th";
char * reader_thd_name = "reader_thd";

#define checkResults(string, val) {             \
 if (val) {                                     \
   printf("Failed with %d at %s", val, string); \
   exit(1);                                     \
 }                                              \
}
 
struct thread_data {
    pthread_t tid;
    long tix;
    long node;
    char *name;
};

/*
 * Bind a thread to the specified numa node.
*/
void setAffinity(void *parm) {
   volatile uint64_t rc, j;
   int node        = ((struct thread_data *)parm)->node;
   char *func_name = ((struct thread_data *)parm)->name;

   numa_run_on_node(node);
   pthread_setname_np(pthread_self(),func_name);
}

/*
 * Thread function to simulate the false sharing.
 * The "lock" threads will test-n-set the lock field,
 * while the reader threads will just read the other fields
 * in the struct.
 */
extern void *read_write_func(void *parm) {

   int tix = ((struct thread_data *)parm)->tix;
   uint64_t start, stop, j;    
   char *thd_name = ((struct thread_data *)parm)->name;

   // Pin each thread to a numa node.
   setAffinity(parm);

   // Wait for all threads to get created before starting.
   while(wait_to_begin) ;

   start = rdtsc();
   for(j=0; j<LOOP_CNT; j++) {

      // Check for lock thread.
      if (*thd_name == *lock_thd_name) {
          __sync_lock_test_and_set(&buf1.lock0, 1 );
          buf1.lock0 += 1;   
          buf2.lock1 = 1;   
 
      } else {
         // Reader threads.
   
         switch(tix % max_node_num) {
            volatile long var;
            case 0:
              var = *(volatile uint64_t *)&buf1.reader1;
              var = *(volatile uint64_t *)&buf2.reader1;
              break;
            case 1:
              var = *(volatile uint64_t *)&buf1.reader2;
              var = *(volatile uint64_t *)&buf2.reader2;
              break;
            case 2:
              var = *(volatile uint64_t *)&buf1.reader3;
              var = *(volatile uint64_t *)&buf2.reader3;
              break;
            case 3:
              var = *(volatile uint64_t *)&buf1.reader4;
              var = *(volatile uint64_t *)&buf2.reader4;
              break;
         }; 
     }; 
  }  // End of for LOOP_CNT loop

  // Print out stats
  //
  stop = rdtsc();
  int cpu = sched_getcpu();
  int node = numa_node_of_cpu(cpu);
  printf("%ld mticks, %s (thread %d), on node %d (cpu %d).\n", (stop-start)/1000000, thd_name, tix, node, cpu);  

  return NULL;
}
 
int main ( int argc, char *argv[] )
{
  int     i, n, rc=0;

  if ( argc != 2 ) /* argc should be 2 for correct execution */
  {
   printf( "usage: %s <n>\n", argv[0] );
   printf( "where \"n\" is the number of threads per node\n");
   exit(1);
  }

  if ( numa_available() < 0 )
  {
   printf( "NUMA not available\n" );
   exit(1);
  }

  int thread_cnt = atoi(argv[1]);

  max_node_num = numa_max_node();
  if ( max_node_num == 0 )
    max_node_num = 1;
  int node_cnt = max_node_num + 1;

  // Use "thread_cnt" threads per node.
  num_threads = (max_node_num +1) * thread_cnt;

  thread = malloc( sizeof(struct thread_data) * num_threads);
 
  // Create the first half of threads as lock threads.
  // Assign each thread a successive round robin node to 
  // be pinned to (later after it gets created.)
  //
  for (i=0; i<=(num_threads/2 - 1); i++) {
     thread[i].tix = i;
     thread[i].node = i%node_cnt;
     thread[i].name = lock_thd_name;
     rc = pthread_create(&thread[i].tid, NULL, read_write_func, &thread[i]);
     checkResults("pthread_create()\n", rc);
     usleep(500);
  }

  // Create the second half of threads as reader threads.
  // Assign each thread a successive round robin node to 
  // be pinned to (later after it gets created.)
  //
  for (i=((num_threads/2)); i<(num_threads); i++) {
     thread[i].tix = i;
     thread[i].node = i%node_cnt;
     thread[i].name = reader_thd_name;
     rc = pthread_create(&thread[i].tid, NULL, read_write_func, &thread[i]);
     checkResults("pthread_create()\n", rc);
     usleep(500);
  }

  // Sync to let threads start together
  usleep(500);
  wait_to_begin = 0;
 
  for (i=0; i <num_threads; i++) {
     rc = pthread_join(thread[i].tid, NULL);
     checkResults("pthread_join()\n", rc);
  }

  return 0;
}
```

### Code explanation

The key data structure that occupies the cache is `struct _buf`. With a 64-byte cache line size, each line can hold 8, 8-byte `long` integers. 

If you do not pass in the `NO_FALSE_SHARING` macro during compilation the `Buf` data structure will contain the elements below. Each structure neatly occupies the entire 64-byte cache line. 

However, the 4 readers and 2 locks are now accessing the same cache line. 

```output
typedef struct _buf {
  long lock0; 
  long lock1;
  long reserved1;
  long pad[1]; 
  long reader1; 
  long reader2; 
  long reader3; 
  long reader4; 
} buf __attribute__((aligned (64)));
```

Alternatively if you pass in the `NO_FALSE_SHARING` macro during compilation, the `Buf` structure has a different shape. 

The 40 bytes of padding pushes the reader variables onto a different cache line. However, notice that this is with the tradeoff the new `Buf` structures occupies multiple cache lines (12 long integers). Therefore it leaves unused cache space of 25% per `Buf` structure. This trade-off uses more memory but eliminates false sharing, improving performance by reducing cache line contention.

```output
typedef struct _buf {
  long lock0; 
  long lock1;
  long reserved1;
  long pad[5]; 
  long reader1; 
  long reader2; 
  long reader3; 
  long reader4; 
} buf __attribute__((aligned (64)));
```

Compile the example with the commands: 

```bash
gcc -lnuma -pthread false_sharing_example.c -o false_sharing
gcc -lnuma -pthread false_sharing_example.c -DNO_FALSE_SHARING -o no_false_sharing
```

Run both binaries with the command line argument of 1. Both binaries successfully return a 0 exit status but the binary with the false sharing runs almost 2x slower!

```bash
time ./false_sharing 1
time ./no_false_sharing 1
```

```output
real    0m12.101s
user    0m18.520s
sys     0m0.000s
...
real    0m6.496s
user    0m8.869s
sys     0m0.000s
```

## Summary
In this section, you ran a hands-on C example to see how false sharing can significantly degrade performance in multithreaded applications. By comparing two versions of the same program, one with aligned memory access and one without, you saw how something as subtle as cache line layout can result in a 2x difference in runtime. This practical example sets the foundation for using Perf C2C to capture and analyze real cache line sharing behavior in the next section.

