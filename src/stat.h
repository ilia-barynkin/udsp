#ifndef UDSP_STAT_H
#define UDSP_STAT_H

#include <math.h>

float mean(const float* sample, int len);
float stddev(const float* sample, int len);
float variance(const float* sample, int len);

#endif // UDSP_STAT_H