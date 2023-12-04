#include "stat.h"

float mean(const float* sample, int len) {
    float sum = 0;
    for (int i = 0; i < len; i++) {
        sum += sample[i];
    }
    return sum / len;
}

float variance(const float* sample, int len) {
    float u = mean(sample, len);
    float sum = 0.f;
    for (int i = 0; i < len; i++) {
        sum += (sample[i] - u) * (sample[i] - u);
    }
    return sum / len;
}

float stddev(const float* sample, int len) {
    return sqrt(variance(sample, len));
}
