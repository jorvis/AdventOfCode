#!/usr/bin/env python3

"""
This is a brute-force version which doesn't even complete on even ridiculous
servers I have available (1 TB RAM+)

I wouldn't try running it.
"""

import re
import copy

molecule = 'CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr'
transitions = dict()

for line in open('day_19.data'):
    line = line.rstrip()

    m = re.match("(\S+) \=\> (\S+)", line)
    if m:
        k = m.group(1)
        if k in transitions:
            transitions[k].append(m.group(2))
        else:
            transitions[k] = [m.group(2)]

possibilities = list()
possibilities.append('')
            
idx = 0
while idx < len(molecule):
    element = None
    
    if idx < len(molecule) - 1:
        # cheating here a bit, because I looked at my particular dataset
        if molecule[idx + 1] in 'abcdfghijklmnopqrstuvwxyz':
            element = molecule[idx] + molecule[idx + 1]
            idx += 1
        else:
            element = molecule[idx]
    else:
        element = molecule[idx]

    idx += 1

    print("INFO: element: {0}".format(element))
    new_seqs = list()
    if element in transitions:
        for product in transitions[element]:
            for seq in possibilities:
                new_seqs.append(seq + product)
    else:
        for i in range(0, len(possibilities)):
            new_seqs.append(possibilities[i] + element)

    possibilities = list(copy.copy(new_seqs))
    print("INFO: There are now {0} possibilities".format(len(possibilities)))
    #print("INFO: They are:")
    #for seq in possibilities:
    #    print("\t{0}".format(seq))


print("RESULT: There seemed to be {0} possibilites".format(len(possibilities)))
uniq = list(possibilities)
print("RESULT: Of these, {0} were unique".format(len(uniq)))
print(possibilities[0])
