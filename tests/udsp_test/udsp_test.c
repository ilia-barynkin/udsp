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
    float input[] = {1, 2, 3, 4, 5};
    float kernel[] = {1, 2, 3};
    float output[] = {0, 0, 0, 0, 0};
    conv(input, kernel, output, 5, 3);
    assert(output[0] == 11);
    assert(output[1] == 14);
    assert(output[2] == 17);
    assert(output[3] == 20);
    assert(output[4] == 23);
}

int main(int argc, char* argv[]) {
    mean_test();
    variance_test();
    conv_test();

    return 0;
}