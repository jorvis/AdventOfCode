#!/usr/bin/env python3

"""
This one is just the traveling salesman problem.  I don't think it's in the spirit
of the challenge to use existing code, and I haven't the time or expertise to quickly
implement an efficient solution that will scale.  So, brute force it is.
"""
distances = dict()
cities = list()
shortest_path = list()
shortest_dist = 10000000000
longest_path = list()
longest_dist = 0

def build_path(dist, path):
    global shortest_path, longest_path
    global shortest_dist, longest_dist

    if len(path) == len(distances):
        # see if this is the best one so far
        last_city = None
        path_dist = 0
        for city in path:
            if last_city is not None:
                path_dist += dist[last_city][city]
            last_city = city

        print("Analyzing path: ", end='')
        for c in path:
            print(c, end=',')
        print("  Distance = {0}".format(path_dist))
            
        if path_dist < shortest_dist:
            shortest_dist = path_dist
            shortest_path = path

        if path_dist > longest_dist:
            longest_dist = path_dist
            longest_path = path
    else:
        for city in cities:
            if city not in path:
                build_path(dist, path + [city])

                
for line in open('day_09.data'):
    line = line.rstrip()
    cols = line.split()

    city1 = cols[0]
    city2 = cols[2]
    distance = int(cols[4])

    if city1 not in distances:
        distances[city1] = dict()
        cities.append(city1)

    if city2 not in distances:
        distances[city2] = dict()
        cities.append(city2)

    distances[city1][city2] = distance
    distances[city2][city1] = distance

for city in cities:
    build_path(distances, [city])

print("Shortest path:", end='')
for c in shortest_path:
    print(c, end=', ')
print("\nDistance: {0}\n".format(shortest_dist))

print("Longest path:", end='')
for c in longest_path:
    print(c, end=', ')
print("\nDistance: {0}\n".format(longest_dist))
