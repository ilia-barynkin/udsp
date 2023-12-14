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

void conv_test() {
    float input[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    float kernel[] = {1, 2, 3};
    float output[] = {0, 0, 0, 0, 0, 0};

    convolve(input, kernel, output, 10, 3);

    printf("hello wrld");
}

int main(int argc, char* argv[]) {
    mean_test();
    variance_test();
    conv_test();

    return 0;
}