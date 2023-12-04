#ifndef UDSP_RUNNING_STAT_H
#define UDSP_RUNNING_STAT_H

#include <math.h>

typedef struct running_stat {
    float mean;
    float m2;
    int n;
} running_stat;

void running_stat_init(running_stat* rs);
void running_stat_add(running_stat* rs, float x);
float running_stat_mean(running_stat* rs);
float running_stat_stddev(running_stat* rs);

#endif // UDSP_RUNNING_STAT_H