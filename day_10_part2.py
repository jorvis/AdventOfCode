#!/usr/bin/env python3

input = '1113222113'
iterations = 50

for i in range(0,iterations):
    print("Iteration: {0}".format(i))

    new_input = ''
    last_c = None
    last_c_count = 0
    for c in input:
        if last_c is not None and c != last_c:
            new_input += "{0}{1}".format(last_c_count, last_c)
            last_c_count = 0

        last_c_count += 1
        last_c = c

    new_input += "{0}{1}".format(last_c_count, last_c)
    input = new_input

print("INFO: After {0} iterations, the length of the result is {1}".format(iterations, len(input)))
