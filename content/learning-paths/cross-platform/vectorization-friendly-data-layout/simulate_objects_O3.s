0000000000000b20 <simulate_objects>:
     b20:       1e202018        fcmpe   s0, #0.0
     b24:       6dbb27e8        stp     d8, d9, [sp, #-80]!
     b28:       bd004fe0        str     s0, [sp, #76]
     b2c:       5400012c        b.gt    b50 <simulate_objects+0x30>
     b30:       6cc527e8        ldp     d8, d9, [sp], #80
     b34:       52800004        mov     w4, #0x0                        // #0
     b38:       52800003        mov     w3, #0x0                        // #0
     b3c:       52800002        mov     w2, #0x0                        // #0
     b40:       b0000001        adrp    x1, 1000 <simulate_objects+0x4e0>
     b44:       52800020        mov     w0, #0x1                        // #1
     b48:       91016021        add     x1, x1, #0x58
     b4c:       17ffff01        b       750 <__printf_chk@plt>
     b50:       91524c01        add     x1, x0, #0x493, lsl #12
     b54:       91524c05        add     x5, x0, #0x493, lsl #12
     b58:       4f05f487        fmov    v7.4s, #-1.000000000000000000e+01
     b5c:       91002009        add     x9, x0, #0x8
     b60:       4f01f490        fmov    v16.4s, #1.000000000000000000e+01
     b64:       b0000000        adrp    x0, 1000 <simulate_objects+0x4e0>
     b68:       1e20403c        fmov    s28, s1
     b6c:       0f00041f        movi    v31.2s, #0x0
     b70:       3dc0281b        ldr     q27, [x0, #160]
     b74:       b0000000        adrp    x0, 1000 <simulate_objects+0x4e0>
     b78:       4e040431        dup     v17.4s, v1.s[0]
     b7c:       91352021        add     x1, x1, #0xd48
     b80:       1e2040fd        fmov    s29, s7
     b84:       1e20421e        fmov    s30, s16
     b88:       3dc02c1a        ldr     q26, [x0, #176]
     b8c:       913000a5        add     x5, x5, #0xc00
     b90:       4f000436        movi    v22.4s, #0x1
     b94:       52800004        mov     w4, #0x0                        // #0
     b98:       52800003        mov     w3, #0x0                        // #0
     b9c:       52800002        mov     w2, #0x0                        // #0
     ba0:       6d012fea        stp     d10, d11, [sp, #16]
     ba4:       6d0237ec        stp     d12, d13, [sp, #32]
     ba8:       6d033fee        stp     d14, d15, [sp, #48]
     bac:       aa0903e0        mov     x0, x9
     bb0:       4f000417        movi    v23.4s, #0x0
     bb4:       4eb71ef8        mov     v24.16b, v23.16b
     bb8:       4e041c57        mov     v23.s[0], w2
     bbc:       4eb81f19        mov     v25.16b, v24.16b
     bc0:       4e0c1c77        mov     v23.s[1], w3
     bc4:       4e141c97        mov     v23.s[2], w4
     bc8:       ad41cc02        ldp     q2, q19, [x0, #48]
     bcc:       ad434800        ldp     q0, q18, [x0, #96]
     bd0:       ad405004        ldp     q4, q20, [x0]
     bd4:       ad44d405        ldp     q5, q21, [x0, #144]
     bd8:       91030000        add     x0, x0, #0xc0
     bdc:       4eb21e4b        mov     v11.16b, v18.16b
     be0:       4eb31e6a        mov     v10.16b, v19.16b
     be4:       4ea01c09        mov     v9.16b, v0.16b
     be8:       4ea01c0e        mov     v14.16b, v0.16b
     bec:       4ea51caf        mov     v15.16b, v5.16b
     bf0:       4e1b214a        tbl     v10.16b, {v10.16b, v11.16b}, v27.16b
     bf4:       4ea21c48        mov     v8.16b, v2.16b
     bf8:       4eb21e4c        mov     v12.16b, v18.16b
     bfc:       4eb51ead        mov     v13.16b, v21.16b
     c00:       4ea41c86        mov     v6.16b, v4.16b
     c04:       4eb41e8b        mov     v11.16b, v20.16b
     c08:       4e1a21c3        tbl     v3.16b, {v14.16b, v15.16b}, v26.16b
     c0c:       4e1b2101        tbl     v1.16b, {v8.16b, v9.16b}, v27.16b
     c10:       4e31ce40        fmla    v0.4s, v18.4s, v17.4s
     c14:       4e1a2189        tbl     v9.16b, {v12.16b, v13.16b}, v26.16b
     c18:       6e1c0446        mov     v6.s[3], v2.s[0]
     c1c:       6e1c066b        mov     v11.s[3], v19.s[0]
     c20:       4e31ce62        fmla    v2.4s, v19.4s, v17.4s
     c24:       4e31cea5        fmla    v5.4s, v21.4s, v17.4s
     c28:       3c9a0000        stur    q0, [x0, #-96]
     c2c:       4e31ce84        fmla    v4.4s, v20.4s, v17.4s
     c30:       4e2ace21        fmla    v1.4s, v17.4s, v10.4s
     c34:       3c970002        stur    q2, [x0, #-144]
     c38:       4e29ce23        fmla    v3.4s, v17.4s, v9.4s
     c3c:       3c9d0005        stur    q5, [x0, #-48]
     c40:       4e2bce26        fmla    v6.4s, v17.4s, v11.4s
     c44:       3c940004        stur    q4, [x0, #-192]
     c48:       6ea0e4ea        fcmgt   v10.4s, v7.4s, v0.4s
     c4c:       6eb0e400        fcmgt   v0.4s, v0.4s, v16.4s
     c50:       6ea2e4e9        fcmgt   v9.4s, v7.4s, v2.4s
     c54:       6ea5e4eb        fcmgt   v11.4s, v7.4s, v5.4s
     c58:       6ea4e4ec        fcmgt   v12.4s, v7.4s, v4.4s
     c5c:       6eb0e442        fcmgt   v2.4s, v2.4s, v16.4s
     c60:       6eb0e4a5        fcmgt   v5.4s, v5.4s, v16.4s
     c64:       6eb0e484        fcmgt   v4.4s, v4.4s, v16.4s
     c68:       6ea1e4ed        fcmgt   v13.4s, v7.4s, v1.4s
     c6c:       6ea3e4ee        fcmgt   v14.4s, v7.4s, v3.4s
     c70:       6ea6e4ef        fcmgt   v15.4s, v7.4s, v6.4s
     c74:       4ea01d40        orr     v0.16b, v10.16b, v0.16b
     c78:       6eb0e421        fcmgt   v1.4s, v1.4s, v16.4s
     c7c:       6eb0e463        fcmgt   v3.4s, v3.4s, v16.4s
     c80:       6eb0e4c6        fcmgt   v6.4s, v6.4s, v16.4s
     c84:       6ea0fa4a        fneg    v10.4s, v18.4s
     c88:       4ea21d22        orr     v2.16b, v9.16b, v2.16b
     c8c:       4ea51d65        orr     v5.16b, v11.16b, v5.16b
     c90:       4ea41d84        orr     v4.16b, v12.16b, v4.16b
     c94:       6ea0fa69        fneg    v9.4s, v19.4s
     c98:       6ea0faab        fneg    v11.4s, v21.4s
     c9c:       6ea0fa8c        fneg    v12.4s, v20.4s
     ca0:       6e721d40        bsl     v0.16b, v10.16b, v18.16b
     ca4:       4ea11da1        orr     v1.16b, v13.16b, v1.16b
     ca8:       4ea31dc3        orr     v3.16b, v14.16b, v3.16b
     cac:       4ea61de6        orr     v6.16b, v15.16b, v6.16b
     cb0:       6e731d22        bsl     v2.16b, v9.16b, v19.16b
     cb4:       3c9b0000        stur    q0, [x0, #-80]
     cb8:       6e751d65        bsl     v5.16b, v11.16b, v21.16b
     cbc:       6e741d84        bsl     v4.16b, v12.16b, v20.16b
     cc0:       4e361c21        and     v1.16b, v1.16b, v22.16b
     cc4:       3c980002        stur    q2, [x0, #-128]
     cc8:       4e361c63        and     v3.16b, v3.16b, v22.16b
     ccc:       3c9e0005        stur    q5, [x0, #-32]
     cd0:       4e361cc0        and     v0.16b, v6.16b, v22.16b
     cd4:       3c950004        stur    q4, [x0, #-176]
     cd8:       4ea18739        add     v25.4s, v25.4s, v1.4s
     cdc:       4ea38718        add     v24.4s, v24.4s, v3.4s
     ce0:       4ea086f7        add     v23.4s, v23.4s, v0.4s
     ce4:       eb00003f        cmp     x1, x0
     ce8:       54fff701        b.ne    bc8 <simulate_objects+0xa8>  // b.any
     cec:       5e1c0721        mov     s1, v25.s[3]
     cf0:       910540af        add     x15, x5, #0x150
     cf4:       5e14070f        mov     s15, v24.s[2]
     cf8:       910580b0        add     x16, x5, #0x160
     cfc:       5e1c06e0        mov     s0, v23.s[3]
     d00:       910540b1        add     x17, x5, #0x150
     d04:       5e0c06ec        mov     s12, v23.s[1]
     d08:       2d7f4de4        ldp     s4, s19, [x15, #-8]
     d0c:       0eaf8421        add     v1.2s, v1.2s, v15.2s
     d10:       0eb78400        add     v0.2s, v0.2s, v23.2s
     d14:       2d7f260a        ldp     s10, s9, [x16, #-8]
     d18:       1e260023        fmov    w3, s1
     d1c:       0eb98581        add     v1.2s, v12.2s, v25.2s
     d20:       5e1406eb        mov     s11, v23.s[2]
     d24:       5e0c072e        mov     s14, v25.s[1]
     d28:       1f0a1384        fmadd   s4, s28, s10, s4
     d2c:       2d401606        ldp     s6, s5, [x16]
     d30:       1e260002        fmov    w2, s0
     d34:       2d4001e3        ldp     s3, s0, [x15]
     d38:       1e260027        fmov    w7, s1
     d3c:       5e14072d        mov     s13, v25.s[2]
     d40:       1f094f93        fmadd   s19, s28, s9, s19
     d44:       0eae8561        add     v1.2s, v11.2s, v14.2s
     d48:       5e0c0712        mov     s18, v24.s[1]
     d4c:       1f060f83        fmadd   s3, s28, s6, s3
     d50:       5e1c0702        mov     s2, v24.s[3]
     d54:       1f050380        fmadd   s0, s28, s5, s0
     d58:       1e272090        fcmpe   s4, s7
     d5c:       0b070063        add     w3, w3, w7
     d60:       1e260026        fmov    w6, s1
     d64:       0eb285a8        add     v8.2s, v13.2s, v18.2s
     d68:       0eb88441        add     v1.2s, v2.2s, v24.2s
     d6c:       2d3f4e24        stp     s4, s19, [x17, #-8]
     d70:       1e260108        fmov    w8, s8
     d74:       1e260024        fmov    w4, s1
     d78:       2d000223        stp     s3, s0, [x17]
     d7c:       0b080042        add     w2, w2, w8
     d80:       0b060084        add     w4, w4, w6
     d84:       54001544        b.mi    102c <simulate_objects+0x50c>  // b.first
     d88:       1e302090        fcmpe   s4, s16
     d8c:       5400150c        b.gt    102c <simulate_objects+0x50c>
     d90:       1e3d2270        fcmpe   s19, s29
     d94:       54001444        b.mi    101c <simulate_objects+0x4fc>  // b.first
     d98:       1e3e2270        fcmpe   s19, s30
     d9c:       5400140c        b.gt    101c <simulate_objects+0x4fc>
     da0:       1e3d2070        fcmpe   s3, s29
     da4:       54001344        b.mi    100c <simulate_objects+0x4ec>  // b.first
     da8:       1e3e2070        fcmpe   s3, s30
     dac:       5400130c        b.gt    100c <simulate_objects+0x4ec>
     db0:       1e3d2010        fcmpe   s0, s29
     db4:       54001264        b.mi    1000 <simulate_objects+0x4e0>  // b.first
     db8:       1e3e2010        fcmpe   s0, s30
     dbc:       5400122c        b.gt    1000 <simulate_objects+0x4e0>
     dc0:       910600ac        add     x12, x5, #0x180
     dc4:       910640ad        add     x13, x5, #0x190
     dc8:       910600ae        add     x14, x5, #0x180
     dcc:       2d7f0983        ldp     s3, s2, [x12, #-8]
     dd0:       2d7f19a9        ldp     s9, s6, [x13, #-8]
     dd4:       2d400181        ldp     s1, s0, [x12]
     dd8:       2d4011a5        ldp     s5, s4, [x13]
     ddc:       1f090f83        fmadd   s3, s28, s9, s3
     de0:       1f060b82        fmadd   s2, s28, s6, s2
     de4:       1f050781        fmadd   s1, s28, s5, s1
     de8:       1f040380        fmadd   s0, s28, s4, s0
     dec:       1e3d2070        fcmpe   s3, s29
     df0:       2d3f09c3        stp     s3, s2, [x14, #-8]
     df4:       2d0001c1        stp     s1, s0, [x14]
     df8:       54000fc4        b.mi    ff0 <simulate_objects+0x4d0>  // b.first
     dfc:       1e3e2070        fcmpe   s3, s30
     e00:       54000f8c        b.gt    ff0 <simulate_objects+0x4d0>
     e04:       1e3d2050        fcmpe   s2, s29
     e08:       54000ec4        b.mi    fe0 <simulate_objects+0x4c0>  // b.first
     e0c:       1e3e2050        fcmpe   s2, s30
     e10:       54000e8c        b.gt    fe0 <simulate_objects+0x4c0>
     e14:       1e3d2030        fcmpe   s1, s29
     e18:       54000dc4        b.mi    fd0 <simulate_objects+0x4b0>  // b.first
     e1c:       1e3e2030        fcmpe   s1, s30
     e20:       54000d8c        b.gt    fd0 <simulate_objects+0x4b0>
     e24:       1e3d2010        fcmpe   s0, s29
     e28:       54000ce4        b.mi    fc4 <simulate_objects+0x4a4>  // b.first
     e2c:       1e3e2010        fcmpe   s0, s30
     e30:       54000cac        b.gt    fc4 <simulate_objects+0x4a4>
     e34:       9106c0a8        add     x8, x5, #0x1b0
     e38:       910700aa        add     x10, x5, #0x1c0
     e3c:       9106c0ab        add     x11, x5, #0x1b0
     e40:       2d7f0903        ldp     s3, s2, [x8, #-8]
     e44:       2d7f1949        ldp     s9, s6, [x10, #-8]
     e48:       2d400101        ldp     s1, s0, [x8]
     e4c:       2d401145        ldp     s5, s4, [x10]
     e50:       1f090f83        fmadd   s3, s28, s9, s3
     e54:       1f060b82        fmadd   s2, s28, s6, s2
     e58:       1f050781        fmadd   s1, s28, s5, s1
     e5c:       1f040380        fmadd   s0, s28, s4, s0
     e60:       1e3d2070        fcmpe   s3, s29
     e64:       2d3f0963        stp     s3, s2, [x11, #-8]
     e68:       2d000161        stp     s1, s0, [x11]
     e6c:       54000a44        b.mi    fb4 <simulate_objects+0x494>  // b.first
     e70:       1e3e2070        fcmpe   s3, s30
     e74:       54000a0c        b.gt    fb4 <simulate_objects+0x494>
     e78:       1e3d2050        fcmpe   s2, s29
     e7c:       54000944        b.mi    fa4 <simulate_objects+0x484>  // b.first
     e80:       1e3e2050        fcmpe   s2, s30
     e84:       5400090c        b.gt    fa4 <simulate_objects+0x484>
     e88:       1e3d2030        fcmpe   s1, s29
     e8c:       54000844        b.mi    f94 <simulate_objects+0x474>  // b.first
     e90:       1e3e2030        fcmpe   s1, s30
     e94:       5400080c        b.gt    f94 <simulate_objects+0x474>
     e98:       1e3d2010        fcmpe   s0, s29
     e9c:       54000764        b.mi    f88 <simulate_objects+0x468>  // b.first
     ea0:       1e3e2010        fcmpe   s0, s30
     ea4:       5400072c        b.gt    f88 <simulate_objects+0x468>
     ea8:       910780a0        add     x0, x5, #0x1e0
     eac:       9107c0a6        add     x6, x5, #0x1f0
     eb0:       910780a7        add     x7, x5, #0x1e0
     eb4:       2d7f0803        ldp     s3, s2, [x0, #-8]
     eb8:       2d7f14c9        ldp     s9, s5, [x6, #-8]
     ebc:       2d400001        ldp     s1, s0, [x0]
     ec0:       2d4010c6        ldp     s6, s4, [x6]
     ec4:       1f090f83        fmadd   s3, s28, s9, s3
     ec8:       1f050b82        fmadd   s2, s28, s5, s2
     ecc:       1f060781        fmadd   s1, s28, s6, s1
     ed0:       1f040380        fmadd   s0, s28, s4, s0
     ed4:       1e3d2070        fcmpe   s3, s29
     ed8:       2d3f08e3        stp     s3, s2, [x7, #-8]
     edc:       2d0000e1        stp     s1, s0, [x7]
     ee0:       540004c4        b.mi    f78 <simulate_objects+0x458>  // b.first
     ee4:       1e3e2070        fcmpe   s3, s30
     ee8:       5400048c        b.gt    f78 <simulate_objects+0x458>
     eec:       1e3d2050        fcmpe   s2, s29
     ef0:       540003c4        b.mi    f68 <simulate_objects+0x448>  // b.first
     ef4:       1e3e2050        fcmpe   s2, s30
     ef8:       5400038c        b.gt    f68 <simulate_objects+0x448>
     efc:       1e3d2030        fcmpe   s1, s29
     f00:       540002c4        b.mi    f58 <simulate_objects+0x438>  // b.first
     f04:       1e3e2030        fcmpe   s1, s30
     f08:       5400028c        b.gt    f58 <simulate_objects+0x438>
     f0c:       1e3d2010        fcmpe   s0, s29
     f10:       540001e4        b.mi    f4c <simulate_objects+0x42c>  // b.first
     f14:       1e3e2010        fcmpe   s0, s30
     f18:       540001ac        b.gt    f4c <simulate_objects+0x42c>
     f1c:       1e3c2bff        fadd    s31, s31, s28
     f20:       bd404fe0        ldr     s0, [sp, #76]
     f24:       1e3f2010        fcmpe   s0, s31
     f28:       54ffe42c        b.gt    bac <simulate_objects+0x8c>
     f2c:       6d412fea        ldp     d10, d11, [sp, #16]
     f30:       b0000001        adrp    x1, 1000 <simulate_objects+0x4e0>
     f34:       6d4237ec        ldp     d12, d13, [sp, #32]
     f38:       91016021        add     x1, x1, #0x58
     f3c:       6d433fee        ldp     d14, d15, [sp, #48]
     f40:       52800020        mov     w0, #0x1                        // #1
     f44:       6cc527e8        ldp     d8, d9, [sp], #80
     f48:       17fffe02        b       750 <__printf_chk@plt>
     f4c:       1e214084        fneg    s4, s4
     f50:       bd01f4a4        str     s4, [x5, #500]
     f54:       17fffff2        b       f1c <simulate_objects+0x3fc>
     f58:       1e2140c6        fneg    s6, s6
     f5c:       11000484        add     w4, w4, #0x1
     f60:       bd01f0a6        str     s6, [x5, #496]
     f64:       17ffffea        b       f0c <simulate_objects+0x3ec>
     f68:       1e2140a5        fneg    s5, s5
     f6c:       11000463        add     w3, w3, #0x1
     f70:       bd01eca5        str     s5, [x5, #492]
     f74:       17ffffe2        b       efc <simulate_objects+0x3dc>
     f78:       1e214129        fneg    s9, s9
     f7c:       11000442        add     w2, w2, #0x1
     f80:       bd01e8a9        str     s9, [x5, #488]
     f84:       17ffffda        b       eec <simulate_objects+0x3cc>
     f88:       1e214084        fneg    s4, s4
     f8c:       bd01c4a4        str     s4, [x5, #452]
     f90:       17ffffc6        b       ea8 <simulate_objects+0x388>
     f94:       1e2140a5        fneg    s5, s5
     f98:       11000484        add     w4, w4, #0x1
     f9c:       bd01c0a5        str     s5, [x5, #448]
     fa0:       17ffffbe        b       e98 <simulate_objects+0x378>
     fa4:       1e2140c6        fneg    s6, s6
     fa8:       11000463        add     w3, w3, #0x1
     fac:       bd01bca6        str     s6, [x5, #444]
     fb0:       17ffffb6        b       e88 <simulate_objects+0x368>
     fb4:       1e214129        fneg    s9, s9
     fb8:       11000442        add     w2, w2, #0x1
     fbc:       bd01b8a9        str     s9, [x5, #440]
     fc0:       17ffffae        b       e78 <simulate_objects+0x358>
     fc4:       1e214084        fneg    s4, s4
     fc8:       bd0194a4        str     s4, [x5, #404]
     fcc:       17ffff9a        b       e34 <simulate_objects+0x314>
     fd0:       1e2140a5        fneg    s5, s5
     fd4:       11000484        add     w4, w4, #0x1
     fd8:       bd0190a5        str     s5, [x5, #400]
     fdc:       17ffff92        b       e24 <simulate_objects+0x304>
     fe0:       1e2140c6        fneg    s6, s6
     fe4:       11000463        add     w3, w3, #0x1
     fe8:       bd018ca6        str     s6, [x5, #396]
     fec:       17ffff8a        b       e14 <simulate_objects+0x2f4>
     ff0:       1e214129        fneg    s9, s9
     ff4:       11000442        add     w2, w2, #0x1
     ff8:       bd0188a9        str     s9, [x5, #392]
     ffc:       17ffff82        b       e04 <simulate_objects+0x2e4>
    1000:       1e2140a5        fneg    s5, s5
    1004:       bd0164a5        str     s5, [x5, #356]
    1008:       17ffff6e        b       dc0 <simulate_objects+0x2a0>
    100c:       1e2140c6        fneg    s6, s6
    1010:       11000484        add     w4, w4, #0x1
    1014:       bd0160a6        str     s6, [x5, #352]
    1018:       17ffff66        b       db0 <simulate_objects+0x290>
    101c:       1e214129        fneg    s9, s9
    1020:       11000463        add     w3, w3, #0x1
    1024:       bd015ca9        str     s9, [x5, #348]
    1028:       17ffff5e        b       da0 <simulate_objects+0x280>
    102c:       1e21414a        fneg    s10, s10
    1030:       11000442        add     w2, w2, #0x1
    1034:       bd0158aa        str     s10, [x5, #344]
    1038:       17ffff56        b       d90 <simulate_objects+0x270>