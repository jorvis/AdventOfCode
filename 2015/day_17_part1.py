#!/usr/bin/env python3

import itertools

sizes = list()
target_limit = 150
orientation_count = 0

for line in open('day_17.data'):
    line = line.rstrip()
    sizes.append(int(line))

for i in range(0, len(sizes)):
    for combination in itertools.combinations(sizes, i):
        if sum(combination) == target_limit:
            orientation_count += 1

print("There appear to be {0} ways to fit the containers".format(orientation_count))
