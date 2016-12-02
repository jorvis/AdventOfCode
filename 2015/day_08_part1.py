#!/usr/bin/env python3

actual_c = 0
eval_c = 0

for line in open('day_08.data'):
    line = line.rstrip()
    for i in line:
        actual_c += 1

    eval_c += len(eval(line))

print("Actual:{0} - Eval:{1} = {2}".format(actual_c, eval_c, (actual_c - eval_c)))


