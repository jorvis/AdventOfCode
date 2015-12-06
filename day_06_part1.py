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
                plane[x][y] = 1
            elif action == 'turn off':
                plane[x][y] = 0
            elif action == 'toggle':
                if plane[x][y] == 0:
                    plane[x][y] = 1
                else:
                    plane[x][y] = 0
            else:
                raise Exception("ERROR: unexpected action: {0}".format(action))

lights_on = 0
                        
for x in plane:
    for val in x:
        if val == 1:
            lights_on += 1

print("INFO: It appears that {0} lights are one".format(lights_on))
