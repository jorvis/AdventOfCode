#!/usr/bin/env python3

actual_c = 0
eval_c = 0
repr_c = 0

for line in open('day_08.data'):
    line = line.rstrip()
    for i in line:
        actual_c += 1

    eval_c += len(eval(line))
    repr_c += line.count('\\') + line.count('"') + 2
    #print("Actual:{0} Eval:{1} Repr:{2}".format(actual_c, eval_c, repr_c))

print("Actual:{0} - Eval:{1} = {2}".format(actual_c, eval_c, (actual_c - eval_c)))
print("Repr:{0}".format(repr_c))

