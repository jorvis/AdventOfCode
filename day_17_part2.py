#!/usr/bin/env python3

import itertools

sizes = list()
target_limit = 150

for line in open('day_17.data'):
    line = line.rstrip()
    sizes.append(int(line))

min_c_count = 1000000
count_variants = dict()
    
for i in range(0, len(sizes)):
    for combination in itertools.combinations(sizes, i):
        if sum(combination) == target_limit:
            container_c = len(combination)
            if container_c < min_c_count:
                min_c_count = container_c
                
            if container_c not in count_variants:
                count_variants[container_c] = 1
            else:
                count_variants[container_c] += 1
                
print("The minimum number of containers required is: {0}".format(min_c_count))
print("There were {0} different arrangements with {1} containers".format(count_variants[min_c_count], min_c_count))
