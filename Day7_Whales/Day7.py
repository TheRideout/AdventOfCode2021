from collections import Counter
from statistics import mean
from math import floor, ceil


def load_input(path):
    with open(path) as f:
        return [int(x) for x in f.readlines()[0].split(',')]


def constant_fuel(subs):
    fuel_use = {}
    for x in range(min(subs), max(subs)+1):
        fuel_use[x] = sum([abs(x-sub) for sub in subs])
    return min(fuel_use.values())


def median_fuel(subs):
    m = mean(subs)
    positions = Counter(subs)
    fuel_use = {}
    for x in range(floor(m), ceil(m) + 1):
        costs = {pos: sum(range(1, abs(x - pos) + 1)) for pos in positions.keys()}
        fuel_use[x] = sum([positions[k] * cost for k, cost in costs.items()])
    return min(fuel_use.values())


def main():
    subs = load_input('Input')
    print('Part 1: {v}'.format(v=constant_fuel(subs)))
    print('Part 2: {v}'.format(v=median_fuel(subs)))


if __name__ == '__main__':
    main()
