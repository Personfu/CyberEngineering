#include <stdio.h>

int main(void) {
    unsigned observed = 0;
    for (unsigned i = 0; i < 3; ++i) {
        observed += 1;
    }
    printf("observed=%u\n", observed);
    return 0;
}
