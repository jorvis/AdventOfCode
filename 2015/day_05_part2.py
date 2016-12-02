#!/usr/bin/env python3

import re

def is_nice_string(s):
    # It contains a pair of any two letters that appears at least twice
    #  in the string without overlapping
    matches = re.findall(r"([a-zA-Z]{2}).*\1", s)
    if len(matches) == 0:
        return False

    # It contains at least one letter which repeats with exactly one letter
    # between them
    m = re.search(r"([a-zA-Z]).\1", s)
    if not m:
        return False
    
    return True

#############################################################

nice_count = 0

for line in open('day_05.data'):
    line = line.rstrip()
    if is_nice_string(line):
        nice_count += 1
        
print("INFO: {0} of the strings are nice".format(nice_count))
