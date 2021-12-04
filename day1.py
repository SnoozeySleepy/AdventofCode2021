#!/usr/bin/env python3

def sliding_increase(m, window):
    increase = 0
    for i in range(len(m)-(window -1)):
        if sum(m[i:i+window]) < sum(m[i+1:i+1+window]):
            increase += 1
    return increase

def sl_inc(m, window):
    # since both windows are overlapping, it's sufficient to compare the first and last values
    return sum(m[i] > m[i-window] for i in range(window, len(m)))

print("Advent of Code 2021 - Day 1")

with open("day1_input") as fh:
    m = [int(x.strip()) for x in fh.readlines()]

# Part 1
print(f"Number of increases: {sliding_increase(m, 1)}")
print(f"Also works: { sum(a < b for a,b in zip(m, m[1:])) }")
print("Alternative: %d" % sum([1 for i,d in enumerate(m) if i>0 and d > m[i-1]]))

# Part 2
print(f"Number of increases (sliding window = 3): {sliding_increase(m, 3)}")

t = [sum(trio) for trio in zip(m, m[1:], m[2:])]
print(f"Also works: { sum(a < b for a,b in zip(t, t[1:])) }")
print(f"Optimized: {sum(a < b for a,b in zip(m, m[3:]))}")
