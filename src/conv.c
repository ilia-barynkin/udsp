#include "conv.h"

void conv(float* input, float* kernel, float* output, int input_size, int kernel_size) {
    int output_size = input_size - kernel_size + 1;
    
    for (int i = 0; i < output_size; i++) {
        output[i] = 0;
        for (int j = 0; j < kernel_size; j++) {
            output[i] += input[i + j] * kernel[j];
        }
    }
}