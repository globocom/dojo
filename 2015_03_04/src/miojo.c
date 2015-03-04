#include <stdlib.h>
#include <math.h>
#include "miojo.h"

int _calc_time(int acc_time, int small, int big) {
  if (abs(acc_time1 - acc_time2) == 3) {
    return big;
  } else {
    if (acc_time % small == 0) {
      return _calc_time(acc_time + small, small, big);
    } else {
      return _calc_time(acc_time + big, small, big);
    }
  }
  return -1;
}

int calc_time(int time1, int time2)
{
    int small = time1 < time2 ? time1 : time2;
    int big = time1 > time2 ? time1 : time2;
    return _calc_time(0, 0, small, big);
}
