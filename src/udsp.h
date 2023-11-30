#ifndef UDSP_H
#define UDSP_H

#include "math.h"

float mean(const float* sample, int len);
float stddev(const float* sample, int len);
float variance(const float* sample, int len);

#endif