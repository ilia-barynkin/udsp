#ifndef UDSP_CONV_H
#define UDSP_CONV_H

#include <math.h>
#include <complex.h>

void conv(float* input, float* kernel, float* output, int input_size, int kernel_size);

#endif // UDSP_CONV_H