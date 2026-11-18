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
