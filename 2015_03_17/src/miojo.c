#include <stdlib.h>
#include <math.h>
#include "miojo.h"

int _calc_time(int acc_small, int acc_big, int small, int big) {
  if (abs(acc_small - acc_big) == 3) {
    return acc_small < acc_big ? acc_big : acc_small;
  }

  if (acc_big >= 32767 || acc_small >= 32767) {
    return -1;
  }

  if (acc_small <= acc_big) {
    return _calc_time(acc_small + small, acc_big, small, big);
  } else {
    return _calc_time(acc_small, acc_big + big, small, big);
  }
}

int calc_time(int time1, int time2)
{
    int small = time1 < time2 ? time1 : time2;
    int big = time1 > time2 ? time1 : time2;
    return _calc_time(0, 0, small, big);
}
