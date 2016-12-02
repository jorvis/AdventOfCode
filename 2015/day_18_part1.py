#!/usr/bin/env python3

import copy

# the light grid
last_lg = list()

def neighbors_on(x,y):
    on_c = 0
    for i in [-1, 0, 1]:
        if x + i < 0: continue
        
        for j in [-1, 0, 1]:
            if y + j < 0: continue
            elif i == 0 and j == 0: continue
            else:
                try:
                    if last_lg[x + i][y + j] == '#':
                        on_c += 1
                except IndexError:
                    pass

    return on_c

def animate():
    global last_lg
    lg = copy.deepcopy(last_lg)

    x = 0
    for row in last_lg:
        y = 0
        for xval in row:
            c = neighbors_on(x,y)
            
            if last_lg[x][y] == '#':
                if c in [2,3]:
                    lg[x][y] = '#'
                else:
                    lg[x][y] = '.'
            else:
                if c == 3:
                    lg[x][y] = '#'
                else:
                    lg[x][y] = '.'
            
            y += 1
        x += 1
    last_lg = lg

for line in open('day_18.data'):
    line = line.rstrip()
    last_lg.append(list(line))

for i in range(0, 100):
    animate()

on_count = 0
for row in last_lg:
    on_count += row.count('#')

print("Lights on: {0}".format(on_count))



