# DOJO

_2016-02-15_

## Desafio: [Hilbert's New Hotel](https://projecteuler.net/problem=359)

An infinite number of people (numbered 1, 2, 3, etc.) are lined up to get a room
at Hilbert's newest infinite hotel. The hotel contains an infinite number of
floors (numbered 1, 2, 3, etc.), and each floor contains an infinite number of
rooms (numbered 1, 2, 3, etc.).

Initially the hotel is empty. Hilbert declares a rule on how the nth person is
assigned a room: person n gets the first vacant room in the lowest numbered
floor satisfying either of the following:

* the floor is empty
* the floor is not empty, and if the latest person taking a room in that floor
  is person `m`, then `m + n` is a perfect square

<!-- sep -->

1. Person 1 gets room 1 in floor 1 since floor 1 is empty.
2. Person 2 does not get room 2 in floor 1 since 1 + 2 = 3 is not a perfect
   square.
3. Person 2 instead gets room 1 in floor 2 since floor 2 is empty.
4. Person 3 gets room 2 in floor 1 since 1 + 3 = 4 is a perfect square.

Eventually, every person in the line gets a room in the hotel.

Define `P(f, r)` to be `n` if person `n` occupies room `r` in floor `f`, and `0`
if no person occupies the room. Here are a few examples:

    P(1, 1) = 1
    P(1, 2) = 3
    P(2, 1) = 2
    P(10, 20) = 440
    P(25, 75) = 4863
    P(99, 100) = 19454

Find the sum of all `P(f, r)` for all positive `f` and `r` such that `f × r =
71328803586048` and give the last 8 digits as your answer (`40632119`).

## Additional info

Assigning rooms for 55 people:

 Floor \ Room |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10
:------------:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|---:
            1 |  1 |  3 |  6 | 10 | 15 | 21 | 28 | 36 | 45 | 55
            2 |  2 |  7 |  9 | 16 | 20 | 29 | 35 | 46 | 54 | 67
            3 |  4 |  5 | 11 | 14 | 22 | 27 | 37 | 44 | 56 | 65
            4 |  8 | 17 | 19 | 30 | 34 | 47 | 53 | 64 | 72 | 85
            5 | 12 | 13 | 23 | 26 | 38 | 43 | 57 | 64 | 80 | 89
            6 | 18 | 31 | 33 | 48 | 52 | 69 | 75 | 94 | 102| 123
            7 | 24 | 25 | 39 | 42 | 58 | 63 | 81 | 88 | 108| 117
            8 | 32 | 49 | 51 | 70 | 74 | 95 | 101| 124| 132| 157
            9 | 40 | 41 | 59 | 62 | 82 | 87 | 109| 116| 140| 149
           10 | 50 | 71 | 73 | 96 | 100| 125| 131| 158| 166| 195

Floor = 1:

P(1, r) = r * (r + 1) / 2

Floor in [2, 3]:

If floor + room is odd:
P(f, r) = P(1, r + 1) - 1

If floor + room is even:
P(f, r) = P(1, r + 1) + 1

Floor > 3:

If floor + room is odd:
P(f, r) = P(f - 2, r + 2) - 1

If floor + room is even:
P(f, r) = P(f - 2, r + 2) + 1
