---
title: Disassemble and verify SME2
description: Cross-check SME/SME2 instruction bytes, operands, and static addresses with otool and llvm-objdump, then validate the checks against negative controls.
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Encode and decode mnemonics and operands

Assemblers encode Arm Instruction Set Architecture (ISA) instruction mnemonics and operands into four-byte, 32-bit words. You can use a disassembler to decode those ISA words to recover the mnemonics and their operands.

Use the true-positive fixture you created earlier as an example of assembly and disassembly. When you wrote the source, you included this line:

```output
fmopa za0.s, p0/m, p0/m, z0.s, z1.s
```

The mnemonic is `fmopa`, and the following operands identify the ZA tile, predicate registers, and vector registers.


When assembled, that mnemonic (za0.s) and operand (p0/m, p0/m, z0.s, z1.s) are converted to four bytes (in little endian format) as 00 00 81 80, which are also represented as 0x80810000 (in big endian format).  

```output
00 00 81 80 -> 0x80810000 -> fmopa za0.s, p0/m, p0/m, z0.s, z1.s
```


## Define a scoped SME/SME2 predicate

Run the following command to create `strict-sme2.awk`. The predicate recognizes the high-signal state-control, ZA access, matrix-operation, and SME2 predicate forms used in this Learning Path.

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

The predicate accepts `ptrue` only when its first operand is PN8 through PN15. It accepts `whilelt` only with that PN range and a `vlx2` or `vlx4` operand. It rejects ordinary SVE forms such as `ptrue p0.s`.

{{% notice Scoped predicate %}}
This predicate is deliberately scoped to the instruction families demonstrated here. It isn't a complete implementation of SME or SME2. Treat every future addition as an ISA-backed classification change with positive, negative, and string-only tests.
{{% /notice %}}

## Decode with otool

The `otool` command selects the arm64 slice and disassembles its main executable code section. Apply the predicate to decoded text rather than scanning raw bytes or strings:

```bash
otool -tvV -arch arm64 "$BIN" | awk -f strict-sme2.awk
```

The expected output is:

```output
0000000100000424  smstart
000000010000042c  ptrue  pn8.s
0000000100000430  whilelt  pn8.s, x0, x0, vlx2
0000000100000434  zero  {za}
0000000100000438  fmopa  za0.s, p0/m, p0/m, z0.s, z1.s
000000010000043c  smstop
```

Static PCs can shift when the source, compiler, linker, or options change. Within one artifact, use the numeric addresses to correlate both decoder views.

## Cross-check with llvm-objdump

LLVM's decoder can show each instruction's four bytes. The `--mattr` option enables the SME and SME2 decoding tables explicitly:

```bash
xcrun llvm-objdump -d --macho --arch=arm64 --mattr=+sme,+sme2 "$BIN" |
  awk -f strict-sme2.awk
```

The expected output is:

```output
100000424:  7f 47 03 d5  smstart
10000042c:  10 78 a0 25  ptrue  pn8.s
100000430:  10 44 a0 25  whilelt  pn8.s, x0, x0, vlx2
100000434:  ff 00 08 c0  zero  {za}
100000438:  00 00 81 80  fmopa  za0.s, p0/m, p0/m, z0.s, z1.s
10000043c:  7f 46 03 d5  smstop
```

The leading zeros differ between the display formats, but the numeric static PCs agree. The following correlation captures the direct static evidence:

| Static PC | Executable bytes | Decoded instruction | Role in the region |
| --- | --- | --- | --- |
| `0x100000424` | `7f 47 03 d5` | `smstart` | Enable streaming mode and ZA |
| `0x10000042c` | `10 78 a0 25` | `ptrue pn8.s` | Initialize an SME2 predicate-as-counter |
| `0x100000430` | `10 44 a0 25` | `whilelt pn8.s, x0, x0, vlx2` | Create an SME2 two-vector predicate |
| `0x100000434` | `ff 00 08 c0` | `zero {za}` | Clear ZA matrix storage |
| `0x100000438` | `00 00 81 80` | `fmopa za0.s, ...` | Update a ZA tile with an outer product |
| `0x10000043c` | `7f 46 03 d5` | `smstop` | Disable streaming mode and ZA |

Two decoders corroborate the meaning of the same bytes in the same artifact. They aren't two runtime measurements.

## Inspect the coherent code region

Use the symbol to display the complete small function from its label through its return:

```bash
otool -tvV -arch arm64 "$BIN" |
  sed -n '/_sme2_fixture_kernel:/,/ret/p'
```

The expected output is:

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

The nearby state setup, predicate operations, ZA initialization, matrix operation, and state teardown form a coherent SME/SME2 region. Region coherence strengthens attribution, but the function could still be unreachable or unselected at runtime.

## Run the controls

Apply the same decoder and predicate to both controls:

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

The string-only control still contains the SME2 hint and symbol you observed earlier. Its zero instruction hits confirm that the predicate scans decoded executable code rather than feature-related words.

## What you've accomplished and what's next

You verified SME/SME2 instructions in the binary by examining their bytes, operands, addresses, and surrounding code. Next, you'll combine these checks in a reusable script and adapt the method to other Arm extensions and binary formats.
