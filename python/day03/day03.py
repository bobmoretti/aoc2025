import numpy as np
from itertools import combinations


def parse(filename):
    lines = open(filename).read().splitlines()

    def parse_line(line):
        return [int(x) for x in line]

    return np.array([parse_line(line) for line in lines])


def pairwise_subsets(items):
    return np.array(list(combinations(items, 2)))


def joltages(items):
    subsets = pairwise_subsets(items)
    return subsets.T[0] * 10 + subsets.T[1]


def part1():
    banks = parse("input")

    # input is 100x200 so only 200 * (100 choose 2) steps; we can easily brute force
    return sum(max(joltages(bank)) for bank in banks)


def index_list_to_joltage(indices, bank):
    return int("".join(str(x) for x in bank[indices]))


def find_largest_joltage12s(bank, n=12):
    start = 0
    indices = []
    l = len(bank)
    for ii in range(n):
        slc = bank[start : l - n + ii + 1]
        start += np.argmax(slc)
        indices.append(start)
        start += 1
    return index_list_to_joltage(indices, bank)


def part2():
    banks = parse("input")
    return sum(find_largest_joltage12s(bank) for bank in banks)


print(part1())
print(part2())
