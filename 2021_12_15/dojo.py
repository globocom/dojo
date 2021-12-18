#!/usr/bin/env python3
from collections import defaultdict

raw_input = open("input.txt").read()
risk_map = [[int(c) for c in line] for line in raw_input.splitlines()]

current_cost = 0  # evaluating this level now
visited = {(0, 0)}  # store visited coords
cost_map = [[0] * len(risk_map[0]) for _ in risk_map]
x_max, y_max = len(cost_map[0]), len(cost_map)

next_positions = defaultdict(list)
next_positions[0] = [((0, 1), 0), ((1, 0), 0)]
while True:
    current_level = sorted(
        next_positions[current_cost], key=lambda p: risk_map[p[0][1]][p[0][0]]
    )  # check for lower risk coords first

    for pos, pos_cost in current_level:
        if pos in visited or pos_cost < current_cost:
            # already visited or
            # cannot reach this cell through that path
            continue
        visited.add(pos)
        new_cost = pos_cost + risk_map[pos[1]][pos[0]]
        cost_map[pos[1]][pos[0]] = new_cost
        for p in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            new_pos = (pos[0] + p[0], pos[1] + p[1])
            if (
                0 <= new_pos[0] < x_max
                and 0 <= new_pos[1] < y_max
                and new_pos not in visited
            ):
                next_positions[new_cost].append((new_pos, new_cost))

    current_cost += 1
    if max(next_positions.keys()) < current_cost:
        print("Solution to part 1:", cost_map[-1][-1])
        break
