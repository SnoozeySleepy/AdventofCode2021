#!/usr/bin/env python3

with open("day9_input") as fh:
    lines = fh.readlines()

# read in the height map
hmap = [[int(y) for y in x.strip()] for x in lines]

# add 9's around the edges of the height map; simplifies further processing
# add 9 to the beginning and end of each row
for i in range(len(hmap)):
    hmap[i].append(9)
    hmap[i].insert(0, 9)

# add 9-rows to the top and bottom of the height map
nines = [9] * (len(hmap[0]))
hmap.append(nines)
hmap.insert(0, nines)

risksum = 0
for row in range(1, len(hmap)-1):
    for col in range(1, len(hmap[0])-1):
        # find the local minima
        if hmap[row][col] < min([hmap[row+1][col],hmap[row-1][col],
                                    hmap[row][col+1],hmap[row][col-1]]):
            risksum += hmap[row][col] + 1 # risk = height + 1

print(f"Part 1: Sum of the risk levels: {risksum}")

# recursive fill algorithm
# fill with 9s and count the filled-in 9s
def fill_hmap(row, col, c):
    if hmap[row][col] != 9:
        c += 1 # count the number of filled-in 9s
        hmap[row][col] = 9 # fill
        c = fill_hmap(row, col+1, c)
        c = fill_hmap(row, col-1, c)
        c = fill_hmap(row+1, col, c)
        c = fill_hmap(row-1, col, c)
    return c

basins = []
for row in range(1, len(hmap)-1):
    for col in range(1, len(hmap[0])-1):
        b = fill_hmap(row, col, 0)
        if b != 0: # size of the basin, only save non-zero
            basins.append(b)

basins.sort()
print(f"Part 2: 3 largest basins multiplied = {basins[-1] * basins[-2] * basins[-3]}")