---
title: Understand core SVE concepts for vectorization
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## SVE concepts you need before writing code

SVE is different from fixed width SIMD like Neon. The vector length is not fixed at compile time. It is determined at runtime by the hardware. This means you can't write `for (i = 0; i < n; i += 16)` and assume you're processing 16 bytes per iteration. SVE code must be vector length agnostic (VLA) to work correctly on any processor with SVE support.

Before writing SVE intrinsics, it's helpful to understand three things:

1. How SVE predicates control which elements are active
2. How to handle loop tails when data length isn't a multiple of the vector length
3. How to widen narrow data types for accumulation

The Arm MCP server is the right tool for this. Ask your AI assistant the questions below and read the responses. The goal isn't to memorize intrinsic names, but to understand the concepts well enough to recognize when you need each one.

## Comparing SVE and Neon

Start with understanding the big picture about SVE.

### ASK AI: about SVE versus Neon

Ask your assistant:

```text
Ask the Arm MCP server what is SVE and how does it differ from Neon? My Makefile targets the native CPU on a Neoverse processor. 
```

A sample response is:

```output
Here's what the Arm knowledge base says:                                                                                          
                                                                                                                                    
  SVE vs Neon                                                                                                                       
                                                                                                                                    
  Neon (also called ASIMD/Advanced SIMD) is Arm's original SIMD extension. It uses fixed 128-bit vector registers (Q0–Q31). Every   
  Neon instruction operates on exactly 128 bits — if your data doesn't fit neatly into 128-bit chunks, you write explicit scalar    
  cleanup code for the remainder.                                                                                                   
                                                                                                                                    
  SVE (Scalable Vector Extension) is fundamentally different in that it uses a Vector Length Agnostic (VLA) programming model. Key  
  differences:                                                                                                                      
                                                                                                                                    
  ┌────────────────┬────────────────────────┬──────────────────────────────────────────────────────────────────┐                    
  │                │ Neon                   │ SVE / SVE2                                                       │                    
  ├────────────────┼────────────────────────┼──────────────────────────────────────────────────────────────────┤                    
  │ Vector width   │ Fixed 128-bit          │ Scalable: 128 to 2048 bits (in 128-bit increments)               │                    
  │ Registers      │ 32 × 128-bit V regs    │ 32 × scalable Z regs + 16 predicate regs                         │                    
  │ Tail handling  │ Manual scalar cleanup  │ Built-in **per-lane predication** (`svwhilelt`, predicate masks) │                    
  │ Loop model     │ Fixed iteration count  │ VLA: `svcntb()` at runtime, one binary works on any SVE width    │                    
  │ Gather/scatter │ No                     │ Yes — `svld1_gather`, `svst1_scatter`                            │                    
  │ Dot product    │ Limited (Armv8.2 UDOT) │ Full `svdot` family with widening accumulate                     │                    
  └────────────────┴────────────────────────┴──────────────────────────────────────────────────────────────────┘                    
                                                                                                                                    
  The key innovation is predication: every SVE instruction can be masked by a predicate register, so the last iteration of a loop   
  naturally handles any remainder without scalar cleanup. Your adler32-sve.c uses this pattern directly — svwhilelt_b8 generates the
  predicate, and all the svdot/svld1 calls respect it.                                                                              
                                                                                                                                    
  What this means for your Neoverse-V2                                                                                              
                                                                                                                                    
  Your system has SVE2 with 128-bit vectors (Neoverse-V2 implements 128-bit SVE). That's the same width as Neon, but you still      
  benefit from:                                                                                                                     
                                                                                                                                    
  - Predicated loads/stores — no cleanup loops needed                                                                               
  - Richer instruction set — svdot, svindex, gather/scatter, bitperm, crypto extensions                                             
  - SVE2 extras — sve2-aes, sve2-bitperm, sve2-sha3 (all present on your CPU)                                                       
  - Portability — the same SVE binary runs unmodified on Graviton4 (Neoverse-V2, 128-bit) or future chips with wider vectors        
                                                                                                                                    
  Since -mcpu=native on your system resolves to armv9-a+sve2-*, your Makefile is already generating SVE2 code. Your adler32-sve.c   
   uses svdot_u32 and svdot_n_u32 which are SVE dot-product intrinsics — these are well-suited to the Neoverse-V2.                  
                                                                                                                                    
  For deeper dives, Arm has several relevant learning paths:                                                                        
                                                                                                                                    
  - Port Code to Arm SVE (https://learn.arm.com/learning-paths/servers-and-cloud-computing/sve/)                                    
  - Learn SVE and SME programming with SIMD Loops (https://learn.arm.com/learning-paths/cross-platform/simd-loops/)                 
  - Accelerate Bitmap Scanning with Neon and SVE                                                                                    
  (https://learn.arm.com/learning-paths/servers-and-cloud-computing/bitmap_scan_sve2/)      
```

The response explains that Neon uses fixed 128 bit vectors, while SVE uses vectors of variable length (a multiple of 128 bits, from 128 to 2048 bits). Neoverse N2 and Neoverse V2 support SVE with 128 bit vectors. Neoverse V1 supports SVE with 256 bit vectors. The key point is that your code doesn't need to know the vector length at compile time. SVE intrinsics handle it at runtime.

## Predicates and loop tails

Predicates and loop tails may be new to software developers.

In fixed-width SIMD like Neon, every lane in a vector always participates in every operation. That works fine when your data length is a multiple of the vector width, but it forces you to write special-case scalar code to handle the leftover elements at the end of a loop. With SVE's variable vector length, you don't even know the vector width at compile time, so that approach breaks down entirely.

SVE solves this with predicate registers. A predicate is a bitmask with one bit per vector element. Each bit controls whether the corresponding lane is active or inactive for a given operation. Inactive lanes are ignored: they don't load memory, don't compute, and don't write results. This lets you run the same vector code on the final partial chunk of data as on every full chunk before it, there is no special-case tail loop needed.

### ASK AI: about how predicate registers work

Ask your assistant:

```text
Masking with predicate registers seems like a key concept in SVE. How does it work to handle loops when my data length isn't a multiple of the vector length? 
```

A sample response is:

```output
 SVE predication for loop tails                                                                                                    
                                                                                                                                    
  SVE has 16 predicate registers (P0–P15) with one bit per byte lane. Each bit says "active" or "inactive." Nearly every SVE        
  instruction takes a predicate, so inactive lanes are simply skipped — loads don't fault, stores don't write, arithmetic ignores   
  them.                                                                                                                             
                                                                                                                                    
  The canonical SVE loop                                                                                                            
                                                                                                                                    
  uint64_t vl = svcntb();                          // vector length in bytes (runtime)                                              
  for (uint64_t i = 0; i < n; i += vl) {                                                                                            
      svbool_t pg = svwhilelt_b8(i, n);            // ① generate mask                                                               
      svuint8_t v = svld1_u8(pg, &data[i]);        // ② predicated load                                                             
      // ... compute with v ...                     // ③ all ops respect pg                                                         
  }                                                                                                                                 
                                                                                                                                    
  ① `svwhilelt_b8(i, n)` — compares each lane index i, i+1, i+2, ... against n. Returns a predicate with true for every index < n,  
  false otherwise.                                                                                                                  
                                                                                                                                    
  With vl=16 and n=50:                                                                                                              
                                                                                                                                    
  i= 0: pg = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]   ← full vector                                                                      
  i=16: pg = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]   ← full vector                                                                      
  i=32: pg = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]   ← full vector                                                                      
  i=48: pg = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]   ← only 2 remaining                                                                 
                                                                                                                                    
  ② Predicated load — svld1_u8(pg, ptr) loads only active lanes. Inactive lanes become zero. It won't fault even if the inactive    
  addresses are unmapped — this is a hardware guarantee.                                                                            
                                                                                                                                    
  ③ Downstream arithmetic — operations like svdot, svadd, etc. either take the predicate directly or naturally get zeros from the   
  inactive lanes of the load. No contribution from out-of-bounds data.                                                              
                                                                                                                                    
  Compare with Neon (fixed 128-bit)                                                                                                 
                                                                                                                                    
  // Neon: need two separate loops                                                                                                  
  for (i = 0; i + 16 <= n; i += 16) {                                                                                               
      uint8x16_t v = vld1q_u8(&data[i]);   // must have 16 valid bytes                                                              
      // ... compute ...                                                                                                            
  }                                                                                                                                 
  for (; i < n; i++) {                      // scalar cleanup for remainder                                                         
      // ... handle tail byte-by-byte ...                                                                                           
  }                                                                                                                                 
                                                                                                                                    
  With SVE, the same loop body handles both full and partial iterations. No cleanup loop.                                           
                                                                                                                                    
  The three predication modes                                                                                                       
                                                                                                                                    
  SVE intrinsics use a suffix to control what happens to inactive lanes:                                                            
                                                                                                                                    
  ┌────────┬─────────────────────────┬──────────────────────────────────────────────┐                                               
  │ Suffix │ Inactive lanes          │ When to use                                  │                                               
  ├────────┼─────────────────────────┼──────────────────────────────────────────────┤                                               
  │ `_z`   │ Zeroed                  │ Need a clean zero for inactive elements      │                                               
  │ `_m`   │ Merged (keep old value) │ Conditional updates within a vector          │                                               
  │ `_x`   │ Don't care (undefined)  │ Fastest — when inactive lanes are never read │                                               
  └────────┴─────────────────────────┴──────────────────────────────────────────────┘                                               
                                                                                                                                    
  Key takeaway                                                                                                                      
                                                                                                                                    
  The predicate register turns the loop tail from a code structure problem (separate cleanup path) into a data problem (a mask). One
  loop, one code path, any data length, any vector width.   
```

The response explains that the `svwhilelt_b8(i, n)` intrinsic creates a predicate where element `k` is active if `i + k < n`. This handles the loop tail automatically. When you're near the end of the data, the predicate deactivates the elements that would go out of bounds.

A typical SVE loop looks like this:

```c
uint64_t vl = svcntb();          // vector length in bytes, determined at runtime
for (size_t i = 0; i < n; i += vl) {
    svbool_t pg = svwhilelt_b8(i, n);   // predicate: active lanes where i+k < n
    svuint8_t data = svld1_u8(pg, &buf[i]);
    // ... process data ...
}
```

The loop body runs even for the final partial vector. The predicate ensures only valid bytes are processed.

## Loading bytes and widening to 32 bit

For Adler-32, you're loading `uint8_t` bytes but accumulating into `uint32_t` sums.

### ASK AI: about widening

Ask your assistant:

```text
The adler32 loop accumulates uint8_t values into a uint32_t sum. How does SVE handle widening from 8 bit to 32 bit elements?
```

A sample output is:

```output
Loading uint8_t values                                                                                                            
                                                                                                                                    
  svbool_t pg = svwhilelt_b8(i, len);                                                                                               
  svuint8_t bytes = svld1_u8(pg, &data[i]);  // predicated load of uint8_t elements                                                 
                                                                                                                                    
  Widening from 8-bit to 32-bit                                                                                                     
                                                                                                                                    
  SVE widens one step at a time (8→16→32), and you select the bottom or top half of the source vector at each step:                 
                                                                                                                                    
  // Step 1: 8-bit → 16-bit (unpack lower and upper halves)                                                                         
  svuint16_t lo16 = svunpklo_u16(bytes);   // lower half of bytes, zero-extended to u16                                             
  svuint16_t hi16 = svunpkhi_u16(bytes);   // upper half of bytes, zero-extended to u16                                             
                                                                                                                                    
  // Step 2: 16-bit → 32-bit (unpack again)                                                                                         
  svuint32_t ll32 = svunpklo_u32(lo16);    // lower quarter → u32                                                                   
  svuint32_t lh32 = svunpkhi_u32(lo16);    // second quarter → u32                                                                  
  svuint32_t hl32 = svunpklo_u32(hi16);    // third quarter → u32                                                                   
  svuint32_t hh32 = svunpkhi_u32(hi16);    // upper quarter → u32                                                                   
                                                                                                                                    
  Visually, for a 128-bit vector (16 bytes):                                                                                        
                                                                                                                                    
  bytes (16 x u8):  [b0 b1 b2 b3 | b4 b5 b6 b7 | b8 b9 b10 b11 | b12 b13 b14 b15]                                                   
                         ↓              ↓               ↓                ↓                                                          
                     svunpklo_u16    svunpkhi_u16                                                                                   
                         ↓    ↓         ↓    ↓                                                                                      
  lo16 (8 x u16):  [b0  b1  b2  b3 | b4  b5  b6  b7 ]                                                                               
  hi16 (8 x u16):  [b8  b9  b10 b11| b12 b13 b14 b15]                                                                               
                      ↓       ↓        ↓       ↓                                                                                    
  ll32 (4 x u32):  [b0  b1  b2  b3 ]                                                                                                
  lh32 (4 x u32):  [b4  b5  b6  b7 ]                                                                                                
  hl32 (4 x u32):  [b8  b9  b10 b11]                                                                                                
  hh32 (4 x u32):  [b12 b13 b14 b15]                                                                                                
                                                                                                                                    
  Accumulating into a uint32_t sum vector                                                                                           
                                                                                                                                    
  Once widened, you add each quarter into your running svuint32_t accumulator:                                                      
                                                                                                                                    
  svbool_t pg32 = svptrue_b32();                                                                                                    
  sum_a = svadd_u32_x(pg32, sum_a, ll32);                                                                                           
  sum_a = svadd_u32_x(pg32, sum_a, lh32);                                                                                           
  sum_a = svadd_u32_x(pg32, sum_a, hl32);                                                                                           
  sum_a = svadd_u32_x(pg32, sum_a, hh32);                                                                                           
                                                                                                                                    
  Alternative: `svld1ub_u32` — direct widening load                                                                                 
                                                                                                                                    
  If you'd rather avoid the unpack chain, SVE can load bytes directly into 32-bit lanes:                                            
                                                                                                                                    
  svbool_t pg32 = svwhilelt_b32(i, len);                                                                                            
  svuint32_t vals = svld1ub_u32(pg32, &data[i]);  // loads u8, zero-extends to u32                                                  
  sum_a = svadd_u32_x(pg32, sum_a, vals);                                                                                           
                                                                                                                                    
  The tradeoff: this processes only VL/4 bytes per iteration (4 bytes on your 128-bit Neoverse-V2) instead of VL bytes (16). Simpler
  code, but fewer elements per loop iteration.                                                                                      
                                                                                                                                    
  Which approach for Adler-32?                                                                                                       
                                                                                                                                    
  The unpack chain is better for performance — you process a full vector of bytes each iteration. The svld1ub_u32 approach is       
  simpler but does 4x more loop iterations on your hardware.                                                                        
                                                                                                                                    
  For the b accumulator in Adler-32, you'll also need a prefix sum pattern since b += a after each byte addition — that's the        
  trickiest part.
```

The response introduces `svld1_u8` for loading bytes, and explains that SVE doesn't have a single "load and widen" intrinsic. Instead, you use `svld1ub_u32` to load bytes and extend them with zeroes directly into a 32 bit vector. This is the right approach for Adler-32 because your accumulators are 32 bit.

The Arm MCP server will return the exact signature:

```c
svuint32_t svld1ub_u32(svbool_t pg, const uint8_t *base);
```

This loads one byte per active 32 bit lane and extends each byte with zeroes to 32 bits. On a processor with 256 bit SVE vectors, this loads 8 bytes per iteration (8 lanes × 32 bits = 256 bits).

## The dot product intrinsic

You may see things in the AI assistant responses you don't understand. You can continue to ask for more explanation until you are totally comfortable. One of the responses above implies svdot is commonly used for arithmetic. You can ask more for information about what it does.

### ASK AI: about the svdot instruction

Ask your assistant:

```text
What is the svdot intrinsic? How does it differ from a simple multiply and accumulate operation?
```

A sample output is:

```output
`svdot` — Dot Product Intrinsic                                                                                                   
                                                                                                                                    
  From the Arm intrinsics reference (https://developer.arm.com/architectures/instruction-sets/intrinsics/#q=svdot[_u32]):           
                                                                                                                                    
  svuint32_t svdot_u32(svuint32_t acc, svuint8_t op1, svuint8_t op2);                                                               
                                                                                                                                    
  For each u32 element i in the result:                                                                                             
                                                                                                                                    
  acc[i] += (u32)op1[4i+0] * (u32)op2[4i+0]                                                                                         
          + (u32)op1[4i+1] * (u32)op2[4i+1]                                                                                         
          + (u32)op1[4i+2] * (u32)op2[4i+2]                                                                                         
          + (u32)op1[4i+3] * (u32)op2[4i+3]                                                                                         
                                                                                                                                    
  It does three things in one instruction: widens u8→u32, multiplies, and accumulates groups of 4.                                  
                                                                                                                                    
  How it differs from a simple multiply-accumulate                                                                                  
                                                                                                                                    
  A naive approach would be:                                                                                                        
                                                                                                                                    
  Step 1: widen 16 × u8  →  16 × u32          (svunpklo/hi, twice)                                                                  
  Step 2: multiply 16 × u32 * 16 × u32        (svmul)                                                                               
  Step 3: accumulate into u32 vector           (svadd)                                                                              
                                                                                                                                    
  That's 5+ instructions and needs 4× the register space (16 u8 elements expand to 16 u32 elements across multiple vectors).        
                                                                                                                                    
  svdot instead:                                                                                                                    
                                                                                                                                    
  One instruction: 16 × u8 → 4 × u32 (widened, multiplied, summed, accumulated)                                                     
                                                                                                                                    
  The key differences:                                                                                                              
                                                                                                                                    
  ┌───────────────────┬───────────────────────────────┬────────────────────────────────────┐                                        
  │                   │ Multiply-accumulate           │ svdot                              │                                        
  ├───────────────────┼───────────────────────────────┼────────────────────────────────────┤                                        
  │ Instructions      │ 5+ (unpack, mul, add)         │ 1                                  │                                        
  │ Output elements   │ Same count as input           │ **4× fewer** (groups of 4 reduced) │                                        
  │ Register pressure │ 4× wider intermediate vectors │ Stays in u32 width                 │                                        
  │ Widening          │ Explicit, multi-step          │ Implicit, fused                    │                                        
  └───────────────────┴───────────────────────────────┴────────────────────────────────────┘                                        
                                                                                                                                    
  The 4:1 reduction is the critical property. On your 128-bit Neoverse-V2, a vector holds 16 u8 bytes. After svdot, you have 4 u32  
  lanes — each holding the accumulated sum of 4 bytes. This compression means you process 4× more input data per u32 accumulator    
  lane than you could with element-wise operations.                                                                                 
                                                                                                                                    
  There's also a scalar-broadcast variant:                                                                                          
                                                                                                                                    
  svuint32_t svdot_n_u32(svuint32_t acc, svuint8_t op1, uint8_t op2);                                                               
                                                                                                                                    
  This multiplies every byte by the same scalar value op2. With op2 = 1, it becomes a pure widening sum — no multiplication cost,   
  just acc[i] += bytes[4i+0] + bytes[4i+1] + bytes[4i+2] + bytes[4i+3].        
```

The response explains that `svdot` computes a dot product between two vectors of narrow elements and accumulates the result into a vector of wider elements. For example, `svdot_u32` takes two `svuint8_t` vectors and a `svuint32_t` accumulator, multiplying corresponding 8 bit elements and adding the products into 32 bit lanes.

The signature is:

```c
svuint32_t svdot_u32(svuint32_t op1, svuint8_t op2, svuint8_t op3);
```

You'll use this to compute the weighted sum for the `B` accumulator. The reason will become clear in the SVE implementation section.

{{< notice Note >}}
You may notice your AI assistant asking to just create the code for you. Resist the urge to say yes and continue to ask questions and understand the theory of operation. You need to do this to get a functional result with the best performance. You also need to be able to explain and maintain the code so it's worth the extra time to learn how SVE works.
{{< /notice >}}

## What you've learned and what's next

In this section:

1. You learned how SVE predicates handle loop tails without special case code
2. You investigated intrinsics for loading bytes and dot product and learned how to ask for more details
3. You understand that SVE code must be vector length agnostic

Before you can use these intrinsics effectively, you need to restructure the Adler-32 algorithm to remove the modulo operation on each byte. That's the subject of the next section.
