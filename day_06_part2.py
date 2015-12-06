#!/usr/bin/env python3

import re

grid_size = 1000
plane = [[0 for i in range(0,grid_size)] for j in range(0,grid_size)]

for line in open('day_06.data'):
    m = re.match("(\D+) ([\d]+),([\d]+) through ([\d]+),([\d]+)", line)
    if m:
        action, xstart, ystart, xstop, ystop = m.groups()
    else:
        raise Exception("ERROR: unexpected line: {0}".format(line))
    
    for x in range(int(xstart), int(xstop) + 1):
        for y in range(int(ystart), int(ystop) + 1):
            if action == 'turn on':
                plane[x][y] += 1
            elif action == 'turn off':
                if plane[x][y] > 0:
                    plane[x][y] -= 1
                else:
                    plane[x][y] = 0
            elif action == 'toggle':
                plane[x][y] += 2

            else:
                raise Exception("ERROR: unexpected action: {0}".format(action))

total_brightness = 0
                        
for x in plane:
    for val in x:
        total_brightness += val

print("INFO: It appears that total brightness = {0}".format(total_brightness))
