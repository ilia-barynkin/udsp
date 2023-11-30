#include "stdlib.h"
#include "stdio.h"
#include "assert.h"

#include "udsp.h"

void mean_test() {
    assert(mean((float[]){1, 2, 3, 4}, 4) == 2.5);
}

void variance_test() {
    assert(variance((float[]){1, 2, 3, 4}, 4) == 1.25f);
}

int main(int argc, char* argv[]) {
    mean_test();
    variance_test();

    return 0;
}