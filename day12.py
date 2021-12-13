#!/usr/bin/env python3

from timeit import default_timer as timer

# print all found paths
def print_paths(paths):
    for i in sorted(paths):
        print(",".join(i))

# recursive depth first search
# enable part 2, one, and only one, small cave can be visited twice
def dfs(graph, start, end, path, part2):
    path.append(start)

    if start == end: # found a path to end
        return [path]
    if start not in graph or end not in graph: # stop if start or end don't exist
        return []

    paths = []
    for node in graph[start]:
        # part 1: large caves can be visited indefinitely, small caves only once
        # part2=True activates the condition for part 2
        if node.isupper(): # visit big caves indefinitely
            paths.extend(dfs(graph, node, end, path.copy(), part2))
        elif node not in path: # visit small caves only once
            paths.extend(dfs(graph, node, end, path.copy(), part2))
        # at this point the small cave (node) was visited once
        # create subpaths like in part 1
        elif part2 and node != "start": 
            paths.extend(dfs(graph, node, end, path.copy(), part2=False))
            
    return paths

caves = {}

# read in the graph & create the adjacency lists
with open("day12_input") as fh:
    line = fh.readline()
    while line != '':
        v = line.strip().split('-')
        if v[0] not in caves:
            caves[v[0]] = [v[1]]
        else:
            caves[v[0]].append(v[1])
        if v[1] not in caves:
            caves[v[1]] = [v[0]]
        else:
            caves[v[1]].append(v[0])
        line = fh.readline()

start = timer()
# problem statement only asked for the distinct paths count
# not the list of actual, distinct paths
# without this extra information, it could be accelerated
# by a factor of 2
paths1 = dfs(caves, 'start', 'end', path=[], part2=False)
paths2 = dfs(caves, 'start', 'end', path=[], part2=True)
end = timer()

print(f"Part 1: number of distinct paths: {len(paths1)}")
print(f"Part 2: number of distinct paths: {len(paths2)}")

print(f"Runtime = {(end - start) *1000}ms")

# print_paths(paths1)
# print_paths(paths2)