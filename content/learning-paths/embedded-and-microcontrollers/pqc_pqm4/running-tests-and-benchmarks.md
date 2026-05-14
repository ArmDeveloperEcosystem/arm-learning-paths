---
title: Run pqm4 tests and benchmarks

weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Understand generated pqm4 binaries

After building pqm4, a set of binaries is generated for each scheme and implementation. You can use these binaries to verify correctness, measure performance, and analyze resource usage on your Cortex-M4 board or in QEMU.

For example, building ML-KEM-768 produces binaries with names in this pattern:

```output
bin/crypto_kem_ml-kem-768_<impl>_<type>.bin
```

The `<impl>` field identifies the implementation variant. The exact suffix depends on the scheme:

- `m4fspeed`: Cortex-M4F implementation optimized for speed (used by ML-KEM)
- `m4fstack`: Cortex-M4F implementation optimized for stack size (used by ML-KEM)
- `m4f`: Cortex-M4F implementation used by some schemes such as BIKE
- `clean`: clean reference implementation from PQClean

The `clean` variant uses a different file prefix: `mupq_pqclean_crypto_kem_<scheme>_clean_<type>.elf`

The `<type>` field identifies what the binary measures. The following section explains each type and how you can run them.

## Flash and run a generated binary

How you run a binary depends on whether you are using a physical board or QEMU.

#### Physical board

Flash the binary and read the serial output.

Flash the binary:

```bash
st-flash write bin/<binary_name>.bin 0x8000000
```

Read the output from the board:

```bash
python3 hostside/host_unidirectional.py
```

Press the RESET button on the board to trigger execution and see the output.

#### QEMU

Run the corresponding ELF file directly.

```bash
qemu-system-arm -M mps2-an386 -nographic -semihosting -kernel elf/<binary_name>.elf
```

To exit QEMU, press `Ctrl+A` then `X`.

### Run a test binary

The test binary verifies that a scheme works correctly end to end.

#### Physical board

Flash the ML-KEM-768 test binary on a physical board:

```bash
st-flash write bin/crypto_kem_ml-kem-768_m4fspeed_test.bin 0x8000000
```

#### QEMU

Run the ML-KEM-768 test binary on QEMU:

```bash
qemu-system-arm -M mps2-an386 -nographic -semihosting -kernel elf/crypto_kem_ml-kem-768_m4fspeed_test.elf
```

It generates a keypair, performs encapsulation and decapsulation, and checks that both sides derive the same shared secret. It also tests failure cases such as an invalid secret key or invalid ciphertext.

The output after running the binary is similar to:

```output
==========================
DONE key pair generation!
DONE encapsulation!
DONE decapsulation!
OK KEYS

+
...
OK invalid sk_a

+
OK invalid ciphertext

+
#
```

### Run a speed binary

The speed binary measures execution time in CPU cycles for each operation.

#### Physical board

Flash the ML-KEM-768 speed binary on a physical board:

```bash
st-flash write bin/crypto_kem_ml-kem-768_m4fspeed_speed.bin 0x8000000
```

#### QEMU

Run the ML-KEM-768 speed binary on QEMU:

```bash
qemu-system-arm -M mps2-an386 -nographic -semihosting -kernel elf/crypto_kem_ml-kem-768_m4fspeed_speed.elf
```

The output after running the binary is similar to:

```output
==========================
keypair cycles:
123456

encaps cycles:
234567

decaps cycles:
210000
=
```

### Run a hashing binary

The hashing binary measures how many cycles are spent in symmetric primitives such as SHA-2, SHA-3, and AES. The number of cycles shows how much of the overall algorithm cost comes from hashing.

#### Physical board

Flash the ML-KEM-768 hashing binary on a physical board:

```bash
st-flash write bin/crypto_kem_ml-kem-768_m4fspeed_hashing.bin 0x8000000
```

#### QEMU

Run the ML-KEM-768 hashing binary on QEMU:

```bash
qemu-system-arm -M mps2-an386 -nographic -semihosting -kernel elf/crypto_kem_ml-kem-768_m4fspeed_hashing.elf
```

The output after running the binary is similar to:

```output
==========================
keypair hash cycles:
50000

encaps hash cycles:
80000

decaps hash cycles:
75000
=
```

### Run a stack binary

The stack binary measures peak stack memory usage for each operation.

#### Physical board

Flash the ML-KEM-768 stack binary on a physical board:

```bash
st-flash write bin/crypto_kem_ml-kem-768_m4fspeed_stack.bin 0x8000000
```

#### QEMU

Run the ML-KEM-768 stack binary on QEMU:

```bash
qemu-system-arm -M mps2-an386 -nographic -semihosting -kernel elf/crypto_kem_ml-kem-768_m4fspeed_stack.elf
```

The output after running the binary is similar to:

```output
==========================
keypair stack usage:
2048

encaps stack usage:
3072

decaps stack usage:
2800
#
```

{{% notice Note %}}
Stack measurement might not work correctly on some boards due to platform-specific memory layout. Memory allocated outside functions, such as public keys and ciphertexts, is not included in these measurements.
{{% /notice %}}

### Run a test vectors binary

The test vectors binary generates deterministic test vectors using a fixed random seed. These are used to validate correctness and compare different implementations against each other.

#### Physical board

Flash the ML-KEM-768 test vectors binary on a physical board:

```bash
st-flash write bin/crypto_kem_ml-kem-768_m4fspeed_testvectors.bin 0x8000000
```

#### QEMU

Run the ML-KEM-768 test vectors binary on QEMU:

```bash
qemu-system-arm -M mps2-an386 -nographic -semihosting -kernel elf/crypto_kem_ml-kem-768_m4fspeed_testvectors.elf
```

To compare the on-device vectors against host-generated reference vectors, use the `testvectors.py` script described in the automated testing section.

## Use scripts to automate testing and benchmarking

pqm4 includes Python scripts that automate flashing, running, and checking results across multiple implementations.

Before running any Python scripts in this section, make sure your virtual environment is active:

```bash
source venv/bin/activate
```

### Run functional tests

The `test.py` script runs the test binary on your chosen platform and checks correctness automatically.

#### NUCLEO-L476RG

Run functional tests on NUCLEO-L476RG:

```bash
python3 test.py -p nucleo-l476rg --uart /dev/tty.usbmodemXXXX ml-kem-768
```

#### QEMU

Run functional tests on QEMU:

```bash
python3 test.py -p mps2-an386 ml-kem-768
```

The output after running functional tests is similar to:

```output
ml-kem-768 - m4fspeed SUCCESSFUL
ml-kem-768 - m4fstack SUCCESSFUL
ml-kem-768 - clean SUCCESSFUL
test: 100%|#############################################| 3/3 [00:12<00:00,  4.29s/it, ml-kem-768 - clean]
```

### Run test vectors

The `testvectors.py` script generates test vectors on your chosen platform and compares them with host-side results.

#### NUCLEO-L476RG

Run test vector validation on NUCLEO-L476RG:

```bash
python3 testvectors.py -p nucleo-l476rg --uart /dev/tty.usbmodemXXXX ml-kem-768
```

#### QEMU

Run test vector validation on QEMU:

```bash
python3 testvectors.py -p mps2-an386 ml-kem-768
```

The output after running test vector validation is similar to:

```output
ml-kem-768 - m4fspeed SUCCESSFUL
ml-kem-768 - m4fstack SUCCESSFUL
ml-kem-768 - clean SUCCESSFUL
test: 100%|#############################################| 3/3 [00:12<00:00,  4.29s/it, ml-kem-768 - clean]
```

### Run benchmarks

The `benchmarks.py` script runs speed and stack benchmarks and stores the results in a `benchmarks/` directory.

#### NUCLEO-L476RG

Run benchmarks on NUCLEO-L476RG:

```bash
python3 benchmarks.py -p nucleo-l476rg --uart /dev/tty.usbmodemXXXX ml-kem-768
```

#### QEMU

Run benchmarks on QEMU:

```bash
python3 benchmarks.py -p mps2-an386 ml-kem-768
```

The output of running benchmarks is similar to:

```output
speed:  33%|################              | 1/3 [00:20<00:40, 20.00s/it, ml-kem-768 - m4fspeed]
speed:  66%|###########################   | 2/3 [00:40<00:20, 20.00s/it, ml-kem-768 - m4fstack]
speed: 100%|##############################| 3/3 [01:00<00:00, 20.00s/it, ml-kem-768 - clean]
```

Results are saved to `benchmarks.csv`. The screenshot shows an example of the benchmark output:

![Screenshot of benchmarks.csv showing cycle counts and stack usage for ML-KEM-768 implementations including the m4fspeed, m4fstack, and clean variants#center](./benchmarks.png "Example benchmark results for ML-KEM-768")

## What you've accomplished and what's next

You've now run functional tests, measured cycle counts and stack usage, and validated test vectors for a post-quantum KEM on Arm Cortex-M4. You can apply the same steps to any scheme included in pqm4 by substituting the scheme name in the binary path or script arguments.

Next, you'll learn how to add a new cryptographic scheme or implementation to the pqm4 framework.
