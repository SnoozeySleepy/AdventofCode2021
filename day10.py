#!/usr/bin/env python3

with open("day10_input") as fh:
    nav = [line.strip() for line in fh.readlines()]

delimiter = {'(': ')', '[': ']', '{': '}', '<': '>'}
opening = delimiter.keys()
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
apoints= {')': 1, ']': 2, '}': 3, '>': 4}
score = 0
ascores = []

for n in nav:
    stack = []
    for c in n:
        if c in opening: # opening character
            stack.append(delimiter[c]) # add the matching closing character to the stack
        elif c == stack[-1]: # closing character matches the one on the stack
            stack.pop()
        else: # closing character does not match the one on the stack
            score += points[c]
            break # done with this line
    else:
        ascore = 0
        while stack: # incomplete line
            ascore = 5 * ascore + apoints[stack.pop()]
        ascores.append(ascore)

print(f"Part 1: Syntax error score: {score}")
ascores.sort()
print(f"Part 2: autocomplete score: {ascores[len(ascores)//2]}")
