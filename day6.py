#!/usr/bin/env python3

from collections import Counter

def shift(population, n):
    # index: day of the cycle (0..8)
    # variable: number of lanternfish in this day of the cycle
    p = [0] * 9
    for k,v in Counter(population).items():
        p[k] = v

    # n: iterations / days to simulate
    for i in range(n):
        q = p[1:] # shift whole popluation
        q.append(p[0]) # new lanternfish
        q[6] += p[0] # reenter 7 day cycle
        p = q
    return sum(p) # total number of lanternfish after n days

if __name__ == "__main__":
    with open("day6_input") as fh:
        line = fh.readline().strip()
    population = [int(x) for x in line.split(',')]
    print(f"Part 1: Number of lanternfish: {shift(population,80)}")
    print(f"Part 2: Number of lanternfish: {shift(population,256)}")
