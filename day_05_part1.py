#!/usr/bin/env python3

import re

def is_nice_string(s):
    # contains at three vowels
    vowel_count = 0
    for vowel in 'aeiou':
        vowel_count += s.count(vowel)

    if vowel_count < 3: return False

    m = re.search(r"([a-zA-Z])\1", s)
    if not m:
        return False

    bad_strings = ['ab', 'cd', 'pq', 'xy']

    for bs in bad_strings:
        if bs in s:
            return False

    return True

#############################################################

nice_count = 0

for line in open('day_05.data'):
    if is_nice_string(line):
        nice_count += 1

print("INFO: {0} of the strings are nice".format(nice_count))
