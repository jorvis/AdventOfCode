#!/usr/bin/env python3

import re

prox = dict()
people = list()

best_path = list()
best_score = 0

def build_path(dist, path):
    global best_path, best_score

    if len(path) == len(dist):
        ## see if this is the best arrangement so far
        last_person = None
        path_dist = 0
        for person in path:
            if last_person is not None:
                path_dist += dist[person][last_person]
                path_dist += dist[last_person][person]
            last_person = person

        ## Don't forget the last two in the circle
        path_dist += dist[path[0]][last_person]
        path_dist += dist[last_person][path[0]]

        print("Analyzing path: ", end='')
        for c in path:
            print(c, end=',')
        print("  Happiness = {0}".format(path_dist))

        if path_dist > best_score:
            best_score = path_dist
            best_path = path
        
    else:
        for person in people:
            if person not in path:
                build_path(dist, path + [person])

for line in open('day_13_part1.data'):
    line = line.rstrip()

    m = re.match("(\S+) would (\S+) (\d+) happiness units by sitting next to (\S+)\.", line)
    if m:
        name, action, units, friend = m.groups()
        if name not in prox:
            prox[name] = dict()
            people.append(name)

        if action == 'gain':
            prox[name][friend] = int(units)
        else:
            prox[name][friend] = 0 - int(units)

for person in people:
    build_path(prox, [person])

print("Seating order: ", end='')
for c in best_path:
    print(c, end=', ')
print("\nHappiness: {0}\n".format(best_score))
