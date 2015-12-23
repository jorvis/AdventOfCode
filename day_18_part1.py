#!/usr/bin/env python3

import copy

# the light grid
last_lg = list()

def neighbors_on(x,y):
    on_c = 0
    #print("DEBUG: Checking x:{0} y:{1} val:{2}".format(x,y,last_lg[x][y]))
    for i in [-1, 0, 1]:
        if x + i < 0: 
            #print("\tlast_lg[{0} + {1}][{2} + {3}] == {4}".format(x, i, y, None, 'out of bounds'))
            continue
        
        for j in [-1, 0, 1]:
            if y + j < 0:
                continue
            elif i == 0 and j == 0:
                #print("\tSkipping self, with value of {0}".format(last_lg[x + i][y + j]))
                continue
            else:
                try:
                    #print("\tlast_lg[{0} + {1}][{2} + {3}] == {4}".format(x, i, y, j, last_lg[x + i][y + j]))
                    if last_lg[x + i][y + j] == '#':
                        on_c += 1
                except IndexError:
                    #print("\tlast_lg[{0} + {1}][{2} + {3}] == {4}".format(x, i, y, j, 'out of bounds'))
                    pass

    #print("DEBUG: Count of position x:{0}, y:{1} is {2}".format(x,y,on_c))
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



