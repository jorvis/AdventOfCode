#!/usr/bin/env python3

def paper_needs(l, w, h):
    area = (2*l*w) + (2*w*h) + (2*h*l)
    return area

def slack(l, w, h):
    sides = sorted([l, w, h])
    return sides[0] * sides[1]

def ribbon_to_wrap(l, w, h):
    sides = sorted([l, w, h])
    return (sides[0]*2) + (sides[1]*2)

def ribbon_for_bow(l, w, h):
    sides = sorted([l, w, h])
    return l*w*h

print("The area of a 2x3x4 is: {0}".format(paper_needs(2,3,4)))
print("The slack needed is: {0}".format(slack(2,3,4)))
print("The ribbon length to wrap is: {0}".format(ribbon_to_wrap(2,3,4)))
print("The ribbon length for a bow : {0}".format(ribbon_for_bow(2,3,4)))

total_sq_footage = 0
total_ribbon_length = 0

for line in open('day_02.data'):
    cols = line.split('x')

    cols[0] = int(cols[0])
    cols[1] = int(cols[1])
    cols[2] = int(cols[2])
    
    sqft = paper_needs(cols[0], cols[1], cols[2]) + \
           slack(cols[0], cols[1], cols[2])
    total_sq_footage += sqft

    total_ribbon_length += ribbon_to_wrap(cols[0], cols[1], cols[2])
    total_ribbon_length += ribbon_for_bow(cols[0], cols[1], cols[2])

print("The total sq footage is: {0}".format(total_sq_footage))
print("Linear feet of ribbon needed: {0}".format(total_ribbon_length))
    


