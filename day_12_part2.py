#!/usr/bin/env python3

import json
import re

total_count = 0

def process_children(item):
    global total_count

    if isinstance(item, dict):
        # if a dict, see if any values are "red".  Ignore if they are
        for k in item:
            if item[k] == 'red':
                return

        # if we got this far, it wasn't
        for k in item:
            if isinstance(item[k], dict) or isinstance(item[k], list):
                process_children(item[k])
            else:
                try:
                    total_count += int(item[k])
                except:
                    pass

    elif isinstance(item, list):
        for k in item:
            if isinstance(k, dict) or isinstance(k, list):
                process_children(k)
            else:
                try:
                    total_count += int(k)
                except:
                    pass
    else:
        raise Exception("ERROR: Unhandled thing: {0}".format(item))

# have to pre-process the data because JSON parsers want the property name to be quoted
ofh = open('day_12.data.fixed', 'wt')
for line in open("day_12.data"):
    line = line.rstrip()
    m = re.match("(.*)([a-z])\:(.*)", line)
    if m:
        ofh.write("{0}\"{1}\":{2}\n".format(m.group(1), m.group(2), m.group(3)))
    else:
        ofh.write("{0}\n".format(line))
ofh.close()

js = json.load(open('day_12.data.fixed'))

## Now actually parse this data
process_children(js)

print("Total: {0}".format(total_count))



