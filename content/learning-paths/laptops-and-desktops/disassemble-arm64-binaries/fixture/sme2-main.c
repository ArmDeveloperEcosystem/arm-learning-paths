#include <stddef.h>

extern void sme2_fixture_kernel(void);

__attribute__((used))
static const char feature_hint[] = "hw.optional.arm.FEAT_SME2";

void (*volatile keep_sme2_kernel)(void) = sme2_fixture_kernel;

int main(void) {
    return keep_sme2_kernel == NULL || feature_hint[0] == '\0';
}
