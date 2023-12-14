#include "filters.h"

float* lowpass_kernel(fc, fs) {
    
}

void lowpass(float* input, float* output, int len, float fc, float fs) {
    convolve(input, lowpass_kernel(fc, fs), output, len, 5);
}

void highpass(float* input, float* output, int len, float fc, float fs);