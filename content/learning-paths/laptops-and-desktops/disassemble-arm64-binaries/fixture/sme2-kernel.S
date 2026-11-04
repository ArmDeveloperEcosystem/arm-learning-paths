.text
.p2align 2
.globl _sme2_fixture_kernel

_sme2_fixture_kernel:
    smstart
    ptrue p0.s
    ptrue pn8.s
    whilelt pn8.s, x0, x0, vlx2
    zero { za }
    fmopa za0.s, p0/m, p0/m, z0.s, z1.s
    smstop
    ret
