#ifndef UDSP_FILTERS_H
#define UDSP_FILTERS_H

#include "convolve.h"

void lowpass(float* input, float* output, int len, float fc, float fs);
void highpass(float* input, float* output, int len, float fc, float fs);

#endif // UDSP_FILTERS_H