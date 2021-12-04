#!/usr/bin/env python3

from collections import Counter

print("Advent of Code 2021 - Day 3")

with open("day3_input") as fh:
    m = [a.strip() for a in fh.readlines()]

# Part 1
# most common element
gamma   = int("".join([Counter([x[i] for x in m]).most_common(1)[0][0] for i in range(len(m[0]))]) ,2)
# least common element
epsilon = int("".join([Counter([x[i] for x in m]).most_common()[-1][0] for i in range(len(m[0]))]), 2)
# alternative: 
# epsilon = 2**len(m[0])-1 - gamma
print(f"Power consumption of the submarine: {gamma * epsilon}")

# Part 2
# for oxygen: switch = True
# for co2: switch = False
def rating(gas, switch):
    i = 0
    while len(gas) > 1:
        freq = Counter([x[i] for x in gas]).most_common()
        if (freq[0][1] == freq[1][1]) == switch:
            # oxygen: case when frequencies match: use '1'; last one since sorted alphanumerically
            # co2: pick the least common, always the last one
            bit = freq[-1][0]
        else:
            # oxygen: pick the most common, always the first one
            # co2: case when frequencies match: use '0'; first one since sorted alphanumerically
            bit = freq[0][0]
        gas = list(filter(lambda x: x[i] == bit, gas))
        i += 1
    return int(gas[0], 2)

oxygen = rating(m, True)
co2 = rating(m, False)
print(f"Life support rating: {oxygen * co2}")
