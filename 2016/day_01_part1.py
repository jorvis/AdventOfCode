#!/usr/bin/env python3

"""
My approach was to treat this like a street grid, tracking which direction
you have faced and the net forward/backward steps in that direction to
yield the final position.

"""

# Let's start with our coordinate position on the street grid
position = {'x':0, 'y':0}

# every step involves a turn first, so this just toggles
current_axis = 'y'

# will steps be forward or backward on the axis?  (+ or -) ?
direction = 1

steps = open('day_01.data').read().rstrip().split(', ')

for entry in steps:
    step_dir = entry[0]
    step_count = int(entry[1:])

    # this just toggles every time
    if current_axis == 'y':
        current_axis = 'x'

        if direction == 1:
            if step_dir == 'R':
                direction = 1
            else:
                direction = -1
        else:
            if step_dir == 'R':
                direction = -1
            else:
                direction = 1
        
    else:
        current_axis = 'y'

        if direction == 1:
            if step_dir == 'R':
                direction = -1
            else:
                direction = 1
        else:
            if step_dir == 'R':
                direction = 1
            else:
                direction = -1

    position[current_axis] += (step_count * direction)

print("Final position: x:{0}, y:{1}".format(position['x'], position['y']))
print("Steps: {0}".format(abs(position['x']) + abs(position['y'])))
    
