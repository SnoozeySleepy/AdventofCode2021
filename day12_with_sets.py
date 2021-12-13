#!/usr/bin/env python3

from timeit import default_timer as timer
from collections import defaultdict, deque

# recursive depth first search
def dfs(caves, start, end, visited, part2):
    count = 0

    if start == end:
        return 1

    for cave in caves[start]:
        if cave.isupper(): # visit big caves indefinitely
            count += dfs(caves, cave, end, visited, part2)
        elif cave not in visited: # visit small caves only once
            count += dfs(caves, cave, end, visited | {cave}, part2)
        elif part2 and cave != "start": # subpath, like in part 1, small caves only once
            count += dfs(caves, cave, end, visited, False)
    
    return count

caves = defaultdict(set)

# read in the graph & create the adjacency lists
with open("day12_input") as fh:
    line = fh.readline()
    while line != '':
        v = line.strip().split('-')
        caves[v[0]].add(v[1])
        caves[v[1]].add(v[0])
        line = fh.readline()

start = timer()
result1 = dfs(caves, 'start', 'end', {'start'}, part2=False)
result2 = dfs(caves, 'start', 'end', {'start'}, part2=True)
end = timer()

print(f"Part 1: number of distinct paths: {result1}")
print(f"Part 2: number of distinct paths: {result2}")

print(f"Runtime = {(end - start) *1000}ms")