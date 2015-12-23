#!/usr/bin/env python3

import hashlib

input = 'iwrupvqb'
i = 0

while True:
    key = "{0}{1}".format(input, i)
    digest = hashlib.md5(key.encode('utf-8')).hexdigest()
    first_five = digest[0:6]

    if first_five == '000000':    
        print("i:{2}\tkey:{3}\t{0}\t{1}".format(digest, first_five, i, key))
        break

    i += 1
