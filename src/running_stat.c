#include "running_stat.h"

void running_stat_init(running_stat* rs) {
    rs->mean = 0;
    rs->m2 = 0;
    rs->n = 0;
}

void running_stat_add(running_stat* rs, float x) {
    rs->n++;
    float delta = x - rs->mean;
    rs->mean += delta / rs->n;
    rs->m2 += delta * (x - rs->mean);
}

float running_stat_mean(running_stat* rs) {
    return rs->mean;
}

float running_stat_stddev(running_stat* rs) {
    return sqrt(rs->m2 / rs->n);
}