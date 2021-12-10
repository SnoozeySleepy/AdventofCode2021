#!/usr/bin/env python3

# total fuel cost is the sum of all movements to the position p
# cost() models the fuel cost of an individual movement
def fuel(crabs, p, cost):
    return sum([cost(abs(p-x)) for x in crabs])

def cost1(n): # linear cost
    return n

def cost2(n): # arithemtic sum
    return n * (n+1) // 2

# this approach works with any cost function
if __name__ == "__main__":
    with open("day7_input") as fh:
        crabs = [int(x) for x in fh.readline().strip().split(',')]

    def f(x):
        return fuel(crabs, x, cost1)
    def g(x):
        return fuel(crabs, x, cost2)

    # optimum lies between min and max positions of all crabs
    # taking advantage of min() to provide a function as key
    limits = range(min(crabs), max(crabs) +1)
    print(f"Part 1 fuel cost: {f(min(limits, key=f))}")
    print(f"Part 2 fuel cost: {g(min(limits, key=g))}")

    # Alternative
    part1 = min( [sum([abs(p-x) for x in crabs]) for p in range(min(crabs), max(crabs)+1)] )
    print(f"Part1 fuel cost: {part1}")

    part2 = min( [sum([cost2(abs(p-x)) for x in crabs]) for p in range(min(crabs), max(crabs)+1)] )
    print(f"Part2 fuel cost: {part2}")
