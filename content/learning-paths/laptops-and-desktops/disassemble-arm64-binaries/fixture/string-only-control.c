__attribute__((used))
static const char feature_hint[] = "hw.optional.arm.FEAT_SME2";

__attribute__((noinline, used))
void sme2_string_only_marker(void) {
    __asm__ volatile("" ::: "memory");
}

int main(void) {
    return feature_hint[0] == '\0';
}
