#!/usr/bin/env python3

from collections import Counter

# return True if all small caves in the path are only visited once
def unique(path):
    # remove all large caves and start from the path list
    p = filter(lambda x: x.islower() and x != 'start', path)
    c = Counter(p).most_common()
    if c: # check if small caves are only visited once
        return c[0][1] < 2
    return True

# recursive depth first search
# enable the special condition, one small cave can be visited twice, with part2=True
def dfs(graph, start, end, path, part2):
    path.append(start)
    if start == end: # found a path to end
        return [path]
    if start not in graph or end not in graph: # stop if start or end don't exist
        return []
    paths = []
    for node in graph[start]:
        # part 1: small caves cannot only be visited once, large caves indefinitely
        # part2=True activates the condition for part 2
        # keep searching for paths as long as it's a small cave, not start
        # and no other small caves have been visited more than once: unique check
        if not(node in path and node.islower()) or part2 and \
            (node.islower() and node != 'start' and unique(path)):
            paths.extend(dfs(graph, node, end, path.copy(), part2))
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

result = dfs(caves, 'start', 'end', path=[], part2=False)
print(f"Part 1: number of distinct paths: {len(result)}")
result = dfs(caves, 'start', 'end', path=[], part2=True)
print(f"Part 2: number of distinct paths: {len(result)}")
