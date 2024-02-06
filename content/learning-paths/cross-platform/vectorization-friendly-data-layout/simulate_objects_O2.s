000000000000b20 <simulate_objects>:																	
 b20:   1e202018        fcmpe   s0, #0.0
 b24:   1e204014        fmov    s20, s0
 b28:   1e204030        fmov    s16, s1
 b2c:   5400010c        b.gt    b4c <simulate_objects+0x2c>
 b30:   52800004        mov     w4, #0x0                        // #0
 b34:   52800003        mov     w3, #0x0                        // #0
 b38:   52800002        mov     w2, #0x0                        // #0
 b3c:   90000001        adrp    x1, 0 <__abi_tag-0x278>
 b40:   52800020        mov     w0, #0x1                        // #1
 b44:   91318021        add     x1, x1, #0xc60
 b48:   17ffff02        b       750 <__printf_chk@plt>
 b4c:   91524c01        add     x1, x0, #0x493, lsl #12
 b50:   0f000413        movi    v19.2s, #0x0
 b54:   91002005        add     x5, x0, #0x8
 b58:   91382021        add     x1, x1, #0xe08
 b5c:   52800004        mov     w4, #0x0                        // #0
 b60:   52800003        mov     w3, #0x0                        // #0
 b64:   52800002        mov     w2, #0x0                        // #0
 b68:   1e349011        fmov    s17, #-1.000000000000000000e+01
 b6c:   1e249012        fmov    s18, #1.000000000000000000e+01
 b70:   aa0503e0        mov     x0, x5
 b74:   d503201f        nop
 b78:   2d400803        ldp     s3, s2, [x0]
 b7c:   2d421807        ldp     s7, s6, [x0, #16]
 b80:   2d410001        ldp     s1, s0, [x0, #8]
 b84:   2d431005        ldp     s5, s4, [x0, #24]
 b88:   1f070e03        fmadd   s3, s16, s7, s3
 b8c:   1f060a02        fmadd   s2, s16, s6, s2
 b90:   1f050601        fmadd   s1, s16, s5, s1
 b94:   1f040200        fmadd   s0, s16, s4, s0
 b98:   1e312070        fcmpe   s3, s17
 b9c:   2d000803        stp     s3, s2, [x0]
 ba0:   2d010001        stp     s1, s0, [x0, #8]
 ba4:   54000484        b.mi    c34 <simulate_objects+0x114>  // b.first
 ba8:   1e322070        fcmpe   s3, s18
 bac:   5400044c        b.gt    c34 <simulate_objects+0x114>
 bb0:   1e312050        fcmpe   s2, s17
 bb4:   54000384        b.mi    c24 <simulate_objects+0x104>  // b.first
 bb8:   1e322050        fcmpe   s2, s18
 bbc:   5400034c        b.gt    c24 <simulate_objects+0x104>
 bc0:   1e312030        fcmpe   s1, s17
 bc4:   54000284        b.mi    c14 <simulate_objects+0xf4>  // b.first
 bc8:   1e322030        fcmpe   s1, s18
 bcc:   5400024c        b.gt    c14 <simulate_objects+0xf4>
 bd0:   1e312010        fcmpe   s0, s17
 bd4:   540001a4        b.mi    c08 <simulate_objects+0xe8>  // b.first
 bd8:   1e322010        fcmpe   s0, s18
 bdc:   5400016c        b.gt    c08 <simulate_objects+0xe8>
 be0:   9100c000        add     x0, x0, #0x30
 be4:   eb01001f        cmp     x0, x1
 be8:   54fffc81        b.ne    b78 <simulate_objects+0x58>  // b.any
 bec:   1e302a73        fadd    s19, s19, s16
 bf0:   1e332290        fcmpe   s20, s19
 bf4:   54fffbec        b.gt    b70 <simulate_objects+0x50>
 bf8:   90000001        adrp    x1, 0 <__abi_tag-0x278>
 bfc:   52800020        mov     w0, #0x1                        // #1
 c00:   91318021        add     x1, x1, #0xc60
 c04:   17fffed3        b       750 <__printf_chk@plt>
 c08:   1e214084        fneg    s4, s4
 c0c:   bd001c04        str     s4, [x0, #28]
 c10:   17fffff4        b       be0 <simulate_objects+0xc0>
 c14:   1e2140a5        fneg    s5, s5
 c18:   11000484        add     w4, w4, #0x1
 c1c:   bd001805        str     s5, [x0, #24]
 c20:   17ffffec        b       bd0 <simulate_objects+0xb0>
 c24:   1e2140c6        fneg    s6, s6
 c28:   11000463        add     w3, w3, #0x1
 c2c:   bd001406        str     s6, [x0, #20]
 c30:   17ffffe4        b       bc0 <simulate_objects+0xa0>
 c34:   1e2140e7        fneg    s7, s7
 c38:   11000442        add     w2, w2, #0x1
 c3c:   bd001007        str     s7, [x0, #16]
 c40:   17ffffdc        b       bb0 <simulate_objects+0x90>