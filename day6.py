#!/usr/bin/env python3

from collections import Counter

# don't track each individual lanternfish
# track only cohorts (= 9)
def shift(population, n):
    # index: day of the cycle (0..8)
    # variable: number of lanternfish in this day of the cycle
    c = Counter(population)
    p = [c[i] for i in range(9)]
    # n: iterations / days to simulate
    for i in range(n):
        p.append(p.pop(0)) # shift the whole population and add the new lanternfish
        p[6] += p[-1] # reenter 7 day cycle
    return sum(p) # total number of lanternfish after n days

if __name__ == "__main__":
    with open("day6_input") as fh:
        line = fh.readline().strip()
    population = [int(x) for x in line.split(',')]
    print(f"Part 1: Number of lanternfish: {shift(population,80)}")
    print(f"Part 2: Number of lanternfish: {shift(population,256)}")
