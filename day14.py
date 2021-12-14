#!/usr/bin/env python3

from collections import Counter

# simple apporach, generating all insertions; only viable for small number of steps
def insertion(template, rules, steps):
    template = template.copy()
    for step in range(steps):
        x = 0
        while True:
            template.insert(x + 1, rules[template[x] + template[x+1]] )
            x += 2
            if x + 1 >= len(template):
                break

    c = Counter(template).most_common()
    return c[0][1] - c[-1][1]


def insert_process(pair, rules, steps):
    # create a counter for each rules pair and set it to 0
    currentc = dict.fromkeys(rules.keys(), 0)
    # create a counter for the next step for each rules pair and set it to 0
    nextc = dict.fromkeys(rules.keys(), 0)
    # set up the pair for propagation
    currentc[pair] = 1

    for i in range(steps):
        # check each rules pair (node) and propagate if current counter > 0
        for node in rules.keys():
            if currentc[node] > 0:
                # propage to all successor nodes for the next step
                for succ in r[node]:
                    nextc[succ] += currentc[node]
        # next counter becomes current counter
        currentc = nextc
        # set the next counter to 0
        nextc = dict.fromkeys(rules.keys(), 0)

    # need to reduce the pairs to single elements: only the first element counts
    tally = dict()
    for node in currentc.keys():
        if node[0] not in tally.keys():
            tally[node[0]] = currentc[node]
        else:
            tally[node[0]] += currentc[node]

    return tally

def process_all(template, rules, steps):
    result = dict()
    # create all pairs
    for i in range(len(template) - 1):
        pair = "".join(template[i:i+2])
        counts = insert_process(pair, rules, steps)
        # sum up for all pairs
        for k,v in counts.items():
            if k in result:
                result[k] += v
            else:
                result[k] = v

    # correct for the last pair
    result[template[-1]] += 1
    
    final = sorted(result.items(), key=lambda x: x[1], reverse=True)
    # most - least common
    return final[0][1] - final[-1][1]


if __name__ == "__main__":
    rules = dict() # used for insertion()
    r = dict() # used for insert_process()

    with open("day14_input") as fh:
        for line in fh:
            t = line.strip().split(" -> ")
            if len(t) == 2:
                rules[t[0]] = t[1]
                r[t[0]] = [t[0][0]+t[1], t[1]+t[0][1]]
            elif t[0] != '':
                template = list(t[0])

    print(f"Part 1: Most - least common element count after 10 cycles: {insertion(template, rules, 10)}")
    # exponential growth: takes too long!
    #print(f"Part 2: Most - least common element count after 40 cycles: {insertion(template, rules, 40)}")
    print(f"Part 2: Most - least common element count after 40 cycles: {process_all(template, r, 40)}")
