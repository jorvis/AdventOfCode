#!/usr/bin/env python3

import re

sues = dict()

for line in open('day_16.data'):
    line = line.rstrip()
    m = re.match("Sue (\d+): (.+)", line)
    if m:
        sue_num, props = m.groups()
        sues[sue_num] = {'valid':True}
        for kv in props.split(", "):
            k, v = kv.split(": ")
            sues[sue_num][k] = int(v)
            
evidence = {'children':3, 'cats':7, 'samoyeds':2, 'pomeranians':3, 'akitas':0, 'vizslas':0,
            'goldfish':5, 'trees':3, 'cars':2, 'perfumes': 1}
    
for sue_num in sues:
    sue = sues[sue_num]
    for k in sue:
        if k != 'valid' and sue[k] != evidence[k]:
            sue['valid'] = False
            break

    if sue['valid'] == True:
        print("Valid Sue {1}: {0}".format(sue, sue_num))
        
