#!/usr/bin/env python3

from collections import Counter

class Vent:
    def __init__(self, p1, p2):
        self.points = self.interpolate(p1, p2)
        self.orthogonal = p1[0] == p2[0] or p1[1] == p2[1]

    def print(self):
        print(self.points)

    def interpolate(self, p1, p2):
        if p1[0] == p2[0]:
            dx = 0
        elif p1[0] < p2[0]:
            dx = 1
        else:
            dx = -1

        if p1[1] == p2[1]:
            dy = 0
        elif p1[1] < p2[1]:
            dy = 1
        else:
            dy = -1
        
        if dx == 0 and dy == 0:
            raise ValueError(f"{p1} -> {p2} not a line!")

        if dx == 0:
            ry = range(p1[1], p2[1]+dy, dy)
            rx = [p1[0]] * len(ry)
        elif dy == 0:
            rx = range(p1[0], p2[0]+dx, dx)
            ry = [p1[1]] * len(rx)
        else:
            rx = range(p1[0], p2[0]+dx, dx)
            ry = range(p1[1], p2[1]+dy, dy)
        return list(zip(rx, ry))


class Floor:
    def __init__(self):
        self.vents = []

    def append(self, line):
        self.vents.append(line)

    def print(self):
        for l in self.vents:
            l.print()

    def count(self, orthogonal=False):
        v = []
        for l in self.vents:
            if  not (orthogonal and not l.orthogonal):
                v.extend(l.points)
        return len(list(filter(lambda x: x[1] > 1, Counter(v).most_common())))


if __name__ == "__main__":
    oceanfloor = Floor()

    with open("day5_input") as fh:
        line = fh.readline()
        while line != '':
            c = line.split()
            c1 = tuple([int(x) for x in c[0].split(',')])
            c2 = tuple([int(x) for x in c[-1].split(',')])
            oceanfloor.append(Vent(c1, c2))
            line = fh.readline()

    print(f"Part1: {oceanfloor.count(True)}")
    print(f"Part2: {oceanfloor.count(False)}")
