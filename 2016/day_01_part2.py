#!/usr/bin/env python3

"""
My approach was to treat this like a street grid, tracking which direction
you have faced and the net forward/backward steps in that direction to
yield the final position.

Part 2 adds the challenge of tracking where you've been so you know where
you first step at the same place twice.  The instructions actually say you
just work out where'd you go, not actually walk it, so you wouldn't visit
any position twice.  Ignoring that though and assuming it means if you did
walk all the paths.

"""

# Let's start with our coordinate position on the street grid
position = {'x':0, 'y':0}

# every step involves a turn first, so this just toggles
current_axis = 'y'

# will steps be forward or backward on the axis?  (+ or -) ?
direction = 1

steps = open('day_01.data').read().rstrip().split(', ')
#steps = ['R8', 'R4', 'R4', 'R8']
steps_taken = {"0:0":1}

first_position_visited = None

for entry in steps:
    print("Processing step: {0}".format(entry))
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

    # need to actually walk it and remember/check each position
    for i in range(1, step_count + 1):
        position[current_axis] += (1 * direction)
        pos_str = "{0}:{1}".format(position['x'], position['y'])

        if pos_str in steps_taken:
            if first_position_visited is None:
                first_position_visited = pos_str
        else:
            steps_taken[pos_str] = 1
        

print("First position visited twice: {0}".format(first_position_visited))

    
