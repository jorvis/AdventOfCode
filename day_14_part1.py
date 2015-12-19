#!/usr/bin/env python3

import re

reindeer = dict()

for line in open('day_14.data'):
    line = line.rstrip()
    m = re.match("(\S+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)
    if m:
        name, velocity, vtime, rtime = m.groups()
        reindeer[name] = {'vel': int(velocity), 'vtime': int(vtime), 'rtime': int(rtime)}

## Travel Log
tl = dict()
target_time = 2503

winner = None
max_distance_traveled = 0

for name in reindeer:
    time_traveled = 0
    distance_traveled = 0

    while time_traveled < target_time:
        # first advance the travel, as long as it's not over
        for i in range(1, reindeer[name]['vtime'] + 1):
            time_traveled += 1
            distance_traveled += reindeer[name]['vel']
            if time_traveled == target_time: break

        # then advance the rest period
        time_traveled += reindeer[name]['rtime']

    tl[name] = distance_traveled
    print("Name:{0}, Distance:{1}".format(name, distance_traveled))
    if winner is None or distance_traveled > max_distance_traveled:
        winner = name
        max_distance_traveled = distance_traveled

print("The winner is {0} with a distance of {1} km traveled after {2}s".format(winner, max_distance_traveled, target_time))
