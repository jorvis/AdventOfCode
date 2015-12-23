#!/usr/bin/env python3

"""
Notes:
- quick string reversal: http://stackoverflow.com/questions/931092/reverse-a-string-in-python
- character incrementing: http://stackoverflow.com/questions/2156892/python-how-can-i-increment-a-char
"""

import re

def increment(pw):
    pw = list(pw[::-1])
    
    for i in range(0, len(pw)):
        if pw[i] == 'z': pw[i] = 'a'
        else:
            pw[i] = chr(ord(pw[i]) + 1)
            break

    return ''.join(pw[::-1])

def is_valid(pw):
    # Passwords must include one increasing straight of at least three letters, like
    #  abc, bcd, cde, and so on, up to xyz
    streak_found = None
    for i in range(0, len(pw) - 2):
        if ord(pw[i+1]) - ord(pw[i]) == 1 and ord(pw[i+2]) - ord(pw[i+1]) == 1:
            streak_found = pw[i] + pw[i+1] + pw[i+2]

    # Passwords may not contain the letters i, o, or l, as these letters can be mistaken
    #  for other characters and are therefore confusing.
    for letter in ['i', 'o', 'l']:
        if letter in pw:
            return False

    # Passwords must contain at least two pairs of letters, like aa, bb, or zz.
    pairs_found = re.findall(r"(.)\1", pw)
    if len(pairs_found) < 2:
        return False

    if streak_found is not None:
        print("Streak: {0}".format(streak_found))
        print("Pairs: {0}".format(pairs_found))
        return True
    else:
        return False

password = 'vzbxkghb'

# this is for part 2
password = 'vzbxxyzz'

while True:
    password = increment(password)
    if is_valid(password): break

print("New password: {0}".format(password))
