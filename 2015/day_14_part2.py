#!/usr/bin/env python3

import re

reindeer = dict()
steps = dict()
scores = dict()

for line in open('day_14.data'):
    line = line.rstrip()
    m = re.match("(\S+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)
    if m:
        name, velocity, vtime, rtime = m.groups()
        reindeer[name] = {'vel': int(velocity), 'vtime': int(vtime), 'rtime': int(rtime)}
        steps[name] = list()
        scores[name] = 0

target_time = 2503

for name in reindeer:
    time_traveled = 0
    distance_traveled = 0

    while time_traveled < target_time:
        # first advance the travel, as long as it's not over
        for i in range(1, reindeer[name]['vtime'] + 1):
            time_traveled += 1
            distance_traveled += reindeer[name]['vel']
            steps[name].append(distance_traveled)
            if time_traveled == target_time: break

        # then advance the rest period
        for i in range(1, reindeer[name]['rtime'] + 1):
            time_traveled += 1
            steps[name].append(distance_traveled)
            if time_traveled == target_time: break

for i in range(0, target_time):
    winner = None
    best_dist = 0
    
    for name in reindeer:
        if winner is None or steps[name][i] > best_dist:
            winner = name
            best_dist = steps[name][i]

    scores[winner] += 1

top_reindeer = max(scores.keys(), key=(lambda k: scores[k]))

    

print("The winner is {0} with {1} points after {2}s".format(top_reindeer, scores[top_reindeer], target_time))
