from typing import Iterable

# sieve
def primes(m: int) -> Iterable[int]:
    if m < 2:
        return []

    all_numbers = [1] * m
    all_numbers[0] = all_numbers[1] = 0

    for i in range(2, m):
        if all_numbers[i]:
            yield i
            for j in range(i, m, i):
                all_numbers[j] = 0

    # if m == 0:
    #     return []
    # if m == 2:
    #     return [2]

    # return [2,3,5,7,11]
