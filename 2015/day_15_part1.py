#!/usr/bin/env python3

import re

ingredients = list()
ingredient_limit = 100
best_score = 0

def try_ingredients(counts):
    global best_score
    
    idx = 0
    properties = {'cap':0, 'dur':0, 'fla':0, 'tex':0}
    for i in counts:
        for k in properties:
            properties[k] += ingredients[idx][k] * i
        idx += 1

    # Any negative values cause it all to be 0
    score = 1
    for k in properties:
        if properties[k] < 0:
            return
        else:
            score *= properties[k]

    #print("\tProperties: {0}".format(properties))
            
    if score > best_score:
        best_score = score

def build_matrix(path):
    current_sum = sum(path)
    remainder = ingredient_limit - current_sum

    # if this is the last slot, just assign the remaining value
    if len(path) == len(ingredients) - 1:
        print("Trying path: {0}".format(path + [remainder]))
        # now calculate the cookie score
        try_ingredients(path + [remainder])
    else:
        # otherwise, try every value remaining
        for i in range(0, remainder + 1):
            build_matrix(path + [i])

for line in open('day_15.data'):
    line = line.rstrip()
    m = re.match("(\S+): capacity ([\-0-9]+), durability ([\-0-9]+), flavor ([\-0-9]+), texture ([\-0-9]+), calories ([\-0-9]+)", line)
    if m:
        name, cap, dur, fla, tex, cal = m.groups()
        ingredients.append({'cap':int(cap), 'dur':int(dur), 'fla':int(fla), 'tex':int(tex), 'cal':int(cal)})

for i in range(0, ingredient_limit + 1):
    build_matrix([i])

print("The best score for a cookie recipe is: {0}".format(best_score))
    

