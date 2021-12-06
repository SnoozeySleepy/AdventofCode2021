#!/usr/bin/env python3

from collections import Counter

class Vent:
    def __init__(self, p1, p2):
        self.points = self.interpolate(p1, p2)
        self.orthogonal = p1[0] == p2[0] or p1[1] == p2[1]

    # for debugging
    def print(self):
        print(self.points)

    # interpolate all intermediate points
    # assuming only orthogonal or 45 deg diagonal lines
    def interpolate(self, p1, p2):
        if p1[0] == p2[0]: # vertical line
            dx = 0
        elif p1[0] < p2[0]:
            dx = 1 
        else:
            dx = -1

        if p1[1] == p2[1]: # horizontal line
            dy = 0
        elif p1[1] < p2[1]:
            dy = 1
        else:
            dy = -1
        
        if dx == 0 and dy == 0: # two identical points, not a line
            raise ValueError(f"{p1} -> {p2} not a line!")

        if dx == 0: # vertical line
            ry = range(p1[1], p2[1]+dy, dy)
            rx = [p1[0]] * len(ry)
        elif dy == 0: # horizontal line
            rx = range(p1[0], p2[0]+dx, dx)
            ry = [p1[1]] * len(rx)
        else: # diagonal line, 45 deg assumed
            rx = range(p1[0], p2[0]+dx, dx)
            ry = range(p1[1], p2[1]+dy, dy)
        return list(zip(rx, ry))


class Floor:
    def __init__(self):
        self.vents = [] # all vents (= lines)

    def append(self, vent):
        self.vents.append(vent)

    # for debugging
    def print(self):
        for vent in self.vents:
            vent.print()

    # orthogonal = True: consider only orthogonal lines
    # return the number of non-overlapping points
    def count(self, orthogonal=False):
        v = []
        for vent in self.vents:
            if  not (orthogonal and not vent.orthogonal):
                v.extend(vent.points)
        return len(list(filter(lambda x: x[1] > 1, Counter(v).most_common())))


if __name__ == "__main__":
    oceanfloor = Floor()

    # Being reasonably robust: expect a tuple at the beginning and one at the end of the line
    # don't care what's between these two tuples
    with open("day5_input") as fh:
        line = fh.readline()
        while line != '':
            c = line.split()
            c1 = [int(x) for x in c[0].split(',')]
            c2 = [int(x) for x in c[-1].split(',')]
            oceanfloor.append(Vent(c1, c2))
            line = fh.readline()

    print(f"Part1: {oceanfloor.count(orthogonal=True)}")
    print(f"Part2: {oceanfloor.count()}")
