#!/usr/bin/env python3

with open("day11_input") as fh:
    energy = [line.strip() for line in fh.readlines()]
energy = [[int(col) for col in list(row)] for row in energy]

xmin = 0
ymin = 0
xmax = len(energy)
ymax = len(energy[0])
total = xmax * ymax # total number of octopuses
part1 = 100 # number of steps for part 1

flashes  = 0 # cumulative number of flashes
step_flashes = 0 # number of flashes during one step
glow = [] # all octopuses that glow and still have to be propagated

step = 0 # step counter
while step_flashes != total: # stop when the goal of part 2 is achieved
    step_flashes = 0
    # increase energy level of each octopus by 1
    for y in range(ymax):
        for x in range(xmax):
            # 9 + 1: starts to flash, becomes 0
            # remember for propagation
            if energy[x][y] == 9:
                energy[x][y] = 0
                glow.append((x,y))
                step_flashes += 1
            # every other energy level is simply increased by 1
            else:
                energy[x][y] += 1

    # propagate to the adjacent 8 octopuses
    # keep doing it until all propagations have settled down
    while glow:
        # remove from the propagation list
        x,y = glow.pop()
        # increase the energy level of the adjacent octopuses
        for q in range(-1, 2):
            for p in range(-1, 2):
                xn = x+p
                yn = y+q
                # don't change the center element
                # stay within the bounds with xn, yn
                if (p, q) != (0, 0) and xmin <= xn < xmax and ymin <= yn < ymax:
                    if energy[xn][yn] == 9:
                        energy[xn][yn] = 0
                        glow.append((xn,yn))
                        step_flashes += 1
                    # don't increase when already flashing (=0)
                    elif energy[xn][yn] != 0:
                        energy[xn][yn] += 1

    step += 1
    flashes += step_flashes
    if step == part1:
        print(f"Part1: Number of flashes after {part1} steps: {flashes}")

print(f"Part 2: First step during which all octopuses flash: {step}")