import numpy as np
from scipy.signal import convolve2d


def parse(fname):
    lines = open(fname).read().splitlines()

    def parse_line(line):
        return [0 if x == "." else 1 for x in line]

    return np.array([parse_line(line) for line in lines])


def part1(fname="input"):
    grid = parse(fname)
    neighbors = count_neighbors(grid)
    x, y = np.where(np.logical_and(neighbors < 4, grid == 1))
    return len(x)


def count_neighbors(grid):
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    result = convolve2d(grid, kernel, mode="same", boundary="fill", fillvalue=0)
    return result


def part2(fname="input"):
    grid = parse(fname)
    total = 0

    while True:
        neighbors = count_neighbors(grid)
        if not np.any(np.logical_and(neighbors < 4, grid == 1)):
            return total
        x, y = np.where(np.logical_and(neighbors < 4, grid == 1))
        total += len(x)
        grid[x, y] = 0


print(part1())
print(part2())
