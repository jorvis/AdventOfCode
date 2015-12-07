#!/usr/bin/env python3

import re

class Wire():
    def __init__( self, id=None, signal=None, source=None ):
        self.id = id
        self.signal = signal
        self.source = source

wires = dict()
commands = list()

# this gets all the primary assignments, and pushes the rest to a process queue
for line in open('day_07.data'):
    line = line.rstrip()

    # 44430 -> b
    m = re.match("(\d+) -> ([a-z]+)", line)
    if m:
        signal, wire_id = m.groups()
        if wire_id not in wires:
            wires[wire_id] = Wire(id=wire_id, signal=int(signal))
            print("DEBUG: Created wire id:{0}".format(wire_id))
        continue

    commands.append(line)
    

new_queue = list()
iteration = 0
while len(commands) > 0:
    iteration += 1
    print("INFO: Starting iteration {0} with {1} commands".format(iteration, len(commands)))
    for cmd in commands:
        # NOT dq -> dr
        m = re.match("NOT ([a-z]+) -> ([a-z]+)", cmd)
        if m:
            src_id, dest_id = m.groups()
            if src_id in wires:
                wires[dest_id] = Wire(id=dest_id)
                wires[dest_id].signal = ~wires[src_id].signal
                #print("DEBUG: NOT value to wire id:{0} = {1}".format(dest_id, wires[dest_id].signal))
            else:
                new_queue.append(cmd)
            continue
        
        # x OR y -> e
        m = re.match("([a-z]+) OR ([a-z]+) -> ([a-z]+)", cmd)
        if m:
            w1, w2, dest = m.groups()
            if w1 in wires and w2 in wires:
                wires[dest] = Wire(id=dest, signal= (wires[w1].signal | wires[w2].signal))
                #print("DEBUG: OR: assigned {0} value of {1}".format(dest, wires[dest].signal))
            else:
                new_queue.append(cmd)
                
            continue

        # x AND y -> d
        m = re.match("([a-z]+) AND ([a-z]+) -> ([a-z]+)", cmd)
        if m:
            w1, w2, dest = m.groups()
            if w1 in wires and w2 in wires:
                wires[dest] = Wire(id=dest, signal= (wires[w1].signal & wires[w2].signal))
                #print("DEBUG: AND: assigned {0} value of {1}".format(dest, wires[dest].signal))
            else:
                new_queue.append(cmd)
            continue

        # 1 AND am -> an
        m = re.match("(\d+) AND ([a-z]+) -> ([a-z]+)", cmd)
        if m:
            val, w2, dest = m.groups()
            if w2 in wires:
                wires[dest] = Wire(id=dest, signal= (int(val) & wires[w2].signal))
                #print("DEBUG: AND: assigned {0} value of {1}".format(dest, wires[dest].signal))
            else:
                new_queue.append(cmd)
            continue
    
        # x LSHIFT 2 -> f
        m = re.match("([a-z]+) LSHIFT (\d+) -> ([a-z]+)", cmd)
        if m:
            w1, val, dest = m.groups()
            val = int(val)
            if w1 in wires:
                wires[dest] = Wire(id=dest, signal= (wires[w1].signal << int(val)))
                #print("DEBUG: LSHIFT: assigned {0} value of {1}".format(dest, wires[dest].signal))
            else:
                new_queue.append(cmd)
            continue

        # y RSHIFT 2 -> g
        m = re.match("([a-z]+) RSHIFT (\d+) -> ([a-z]+)", cmd)
        if m:
            w1, val, dest = m.groups()
            val = int(val)
            if w1 in wires:
                wires[dest] = Wire(id=dest, signal= (wires[w1].signal >> int(val)))
                #print("DEBUG: RSHIFT: assigned {0} value of {1}".format(dest, wires[dest].signal))
            else:
                new_queue.append(cmd)
            continue

        # lx -> a
        m = re.match("([a-z]+) -> ([a-z]+)", cmd)
        if m:
            src, dest = m.groups()
            if src in wires:
                wires[dest] = Wire(id=dest, signal=wires[src].signal)
                #print("DEBUG: DIRECT: assigned {0} value of {1}".format(dest, wires[dest].signal))
            else:
                new_queue.append(cmd)
            continue

        ## If we got this far, the command was unrecognized
        raise Exception("ERROR: unrecognized command: {0}".format(cmd))

    commands = new_queue
    new_queue = list()

print("DEBUG: unprocessed command count: {0}".format(len(commands)))
    
for wire_id in wires:
    if wires[wire_id].signal >= 0:
        print("{0}: {1}".format(wire_id, wires[wire_id].signal))
    else:
        print("{0}: {1}".format(wire_id, 65535 + wires[wire_id].signal + 1))

print("INFO: signal for wire A is {0}".format(wires['a'].signal))
