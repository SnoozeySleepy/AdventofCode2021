#!/usr/bin/env python3

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
        # part 1: small caves can only be visited once, large caves indefinitely
        # part2=True activates the condition for part 2
        if not(node in path and node.islower()): # this covers part 1 and part 2
            paths.extend(dfs(graph, node, end, path.copy(), part2))
        # find additional paths for part 2
        elif (node in path and node.islower()) and part2 and node != "start":
            paths.extend(dfs(graph, node, end, path.copy(), False))
            
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
