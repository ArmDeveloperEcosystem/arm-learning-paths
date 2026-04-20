---
title: Adding New Schemes and Implementations to pqm4

weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Adding New Schemes and Implementations

The pqm4 build system facilitates easy addition of new schemes and implementations provided they follow the **NIST/SUPERCOP/PQClean API**. Follow these steps to add an M4-optimized implementation of a scheme like NewHope-512-CPA-KEM:


#### Step 1 : Download the Scheme Implementation

Download the NewHope implementation from GitHub:
```bash
git clone https://github.com/newhopecrypto/newhope.git
```
Navigate to the reference implementation:
```bash
cd newhope/ref
```
This directory contains the implementation files required for integration.

#### Step 2 : Create Scheme Directory
Inside pqm4, create a directory for the scheme:
```bash
mkdir -p crypto_kem/newhope512cpa/m4
```

#### Step 3 : Copy Implementaion Files
Copy required files into pqm4
Include files : 
* Core algorithm files(.c,.h)
* Polynomial and NTT operations
* CPA KEM logic (cpakem.c, cpapke.c)
Do not Include file such as : 
* randombytes.c
* PQCgenKAT_kem.c
* standalone test/benchmark files (speed.c, test.c)
* .o files

#### Step 4 : Create API File

create file name **api.h**  

```bash
crypto_kem/newhope512cpa/m4/api.h
```

Define CRYPTO_SECRETKEYBYTES, CRYPTO_PUBLICKEYBYTES, and CRYPTO_CIPHERTEXTBYTES using the values from the **params.h** file in the NewHope reference implementation, and implement the required functions: **crypto_kem_keypair**, **crypto_kem_enc** , and **crypto_kem_dec**

* Example of api.h file

```python
#ifndef API_H
#define API_H

#define CRYPTO_SECRETKEYBYTES 3680
#define CRYPTO_PUBLICKEYBYTES 1824
#define CRYPTO_CIPHERTEXTBYTES 2208
#define CRYPTO_BYTES 32

#define CRYPTO_ALGNAME "NewHope512-CCA"

int crypto_kem_keypair(unsigned char *pk, unsigned char *sk);
int crypto_kem_enc(unsigned char *ct, unsigned char *ss, const unsigned char *pk);
int crypto_kem_dec(unsigned char *ss, const unsigned char *ct, const unsigned char *sk);

#endif
```
#### Step 5 : Handle Randomness 

* Do not include your own randombytes.c 
* pmq4 provides its own RNG implementation

#### Step 6 : Build the Scheme 

```bash
make clean
make -j4 PLATFORM=<platform
```

check binaries:
```bash
ls bin | grep newhope512cpa
```

#### Step 7 : Test the Implementation

```bash
python3 test.py -p <platform> --uart <serial_port> newhope512cpa
```
Expected output: 
```
SUCCESSFUL
```

### Using Optimized Cryptographic Functions

- **FIPS202 (Keccak, SHA3, SHAKE)**: Use optimized Keccak code available in `mupq/common/fips202.h`.
- **SHA-2**: Use C implementations available in `sha2.h`.
- **AES**: Use assembly-optimized implementations available in `common/aes.h`.

for our NewHope-512-CPA-KEM  Implementation we have used optimized keccak code which is in `mupq/common/fips202.h`

### Contributing Implementations

- For reference implementations, contribute to [PQClean](https://github.com/PQClean/PQClean).
- For optimized C implementations, contribute to [mupq](https://github.com/mupq/mupq).
- For Cortex-M4 optimized implementations, contribute directly to pqm4.
