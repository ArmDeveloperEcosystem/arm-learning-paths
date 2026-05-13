---
title: Add a KEM implementation to pqm4

weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand schemes in pqm4

pqm4 ships with a curated set of NIST-standardized schemes, but you can extend it with additional algorithms. You might want to do this to evaluate an experimental scheme, test a custom Cortex-M4 assembly optimization, or contribute a new implementation to the community.

A scheme in pqm4 is a self-contained cryptographic algorithm implementation. Each scheme lives in its own directory under `crypto_kem/`, and pqm4's build system automatically discovers and compiles it alongside the existing schemes.

## Integrate the NewHope implementation into pqm4

In this section, you'll use NewHope-512-CPA-KEM as a concrete example of a scheme. NewHope is a lattice-based KEM that was a candidate in the NIST PQC standardization process. Although NewHope was not selected for standardization, it remains a useful example because it shares structural similarities with ML-KEM. It also has a clean, well-documented reference implementation. The following steps apply equally to any KEM that follows the NIST/SUPERCOP/PQClean API.

### Download the scheme implementation

Clone the NewHope reference implementation from the pqm4 root directory:

```bash
git clone https://github.com/newhopecrypto/newhope.git
```

The source files you need are in `newhope/ref/`.

### Create the scheme directory

Inside the pqm4 repository, create a directory for the new scheme:

```bash
mkdir -p crypto_kem/newhope512cpa/m4
```

### Copy implementation files

Copy the following files from `newhope/ref/` into `crypto_kem/newhope512cpa/m4/`:

```bash
cp newhope/ref/poly.c    crypto_kem/newhope512cpa/m4/
cp newhope/ref/poly.h    crypto_kem/newhope512cpa/m4/
cp newhope/ref/ntt.c     crypto_kem/newhope512cpa/m4/
cp newhope/ref/ntt.h     crypto_kem/newhope512cpa/m4/
cp newhope/ref/reduce.c  crypto_kem/newhope512cpa/m4/
cp newhope/ref/reduce.h  crypto_kem/newhope512cpa/m4/
cp newhope/ref/cpapke.c  crypto_kem/newhope512cpa/m4/
cp newhope/ref/cpapke.h  crypto_kem/newhope512cpa/m4/
cp newhope/ref/cpakem.c  crypto_kem/newhope512cpa/m4/
cp newhope/ref/cpakem.h  crypto_kem/newhope512cpa/m4/
cp newhope/ref/params.h  crypto_kem/newhope512cpa/m4/
cp newhope/ref/precomp.c crypto_kem/newhope512cpa/m4/
cp newhope/ref/verify.c  crypto_kem/newhope512cpa/m4/
cp newhope/ref/verify.h  crypto_kem/newhope512cpa/m4/
```

Don't copy the following files:

- `randombytes.c` and `randombytes.h`, `rng.c` and `rng.h` — pqm4 provides its own RNG
- `fips202.c` and `fips202.h` — use `mupq/common/fips202.h` instead
- `ccakem.c` and `ccakem.h` — this Learning Path uses the CPA variant only
- `PQCgenKAT_kem.c`
- Standalone test or benchmark files such as `speed.c` and `test_newhope.c`
- Compiled `.o` files

### Create the API header

Create `crypto_kem/newhope512cpa/m4/api.h` and define the required constants and function declarations. Use the values from `params.h` in the NewHope reference implementation for the byte sizes:

```c
#ifndef API_H
#define API_H

#define CRYPTO_SECRETKEYBYTES 3680
#define CRYPTO_PUBLICKEYBYTES 1824
#define CRYPTO_CIPHERTEXTBYTES 2208
#define CRYPTO_BYTES 32

#define CRYPTO_ALGNAME "NewHope512-CPA"

int crypto_kem_keypair(unsigned char *pk, unsigned char *sk);
int crypto_kem_enc(unsigned char *ct, unsigned char *ss, const unsigned char *pk);
int crypto_kem_dec(unsigned char *ss, const unsigned char *ct, const unsigned char *sk);

#endif
```

## Build and verify pqm4

Clean and rebuild pqm4 with your target platform.

#### Physical board

To clean and rebuild pqm4 on a physical board:

```bash
make clean
make -j4 PLATFORM=nucleo-l476rg
```

#### QEMU

To clean and rebuild pqm4 on QEMU:

```bash
make clean
make -j4 PLATFORM=mps2-an386
```

After cleaning and rebuilding, check that the new binaries were generated:

```bash
ls elf/ | grep newhope512cpa | grep '\.elf$'
```

The output is similar to:

```output
crypto_kem_newhope512cpa_m4_hashing.elf
crypto_kem_newhope512cpa_m4_speed.elf
crypto_kem_newhope512cpa_m4_stack.elf
crypto_kem_newhope512cpa_m4_test.elf
crypto_kem_newhope512cpa_m4_testvectors.elf
```

## Test the implementation

Make sure your virtual environment is active, then run the automated test script to verify correctness.

#### Physical board

Run the automated test script on a physical board:

```bash
python3 test.py -p nucleo-l476rg --uart /dev/tty.usbmodemXXXX newhope512cpa
```

#### QEMU

Run the automated test script on QEMU:

```bash
python3 test.py -p mps2-an386 newhope512cpa
```

The output is similar to:

```output
newhope512cpa - m4 SUCCESSFUL
```

## Use optimized cryptographic primitives

pqm4 provides optimized implementations of common primitives that you should use instead of bundling your own:

- Keccak, SHA-3, and SHAKE: use `mupq/common/fips202.h`
- SHA-2: use `sha2.h`
- AES: use the assembly-optimized implementation in `common/aes.h`

The NewHope-512-CPA-KEM example uses the optimized Keccak code from `mupq/common/fips202.h`.

## Contribute your implementation

After your implementation is working and tested, you can contribute it upstream:

- Reference implementations: contribute to [PQClean](https://github.com/PQClean/PQClean)
- Optimized C implementations: contribute to [mupq](https://github.com/mupq/mupq)
- Cortex-M4 optimized implementations: contribute directly to [pqm4](https://github.com/mupq/pqm4)

## What you've accomplished

You've now set up the pqm4 environment, run tests and benchmarks for a NIST-standardized post-quantum KEM on Arm Cortex-M4, and integrated a new scheme into the framework.

You can now create your own post-quantum cryptography algorithm implementations for pqm4 and contribute them upstream.