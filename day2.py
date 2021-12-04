#!/usr/bin/env python3

print("Advent of Code 2021 - Day 2")

with open("day2_input") as fh:
    lines = fh.readlines()

m = [a.strip().split() for a in lines]

x, depth = 0, 0
for command,value in m:
    if command == "forward":
        x += int(value)
    elif command == "down":
        depth += int(value)
    elif command == "up":
        depth -= int(value)
        
print(f"x = {x}, depth = {depth}")
print(f"x * depth = {x * depth}")

# get all possible directions (forward, up, down)
# set(map(lambda d: d[0], m))
# cast string (2nd index) to integer: lambda d: int(d[1])
# get a list that matches one of the possible directions:
# filter(lambda d: d[0]==k, m)
# dictionary comprehension
h = { k: sum(map(lambda d: int(d[1]), filter(lambda d: d[0]==k, m))) for k in set(map(lambda d: d[0], m)) }
print(f"Another way: {h['forward'] * (h['down'] - h['up'])}")

# Part 2
aim = 0
x, depth = 0, 0
for command,value in m:
    if command == "forward":
        x += int(value)
        depth += aim * int(value)
    elif command == "down":
        aim += int(value)
    elif command == "up":
        aim -= int(value)

print(f"Part 2:")        
print(f"x = {x}, depth = {depth}")
print(f"x * depth = {x * depth}")
