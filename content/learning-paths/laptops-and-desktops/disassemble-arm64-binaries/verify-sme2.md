---
title: Disassemble and verify SME2
description: Use otool and llvm-objdump to check SME and SME2 instructions in the example binary, then test the filter on comparison binaries.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Encode and decode mnemonics and operands

Assemblers encode Arm Instruction Set Architecture (ISA) instruction mnemonics and operands into four-byte, 32-bit words. You can use a disassembler to decode those ISA words to recover the mnemonics and their operands.

Use the example program you created earlier to explore assembly and disassembly. When you wrote the source, you included this line:

```output
fmopa za0.s, p0/m, p0/m, z0.s, z1.s
```

The mnemonic is `fmopa`, and the following operands identify the ZA tile, predicate registers, and vector registers.

The assembler converts `fmopa` and its operands into the four bytes shown here:

```output
00 00 81 80 -> 0x80810000 -> fmopa za0.s, p0/m, p0/m, z0.s, z1.s
```

## Create a filter for SME and SME2 instructions

AWK is a command-line tool for processing text. This AWK script filters disassembly output by checking instruction names and operands. It recognizes the state-control, ZA access, matrix-operation, and SME2 predicate instructions used in this example.

Run the following command to create `strict-sme2.awk`:

```bash
cat > strict-sme2.awk <<'EOF'
function has_pn_operand(text, mnemonic, pattern) {
    pattern = "(^|[[:space:]])" mnemonic "[[:space:]]+" \
              "pn(8|9|1[0-5])(\\.[bhsd])?([[:space:],]|$)"
    return text ~ pattern
}

function is_strict_sme2(line, text) {
    text = tolower(line)

    if (text ~ /(^|[[:space:]])(smstart|smstop)([[:space:]]|$)/)
        return 1
    if (text ~ /(^|[[:space:]])msr[[:space:]]+svcr(sm|za|smza)([[:space:],]|$)/)
        return 1
    if (text ~ /(^|[[:space:]])(bfmopa|bfmops|fmopa|fmops|smopa|smops|umopa|umops)([[:space:]]|$)/ ||
        text ~ /(^|[[:space:]])(sumopa|sumops|usmopa|usmops|bmopa|bmops)([[:space:]]|$)/)
        return 1
    if (text ~ /(^|[[:space:]])fmla[[:space:]]+za([0-9]|\.)/)
        return 1
    if (text ~ /(^|[[:space:]])(ld1|st1)[bhwdq][[:space:]]+\{[[:space:]]*za/)
        return 1
    if (text ~ /(^|[[:space:]])zero[[:space:]]+\{[[:space:]]*za/)
        return 1
    if (has_pn_operand(text, "ptrue"))
        return 1
    if (has_pn_operand(text, "whilelt") &&
        text ~ /(^|[[:space:],])vlx(2|4)([[:space:],]|$)/)
        return 1

    return 0
}

is_strict_sme2($0) { print }
EOF
```

The filter accepts `ptrue` only when its first operand is `pn8` through `pn15`. It accepts `whilelt` only with that register range and a `vlx2` or `vlx4` operand. It rejects ordinary SVE forms such as `ptrue p0.s`.

{{% notice Filter scope %}}
This filter recognizes the instruction forms used in this example. It doesn't detect every SME or SME2 instruction. Check the instruction reference and test any additional matching rules against binaries with and without the instructions.
{{% /notice %}}

## Decode with `otool`

The `otool` command selects the arm64 slice and disassembles its main executable code section. Apply the filter to decoded text rather than scanning raw bytes or strings:

```bash
otool -tvV -arch arm64 "$BIN" | awk -f strict-sme2.awk
```

The output is similar to:

```output
0000000100000424  smstart
000000010000042c  ptrue  pn8.s
0000000100000430  whilelt  pn8.s, x0, x0, vlx2
0000000100000434  zero  {za}
0000000100000438  fmopa  za0.s, p0/m, p0/m, z0.s, z1.s
000000010000043c  smstop
```

Instruction addresses can change when you rebuild the program. When comparing disassembler output for the same binary, check that the addresses match.

## Cross-check with `llvm-objdump`

The `llvm-objdump` disassembler can show each instruction's four bytes. The `--mattr` option enables decoding of SME and SME2 instructions:

```bash
xcrun llvm-objdump -d --macho --arch=arm64 --mattr=+sme,+sme2 "$BIN" |
  awk -f strict-sme2.awk
```

The output is similar to:

```output
100000424:  7f 47 03 d5  smstart
10000042c:  10 78 a0 25  ptrue  pn8.s
100000430:  10 44 a0 25  whilelt  pn8.s, x0, x0, vlx2
100000434:  ff 00 08 c0  zero  {za}
100000438:  00 00 81 80  fmopa  za0.s, p0/m, p0/m, z0.s, z1.s
10000043c:  7f 46 03 d5  smstop
```

The tools display leading zeros differently, but the instruction addresses match. Compare the addresses, bytes, and decoded instructions:

| Instruction address | Executable bytes | Decoded instruction | Purpose |
| --- | --- | --- | --- |
| `0x100000424` | `7f 47 03 d5` | `smstart` | Enable streaming mode and ZA |
| `0x10000042c` | `10 78 a0 25` | `ptrue pn8.s` | Initialize an SME2 predicate-as-counter |
| `0x100000430` | `10 44 a0 25` | `whilelt pn8.s, x0, x0, vlx2` | Create an SME2 two-vector predicate |
| `0x100000434` | `ff 00 08 c0` | `zero {za}` | Clear ZA matrix storage |
| `0x100000438` | `00 00 81 80` | `fmopa za0.s, ...` | Update a ZA tile with an outer product |
| `0x10000043c` | `7f 46 03 d5` | `smstop` | Disable streaming mode and ZA |

Both disassemblers identify the same instructions in the same binary. This confirms their presence, but doesn't show whether they run.

## Inspect the complete function

Use the function's symbol to display all its instructions, from the label through the `ret` instruction:

```bash
otool -tvV -arch arm64 "$BIN" |
  sed -n '/_sme2_fixture_kernel:/,/ret/p'
```

The output is similar to:

```output
_sme2_fixture_kernel:
0000000100000424  smstart
0000000100000428  ptrue  p0.s
000000010000042c  ptrue  pn8.s
0000000100000430  whilelt  pn8.s, x0, x0, vlx2
0000000100000434  zero  {za}
0000000100000438  fmopa  za0.s, p0/m, p0/m, z0.s, z1.s
000000010000043c  smstop
0000000100000440  ret
```

The function contains setup instructions, matrix operations, and cleanup instructions. Their presence doesn't prove the application calls this function.

## Check the comparison binaries

Apply the same disassembler and filter to both comparison binaries:

```bash
for CONTROL in string-only-control plain-arm64-control; do
  printf '%s: ' "$CONTROL"
  HITS=$(otool -tvV -arch arm64 "$CONTROL" | awk -f strict-sme2.awk)
  if [ -n "$HITS" ]; then printf '%s\n' "$HITS"; else printf 'no strict hits\n'; fi
done
```

The expected output is:

```output
string-only-control: no strict hits
plain-arm64-control: no strict hits
```

The string-only comparison binary still contains the SME2-related string and symbol you found earlier. The filter finds no matching instructions because it checks disassembled code rather than strings or symbol names.

## What you've accomplished and what's next

You verified SME and SME2 instructions in the binary by examining their bytes, operands, addresses, and surrounding code. Next, you'll combine these checks in a reusable script and adapt the method to other instruction groups and binary formats.
