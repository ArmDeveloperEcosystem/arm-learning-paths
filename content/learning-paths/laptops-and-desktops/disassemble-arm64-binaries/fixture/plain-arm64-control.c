__attribute__((noinline))
int arm64_plain_add(int left, int right) {
    return left + right;
}

int main(void) {
    return arm64_plain_add(1, 2) == 3 ? 0 : 1;
}
