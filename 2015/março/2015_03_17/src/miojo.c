#include <stdlib.h>
#include <math.h>
#include <limits.h>
#include "miojo.h"


int safe_mult(x, y)
{
  if (x >= INT_MAX/y) {
    return -2;
  } else {
    return x * y;
  }
}

int _calc_time(int wanted, int acc_small, int acc_big, int small, int big) {
  if (abs(acc_small - acc_big) == wanted) {
    return acc_small < acc_big ? acc_big : acc_small;
  }

  int mult = safe_mult(big, small);
  if (mult == -2) {
    return mult;
  } else if (acc_big >= mult || acc_small >= mult) {
    return -1;
  }

  if (abs(acc_small - acc_big) < big && wanted > big || acc_small <= acc_big) {
    return _calc_time(wanted, acc_small + small, acc_big, small, big);
  } else {
    return _calc_time(wanted, acc_small, acc_big + big, small, big);
  }
}

int calc_time(int wanted, int time1, int time2)
{
    int small = time1 < time2 ? time1 : time2;
    int big = time1 > time2 ? time1 : time2;
    return _calc_time(wanted, 0, 0, small, big);
}
